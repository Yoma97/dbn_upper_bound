# Round 49 — Sparse symmetric-pair amplification and the Montgomery-range barrier

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED SCALING BARRIER / SOURCE-GROUNDED / CONDITIONAL DETECTOR / NEW TOOL TARGET / NOVELTY UNVERIFIED.

## 0. Executive verdict

The unconditional RH-free pair-correlation function of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh already contains exactly the horizontal exponential weight one would want for sparse-exception amplification:

\[
F(x,T)
=\sum_{\rho,\rho'}x^{\rho-\rho'}w(\rho-\rho'),
\qquad
w(u)=\frac4{4-u^2}.
\]

For a functional-equation pair at the same ordinate,

\[
\rho_+=\frac12+\delta+i\gamma,
\qquad
\rho_-=\frac12-\delta+i\gamma,
\qquad 0<\delta<\frac12,
\]

the two cross-terms alone carry a positive hyperbolic factor

\[
\boxed{
\frac{2\cosh(2\delta\log x)}{1-\delta^2}.}
\]

Thus the statistic has the correct *formal* sparse amplifier.

However, the unconditional Montgomery theorem is currently proved only for `x=T^alpha` with `0<=alpha<=1`, with absolute error of order `T sqrt(log T)` after de-normalization. In that entire range a single fixed off-line pair contributes only

\[
T^{2\alpha\delta}=o(T),
\]

because `delta<1/2`. Therefore one isolated pair is asymptotically smaller than the known error throughout the proved range.

The first possible power-scale detection threshold is

\[
\boxed{\alpha>\frac1{2\delta}>1.}
\]

Hence sparse-exception elimination by this architecture requires **long-range RH-free pair correlation beyond alpha=1**, together with a positivity/localization theorem that prevents the amplified symmetric term from being cancelled by the rest of the double sum.

---

## 1. Primary source input

Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh define unconditionally

\[
\boxed{
F(x,T)
:=\sum_{\substack{\rho,\rho'\\0<\gamma,\gamma'\le T}}
 x^{\rho-\rho'}w(\rho-\rho'),
\qquad
w(u):=\frac4{4-u^2}.}
\]

The normalized function is

\[
F(\alpha)
:=\left(\frac{T}{2\pi}\log T\right)^{-1}F(T^\alpha,T).
\]

Their unconditional theorem gives, uniformly for `0<=alpha<=1`,

\[
\boxed{
F(\alpha)
=T^{-2\alpha}(\log T+O(1))
+\alpha
+O\!\left(\frac1{\sqrt{\log T}}\right).}
\]

They also prove that `F(alpha)` is real, even, and nonnegative. Importantly, this global nonnegativity comes from the exact square-integral representation

\[
F(x,T)
=\frac2\pi\int_{-\infty}^{\infty}
\left|
\sum_{0<\gamma\le T}
\frac{x^{\rho-1/2}}
{1-(\rho-(1/2+it))^2}
\right|^2dt.
\]

This is unconditional and does not place the zeros on the critical line.

The source also gives the de-normalized estimate, for `1<=x<=T`,

\[
F(x,T)
=\frac{T\log^2T}{2\pi x^2}(1+O(1/\log T))
+\frac{T}{2\pi}\log x
+O(T\sqrt{\log T}),
\]

up to harmless equivalent presentations of the first error term.

---

## 2. Exact symmetric same-ordinate contribution

Let

\[
\rho_+=\frac12+\delta+i\gamma,
\qquad
\rho_-=\frac12-\delta+i\gamma.
\]

For the ordered pair `(rho_+,rho_-)`,

\[
\rho_+-\rho_-=2\delta
\]

and hence

\[
x^{\rho_+-\rho_-}w(\rho_+-\rho_-)
=x^{2\delta}\frac4{4-4\delta^2}
=\frac{x^{2\delta}}{1-\delta^2}.
\]

The reverse ordered pair contributes

\[
\frac{x^{-2\delta}}{1-\delta^2}.
\]

Therefore the two cross-terms have the exact positive sum

\[
\boxed{
P_{\delta}(x)
:=\frac{x^{2\delta}+x^{-2\delta}}{1-\delta^2}
=\frac{2\cosh(2\delta\log x)}{1-\delta^2}.}
\]

For `x=T^alpha` and fixed `alpha,delta>0`,

\[
\boxed{
P_\delta(T^\alpha)
=\frac{T^{2\alpha\delta}}{1-\delta^2}
\left(1+T^{-4\alpha\delta}\right).}
\]

This is the desired horizontal exponential amplification.

---

## 3. Sparse-orbit range barrier

Let

\[
N_T:=\frac{T}{2\pi}\log T.
\]

The normalized theorem has error `O((log T)^(-1/2))`; hence the corresponding absolute uncertainty in `F(T^alpha,T)` is

\[
\boxed{O(T\sqrt{\log T}).}
\]

A necessary power-scale condition for a single fixed symmetric pair to dominate this uncertainty is

\[
T^{2\alpha\delta}
\gg T\sqrt{\log T}.
\]

Ignoring the logarithmic factor, this requires

\[
\boxed{2\alpha\delta>1.}
\]

Equivalently,

\[
\boxed{\alpha>\alpha_{\rm sparse}(\delta):=\frac1{2\delta}.}
\]

Since every non-trivial zero lies in the critical strip,

\[
0<\delta<\frac12,
\]

so

\[
\boxed{\alpha_{\rm sparse}(\delta)>1.}
\]

Thus the complete proven Montgomery range `0<=alpha<=1` lies strictly below the first possible sparse-single-orbit detection scale.

For a zero very close to the critical line (`delta<<1`), the required range becomes correspondingly very long: `alpha>>1/delta`.

---

## 4. Stronger comparison with the current error

At the endpoint `alpha=1`,

\[
P_\delta(T)
\asymp T^{2\delta}.
\]

For every fixed `delta<1/2`,

\[
\frac{P_\delta(T)}{T\sqrt{\log T}}
\asymp
\frac{T^{-(1-2\delta)}}{\sqrt{\log T}}
\longrightarrow0.
\]

Even if one supplements the critical-strip condition by the classical zero-free region near `Re s=1`, so that `delta<=1/2-eta(T)`, the endpoint contribution is at most

\[
T^{1-2\eta(T)},
\]

which remains below `T` by the corresponding zero-free-region saving and hence still below the present `T sqrt(log T)` error.

Therefore this is not merely a failure of a constant: the range/exponent is wrong for sparse detection.

---

## 5. Critical positivity caveat

The previous section compares the magnitude of the **explicit symmetric-pair sub-sum** with the known global error. It does **not** prove a lower bound

\[
F(x,T)\ge P_\delta(x).
\]

Although `F(x,T)>=0` globally, its original double-sum expansion is not termwise nonnegative. Other pair terms can have complex phases and can cancel the symmetric-pair contribution.

The square-integral representation proves positivity only after the entire zero sum is assembled.

Therefore two independent obstacles remain:

1. **range:** current unconditional control stops at `alpha=1`, while a fixed pair requires `alpha>1/(2delta)`;
2. **localization/positivity:** one must isolate the same-ordinate symmetric pair inside a positive statistic rather than merely identify a positive term inside a non-termwise-positive expansion.

Both are mandatory. Solving only one does not eliminate a sparse orbit.

---

## 6. Relation to horizontal-distribution pair-correlation work

Recent pair-correlation work does obtain horizontal information by inserting a complex Fourier/Tsang kernel whose real part is positive for pairs lying in a prescribed narrow vertical box. This permits the diagonal and the functional-equation symmetric diagonal to be retained as positive lower-bound terms and yields positive-proportion results for zeros on the critical line.

But this architecture is not currently a sparse-exception theorem:

- the positivity region is guaranteed by a narrow-box assumption on **all** zeros under consideration;
- each off-line symmetric pair contributes only a bounded amount in the narrow-box scaling;
- the resulting theorem controls a proportion of off-line zeros, not the existence of one exceptional orbit.

Thus the new horizontal pair-correlation results validate the *mechanism* of symmetric-diagonal extraction, but not sparse-single-orbit elimination.

---

## 7. New mathematical tool exposed

A pair-correlation closure of RH would require a new theorem with both components:

### PC-A — long-range RH-free Montgomery theorem

For `x=T^alpha` in a range extending beyond

\[
\alpha>\frac1{2\delta},
\]

obtain an unconditional explicit-formula evaluation with an error `o(T^{2 alpha delta})` for the target orbit scale.

For arbitrarily small `delta`, a fixed finite alpha range cannot be complete. A genuinely sparse-complete theorem must therefore either have an adaptive/unbounded alpha parameter or amplify `delta` by another mechanism.

### PC-B — positive symmetric-pair localization

Construct a positive semidefinite / sum-of-squares / positive-real-part transform for which the contribution of

\[
(\rho,1-\rho)
\]

is bounded below by a quantity comparable to

\[
\cosh(2\delta\alpha\log T),
\]

without assuming beforehand that all zeros lie in a `O(1/log T)` box around the critical line.

The present global positivity of `F` is insufficient because it does not localize individual pair contributions.

---

## 8. Program decision

- Standard equal-ordinate counting / bounded kernels: **INSUFFICIENT for sparse exceptions**; one orbit contributes `O(1)`.
- RH-free Montgomery `F` with horizontal exponential weight: **VALID DETECTOR ARCHITECTURE**.
- Current proved range `alpha<=1`: **PROVED INSUFFICIENT for one fixed off-line pair**.
- Long-range plus localization: **NEW TOOL REQUIRED**.

The immediate next round should attack PC-B first: determine whether Tsang/positive-real-part kernels can preserve `T^{2 alpha delta}` amplification while guaranteeing positivity for every possible horizontal zero displacement, or whether a quantitative positivity--amplification uncertainty principle rules this out.

**No proof of RH is claimed. Novelty of the sparse-range packaging is unverified.**