# Current Collision Program State

**Updated:** 2026-08-15 after Round 12.

## Structural pivot

The program no longer treats a globally regularized infinite discriminant as the mandatory first object.

Round 12 proved that for every finite simple real-zero cluster of an entire backward-heat family one has the oriented local collision section

\[
\mathcal D_I(t)=(-1)^{m(m-1)/2}\prod_{k\in I}F_z(t,x_k(t)),
\]

with exact local factorization

\[
\mathcal D_I=\Delta_I A_{\rm tail},\qquad A_{\rm tail}\neq0,
\]

and exact evolution

\[
\frac d{dt}\log|\mathcal D_I|
=\sum_{k\in I}(A_k^2+3B_k),
\]

where

\[
A_k=\frac{F_{zz}}{2F_z}(x_k),
\qquad
B_k=A_k^2-\frac{F_{zzz}}{3F_z}(x_k).
\]

For order-one entire functions,

\[
B_k=\sum_{\rho\neq x_k}(x_k-\rho)^{-2}
\]

is absolutely convergent at each fixed zero. Global renormalization is only needed after summing over infinitely many zero labels.

## Exact Laguerre reduction

Using

\[
L_1=F_z^2-FF_{zz}
\]

and the coefficient identity

\[
L_2=\frac14F_{zz}^2-\frac13F_zF_{zzz}+\frac1{12}FF_{zzzz},
\]

at a simple zero `x_k` one has

\[
L_1(x_k)=F_z(x_k)^2,
\]

\[
L_2(x_k)=F_z(x_k)^2B_k.
\]

Therefore

\[
\boxed{B_k=\frac{L_2(x_k)}{L_1(x_k)}}.
\]

Also

\[
\partial_xL_1(x_k)=F_z(x_k)F_{zz}(x_k),
\]

so

\[
\boxed{A_k=\frac{\partial_xL_1(x_k)}{2L_1(x_k)}}.
\]

Consequently the one-root collision-growth identity can be written

\[
\boxed{
\frac d{dt}\log|F_z(t,x_k(t))|
=\frac14\bigl(\partial_x\log L_1(t,x_k(t))\bigr)^2
+3\frac{L_2(t,x_k(t))}{L_1(t,x_k(t))}.
}
\]

This is an exact bridge between the local collision divisor and the Two-Laguerre program.

## Kernel-side form

With the previously derived associated-kernel identities

\[
L_1=4\,\mathcal C[K_1](2x),
\qquad
L_2=\frac43\,\mathcal C[K_2](2x),
\]

one obtains at a simple zero

\[
\boxed{
\frac d{dt}\log|F_z(t,x_k(t))|
=\frac14\left(\partial_x\log\mathcal C[K_1](2x_k)\right)^2
+\frac{\mathcal C[K_2](2x_k)}{\mathcal C[K_1](2x_k)}.
}
\]

This is the preferred C6 interface: any genuinely new Riemann-kernel inequality should act on this ratio/current, rather than on a formal infinite discriminant.

## Critical global caveat

Excluding every fixed finite collision is not by itself enough to settle the de Bruijn–Newman endpoint. A hypothetical positive `Lambda` can be controlled by collision/near-collision events whose heights tend to infinity. Therefore the C6 estimate must be **uniform in zero height/index**, not merely local for a fixed cluster.

This is mandatory in all future rounds.

## Single next target

Seek an independently provable Riemann-kernel estimate, uniform in zero height, that controls

\[
R_k(t):=
\frac14\bigl(\partial_x\log L_1(t,x_k(t))\bigr)^2
+3\frac{L_2(t,x_k(t))}{L_1(t,x_k(t))}
\]

on each strip `t in [epsilon,t_1]`, strongly enough that a local collision section cannot vanish at a positive time.

A proposal is rejected if its proof assumes any of:

- all zeros remain real below the current time;
- a uniform lower gap bound equivalent to the desired conclusion;
- global `L_1>=0` or `L_2>=0` at unknown times without independent proof;
- an RH-equivalent positivity criterion.

Potential acceptable inputs are restricted to independently established properties of the Riemann kernel, explicit-formula estimates, zero-density/pair-statistic inputs, or a new kernel inequality with a separate non-RH application.

## Status

- Local collision divisor geometry: **PROVED** under stated local hypotheses.
- Root-wise inverse-square trace: **PROVED** for order-one entire functions.
- Laguerre reduction: **PROVED**.
- Kernel ratio representation: **PROVED** from the associated-kernel identities.
- Uniform-in-height C6 estimate: **OPEN**.
- RH: **OPEN**.
- Novelty of the package: **NOVELTY UNVERIFIED**.