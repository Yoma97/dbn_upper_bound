# Round 50 — A positivity–amplification uncertainty principle for Tsang-type pair kernels

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED FOR THE STATED KERNEL CLASS / SOURCE-GROUNDED / NO-GO / NEW TOOL TARGET / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 49 exposed two requirements for a sparse pair-correlation proof:

1. long enough horizontal amplification;
2. a positive localization that permits the functional-equation symmetric pair to be retained as a lower-bound contribution.

The Tsang kernel used in recent horizontal pair-correlation work supplies the second property only inside a prescribed strip of the complex difference variable. This round proves a quantitative tradeoff:

> For the natural Tsang/compact-Fourier-support class, widening the positivity strip enough to cover **all** possible zero differences in the critical strip exponentially damps the Fourier parameter that produces horizontal amplification. After normalization by the diagonal weight, a single symmetric off-line pair receives only an `O_delta(1)` weight, not a power of `T`.

Thus a Tsang-type kernel cannot simultaneously provide unconditional global termwise positivity and sparse power amplification.

A new proof tool must break this positivity--bandwidth tradeoff rather than merely optimize `j` inside the same architecture.

---

## 1. Primary source mechanism

Recent pair-correlation work uses an even entire kernel of the form

\[
\boxed{
K_B(z)
=\frac1\pi\int_0^1 J_B(\alpha)\cos(z\alpha)\,d\alpha,
\qquad
J_B(\alpha):=\frac{j(\alpha)}{\cosh(B\alpha)},}
\]

where `j` is a fixed even compactly supported Fourier weight with the positivity properties required by Tsang's construction.

The source proves, for its stated fixed-`B` regime,

\[
\boxed{
\Re K_B(x+iy)>0\qquad(|y|<B).}
\]

The proof factors the real part as a convolution of two positive Fourier transforms. The same calculation shows the strip-width mechanism transparently: the factor `1/cosh(B alpha)` is exactly what purchases positivity for imaginary displacement up to size `B`.

When the kernel is applied to zero differences,

\[
z=-i(\rho-\rho')\log T,
\]

we have

\[
\Im z=-(\beta-\beta')\log T.
\]

Hence positivity for a prescribed zero set follows whenever

\[
|\beta-\beta'|\log T<B
\]

for all pairs under consideration.

---

## 2. Why unconditional global positivity requires a widening strip

For non-trivial zeta zeros,

\[
0<\beta<1.
\]

Without a narrow-box assumption, pair differences may satisfy

\[
|\beta-\beta'|=1-o(1).
\]

Therefore any direct use of the Tsang strip criterion to guarantee termwise positivity for **every** possible pair up to height `T` requires, at the scaling level,

\[
\boxed{B_T\ge(1-o(1))\log T.}
\]

For the clean theorem below we assume simply

\[
B_T\ge\log T.
\]

A standard zero-free region could replace `log T` by `(1-o(1))log T`; this does not change the conclusion.

---

## 3. Symmetric-pair weight

Let

\[
\rho_+=\frac12+\delta+i\gamma,
\qquad
\rho_-=\frac12-\delta+i\gamma,
\qquad 0<\delta<\frac12.
\]

The symmetric difference is

\[
\rho_+-\rho_-=2\delta.
\]

Thus the real kernel weight of this pair is

\[
\boxed{
K_{B_T}(-2i\delta\log T)
=\frac1\pi\int_0^1
\frac{j(\alpha)}{\cosh(B_T\alpha)}
\cosh(2\delta\alpha\log T)\,d\alpha.}
\]

The diagonal weight is

\[
\boxed{
K_{B_T}(0)
=\frac1\pi\int_0^1
\frac{j(\alpha)}{\cosh(B_T\alpha)}\,d\alpha.}
\]

Assume throughout this round that `j` is continuous at zero, `j(0)>0`, and bounded on `[0,1]`, as is true for the standard admissible choices.

---

## 4. Global-positivity scaling theorem

### Theorem 50.1

Let

\[
L:=\log T,
\qquad
B_T\ge L,
\]

and fix `0<delta<1/2`. Then

\[
\boxed{
K_{B_T}(0)\asymp_j \frac1{B_T}}
\]

and

\[
\boxed{
K_{B_T}(-2i\delta L)
\ll_{j,\delta}
\frac1{B_T}.}
\]

Consequently

\[
\boxed{
\frac{K_{B_T}(-2i\delta L)}{K_{B_T}(0)}
=O_{j,\delta}(1),}
\]

uniformly in `T`.

Thus the symmetric off-line pair has only bounded weight relative to a diagonal zero when the positivity strip is wide enough to cover the whole critical strip.

### Proof: diagonal

Set `u=B_T alpha`. Then

\[
K_{B_T}(0)
=\frac1{\pi B_T}
\int_0^{B_T}\frac{j(u/B_T)}{\cosh u}\,du.
\]

Since `j(0)>0` and is continuous, a fixed interval `0<=u<=u_0` supplies a positive lower bound `c_j/B_T`. Boundedness of `j` and integrability of `sech u` supply the upper bound `C_j/B_T`. Hence

\[
K_{B_T}(0)\asymp_j B_T^{-1}.
\]

### Proof: symmetric pair

Since `B_T>=L`,

\[
2\delta L\le2\delta B_T,
\]

and therefore

\[
\frac{\cosh(2\delta L\alpha)}{\cosh(B_T\alpha)}
\le
2e^{-(1-2\delta)B_T\alpha}+2e^{-(1+2\delta)B_T\alpha}
\ll_\delta e^{-(1-2\delta)B_T\alpha}.
\]

Using boundedness of `j`,

\[
K_{B_T}(-2i\delta L)
\ll_j
\int_0^1 e^{-(1-2\delta)B_T\alpha}\,d\alpha
\ll_{j,\delta}\frac1{B_T}.
\]

Dividing by the diagonal estimate proves the normalized bound. ∎

---

## 5. Exact limiting profile at the minimal global strip

The loss of power amplification can be seen more sharply if

\[
B_T=L.
\]

With `u=L alpha`, dominated convergence gives

\[
L K_L(0)
\longrightarrow
\frac{j(0)}\pi
\int_0^\infty\frac{du}{\cosh u},
\]

and

\[
L K_L(-2i\delta L)
\longrightarrow
\frac{j(0)}\pi
\int_0^\infty
\frac{\cosh(2\delta u)}{\cosh u}\,du.
\]

For `0<delta<1/2` both integrals are finite. Therefore

\[
\boxed{
\frac{K_L(-2i\delta L)}{K_L(0)}
\longrightarrow
R(\delta)
:=
\frac{\int_0^\infty\cosh(2\delta u)\,\operatorname{sech}u\,du}
{\int_0^\infty\operatorname{sech}u\,du},}
\]

a finite constant depending on the horizontal displacement but **not** on `T`.

The Fourier scale has collapsed from `alpha=O(1)` to

\[
\boxed{\alpha=O(1/\log T).}
\]

At this scale

\[
T^{2\delta\alpha}=e^{2\delta\alpha\log T}=e^{O(\delta)},
\]

which explains the disappearance of the power amplifier.

---

## 6. The positivity--amplification uncertainty principle

Within this Tsang-type architecture there are two regimes.

### Narrow positivity strip

If `B=O(1)`, the Fourier weight `1/cosh(B alpha)` leaves `alpha=O(1)` available, and a symmetric pair can retain the power factor

\[
T^{2\delta\alpha}.
\]

But positivity requires

\[
|\beta-\beta'|=O(1/\log T)
\]

for all pairs to which the lower-bound argument is applied. This is precisely a narrow-box/horizontal-localization hypothesis.

### Global positivity strip

If `B_T\asymp log T` so that arbitrary critical-strip pair differences are admitted, positivity can be global, but the Fourier weight forces

\[
\alpha\asymp1/\log T,
\]

and the symmetric-pair amplification is only `O_delta(1)` relative to the diagonal.

Hence

\[
\boxed{
\text{global termwise positivity}
+\text{Tsang compact-frequency architecture}
\Longrightarrow
\text{loss of polynomial sparse amplification}.}
\]

This is the claimed uncertainty principle.

---

## 7. What this theorem does and does not say

The theorem is a no-go for the **stated Tsang/positive-strip kernel mechanism**, not for every conceivable positive pair statistic.

It does not rule out:

- matrix-valued or operator-valued positive kernels;
- a projection that isolates the functional-equation partner before taking a norm;
- adaptive kernels depending on the target ordinate or suspected displacement;
- higher-order correlations with an exact positive decomposition;
- a prime-side quadratic form whose positivity is not obtained from a strip-positive scalar kernel.

It does rule out the idea that simply increasing the Tsang strip width while optimizing the scalar `j(alpha)` will preserve the sparse `T^{2delta alpha}` gain.

---

## 8. New-tool specification after Rounds 49--50

A genuinely new pair-correlation tool should satisfy simultaneously:

1. **global soundness:** no narrow-box or RH-like horizontal localization assumption;
2. **positive isolation:** the pair `(rho,1-rho)` contributes through a nonnegative summand or norm component that cannot be cancelled by other zeros;
3. **macroscopic horizontal bandwidth:** retain an effective `alpha=O(1)` or larger scale, rather than collapsing to `1/log T`;
4. **explicit-formula computability:** the statistic has a prime-side representation with an unconditional error smaller than the amplified one-orbit defect;
5. **sparse completeness:** for every fixed `delta>0`, one off-line orbit eventually violates the unconditional bound; ideally the parameter is adaptive enough to handle `delta` tending to zero with height.

This combination is not present in the current scalar Tsang/Montgomery machinery.

---

## 9. Immediate next invention target

The most promising escape from the scalar-kernel uncertainty principle is to **project onto the functional-equation symmetric subspace before squaring**.

Schematic goal:

\[
\mathcal S_x(t)
=\sum_\rho A_x(t;\rho),
\]

construct an involution-aware linear transform `P` such that

\[
\|P\mathcal S_x\|^2
\]

contains a positive component proportional to

\[
\sinh^2(\delta\log x)
\quad\text{or}\quad
\cosh(2\delta\log x)-1,
\]

for each off-line pair, while vanishing on critical-line pairs, and still admits a controllable explicit-formula representation.

This would turn horizontal displacement into a **positive defect norm** rather than a positive term hidden inside a non-termwise-positive double sum.

Whether such a projection exists with a usable prime-side formula is OPEN and is now the appropriate place to generate a genuinely new mathematical tool.

**No proof of RH is claimed. Novelty remains unverified.**