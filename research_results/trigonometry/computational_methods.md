# Computational Methods
### Dirk J. Botha, April 2026

---

The geometric framework produces exact values for constructible angles.
This document describes how those exact values are used as the foundation
for computing trig ratios at arbitrary angles -- more precisely and with
fewer operations than the standard approach.

---

## 1. The 3° Lookup Table

The five base angles from [`special_angles.md`](special_angles.md) --
$0°$, $30°$, $45°$, $60°$, $90°$ -- have a greatest common divisor of
$3°$. Every integer multiple of $3°$ is reachable from these five by
the angle addition formula in a finite number of steps. Each result is
an exact algebraic number.

The complete table spans $0°$ to $90°$ in $3°$ steps: **31 entries**.

By the standard symmetry identities:

$$\begin{aligned}
\sin(90° + A) &= \cos(A) \\
\sin(180° - A) &= \sin(A) \\
\sin(180° + A) &= -\sin(A)
\end{aligned}$$

the full $0°$--$360°$ range follows from those 31 values.

For each entry, store $\cos(A)$ -- the geometrically natural quantity,
monotone decreasing over $[0°, 90°]$. The sine follows from Pythagoras:

$$\sin(A) = \sqrt{1 - \cos^2(A)}$$

No trig function called. One square root.

---

## 2. Bounding Any Arbitrary Angle

For any angle $X$ not in the table, find the two nearest entries:

$$A_{\text{lower}} = \lfloor X \mathbin{:} 3° \rfloor \times 3°, \qquad
A_{\text{upper}} = A_{\text{lower}} + 3°$$

Because $\cos$ is monotone over $[0°, 90°]$:

$$\cos(A_{\text{upper}}) \leq \cos(X) \leq \cos(A_{\text{lower}})$$

Hard bounds. No approximation. No error term. The true value is
guaranteed to fall between them.

---

## 3. Geometric Bisection

To narrow the bounds without a series, apply the half-angle formula:

$$\cos(A \mathbin{:} 2) = \sqrt{(1 + \cos A) \mathbin{:} 2}$$

$$\sin(A \mathbin{:} 2) = \sqrt{(1 - \cos A) \mathbin{:} 2}$$

This is pure Pythagoras. If $\cos(A)$ is known exactly, $\cos(A/2)$
and $\sin(A/2)$ follow from one square root each. No series.

Each bisection halves the interval:

| Steps | Precision |
|-------|-----------|
| 0 (table only) | $\pm 1.5°$ |
| 1 bisection | $\pm 0.75°$ |
| 2 bisections | $\pm 0.375°$ |
| $n$ bisections | $\pm 3° \mathbin{:} 2^n$ |

Ten bisections give $\pm 0.003°$ -- better than any practical
application requires. Each step costs one square root.

---

## 4. The Chord-Geometry Method

For the small residual angle $\varepsilon = X - A$ (where $A$ is the
nearest table entry, $|\varepsilon| \leq 1.5°$), the chord-geometry
method computes $\cos(\varepsilon)$ and $\sin(\varepsilon)$ directly
from the unit circle curvature.

The unit circle has constant curvature $\kappa = 1$ everywhere. The
chord subtending arc $\varepsilon$ is shorter than the arc by the
parabolic sliver (see [`../calculus/integration.md`](../calculus/integration.md)).
With $\kappa = 1$ this correction is exact at every order:

$$\text{chord}(\varepsilon) = \varepsilon - \varepsilon^3 \mathbin{:} 24 + \varepsilon^5 \mathbin{:} 1920$$

From the chord, Pythagoras gives $\cos(\varepsilon)$:

$$\cos(\varepsilon) = 1 - \text{chord}^2 \mathbin{:} 2$$

And the direct series for $\sin(\varepsilon)$ -- used instead of
$\sqrt{1 - \cos^2(\varepsilon)}$ to avoid catastrophic cancellation
for small $\varepsilon$:

$$\sin(\varepsilon) = \varepsilon - \varepsilon^3 \mathbin{:} 6 + \varepsilon^5 \mathbin{:} 120$$

Both $\cos(\varepsilon)$ and $\sin(\varepsilon)$ in hand, the full
result follows from the angle addition formula:

$$\cos(X) = \cos(A + \varepsilon) = \cos A \cdot \cos\varepsilon - \sin A \cdot \sin\varepsilon$$

---

## 5. The Half-Angle Method

The half-angle method reaches the same precision as chord-geometry with
fewer operations, by computing $\sin(\varepsilon \mathbin{:} 2)$ first
and recovering $\cos(\varepsilon)$ via the double-angle identity.

Let $h = \varepsilon \mathbin{:} 2$. For $|\varepsilon| \leq 1.5°$,
$h \leq 0.75°$ -- a smaller argument where one correction term suffices:

$$\sin(h) = h - h^3 \mathbin{:} 6$$

From this, $\cos(\varepsilon)$ follows exactly:

$$\cos(\varepsilon) = 1 - 2\sin^2(h)$$

No correction to $\cos$ itself is needed -- the double-angle identity
is exact. For $\sin(\varepsilon)$:

$$\cos(h) = 1 - h^2 \mathbin{:} 2 + h^4 \mathbin{:} 24$$

$$\sin(\varepsilon) = 2 \cdot \sin(h) \cdot \cos(h)$$

### Operation count comparison

| Step                   | Chord-geo | Half-angle |
|------------------------|:---------:|:----------:|
| Multiplications        |     7     |     6      |
| Divisions              |     6     |     4      |
| Additions/subtractions |     7     |     5      |
| Square roots           |     0     |     0      |

- One fewer multiplication.
- Two fewer divisions.
- Two fewer additions/subtractions.
- Both methods then apply the same angle addition step.
- Full benchmark results in [`test_results.md`](test_results.md).

---

## 6. Comparison with Current Hardware

Modern CPUs and GPUs use a two-step approach:

1. **Range reduction** -- map the input to $[0°, 45°]$ using symmetry
2. **Minimax polynomial** -- evaluate a polynomial optimised to minimise
   maximum error over the interval (Chebyshev / minimax approximation)

For single-precision GPU trig this typically requires 4--5 polynomial
terms after reduction to $[0°, 45°]$.

The geometric approach differs in two ways:

|                 | GPU (current) | Geometric approach         |
|-----------------|---------------|----------------------------|
| Range reduction | to $45°$      | to $1.5°$ (31-entry table) |
| Series terms    | 4--5          | 2--3                       |
| Seeds           | Approximate   | Algebraically exact        |

The GPU approach is engineered for throughput on specific silicon. The
geometric approach is mathematically cleaner: the seeds are exact, the
series is shorter, and the residual error at table points is zero --
not managed, not budgeted, zero.

Whether the geometric approach is faster in hardware depends on the
cost of memory reads versus arithmetic on a given architecture. On
architectures where the 31-value table fits in registers or L1 cache,
the geometric approach wins on both accuracy and speed.

**Current hardware left geometric exactness on the table. The 31-entry
table puts it back.**

---

- *Source code: [`source_code/trig_methods_benchmark.cpp`](source_code/trig_methods_benchmark.cpp)*
- *Test results: [`test_results.md`](test_results.md)*
- *Calculus connection: [`../calculus/integration.md`](../calculus/integration.md)*
- *Notation register: [`../notation.md`](../notation.md)*
- *Previous: [`exact_computation.md`](exact_computation.md)*
- *Next: [`test_results.md`](test_results.md)*
