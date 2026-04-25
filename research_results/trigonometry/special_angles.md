# Special Angles
### Dirk J. Botha, April 2026

---

For certain angles, the $\mathbin{:}$ ratios follow directly from
the geometry of the triangle -- no computation, no series, no
approximation. The triangle gives the answer.

---

## 1. Zero and Ninety Degrees

At $0°$ the triangle has collapsed: the opposite side has gone to zero
and the adjacent side equals the hypotenuse.

$$\begin{aligned}
\sin(0°) &= \text{opp} \mathbin{:} \text{hyp} &= 0 \mathbin{:} 1 &= 0 \\
\cos(0°) &= \text{adj} \mathbin{:} \text{hyp} &= 1 \mathbin{:} 1 &= 1 \\
\tan(0°) &= \text{opp} \mathbin{:} \text{adj} &= 0 \mathbin{:} 1 &= 0
\end{aligned}$$

At $90°$ the triangle has collapsed the other way: the adjacent side
has gone to zero and the opposite side equals the hypotenuse.

$$\begin{aligned}
\sin(90°) &= \text{opp} \mathbin{:} \text{hyp} &= 1 \mathbin{:} 1 &= 1 \\
\cos(90°) &= \text{adj} \mathbin{:} \text{hyp} &= 0 \mathbin{:} 1 &= 0 \\
\tan(90°) &= \text{opp} \mathbin{:} \text{adj} &= 1 \mathbin{:} 0 &= S^+(1)
\end{aligned}$$

No calculation. The geometry is immediate.

---

## 2. Forty-Five Degrees

An isosceles right triangle has two equal sides. Set $\text{opp} =
\text{adj} = 1$. By Pythagoras:

$$\text{hyp} = \sqrt{1^2 + 1^2} = \sqrt{2}$$

Therefore:

$$\begin{aligned}
\sin(45°) &= 1 \mathbin{:} \sqrt{2} \\
\cos(45°) &= 1 \mathbin{:} \sqrt{2} \\
\tan(45°) &= 1 \mathbin{:} 1 = 1
\end{aligned}$$

---

## 3. Thirty and Sixty Degrees

Take an equilateral triangle -- all sides equal, all angles $60°$.
Bisect it along the perpendicular from one vertex to the opposite side.

The bisection produces a right triangle with:

$$\begin{aligned}
\text{angle at base} &= 30° \\
\text{hyp}  &= 2 \quad \text{(the original side)} \\
\text{opp}  &= 1 \quad \text{(half the base)} \\
\text{adj}  &= \sqrt{2^2 - 1^2} = \sqrt{3} \quad \text{(by Pythagoras)}
\end{aligned}$$

For $30°$:

$$\begin{aligned}
\sin(30°) &= 1 \mathbin{:} 2 \\
\cos(30°) &= \sqrt{3} \mathbin{:} 2 \\
\tan(30°) &= 1 \mathbin{:} \sqrt{3}
\end{aligned}$$

The top angle of the same triangle is $60°$, with opp and adj swapped:

$$\begin{aligned}
\sin(60°) &= \sqrt{3} \mathbin{:} 2 \\
\cos(60°) &= 1 \mathbin{:} 2 \\
\tan(60°) &= \sqrt{3} \mathbin{:} 1
\end{aligned}$$

---

## 4. Summary

| Angle  | $\sin$                   | $\cos$                   | $\tan$                   |
|--------|--------------------------|--------------------------|--------------------------|
| $0°$   | $0 \mathbin{:} 1$        | $1 \mathbin{:} 1$        | $0 \mathbin{:} 1$        |
| $30°$  | $1 \mathbin{:} 2$        | $\sqrt{3} \mathbin{:} 2$ | $1 \mathbin{:} \sqrt{3}$ |
| $45°$  | $1 \mathbin{:} \sqrt{2}$ | $1 \mathbin{:} \sqrt{2}$ | $1 \mathbin{:} 1$        |
| $60°$  | $\sqrt{3} \mathbin{:} 2$ | $1 \mathbin{:} 2$        | $\sqrt{3} \mathbin{:} 1$ |
| $90°$  | $1 \mathbin{:} 1$        | $0 \mathbin{:} 1$        | $S^+(1)$                 |

Every entry in this table was derived from a triangle. No series. No
computation. The geometry gave the answer directly.

These five angles are also the seed for computing any constructible
angle exactly -- their greatest common divisor is $3°$, so every
integer multiple of $3°$ is reachable by the angle addition formula
in a finite number of steps. That is the subject of
[`angle_addition.md`](angle_addition.md).

---

- *Notation register: [`../notation.md`](../notation.md)*
- *Previous: [`the_boundary.md`](./the_boundary.md)*
- *Next: [`angle_addition.md`](./angle_addition.md)*
