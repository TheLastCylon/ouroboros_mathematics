# Ouroboros Mathematics
### A Consistent Framework for Division by Zero

*Dirk J. Botha, April 2026*

---

## Abstract

Standard arithmetic leaves `0 ÷ 0` undefined and stops there. This paper does
not stop there.

We distinguish strictly between two operations that conventional notation
conflates:
- division (`÷`), which is operational and breaks at zero, and
- ratio (`:`), which is relational and does not.

From three axioms governing the ratio operator (information preservation,
identity, and direction) we name the object at `0 ÷ 0` as `⟲` (Ouroboros) and
derive its properties.

The resulting framework is closed under division by zero: every path through
zero has exactly one destination, and that destination is stable. Key results
include `0 : 0 = 1` (nothing compared to nothing is unity) and the singularity
formula `0 ≡_⟲ 1`: from inside `⟲`, no operation distinguishes zero from
totality.

All values are indistinguishable within `⟲`.

We compare this framework to Wheel Algebra, which starts at the same point but
cannot recover `x : x = 1` for degenerate elements due to its single-operator
structure. The singularity formula is outside the reach of wheel algebra entirely.

The entire framework follows from one refusal: that the ratio `0 : 9` is not zero,
because the nine is still there and relivant.

---

## Motivation

Standard arithmetic defines division as the inverse of multiplication. Because
multiplication by zero destroys information irreversibly, its inverse breaks.

`0 ÷ 0` is declared undefined and left at that.

This framework takes a different approach:

Rather than patching around the break, it names the object that lives at that
point and derives what it can and cannot do. The result is a system that is
**closed under division by zero**. Every path through zero has exactly one
destination, and that destination is stable.

The central insight is a strict distinction between two operations that standard
notation conflates:

- **Division (`÷`)** is operational.
    - i.e. How many times does this go into that?
    - It Breaks at zero.
- **Ratio (`:`)** is relational.
    - i.e. What is the relationship between these two things?
    - Does not break at zero.

Division and Ratio can agree (e.g. `3 ÷ 4 = 0.75` and `3 : 4 = 0.75`) but they
are fundamentally different.

Within this framework they are never treated as equivalent.

### The critical observation: `0 : a ≠ 0`

Standard treatments of ratio (including basic textbooks) treat `a : b` as
shorthand for `a ÷ b`. Under that treatment, `0 : 9 = 0 ÷ 9 = 0`. This is
convenient and apparently harmless.

It is not harmless. It is a loss of information.

`0 : 9` does not mean zero. It means *zero of one thing, in the presence of nine
of another*.

Both quantities exist. Both are real. The nine is not a denominator to be
discarded; it is half of a relationship.

Writing `0 : 9 = 0` erases the fact that even though none of `x` is needed,
nine of `y` are still present. The context is lost.

A ratio `a : b` is irreducible. It is already in its simplest form as a
relational statement. Collapsing it to a single number (treating `a : b` as `a ÷ b`)
is valid only under explicitly stated conditions, that are not always met. The
relational context is not redundant. Discarding it produces either the wrong
answer or the loss of critical information.

This matters most at the boundary.

Under the textbook treatment:
`0 : 0 = 0 ÷ 0` is undefined.

Under Ouroboros Mathematics treatment:
`0 : 0` means: zero of one thing, in the presence of zero of another.

The same thing.

The same relationship.

**Unity.** `0 : 0 = 1`.

The entire framework follows from refusing to lose that information. Everything
else is derivation.

---

## Axioms of the Ratio Operator `:`

These axioms govern the `:` operator throughout the framework. They are stated
before the rules because the rules are derived from them.

**Axiom 1 — Information Preservation:**

*A ratio `a : b` is irreducible. Neither `a` nor `b` may be discarded. The
simplification `a : b = a ÷ b` is only valid when `a ≠ 0`, `b ≠ 0` and loss
of `b` as context does not affect the result.*

This is the foundational axiom. It is the refusal to silently discard data.
Under everyday conditions, `a : b = a ÷ b` is a convenient and mostly harmless
shorthand. At the boundary, specifically at `0 : 0`, the shorthand fails
catastrophically and the information that was being discarded turns out to be
critical.

**Axiom 2 — Identity:**

*`x : x = 1` for any `x`.*

Any quantity compared to itself is unity. This holds universally -- for ordinary
numbers, for zero, for `⟲`, and for compound ratio expressions. No exceptions.
The identity property is not conditional on `x` being "well-behaved."

This axiom is what Wheel Algebra's single-operator framework cannot achieve for
degenerate elements. It is available here because `:` is not `÷`.

**Axiom 3 — Direction:**

*`:` is ordered. `a : b ≠ b : a` in general.*

A ratio is a directed relationship. "3 of x in relation to 4 of y" is not the
same statement as "4 of y in relation to 3 of x." They are reciprocals, not
equals. Direction is part of the information that Axiom 1 requires to be
preserved.

---

## The Framework

### Definition

**`0 ÷ 0 = ⟲`**

Where `⟲` (Ouroboros) is defined as:

> *The beginning, end, and everything between (including nothing) all at the same time.*

`⟲` is not undefined. It is a named object with specific, derivable properties.

---

### Rule 1 — Self-Ratio

**`⟲ : ⟲ = 1`**

The totality relative to itself is pure unity.

*Consistent with:* `lim(x→0) x/x = 1`

---

### Rule 2 — Reciprocity (opposite directions)

**`(a : ⟲) : (⟲ : a) = 1` for ANY `a`**

The two complementary views of `a` and `⟲` balance to oneness.

**Proof:**

Write the expression as a continued proportion by removing the outer parentheses:

`(a : ⟲) : (⟲ : a)` = `a : ⟲ : ⟲ : a`

The term `⟲` appears consecutively as the bridge of the continued proportion. In
a continued proportion, a common bridge term cancels -- `a:b` then `b:c` reduces
to `a:c`. Applied here:

`a : ⟲` then `⟲ : a` reduces to `a : a`

By Axiom 2: `a : a = 1`.

The `⟲ : ⟲` structure in the middle of the chain is visible directly -- Rule 1
confirms it collapses to unity before either `a : ⟲` or `⟲ : a` need to be
evaluated in isolation. Structural pattern recognition takes precedence over
component evaluation.

---

### Rule 3 — Same-Direction Reduction (common reference)

**`(a : ⟲) : (b : ⟲) = a : b` for ANY `a`, `b`**

When both are measured against the same totality, the Ouroboros cancels cleanly,
recovering the direct ordinary ratio.

**Structural cancellation takes precedence over component evaluation.** When the
structural pattern of the rule is present (same reference in both denominators),
cancel first, then evaluate what remains.

*Consistent with:* `lim(x→0) ax/bx = a/b`

---

### Rule 4 — Closure Under Division by Zero

**`⟲ ÷ 0 = 0 ÷ 0 ÷ 0 = (0 × 1) ÷ (0 × 0) = 0 ÷ 0 = ⟲`**

- The fraction chain rule is being extended to the case where `a = b = c = 0`.
- Through algebraic manipulation, using the fraction multiplication rule.
- **`⟲ ÷ 0 = ⟲`**
- The system is closed under division by zero.
- It has exactly one destination. You cannot escape `⟲` by dividing by zero. Zero is not a trapdoor out.
- Every path through zero routes back to `⟲`, and `⟲` is stable.

---

## Derived Properties

These follow from the definition and rules above.

### Absorption

`⟲` absorbs under all standard arithmetic operations:

- `⟲ + a = ⟲` -- `⟲` already contains `a`
- `⟲ × a = ⟲` -- multiplication is repeated addition
- `⟲ - a = ⟲` -- follows from the above (verified: `(0/0) - a = (0 - 0a)/(0) = 0/0 = ⟲`)
- `⟲² = ⟲`    -- follows from multiplication absorption
- `⟲ ÷ a = ⟲` -- for **all** `a` -- see below

### Universal Absorption Under Division

`⟲ ÷ a = ⟲` holds for every `a`, not just `a = 0`:

- For `a ≠ 0`: `(0/0) ÷ (a/1) = (0×1)/(0×a) = 0/0 = ⟲`
- For `a = 0`: Rule 4
- For `a = ⟲`: `(0/0) ÷ (0/0) = (0×0)/(0×0) = 0/0 = ⟲`

**Consequence:**

`⟲ ÷ ⟲ = ⟲` (not 1). The ratio `⟲ : ⟲ = 1` and the division `⟲ ÷ ⟲ = ⟲` are
different results from different operators. This is not a contradiction -- it
demonstrates exactly why the ratio/division distinction matters.

### Universal Closure: `a ÷ 0 = ⟲` for All `a`

The framework is closed under division by zero for any numerator, not only `a = 0`.

**Proof:**

By the fraction multiplication rule:

`(0 ÷ 1) × (1 ÷ 0) = (0×1) ÷ (1×0) = 0 ÷ 0 = ⟲`

Since `0 ÷ 1 = 0`:

`0 × (1 ÷ 0) = ⟲`

From the absorption properties established above, `0 × (finite) = 0` and `0 × ⟲ = ⟲`.

Therefore: `0 × x = ⟲` has exactly one solution in the system: `x = ⟲`.

Therefore: **`1 ÷ 0 = ⟲`**

For any `a`:

`a ÷ 0 = a × (1 ÷ 0) = a × ⟲ = ⟲`

By absorption.

**`a ÷ 0 = ⟲` for all `a`, without exception.** The numerator is irrelevant.
Division by zero has one destination regardless of what is being divided.
Rule 4 (`⟲ ÷ 0 = ⟲`) is now seen as a special case of this general result.

### Exponentiation

The absorption behaviour of `⟲` extends to exponentiation -- in both the base
and exponent positions.

**`0^0 = ⟲`**

By the exponent subtraction rule `a^0 = a^n ÷ a^n`, setting `a = 0, n = 1`:

`0^0 = 0^1 ÷ 0^1 = 0 ÷ 0 = ⟲`

**`⟲^0 = ⟲`**

By the same rule: `⟲^0 = ⟲^n ÷ ⟲^n = ⟲ ÷ ⟲ = ⟲` (universal absorption under division).

Note: `⟲^0 = ⟲`, not 1. The conventional `a^0 = 1` does not hold when `a = ⟲` -- absorption takes precedence.

**`⟲^n = ⟲` for all `n ≥ 1`**

Follows directly from multiplication absorption: repeated multiplication of `⟲` by itself remains `⟲`.

**`a^⟲ = ⟲` for any `a`**

Since `1 ÷ 0 = ⟲`, the zeroth root `a^(1/0) = a^⟲`. Two cases:

1. `a = 0`: `0^⟲ = ⟲^⟲`. By multiplication absorption: `⟲^⟲ = ⟲^n × ⟲^(⟲-n) = ⟲ × ⟲^(⟲-n) = ⟲`.

2. `a ≠ 0`: `a^⟲ = (a^0)^(1÷0) = 1^⟲`. Since `⟲` contains all values -- including
   those for which `1^z ≠ 1` (complex exponents) -- the output spans all values: `1^⟲ = ⟲`.

**Summary -- `⟲` absorbs in any position:**

| Expression      | Result | Route                           |
|-----------------|--------|---------------------------------|
| `0^0`           | `⟲`    | Exponent subtraction; `0÷0 = ⟲` |
| `⟲^0`           | `⟲`    | Exponent subtraction; `⟲÷⟲ = ⟲` |
| `⟲^n` (n ≥ 1)   | `⟲`    | Multiplication absorption       |
| `a^⟲` (any `a`) | `⟲`    | Universal closure; `1÷0 = ⟲`    |

---

## The `0 : 0` Result

From Rule 3 with `a = b = 0`:

`(0 : ⟲) : (0 : ⟲) = 0 : 0`

The left side has identical expressions on both sides of `:`. By the identity
property of the ratio operator -- **any expression compared to itself is 1** --
the left side equals 1.

Therefore: **`0 : 0 = 1`**

This is NOT `0 ÷ 0`. Under the strict separation:

| Expression | Operator               | Result |
|------------|------------------------|--------|
| `0 ÷ 0`    | Division (operational) | `⟲`    |
| `0 : 0`    | Ratio (relational)     | `1`    |

Zero divided by zero is Ouroboros. Zero compared to zero is unity. Same inputs,
different operators, different answers. The separation is not a convenience -- it
is load-bearing.

---

## The Singularity

### The Observation

From Rule 1 and the `0 : 0` result:

**`⟲ : ⟲ = 0 : 0 = 1`**

The totality compared to itself, and nothing compared to itself, are the same relationship: unity.

### Why `⟲ ÷ a = ⟲` for all `a` Matters

Since `⟲` absorbs everything under division, the map `f(x) = ⟲ ÷ x` is **constant**.
A constant map has no discriminatory power -- it cannot tell its inputs apart.
This means that from within `⟲`, no operation can distinguish between two values.
All values are **indistinguishable** within `⟲`.

### The Singularity Formula

**`0 ≡_⟲ 1`**

Where `a ≡_⟲ b` means: *no operation within `⟲` can distinguish `a` from `b`.*

More generally: `∀ a, b : a ≡_⟲ b`

This does NOT mean `0 = 1` on the number line. `0` and `1` are distinct in
ordinary arithmetic. The statement is scoped to `⟲`: from inside `⟲`, the
distinction does not exist.

The beginning and the end are indistinguishable at the singularity. The
definition predicted this. The algebra confirms it.

---

## Order of Operations Principle

**Structural pattern recognition takes precedence over component evaluation.**

When a rule's structural pattern is present in an expression, apply the rule to
the whole expression first. Do not evaluate individual components before applying
the structural rule -- doing so can lose structural information and produce
incorrect results.

This principle is implicit throughout the framework and must be made explicit in
any formal treatment.

Examples where it applies:
- Rule 3        : cancel the common `⟲` reference before evaluating `a` or `b`
- Rule 4's proof: apply the fraction chain rule to `0 ÷ 0 ÷ 0` as a whole before
  evaluating the left pair

---

## Relationship to Existing Literature

### Wheel Algebra (Jesper Carlström, 2001)

*"Wheels — On Division by Zero"*, Research Reports in Mathematics No. 11, 2001.
Department of Mathematics, Stockholm University. (Filosofie licentiatavhandling.)

Wheel algebra extends any commutative ring or semiring so that division by any
element -- including zero -- is always possible. The resulting structure is
called a *wheel*. The bottom element is `⊥ = 0/0`. Structural overlap with `⟲`
exists at the starting point and in some absorption properties.

#### What wheel algebra does

- `/` is a **unary** reciprocal operator (not binary division): `x/y` means `x · (/y)`
- `⊥ = 0/0` absorbs under addition: `x + ⊥ = ⊥` (Axiom 8)
- `⊥` absorbs under multiplication: `(0/0)x = 0/0` (derived Rule 11)
- Derived Rule 12: **`x/x = 1 + 0x/x`** -- NOT simply `x/x = 1`

Rule 12 is the critical one. For ordinary elements where `0x = 0`, it simplifies
to `x/x = 1`. But for `x = ⊥`: `0·⊥ = ⊥` (by Rule 11), so `⊥/⊥ = 1 + ⊥/⊥`.
Since `⊥` absorbs under addition, `1 + ⊥ = ⊥`, therefore:

**`⊥/⊥ = ⊥` in wheel algebra.**

The bottom element divided by itself is itself -- not 1. This is consistent
with `⟲ ÷ ⟲ = ⟲` in Ouroboros. The division result agrees.

The Wheel Algebra framework uses a single operator. Within that structure, there
is no equivalent of `⟲ : ⟲ = 1` -- the property `x/x = 1` holds only in `ℛH`, the
regular subset where `0x = 0`. For degenerate elements it does not extend, and
the single-operator design offers no path to recover it. This is not a gap in
the work -- it is a consequence of different goals.

#### The divergence

| Property              | Carlström Wheels (2001)                           | Ouroboros (2026)                                   |
|-----------------------|---------------------------------------------------|----------------------------------------------------|
| Bottom element        | `⊥ = 0/0`                                         | `⟲ = 0 ÷ 0`                                        |
| `(0/0) ÷ (0/0)`       | `⊥`                                               | `⟲ ÷ ⟲ = ⟲` — agrees                               |
| `(0/0) : (0/0)`       | Not defined — no `:` operator                     | `⟲ : ⟲ = 1`                                        |
| `x:x = 1` universally | Not present                                       | Yes — identity property of `:`                     |
| `0 : 0`               | Not defined                                       | `0 : 0 = 1`                                        |
| `⟲:⟲ = 0:0 = 1`       | Not present                                       | Singularity observation                            |
| Singularity formula   | Not present                                       | `0 ≡_⟲ 1`                                          |
| Operator structure    | Single unary `/`                                  | Two operators: `÷` (operational), `:` (relational) |
| Motivation            | Make division total; algebraic extension of rings | Name the object; relational interpretation         |
| `0x = 0`              | Does NOT hold in general                          | Absorption: `0 × ⟲ = ⟲` (consistent)               |

#### Summary

The two frameworks start at the same point (`0/0` named and given properties)
and agree on the division behaviour of their respective bottom elements (`⊥/⊥ = ⊥` and `⟲ ÷ ⟲ = ⟲`).
They diverge at the ratio/division distinction -- a fork that Wheel Algebra's design
does not take, because it was not the intended destination.

Within a single-operator structure, `x:x = 1` for degenerate elements is not
reachable. The Ouroboros framework reaches it by treating ratio and division as
fundamentally different operations. That distinction is what opens the path to
the singularity.

Wheel algebra and Ouroboros mathematics are not in conflict. They set out to do
different things and both succeed. The singularity (`0 ≡_⟲ 1`) is simply outside
the scope of wheel algebra -- not contradicted, not superseded. A different road
from the same starting point.

---

## Open Questions

1. Does the framework extend to `∞` without additional axioms? (Standard
   limitation -- most extended number systems have edge cases at `∞`)
