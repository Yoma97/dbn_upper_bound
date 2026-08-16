# Round 70 — Analytic small-time closure for `lambda >= 7.10`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED + independent 512/768-bit scalar arithmetic audit.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Closes the singular end `0<t<=0.01` of the proposed `lambda=7.10` shoulder improvement without any infinite sequence of numerical boxes.

---

## 1. Theorem

Let

\[
\lambda=t\log\frac{x}{4\pi}.
\]

For every real `x>0` satisfying

\[
0<t\le0.01,
\qquad
7.10\le\lambda\le10.52,
\]

one has

\[
\boxed{(H_t(x),H_t'(x))\neq(0,0).}
\tag{70.1}
\]

By evenness the same statement holds for negative `x`.

The proof uses only the unconditional Polymath effective approximation, the phase-slope transversality certificate, elementary positive-series estimates, and directed-rounding scalar arithmetic.

---

## 2. Extreme large-`x` geometry

Put

\[
L=\frac\lambda t.
\]

In the present range

\[
L\ge710.
\tag{70.2}
\]

A rational Taylor lower bound gives `e^7>1000`; hence `e^700>10^300`. Since `4pi>12`,

\[
x=4\pi e^L>12\cdot10^{300}.
\]

Fix the Cauchy radius

\[
\rho=0.1.
\]

Every point of the corresponding disk has real part greater than `10^301`. Consequently every displacement correction appearing below is vastly smaller than `10^-4`. We use that deliberately excessive common allowance rather than optimize constants.

In particular, on the real axis

\[
\sigma
=\frac12+\frac\lambda4+\eta,
\qquad
-10^{-4}<\eta\le0.
\tag{70.3}
\]

The actual correction is exponentially smaller.

---

## 3. Head/tail split for the true phase amplitudes

The real phase weights are

\[
a_n
=
\exp\left(
\frac t4(\log n)^2-\sigma\log n
\right).
\]

Split them by

\[
u=t\log n.
\]

### Head: `u<=1`

Here

\[
\frac t4(\log n)^2
=\frac u4\log n
\le\frac14\log n.
\]

Using (70.3) and `lambda>=7.10`,

\[
\sigma-\frac t4\log n
>
\frac12+\frac{7.10}{4}-\frac14-10^{-4}
>2.024.
\]

Thus

\[
\boxed{a_n\le n^{-2.024}}
\qquad(u\le1).
\tag{70.4}
\]

### Tail: `u>1`

For every term before the real Riemann--Siegel cutoff,

\[
\log n
\le
\frac12\log\left(e^{\lambda/t}+\frac t{16}\right).
\]

Therefore

\[
\frac t4\log n
\le
\frac\lambda8+
\frac t8\log\left(1+rac t{16}e^{-\lambda/t}\right)
<
\frac\lambda8+10^{-4}.
\]

Together with (70.3),

\[
\sigma-\frac t4\log n
>
\frac12+rac\lambda8-2\cdot10^{-4}
\ge1.3873.
\]

Hence

\[
\boxed{a_n\le n^{-1.387}}
\qquad(u>1).
\tag{70.5}
\]

The tail condition `u>1` also gives

\[
\log n>1/t\ge100.
\tag{70.6}
\]

---

## 4. Explicit `A0,A1` bounds

For a decreasing power `u^{-s}`,

\[
\sum_{n=2}^{\infty}n^{-s}
\le
2^{-s}+\frac{2^{1-s}}{s-1}.
\]

For `s=2.024`, the 512/768-bit directed scalar audit gives

\[
A_{0,\rm head}
\le0.72610114058969122.
\tag{70.7}
\]

Similarly, since `(log u)u^{-2.024}` is decreasing for `u>=2`,

\[
\sum_{n=2}^{\infty}(\log n)n^{-s}
\le
(\log2)2^{-s}
+2^{1-s}
\left(
\frac{\log2}{s-1}+rac1{(s-1)^2}
\right),
\]

and the audit gives

\[
A_{1,\rm head}
\le0.97226529246666071.
\tag{70.8}
\]

For the tail put

\[
q=1.387,
\qquad M=e^{100}.
\]

By (70.6), every tail integer exceeds `M`. The decreasing integral test gives

\[
\sum_{n>M}n^{-q}
\le M^{-q}+\frac{M^{1-q}}{q-1}
\le4.0280289694592933\times10^{-17},
\tag{70.9}
\]

and

\[
\sum_{n>M}(\log n)n^{-q}
\le
(\log M)M^{-q}
+M^{1-q}
\left(
\frac{\log M}{q-1}+rac1{(q-1)^2}
\right)
\le4.1321124053626342\times10^{-15}.
\tag{70.10}
\]

Consequently

\[
\boxed{A_0<0.727,\qquad A_1<0.973,\qquad S_0=1-A_0>0.273.}
\tag{70.11}
\]

No oscillatory cancellation has been used.

---

## 5. Phase speed and amplitude derivative

On the real axis the exact formulas recorded in the phase-slope note give

\[
\Phi=|\phi_x|
\ge\frac L4-\frac1{2x^2}.
\]

From `L>=710`,

\[
\boxed{\Phi>177.49.}
\tag{70.12}
\]

Also

\[
\sigma_x=\frac t4D,
\qquad
\tau_x=-\frac12\left(1+\frac t2C\right),
\]

with

\[
0<C\le7/x^2,
\qquad
0<D\le1/x+5/x^3.
\]

Thus throughout this range

\[
\boxed{d=\sqrt{\sigma_x^2+\tau_x^2}<0.501.}
\tag{70.13}
\]

---

## 6. Polymath positive-error sums

On the upper Cauchy semicircle `0<=y<=0.1`, all neighborhood and saddle corrections are smaller than `10^-4` by Section 2.

The first positive series in Polymath (23) therefore has effective power at least

\[
\frac12+rac{7.10}{8}-2\cdot10^{-4}>1.387,
\]

while after the possible `n^y` multiplier the second has effective power at least

\[
\frac{1-0.1}{2}+rac{7.10}{8}-2\cdot10^{-4}>1.337.
\]

Polymath (20), (22) and the enormous lower bound for `x` give

\[
|\gamma|N^{|\kappa|}<1.004.
\tag{70.14}
\]

Using only

\[
\zeta(s)\le1+\frac1{s-1}
\qquad(s>1),
\]

we obtain

\[
\zeta(1.387)+1.004\zeta(1.337)<8.
\tag{70.15}
\]

For the exponential error factor in Polymath (23), every local summand satisfies

\[
t\left|\log\frac{x'}{4\pi n^2}\right|<10.53.
\]

The denominator `x'-6.66` exceeds `e^{lambda/t}`. Therefore

\[
h_n
<8e^{-7.10/t}.
\]

Since `h_n<1` and `e^h-1<2h` on `[0,1]`, (70.15) gives

\[
\boxed{e_A+e_B<128e^{-7.10/t}.}
\tag{70.16}
\]

---

## 7. `e_C,0`

For disk points let

\[
L'=\log\frac{x'}{4\pi}.
\]

The disk displacement is exponentially tiny, so

\[
tL'>7.
\tag{70.17}
\]

The main exponent in Polymath (24) therefore obeys

\[
-\frac{1+y}{4}L'-\frac t{16}(L')^2
\le
-\frac1t\left(\frac74+\frac{49}{16}\right)
=-\frac{4.8125}{t}.
\]

The first positive correction in (24) is less than `1/2`: the cutoff is already far larger than `100`. The second is also less than `1/2`; after the elementary estimate

\[
\sqrt{(L')^2+\pi^2/4}\le L'+\pi/2,
\]

the ratio is bounded by a decreasing multiple of `(3L'+16)e^{-L'}` for `L'>710`.

Hence

\[
\boxed{e_{C,0}<e^{1-4.8125/t}.}
\tag{70.18}
\]

---

## 8. Pointwise cutoff jump

For the pointwise fixed-cutoff Cauchy construction, the disk-local Riemann--Siegel cutoff changes by at most one.

The base cutoff satisfies

\[
N_0>\frac12e^{\lambda/(2t)}.
\tag{70.19}
\]

The possible extra normalized term is bounded by the two effective powers from Section 6:

\[
n^{-1.387}+1.004n^{-1.337}
<2.004n^{-1.337}.
\]

Using (70.19),

\[
\boxed{
E_{\rm jump}
<6e^{-4.74635/t},
}
\tag{70.20}
\]

because

\[
\frac{1.337\cdot7.10}{2}=4.74635.
\]

---

## 9. Cauchy derivative remainder

The separately audited symmetric-normalization identity gives

\[
\left|\frac{B_t}{D_t}\right|
\le
\exp\left(\frac\rho2\sup|\beta_t|\right).
\]

The elementary Polymath logarithmic-derivative bound implies in the present strip

\[
\boxed{
\left|\frac{B_t}{D_t}\right|
<\exp(0.526/t+0.2).
}
\tag{70.21}
\]

Define

\[
E_0(t)
:=128e^{-7.10/t}
+e^{1-4.8125/t}
+6e^{-4.74635/t}.
\tag{70.22}
\]

Equations (70.16), (70.18), (70.20) give the pointwise normalized value remainder `<=E0(t)`.

Cauchy's estimate gives

\[
E_1(t)
\le
10e^{0.526/t+0.2}E_0(t).
\tag{70.23}
\]

Every net exponential rate is positive:

\[
7.10-0.526=6.574,
\]

\[
4.8125-0.526=4.2865,
\]

\[
4.74635-0.526=4.22035.
\]

Therefore both `E0(t)` and the right side of (70.23) increase with `t` on `(0,0.01]`. It suffices to evaluate them at `t=0.01`.

The independent 512/768-bit scalar audit gives

\[
\boxed{E_0<4.4366322071234693\times10^{-206},}
\tag{70.24}
\]

\[
\boxed{E_1<3.7827015035898539\times10^{-182}.}
\tag{70.25}
\]

---

## 10. PSC contradiction

At a hypothetical multiple real zero, the phase-slope certificate would require

\[
|p'|\le E_1.
\]

But (70.7)--(70.13), together with the exact tail bounds and (70.24), imply

\[
\sqrt{S_0^2-(E_0/2)^2}
\ge0.27389885941030878
\]

and

\[
2\left[
\Phi\sqrt{S_0^2-(E_0/2)^2}-dA_1
\right]
\ge96.25440729041982.
\]

Thus the certified contradiction margin is

\[
\boxed{
96.25440729041982-E_1>96.25>0.
}
\tag{70.26}
\]

This proves (70.1).

---

## 11. Directed-rounding audit

Canonical audit source:

`research_lab/certificates/low_shoulder/small_time_lambda710_audit.c`.

It is compiled independently at 512 and 768 bits. Both runs reproduce the outward decimal projections in Sections 4, 9, 10 and return

`AUDIT_RESULT pass=1`.

The audit checks only scalar arithmetic after the analytic inequalities above have reduced the infinite problem to explicit elementary expressions.

---

## 12. Circularity audit

Used:

1. unconditional Polymath Theorem 1.3 / Corollary 6.5;
2. the established phase-slope algebra;
3. Schwarz symmetry and Cauchy's estimate;
4. elementary positive-series/integral bounds;
5. explicit large-`x` geometry;
6. MPFR directed rounding for final scalar constants.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- real-rootedness of `H_0`;
- numerical RH verification;
- zero-spacing or pair-correlation input;
- GUE;
- Laguerre--Polya membership;
- Rodgers--Tao negative-time estimates whose proof assumes `Lambda<0` for contradiction.

No hidden RH-equivalent input occurs.

---

## 13. Scope

Round 70 proves only the small-time middle shoulder

\[
0<t\le0.01,
\qquad
7.10\le\lambda\le10.52.
\]

The complementary rectangle

\[
0.01\le t\le0.5,
\qquad
7.10\le\lambda\le10.52
\]

is a separate finite-certification task (Rounds 68--69 plus the MPFR tiler).

The already proved high-shoulder theorem covers `lambda>=10.52`.

No statement about RH follows until all lower-shoulder and bounded-core regions are also closed.
