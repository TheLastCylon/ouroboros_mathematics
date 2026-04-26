# Ouroboros Mathematics — Papers

*Dirk J. Botha*

These are the citable outputs of the Ouroboros mathematics framework. Each paper
is self-contained. They share a common foundation: the distinction between `:` (ratio,
relational) and `÷` (division, operational), and the geometric picture that follows
from it.

The working notes, derivations, benchmarks, and source code behind each paper live
in [`../research_results/`](../research_results/).

---

## Available

| Paper                                            | Title                    | Status                       |
|--------------------------------------------------|--------------------------|------------------------------|
| [cos_from_pythagoras.md](cos_from_pythagoras.md) | *cos(x) from Pythagoras* | planned submittion to arXiv  |

---

## In Preparation

| #   | Title                                                                      | One line                                                                                                                                          |
|-----|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| P01 | *Ouroboros: A Consistent Framework for Division by Zero*                   | Names the object at `0÷0`, proves closure, compares to Wheel Algebra.                                                                             |
| P02 | *The Ratio/Division Distinction: Why Two Operators Are Necessary*          | `:` is relational and irreducible. `÷` is operational and breaks at zero. Every field that confused them built scaffolding to manage the fallout. |
| P03 | *The Rectangle Was Wrong: Integration Without Limits*                      | The limit exists because the rectangle was the wrong shape. The trapezoid is exact. The remaining sliver has a direct geometric formula.          |
| P04 | *Trigonometry from Ratio*                                                  | Sin, cos, and tan are `:` ratios on the unit circle. No series. No π in the definitions.                                                          |
| P05 | *A Geometric Trig Computation System*                                      | 31-entry table from five constructible angles, plus chord-geometry for arbitrary precision. Benchmarked against standard library.                 |
| P06 | *Calculus Without Limits: Differentiation as a `:` Ratio*                  | For polynomials, Δx cancels before the boundary is reached. No limit required.                                                                    |
| P07 | *Statistics Is `:` Underneath*                                             | Probability, Bayes, softmax, likelihood -- all `:` ratios. The breakdowns are `÷` artefacts.                                                      |
| P08 | *Geometry Invades Algebra: A Historical Reckoning*                         | Descartes 1637. Four centuries of scaffolding. What the geometry was always saying.                                                               |
| P09 | *Fractals as Integer-Dimensional Objects with `:` Filling Ratios*          | Hausdorff dimension is a `:` scaling ratio, not a fractional dimension.                                                                           |
| P10 | *Dimensional Collapse: DI[n] and the Geometry of Scale*                    | Every scale is 3-dimensional geometry. ⟲ as the seam between scales.                                                                              |
| P11 | *The AI Training Implication*                                              | If statistics is `:` underneath, the parameter budget changes.                                                                                    |
| P12 | *I Don't Want to Learn Your Math, your Math is toxic*                      | The synthesis. For everyone who was ever made to feel stupid for asking the obvious question. Write this one last.                                |
| P13 | *The Versed Sine: A Non-Trigonometric Foundation for Circular Computation* | chord² = 2·versin from Pythagoras alone. The complete circular geometry without trig definitions.                                                 |
| P14 | *Irrational Numbers Are a Notation Problem, Not a Number Problem*          | √2 is exact. π is exact. They only look broken when forced through decimal notation.                                                              |

---

*One weld at a time.*
