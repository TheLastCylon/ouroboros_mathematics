# Open Questions -- Trigonometry
### Dirk J. Botha, April 2026

These are honest gaps. The results in the preceding documents stand
independent of what these questions yield. They are recorded here
because they are worth pursuing, not because anything already written
depends on them.

---

## Q1 -- Exact computation for non-constructible angles

**Status: OPEN**

The geometric construction in [`exact_computation.md`](exact_computation.md)
is exact and finite for all constructible angles -- every integer
multiple of $3°$, and any angle reachable by the addition and
subtraction formulae from the base set.

For non-constructible angles (for example, $1°$ or any irrational
multiple of a degree), no finite geometric chain reaches the answer.
A series remains the standard route.

The bowstring definition offers a different framing: the angle names
an arc fraction $A \mathbin{:} 180$, and the circle produces the chord
directly. For integer $A$ this is a ratio of two integers -- no $\pi$,
no transcendental step. Whether this arc-ratio framing suggests a new
exact numerical path for non-constructible angles -- one that bypasses
the series entirely -- has not been investigated.

**What requires investigation:** Whether stepping off $A \mathbin{:} 180$
of the circumference as a pure ratio, without locating it via
coordinates, provides a computational path that does not require
$\cos\theta$ and $\sin\theta$ as inputs. If it does, the circularity
of the square construction for arbitrary angles may be resolvable.

---

## Q2 -- Half-angle method verification

**Status: CLOSED -- 2026-04-25. Tested in `geo_trig_demo.cpp`.**

**Results:**

| Method     | Accuracy   | Speed        |
|------------|------------|--------------|
| Half-angle | 8.05e-16   | 54.1 M ops/s |
| Horner     | 2.20e-15   | 55.8 M ops/s |

The half-angle method is more precise than Horner (8.05e-16 vs
2.20e-15 -- nearly one order better) and within 3% of its speed on
CPU. The precision improvement confirms the theoretical prediction.
The speed gap from the earlier chord-geo benchmark is closed.

**What this establishes:**

The half-angle method reaches sub-machine-epsilon accuracy and matches
Horner in practical speed. It is the most precise of the five methods
tested (chord-geo, half-angle, versin, kite, Horner). Full results in
[`test_results.md`](test_results.md).

---

*Previous documents: [`the_six_functions.md`](the_six_functions.md)
through [`exact_computation.md`](exact_computation.md)*
*Computational methods: [`computational_methods.md`](computational_methods.md)*
*Notation register: [`../notation.md`](../notation.md)*
