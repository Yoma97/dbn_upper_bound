# Round 54 — Pole–prime cancellation and the long Dirichlet-polynomial gap

**Date:** 2026-08-16

**CORRECTED after direct audit of the proof of the RH-free pair-correlation theorem.**

**RH status:** OPEN.

**Status labels:** PROVED SOURCE DECOMPOSITION / CORRECTED / CIRCULARITY GUARD / ARITHMETIC GAP / TRUNCATION GAP / NOVELTY UNVERIFIED.

## 0. Correction and executive verdict

An earlier version of this round overstated the origin of the `O(x)` barrier by saying that it came entirely from separating the pole at `s=1` from the continuous main term of the prime polynomial.

That statement is **CORRECTED**.

There are at least two logically distinct long-range `O(x)`-scale channels in the published RH-free proof:

1. a **prime/pole channel**: the exact pole term has size `x^{1/2}` and is also the continuous main term of the prime polynomial; bounding these separately loses an `O(x)` contribution after squaring;
2. a **zero-window truncation channel**: in the step converting the all-zero explicit-formula square to the finite-height statistic `F(x,T)`, truncating zeros at `Z=T log^2 T` already contributes `O(x)`, independently of the prime/pole separation. The proof also incurs a zero-free-region-dependent term of shape
   \[
   O\!\left(x^{1-2\eta(T\log^2T)}\log^3T\right).
   \]

Therefore improving the long prime mean square alone does **not** automatically extend `F(x,T)` to `x>>T`. A successful LREF theorem must control **both** prime/pole cancellation and the mismatch between the all-zero explicit formula and the finite zero window.

The exact pole--prime identity established below remains valid and useful.

---

## 1. RH-free explicit-formula side

The unconditional Montgomery-type lemma used in the pair-correlation theorem yields an all-zero resolvent of the schematic form

\[
\sum_\rho
\frac{2x^{\delta+i(\gamma-t)}}
{1+((t-\gamma)+i\delta)^2}
=
-P_x(t)
+x^{-1}(\log(|t|+2)+O(1))
+O\!\left(\frac{x^{1/2}}{1+t^2}\right)
+O\!\left(\frac{x^{-5/2}}{|t|+2}\right),
\]

where

\[
\boxed{
P_x(t)
:=\sum_{n\ge1}\frac{\Lambda(n)}{n^{1/2+it}}
W(n/x),
\qquad
W(y):=\min(y,y^{-1}).}
\]

The `x^{1/2}` channel comes from the pole at `s=1`.

Separately, in the proof relating the square of the all-zero sum to the finite-height pair statistic, one first truncates the zero set at

\[
Z=T\log^2T.
\]

The published estimate for the omitted tail is of size

\[
\ll \frac{xT\log^2Z}{Z}=O(x).
\]

After restricting from `|gamma|<=Z` to `0<=gamma<=T` and extending the `t`-integral, another term of size

\[
O\!\left(x^{1-2\eta(T\log^2T)}\log^3T\right)
\]

appears, together with `O(x)`.

Thus the finite-window reconstruction has an `O(x)` obstruction even before any proposed improvement of the prime mean square is used.

---

## 2. Exact pole term before absolute-value bounding

Start from the pole contribution in Landau's formula

\[
-\frac{x^{1-s}}{1-s}.
\]

After the reflection/subtraction step and setting `sigma=3/2`, the exact pole term is

\[
\boxed{
I_x(t)
=x^{1/2-it}
\left(
\frac1{3/2-it}
+
\frac1{1/2+it}
\right).}
\]

Its crude size is

\[
I_x(t)=O\!\left(\frac{x^{1/2}}{1+t^2}\right).
\]

---

## 3. The same term is the continuous main term of the prime polynomial

Write

\[
P_x(t)=\int_{1^-}^{\infty}
 u^{-1/2-it}W(u/x)\,d\psi(u),
\qquad
\psi(u)=\sum_{n\le u}\Lambda(n).
\]

Replacing `d psi(u)` by `du`, define

\[
I_x^{\rm cont}(t)
:=\int_0^\infty u^{-1/2-it}W(u/x)\,du.
\]

Split at `u=x`. For `u<=x`,

\[
\frac1x\int_0^x u^{1/2-it}du
=\frac{x^{1/2-it}}{3/2-it},
\]

while for `u>=x`,

\[
x\int_x^\infty u^{-3/2-it}du
=\frac{x^{1/2-it}}{1/2+it}.
\]

Therefore

\[
\boxed{I_x^{\rm cont}(t)=I_x(t).}
\]

This exact identity is unaffected by the correction above.

---

## 4. Centered prime residual

Let

\[
R(u):=\psi(u)-u.
\]

Then, up to the harmless lower-end convention,

\[
\boxed{
E_x(t)
:=P_x(t)-I_x(t)
=\int_{1^-}^{\infty}
 u^{-1/2-it}W(u/x)\,dR(u).}
\]

Thus one long-range obstruction is genuinely a smoothed Mellin transform of the PNT error.

The key distinction is now:

\[
\boxed{
\text{arithmetic residual }E_x(t)
\quad\text{versus}\quad
\text{finite-zero-window truncation}.}
\]

They must not be conflated.

---

## 5. Why separate pole bounds lose `O(x)`

If the pole term is bounded separately,

\[
\int_0^T|I_x(t)|^2dt\ll x.
\]

So an `O(x)` channel is indeed created by failing to exploit the exact prime/pole cancellation.

But this is **not the only `O(x)` channel** in the complete proof, because the zero truncation described in Section 1 contributes another `O(x)`.

The correct conclusion is therefore

\[
\boxed{
\text{pole subtraction is necessary for long range, but not sufficient}.}
\]

---

## 6. Circularity guard for pointwise PNT improvement

A bound such as

\[
E_x(t)=x^{o(1)}
\]

uniformly pointwise in fixed `t` is already of RH strength: a zero at horizontal displacement `delta>0` naturally produces Mellin growth `x^delta` after pole subtraction.

Therefore such a statement cannot be inserted as an apparently innocuous prime-side lemma.

The legitimate opportunity is averaged control in `t`, not a pointwise zero-free-strength PNT error.

---

## 7. Long Dirichlet-polynomial mean square

Expanding

\[
\int_0^T|P_x(t)|^2dt
\]

produces

\[
\sum_{m,n}
\frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
W(m/x)W(n/x)
\int_0^T e^{it\log(m/n)}dt.
\]

The oscillatory kernel obeys

\[
\left|\int_0^T e^{it\log(m/n)}dt\right|
\ll
\min\left(T,\frac1{|\log(m/n)|}\right).
\]

For `x=T^alpha`, near-coherent pairs satisfy roughly

\[
|m-n|\lesssim x/T=T^{\alpha-1}.
\]

Thus extension beyond `alpha=1` requires averaged shifted-prime cancellation, or an equivalent short-interval variance theorem, for increasingly long prime polynomials.

---

## 8. A second long-range problem: zero-window tails

Let

\[
S_x(t)
:=\sum_\rho
\frac{x^{\delta+i\gamma}}
{1+((t-\gamma)+i\delta)^2}
\]

be the all-zero resolvent and `S_{x,T}` its restriction to the finite zero window defining `F(x,T)`.

The source bound used in the unconditional theorem is based on

\[
\left|S_x(t)-S_{x,Z}(t)\right|
\ll x^{1/2}\frac{\log Z}{Z}
\]

for `0<=t<=T` after the zero-free-region bound and zero counting, leading after integration to the `O(x)` truncation scale at `Z=T log^2T`.

For `x>>T`, a new theorem must improve this **without assuming a horizontal zero bound equivalent to RH**.

Possible mechanisms include:

- cancellation in the far-zero resolvent rather than absolute summation;
- a smoother vertical cutoff replacing the hard `0<gamma<=T` window;
- a statistic whose zero window and explicit-formula test are matched from the start, avoiding the all-zero-to-truncated-zero comparison;
- a two-parameter transform in which the vertical cutoff is encoded analytically and prime-side errors decay with the cutoff smoothness.

---

## 9. Corrected tool specification

A long-range RH-free proof now needs **two** advances.

### LDP-MS — Long Dirichlet Polynomial Mean Square

Control the centered arithmetic residual

\[
E_x(t)=P_x(t)-I_x(t)
\]

for `x>T` using averaged prime correlations / Selberg variance rather than RH-strength pointwise cancellation.

### ZWT — Zero-Window Transfer theorem

Replace the existing `O(x)` finite-window truncation by an estimate compatible with `x^{2delta}` sparse signals, without assuming the desired horizontal zero localization.

The cleanest possibility would be to redesign the statistic so that no separate ZWT step is required.

---

## 10. Program decision

- Exact pole--prime main cancellation: **PROVED**.
- Claim that the complete `O(x)` barrier comes only from that cancellation: **REFUTED / CORRECTED**.
- Independent `O(x)` zero-window truncation: **PROVED FROM THE PRIMARY PAIR-CORRELATION PROOF**.
- Pointwise PNT residual as shortcut: **REJECTED AS RH-STRENGTH**.
- Long mean-square arithmetic cancellation: **OPEN / NEW TOOL NEEDED**.
- Long-range finite-window transfer: **OPEN / NEW TOOL NEEDED**.

Round 55's Mellin-resolvent reduction remains valid for the prime-polynomial channel, but it must not be mistaken for a complete treatment of the finite-height statistic `F(x,T)`.

**No proof of RH is claimed. Novelty remains unverified.**