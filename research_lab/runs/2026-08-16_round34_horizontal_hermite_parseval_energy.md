# Round 34 — Exact horizontal Gaussian-Hermite Parseval energy for xi and the heat family

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED IDENTITY / POSITIVE CROSS-FRONTIER ENERGY / NON-CIRCULAR / NOVELTY UNVERIFIED.

## 0. Executive theorem

Round 32 identified the horizontal Gaussian-Hermite moments

\[
M_k(t,\gamma)
:=\int_{\mathbb R}
G_t(a)H_k(a/\sqrt t)
\xi\!\left(\frac12+a+i\gamma\right)\,da,
\qquad
G_t(a)=\frac1{\sqrt{\pi t}}e^{-a^2/t},
\]

and proved

\[
M_k(t,\gamma)
=8(2\sqrt t)^k i^{-k}H_t^{(k)}(2\gamma).
\]

This round applies Hermite Parseval and obtains the exact positive identity

\[
\boxed{
\int_{\mathbb R}G_t(a)
\left|\xi\!\left(\frac12+a+i\gamma\right)\right|^2da
=
64\sum_{k=0}^{\infty}
\frac{(2t)^k}{k!}
\left|H_t^{(k)}(2\gamma)\right|^2.
}
\]

Thus a positive horizontal second moment of the classical completed zeta function equals an explicit weighted derivative energy of the de Bruijn--Newman heat flow.

If `H_t` has a zero of multiplicity at least `m` at `x=2 gamma`, then exactly

\[
\boxed{
\int_{\mathbb R}G_t(a)|\xi(1/2+a+i\gamma)|^2da
=
64\sum_{k=m}^{\infty}
\frac{(2t)^k}{k!}|H_t^{(k)}(2\gamma)|^2.
}
\]

For exact multiplicity `m`, the first term on the right is strictly positive. Hence

\[
\boxed{
\mathcal N_t(\gamma)
\ge
64\frac{(2t)^m}{m!}|H_t^{(m)}(2\gamma)|^2>0.
}
\]

This is not a collision exclusion theorem. It is an exact positive energy bridge that converts collision multiplicity into a low-Hermite-mode spectral gap in a horizontal Gaussian `L^2` space.

---

## 1. Gaussian Hermite space

Put

\[
y=\frac a{\sqrt t},
\qquad
X_{t,\gamma}(y):=\xi\!\left(\frac12+\sqrt t\,y+i\gamma\right).
\]

Then

\[
G_t(a)da=\frac{e^{-y^2}}{\sqrt\pi}dy=:d\mu(y).
\]

For the physicists' Hermite polynomials,

\[
\int_{\mathbb R}H_j(y)H_k(y)d\mu(y)
=2^kk!\,\delta_{jk}.
\]

The completed zeta function has at most order-one entire growth, while the Gaussian decays quadratically. Hence

\[
X_{t,\gamma}\in L^2(\mathbb R,d\mu)
\]

for every fixed `t>0` and real `gamma`.

Therefore the Hermite polynomials form a complete orthogonal basis for this horizontal slice.

---

## 2. Hermite coefficients

Define

\[
M_k(t,\gamma)
=\int_{\mathbb R}H_k(y)X_{t,\gamma}(y)d\mu(y).
\]

The Hermite expansion is

\[
X_{t,\gamma}(y)
=\sum_{k=0}^{\infty}c_k(t,\gamma)H_k(y)
\]

in `L^2(dmu)`, where

\[
\boxed{
c_k(t,\gamma)=\frac{M_k(t,\gamma)}{2^kk!}.}
\]

Round 32 proved the exact derivative relation

\[
\boxed{
M_k(t,\gamma)
=8(2\sqrt t)^k i^{-k}H_t^{(k)}(2\gamma).
}
\]

Thus each horizontal Hermite coefficient is exactly a heat-flow derivative channel.

---

## 3. Parseval identity — PROVED

Hermite Parseval gives

\[
\int_{\mathbb R}|X_{t,\gamma}(y)|^2d\mu(y)
=
\sum_{k=0}^{\infty}2^kk!|c_k|^2
=
\sum_{k=0}^{\infty}
\frac{|M_k|^2}{2^kk!}.
\]

Using the Round-32 formula,

\[
|M_k|^2
=64(4t)^k|H_t^{(k)}(2\gamma)|^2.
\]

Therefore

\[
\boxed{
\mathcal N_t(\gamma)
:=\int_{\mathbb R}G_t(a)
|\xi(1/2+a+i\gamma)|^2da
=64\sum_{k=0}^{\infty}
\frac{(2t)^k}{k!}|H_t^{(k)}(2\gamma)|^2.
}
\]

Every term is nonnegative and all constants are explicit.

---

## 4. Collision spectral-gap identity

Suppose `H_t` has multiplicity at least `m` at `x=2 gamma`. Then

\[
H_t^{(0)}(2\gamma)=\cdots=H_t^{(m-1)}(2\gamma)=0.
\]

Equivalently, the horizontal slice is orthogonal to

\[
H_0,H_1,\ldots,H_{m-1}.
\]

Thus Parseval reduces to

\[
\boxed{
\mathcal N_t(\gamma)
=64\sum_{k=m}^{\infty}
\frac{(2t)^k}{k!}|H_t^{(k)}(2\gamma)|^2.
}
\]

If the multiplicity is exactly `m`, then `H_t^{(m)}(2 gamma)!=0`, giving

\[
\boxed{
\mathcal N_t(\gamma)
\ge64\frac{(2t)^m}{m!}|H_t^{(m)}(2\gamma)|^2.
}
\]

For a double collision,

\[
\boxed{
\mathcal N_t(\gamma)
=64\sum_{k=2}^{\infty}\frac{(2t)^k}{k!}|H_t^{(k)}(2\gamma)|^2
\ge128t^2|H_t''(2\gamma)|^2.
}
\]

---

## 5. Low-mode defect energy

Define the low-mode energy through order `m-1` by

\[
\mathcal L_{m,t}(\gamma)
:=
64\sum_{k=0}^{m-1}
\frac{(2t)^k}{k!}|H_t^{(k)}(2\gamma)|^2.
\]

Then

\[
0\le\mathcal L_{m,t}(\gamma)\le\mathcal N_t(\gamma),
\]

and

\[
\boxed{
H_t\text{ has multiplicity at least }m\text{ at }2\gamma
\iff
\mathcal L_{m,t}(\gamma)=0.
}
\]

This creates a positive collision detector different from a signed Laguerre expression: it is a finite sum of squares.

The difficulty has moved to proving a **strict lower bound** on this low-mode fraction from independent horizontal information.

---

## 6. Normalized low-mode concentration ratio

Whenever `mathcal N_t(gamma)>0`, define

\[
\boxed{
\eta_{m,t}(\gamma)
:=\frac{\mathcal L_{m,t}(\gamma)}{\mathcal N_t(\gamma)}\in[0,1].
}
\]

Then an `m`-fold collision is exactly

\[
\boxed{\eta_{m,t}(\gamma)=0.}
\]

For double collisions,

\[
\eta_{2,t}(\gamma)
=
\frac{64\bigl(|H_t(2\gamma)|^2+2t|H_t'(2\gamma)|^2\bigr)}
{\mathcal N_t(\gamma)}.
\]

The numerator is manifestly positive away from collision, and the denominator is an explicit horizontal xi second moment.

This is a useful quantitative reformulation because a theorem of the form

\[
\eta_{2,t}(\gamma)\ge\delta(t,\gamma)>0
\]

can potentially be attacked by horizontal mean-value/large-value estimates rather than by zero-gap dynamics.

---

## 7. Relation to Round 33 sign changes

Round 33 showed that vanishing of the first `m` Hermite coefficients forces at least

\[
\lceil m/2\rceil
\]

sign changes of the horizontal real part and

\[
\lfloor m/2\rfloor
\]

sign changes of the horizontal imaginary part.

Round 34 adds an orthogonal-energy interpretation:

\[
\boxed{
\text{collision}
\Longrightarrow
\text{all horizontal Gaussian }L^2\text{ mass is projected onto Hermite modes }k\ge m.
}
\]

Thus collision creates both oscillation and high-Hermite-mode concentration.

---

## 8. Why this is not Laguerre positivity in disguise

The identity is valid for every entire horizontal slice for which the Gaussian norm is finite. It does not assert a sign for

\[
(H_t')^2-H_tH_t''
\]

or any generalized Laguerre expression.

It is simply Hilbert-space orthogonality plus the unconditional Polymath Gaussian heat representation.

Of course, proving a positive lower bound for `eta_{2,t}` uniformly over all positive `t,gamma` would be strong enough to exclude collisions. Such a bound must therefore be derived from an independent analytic input and cannot be assumed.

---

## 9. New cross-frontier target

The preferred next target is now sharper than the qualitative sign-change localization problem:

> Estimate the horizontal Gaussian norm `mathcal N_t(gamma)` and the first two Hermite coefficients `M_0,M_1` using an unconditional representation of xi, and determine whether current large-value/zero-density technology yields any nontrivial lower bound for
> \[
> \eta_{2,t}(\gamma).
> \]

A useful theorem need not be uniform initially. Even a lower bound in a high-`gamma`, positive-`t` regime not already covered trivially by Polymath would be a genuine bridge result.

---

## 10. Circularity audit

Used:

- Polymath's exact Gaussian heat representation;
- Hermite orthogonality/completeness;
- the Round-32 derivative identity.

Not used:

- RH or `Lambda<=0`;
- real-rootedness at the unknown time;
- Laguerre positivity;
- zero-gap lower bounds;
- negative-time Rodgers--Tao estimates.

---

## 11. Status

- horizontal Gaussian `L^2` finiteness: **PROVED**;
- exact Hermite Parseval energy identity: **PROVED**;
- collision removes first `m` derivative-energy channels: **PROVED**;
- low-mode sum-of-squares collision detector: **PROVED**;
- normalized concentration ratio `eta_m`: **DEFINED / EXACT**;
- independent positive lower bound for `eta_2`: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
