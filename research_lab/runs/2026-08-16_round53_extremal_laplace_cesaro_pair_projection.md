# Round 53 — Extremal Laplace–Cesàro projection: exact sparse isolation on the zero side

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED FINITE-HEIGHT SPECTRAL THEOREM / POSITIVE ISOLATION / PRIME-SIDE GAP / NOVELTY UNVERIFIED.

## 0. Executive verdict

Rounds 49--52 treated sparse horizontal amplification as a long-range pair-correlation problem and worried that destructive Gram interference might prevent one off-line orbit from being isolated.

This round removes that second obstacle **exactly on the zero side**.

For fixed `T`, let

\[
\delta_*(T)
:=\max_{\substack{\rho=1/2+\delta+i\gamma\\0<\gamma\le T}}\delta.
\]

By functional-equation symmetry `delta_*>=0`, and

\[
\delta_*(T)=0
\iff
\text{all zeros with }0<\gamma\le T\text{ lie on the critical line}.
\]

Then the RH-free Gram pair-correlation function satisfies the exact extremal projection law

\[
\boxed{
\lim_{A\to\infty}
\frac1A\int_0^A
T^{-2\alpha\delta_*}
F(T^\alpha,T)\,d\alpha
=
\frac1{1-\delta_*^2}
\sum_{\substack{\rho:\,\delta=\delta_*\\0<\gamma\le T}}
 m_\rho^2>0.}
\]

Thus Laplace normalization in the horizontal displacement and Cesàro averaging in the long pair-correlation parameter automatically perform three tasks:

1. suppress every zero with smaller horizontal displacement;
2. dephase maximal zeros at distinct ordinates;
3. retain only the positive diagonal mass of the extremal horizontal layer.

No narrow box, zero separation, Riesz lower bound, or termwise positivity is needed.

Equivalently,

\[
\boxed{
\delta_*(T)
=rac12\limsup_{\alpha\to\infty}
\frac{\log F(T^\alpha,T)}{\alpha\log T}.}
\]

Therefore the **localization/positivity problem PC-B is solved spectrally**. The remaining obstruction is purely arithmetic: obtain a prime-side long-range upper bound for `F` strong enough to contradict positive horizontal growth.

---

## 1. Setup

Use the exact unconditional Gram representation

\[
F(x,T)
=\frac2\pi\int_{\mathbb R}
\left|
\sum_{\substack{\rho=1/2+\delta+i\gamma\\0<\gamma\le T}}
\frac{x^{\delta+i\gamma}}
{1+((t-\gamma)+i\delta)^2}
\right|^2dt.
\]

For fixed `T`, only finitely many zeros occur in the sum. Group multiplicities at identical zero locations.

Write

\[
q_\rho(t)
:=\sqrt{\frac2\pi}
\frac1{1+((t-\gamma)+i\delta)^2}.
\]

Then

\[
F(T^\alpha,T)
=\left\|
\sum_\rho
m_\rho T^{\alpha(\delta+i\gamma)}q_\rho
\right\|_2^2.
\]

Expanding the norm,

\[
F(T^\alpha,T)
=\sum_{\rho,\rho'}
 m_\rho m_{\rho'}
 T^{\alpha(\delta+\delta')}
 e^{i\alpha(\gamma-\gamma')\log T}
 \langle q_\rho,q_{\rho'}\rangle.
\]

---

## 2. Extremal normalization

Let

\[
\delta_*:=\max_\rho\delta.
\]

Define

\[
\boxed{
G_T(\alpha)
:=T^{-2\alpha\delta_*}F(T^\alpha,T).}
\]

Then

\[
G_T(\alpha)
=\sum_{\rho,\rho'}
 m_\rho m_{\rho'}
 T^{\alpha(\delta+\delta'-2\delta_*)}
 e^{i\alpha(\gamma-\gamma')\log T}
 \langle q_\rho,q_{\rho'}\rangle.
\]

Since `delta,delta'<=delta_*`, every real exponential rate is nonpositive.

Equality of the rate with zero occurs iff

\[
\delta=\delta'=\delta_*.
\]

---

## 3. Cesàro elimination lemma

For a complex number `c+i omega` with `c<=0`,

\[
\frac1A\int_0^A e^{(c+i\omega)\alpha}\,d\alpha
\longrightarrow
\begin{cases}
1,&c=0,\ \omega=0,\\
0,&\text{otherwise}.
\end{cases}
\]

Indeed, for `c<0` the integral stays bounded while `A` grows; for `c=0,omega!=0` it is an ordinary Cesàro average of a nonconstant exponential.

Apply this termwise to the finite Gram expansion, with

\[
c=(\delta+\delta'-2\delta_*)\log T,
\qquad
\omega=(\gamma-\gamma')\log T.
\]

All terms vanish except those satisfying simultaneously

\[
\delta=\delta'=\delta_*,
\qquad
\gamma=\gamma'.
\]

Distinct zeros with the same `delta` and `gamma` are just multiplicity copies and have already been grouped into `m_rho`.

Therefore

\[
\boxed{
\lim_{A\to\infty}\frac1A\int_0^A G_T(\alpha)d\alpha
=\sum_{\substack{\rho:\delta=\delta_*}}
 m_\rho^2\|q_\rho\|_2^2.}
\]

---

## 4. Exact diagonal norm

From the Hermitian diagonal of the RH-free pair-correlation kernel,

\[
\|q_\rho\|_2^2
=w(2\delta)
=\frac4{4-4\delta^2}
=\frac1{1-\delta^2}.
\]

Hence for every maximal-displacement zero,

\[
\|q_\rho\|_2^2
=\frac1{1-\delta_*^2}.
\]

This proves

\[
\boxed{
\lim_{A\to\infty}
\frac1A\int_0^A
T^{-2\alpha\delta_*}F(T^\alpha,T)d\alpha
=
\frac1{1-\delta_*^2}
\sum_{\substack{\rho:\delta=\delta_*}}
 m_\rho^2.}
\]

The right side is strictly positive.

---

## 5. Growth-exponent corollary

A trivial finite-dimensional upper bound gives

\[
F(T^\alpha,T)\ll_T T^{2\alpha\delta_*}.
\]

Thus

\[
\limsup_{\alpha\to\infty}
\frac{\log F(T^\alpha,T)}{\alpha\log T}
\le2\delta_*.
\]

On the other hand, the positive Cesàro limit implies that for arbitrarily large `alpha`,

\[
T^{-2\alpha\delta_*}F(T^\alpha,T)\ge c_T>0.
\]

Hence the reverse limsup inequality holds, and therefore

\[
\boxed{
\delta_*(T)
=\frac12\limsup_{\alpha\to\infty}
\frac{\log F(T^\alpha,T)}{\alpha\log T}.}
\]

This is an exact finite-height spectral-abscissa formula.

---

## 6. Sparse completeness

If a single off-line orbit exists below height `T`, then functional symmetry gives a right-half zero and hence

\[
\delta_*(T)>0.
\]

The long-range pair-correlation growth exponent is then strictly positive.

Conversely, if all zeros below height `T` lie on the critical line, then `delta_*(T)=0`, and the exponential growth rate is zero.

Thus

\[
\boxed{
\text{RH up to height }T
\iff
\limsup_{\alpha\to\infty}
\frac{\log F(T^\alpha,T)}{\alpha\log T}=0.}
\]

**Circularity warning:** this equivalence is not by itself progress toward RH. Its value is that it isolates a positive long-range statistic whose growth rate detects the rightmost zero without requiring zero separation.

---

## 7. Why this resolves the cancellation problem from Rounds 49--52

Round 49 warned that the explicit symmetric-pair term need not lower-bound the entire pair sum.

Round 52 warned that raw Gram vectors can be badly conditioned.

The extremal Laplace--Cesàro projection bypasses both issues:

- smaller horizontal exponents are eliminated by Laplace normalization;
- equal maximal exponents at different ordinates are eliminated by Cesàro dephasing;
- tight vertical clusters do not require a uniform frame bound;
- multiplicity at one location contributes positively as `m_rho^2`.

Therefore **no new zero-side localization theorem is needed for extremal displacement**.

This materially simplifies the P0 program.

---

## 8. The remaining prime-side gap

The existing unconditional Montgomery theorem controls only

\[
x\le T
\quad(\alpha\le1).
\]

More generally, the explicit-formula comparison used to prove it contains errors such as `O(x)` and zero-free-region-dependent powers. For an off-line zero,

\[
2\delta_*<1,
\]

so the desired signal

\[
x^{2\delta_*}
\]

is smaller than the crude `O(x)` long-range error.

Thus the current prime-side machinery is too weak exactly where the extremal projection becomes decisive.

This is not a positivity problem anymore. It is a **long-range explicit-formula cancellation problem**.

---

## 9. Relation to extended pair-correlation literature

Long-range pair-correlation bounds are already recognized as substantially stronger input in the literature. Work on extended pair-correlation conjectures studies bounds such as

\[
F(x,T)\ll T\log x
\]

in ranges extending far beyond `x=T`; such hypotheses imply improvements in prime-number-theorem error terms.

Those results are generally formulated under RH or as conjectural long-range input. The present project needs an RH-free analogue strong enough to control the **horizontal-weighted** `F` used here.

The extremal projection explains why such a theorem would have direct zero-location force: a uniform bound of sufficiently slow growth in `x` is incompatible with any positive `delta_*`.

---

## 10. New-tool target after Round 53

The required new mathematics has now narrowed to one principal object.

### LREF — Long-Range RH-Free Explicit Formula

Develop an unconditional estimate for

\[
F(x,T)
=\sum_{\rho,\rho'}x^{\rho-\rho'}w(\rho-\rho')
\]

or its exact Gram equivalent, in a range `x>>T`, with error/growth exponent strictly below the spectral signal generated by a hypothetical rightmost zero.

A sparse-complete version should imply, for every fixed `T`, something of the schematic form

\[
\boxed{
F(x,T)\le x^{o(1)}C(T)
\qquad(x\to\infty),}
\]

or a weaker adaptive estimate sufficient to force

\[
\limsup_{x\to\infty}\frac{\log F(x,T)}{\log x}=0.
\]

By the theorem above, that would force `delta_*(T)=0`.

But proving such a bound from current prime technology is a genuinely new problem; the known `O(x)` error is far too large.

---

## 11. Program decision

- PC-B positive sparse localization: **SOLVED on the zero side by extremal Laplace--Cesàro projection**.
- Raw Riesz/frame route: **DEMOTED; no longer required for extremal displacement**.
- PC-A long-range RH-free arithmetic control: **NOW THE SINGLE MAIN PAIR-CORRELATION GAP**.
- New mathematical tool required: **LREF**, not another scalar positivity kernel.

The immediate next round should dissect the `O(x)` term in the RH-free explicit-formula proof and determine whether it is structural or merely a truncation/absolute-value artifact. If it is structural, identify the smallest cancellation theorem on primes needed to lower it below `x^{2 delta}`.

**No proof of RH is claimed. Novelty remains unverified.**