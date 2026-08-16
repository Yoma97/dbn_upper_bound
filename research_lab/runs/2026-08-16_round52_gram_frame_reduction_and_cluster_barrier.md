# Round 52 — Gram-space sparse isolation and the fixed-width frame-conditioning barrier

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED REDUCTION / PROVED CONDITIONING BARRIER / NEW TOOL TARGET / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 51 showed that exact horizontal projection is intrinsically Hermitian/two-variable. The unconditional pair-correlation formula already supplies such a Hermitian object through an exact Gram norm.

For a zero

\[
\rho=\frac12+\delta+i\gamma,
\]

the associated Gram vector has self-energy

\[
\boxed{
\|v_{\rho,x}\|^2
=\frac{x^{2\delta}}{1-\delta^2}.}
\]

Thus the desired sparse horizontal power amplifier is already present as a **positive diagonal Gram energy**. The obstruction is entirely in Gram conditioning: the vector attached to one zero can interfere with vectors attached to nearby ordinates.

A raw Riesz/frame lower bound with a `T`-independent constant is impossible for the fixed-width Montgomery kernel. Even among critical-line zeros, two ordinates at spacing `d<<1` produce almost collinear kernel vectors. For the basic Lorentzian width `eta`, the exact normalized correlation is

\[
\boxed{
r_\eta(d)=\frac{4\eta^2}{d^2+4\eta^2},}
\]

so the two-vector lower Gram eigenvalue is

\[
\boxed{1-r_\eta(d)=\frac{d^2}{d^2+4\eta^2}.}
\]

Since a positive proportion of zeta zeros are known unconditionally to lie on the critical line, there are arbitrarily high critical-line pairs with spacing `d=O(1/log T)`. Hence any global fixed-width frame constant satisfies at best

\[
\boxed{A_T\ll_\eta (\log T)^{-2}.}
\]

This logarithmic degeneration does not by itself destroy the long-range power-amplification program, but it proves that **positivity is not enough**: a sparse proof needs a cluster-stable Gram decomposition with quantitatively controlled conditioning.

---

## 1. Exact Gram representation

The RH-free pair-correlation identity gives

\[
F(x,T)
=\frac2\pi\int_{\mathbb R}
\left|
\sum_{\substack{\rho\\0<\gamma\le T}}
\frac{x^{\rho-1/2}}
{1-(\rho-(1/2+it))^2}
\right|^2dt.
\]

Writing

\[
\rho=\frac12+\delta+i\gamma,
\]

define

\[
\boxed{
v_{\rho,x}(t)
:=\sqrt{\frac2\pi}
\frac{x^{\delta+i\gamma}}
{1+((t-\gamma)+i\delta)^2}.}
\]

Then exactly

\[
\boxed{
F(x,T)
=\left\|\sum_{0<\gamma\le T}v_{\rho,x}\right\|_{L^2(\mathbb R)}^2.}
\]

Thus pair correlation is a Gram norm, not merely a formal double sum.

---

## 2. Exact self-energy and the hidden horizontal amplifier

The diagonal Gram entry is obtained either directly by residues or from the diagonal term in the Hermitian expansion of the source formula:

\[
\boxed{
\|v_{\rho,x}\|_2^2
=x^{2\delta}w(2\delta)
=\frac{x^{2\delta}}{1-\delta^2}.}
\]

For a right-half zero `delta>0`, this is already the desired positive sparse amplifier.

Its functional-equation partner has displacement `-delta` and self-energy

\[
\frac{x^{-2\delta}}{1-\delta^2}.
\]

Even within this pair the larger vector cannot be completely cancelled by the smaller one, since

\[
\|v_++v_-\|
\ge\big|\|v_+\|-\|v_-\|\big|
=\frac{x^\delta-x^{-\delta}}{\sqrt{1-\delta^2}}.
\]

Thus the principal cancellation problem comes from the rest of the zero system, not from the functional-equation partner itself.

---

## 3. What a frame theorem would provide

If one had a lower-frame estimate

\[
\boxed{
\left\|\sum_\rho c_\rho u_\rho\right\|_2^2
\ge A_T\sum_\rho|c_\rho|^2\|u_\rho\|_2^2}
\]

for the relevant kernel vectors and coefficient family, then the amplified diagonal term of a single right-half zero could not disappear into destructive interference.

A constant `A_T>=A>0` would be ideal. This section shows that such a fixed positive constant is impossible for a fixed-width kernel at zeta-zero density.

---

## 4. Exact two-kernel conditioning model

Consider the real critical-line model with width `eta>0`:

\[
q_\eta(t):=\frac1{\eta^2+t^2}.
\]

Its Fourier transform is

\[
\widehat q_\eta(\xi)
=\frac\pi\eta e^{-\eta|\xi|}
\]

under the standard full Fourier convention. Hence

\[
\|q_\eta\|_2^2
=\frac\pi{2\eta^3}.
\]

For two translates separated by `d`, convolution or Plancherel gives

\[
\langle q_\eta(\cdot),q_\eta(\cdot-d)\rangle
=\frac{2\pi}{\eta(d^2+4\eta^2)}.
\]

After normalization,

\[
\boxed{
r_\eta(d)
:=\frac{\langle q_\eta,q_\eta(\cdot-d)\rangle}
{\|q_\eta\|_2^2}
=\frac{4\eta^2}{d^2+4\eta^2}.}
\]

The normalized two-vector Gram matrix is

\[
G_2=
\begin{pmatrix}
1&r_\eta(d)\\
r_\eta(d)&1
\end{pmatrix},
\]

with eigenvalues

\[
1\pm r_\eta(d).
\]

Therefore

\[
\boxed{
\lambda_{\min}(G_2)
=1-r_\eta(d)
=\frac{d^2}{d^2+4\eta^2}.}
\]

For `d<<eta`,

\[
\boxed{
\lambda_{\min}(G_2)
\sim\frac{d^2}{4\eta^2}.}
\]

This is an exact conditioning obstruction.

---

## 5. Application to zeta-density scale

Unconditionally, a positive proportion of non-trivial zeros lie on the critical line. Together with the Riemann--von Mangoldt count, this implies that in dyadic height intervals there are `asymp T log T` critical-line zeros along a vertical interval of length `asymp T`.

By pigeonhole, arbitrarily high such intervals contain consecutive critical-line ordinates with

\[
\boxed{d\ll\frac1{\log T}.}
\]

For any fixed `eta asy 1`, the two-vector calculation therefore forces every lower-frame constant for a system containing these vectors to satisfy

\[
\boxed{
A_T
\le\lambda_{\min}(G_2)
\ll_\eta\frac1{\log^2T}.}
\]

Thus a `T`-independent Riesz lower bound is impossible for the natural fixed-width system.

---

## 6. Width versus horizontal robustness

A natural response is to shrink the vertical/Lorentzian width to

\[
\eta\asymp1/\log T,
\]

which is comparable to mean zero spacing and improves Gram conditioning.

But in the RH-free complex kernels the denominator poles remain safely separated from the real integration line only when the width dominates the horizontal displacement `|delta|`. To accommodate arbitrary critical-strip zeros one needs a width of order one, whereas `eta~1/log T` is compatible only with a narrow horizontal box

\[
|\delta|=O(1/\log T).
\]

This is the Gram-space analogue of the positivity--bandwidth tradeoff from Round 50.

---

## 7. What the logarithmic frame loss means

The estimate

\[
A_T\ll(\log T)^{-2}
\]

does **not** by itself refute the sparse pair-correlation strategy. If a long-range theorem produces a target diagonal energy `T^{2 alpha delta}` with a genuine power surplus over all arithmetic errors, a polylogarithmic conditioning loss may be harmless.

Therefore the correct conclusion is narrower:

> no proof may replace the full Gram norm by its diagonal energy with an implicit constant independent of height.

Any successful argument must quantify cluster conditioning explicitly.

---

## 8. Cluster-stable replacement as a new tool

The almost-collinearity of nearby translates suggests replacing raw kernel vectors by a **confluent/divided-difference basis**.

For two nearby centers,

\[
\frac{q_\eta(t-\gamma-d)-q_\eta(t-\gamma)}d
\longrightarrow
-\partial_t q_\eta(t-\gamma).
\]

Thus instead of treating a tight zero cluster as many nearly identical vectors, one can encode it by a jet basis

\[
q_\eta,\quad
\partial_tq_\eta,\quad
\partial_t^2q_\eta,\ldots
\]

at a cluster center.

This is analogous to confluent interpolation for multiple or coalescing nodes and is structurally compatible with the multiplicity/jet philosophy developed earlier in the heat-flow program.

The missing theorem is not elementary linear algebra: one needs a decomposition that is simultaneously

1. quantitatively well-conditioned for arbitrarily tight zero clusters;
2. positive / Gram-compatible;
3. uniform in horizontal displacement `delta`;
4. expressible on the prime side without inserting the unknown zero locations by hand.

---

## 9. New-tool target: CGEF

### Cluster-stable Gram Explicit Formula (CGEF)

Construct a canonical arithmetic transform of the RH-free zero kernel with the following property.

Partition or encode the zero system into local confluent blocks and obtain

\[
\boxed{
F_{\rm defect}(x,T)
=\sum_{\mathcal C}
\|\mathbf J_{\mathcal C}(x)\|_{M_{\mathcal C}}^2
+\text{controlled cross-block error},}
\]

where

- each matrix `M_C` is positive definite with explicit condition number after natural local scaling;
- an off-line displacement contributes a positive component growing like `x^{2|delta|}` or an equivalent amplifier;
- close vertical ordinates are represented by jets/divided differences rather than nearly parallel raw kernels;
- the prime-side evaluation has an error smaller than one amplified orbit.

This would implement the Hermitian Explicit Projection Formula target of Round 51 in a cluster-stable basis.

---

## 10. Program decision

- The Gram diagonal already contains the correct power amplifier: **PROVED**.
- Raw global diagonal domination by positivity: **INVALID**.
- Uniform fixed-width Riesz lower bound: **REFUTED**.
- Polylogarithmic conditioning loss: **PROVED unavoidable at least at the two-kernel level**.
- Confluent/divided-difference Gram renormalization: **OPEN / NEW TOOL TARGET**.
- Long-range explicit-formula control from Round 49 is still separately required.

The next round should test whether a simple two-zero confluent block can be written on the prime side without knowing the zeros explicitly. If even the first divided-difference block requires zero-dependent coefficients, that dependence must be isolated as the next obstruction.

**No proof of RH is claimed. Novelty remains unverified.**