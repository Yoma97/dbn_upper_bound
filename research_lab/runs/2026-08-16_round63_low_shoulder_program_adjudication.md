# Round 63 — Low-Shoulder program adjudication and reprioritization

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Status labels:** PROVED BASELINE / PROGRAM DECISION / CANDIDATE ASYMPTOTIC THEOREM / STRUCTURAL NO-GO / CIRCULARITY AUDITED.

## 0. Executive verdict

A newly certified high-shoulder theorem materially changes the project ranking after Round 61.

We now have an unconditional collision exclusion

\[
\lambda=t\log\frac{|x|}{4\pi}\ge10.52
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0)
\]

for `0<t<=1/2`, together with a phase-slope transversality certificate whose actual-weight regression has enormous slack compared with the uniform power-majorant proof.

Therefore the immediate project priority is changed from the Round-62 prime-side all-orders invention gate to:

\[
\boxed{
\text{exact heat-weight analysis}
\to
\text{renormalized small-time PSC limit}
\to
\text{compact certified cover}.
}
\]

The prime-side all-orders program remains the principal long-horizon backup for the region below the structural floor of the current PSC mechanism.

## 1. Why the ranking changed

The global `10.52` proof replaces

\[
a_n=\exp\left(\frac t4\log^2n-\sigma\log n\right)
\]

by the worst-edge majorant `a_n<=n^-1.814`.

This gives

\[
A_0\le0.861634072184451,
\qquad A_1\le1.444773803962031,
\]

whereas a full certified actual-weight boundary regression gives

\[
A_0\le0.20955042280644084,
\qquad A_1\le0.22794011633558037.
\]

The resulting PSC margin jumps from roughly `0.00518` to `8.08759`.

Thus the first quantitative obstruction is located: the uniform edge exponent loses the quadratic heat-weight structure. `Phi0`, `d`, `E0`, and `E1` are not the dominant loss at the proved boundary.

## 2. Correct small-time scaling

Write

\[
x=4\pi e^{\lambda/t}.
\]

Then

\[
\sigma=\frac12+\frac\lambda4+o(1),
\]

and fixed-`n` amplitudes satisfy

\[
a_n\to n^{-(1/2+\lambda/4)}.
\]

For `lambda>4`, the moving-cutoff counting tail has exponentially negative endpoint exponent `lambda(4-lambda)/(16t)`. This identifies `lambda>4` as the natural domain for proving a uniform exact-weight zeta limit.

The frozen theorem target is

\[
A_0(t,\lambda)
=\zeta\left(\frac12+\frac\lambda4\right)-1+o_K(1),
\]

\[
A_1(t,\lambda)
=-\zeta'\left(\frac12+\frac\lambda4\right)+o_K(1)
\]

uniformly on each compact `K subset (4,infinity)`, with explicit remainders.

## 3. Correct renormalized margin

Since

\[
t\Phi_0\to\frac\lambda4,
\qquad d\to\frac12,
\]

and the normalized effective errors should vanish on fixed positive `lambda` compacta, the correct finite scaling is not `T` but `tT`.

The candidate limit is

\[
\boxed{
 t\mathcal T(t,\lambda)
\to
\frac\lambda2
\left[
2-\zeta\left(\frac12+\frac\lambda4\right)
\right].
}
\]

This identity is currently a theorem target, not yet promoted to PROVED. It must be supplied with a uniform explicit remainder and independently reconstructed.

## 4. Structural floor

Let `p0` satisfy `zeta(p0)=2` and

\[
\lambda_*=4(p_0-1/2)=4.914588956\ldots.
\]

The limiting triangle-envelope margin changes sign exactly at `lambda_*`.

Therefore:

- `lambda_*` is **not** a proved collision threshold;
- it is the natural structural floor of the unchanged `S0=1-A0` PSC mechanism;
- below it, finer interval subdivision cannot repair the fact that the asymptotic lower bound `S0` itself becomes nonpositive.

This is a structural stop condition for Track A.

## 5. Clean project ranking

### P0 — exact-weight Low Shoulder

**PRIMARY NOW.** Prove the exact-weight moment collapse, renormalized PSC limit, and one explicit small-time exclusion theorem above `lambda_*+epsilon`.

### P1 — compact certified bridge

After an explicit `t_epsilon` is obtained, cover the remaining compact strip up to `10.52` with 512/768-bit directed rounding.

### P2 — below-floor certificate invention

Only after the structural floor is rigorously established, test exact-head/convex-tail joint-jet and collision-conditioned phase-velocity mechanisms. Do not continue unchanged triangle PSC below its sign floor.

### P3 — prime-side all-orders factorization

Retain Rounds 48--61 as a parallel long-horizon program. It is higher-risk but potentially sparse-complete and may become the main route if no finite collision-side mechanism crosses the low-low shoulder.

## 6. Frozen/deprioritized mechanisms

Do not reopen without a material new input:

- raw global winding;
- ordinary Laguerre `L1` positivity;
- entropy/Vandermonde without an independent one-sided budget;
- raw/finite theta decomposition;
- generic log-concavity kernel arguments;
- weight-only Poincare upper bounds;
- finite moment hierarchy as a way to change an endpoint large-deviation exponent;
- pair-kernel generation of all connected prime cumulants.

## 7. Immediate next proof obligation

The next round must prove, or refute with an explicit obstruction, the following one-new-lemma target:

> **LS-A1.** On each compact `K subset (4,infinity)`, derive explicit uniform remainders for the true-weight limits of `A0` and `A1` under `x=4pi exp(lambda/t)`.

No new numerical machinery should be introduced before this analytic step is completed, because the current regression shows interval arithmetic is not the primary loss at the high-shoulder boundary.
