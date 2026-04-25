# Differentiation; A Geometric Account
### Dirk J. Botha, April 2026

---

## 1. The Question

What is the instantaneous rate of change of $f(x)$ at a point?

This is a geometric question. It has a geometric answer.

---

## 2. The Chord

The diagram from `integration.md` applies here without modification.

![Chord between two points on a curve](./images/trapezoid_diagram.png)

Given two points on a curve:

$$P_1 = (x,\ f(x)), \qquad P_2 = (x + \Delta x,\ f(x + \Delta x))$$

the slope of the chord connecting them is:

$$\text{slope} = (f(x + \Delta x) - f(x)) \mathbin{:} \Delta x$$

This is a $\mathbin{:}$ ratio. It exists for any finite $\Delta x$. It is
the average rate of change of $f$ over the interval. No limit. No
approximation.

Integration asked: what area lies beneath this chord?
Differentiation asks: what is the slope of this chord?

Same geometry. Two questions.

---

## 3. The Boundary

The instantaneous rate of change is this same ratio, evaluated at the
point where $\Delta x = 0$. In $\mathbin{:}$ notation, that is the
$S^+$ boundary — the ratio as the denominator approaches zero.

$$f'(x) = [f(x + \Delta x) - f(x)] \mathbin{:} \Delta x \quad \text{at } S^+$$

The $\mathbin{:}$ operator does not break at zero. $S^+$ encodes both
the direction and the magnitude of the ratio at the boundary. The
derivative is not a process approaching a limit; it is a $\mathbin{:}$
ratio evaluated at a point. The limit was invented to reach what
$\mathbin{:}$ already handles.

---

## 4. Bridge Cancellation

For polynomial functions, the numerator factors before the boundary
is reached. The $\Delta x$ cancels algebraically; this is bridge
cancellation. The $S^+$ transition is then clean: nothing divides by
zero because the zero has already been removed.

For $f(x) = x^2$:

$$\begin{aligned}
[f(x + \Delta x) - f(x)] \mathbin{:} \Delta x
&= [(x + \Delta x)^2 - x^2] \mathbin{:} \Delta x \\
&= [2x \cdot \Delta x + \Delta x^2] \mathbin{:} \Delta x \\
&= \Delta x \cdot [2x + \Delta x] \mathbin{:} \Delta x \\
&= [2x + \Delta x] \mathbin{:} 1
\end{aligned}$$

At $\Delta x = 0$: $\quad f'(x) = 2x$.

The cancellation is algebraic. No limit was needed; the limit was
invented to justify a cancellation that $\mathbin{:}$ handles directly.

---

## 5. Trig Derivatives

The derivatives of $\sin(\theta)$ and $\cos(\theta)$ follow from the
geometry of the unit circle. No limit is required.

On the unit circle, $\sin(\theta)$ is the height of a point at angle
$\theta$ and $\cos(\theta)$ is its horizontal position. As $\theta$
increases, the point moves along the arc. The rate of change of height
with respect to arc length equals the horizontal coordinate at that
point — and the rate of change of horizontal position equals the
negative of the height. Both are geometric facts about the circle.

$$\begin{aligned}
d(\sin \theta) \mathbin{:} d\theta &= \cos \theta \\
d(\cos \theta) \mathbin{:} d\theta &= -\sin \theta
\end{aligned}$$

These results fall directly from the geometry. The limit formulation
was a reconstruction of what the circle states immediately.

*Full derivation: trigonometry section (forthcoming).*

---

## 6. What Was Removed

The derivative is not a process. It is a $\mathbin{:}$ ratio at a
point; the ratio of the change in the function to the change in the
input, evaluated where the input change is zero. The ratio exists at
that point. The geometry determines it.

What is removed:

| Removed                           | Replaced by                                          |
|-----------------------------------|------------------------------------------------------|
| The limit                         | $S^+$ boundary of a $\mathbin{:}$ ratio              |
| $\varepsilon$-$\delta$ definition | Bridge cancellation + $S^+$ transition               |
| $\frac{d}{dx}$ as a process       | $\mathbin{:}$ ratio evaluated at a point             |
| $\frac{0}{0}$ indeterminate form  | Cancellation precedes the boundary; it never arrives |

**What is kept:** every derivative calculus ever computed.

---

- *Notation register: [`../notation.md`](../notation.md)*
- *Integration: [`integration.md`](integration.md)*
