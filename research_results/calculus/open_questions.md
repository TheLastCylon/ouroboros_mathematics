# Open Questions -- Integration
### Dirk J. Botha, April 2026

These are honest gaps. The results in `integration.md` stand independent
of what these questions yield. They are recorded here because they are
worth pursuing, not because anything already written depends on them.

---

## Q1 -- The quadrature hierarchy

**Status: OPEN**

The trapezoid plus one parabolic segment correction gives the three-point
rule (Simpson's rule) -- exact for polynomials of degree $\leq 3$.

The question is whether adding a second correction term gives Boole's
rule (exact for degree $\leq 5$), a third gives the next rule in the
sequence, and so on -- reproducing the full quadrature hierarchy as
successive geometric corrections.

If true, the standard quadrature rules are not independent constructions.
They are a single geometric sequence: each rule is the previous rule plus
the next curvature correction.

**What is known:** The first step (trapezoid -> Simpson) is confirmed
geometrically and computationally. The pattern is plausible. It has not
been derived beyond the first correction.

**What requires derivation:** The second correction term -- its geometric
shape, its formula in terms of function values, and whether the result
matches Boole's rule algebraically. If the sequence continues, the
further question is whether it converges to Gaussian quadrature or to
something geometrically distinct.

---

## Q2 -- The second correction term

**Status: OPEN**

The first correction is the parabolic segment -- the area between the
chord and the curve, computed from the midpoint function value. It
accounts for the first-order variation in curvature across the interval.

The second correction accounts for the variation in that variation -- the
rate at which curvature changes. Its geometric shape is not a parabolic
segment. What shape it is, and whether it has a clean formula in terms
of function values at specific points, has not been investigated.

**What is known:** The $x^4$ and $\sin(x)$ test results confirm that the
corrected error after one term scales as $O(\Delta x^5)$ per interval.
The residual is real and measurable. A second correction term exists and
would reduce it further.

**What requires derivation:** The geometric identity of the second
correction shape, its area formula, and the resulting five-point rule (if
that is what it produces).

**Connection to Q1:** These two questions are the same question approached
from different ends. Q1 asks whether the destination matches a known rule.
Q2 asks what the next step looks like geometrically. The answer to either
one answers both.

---

## Q3 -- The multidimensional extension

**Status: OPEN**

The trapezoid and `:` ratio structure of `integration.md` and the
$\mathbin{:}$ ratio derivative of `differentiation.md` both extend
naturally to $n$ dimensions. The conjecture is:

- **Integration:** average the $2^n$ corner values of an $n$-dimensional
  cell, multiply by the cell volume. Exact for multilinear surfaces.
  The correction term is the curvature of the surface over the cell.
- **Partial derivatives:** identical in structure to ordinary derivatives
  -- a `:` ratio with respect to one variable, all others held constant.
- **Gradient, divergence, curl:** collections or combinations of partial
  `:` ratios.
- **Jacobian:** a matrix of `:` ratios; its determinant is the volume
  scaling factor -- a `:` quantity.

**What requires honest derivation:**

Green's theorem, Stokes' theorem, and the Divergence theorem relate
integrals over regions to integrals over their boundaries. The conjecture
is that these survive as geometric `:` statements -- the accumulated
`:` ratio over a region equals a boundary `:` ratio. This has not been
derived. It must be, not assumed.

Surface integrals and line integrals require the geometric area element
(cross product for surfaces; tangent magnitude for curves). Both are
plausibly `:` quantities. The extension is geometrically motivated.
The derivation is pending.

**What does not depend on this question:** The one-dimensional results
in `integration.md` are complete and independent. They stand regardless
of what the multidimensional extension yields.

---

## Note -- Computational comparison

**For future investigation. Not a geometry question.**

The trapezoid+correction form separates the base area from the sliver
correction cleanly. In Simpson's rule the two are merged into a single
formula. The separation may have practical value: the correction can be
computed as a second pass, or omitted entirely when the trapezoid
precision is sufficient for the application.

Whether this separation produces a measurable speed or flexibility
advantage over the merged Simpson's form has not been profiled. It is
noted here because it arises directly from the geometric decomposition
and may be worth investigating once the geometric story is complete.

---

- *Integration: [`integration.md`](./integration.md)*
- *Differentiation: [`differentiation.md`](./differentiation.md)*
- *Notation register: [`../notation.md`](../notation.md)*
