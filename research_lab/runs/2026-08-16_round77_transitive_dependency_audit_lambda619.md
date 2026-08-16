# Round 77 — Transitive dependency audit of the `lambda >= 6.19` shortcut

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status of the mathematical implication:** INTERNALLY_PROVED relative to the published unconditional Polymath theorem `Lambda <= 0.22`.  
**Strict-program admissibility:** **FAILS the project's explicit no-finite-height-RH-verification rule.**  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Why this audit was necessary

Round 73 / Round 75 introduced a strong shortcut:

\[
\Lambda\le0.22
\]

plus interior simplicity for `t>Lambda` removes all times `t>0.22`, leaving only a direct PSC certificate on `0<t<=0.22`. That gives the mathematically unconditional shoulder statement

\[
\lambda\ge6.19
\Longrightarrow
(H_t,H_t')\ne(0,0)
\]

for `0<t<=1/2`, provided the published Polymath upper bound is admitted as a black-box theorem.

The project's user-specified research constitution, however, contains a stricter methodological rule:

> finite-height verification of RH is not to be used as part of the global proof.

The earlier hostile audit checked only the **direct** inputs of the `6.19` argument and therefore missed a transitive dependency inside the proof of `Lambda<=0.22`.

---

## 2. Source-level dependency check

D.H.J. Polymath states Theorem 1.1:

\[
\boxed{\Lambda\le0.22.}
\]

This theorem is unconditional in the usual mathematical sense.

But the paper immediately says that the proof of Theorem 1.1 combines numerical verification with asymptotic arguments. Its Theorem 1.2 explicitly assumes as hypothesis (i):

`Numerical verification of RH at initial time 0`.

More precisely, hypothesis (i) requires absence of zeta zeros in a finite box up to height `X/2`. The paper then proves Theorem 1.1 by taking

\[
t_0=0.2,
\qquad
X=6\times10^{10}+83952-0.5,
\qquad
y_0=0.2,
\]

and explains that the choice `X` is close to the limit of then-known numerical verifications of RH, which are needed for hypothesis (i).

Therefore the dependency graph is

\[
\boxed{
\text{finite-height RH verification}
\longrightarrow
\text{Polymath }\Lambda\le0.22
\longrightarrow
\text{Round-73 time reduction}
\longrightarrow
C=6.19.
}
\tag{77.1}
\]

The finite-height verification is not an **assumption** of RH and does not make the published theorem conditional. But it is nevertheless a genuine transitive proof dependency.

---

## 3. Mathematical circularity versus project admissibility

These must be separated.

### 3.1 Mathematical circularity

There is no ordinary logical circularity in using `Lambda<=0.22` to seek `Lambda<=0`.
The former is an independently proved, strictly weaker upper bound. Thus the `6.19` theorem remains a mathematically unconditional theorem relative to accepted published computation.

### 3.2 Strict project rule

The project's explicit rule is stronger than ordinary non-circularity: it forbids finite-height RH verification from entering the global proof route.

Under that rule, transitive dependencies count. Consequently the `Lambda<=0.22` reduction cannot be part of the **canonical strict proof graph**, because its published proof uses exactly the excluded finite-height verification input.

Hence the earlier Round-75 sentence

> `finite-height RH verification` is not used

was too strong and is corrected here. The accurate statement is:

> Round 75 does not invoke finite-height RH verification directly, but its `Lambda<=0.22` black-box input has such verification in its proof ancestry.

---

## 4. Correct two-track status

We now maintain two distinct shoulder constants.

### Track U — unrestricted unconditional published-input track

If all unconditional published theorems are admissible regardless of their certified computational ancestry, then

\[
\boxed{C_U=6.19.}
\]

The Round-73/75 K=2048 certificate and the interior-simplicity reduction remain valid on this track.

### Track S — strict no-finite-height-RH-verification track

If the user's research constitution is enforced transitively, the `Lambda<=0.22` reduction is excluded.

The strongest currently certified shoulder theorem whose dependency closure avoids finite-height RH verification is Round 76:

\[
\boxed{
0<t\le1/2,
\quad
\lambda\ge6.90
\Longrightarrow
(H_t,H_t')\ne(0,0).
}
\]

Thus

\[
\boxed{C_S=6.90.}
\tag{77.2}
\]

The active research program must continue from `6.90`, not from `6.19`, unless the project constitution is explicitly changed.

---

## 5. Interior-simplicity lemma survives

This audit does **not** refute the lemma

\[
t>\Lambda\Longrightarrow\text{all zeros of }H_t\text{ are simple}.
\]

The local proof is sound: a multiplicity-`m>=2` real zero at `t_0>Lambda`, evolved a sufficiently small distance backward while remaining above `Lambda`, has scaled leading model

\[
e^{+\partial_w^2}w^m=i^{-m}Q_m(iw),
\]

where `Q_m=e^{-\partial_w^2}w^m` has distinct real zeros. For `m>=2` the backward model has a genuinely nonreal zero, and Hurwitz/Rouche transfers it to the exact nearby function, contradicting real-rootedness for times still greater than `Lambda`.

The issue is solely that the numerical value `0.22` used to instantiate `t>Lambda` is not admissible on Track S.

---

## 6. What remains admissible from Polymath

The strict track may continue to use the **analytic effective Riemann--Siegel estimates** from Polymath (Theorem 1.3 / Corollary 6.5 and their explicit error bounds), provided the particular estimates invoked do not themselves depend on the finite-height RH verification hypothesis.

Those analytic estimates are exactly the inputs used by Rounds 64--66 and Round 76. They are separate from Theorem 1.1's global `Lambda<=0.22` numerical-verification argument.

Thus Round 76 remains the canonical strict shoulder theorem.

---

## 7. Corrected research priority

Track S is the project's primary track under the user's stated rules.

Current strict frontier:

\[
\boxed{C_S=6.90.}
\]

Next target:

\[
\boxed{C_{S,\rm target}=6.85.}
\]

Use the established hierarchy:

1. exact-weight PSC for the small-time and lower-time sectors;
2. Round-74 soft APVC for the finite-time upper corner;
3. Round-75 convex-secant APVC for residual interval/majorant losses;
4. only after a pointwise APVC obstruction is localized, move to the joint invariant `J` or exact joint-jet certificate.

The `6.19` computations remain valuable as diagnostics and as a theorem on Track U, but they must not be used to close any gap in Track S.

---

## 8. Corrected circularity/admissibility labels

For future state files use:

- `MATHEMATICALLY_UNCONDITIONAL`: yes for the Polymath `Lambda<=0.22` theorem and Track-U `6.19` consequence;
- `ORDINARY_CIRCULARITY`: no circularity detected;
- `STRICT_PROGRAM_ADMISSIBLE`: **no** for any proof path containing Polymath Theorem 1.1 / `Lambda<=0.22`, because of the finite-height RH-verification ancestor;
- `STRICT_PROGRAM_ADMISSIBLE`: yes for Round 76's `6.90` proof path;
- `RH`: OPEN.

This distinction is mandatory in all subsequent summaries.
