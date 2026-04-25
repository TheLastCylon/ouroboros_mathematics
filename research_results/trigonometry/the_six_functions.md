# The Six Functions
### Dirk J. Botha, April 2026

---

## 1. The Angle

Before the functions. Before the triangle. The angle itself.

An angle is not a number of degrees. It is not a number of radians.
It is a `:` relationship between two lengths -- the arc traced on a
circle and the radius of that circle:

$$\theta = \text{arc} \mathbin{:} \text{radius}$$

A full rotation traces the full circumference. Since the circumference
and the radius are related by:

$$\pi = C \mathbin{:} d = C \mathbin{:} 2r \quad \Rightarrow \quad C \mathbin{:} r = 2\pi$$

a full rotation is $2\pi$ -- not because someone defined it that way,
but because the full arc is the circumference and $C \mathbin{:} r = 2\pi$.

**Consequence:** Every angle in trigonometry is a $\mathbin{:}$ quantity
from the ground up. The functions built on angles are $\mathbin{:}$
relationships built on $\mathbin{:}$ relationships. Division never enters.

---

## 2. The Triangle

Consider a right triangle. Label the three sides relative to an angle $\theta$:

- **opp** -- the side opposite $\theta$
- **adj** -- the side adjacent to $\theta$ (not the hypotenuse)
- **hyp** -- the hypotenuse

These three sides are the complete geometric vocabulary of the right
triangle. Everything trigonometry has ever said about angles is a
statement about the $\mathbin{:}$ relationships between these three
magnitudes.

---

## 3. The Six Functions

Three distinct magnitudes. How many ordered $\mathbin{:}$ relationships
exist between distinct pairs?

The $\mathbin{:}$ operator is ordered -- $a \mathbin{:} b$ and
$b \mathbin{:} a$ are different relationships. Each pair of magnitudes
therefore contributes two entries. Three pairs, two directions each:
exactly six.

| Ratio                               | Name      | Notation       |
|-------------------------------------|-----------|----------------|
| $\text{opp} \mathbin{:} \text{hyp}$ | sine      | $\sin(\theta)$ |
| $\text{hyp} \mathbin{:} \text{opp}$ | cosecant  | $\csc(\theta)$ |
| $\text{adj} \mathbin{:} \text{hyp}$ | cosine    | $\cos(\theta)$ |
| $\text{hyp} \mathbin{:} \text{adj}$ | secant    | $\sec(\theta)$ |
| $\text{opp} \mathbin{:} \text{adj}$ | tangent   | $\tan(\theta)$ |
| $\text{adj} \mathbin{:} \text{opp}$ | cotangent | $\cot(\theta)$ |

This is a complete enumeration. Not six definitions that happened to be
useful. Not a collection that grew over centuries. The complete set of
ordered $\mathbin{:}$ relationships between three distinct magnitudes --
closed by construction. No more exist. None are missing.

### Forward and reverse

Each function pairs with its reverse:

| Forward                                            | Reverse                                            | Relationship                |
|----------------------------------------------------|----------------------------------------------------|-----------------------------|
| $\sin(\theta) = \text{opp} \mathbin{:} \text{hyp}$ | $\csc(\theta) = \text{hyp} \mathbin{:} \text{opp}$ | $\sin \mathbin{:} \csc = 1$ |
| $\cos(\theta) = \text{adj} \mathbin{:} \text{hyp}$ | $\sec(\theta) = \text{hyp} \mathbin{:} \text{adj}$ | $\cos \mathbin{:} \sec = 1$ |
| $\tan(\theta) = \text{opp} \mathbin{:} \text{adj}$ | $\cot(\theta) = \text{adj} \mathbin{:} \text{opp}$ | $\tan \mathbin{:} \cot = 1$ |

The third column follows from a single fact: any magnitude in ratio with
itself equals 1. Each forward function and its reverse are the same
$\mathbin{:}$ relationship stated twice -- once in each direction. Their
ratio is therefore always 1.

What algebra calls "reciprocal identities" -- $\csc = 1 \div \sin$,
$\sec = 1 \div \cos$, $\cot = 1 \div \tan$ -- is this table expressed
using $\div$ instead of $\mathbin{:}$. The relationship was never
algebraic. It was always geometric direction.

### The arc functions

The six functions take an angle and return a ratio. The arc functions
run the other way -- they take a ratio and return an angle:

$$\sin(\theta) = \text{opp} \mathbin{:} \text{hyp}
\quad \Longleftrightarrow \quad
\arcsin(\text{opp} \mathbin{:} \text{hyp}) = \theta$$

The cycle is complete:

$$\theta \;\xrightarrow{\sin}\; \text{opp} \mathbin{:} \text{hyp}
\;\xrightarrow{\arcsin}\; \theta$$

Six functions. Six arc functions. A closed loop -- entirely within the
$\mathbin{:}$ domain.

The domain restrictions on arc functions in standard notation --
$\arcsin$ only accepts $[-1, 1]$, $\arctan$ never reaches $\pm 90°$ --
are not geometric constraints. They are the boundary walls of the $\div$
operator. In $\mathbin{:}$ notation those walls are not present. The arc
functions accept any input the geometry produces.

---

## 4. The One Identity

Standard trigonometry teaches three Pythagorean identities:

$$\begin{aligned}
\sin^2(\theta) &+ \cos^2(\theta) &= 1 \\
\tan^2(\theta) &+ 1 &= \sec^2(\theta) \\
1 &+ \cot^2(\theta) &= \csc^2(\theta)
\end{aligned}$$

Substitute the $\mathbin{:}$ definitions into each:

$$\begin{aligned}
(\text{opp} \mathbin{:} \text{hyp})^2 + (\text{adj} \mathbin{:} \text{hyp})^2 &= 1
&\Rightarrow\quad \text{opp}^2 + \text{adj}^2 &= \text{hyp}^2 \\
(\text{opp} \mathbin{:} \text{adj})^2 + 1 &= (\text{hyp} \mathbin{:} \text{adj})^2
&\Rightarrow\quad \text{opp}^2 + \text{adj}^2 &= \text{hyp}^2 \\
1 + (\text{adj} \mathbin{:} \text{opp})^2 &= (\text{hyp} \mathbin{:} \text{opp})^2
&\Rightarrow\quad \text{opp}^2 + \text{adj}^2 &= \text{hyp}^2
\end{aligned}$$

All three reduce to the same statement:

$$\text{opp}^2 + \text{adj}^2 = \text{hyp}^2$$

There is one identity. It is Pythagoras.

The three versions in standard trigonometry are the same geometric truth
stated with three different reference denominators. In $\div$ notation
they look different. In $\mathbin{:}$ notation they are visibly,
immediately, the same statement.

The Pythagorean trigonometric identities were never trigonometric
identities. They were always geometry.

---

- *Notation register: [`../notation.md`](../notation.md)*
- *Next: [`the_boundary.md`](./the_boundary.md)*
