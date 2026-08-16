# Round 57 — Selberg-variance / long-Dirichlet dictionary and the full-saving necessity for sparse completeness

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED SCALING BRIDGE / CONDITIONAL ARITHMETIC TRANSFER / NECESSARY-STRENGTH THEOREM / NOVELTY UNVERIFIED.

## 0. Executive verdict

Rounds 54--56 leave a centered prime mean-square as the arithmetic core of both the hard-window and soft-window architectures. This round translates that core into the classical variance of primes in short intervals.

For a dyadic prime block `n asy X` and vertical averaging length `T`, the natural additive interval length is

\[
\boxed{H=X/T.}
\]

A Gallagher/Parseval transfer gives, at the level needed here,

\[
\boxed{
\int_{-T}^{T}|E_X(t)|^2dt
\ll
\frac{T^2}{X^2}J(X,H)
+\text{controlled endpoint/discretization terms},}
\]

where

\[
J(X,H)
:=\int_X^{2X}
|\psi(u+H)-\psi(u)-H|^2du.
\]

Thus the generic quadratic scale

\[
J(X,H)\ll H^2X
\]

reproduces the long-polynomial barrier `O(X)`, whereas the Poisson/Selberg scale

\[
J(X,H)\ll HX\,\operatorname{polylog}X
\]

would give

\[
\int|E_X|^2\ll T\,\operatorname{polylog}X,
\]

independently of the polynomial length `X` up to logarithms.

More generally, if one can save a fractional power of the interval length,

\[
J(X,H)\ll H^{2-\kappa}X^{1+o(1)},
\qquad0\le\kappa\le1,
\]

then

\[
\boxed{
\int|E_X|^2
\ll T^\kappa X^{1-\kappa+o(1)}.}
\]

For `X=T^alpha`, the exponent relative to `X` is

\[
\boxed{
\theta_\kappa(\alpha)
=1-\kappa+\frac\kappa\alpha.}
\]

A sparse off-line signal `X^{2delta}` can dominate this only when

\[
2\delta>\theta_\kappa(\alpha).
\]

Letting `alpha` become large shows a qualitative necessity:

\[
\boxed{
\text{any fixed }\kappa<1
\text{ can at best exclude }
\delta>\frac{1-\kappa}{2}.}
\]

Therefore sparse completeness for zeros arbitrarily close to the critical line requires, within this architecture, the **full interval-length saving `kappa=1`** (up to subpowers/logarithms), not merely a nontrivial power saving.

This precisely identifies the strength of the new arithmetic tool that would be needed.

---

## 1. Dyadic centered prime polynomial

On a dyadic block `X<n<=2X`, define

\[
b_n:=\Lambda(n)-1
\]

and

\[
\boxed{
D_X(t)
:=\sum_{X<n\le2X}
\frac{b_n}{\sqrt n}n^{-it}.}
\]

The replacement of the continuous integral by the discrete `1` sequence produces only standard endpoint/Euler-summation corrections at this scale; the essential fluctuation is `Lambda(n)-1`.

The full triangular residual `E_x(t)` from Round 54 can be decomposed into such dyadic blocks with smooth coefficients. Hence a uniform dyadic theorem transfers to the full residual with logarithmic bookkeeping losses.

---

## 2. Gallagher frequency-window principle

The frequencies of the Dirichlet polynomial are

\[
\nu_n:=\frac{\log n}{2\pi}.
\]

A standard Gallagher/Parseval inequality bounds the time mean square on `|t|<=T` by squared local sums of coefficients in frequency windows of width `asymp1/T`.

For `n asy X`,

\[
\log(n+h)-\log n
=\frac hX+O(h^2/X^2).
\]

Thus a logarithmic-frequency window `asymp1/T` corresponds to an additive interval

\[
\boxed{h\asymp H:=X/T.}
\]

After changing variables from logarithmic frequency back to `u`, and using `n^{-1/2} asy X^{-1/2}`, the local coefficient sum is, up to harmless smooth endpoint terms,

\[
X^{-1/2}
\bigl(\psi(u+H)-\psi(u)-H\bigr).
\]

The frequency measure contributes another factor `du/X`.

Consequently

\[
\boxed{
\int_{-T}^{T}|D_X(t)|^2dt
\ll
\frac{T^2}{X^2}
J(X,cH)
+\text{endpoint terms},}
\]

for an absolute constant `c>0`; changing `cH` to `H` is immaterial for the scaling statements below.

This is the precise dimensional bridge used in this round.

---

## 3. Two benchmark variance scales

### 3.1 Quadratic interval bound

Suppose only

\[
J(X,H)\ll H^2X\,L^C,
\qquad L:=\log X.
\]

Then

\[
\frac{T^2}{X^2}J(X,H)
\ll
\frac{T^2}{X^2}\frac{X^2}{T^2}X L^C
=\boxed{XL^C.}
\]

This is exactly the ordinary long-Dirichlet-polynomial barrier.

### 3.2 Poisson/Selberg variance scale

Suppose instead

\[
J(X,H)\ll HX L^C.
\]

Then

\[
\frac{T^2}{X^2}J(X,H)
\ll
\frac{T^2}{X^2}\frac XT X L^C
=\boxed{TL^C.}
\]

Thus saving one complete factor of `H` in short-interval variance removes the polynomial-length penalty.

---

## 4. Fractional-saving interpolation

Assume a family of bounds

\[
\boxed{
J(X,H)\ll H^{2-\kappa}X^{1+o(1)},
\qquad0\le\kappa\le1.}
\]

With `H=X/T`,

\[
\begin{aligned}
\frac{T^2}{X^2}J(X,H)
&\ll
\frac{T^2}{X^2}
\left(\frac XT\right)^{2-\kappa}
X^{1+o(1)}\\
&=\boxed{T^\kappa X^{1-\kappa+o(1)}}.
\end{aligned}
\]

For

\[
X=T^\alpha,
\]

this is

\[
T^{\kappa+\alpha(1-\kappa)+o(1)}
=X^{1-\kappa+\kappa/\alpha+o(1)}.
\]

Define

\[
\boxed{
\theta_\kappa(\alpha)
:=1-\kappa+\frac\kappa\alpha.}
\]

---

## 5. Comparison with a sparse horizontal signal

A right-half zero of displacement `delta>0` creates a natural quadratic horizontal amplifier of size

\[
X^{2\delta}
\]

in the pair/Gram architecture.

If the arithmetic side is bounded by

\[
X^{\theta_\kappa(\alpha)+o(1)},
\]

then a necessary exponent separation for contradiction is

\[
\boxed{
2\delta>	heta_\kappa(\alpha)
=1-\kappa+\frac\kappa\alpha.}
\]

For fixed `kappa`, increasing `alpha` gives the best possible threshold

\[
\boxed{
2\delta>1-\kappa.}
\]

Equivalently,

\[
\boxed{
\delta>\frac{1-\kappa}{2}.}
\]

---

## 6. Full-saving necessity for sparse completeness

Suppose `kappa<1` is fixed. Then the threshold

\[
\frac{1-\kappa}{2}>0.
\]

Therefore the variance theorem can never rule out zeros whose horizontal displacement lies in

\[
0<\delta\le\frac{1-\kappa}{2},
\]

no matter how long a pair-correlation parameter `alpha` is used.

Thus, within this scaling architecture,

\[
\boxed{
\text{sparse completeness for arbitrarily small }\delta
\Longrightarrow
\kappa=1-o(1).}
\]

In words: a fixed fractional improvement over the trivial variance is not qualitatively enough. One needs essentially Poisson-scale variance.

This is a **necessary-strength statement for this route**, not a theorem that such variance would by itself prove RH; the hard-window architecture still has the zero-window-transfer problem from corrected Round 54, while the soft-window architecture requires a corresponding Gaussian version.

---

## 7. Comparison with what is currently known

Two facts must be distinguished.

1. Under RH, classical Selberg/Saffari--Vaughan mean-square estimates reach essentially the target scale
   \[
   J(X,H)\ll HX\,\log^2(2X/H)
   \]
   over the full natural interval range. Such a theorem cannot be imported here as an unconditional input.

2. Modern unconditional results prove the expected prime-count asymptotic for **almost all** intervals once
   \[
   H\ge X^{1/6+o(1)}
   \]
   (a 2023 survey/theorem discussion records this as the best current asymptotic almost-all range).

The second statement does **not** automatically imply the global quadratic bound

\[
J(X,H)\ll HX\,\operatorname{polylog}X.
\]

A very small exceptional set can still dominate an `L^2` integral. Therefore an almost-all counting theorem cannot be substituted for the variance estimate without a quantitative exceptional-tail analysis.

This distinction is essential for circularity control.

---

## 8. What existing long-interval information can still do

For `X=T^alpha`,

\[
H=X/T=X^{1-1/\alpha}.
\]

As `alpha` grows, `H` is a very long interval on the `X` scale. Thus known unconditional distribution results suggest that the **prime mean-square channel may become more tractable for very large alpha**.

But corrected Round 54 shows that the hard finite-zero-window statistic still suffers an independent `O(x)` transfer error. Therefore success on the Selberg variance alone cannot close the hard-window program.

This is one reason the soft holomorphic window of Round 56 is strategically important.

---

## 9. New-tool specification sharpened

The arithmetic tool required for sparse completeness is not merely

> prove some nontrivial short-interval variance saving.

It is closer to

### PSV — Poisson-Scale Variance theorem

Prove, in the exact multiplicative/Gaussian range required by the chosen explicit-formula statistic,

\[
\boxed{
J_{\rm adapted}(X,H)
\ll HX\,X^{o(1)}}
\]

or an equivalent long-Dirichlet mean-square estimate, from unconditional arithmetic structure.

A version with

\[
J\ll H^{2-\kappa}X^{1+o(1)}
\]

for fixed `kappa<1` would still be mathematically valuable: it would exclude a definite horizontal band

\[
\beta>1-\kappa/2
\]

in an idealized long-range architecture. But it is not sparse-complete near the critical line.

---

## 10. Program decision

- Selberg variance is the correct arithmetic dual of the long prime mean square: **PROVED at the scaling/transfer level**.
- Trivial quadratic variance `H^2X`: **REPRODUCES the `X` barrier**.
- Poisson variance `HX polylog`: **REMOVES polynomial-length loss**.
- Fixed fractional saving `kappa<1`: **INSUFFICIENT for arbitrarily small horizontal displacement**.
- Full `kappa=1` saving: **QUALITATIVELY NECESSARY for sparse completeness in this architecture**.
- Existing almost-all prime theorems: **NOT a substitute for the required global `L^2` bound without further tail control**.

The next invention step should therefore not be a generic improvement to prime intervals. It should target one of two highly structured objects:

1. an `L^2` theorem at Poisson scale for the exact triangular/Gaussian weights generated by the explicit formula; or
2. a new statistic whose sparse signal grows faster, so that a fractional variance saving `kappa<1` becomes sufficient.

The second option may be more realistic and should be tested next by searching for **higher-order horizontal amplification** without increasing the prime-side correlation order beyond what is controllable.

**No proof of RH is claimed. Novelty remains unverified.**