# The Boundary
### Dirk J. Botha, April 2026

---

## 1. The Problem

In standard notation, four trigonometric values are declared undefined:

$$\tan(90°) = \sin(90°) \div \cos(90°) = 1 \div 0 \quad \text{-- undefined}$$

$$\sec(90°) = 1 \div \cos(90°) = 1 \div 0 \quad \text{-- undefined}$$

$$\csc(0°) = 1 \div \sin(0°) = 1 \div 0 \quad \text{-- undefined}$$

$$\cot(0°) = 1 \div \tan(0°) = 1 \div 0 \quad \text{-- undefined}$$

These are treated as walls -- places the functions cannot go. The
geometry stops. The algebra has nothing left to say.

The geometry did not stop. The notation did.

---

## 2. What Actually Happens

At $\tan(90°)$, the triangle has not collapsed into nonsense. It has
reached a specific, well-defined geometric state: the adjacent side has
gone to zero while the opposite side remains. The ratio $\text{opp}
\mathbin{:} \text{adj}$ still exists. It is a real geometric relationship.
The $\div$ operator cannot express it. The $\mathbin{:}$ operator can.

When the denominator of a $\mathbin{:}$ relationship reaches zero, the
result is not undefined. It is a junction point -- a value that encodes
both the direction of approach and the magnitude being carried at the
moment of transition. This is written $S^+(x)$, where $x$ is the value
carried through.

| Function       | Angle  | $\mathbin{:}$ expression                                       | Result            |
|----------------|--------|----------------------------------------------------------------|-------------------|
| $\tan(\theta)$ | $90°$  | $\sin(90°) \mathbin{:} \cos(90°) = 1 \mathbin{:} 0$            | $S^+(1)$          |
| $\sec(\theta)$ | $90°$  | $\text{hyp} \mathbin{:} \text{adj} = \text{hyp} \mathbin{:} 0$ | $S^+(\text{hyp})$ |
| $\csc(\theta)$ | $0°$   | $\text{hyp} \mathbin{:} \text{opp} = \text{hyp} \mathbin{:} 0$ | $S^+(\text{hyp})$ |
| $\cot(\theta)$ | $0°$   | $\text{adj} \mathbin{:} \text{opp} = \text{adj} \mathbin{:} 0$ | $S^+(\text{adj})$ |

The function does not fail. It transitions.

---

## 3. Direction Is Preserved

The $S^+$ transition carries the sign of the numerator through the
boundary. This matters.

$\tan(90°)$ is approached from below with a positive numerator:
$S^+(1)$.

$\tan(270°)$ is approached with a negative numerator: $S^+(-1)$.

In $\div$ notation both are simply "undefined." The direction is
discarded. In $\mathbin{:}$ notation the direction survives:

$$\tan(90°) = S^+(1) \neq S^+(-1) = \tan(270°)$$

Two distinct geometric states. One notation can express them. The other
cannot.

---

## 4. One Boundary, Not Four Walls

In $\div$ notation the four undefined values look like four separate
failures -- four places where different functions break for different
reasons.

In $\mathbin{:}$ notation they are the same event, encountered from
different directions by different functions:

- $\cos(\theta) = 0$ at $90°$ and $270°$ -- $\tan$ and $\sec$ transition here
- $\sin(\theta) = 0$ at $0°$ and $180°$ -- $\csc$ and $\cot$ transition here

Every case is the geometry reaching the point where one side of the
triangle goes to zero while the other remains. The $\mathbin{:}$
relationship is still real. The $S^+$ value records it.

The four walls were never four walls. They were one boundary, seen
through a notation that could not look past it.

The geometry continues.

---

- *Notation register: [`../notation.md`](../notation.md)*
- *Previous: [`the_six_functions.md`](./the_six_functions.md)*
- *Next: [`special_angles.md`](./special_angles.md)*
