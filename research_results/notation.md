# Notation Register - Ouroboros Framework
### Dirk J. Botha - maintained from 2026-04-16

This file is the single source of truth for symbol usage across all
Ouroboros research documents. Update it whenever a new symbol is
introduced or an existing meaning is extended. If a symbol is not
listed here, do not use it without adding it first.

---

## Rendering Note

All research documents use GitHub-flavoured markdown with LaTeX math
blocks: `$...$` for inline, `$$...$$` for display.

`\newcommand` is not supported in GitHub's math renderer. Custom macros
defined in preambles will not render. Use the explicit LaTeX forms
listed in the tables below.

**The ratio operator in LaTeX is `\mathbin{:}`.**
This is the LaTeX form of the `:` operator throughout all documents.
Any occurrence of `\mathbin{:}` in a raw file means ratio; not division,
not punctuation.

---

## Operators

| Symbol    | Meaning                | LaTeX              | Notes                                                                                                          |
|-----------|------------------------|--------------------|----------------------------------------------------------------------------------------------------------------|
| `:`       | Ratio (relational)     | `\mathbin{:}`      | The foundational operator. Defines a proportional relationship between two magnitudes. Does not break at zero. |
| `÷`       | Division (operational) | `\div`             | Arithmetic only. Belongs in S⁻. Breaks at zero. Do not use in relational contexts.                             |
| `·`       | Multiplication         | `\cdot`            | Standard.                                                                                                      |
| `+`, `−`  | Addition, subtraction  | `+`, `-`           | Standard.                                                                                                      |
| `²`, `^`  | Exponentiation         | `^{2}`, `^{n}`     | Standard.                                                                                                      |

---

## Domain and State Notation

| Symbol          | Meaning                    | LaTeX                     | Notes                                                                                                                                                                                                                                             |
|-----------------|----------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S⁻              | Standard domain            | `S^-`                     | The domain where the denominator of `:` is non-zero. Ordinary ratios. Keyboard: `S-`.                                                                                                                                                             |
| S⁺(x)           | Domain-switched value      | `S^+(x)`                  | The result of $x \mathbin{:} 0$. Encodes both the direction (sign/argument of x) and magnitude of x at the boundary. Not undefined! A junction point. Keyboard: `S+(x)`.                                                                          |
| ⟲               | Ouroboros                  | `\circlearrowleft`        | The universal closure state: $a \mathbin{:} 0 = 0$, and $a \equiv_\circlearrowleft b$ for all $a, b$. The single point at infinity on the Riemann sphere. Keyboard: `Oro`. Note: `\Oro` macro does not render on GitHub — use `\circlearrowleft`. |
| ≡_⟲             | Oro-equivalence            | `\equiv_\circlearrowleft` | All $S^+$ transitions - real ∞, i·∞, and every complex direction - are Oro-equivalent. They are the same state. Keyboard: `≡_Oro`.                                                                                                                |

---

## Mathematical Constants

| Symbol  | Meaning                      | LaTeX     | Notes                                                                                                                                    |
|---------|------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| π       | Circumference : diameter     | `\pi`     | $\pi = C \mathbin{:} d$. A `:` relationship, not a `÷` result. The numerical value is a consequence, not the definition.                 |
| φ       | **Golden ratio — RESERVED**  | `\varphi` | $\varphi = (a+b) \mathbin{:} a = a \mathbin{:} b$. Defined in `euclidean_geometry.md`. **Do not use φ for angles or any other purpose.** |
| e       | Euler's number               | `e`       | Base of the natural logarithm. Standard.                                                                                                 |
| i       | Imaginary unit               | `i`       | $i^2 = -1$. Standard.                                                                                                                    |

---

## Angle Variables

| Symbol | Meaning                                      | LaTeX    | Notes                                                                                                                                                                                                                 |
|--------|----------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| θ      | Primary trig angle                           | `\theta` | Defined as arc:radius (a `:` quantity). Used throughout all trig derivations. Ranges over ℝ for real angles; over ℂ for complex angles.                                                                               |
| ψ      | Argument / phase of a complex number         | `\psi`   | $\psi = \arg(z)$ for $z = re^{i\psi}$. Range: $(-\pi, \pi]$ for the principal value. Chosen to avoid collision with φ (golden ratio).                                                                                 |
| A, B   | General angles in addition formulae          | `A`, `B` | Used when two distinct angles appear simultaneously (e.g. $\sin(A+B)$).                                                                                                                                               |
| α      | Sphere orientation — polar angle from Z-axis | `\alpha` | Used in the dimensional address system. Expresses the orientation of the unit circle within the sphere relative to the Z-axis. Expressed as $\alpha \mathbin{:} \tau$ (fraction of full rotation).                    |

---

## Geometric Quantities (Right Triangle)

| Symbol | Meaning                              | LaTeX        | Notes                                                        |
|--------|--------------------------------------|--------------|--------------------------------------------------------------|
| opp    | Side opposite θ                      | `\text{opp}` | One of the three geometric primitives.                       |
| adj    | Side adjacent to θ (not hypotenuse)  | `\text{adj}` | One of the three geometric primitives.                       |
| hyp    | Hypotenuse                           | `\text{hyp}` | Equals the radius r in the unit circle. The third primitive. |

---

## General Variables

| Symbol  | Meaning                                                                   | LaTeX         | Notes                                                                                            |
|---------|---------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------|
| r       | Magnitude / modulus of a complex number; also radius of a general circle  | `r`           | $r = \|z\|$ in complex contexts. In the unit circle, $r = 1$ and $\text{hyp} = r = 1$.          |
| a, b, c | General magnitudes                                                        | `a`, `b`, `c` | Used in Euclidean geometry contexts. $a^2 + b^2 = c^2$ is Pythagoras.                           |
| x, y    | General real variables                                                    | `x`, `y`      | Standard.                                                                                        |
| z       | Complex variable                                                          | `z`           | $z = a + bi = re^{i\psi}$.                                                                       |
| u, v    | Real and imaginary parts of a complex angle                               | `u`, `v`      | $\theta = u + iv$. $u$ is the real part (rotation), $v$ is the imaginary part (scaling via sinh/cosh). |
| n       | Integer index                                                             | `n`           | Used in periodicity ($\cos(\theta + 2\pi n) = \cos(\theta)$), summation, etc.                   |

---

## Number Sets and Geometric Objects

| Symbol | Meaning         | LaTeX       | Notes                                                                                                                                                          |
|--------|-----------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ℝ      | Real numbers    | `\mathbb{R}` | Standard.                                                                                                                                                     |
| ℂ      | Complex numbers | `\mathbb{C}` | Standard. $\mathbb{C} \cup \{\circlearrowleft\}$ = Riemann sphere.                                                                                            |
| ℤ      | Integers        | `\mathbb{Z}` | Standard.                                                                                                                                                     |
| S¹     | Unit circle     | `S^1`        | The 1-sphere in 2D real space. The domain of the standard trig functions over ℝ. Becomes the equator of the Riemann sphere in the ℂ extension.                |

---

## Trig Functions (shorthand for `:` relationships)

These are not defined independently — they are named abbreviations for
ordered `:` relationships between {opp, adj, hyp}. Listed here for
reference; defined fully in `trigonometry_from_ratio.md` Part 3.

| Symbol    | `:` definition                  | LaTeX        |
|-----------|---------------------------------|--------------|
| sin(θ)    | $\text{opp} \mathbin{:} \text{hyp}$ | `\sin(\theta)` |
| cos(θ)    | $\text{adj} \mathbin{:} \text{hyp}$ | `\cos(\theta)` |
| tan(θ)    | $\text{opp} \mathbin{:} \text{adj}$ | `\tan(\theta)` |
| csc(θ)    | $\text{hyp} \mathbin{:} \text{opp}$ | `\csc(\theta)` |
| sec(θ)    | $\text{hyp} \mathbin{:} \text{adj}$ | `\sec(\theta)` |
| cot(θ)    | $\text{adj} \mathbin{:} \text{opp}$ | `\cot(\theta)` |

Arc functions (arcsin, arccos, arctan, arccsc, arcsec, arccot) are their
inverses. Domain restrictions in `÷` notation are notational artefacts;
in `:` notation the arc functions accept S⁺ inputs. See Part 13–14 of
`trigonometry_from_ratio.md`.

---

## Calculus Notation

| Symbol    | Meaning                  | LaTeX                     | Notes                                                                                                                                                                                                                             |
|-----------|--------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Δx        | Finite difference in x   | `\Delta x`                | A `:` quantity -- a change in magnitude, not an infinitesimal.                                                                                                                                                                    |
| Δf        | Finite difference in f   | `\Delta f`                | $\Delta f = f(x + \Delta x) - f(x)$. A `:` quantity.                                                                                                                                                                              |
| f'(x)     | Derivative of f at x     | `f'(x)`                   | Shorthand for $[f(x+\Delta x) - f(x)] \mathbin{:} \Delta x$ at S⁺. Not a limit -- a `:` ratio at the boundary.                                                                                                                    |
| ∂f/∂x     | Partial derivative       | `\partial f / \partial x` | Shorthand for the `:` ratio with respect to x, all other variables held constant. **Use with caution** -- the `÷` form implies limit machinery that is not present. Prefer $\Delta f \mathbin{:} \Delta x$ where clarity matters. |
| Σ         | Finite sum               | `\sum`                    | The complete statement of integration in this framework. No limit. No `∫` required.                                                                                                                                               |
| ∫         | Avoid                    | --                        | The integral sign implies a limit process that is not present. Use `\sum` with the trapezoid formula instead.                                                                                                                     |

---

## Symbols to Avoid / Reserved for Future Use

| Symbol | Status                        | Reason                                                                                                                                                     |
|--------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| φ      | Reserved -- golden ratio only | Already defined above. Using it for angles caused a collision; replaced with ψ in Part 14 (2026-04-16).                                                    |
| δ, ε   | Avoid in `:` contexts         | Traditionally paired with limits (ε-δ definition). Their presence implies limit machinery; using them here would suggest a connection that does not exist. |
| lim    | Avoid                         | The limit is the workaround the `:` framework makes unnecessary. Do not import the notation.                                                               |
| /      | Avoid                         | Ambiguous between `:` and `÷`. Use `:` or `÷` explicitly.                                                                                                  |

---

## Update Log

| Date       | Change                                                                                                                                                                                                                                                  |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2026-04-16 | File created. Symbols compiled from all Ouroboros documents to date. ψ introduced for complex argument (replacing φ to avoid golden ratio collision).                                                                                                   |
| 2026-04-16 | α introduced for sphere orientation (polar angle from Z-axis) in dimensional address system.                                                                                                                                                            |
| 2026-04-17 | `Oro` claimed as the keyboard-typeable notation for ⟲. LaTeX macro `\Oro` defined but not supported in GitHub markdown -- use `\circlearrowleft` in rendered documents.                                                                                 |
| 2026-04-17 | `S+` / `S-` adopted as keyboard-typeable notation for S⁺ / S⁻. LaTeX: `S^+` / `S^-`.                                                                                                                                                                    |
| 2026-04-18 | Calculus notation registered. `Δ` for finite difference, `Σ` for finite sum, `∂` retained as shorthand for partial `:` ratio (with caution).                                                                                                            |
| 2026-04-25 | File moved to `research_results/notation.md` -- now spans all research output, not calculus only. LaTeX column added to all tables. Rendering note added: `\mathbin{:}` is the LaTeX form of the ratio operator; `\newcommand` not supported on GitHub. |
