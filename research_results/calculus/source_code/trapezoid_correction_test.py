"""
Test: Trapezoid integration and curvature correction.

Claim under test (integration.md -- sections 2 through 5):
  The trapezoid sum is the exact geometric area of the chord-bounded region.
  The remaining error (chord-arc sliver) is proportional to Δx^3 per interval,
  determined by curvature. Curvature is a `:` ratio. The correction is exact
  and finite.

We test:
  1. Trapezoid sum error vs exact integral -- confirm O(Δx^3) per interval
  2. Curvature correction -- does it close the gap?
  3. Residual after correction -- how does it scale?
  4. Whether the correction is itself exact for polynomials

Functions tested: x^2, x^3, sin(x), x^4 (to find the boundary of exactness)

Run:
  python3 trapezoid_correction_test.py
"""

import math

# ---------------------------------------------------------------------------
# Test functions: (f, f'', exact_integral over [a, b], label)
# ---------------------------------------------------------------------------
def make_tests():
    a, b = 0.0, 1.0
    return [
        {
            "label": "f(x) = x^2",
            "f"    : lambda x: x**2,
            "f2"   : lambda x: 2.0,           # second derivative
            "exact": (b**3 - a**3) / 3,
            "a"    : a, "b": b,
        },
        {
            "label": "f(x) = x^3",
            "f"    : lambda x: x**3,
            "f2"   : lambda x: 6*x,
            "exact": (b**4 - a**4) / 4,
            "a"    : a, "b": b,
        },
        {
            "label": "f(x) = x^4",
            "f"    : lambda x: x**4,
            "f2"   : lambda x: 12*x**2,
            "exact": (b**5 - a**5) / 5,
            "a"    : a, "b": b,
        },
        {
            "label": "f(x) = sin(x) over [0, π]",
            "f"    : math.sin,
            "f2"   : lambda x: -math.sin(x),
            "exact": 2.0,
            "a"    : 0.0, "b": math.pi,
        },
    ]

# ---------------------------------------------------------------------------
# Integration methods
# ---------------------------------------------------------------------------
def trapezoid_sum(f, a, b, n):
    """Finite sum of trapezoid areas. No limit."""
    dx    = (b - a) / n
    total = 0.0
    for i in range(n):
        x1     = a + i * dx
        x2     = x1 + dx
        total += dx * (f(x1) + f(x2)) / 2.0   # (x2-x1)·(y1+y2) : 2
    return total

# ---------------------------------------------------------------------------
def curvature_correction(f2, a, b, n):
    """
    Correction term: area of chord-arc sliver per interval.

    For each interval the sliver area is (Δx^3/12)·f''(midpoint).
    This uses the curvature at the midpoint -- a `:` ratio.

    Sign: trapezoid overestimates for convex (f''>0), underestimates for
    concave (f''<0). Subtract the correction.
    """
    dx    = (b - a) / n
    total = 0.0
    for i in range(n):
        x_mid  = a + (i + 0.5) * dx
        total += (dx**3 / 12.0) * f2(x_mid)
    return total

# ---------------------------------------------------------------------------
def corrected_sum(f, f2, a, b, n):
    return trapezoid_sum(f, a, b, n) - curvature_correction(f2, a, b, n)

# ---------------------------------------------------------------------------
# Error scaling: confirm O(Δx^3) per interval for trapezoid,
#                        O(Δx^5) per interval after correction
# ---------------------------------------------------------------------------
def error_scaling(f, f2, exact, a, b):
    ns        = [4, 8, 16, 32, 64, 128]
    prev_trap = None
    prev_corr = None

    print(f"  {'n':>5}  {'trap error':>14}  {'ratio':>7}  {'corr error':>14}  {'ratio':>7}")

    for n in ns:
        trap_err   = abs(trapezoid_sum(f, a, b, n) - exact)
        corr_err   = abs(corrected_sum(f, f2, a, b, n) - exact)
        trap_ratio = f"{prev_trap/trap_err:.2f}" if prev_trap else "    -"
        corr_ratio = f"{prev_corr/corr_err:.2f}" if prev_corr else "    -"
        print(f"  {n:>5}  {trap_err:>14.2e}  {trap_ratio:>7}  {corr_err:>14.2e}  {corr_ratio:>7}")
        prev_trap = trap_err
        prev_corr = corr_err

# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
def run():
    print("=" * 70)
    print("TRAPEZOID INTEGRATION — CURVATURE CORRECTION TEST")
    print("=" * 70)
    print()
    print("Claim: trapezoid error is O(Δx^3) per interval.")
    print("       curvature correction reduces this to O(Δx^5) per interval.")
    print("       (doubling n should multiply trap error by ~4, corr error by ~16)")
    print()

    for test in make_tests():
        print(f"--- {test['label']} ---")
        print(f"    exact = {test['exact']:.15f}")
        print()
        error_scaling(test["f"], test["f2"], test["exact"], test["a"], test["b"])
        print()

        # spot-check with n=100
        n    = 100
        trap = trapezoid_sum(test["f"], test["a"], test["b"], n)
        corr = corrected_sum(test["f"], test["f2"], test["a"], test["b"], n)
        print(f"    n=100  trapezoid = {trap:.15f}  err = {abs(trap - test['exact']):.2e}")
        print(f"    n=100  corrected = {corr:.15f}  err = {abs(corr - test['exact']):.2e}")
        print()

    print("=" * 70)
    print("POLYNOMIAL EXACTNESS CHECK (n=1, single interval)")
    print("=" * 70)
    print()
    print("For polynomials ≤ degree 3, the correction should be exact (or")
    print("very close — limited only by floating point).")
    print()

    for test in make_tests():
        n    = 1
        trap = trapezoid_sum(test["f"], test["a"], test["b"], n)
        corr = corrected_sum(test["f"], test["f2"], test["a"], test["b"], n)
        print(f"  {test['label']:<25}  "
              f"trap err = {abs(trap - test['exact']):.2e}  "
              f"corr err = {abs(corr - test['exact']):.2e}")
    print()

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    run()
