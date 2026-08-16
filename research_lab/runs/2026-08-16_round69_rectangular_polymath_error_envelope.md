# Round 69 — Rectangular Polymath/Cauchy error envelope in `(t,lambda)`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Supplies the box-level `(E0,E1)` module required by Round 68, while avoiding the false requirement that one Riemann--Siegel cutoff be fixed across an entire parameter rectangle.

---

## 1. Geometry and the pointwise fixed-cutoff convention

Let

\[
B=[t_-,t_+]\times[\lambda_-,\lambda_+]
\]

with

\[
0<t_-\le t_+\le1/2,
\qquad
4<\lambda_-\le\lambda_+,
\]

and fix

\[
0<\rho\le0.1.
\]

At each parameter point define

\[
x_c=4\pi e^{\lambda/t}.
\]

For Cauchy's estimate at this **one parameter point**, choose

\[
N_0(t,\lambda)
=
\left\lfloor
\sqrt{
\frac{x_c-\rho}{4\pi}+rac t{16}}
\right\rfloor.
\tag{69.1}
\]

This is no larger than every local Polymath cutoff on the disk `|z-x_c|<=rho`.

Crucially, `N0(t,lambda)` is allowed to vary across the parameter box. Cauchy's derivative theorem is applied pointwise in `z` at fixed `(t,lambda)`; it does **not** require the same integer cutoff for two different parameter points.

Across the single Cauchy disk, the argument

\[
\frac{\Re z}{4\pi}+rac t{16}
\]

changes by only

\[
\frac{2\rho}{4\pi}<0.016.
\]

Therefore the local Riemann--Siegel cutoff differs from the pointwise base cutoff (69.1) by at most one. Only this one possible jump is absorbed into the pointwise remainder.

This observation prevents an artificial, enormous `Ntop-Nbase` loss when a `(t,lambda)` box spans many distinct cutoffs.

---

## 2. Box geometry

Put

\[
X_c^-:=4\pi e^{\lambda_-/t_+},
\qquad
X_c^+:=4\pi e^{\lambda_+/t_-},
\]

and

\[
X_-:=X_c^- -\rho,
\qquad
X_+:=X_c^+ +\rho.
\tag{69.2}
\]

Assume `X_->200` so the whole upper semicircle remains in the Polymath Theorem-1.3 region.

Define

\[
h_\rho^-:=-\log\left(1-\frac\rho{X_c^-}\right)>0,
\]

\[
h_\rho^+:=\log\left(1+\frac\rho{X_c^-}\right)>0.
\tag{69.3}
\]

For every disk point `z=x'+iy`, `0<=y<=rho`, one has

\[
\frac\lambda t-h_\rho^-
\le
\log\frac{x'}{4\pi}
\le
\frac\lambda t+h_\rho^+.
\tag{69.4}
\]

The use of `X_c^-` in both small geometry corrections is conservative and uniform.

---

## 3. Lower exponent in the positive error sums

Polymath (21) gives

\[
\Re s_*
\ge
\frac{1+y}{2}
+rac t4\log\frac{x'}{4\pi}
-R_s,
\]

where, uniformly on the box,

\[
R_s
\le
R_{s,B}:=
\frac{t_+}{2X_-^2}
\left(
1+rac{4\rho(1+\rho)}{X_-^2}
\right).
\tag{69.5}
\]

Using (69.4) and `lambda>=lambda_-`,

\[
\Re s_*
\ge
\sigma_{E,B}
:=
\frac12+rac{\lambda_-}{4}
-rac{t_+h_\rho^-}{4}
-R_{s,B}.
\tag{69.6}
\]

Thus

\[
\frac{b_n^t}{n^{\Re s_*}}
\le
F_E(n)
:=
\exp\left(
\frac{t_+}{4}\log^2n
-\sigma_{E,B}\log n
\right).
\tag{69.7}
\]

This dominates the first positive series in Polymath (23) throughout the box and the Cauchy disks.

---

## 4. The gamma/kappa multiplier

Polymath (20), (22) give

\[
|\gamma|
\le
e^{0.02y}
\left(\frac{x'}{4\pi}\right)^{-y/2}
\le e^{0.02\rho},
\]

and

\[
|\kappa|
\le
\frac{t_+\rho}{2(X_- -6)}
=:\kappa_B.
\tag{69.8}
\]

Every local cutoff satisfies

\[
N\le N_B^+
:=
\sqrt{
\frac{X_+}{4\pi}+rac{t_+}{16}},
\]

so with

\[
V_E:=\log N_B^+,
\]

we obtain

\[
|\gamma|N^{|\kappa|}
\le
G_B:=
\exp(0.02\rho+\kappa_B V_E).
\tag{69.9}
\]

Hence the positive factor in (23) satisfies

\[
1+|\gamma|N^{|\kappa|}n^y
\le
1+G_B n^\rho.
\tag{69.10}
\]

---

## 5. Closed positive-sum module

For `sigma>0` define

\[
F_{B,\sigma}(u)
=
\exp\left(
\frac{t_+}{4}\log^2u-\sigma\log u
\right).
\]

Let

\[
\mathscr S_B(\sigma;K)
\]

denote the Round-68 exact-head/convex-secant upper bound for

\[
\sum_{n\le N}F_{B,\sigma}(n)
\]

with upper logarithmic cutoff `V_E`. Explicitly, when the corresponding decreasing-tail gate is satisfied,

\[
\mathscr S_B(\sigma;K)
=
1+
\sum_{n=2}^{K}F_{B,\sigma}(n)
+e^{g_\sigma(r)}\mathfrak F_0(m_\sigma,D),
\tag{69.11}
\]

where

\[
g_\sigma(v)=\frac{t_+}{4}v^2-(\sigma-1)v,
\quad r=\log K,
\quad D=V_E-r,
\]

and `m_sigma` is the secant slope between `r` and `V_E`.

The factor `n^rho` is absorbed by replacing `sigma` with `sigma-rho`. Therefore

\[
\sum_{n\le N}(1+G_Bn^\rho)F_E(n)
\le
\boxed{
Z_{E,B}:=
\mathscr S_B(\sigma_{E,B};K)
+G_B\mathscr S_B(\sigma_{E,B}-\rho;K).
}
\tag{69.12}
\]

A box failing either tail-decrease gate is subdivided; no sign claim is inferred from such a failure.

---

## 6. Uniform exponential-error factor in e_A+e_B

Polymath (23) contains

\[
\exp\left(
\frac{rac{t^2}{16}
\log^2\frac{x'}{4\pi n^2}+0.626}
{x'-6.66}
\right)-1.
\]

For `n<=N`, the positive part of

\[
\log\frac{x'}{4\pi n^2}
\]

is at most `log(x'/(4pi))`, while its negative part near the moving cutoff is tiny. A safe uniform bound is obtained from

\[
U_B:=
\lambda_+ + t_+h_\rho^+ +\frac{t_+^2}{16}e^{-\lambda_-/t_+},
\tag{69.13}
\]

which dominates

\[
t\left|\log\frac{x'}{4\pi n^2}\right|.
\]

Thus put

\[
H_B:=
\frac{U_B^2/16+0.627}{X_- -6.66}.
\tag{69.14}
\]

The harmless enlargement `0.626 -> 0.627` absorbs the small neighbourhood simplifications.

Then

\[
\boxed{
(e_A+e_B)_B^{\rm up}
:=Z_{E,B}(e^{H_B}-1)
}
\tag{69.15}
\]

is a uniform box upper bound.

---

## 7. Uniform e_C,0 bound

From (69.4),

\[
t\log\frac{x'}{4\pi}
\ge
W_B:=\lambda_- -t_+h_\rho^-.
\tag{69.16}
\]

Assume `W_B>0`.

Since

\[
-\frac14L'-\frac t{16}(L')^2
=-\frac1t\left(
\frac{tL'}4+rac{(tL')^2}{16}
\right),
\]

and `t<=t_+`, the main negative exponent in Polymath (24) obeys

\[
-\frac{1+y}{4}L'-\frac t{16}(L')^2
\le
-\frac1{t_+}
\left(
\frac{W_B}{4}+rac{W_B^2}{16}
\right).
\tag{69.17}
\]

For the cutoff correction define the lower pointwise base cutoff

\[
N_B^-:=
\left\lfloor
\sqrt{
\frac{X_c^- -\rho}{4\pi}+rac{t_-}{16}}
\right\rfloor.
\tag{69.18}
\]

Assume `N_B^->1`.

Also define

\[
L_B^+:=rac{\lambda_+}{t_-}+h_\rho^+.
\tag{69.19}
\]

Then Polymath (24) gives

\[
\boxed{
(e_{C,0})_B^{\rm up}
:=
\exp\left[
-\frac1{t_+}
\left(
\frac{W_B}{4}+rac{W_B^2}{16}
\right)
+
\frac{1.24(3^\rho+3^{-\rho})}{N_B^- -0.125}
+
\frac{3\sqrt{(L_B^+)^2+\pi^2/4}+10.44}{X_- -12}
\right].
}
\tag{69.20}
\]

This is uniform over the full Cauchy upper semicircles.

---

## 8. The pointwise cutoff-jump bridge

Although `N0(t,lambda)` varies across the parameter rectangle, its disk-local jump is at most one.

A lower bound for every pointwise base cutoff is `N_B^-`. If the shifted weight

\[
F_E(n)(1+G_Bn^\rho)
\]

is decreasing for `n>=N_B^-`, the possible one-term jump is bounded by

\[
\boxed{
J_B^{\rm up}
:=
F_E(N_B^-)
\left(1+G_B(N_B^-)^\rho\right).
}
\tag{69.21}
\]

If the monotonicity gate fails, the box is subdivided or the finite maximum over the short relevant range is evaluated directly.

This is the correct cutoff treatment in `(t,lambda)` boxes. One does not sum from the smallest cutoff in the whole parameter box to the largest cutoff in that box.

---

## 9. Box value error

Define

\[
\boxed{
E_{0,B}^{\rm up}
:=
(e_A+e_B)_B^{\rm up}
+(e_{C,0})_B^{\rm up}
+J_B^{\rm up}.
}
\tag{69.22}
\]

This uniformly bounds the fixed-point normalized remainder at every real center in `B`.

---

## 10. Symmetric normalization ratio

For

\[
s_+=(1+y-ix')/2,
\qquad
s_-=(1-y+ix')/2,
\]

Schwarz symmetry gives

\[
\Re\log M_t(s_-)
=
\Re\log M_t(\overline{s_-}),
\]

and `s_+` differs from `overline{s_-}` by the short real displacement `y`.

Hence

\[
\left|\frac{B_t}{D_t}\right|
\le
\exp\left(
\frac y2\sup|\beta_t|
\right),
\qquad
\beta_t=\alpha+\frac t2\alpha\alpha'.
\tag{69.23}
\]

Using the elementary Polymath bounds for `alpha,alpha'` in the large-`x` rectangle, a deliberately loose box bound is

\[
\sup|\beta_t|\le L_B^+ +2.
\tag{69.24}
\]

Therefore

\[
\boxed{
R_B^{\rm up}
:=
\exp\left(
\frac\rho2(L_B^+ +2)
\right)
}
\tag{69.25}
\]

satisfies

\[
|B_t/D_t|\le R_B^{\rm up}
\]

on every Cauchy circle in the box.

This is intentionally conservative; a later implementation may use the sharper direct interval evaluation of `beta_t`.

---

## 11. Cauchy derivative error

By Schwarz symmetry, the upper semicircle bound extends to the full circle. Thus Cauchy's estimate gives

\[
\boxed{
E_{1,B}^{\rm up}
:=
\frac{R_B^{\rm up}}{\rho}
E_{0,B}^{\rm up}.
}
\tag{69.26}
\]

This is the error quantity entering Round 68's box PSC test.

---

## 12. Complete box certificate

Combine Round 68 with (69.22), (69.26).

A rectangle is certified collision-free if all analytic gates hold and

\[
S_{0,B}^{\rm lo}=1-A_{0,B}^{\rm up}
>E_{0,B}^{\rm up}/2,
\]

and

\[
2\left[
\Phi_B^{\rm lo}
\sqrt{(S_{0,B}^{\rm lo})^2-(E_{0,B}^{\rm up}/2)^2}
-d_B^{\rm up}A_{1,B}^{\rm up}
\right]
>E_{1,B}^{\rm up}.
\tag{69.27}
\]

Every quantity in this test is non-oscillatory and is evaluable by directed rounding.

---

## 13. Failure labels supplied by the module

A failed box should report one of:

- `WEIGHT_MONOTONICITY_GATE` — Round-68/69 convex tail too wide; split mainly in `t`;
- `JUMP_MONOTONICITY_GATE` — pointwise one-jump envelope not monotone at `N_B^-`;
- `POLYMATH_REGION` — `X_-<=200` or another theorem-domain failure;
- `TRIANGLE_SIGN` — `S0` lower bound is nonpositive/too small;
- `REMAINDER_DOMINATES` — `E0/E1` is the leading failure;
- `PSC_CORE` — analytic phase/amplitude core itself fails;
- `CERTIFIED`.

This makes the next tiler diagnostic rather than merely Boolean.

---

## 14. Circularity audit

Inputs:

- unconditional Polymath Theorem 1.3 inequalities (20)--(24);
- the pointwise fixed-cutoff construction already used by the certified joint-jet program;
- Schwarz symmetry;
- Cauchy's estimate;
- Round 68's positive convex-tail module;
- elementary logarithmic geometry.

Not used:

- RH;
- `Lambda<=0`;
- numerical RH verification;
- zero spacings or real-rootedness;
- GUE/pair correlation;
- Laguerre--Polya positivity.

The box error theorem is therefore non-circular.

---

## 15. Implementation gate

The next executable must implement Rounds 68--69 literally with separate MPFR lower/upper variables. It must first reproduce the already certified `lambda=10.52` region, then attack the exploratory target `lambda=7.10`.

No threshold is lowered by this round alone.
