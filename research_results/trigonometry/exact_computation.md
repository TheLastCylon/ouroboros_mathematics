# Exact Computation
### Dirk J. Botha, April 2026

**TODO**: Add diagram.

---

For most angles, computing the $\mathbin{:}$ ratios requires arithmetic.
This document describes two geometric results that make that arithmetic
exact -- no series, no approximation -- for a well-defined family of angles.

---

## 1. Sine as Half-Chord

The geometric meaning of sine predates algebra. In Sanskrit mathematics
the term was *jya* -- bowstring. The arc is the bow. The chord across
it is the string. The sine is half the string.

This is not a metaphor. It is the definition, stated geometrically.

On a unit circle, to find $\sin(A)$:

1. Mark an arc equal to $A \mathbin{:} 180$ of the full circumference
2. Connect the two endpoints of that arc -- the chord
3. Half the chord $= \sin(A)$

No formula. No series. The circle produces the answer directly from the
arc fraction.

### Why $\pi$ cancels

Expressed as an absolute length, the arc requires $\pi$. But in the
$\mathbin{:}$ framework, the arc is a ratio:

$$\text{arc} \mathbin{:} \text{circumference} = 2A° \mathbin{:} 360° = A \mathbin{:} 180$$

No $\pi$. The circumference appears on both sides and cancels. For
integer $A$, this is a ratio of two integers. The angle in degrees maps
directly to a fraction of the circle.

### The full chain

$$A° \;\longrightarrow\;
\text{arc} \mathbin{:} \text{circumference} = A \mathbin{:} 180 \;\longrightarrow\;
\text{chord} \;\longrightarrow\;
\sin(A) = \text{chord} \mathbin{:} 2$$

Everything stays in $\mathbin{:}$ ratios throughout. The circle converts
the arc fraction into the chord ratio directly. The sine function is
the circle's native response to a fraction of its own circumference.

---

## 2. The Square Construction

On the unit circle at angle $\theta$, draw the radius $OP =
(\cos\theta, \sin\theta)$, length 1. Build the square with $OP$ as its
diagonal.

From the $45°$ geometry (see [`special_angles.md`](special_angles.md)):

$$\text{side} \mathbin{:} \text{diagonal} = 1 \mathbin{:} \sqrt{2}$$

Since the diagonal is 1, the side is $1 \mathbin{:} \sqrt{2}$. This
is fixed -- it does not depend on $\theta$.

### The corners

The four corners of the square include two points $C$ and $D$:

$$\begin{aligned}
C &= \tfrac{1}{2}(\cos\theta - \sin\theta,\ \cos\theta + \sin\theta) \\
D &= \tfrac{1}{2}(\cos\theta + \sin\theta,\ \sin\theta - \cos\theta)
\end{aligned}$$

Both $C$ and $D$ sit at distance $1 \mathbin{:} \sqrt{2}$ from the
origin. Their angles from the $x$-axis:

$$\text{angle of } C = \theta + 45°, \qquad \text{angle of } D = \theta - 45°$$

The $45°$ shift is not introduced from outside -- it is built into the
square by the $1 \mathbin{:} \sqrt{2}$ side-to-diagonal ratio.

### The key result

$$\begin{aligned}
D_x + D_y &= \tfrac{1}{2}(\cos\theta + \sin\theta) + \tfrac{1}{2}(\sin\theta - \cos\theta) = \sin\theta \\
D_x - D_y &= \tfrac{1}{2}(\cos\theta + \sin\theta) - \tfrac{1}{2}(\sin\theta - \cos\theta) = \cos\theta
\end{aligned}$$

The coordinates of corner $D$ give $\sin(\theta)$ and $\cos(\theta)$
by addition and subtraction. One addition. One subtraction. Nothing else.

### The complete chain for 63°

$$\begin{aligned}
&63° = 45° + 18° \\
&\text{Corner } D \text{ sits at angle } 63° - 45° = 18°,\text{ distance } 1 \mathbin{:} \sqrt{2} \\
&18° \text{ is a pentagon angle:} \\
&\quad \sin(18°) = (\sqrt{5} - 1) \mathbin{:} 4 \quad \text{(exact, from golden ratio geometry)} \\
&\quad \cos(18°) = \sqrt{10 + 2\sqrt{5}} \mathbin{:} 4 \quad \text{(exact, from Pythagoras)} \\
&\therefore \\
&\sin(63°) = D_x + D_y = \tfrac{1}{\sqrt{2}}\bigl[\cos(18°) + \sin(18°)\bigr] \\
&\cos(63°) = D_x - D_y = \tfrac{1}{\sqrt{2}}\bigl[\cos(18°) - \sin(18°)\bigr]
\end{aligned}$$

Every value exact. Every step a $\mathbin{:}$ relationship. Every
intermediate result an algebraic number.

---

## 3. The General Case and Its Honest Limitation

Corner $D$ always sits at angle $\theta - 45°$ and distance
$1 \mathbin{:} \sqrt{2}$. For any angle $\theta$:

- If $\theta - 45°$ is in the special angles table: one step, done
- If $\theta - 45°$ is a pentagon-family angle: the golden ratio gives
  exact values, done
- Otherwise: apply the square again, reducing by $45°$ per step, until
  a known angle is reached

All integer multiples of $3°$ are reachable. The chain terminates. The
result is exact.

**The honest limitation:** To locate corner $D$ geometrically for an
arbitrary angle $\theta$, you need the coordinates of the unit-circle
point at $\theta$ -- which are $\cos\theta$ and $\sin\theta$, the values
being sought. For arbitrary angles the construction is therefore circular
as a standalone algorithm. Its role in computation is as a reduction
tool: given a nearby known angle, it steps $45°$ closer per application.
The computation path for arbitrary angles rests on the angle addition
formula in [`angle_addition.md`](angle_addition.md), not on this
construction alone.

The theorem -- that $D_x + D_y = \sin\theta$ and $D_x - D_y = \cos\theta$
-- is universal and exact. The computational limitation is separate from
the theorem.

---

## 4. What Was Available All Along

For constructible angles -- all integer multiples of $3°$, and any
angle reachable by the addition and subtraction formulae from the base
set -- the geometric construction gives:

| Standard approach     | Geometric approach        |
|-----------------------|---------------------------|
| Infinite series       | No series                 |
| Truncated at $n$ terms | No truncation             |
| Approximation at every step | Exact at every step |
| Error budget required | No error -- the result is the result |

This does not extend to all angles. For non-constructible angles, a
series remains the standard computational route. The geometric route
applies exactly where the angle is constructible -- and for that family,
it is exact and finite.

The Taylor series was built because this geometric route was not
followed. For the constructible family, it was never needed.

---

- *Notation register: [`../notation.md`](../notation.md)*
- *Previous: [`the_sphere.md`](the_sphere.md)*
- *Next: [`open_questions.md`](open_questions.md)*
