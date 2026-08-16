# Round 80 — Dedicated literature survey for the singular wedge

**Date:** 2026-08-16

**Target scaling:**

\[
t\to0^+,
\qquad
x=\exp(O(1/t)),
\qquad
\lambda=t\log(x/(4\pi))=O(1).
\]

**RH status:** OPEN.

## 1. Main finding

The dedicated search did **not** locate a published theorem that directly gives a uniform no-multiple-zero result in the fixed-lambda double-scaling regime.

The closest existing result is already the D.H.J. Polymath effective Riemann--Siegel / large-x theory. Its heat-deformed Riemann--Siegel formula has precisely the parameter combination relevant to the wedge:

- heat weights `b_n^t = exp((t/4) log^2 n)`;
- shifted Dirichlet exponent `s_*` containing approximately `(t/4) log(x/(4pi)) = lambda/4`;
- large-x dominance once `x>=exp(C/t)`.

Thus the literature already identifies the correct scaling, but it treats it mainly through a sufficiently-large-constant threshold `lambda>=C`, not through a sharp fixed-lambda transversality theorem.

## 2. Ki--Kim--Lee

Ki--Kim--Lee prove fixed-positive-parameter eventual reality and simplicity of zeros. Their asymptotic counting/error terms are not uniform as the heat parameter tends to zero. Secondary summaries explicitly warn that the threshold is not made quantitatively uniform in the deformation parameter.

Therefore KKL removes the fixed-t tail qualitatively, but it does not solve the wedge.

## 3. Polymath

Polymath explicitly improves and makes KKL effective. Proposition 9.1 / Theorem 1.5 control `H_t` for `x>=exp(C/t)`. Their Riemann--Siegel formula is already the natural analytic starting point for the fixed-lambda wedge.

Crucially, Polymath also remarks that a bound `Lambda<=O(t0)` is naturally tied to RH verification up to height `exp(C/t0)`, and heuristically argues that an `O(1/log T)` barrier is difficult to beat without major new RH information.

This does **not** prove that a no-multiple-zero wedge theorem is impossible; it says that any such theorem strong enough to drive Lambda to zero must contain genuinely new information rather than merely repackaging the existing large-x estimate.

## 4. Rodgers--Tao

Rodgers--Tao contains strong saddle-point asymptotics and zero-dynamics machinery, but its main negative-time proof is organized under the contradiction assumption `Lambda<0`, and its zero-motion formulas are used where simplicity is already available. It is therefore not a black-box solution to the positive-time unknown wedge.

Some saddle-point techniques may be reusable analytically, but every imported lemma must be dependency-audited before use.

## 5. Total positivity / PF route

A 2026 preprint, arXiv:2602.20313, gives a certified negative `5x5` Toeplitz minor for the original de Bruijn--Newman kernel, proving that kernel is not PF5. Hence the direct route

`original kernel -> PF_infinity -> LP -> RH`

is closed.

This is useful negative knowledge: do not spend research time trying to prove full total positivity of the undeformed original kernel.

It does not rule out transformed kernels, parameter-dependent positivity, or local determinant inequalities tailored to the wedge.

## 6. What appears genuinely new

The literature gap is now quite specific. We need one of the following, uniformly for fixed lambda in a useful interval as `t->0+`:

1. a sharper two-saddle / two-Dirichlet-sum transversality theorem;
2. a phase-sensitive lower bound preventing simultaneous cancellation of value and derivative;
3. an exact-weight asymptotic theorem retaining enough correlation to beat positive triangle majorants;
4. a uniform joint-jet theorem for the normalized Riemann--Siegel model;
5. a rigorous matched asymptotic expansion with error small enough to transfer simple-zero structure from a limiting model.

The existing project tools PSC, APVC, secant APVC, and `J` are therefore not redundant. Their correct role is precisely to probe this missing fixed-lambda theorem.

## 7. Recommended next program

Do not continue reducing the numerical shoulder by hundredths as the primary goal.

Instead:

### Phase A — derive the limiting fixed-lambda model

Starting from Polymath Theorem 1.3, derive uniformly on compact lambda intervals the exact `t->0+` limit of the normalized value and first derivative, including the two conjugate Riemann--Siegel pieces and exact heat weights.

### Phase B — classify limiting collisions

Solve the limiting simultaneous system

\[
F_\lambda(\theta)=0,
\qquad
\partial_x F_\lambda(\theta)=0
\]

or its correctly rescaled derivative analogue. Determine whether the limiting model itself has a positive transversality gap for lambda above a threshold, and identify the exact threshold/mechanism if not.

### Phase C — uniform perturbation theorem

Prove that the finite-t normalized joint jet converges to the limiting joint jet uniformly enough that a positive limiting gap survives for all sufficiently small t.

### Phase D — match to fixed-positive-time literature/computation

Once small `0<t<=epsilon0` is handled analytically in lambda coordinates, use Polymath Theorem 1.5 plus validated compact computation for `epsilon0<=t<=Tmax`.

This architecture separates the only genuinely singular analytic task from the already-known fixed-positive-time theory.

## 8. Status of current 6.83 campaign

The `6.85` strict shoulder theorem remains valid and useful as a certified benchmark. The `6.83` computations may continue as diagnostics of the limiting threshold, but they should no longer be treated as the main research objective.

The next main theorem target is not `C=6.83`; it is a **uniform singular-wedge theorem** in a nontrivial compact lambda interval, with an explicit limiting joint-jet and a rigorous perturbation estimate.
