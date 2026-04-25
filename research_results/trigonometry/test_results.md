# Test Results -- Trigonometric Computation Methods
### Dirk J. Botha, April 2026

---

## What Was Tested

Five methods for computing sin/cos pairs were tested for accuracy and
speed. All five use the same 31-entry geometric lookup table and the
same angle addition step. The difference between them is entirely in
how the small residual angle $\varepsilon$ is handled.

**Source:** [`source_code/c++/trig_methods_benchmark.cpp`](source_code/c++/trig_methods_benchmark.cpp)

**Methods:**

| Method     | Approach                                                                        |
|------------|---------------------------------------------------------------------------------|
| Horner     | Standard polynomial (Horner form) -- the baseline                               |
| Chord-geo  | Chord length from arc minus curvature corrections; $\cos$ from Pythagoras       |
| Half-angle | $\sin(\varepsilon/2)$ first; $\cos(\varepsilon)$ from double-angle identity     |
| Versin     | Versine ($1 - \cos$) formulation -- avoids cancellation for small $\varepsilon$ |
| Kite       | Sagitta (versed sine) via kite geometry; $\cos$ and $\sin$ from sagitta         |

---

## A Note on Machine Precision

Double-precision floating point (IEEE 754) stores approximately 15--16
significant decimal digits. Machine epsilon -- the smallest $\varepsilon$
such that $1 + \varepsilon \neq 1$ -- is:

$$\varepsilon_{\text{machine}} \approx 2.22 \times 10^{-16}$$

The reference values used in the accuracy test come from `<cmath>` --
itself a floating-point implementation. Any error below
$\sim 10^{-16}$ is indistinguishable from the reference implementation's
own rounding. **An accuracy result below machine epsilon does not mean
the method is more accurate than exact -- it means the method and the
reference agree to within the limits of the number system.**

---

## Results -- CPU

Platform: Intel i5 (2018), compiled with
`g++ -O3 -march=native -std=c++17`.

### Accuracy

Tested over 36,001 angles ($0.00°$ to $360.00°$ in $0.01°$ steps),
compared against `<cmath>` double-precision `sin` / `cos`.

| Method     | Max error  | Notes                           |
|------------|------------|---------------------------------|
| Versin     | 7.77e-16   | Sub-machine-epsilon             |
| Kite       | 7.77e-16   | Sub-machine-epsilon             |
| Half-angle | 8.05e-16   | Sub-machine-epsilon             |
| Chord-geo  | 2.20e-15   | One order above machine epsilon |
| Horner     | 2.20e-15   | One order above machine epsilon |

Three of the five geometric methods reach sub-machine-epsilon accuracy.
Chord-geo and Horner land one order above machine epsilon -- identical
to each other.

### Speed

Tested over 20,000,000 sin/cos pairs.

| Method     | Speed         | vs Horner        |
|------------|---------------|------------------|
| Horner     | 55.9 M ops/s  | 1.00× (baseline) |
| Half-angle | 54.7 M ops/s  | 0.98×            |
| Chord-geo  | 52.6 M ops/s  | 0.94×            |
| Versin     | 49.7 M ops/s  | 0.89×            |
| Kite       | 48.9 M ops/s  | 0.87×            |

Horner is fastest on CPU. Half-angle is within 2% -- essentially tied.
The more precise methods (versin, kite) are 11--13% slower.

---

## Results -- GPU

Platform: NVIDIA Quadro P400, CUDA 12.0,
compiled with `nvcc -O3 -arch=sm_61 -std=c++17`.
20,000,000 sin/cos pairs, 512 blocks × 256 threads.

| Method    | Max error  | Speed          |
|-----------|------------|----------------|
| Chord-geo | 2.24e-15   | 119.3 M ops/s  |
| Horner    | 2.24e-15   | 216.2 M ops/s  |

Horner is 1.81× faster on GPU. On a GPU, threads hide latency by
switching between warps -- there is no out-of-order execution the way a
CPU has. Chord-geo has more arithmetic operations, and those operations
are exposed directly as cycles. The gap between methods is larger on GPU
than on CPU for this reason.

Both methods are faster in absolute terms on GPU than on CPU
(119--216 M ops/s vs 50--56 M ops/s), confirming the parallelism is
being used.

---

## What the Results Confirm

**1. The geometric framework computes at machine precision.**
Methods derived purely from geometry -- chord, curvature, Pythagoras,
sagitta -- reach the same accuracy as an optimised industry-standard
implementation. Three of them exceed it.

**2. No CPU speed claim.**
Horner is fastest on CPU and GPU. Half-angle is within 2% on CPU but
the gap widens on GPU. The structural advantages of the geometric
methods do not translate to speed on hardware optimised for polynomial
evaluation.

**3. Precision and derivation are independent of speed.**
The versin and kite methods are most precise. They know why their
correction terms are what they are -- sliver on the unit circle,
constant curvature, Pythagoras. The Horner polynomial does not. Both
arrive at equivalent or better answers. One of them understands the
geometry.

**4. The geometric derivation stands.**
The correction terms mean something: parabolic sliver on the unit
circle, $\kappa = 1$, Pythagoras. The Horner polynomial is a numerical
fit to the same curve. Same answer -- one road is geometric, one is
algebraic. Both are correct. The geometric road was always there.

---

- *Computational methods: [`computational_methods.md`](./computational_methods.md)*
- *Notation register: [`../notation.md`](../notation.md)*
