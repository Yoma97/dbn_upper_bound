# Round 56 — Holomorphic heat-window localization removes hard truncation but exposes a Gaussian prime-cancellation barrier

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED SPECTRAL DETECTOR / SOFT-WINDOW REDUCTION / PRIME-SIDE BARRIER / NEW TOOL TARGET / NOVELTY UNVERIFIED.

## 0. Executive verdict

The correction to Round 54 shows that the finite-height RH-free pair-correlation proof has two long-range obstacles:

1. long prime/pole cancellation;
2. an `O(x)` transfer error caused by replacing the all-zero explicit-formula resolvent with a hard finite zero window.

This round removes the second obstacle at the level of **statistic design**.

Instead of cutting zeros sharply at height `T`, use the holomorphic Gaussian spectral test

\[
\boxed{
h_{c,L}(z):=e^{-cLz^2+iLz},\qquad c,L>0.}
\]

For a zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad
z_\rho:=\frac{\rho-1/2}{i}=\gamma-i\delta,
\]

the term `h_{c,L}(z_rho)` has real exponential rate

\[
\boxed{
q_c(\rho)
:=\delta-c(\gamma^2-\delta^2).}
\]

The quadratic height penalty forces the maximal rate to be attained by finitely many zeros. Hence no hard vertical truncation is required.

If RH holds, every `delta=0` and all rates are strictly negative. If any off-line zero exists, choosing `c` sufficiently small makes its rate positive. Thus this family is a complete soft spectral detector.

However, its Guinand--Weil Fourier transform is a Gaussian centered at logarithmic prime scale `u=L`. The corresponding prime main term has an exponential saddle whose leading exponent reflects the line `Re s=1`, and current unconditional PNT errors reduce it only subexponentially. Therefore soft-window localization avoids the `O(x)` zero-truncation channel but **does not** supply the required centered-prime cancellation.

The new tool requirement is now clean: a Gaussian/log-normal prime-error estimate with genuine exponential saving relative to the continuous prime saddle, derived by a mechanism weaker than RH.

---

## 1. Spectral variable and zero symmetries

For every nontrivial zero

\[
\rho=\frac12+\delta+i\gamma,
\]

define

\[
\boxed{
z_\rho:=\frac{\rho-1/2}{i}=\gamma-i\delta.}
\]

The critical line corresponds to the real `z`-axis.

Complex conjugation and the functional equation generate the quartet

\[
\gamma-i\delta,
\quad
\gamma+i\delta,
\quad
-\gamma-i\delta,
\quad
-\gamma+i\delta.
\]

For nontrivial zeta zeros, `|delta|<1/2` and `|gamma|` tends to infinity along the zero set.

---

## 2. Holomorphic soft window

Fix `c>0` and `L>0`. Define

\[
\boxed{
h_{c,L}(z)=\exp(-cLz^2+iLz).}
\]

This is entire. On the real axis,

\[
|h_{c,L}(x)|=e^{-cLx^2},
\]

so it has Gaussian decay and is an admissible Schwartz-type spectral test for standard explicit-formula purposes.

At a zero spectral point `z=gamma-i delta`,

\[
\begin{aligned}
-cLz^2+iLz
&=-cL(\gamma^2-\delta^2-2i\gamma\delta)
+iL\gamma+L\delta\\
&=L\bigl[\delta-c(\gamma^2-\delta^2)\bigr]
+iL\bigl[\gamma+2c\gamma\delta\bigr].
\end{aligned}
\]

Thus

\[
\boxed{
|h_{c,L}(z_\rho)|
=e^{Lq_c(\rho)},
\qquad
q_c(\rho)=\delta-c(\gamma^2-\delta^2).}
\]

---

## 3. The maximal soft horizontal score is attained

For fixed `c>0`,

\[
q_c(\rho)
\le\frac12+c/4-c\gamma^2.
\]

Hence

\[
q_c(\rho)\to-\infty
\quad\text{as }|\gamma|\to\infty.
\]

The zero set is locally finite, so

\[
\boxed{
q_*(c):=\max_\rho q_c(\rho)}
\]

is attained by a finite nonempty collection of zeros.

This is the key soft-localization advantage: far zeros are suppressed at an exponential-in-`L` rate, not merely by a fixed polynomial resolvent tail.

---

## 4. RH versus positive soft score

If RH holds, `delta=0` for every nontrivial zero. Therefore

\[
q_c(\rho)=-c\gamma^2<0
\]

and hence

\[
\boxed{q_*(c)<0\quad\text{for every }c>0.}
\]

Conversely, suppose an off-line right-half zero exists:

\[
\rho_0=\frac12+\delta+i\gamma,
\qquad\delta>0.
\]

Since `gamma^2-delta^2>0`, choose

\[
0<c<\frac{\delta}{\gamma^2-\delta^2}.
\]

Then

\[
q_c(\rho_0)>0,
\]

so

\[
\boxed{q_*(c)>0.}
\]

Therefore

\[
\boxed{
\mathrm{RH}
\iff
q_*(c)<0\text{ for every }c>0.}
\]

**Circularity warning:** this equivalence alone is not progress toward RH; its value is the soft statistic that avoids a hard zero cutoff.

---

## 5. Zero-side exponential extraction

Define the absolutely convergent soft zero sum

\[
\boxed{
S_c(L):=\sum_\rho m_\rho h_{c,L}(z_\rho).}
\]

For every fixed `c,L>0`, Gaussian decay in `gamma` and standard zero counting give absolute convergence.

Let

\[
p_c(\rho):=\gamma+2c\gamma\delta.
\]

Then

\[
S_c(L)=\sum_\rho m_\rho e^{Lq_c(\rho)}e^{iLp_c(\rho)}.
\]

The finite set with `q_c=q_*` dominates exponentially. A Cesàro average of the squared modulus removes phase cancellation among distinct maximal frequencies:

\[
\boxed{
\lim_{A\to\infty}\frac1A
\int_1^A
 e^{-2q_*L}|S_c(L)|^2\,dL
=
\sum_{p}
\left|
\sum_{\substack{\rho:q_c(\rho)=q_*\\p_c(\rho)=p}}
 m_\rho
\right|^2>0.}
\]

Consequently

\[
\boxed{
q_*(c)
=\frac12\limsup_{L\to\infty}
\frac1L\log|S_c(L)|^2.}
\]

This is the soft-window analogue of Round 53's extremal Laplace--Cesàro projection.

---

## 6. Exact Fourier transform

Use the Fourier convention

\[
\widehat h(u)=\int_{\mathbb R}h(x)e^{-iux}\,dx.
\]

Gaussian integration gives

\[
\boxed{
\widehat h_{c,L}(u)
=\sqrt{\frac{\pi}{cL}}
\exp\!\left(-\frac{(u-L)^2}{4cL}\right).}
\]

Thus the prime side of the Guinand--Weil explicit formula contains the positive Gaussian logarithmic weight

\[
\boxed{
\frac{\Lambda(n)}{\sqrt n}
\sqrt{\frac{\pi}{cL}}
\exp\!\left(-\frac{(\log n-L)^2}{4cL}\right),}
\]

plus the reflected `-log n` Gaussian and the explicit archimedean channels.

The hard cutoff in zero height has disappeared entirely.

---

## 7. Continuous prime saddle

Replace `d psi(u)` by `du` and use `y=log u`. Ignoring harmless constants, the positive-frequency continuous prime mass has exponential factor

\[
\exp\left(
\frac y2-rac{(y-L)^2}{4cL}
\right).
\]

The exponent is

\[
\Phi(y)=\frac y2-rac{(y-L)^2}{4cL}.
\]

Its stationary point satisfies

\[
\Phi'(y)=\frac12-\frac{y-L}{2cL}=0,
\]

hence

\[
\boxed{y_*=(1+c)L.}
\]

At the saddle,

\[
\boxed{
\Phi(y_*)=\left(\frac12+\frac c4\right)L.}
\]

Thus the raw prime and archimedean terms are individually exponentially much larger than the off-line score one hopes to detect.

As in Round 54, the continuous main term must be subtracted/cancelled exactly before any meaningful sparse estimate is attempted.

---

## 8. Why the classical unconditional PNT error is insufficient

After subtracting the continuous main term, a classical zero-free-region PNT estimate has only a subexponential relative saving of the schematic type

\[
\psi(x)-x
\ll x\exp(-C(\log x)^a(\log\log x)^{-b})
\]

with `a<1` in standard unconditional regions.

Inserted into the Gaussian window, this changes

\[
\left(\frac12+\frac c4\right)L
\]

only by a sublinear negative correction in `L`.

But every nontrivial off-line zero has

\[
\delta<\frac12.
\]

Therefore a bound obtained merely by taking absolute values of the classical PNT error retains a leading exponent at least near `1/2`, while the target soft-zero signal has exponent

\[
q_c(\rho)=\delta-c(\gamma^2-\delta^2)<\delta<1/2.
\]

Hence classical pointwise PNT error estimates cannot upper-bound the centered Gaussian prime sum at the required exponential scale.

This is the soft-window version of the same arithmetic obstruction found in Rounds 54--55.

---

## 9. General drift parameter and the invariant gap

More generally let

\[
h_{a,c,L}(z)=e^{-cLz^2+iaLz},\qquad a>0.
\]

An off-line zero has score

\[
q_{a,c}(\rho)=a\delta-c(\gamma^2-\delta^2),
\]

while the continuous prime saddle exponent is

\[
\boxed{\frac a2+\frac c4.}
\]

Since `delta<1/2`, the leading prime-line exponent exceeds `a delta` before the quadratic height penalty is even included.

Thus changing the drift does not remove the fundamental `Re s=1` versus `Re rho<1` gap.

---

## 10. What Round 56 accomplishes

The round **does** solve a design problem:

\[
\boxed{
\text{hard finite-height zero window}
\longrightarrow
\text{holomorphic Gaussian height penalty}.}
\]

This removes the separate `O(x)` zero-truncation error that afflicted the hard-window statistic.

But it exposes a cleaner arithmetic problem:

\[
\boxed{
\text{centered Gaussian/log-normal prime cancellation at exponential precision}.}
\]

The required estimate cannot come from the classical pointwise PNT error by absolute values.

---

## 11. New-tool target: GWPC

### Gaussian-Window Prime Cancellation theorem

For the exact Gaussian weight generated by `h_{c,L}`, obtain a centered prime-side estimate whose exponential rate is strictly below the continuous line `Re s=1` rate and is strong enough to compare with

\[
q_*(c)=\max_\rho[\delta-c(\gamma^2-\delta^2)].
\]

The theorem must be derived by genuinely averaged/bilinear arithmetic cancellation, not by assuming a PNT error equivalent to RH.

Potential mechanisms:

- mean-square averaging in the drift/location parameter `L`;
- a bilinear/Vaughan or Heath--Brown decomposition adapted to the log-Gaussian weight;
- dispersion in both prime scale and spectral parameter;
- a positive quadratic explicit formula in which the continuous prime saddle cancels algebraically before estimation;
- a Selberg-variance theorem with the Gaussian multiplicative window built in.

---

## 12. Program decision

- Hard-window truncation `O(x)`: **AVOIDABLE by redesigning the statistic**.
- Holomorphic soft height localization: **PROVED**.
- Sparse completeness of the soft score: **PROVED**.
- Classical unconditional PNT error as closure: **INSUFFICIENT**.
- Prime-side Gaussian cancellation: **OPEN / NEW TOOL REQUIRED**.

There are now two candidate arithmetic architectures:

1. hard-window pair statistic + LDP-MS + ZWT;
2. soft holomorphic heat window + GWPC, which avoids ZWT but requires stronger Gaussian-centered prime cancellation.

The next round should compare their arithmetic strength through the Selberg integral / short-interval variance. Whichever architecture reduces to the weaker known or plausibly provable variance theorem should become primary.

**No proof of RH is claimed. Novelty remains unverified.**