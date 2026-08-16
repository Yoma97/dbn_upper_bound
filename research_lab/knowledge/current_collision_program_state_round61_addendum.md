# Collision Program State — Round 61 addendum

**Date:** 2026-08-16

**RH status:** OPEN.

## Executive update

Rounds 48--61 move the project from local heat-collision identities into a sharply defined sparse-exception / explicit-formula program.

The main achievement is not an RH proof. It is a sequence of reductions and no-go theorems that identify where genuinely new mathematics is required.

The current architecture is:

\[
\boxed{
\text{off-line orbit}
\longrightarrow
\text{amplified Hermitian spectral defect}
\longrightarrow
\text{prime-side connected/variance statistic}.}
\]

The zero-side localization problem has been solved in one important sense by Round 53. The remaining difficulty is arithmetic cancellation. Several apparently simpler prime-side closures have now been proved RH-strength or structurally insufficient.

---

## 1. Round 48 — height-adaptive modified Li amplifier

For

\[
a=\frac12-h,
\qquad
\rho=\frac12+\delta+i\gamma,
\]

the modified-Li Möbius factor has logarithmic amplitude

\[
A(h)
=\frac12\log
\frac{(h+\delta)^2+\gamma^2}
{(h-\delta)^2+\gamma^2}.
\]

The unique maximizer is

\[
\boxed{h_*=\sqrt{\gamma^2+\delta^2}},
\]

and

\[
A(h_*)
=\operatorname{artanh}
\frac{\delta}{\sqrt{\gamma^2+\delta^2}}
=\frac\delta\gamma+O(\delta^3/\gamma^3).
\]

Thus the adaptive modified-Li amplification scale is

\[
\boxed{n\asymp\gamma/\delta},
\]

one factor `gamma` better than standard Li.

But the exact conformal disk theorem proves that any Jensen disk whose reflected image stays wholly inside `Re s>1` misses every non-trivial zero in the critical strip. Hence absolute Euler-product convergence cannot close the amplifier.

**Status:** detector PROVED; absolute-Euler-product closure REFUTED.

---

## 2. Rounds 49--50 — pair amplification and positivity-bandwidth barrier

The RH-free pair-correlation function

\[
F(x,T)
=\sum_{\rho,\rho'}x^{\rho-\rho'}w(\rho-\rho')
\]

contains for a same-ordinate functional pair `1/2+-delta+i gamma` the exact positive cross contribution

\[
\boxed{
\frac{2\cosh(2\delta\log x)}{1-\delta^2}.}
\]

Thus the correct sparse power amplifier exists formally.

However, the published unconditional Montgomery range is `x=T^alpha`, `alpha<=1`. A single orbit requires power scale

\[
2\alpha\delta>1,
\]

hence `alpha>1/(2delta)>1` before it can exceed the present absolute error.

Round 50 then proves a positivity--amplification uncertainty principle for Tsang-type scalar kernels: widening the strip of termwise positivity to cover arbitrary horizontal zero differences forces the Fourier scale down to `alpha=O(1/log T)`, reducing polynomial amplification to `O_delta(1)`.

**Status:** current scalar long-range + positivity architecture insufficient.

---

## 3. Round 51 — exact horizontal variance and holomorphic no-go

For a finite zero window,

\[
\boxed{
\mathcal V(T)
=\sum_{0<\gamma\le T}m_\rho
\left(\beta-\frac12\right)^2}
\]

is an ideal positive sparse-complete horizontal defect.

It appears as the second derivative at zero of the difference between the true horizontal generating function and its projection to the critical line.

But exact horizontal projection depends on `Re z` and cannot be realized by a nonconstant one-variable holomorphic test on an open strip. Thus ordinary scalar Guinand--Weil testing cannot implement the desired projection exactly.

**Status:** Hermitian/two-variable explicit formula required.

---

## 4. Round 52 — Gram diagonal contains the amplifier

The RH-free pair statistic is an exact Gram norm

\[
F(x,T)
=\left\|\sum_\rho v_{\rho,x}\right\|_2^2,
\]

with

\[
\boxed{
\|v_{\rho,x}\|^2
=\frac{x^{2\delta}}{1-\delta^2}.}
\]

So positive horizontal amplification already sits on the Gram diagonal.

A uniform fixed-width Riesz lower bound is impossible because nearby zero ordinates give almost collinear kernel vectors. In the Lorentzian model,

\[
\boxed{
r_\eta(d)=\frac{4\eta^2}{d^2+4\eta^2}},
\]

so the smallest two-vector Gram eigenvalue is

\[
\frac{d^2}{d^2+4\eta^2}.
\]

At zero spacing `d=O(1/log T)`, any fixed-width frame constant degenerates at least polylogarithmically.

This route was subsequently demoted by Round 53.

---

## 5. Round 53 — extremal Laplace--Cesaro projection solves zero-side localization

Fix `T` and define

\[
\delta_*(T)
:=\max_{0<\gamma\le T}
\left(\beta-\frac12\right).
\]

Then

\[
\boxed{
\lim_{A\to\infty}\frac1A\int_0^A
T^{-2\alpha\delta_*}F(T^\alpha,T)d\alpha
=
\frac1{1-\delta_*^2}
\sum_{\substack{\rho:\delta=\delta_*\\0<\gamma\le T}}
 m_\rho^2>0.}
\]

Hence

\[
\boxed{
\delta_*(T)
=\frac12\limsup_{\alpha\to\infty}
\frac{\log F(T^\alpha,T)}{\alpha\log T}.}
\]

Laplace normalization removes all smaller horizontal exponents; Cesaro averaging dephases distinct maximal ordinates. No zero separation, narrow-box assumption, or frame lower bound is required.

**Status:** PC-B zero-side sparse localization SOLVED spectrally.

**Circularity warning:** the resulting growth criterion is RH-equivalent at finite height and is not itself a proof.

---

## 6. Rounds 54--55 — prime/pole cancellation, correction, and Mellin resolvent

The triangular prime polynomial is

\[
P_x(t)
=\sum_n\frac{\Lambda(n)}{n^{1/2+it}}W(n/x),
\qquad
W(y)=\min(y,y^{-1}).
\]

The exact pole term is

\[
\boxed{
I_x(t)
=x^{1/2-it}
\left(
\frac1{3/2-it}+\frac1{1/2+it}
\right),}
\]

and exactly equals the continuous prime main term obtained by replacing `d psi` with `du`.

Thus

\[
E_x(t)=P_x(t)-I_x(t)
\]

is a centered PNT Mellin transform.

### Important correction to the original Round-54 wording

The complete `O(x)` barrier in the published finite-height pair-correlation proof does **not** arise only from pole/prime separation. There is an independent `O(x)` error when the all-zero resolvent is truncated at `Z=T log^2 T` and converted to the finite zero window; a zero-free-region-dependent term also appears.

So there are two obstacles:

\[
\boxed{\text{prime/pole long mean square}}
\]

and

\[
\boxed{\text{zero-window transfer}}.
\]

Round 55 proves the exact Mellin identity

\[
\boxed{
\int_0^\infty x^{-z-1}P_x(t)dx
=-\frac2{1-z^2}
\frac{\zeta'}{\zeta}\!\left(\frac12+it+z\right),
\qquad\frac12<\Re z<1.}
\]

The pole term is exactly the residue at `z=1/2-it`; nontrivial zeros become the next Mellin poles at

\[
z=\rho-(1/2+it),
\]

whose real parts are `beta-1/2`.

Therefore direct linear continuation of the pole-subtracted transform through `Re z>0` is RH-strength. The legitimate opportunity is quadratic/mean-square arithmetic structure.

---

## 7. Round 56 — holomorphic soft height window

To avoid the hard zero-window transfer entirely, define

\[
\boxed{
h_{c,L}(z)=e^{-cLz^2+iLz}.}
\]

For

\[
z_\rho=\gamma-i\delta,
\]

the real exponential score is

\[
\boxed{
q_c(\rho)=\delta-c(\gamma^2-\delta^2).}
\]

For fixed `c>0`, the maximum is attained by finitely many zeros because of the quadratic height penalty.

RH implies `q_*(c)<0` for every `c`; any off-line zero makes `q_*(c)>0` for sufficiently small `c`.

The Fourier transform is

\[
\boxed{
\widehat h_{c,L}(u)
=\sqrt{\frac\pi{cL}}
\exp\left(-\frac{(u-L)^2}{4cL}\right).}
\]

Thus the hard zero cutoff is replaced by a Gaussian log-prime window.

But classical unconditional PNT error estimates leave the continuous prime saddle exponent essentially at the `Re s=1` scale, which is larger than any zero displacement `delta<1/2`. Hence a new Gaussian-centered prime cancellation theorem would be required.

**Status:** ZWT avoidable by redesign; arithmetic cancellation still open.

---

## 8. Round 57 — Selberg variance dictionary

For a dyadic prime block `n asy X` and vertical averaging length `T`, Gallagher's frequency-window principle associates

\[
\boxed{H=X/T.}
\]

At the scaling level,

\[
\boxed{
\int_{-T}^{T}|E_X(t)|^2dt
\ll\frac{T^2}{X^2}J(X,H),}
\]

where

\[
J(X,H)=\int_X^{2X}|\psi(u+H)-\psi(u)-H|^2du.
\]

If

\[
J(X,H)\ll H^{2-\kappa}X^{1+o(1)},
\]

then

\[
\boxed{
\int|E_X|^2
\ll T^\kappa X^{1-\kappa+o(1)}.}
\]

For `X=T^alpha`, the `X`-exponent is

\[
\boxed{
\theta_\kappa(\alpha)=1-\kappa+\kappa/\alpha.}
\]

A sparse pair signal `X^{2delta}` can beat this only if

\[
2\delta>\theta_\kappa(\alpha).
\]

Thus any fixed `kappa<1` can at best exclude

\[
\delta>(1-\kappa)/2.
\]

Sparse completeness requires essentially the full `kappa=1` interval-length saving.

Modern unconditional almost-all short-interval theorems must not be confused with this global `L^2` requirement.

---

## 9. Round 58 — homogeneous higher amplification no-go

Taking fixed powers, tensor powers, or replacing `X` by `X^r` does not improve the exponent threshold: signal and available bound are both multiplied by `r` in the exponent.

Thus naive higher moments cannot compensate for a fixed `kappa<1` variance saving.

Polynomial conformal amplification returns to the modified-Li architecture of Round 48.

A genuine improvement must remove disconnected arithmetic background before estimation.

---

## 10. Round 59 — sparse-complete Poisson variance is RH-strength

Let

\[
R(x)=\psi(x)-x.
\]

For any fixed `lambda>1`, if one had for every `epsilon>0`

\[
\boxed{
\int_X^{2X}|R(\lambda x)-R(x)|^2dx
\ll_{\lambda,\epsilon}X^{2+\epsilon},}
\]

then RH would follow.

The proof uses the Mellin transform

\[
M_R(s)
=-\frac1s\frac{\zeta'}{\zeta}(s)-\frac1{s-1}
\]

and the multiplier `lambda^s-1`, which has no zeros in `Re s>0`. The `L^2` bound analytically continues the centered PNT transform to `Re s>1/2`, excluding off-line zeros.

Therefore the final sparse-complete Poisson-scale variance is itself an RH-strength endpoint and should not be promoted as an unexplained missing lemma.

**Consequence:** direct PSV remains useful for partial zero-free bands, but a satisfactory proof architecture needs a lower-level structural reason.

---

## 11. Rounds 60--61 — connected cumulants: real amplification, all-orders barrier

Connected `2r`-point statistics can in principle escape the homogeneous no-go. A balanced off-line conjugate pair can produce a phase-free spectral monomial of size

\[
\boxed{X^{2r\delta}.}
\]

If the connected arithmetic background grew sublinearly in `r`, increasing `r` could detect arbitrarily small `delta`.

But order-by-order implementation requires centered prime correlations of order `2r`.

Round 61 proves the first obstruction at order four. The fourth cumulant contains the irreducible term

\[
\sum_n\prod_{j=1}^4(\Lambda(n+h_j)-1)
\]

minus the three pair contractions. Pair covariance does not determine this term; abstractly, Gaussian and Rademacher fields can have identical covariance and different fourth cumulants.

Thus

\[
\boxed{
\text{pair data alone cannot generate the connected hierarchy}.}
\]

Montgomery--Soundararajan's Gaussian short-interval program is consistent with this: high moments rely on strong high-order prime-correlation input.

---

## 12. Current new-tool map

### Tool A — fractional Selberg/long-DP variance

**LEGITIMATE PARTIAL TARGET.** A fixed `kappa>0` saving could yield a genuine horizontal zero-free band.

It is not sparse-complete unless `kappa` tends to 1.

### Tool B — full Poisson-scale variance

**RH-STRENGTH ENDPOINT.** Do not treat it as an independent final lemma without a lower-level proof mechanism.

### Tool C — Gaussian-window prime cancellation

**OPEN.** Avoids hard zero truncation, but requires centered prime cancellation at a stronger exponential scale than classical pointwise PNT estimates provide.

### Tool D — connected-correlation explicit formula

**AMPLIFICATION MECHANISM VALID IN PRINCIPLE.** Order-by-order closure becomes all-prime-tuples. Pair data fail already at fourth order.

### Tool E — arithmetic all-orders factorization/operator

**HIGHEST INVENTION PRIORITY.** Find one prime-side structural theorem that generates or controls connected correlations of all orders without assuming the Hardy--Littlewood hierarchy.

Possible forms:

- Euler/local-prime cluster generator with rigorous global coupling correction;
- trace/Fredholm determinant from an arithmetic operator;
- convergent cluster expansion;
- martingale/dependency decomposition;
- Hermitian explicit-formula factorization with a contraction estimate independent of RH.

Every proposal must be audited to ensure it is not merely Euler-product analytic continuation, Weil positivity, modified Li, or an all-orders prime-tuple conjecture under new notation.

---

## 13. Current ranking

The project ranking is now

\[
\boxed{
E\;\gtrsim\;A_{\rm partial}\;\gtrsim\;C\;>\;D_{\rm order-by-order}
}
\]

in terms of **invention value**, where

- `E` = one finite all-orders arithmetic factorization/operator;
- `A_partial` = fractional Selberg/long-DP variance giving partial zero-free bands;
- `C` = soft Gaussian prime-cancellation bridge;
- `D_order-by-order` = explicit high-prime-tuple cumulants, demoted because complexity grows without bound.

The old local heat routes remain valuable diagnostics but are not the primary invention target.

---

## 14. Immediate next experiment

Do **not** start by postulating an operator with spectrum equal to zeta zeros; that would simply encode the goal.

Start prime-side.

The smallest admissible all-orders experiment is:

> construct a generating functional for smoothed centered prime counts from local prime/divisor variables, take its logarithm, and test whether the fourth connected coefficient agrees with the true `Lambda` fourth cumulant up to an error that is controlled by existing sieve/dispersion theorems.

If the mismatch is already main-order at fourth degree, naive Euler/local independence is refuted and the missing global-coupling correction is identified explicitly.

A parallel lower-risk branch may seek a fractional `kappa>0` Selberg-variance saving for the exact triangular/Gaussian weights, because even a partial horizontal zero-free band would be a genuine theorem and would provide a testbed for the new machinery.

**No proof of RH is claimed. Novelty remains unverified.**