// trig_methods_benchmark.cpp
//
// Five epsilon-correction strategies compared on the same 31-entry table.
// All methods: table lookup -> Q1 correction -> angle-addition -> quadrant reflect.
// Only the epsilon correction differs.
//
// Methods:
//   chord-geo   -- arc minus curvature slivers; cos from Pythagoras; no sqrt
//   horner      -- Horner-form Taylor; sequential dependency chain
//   half-angle  -- double-angle identities applied to eps/2 series; no sqrt
//   versin      -- versed-sine series; cos=1-v, sin=sqrt(v*(2-v)); one sqrt
//   kite        -- sagitta H=versin(eps/2); split alternating series (pos/neg
//                  sums independent); cos=1-2H(2-H); sin=2(1-H)sqrt(H(2-H))
//
// Build:
//   g++ -O3 -march=native -std=c++17 -o trig_methods_benchmark trig_methods_benchmark.cpp
#include <array>
#include <chrono>
#include <cmath>
#include <cstdio>

// ---------------------------------------------------------------------------
// Table -- 31 entries, 0° to 90° in steps of 3°
// ---------------------------------------------------------------------------
struct SC { double s, c; };
static std::array<SC, 31> TABLE;

static void build_table() {
    const double sq2 = std::sqrt(2.0);
    const double sq3 = std::sqrt(3.0);
    const double sq5 = std::sqrt(5.0);

    SC b18 = {(sq5 - 1.0) / 4.0              , std::sqrt(10.0 + 2.0*sq5) / 4.0};
    SC b30 = {0.5                            , sq3 / 2.0};
    SC b45 = {sq2 / 2.0                      , sq2 / 2.0};
    SC b60 = {sq3 / 2.0                      , 0.5};
    SC b72 = {std::sqrt(10.0 + 2.0*sq5) / 4.0, (sq5 - 1.0) / 4.0};

    double s15 = b45.s*b30.c - b45.c*b30.s;
    double c15 = b45.c*b30.c + b45.s*b30.s;
    double s3  = b18.s*c15   - b18.c*s15;
    double c3  = b18.c*c15   + b18.s*s15;

    TABLE[0]  = {0.0, 1.0};
    TABLE[1]  = {s3, c3};
    TABLE[30] = {1.0, 0.0};

    for (int i = 2; i <= 29; ++i) {
        int deg = i * 3;
        if      (deg == 18) TABLE[i] = b18;
        else if (deg == 30) TABLE[i] = b30;
        else if (deg == 45) TABLE[i] = b45;
        else if (deg == 60) TABLE[i] = b60;
        else if (deg == 72) TABLE[i] = b72;
        else                TABLE[i] = {TABLE[i-1].s*c3 + TABLE[i-1].c*s3,
                                        TABLE[i-1].c*c3 - TABLE[i-1].s*s3};
    }
}

// ---------------------------------------------------------------------------
// Nearest table index for deg in [0°, 90°]
// ---------------------------------------------------------------------------
static inline int nearest_idx(double deg) {
    int lo = static_cast<int>(deg / 3.0);
    if (lo > 29) lo = 29;
    return (deg - lo*3.0 <= (lo + 1)*3.0 - deg) ? lo : lo + 1;
}

// ---------------------------------------------------------------------------
// Q1 epsilon corrections
// ---------------------------------------------------------------------------
static inline SC sc_geo(double deg) {
    const int    idx = nearest_idx(deg);
    const double sa  = TABLE[idx].s,  ca  = TABLE[idx].c;
    const double eps = (deg - idx * 3.0) * (M_PI / 180.0);
    const double e2  = eps * eps,  e4 = e2 * e2;

    const double chord  = eps * (1.0 - e2/24.0 + e4/1920.0);
    const double cos_ep = 1.0 - chord * chord * 0.5;
    const double sin_ep = eps * (1.0 - e2/6.0  + e4/120.0);

    return {sa*cos_ep + ca*sin_ep,
            ca*cos_ep - sa*sin_ep};
}

// ---------------------------------------------------------------------------
static inline SC sc_horner(double deg) {
    const int    idx = nearest_idx(deg);
    const double sa  = TABLE[idx].s,  ca  = TABLE[idx].c;
    const double eps = (deg - idx * 3.0) * (M_PI / 180.0);
    const double e2  = eps * eps;

    const double cos_ep = 1.0 + e2*(-0.5 + e2*(1.0/24.0 + e2*(-1.0/720.0)));
    const double sin_ep = eps * (1.0 + e2*(-1.0/6.0 + e2*(1.0/120.0)));

    return {sa*cos_ep + ca*sin_ep,
            ca*cos_ep - sa*sin_ep};
}

// Half-angle method: derive cos(eps) and sin(eps) via double-angle identities.
// cos(eps) = 1 - 2*sin^2(eps/2)             -- exact identity, no correction
// sin(eps) = 2*sin(eps/2)*cos(eps/2)        -- exact identity, no correction
// Two corrections needed for sin(eps/2) and cos(eps/2) to reach machine epsilon.
static inline SC sc_halfangle(double deg) {
    const int    idx = nearest_idx(deg);
    const double sa  = TABLE[idx].s,  ca  = TABLE[idx].c;
    const double eps = (deg - idx * 3.0) * (M_PI / 180.0);
    const double h   = eps * 0.5;
    const double h2  = h * h;

    const double sin_h  = h  * (1.0 - h2 * (1.0/6.0 - h2 * (1.0/120.0)));
    const double cos_ep = 1.0 - 2.0 * sin_h * sin_h;
    const double cos_h  = 1.0 - h2 * (0.5 - h2 * (1.0/24.0));
    const double sin_ep = 2.0 * sin_h * cos_h;

    return {sa*cos_ep + ca*sin_ep, ca*cos_ep - sa*sin_ep};
}

// Versin method: the two-triangle geometric closure.
// Three points on/in the unit circle: O=(0,0), B=(1,0), A=(cos t, sin t).
// D = foot of perpendicular from A to x-axis.
// OD=cos, DB=versin=1-cos, AD=sin -- shared between triangles OAD and ADB.
// Pythagoras twice: sin^2 + cos^2 = 1 (OAD); sin^2 + versin^2 = chord^2 (ADB).
// Subtracting: chord^2 = 2*versin.  From OAD: sin = sqrt(versin*(2-versin)).
// cos(eps) = 1 - versin(eps);  sin(eps) = sqrt(versin * (2-versin)).
// Four terms of the versin series give sub-machine-epsilon truncation error.
static inline SC sc_versin(double deg) {
    const int    idx = nearest_idx(deg);
    const double sa  = TABLE[idx].s,  ca  = TABLE[idx].c;
    const double eps = (deg - idx * 3.0) * (M_PI / 180.0);
    const double e2  = eps * eps;

    const double v      = e2 * (0.5 + e2 * (-1.0/24.0 + e2 * (1.0/720.0 - e2/40320.0)));
    const double cos_ep = 1.0 - v;
    const double sin_ep = std::copysign(std::sqrt(v * (2.0 - v)), eps);

    return {sa*cos_ep + ca*sin_ep, ca*cos_ep - sa*sin_ep};
}

// Kite method: O, B, M (arc midpoint), A form a kite; long diagonal OM bisects
// chord BA at C.  H = versin(eps/2) = sagitta of the half-arc.
// cos(eps) = 1 - 2*H*(2-H)        exact double-angle identity once H is known
// sin(eps) = 2*(1-H)*sqrt(H*(2-H))  = 2*cos(eps/2)*sin(eps/2)
// H accumulated as two independent sums (alternating signs split apart) so
// pos and neg chains carry no inter-dependency; one subtraction closes them.
// Four terms of H give sub-machine-epsilon truncation on eps in [-1.5deg, 1.5deg].
static inline SC sc_kite(double deg) {
    const int    idx = nearest_idx(deg);
    const double sa  = TABLE[idx].s,  ca  = TABLE[idx].c;
    const double eps = (deg - idx * 3.0) * (M_PI / 180.0);
    const double e2  = eps * eps;
    const double e4  = e2 * e2;
    const double e6  = e4 * e2;
    const double e8  = e4 * e4;

    const double pos    = e2 * (1.0/8.0)   + e6 * (1.0/46080.0);
    const double neg    = e4 * (1.0/384.0) + e8 * (1.0/10321920.0);
    const double H      = pos - neg;
    const double t      = H * (2.0 - H);
    const double cos_ep = 1.0 - 2.0 * t;
    const double sin_ep = std::copysign(2.0 * (1.0 - H) * std::sqrt(t), eps);

    return {sa*cos_ep + ca*sin_ep, ca*cos_ep - sa*sin_ep};
}

// ---------------------------------------------------------------------------
// Full-circle dispatch via quadrant reflection
// ---------------------------------------------------------------------------
template<SC(*Q1)(double)>
static inline SC full(double degrees) {
    double d = std::fmod(degrees, 360.0);
    if (d < 0.0) d += 360.0;
    if (d <=  90.0) { SC r = Q1(d);         return r; }
    if (d <= 180.0) { SC r = Q1(180.0 - d); return { r.s, -r.c}; }
    if (d <= 270.0) { SC r = Q1(d - 180.0); return {-r.s, -r.c}; }
                    { SC r = Q1(360.0 - d); return {-r.s,  r.c}; }
}

// ---------------------------------------------------------------------------
// Accuracy -- 36 001 angles against <cmath>
// ---------------------------------------------------------------------------
template<SC(*Fn)(double)>
static void test_accuracy(const char* label) {
    double max_err = 0.0;
    for (int i = 0; i <= 36000; ++i) {
        double deg = i * 0.01;
        double rad = deg * (M_PI / 180.0);
        SC r = full<Fn>(deg);
        double e = std::fmax(std::fabs(r.s - std::sin(rad)),
                             std::fabs(r.c - std::cos(rad)));
        if (e > max_err) max_err = e;
    }
    std::printf("  %-12s  %.2e\n", label, max_err);
}

// ---------------------------------------------------------------------------
// Throughput benchmark
// ---------------------------------------------------------------------------
template<SC(*Fn)(double)>
static double bench(const char* label, int N) {
    static double angles[3601];
    for (int i = 0; i < 3601; ++i) angles[i] = i * (360.0 / 3600.0);

    double acc = 0.0;
    auto t0    = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < N; ++i) {
        SC r = Fn(angles[i % 3601]);
        acc += r.s + r.c;
    }
    auto t1     = std::chrono::high_resolution_clock::now();
    double ms   = std::chrono::duration<double, std::milli>(t1 - t0).count();
    double mops = N / ms / 1000.0;
    std::printf("  %-12s  %7.1f ms   %5.1f M ops/s  (acc %.4f)\n", label, ms, mops, acc);
    return ms;
}

// ---------------------------------------------------------------------------
int main() {
    build_table();

    std::printf("Accuracy (36 001 angles, 0.00deg to 360.00deg, vs <cmath>):\n");
    test_accuracy<sc_geo>       ("chord-geo");
    test_accuracy<sc_horner>    ("horner");
    test_accuracy<sc_halfangle> ("half-angle");
    test_accuracy<sc_versin>    ("versin");
    test_accuracy<sc_kite>      ("kite");

    const int N = 20'000'000;

    std::printf("\nThroughput (%d sin/cos pairs):\n", N);
    double ms_geo = bench<full<sc_geo>>       ("chord-geo",  N);
    double ms_hor = bench<full<sc_horner>>    ("horner",     N);
    double ms_ha  = bench<full<sc_halfangle>> ("half-angle", N);
    double ms_vs  = bench<full<sc_versin>>    ("versin",     N);
    double ms_kit = bench<full<sc_kite>>      ("kite",       N);

    double best = std::fmin(std::fmin(ms_geo, ms_hor), std::fmin(std::fmin(ms_ha, ms_vs), ms_kit));
    std::printf("\n  vs horner:  chord-geo %.2fx  half-angle %.2fx  versin %.2fx  kite %.2fx\n", ms_hor/ms_geo, ms_hor/ms_ha, ms_hor/ms_vs, ms_hor/ms_kit);
    std::printf("  fastest overall: %.2fx over horner\n", ms_hor/best);
    return 0;
}
