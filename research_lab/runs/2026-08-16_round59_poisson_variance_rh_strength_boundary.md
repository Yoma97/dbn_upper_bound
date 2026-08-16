# Round 59 — The sparse-complete Poisson-variance endpoint is itself RH-strength

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED CIRCULARITY BOUNDARY / MELLIN ARGUMENT / TOOL-SELECTION CORRECTION / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 57 identified essentially Poisson-scale variance as the strength needed for sparse completeness in the second-moment architecture. This round shows why such a target must be treated with extreme care:

> a natural multiplicative long-interval `L^2` bound at the Poisson/Cramer scale already implies RH.

Let

\[
R(x):=\psi(x)-x.
\]

Fix any `lambda>1`. If, for every `epsilon>0`, one could prove unconditionally

\[
\boxed{
\int_X^{2X}|R(\lambda x)-R(x)|^2dx
\ll_{\lambda,\varepsilon}X^{2+\varepsilon},}
\]

then RH would follow.

The proof is short and rigorous: the `L^2` estimate analytically continues the Mellin transform of the multiplicative PNT difference into `Re s>1/2`; the multiplier `lambda^s-1` has no zeros there; hence the centered PNT Mellin transform continues to that half-plane; but its poles are precisely nontrivial zeros of `zeta`.

Therefore “prove the full Poisson-scale variance needed by Round 57” is **not by itself an acceptable new-tool specification**. In the sparse-complete limit it risks being merely RH rewritten on the prime side.

A useful new theorem must have an independently motivated structural mechanism, a weaker premise, or an application beyond zero-freeness. This increases the relative priority of a connected/cumulant or factorized explicit-formula construction.

---

## 1. Centered PNT Mellin transform

For `Re s>1`, Stieltjes integration gives

\[
\int_1^\infty\psi(x)x^{-s-1}dx
=\frac1s\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=-\frac1s\frac{\zeta'}{\zeta}(s).
\]

Also

\[
\int_1^\infty x\,x^{-s-1}dx
=\frac1{s-1}.
\]

Hence

\[
\boxed{
M_R(s)
:=\int_1^\infty R(x)x^{-s-1}dx
=-\frac1s\frac{\zeta'}{\zeta}(s)
-\frac1{s-1}.}
\]

The pole at `s=1` cancels in this combination. Nontrivial zeros of `zeta` appear as poles of `M_R`.

---

## 2. Multiplicative difference

Fix `lambda>1` and define

\[
\boxed{
\Delta_\lambda R(x):=R(\lambda x)-R(x).}
\]

Let

\[
M_{\Delta,\lambda}(s)
:=\int_1^\infty\Delta_\lambda R(x)x^{-s-1}dx.
\]

For `Re s>1`, changing variables `y=lambda x` gives

\[
\begin{aligned}
\int_1^\infty R(\lambda x)x^{-s-1}dx
&=\lambda^s\int_\lambda^\infty R(y)y^{-s-1}dy\\
&=\lambda^sM_R(s)
-\lambda^sB_\lambda(s),
\end{aligned}
\]

where

\[
B_\lambda(s):=\int_1^\lambda R(y)y^{-s-1}dy
\]

is entire in `s`.

Therefore

\[
\boxed{
M_{\Delta,\lambda}(s)
=(\lambda^s-1)M_R(s)-\lambda^sB_\lambda(s).}
\]

---

## 3. `L^2` bound gives analytic continuation

Assume that for every `epsilon>0`,

\[
\boxed{
\int_X^{2X}|\Delta_\lambda R(x)|^2dx
\ll_{\lambda,\varepsilon}X^{2+\varepsilon}.}
\]

Fix `sigma>1/2`. Choose `epsilon>0` so small that

\[
\sigma>\frac12+\frac\varepsilon2.
\]

On a dyadic block `[X,2X]`, Cauchy--Schwarz gives

\[
\begin{aligned}
\int_X^{2X}|\Delta_\lambda R(x)|x^{-\sigma-1}dx
&\le
\left(\int_X^{2X}|\Delta_\lambda R(x)|^2dx\right)^{1/2}
\left(\int_X^{2X}x^{-2\sigma-2}dx\right)^{1/2}\\
&\ll
X^{1+\varepsilon/2}X^{-\sigma-1/2}\\
&=X^{1/2-\sigma+\varepsilon/2}.
\end{aligned}
\]

The exponent is negative. Summing over dyadic blocks proves absolute and locally uniform convergence of

\[
M_{\Delta,\lambda}(s)
\]

throughout

\[
\boxed{\Re s>1/2.}
\]

Thus `M_Delta,lambda` is holomorphic there.

---

## 4. Recovering the centered PNT transform

From

\[
M_{\Delta,\lambda}(s)
=(\lambda^s-1)M_R(s)-\lambda^sB_\lambda(s),
\]

we have

\[
\boxed{
M_R(s)
=\frac{M_{\Delta,\lambda}(s)+\lambda^sB_\lambda(s)}{\lambda^s-1}.}
\]

If

\[
\lambda^s=1,
\]

then

\[
\Re s=0.
\]

Hence the denominator has no zeros in `Re s>1/2`. Therefore `M_R(s)` extends holomorphically throughout that half-plane.

---

## 5. Deduction of RH

For `Re s>1`,

\[
M_R(s)
=-\frac1s\frac{\zeta'}{\zeta}(s)-\frac1{s-1}.
\]

The right side is meromorphic wherever `zeta` is meromorphic; every nontrivial zero of `zeta` is a pole of `zeta'/zeta` and hence of `M_R`.

But Section 4 shows that `M_R` is holomorphic in

\[
\Re s>1/2.
\]

Thus there are no nontrivial zeros with

\[
\Re\rho>1/2.
\]

The functional equation then excludes zeros with `Re rho<1/2`. Hence all nontrivial zeros lie on the critical line.

Therefore

\[
\boxed{
\text{the multiplicative Poisson-scale }L^2\text{ bound above implies RH}.}
\]

---

## 6. Relation to Round 57

For `X=T^alpha`, the natural Gallagher interval is

\[
H=X/T=X^{1-1/\alpha}.
\]

Sparse detection for increasingly small horizontal displacement requires larger and larger `alpha`, so

\[
H=X^{1-o(1)}.
\]

Thus the full-saving endpoint of the Round-57 variance program naturally approaches the long-interval/global-PNT regime in which the theorem above applies.

This explains conceptually why the required `kappa=1` saving felt qualitatively different from any fixed fractional saving: it reaches RH-strength mean-square control.

---

## 7. What is still legitimate

The theorem does **not** say that every useful variance improvement is circular.

Legitimate targets include:

- a fractional `kappa<1` saving, which would yield a genuine zero-free horizontal band but not full RH;
- Poisson-scale variance only for a restricted family of structured weights, provided the theorem has an independent proof and does not automatically recover the full multiplicative PNT difference;
- a factorization theorem that derives the needed cancellation from a separate positive/orthogonal structure;
- a connected/cumulant statistic in which the RH-strength background is removed algebraically before estimation.

The rejection rule is narrower:

> do not promote the final sparse-complete Poisson-scale PNT variance itself as the missing lemma without an independent lower-level mechanism.

---

## 8. Tool-selection consequence

After Rounds 57--59, the two candidate tool families are no longer symmetric.

### Direct PSV/GWPC

Mathematically clean, but its sparse-complete endpoint is RH-strength. It is useful as a **benchmark** and for partial zero-free regions, not as a satisfactory unexplained final lemma.

### Connected-Correlation Explicit Formula (CCEF)

More structurally promising because it seeks to remove disconnected/PNT background algebraically before invoking a bound. If successful, its required estimate might be genuinely weaker than the final RH-equivalent variance.

Therefore CCEF should now receive the higher invention priority.

---

## 9. Immediate next target

Construct the **lowest-complexity connected object** beyond the centered second moment.

The first candidate should not jump directly to arbitrary prime `k`-tuples. It should start with a two-scale or three-point cumulant whose disconnected pieces are explicitly computable from the PNT and pair correlations.

Promotion criterion:

1. off-line spectral displacement produces a nonzero connected term with an amplifiable sign/norm;
2. the continuous prime/PNT saddle cancels algebraically;
3. the remaining arithmetic object is an averaged correlation strictly weaker than a full Hardy--Littlewood `k`-tuple conjecture;
4. the construction has an application to another long Dirichlet-polynomial or prime-variance problem.

If the lowest connected object already requires full prime triples, that should be recorded as a no-go and the program should pivot again.

**No proof of RH is claimed. Novelty remains unverified.**