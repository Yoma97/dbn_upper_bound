# Round 68 — Rectangular true-weight envelope in `(t,lambda)`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Converts Round 66's pointwise exact-head/convex-tail bound into a rigorous box theorem suitable for adaptive directed-rounding certification.

---

## 1. Why a separate box theorem is necessary

Round 66 is a pointwise theorem. A computer proof over a rectangle may not simply evaluate every ingredient at a visually plausible “worst corner”, because the weight exponent and the moving cutoff depend on `t` in opposite ways.

This round constructs one function that dominates **every true heat weight in the whole box** and one cutoff that dominates every local cutoff. The resulting loss is explicit. If it is too large, the correct response is subdivision.

---

## 2. Box and geometric extrema

Let

\[
B=[t_-,t_+]\times[\lambda_-,\lambda_+]
\]

with

\[
0<t_-\le t_+\le\frac12,
\qquad
4<\lambda_-\le\lambda_+.
\]

At a point of the box put

\[
L=\frac\lambda t,
\qquad
x=4\pi e^L,
\qquad
p(\lambda)=\frac12+\frac\lambda4.
\]

Then

\[
L\ge L_{\min}:=\frac{\lambda_-}{t_+},
\qquad
x\ge x_{\min}:=4\pi e^{L_{\min}}.
\tag{68.1}
\]

Also every real-axis Riemann--Siegel cutoff obeys

\[
\log N
\le
V_B
:=
\frac12\log\left(e^{\lambda_+/t_-}+\frac{t_+}{16}\right).
\tag{68.2}
\]

The same expression, enlarged by the fixed Cauchy radius in the obvious way, is used for a complex-neighbourhood `Ntop`; this round treats the real positive moments only.

---

## 3. One weight dominating the entire box

Round 64 gives, pointwise,

\[
\sigma(t,\lambda)
\ge
\frac12+\frac\lambda4-rac{t}{2x^2}.
\]

Hence throughout `B`,

\[
\boxed{
\sigma(t,\lambda)\ge
\sigma_B
:=
\frac12+\frac{\lambda_-}{4}
-rac{t_+}{2x_{\min}^2}.
}
\tag{68.3}
\]

Because `t<=t_+`, every true amplitude

\[
a_n(t,\lambda)
=
\exp\left(
\frac t4\log^2n-\sigma(t,\lambda)\log n
\right)
\]

satisfies

\[
\boxed{
a_n(t,\lambda)\le F_B(n),}
\tag{68.4}
\]

where

\[
F_B(u)=
\exp\left(
\frac{t_+}{4}\log^2u-\sigma_B\log u
\right).
\tag{68.5}
\]

This is a genuine rectangular domination; it does not assume that `A0` or `A1` themselves are monotone across the moving cutoff.

---

## 4. Monotonicity gate

Writing `v=log u`,

\[
\frac d{dv}\log F_B(e^v)
=
\frac{t_+}{2}v-\sigma_B.
\]

Therefore a sufficient condition for `F_B` to be decreasing over the entire possible tail is

\[
\boxed{
\mu_B:=\sigma_B-rac{t_+}{2}V_B>0.
}
\tag{68.6}
\]

For the logarithmic moment, `F_B(u)log u` is decreasing for `u>=K` if

\[
\boxed{
\mu_B>\frac1{\log K}.
}
\tag{68.7}
\]

These are **acceptance gates** for the box envelope. A box that fails them is not evidence of a mathematical failure; subdivide it in `t` and/or `lambda`.

---

## 5. Convex counting-measure exponent

Under `u=e^v`,

\[
F_B(u)\,du=e^{g_B(v)}\,dv,
\]

where

\[
\boxed{
g_B(v)=\frac{t_+}{4}v^2-(\sigma_B-1)v.}
\tag{68.8}
\]

Again

\[
\boxed{g_B''(v)=t_+/2>0.}
\tag{68.9}
\]

Fix an integer `K>=2` satisfying

\[
\log K<V_B.
\]

Put

\[
r=\log K,
\qquad
D_B=V_B-r,
\]

\[
m_B=rac{g_B(V_B)-g_B(r)}{D_B}.
\tag{68.10}
\]

Convexity yields

\[
g_B(v)\le g_B(r)+m_B(v-r)
\qquad(r\le v\le V_B).
\tag{68.11}
\]

---

## 6. Uniform A0 bound on the box

Assume (68.6). Since `F_B` is decreasing and every true cutoff satisfies `log N<=V_B`,

\[
\sum_{n=K+1}^{N}a_n(t,\lambda)
\le
\int_K^{e^{V_B}}F_B(u)\,du.
\]

Define

\[
\mathfrak F_0(m,D)=
\begin{cases}
(e^{mD}-1)/m,&m\ne0,\\
D,&m=0.
\end{cases}
\]

Then

\[
\boxed{
A_0(t,\lambda)
\le
A_{0,B}^{\rm up}
:=
\sum_{n=2}^{K}F_B(n)
+e^{g_B(r)}\mathfrak F_0(m_B,D_B)
}
\tag{68.12}
\]

for every point in `B` whose cutoff is at least `K`. If a box contains a smaller cutoff, the finite head is truncated accordingly and is easier.

---

## 7. Uniform A1 bound on the box

Assume the stronger gate (68.7). Define

\[
\mathfrak F_1(m,D)=
\begin{cases}
\dfrac{e^{mD}(mD-1)+1}{m^2},&m\ne0,\\
D^2/2,&m=0.
\end{cases}
\]

Then

\[
\boxed{
A_1(t,\lambda)
\le
A_{1,B}^{\rm up}
:=
\sum_{n=2}^{K}F_B(n)\log n
+
 e^{g_B(r)}
\left[
 r\mathfrak F_0(m_B,D_B)
+\mathfrak F_1(m_B,D_B)
\right].
}
\tag{68.13}
\]

The complexity is `O(K)` per box regardless of the actual Riemann--Siegel cutoff.

---

## 8. Uniform phase-speed and amplitude-derivative bounds

For `x>=x_min` in the intended large-x region,

\[
A=\Re\alpha
\ge
\frac L2-\frac1{x^2},
\]

and `A>0,B<0,C>0,D>0`, so

\[
\Re\beta_t=A+\frac t2(AC-BD)\ge A.
\]

Hence

\[
\boxed{
\Phi=|\phi_x|
\ge
\Phi_B^{\rm lo}
:=
\frac{\lambda_-}{4t_+}
-rac1{2x_{\min}^2}.
}
\tag{68.14}
\]

Using

\[
0<C\le\frac7{x^2},
\qquad
0<D\le\frac1x+\frac5{x^3},
\]

we also obtain

\[
\boxed{
d\le d_B^{\rm up}:=
\sqrt{
\left[
\frac{t_+}{4}
\left(\frac1{x_{\min}}+\frac5{x_{\min}^3}\right)
\right]^2
+
\frac14
\left(1+rac{7t_+}{2x_{\min}^2}\right)^2
}.
}
\tag{68.15}
\]

Thus a box-level phase-slope core lower bound is available without evaluating any oscillatory trigonometric sum.

---

## 9. Box-level PSC interface

Let a separate certified error module provide

\[
E_0(t,\lambda)\le E_{0,B}^{\rm up},
\qquad
E_1(t,\lambda)\le E_{1,B}^{\rm up}
\]

throughout `B`, including the fixed-cutoff jump bridge.

Put

\[
S_{0,B}^{\rm lo}=1-A_{0,B}^{\rm up}.
\]

If

\[
S_{0,B}^{\rm lo}>E_{0,B}^{\rm up}/2
\tag{68.16}
\]

and

\[
\boxed{
2\left[
\Phi_B^{\rm lo}
\sqrt{(S_{0,B}^{\rm lo})^2-(E_{0,B}^{\rm up}/2)^2}
-d_B^{\rm up}A_{1,B}^{\rm up}
\right]
>E_{1,B}^{\rm up},
}
\tag{68.17}
\]

then the entire rectangle `B` is collision-free.

This is the precise theorem that the adaptive `(t,lambda)` tiler must implement.

---

## 10. Dependency / interval audit

The potentially dangerous dependency is visible in

\[
V_B=\frac12\log(e^{\lambda_+/t_-}+t_+/16),
\]

while the weight coefficient uses `t_+`.

For a wide box this combines a long cutoff coming from `t_-` with a heavy heat weight coming from `t_+`. This is deliberately conservative. The monotonicity gates (68.6)--(68.7) detect when that mixing has become too destructive.

Therefore the tiler should prioritize subdivision in `t` when `mu_B` is small.

No affine arithmetic is needed to understand this particular loss; it is structural interval dependency caused by the moving cutoff.

---

## 11. Circularity audit

Inputs:

- the exact real-axis heat weights from the unconditional Polymath model;
- Round 64's elementary lower bound for `sigma`;
- moving-cutoff geometry;
- monotone integral comparison;
- convexity of the quadratic exponent;
- elementary real-axis `alpha,alpha'` bounds.

Not used:

- RH;
- `Lambda<=0`;
- zero locations or gaps;
- GUE/pair correlation;
- Laguerre--Polya assumptions;
- numerical RH verification.

Thus the rectangular envelope is an unconditional analytic tool.

---

## 12. Next module

Round 69 should construct the matching rectangular error envelope

\[
(E_{0,B}^{\rm up},E_{1,B}^{\rm up})
\]

directly from Polymath (20)--(24), the symmetric normalization ratio, and the cutoff-jump bridge.

Only after Rounds 68--69 are combined should the adaptive tiler attempt the exploratory target `lambda>=7.10`.
