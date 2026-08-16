# Collision Program State — Round 63 addendum

**Date:** 2026-08-16  
**RH status:** OPEN.

## New certified baseline

The research lab now contains an unconditional high-shoulder collision-exclusion theorem:

\[
\boxed{
0<t\le1/2,
\quad
\lambda=t\log\frac{|x|}{4\pi}\ge10.52
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\]

The associated phase-slope transversality certificate and 512/768-bit regression data are integrated under:

- `knowledge/phase_slope_transversality_v1.md`;
- `knowledge/high_shoulder_lambda1052_proposition.md`;
- `knowledge/high_shoulder_lambda1052_regression.json`.

The boundary-collision reduction is also integrated under `knowledge/boundary_collision_reduction.md`.

## Reprioritization

This evidence materially changes the post-Round-61 ranking.

### P0 — Low-Shoulder exact-weight PSC

**PRIMARY.** Replace the worst-edge `n^{-p}` majorant by the true quadratic heat weights, prove the small-time moment collapse, and prove the renormalized transversality limit.

Frozen asymptotic target:

\[
\boxed{
 t\mathcal T(t,\lambda)
\to
\frac\lambda2
\left[
2-\zeta\left(\frac12+\frac\lambda4\right)
\right]
}
\]

uniformly on compact subsets of `(4,infinity)`, with explicit remainder.

### P1 — compact certified bridge

After an explicit small-time cutoff is obtained, cover the compact remaining strip from `lambda_*+epsilon` to `10.52` using audited directed rounding.

### P2 — below-floor mechanism

Let `p0` satisfy `zeta(p0)=2` and

\[
\lambda_*=4(p_0-1/2)=4.914588956\ldots.
\]

This is **not** a proved collision threshold. It is the structural sign floor of the unchanged `S0=1-A0` triangle PSC architecture. Below it a different certificate is required.

### P3 — prime-side all-orders program

Rounds 48--61 remain valid and are retained as the long-horizon sparse-complete backup. Their invention target is a finite prime-side all-orders factorization/operator. This route is no longer the immediate P0 because the certified `10.52` theorem exposes a lower-risk quantitative obstruction that should be removed first.

## Immediate one-new-lemma target

Prove explicit, uniform true-weight asymptotics for

\[
A_0(t,\lambda)
\quad\text{and}\quad
A_1(t,\lambda)
\]

under `x=4pi exp(lambda/t)` on compact `lambda` intervals contained in `(4,infinity)`.

Until that analytic lemma is resolved, do not spend the primary effort on finer interval arithmetic or on further constant shaving.
