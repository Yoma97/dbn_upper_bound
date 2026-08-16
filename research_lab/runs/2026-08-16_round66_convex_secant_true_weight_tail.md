# Round 66 — Convex-secant tail bounds for the true heat weights

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Replaces the impractically conservative near-`q=1` moment majorant by an exact finite head plus a closed-form convex tail. This is designed for the practical `t_epsilon` and compact-bridge certification.

---

## 1. Motivation

Round 64 proves the exact-weight zeta-moment limit with an `O(t)` error, but its simple global domination

\[
a_n\le n^{-q}
\]

uses a `q` close to `1` when `lambda` approaches the low shoulder. Then `Z_2(q),Z_3(q)` are large. This is harmless for the existence theorem but can make the resulting certified `t_epsilon` unnecessarily tiny.

We therefore keep a finite head exactly and bound the huge remaining moving-cutoff tail without summing it term by term.

---

## 2. Weight majorant

Put

\[
L=\frac\lambda t,
\qquad
x=4\pi e^L,
\qquad
p=\frac12+\frac\lambda4.
\]

From Round 64,

\[
\sigma\ge \underline\sigma
:=p-\frac{t}{2x^2}.
\tag{66.1}
\]

Thus for every positive integer `n`,

\[
a_n
=\exp\left(\frac t4\log^2n-\sigma\log n\right)
\le
F(n),
\]

where

\[
F(u)=\exp\left(\frac t4\log^2u-\underline\sigma\log u\right).
\tag{66.2}
\]

Let

\[
V:=\frac12\log\left(e^L+\frac t{16}\right).
\tag{66.3}
\]

Every real-axis Riemann--Siegel cutoff satisfies `log N<=V`.

---

## 3. Monotonicity through the whole moving cutoff

Writing `v=log u`,

\[
\frac{d}{dv}\log F(e^v)
=\frac t2v-\underline\sigma.
\]

For `v<=V`,

\[
\frac t2v
\le
\frac\lambda4+
\frac t4\log\left(1+\frac t{16}e^{-L}\right)
\le
\frac\lambda4+rac{t^2}{64}e^{-L}.
\]

Hence

\[
\frac{d}{dv}\log F(e^v)
\le
-\frac12+\delta_{\rm dec},
\]

where

\[
\boxed{
\delta_{\rm dec}(t,\lambda)
:=
\frac{t}{2x^2}+rac{t^2}{64}e^{-L}.
}
\tag{66.4}
\]

Whenever `delta_dec<1/2`, `F` is strictly decreasing through the entire cutoff.

In the project region `0<t<=1/2, lambda>4`, this condition has enormous slack.

---

## 4. Convex logarithmic tail

After the change of variables `u=e^v`,

\[
F(u)\,du=e^{g(v)}\,dv,
\]

with

\[
\boxed{
g(v)=\frac t4v^2-(\underline\sigma-1)v.}
\tag{66.5}
\]

The crucial observation is

\[
\boxed{g''(v)=t/2>0.}
\tag{66.6}
\]

Thus `g` is convex.

Fix an integer `K>=2` with `K<N` and put

\[
r=\log K,
\qquad
D=V-r,
\]

\[
g_r=g(r),
\qquad
g_V=g(V),
\qquad
m=\frac{g_V-g_r}{D}.
\tag{66.7}
\]

By convexity, for `r<=v<=V`,

\[
\boxed{
g(v)\le g_r+m(v-r).}
\tag{66.8}
\]

This remains valid whether `m` is negative, zero, or positive.

---

## 5. Closed-form A0 tail

Because `F` is decreasing,

\[
\sum_{n=K+1}^{N}a_n
\le
\sum_{n=K+1}^{N}F(n)
\le
\int_K^N F(u)\,du
\le
\int_r^V e^{g(v)}\,dv.
\tag{66.9}
\]

Define

\[
\mathfrak F_0(m,D)=
\begin{cases}
\dfrac{e^{mD}-1}{m},&m\ne0,\\[6pt]
D,&m=0.
\end{cases}
\tag{66.10}
\]

Then (66.8) gives

\[
\boxed{
T_0(K;t,\lambda)
:=
\sum_{n=K+1}^{N}a_n
\le
e^{g_r}\mathfrak F_0(m,D).
}
\tag{66.11}
\]

No dependence linear in the astronomical cutoff `N` remains.

---

## 6. Closed-form A1 tail

For the logarithmic moment we need monotonicity of `F(u) log u`. Its logarithmic derivative in `v` is

\[
\frac t2v-\underline\sigma+\frac1v.
\]

Therefore it is decreasing on `[K,e^V]` whenever

\[
\boxed{
\frac1{\log K}<\frac12-\delta_{\rm dec}.
}
\tag{66.12}
\]

For the intended choice `K>=8`, this condition is automatic in the project region.

Hence

\[
\sum_{n=K+1}^{N}a_n\log n
\le
\int_r^V v e^{g(v)}\,dv.
\tag{66.13}
\]

Define

\[
\mathfrak F_1(m,D)=
\begin{cases}
\dfrac{e^{mD}(mD-1)+1}{m^2},&m\ne0,\\[6pt]
D^2/2,&m=0.
\end{cases}
\tag{66.14}
\]

because

\[
\int_0^D u e^{mu}\,du=\mathfrak F_1(m,D).
\]

Then

\[
\boxed{
T_1(K;t,\lambda)
:=
\sum_{n=K+1}^{N}a_n\log n
\le
 e^{g_r}
\left[
 r\mathfrak F_0(m,D)+\mathfrak F_1(m,D)
\right].
}
\tag{66.15}
\]

---

## 7. Exact-head / convex-tail moment certificate

Define the exact finite head

\[
H_0^{(K)}=
\sum_{n=2}^{K}a_n,
\qquad
H_1^{(K)}=
\sum_{n=2}^{K}a_n\log n.
\]

Then

\[
\boxed{
A_0\le
H_0^{(K)}+e^{g_r}\mathfrak F_0(m,D),
}
\tag{66.16}
\]

and, under (66.12),

\[
\boxed{
A_1\le
H_1^{(K)}+
 e^{g_r}
\left[
 r\mathfrak F_0(m,D)+\mathfrak F_1(m,D)
\right].
}
\tag{66.17}
\]

Every quantity on the right is evaluable with directed rounding in `O(K)` operations, independent of the magnitude of `N`.

This is exactly the computational geometry needed for a proof in `(t,lambda)` rather than `(t,x)`.

---

## 8. Stability near m=0

The formulas (66.10), (66.14) have removable singularities at `m=0`. A rigorous implementation must not divide by an interval containing zero.

Use either:

1. the explicit `m=0` branches together with interval subdivision until `m` has fixed sign; or
2. the entire functions
   \[
   \operatorname{exprel}(z)=\frac{e^z-1}{z},
   \]
   and its first moment analogue, evaluated by a directed-rounding Taylor series around zero.

This is an implementation requirement, not a mathematical gap.

---

## 9. Why this is sharper than the Round-64 practical bound

Round 64 controls the whole cutoff by one exponent `q>1`, forcing large constants `Z_2(q),Z_3(q)` when `q` is near one.

Round 66 instead:

- evaluates the first `K` true weights exactly;
- exploits the exact quadratic heat exponent in the tail;
- uses the fact that the counting-measure exponent `g` is convex;
- captures both endpoints of the tail rather than replacing the whole interval by its weakest power.

The proof remains unconditional and does not use any oscillatory cancellation.

---

## 10. Exploratory diagnostic — NOT A PROOF

A non-rigorous high-precision evaluation of the Round-66 formulas with `K=128` indicates that, at `t=1/2`, the PSC core lower bound changes sign near `lambda≈7.1`, far below `10.52` but still well above `lambda_*`.

This numerical observation is **HEURISTIC/EXPLORATORY ONLY**. It is recorded solely to choose the next certified target. It must not be cited as a proved threshold.

The immediate certification target is therefore

\[
\boxed{C_{\rm target}=7.10}
\]

with the goal of determining rigorously whether the existing PSC plus the Round-66 moment envelope proves

\[
\lambda\ge7.10
\Longrightarrow
(H_t,H_t')\ne(0,0)
\]

for every `0<t<=1/2`.

If the 512/768-bit global audit fails, record the exact failure channel and raise the target rather than silently treating `7.10` as established.

---

## 11. Circularity audit

Inputs:

- exact heat weights from the unconditional Polymath approximation;
- elementary monotonicity;
- the decreasing integral test;
- convexity of a quadratic polynomial;
- finite directed-rounding head sums in the intended implementation.

Not used:

- RH;
- `Lambda<=0`;
- real-rootedness;
- zero spacings;
- pair correlation;
- Laguerre inequalities;
- numerical RH verification.

This theorem is independent of the desired no-collision conclusion.

---

## 12. Next step

Implement `convex_tail_psc_mpfr.c` with:

1. directed-rounding evaluation of the `K=128` head;
2. interval-safe evaluation of (66.10), (66.14);
3. the existing PSC phase bounds;
4. Polymath `E0,E1` and dynamic-cutoff bridge;
5. adaptive tiling in `(t,lambda)`;
6. 512-bit pass followed by an independent 768-bit rerun.

The first target is `lambda>=7.10`; only a complete cover can lower `C_proved` from `10.52`.
