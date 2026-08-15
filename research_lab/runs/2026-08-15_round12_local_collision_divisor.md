# Round 12 — Local collision divisor instead of a global regularized discriminant

Date: 2026-08-15

Status labels used here: **PROVED**, **CANDIDATE**, **REFUTED**, **NOVELTY UNVERIFIED**.

## Executive verdict

The global scalar `Disc_reg(H_t)` is not needed for the first five collision-geometry gates. A cleaner object exists locally on every finite simple zero cluster:

\[
\mathcal D_I(t):=(-1)^{m(m-1)/2}\prod_{k=1}^m F_z(t,x_k(t)),
\]

where `I={x_1<...<x_m}` is a finite ordered cluster of simple real zeros of a real-entire heat family

\[
\partial_tF=-F_{zz}.
\]

This is an oriented local collision section. It is a scalar only in a chosen finite zero chart; changing the chart multiplies it by a nonvanishing transition factor as long as the added zeros remain simple. Thus the canonical object is better viewed as a **collision divisor / local line-bundle section**, not as one globally regularized infinite product.

The exact heat evolution law is

\[
\boxed{
\frac d{dt}\log|\mathcal D_I(t)|
=\sum_{k\in I}\left(A_k(t)^2+3B_k(t)\right)
}
\]

with

\[
A_k:=\frac{F_{zz}(t,x_k)}{2F_z(t,x_k)},
\qquad
B_k:=A_k^2-\frac{F_{zzz}(t,x_k)}{3F_z(t,x_k)}.
\]

For an order-one entire function with simple zeros `rho`, the second quantity is canonically

\[
\boxed{
B_k=\sum_{\rho\neq x_k}\frac1{(x_k-\rho)^2},
}
\]

and this root-wise inverse-square trace is absolutely convergent. The divergence problem enters only after summing over infinitely many `k`.

This yields a rigorous local unification of discriminant, phase current, inverse-square gap trace, and generic topological collision index. It does **not** prove RH and does **not** provide a backward no-collision estimate.

---

## 1. Hypotheses

Let `F(t,z)` be real analytic in `t`, entire in `z`, real on the real axis, and satisfy

\[
\partial_tF(t,z)=-\partial_z^2F(t,z).
\]

Let `J` be a time interval on which `m` real zero branches

\[
x_1(t)<\cdots<x_m(t)
\]

are simple and can be isolated in a common zero chart from all other zeros.

Define

\[
M:=\frac{m(m-1)}2,
\qquad
\mathcal D_I(t):=(-1)^M\prod_{k=1}^mF_z(t,x_k(t)).
\]

The square `\mathcal D_I^2` is independent of orientation/ordering. On the real ordered chart the sign convention above matches the classical positive squared Vandermonde in the polynomial case.

---

## 2. Root velocity and local gap variables — PROVED

Differentiating `F(t,x_k(t))=0` gives

\[
0=F_t+\dot x_kF_z=-F_{zz}+\dot x_kF_z,
\]

hence

\[
\boxed{\dot x_k=\frac{F_{zz}}{F_z}(t,x_k)=2A_k.}
\]

Define

\[
A_k:=\frac{F_{zz}}{2F_z}(t,x_k),
\qquad
B_k:=A_k^2-\frac{F_{zzz}}{3F_z}(t,x_k).
\]

These definitions are intrinsic and require no infinite product or zero enumeration.

If `F` has genus at most one (in particular, order one) then the logarithmic derivative of its Hadamard product shows that the derivative of the regular part at `x_k` is

\[
-B_k=-\sum_{\rho\neq x_k}(x_k-\rho)^{-2}.
\]

Equivalently,

\[
\boxed{B_k=\sum_{\rho\neq x_k}\frac1{(x_k-\rho)^2}.}
\]

The sum is absolutely convergent because the tail is `O(|rho|^{-2})` and an order-one zero divisor has convergent square reciprocal sum.

For an even order-one real-entire function with real zeros `\pm x_j`, one may also pair the first-order sum:

\[
A_k=\frac1{2x_k}+\sum_{j\neq k,\ j>0}\frac{2x_k}{x_k^2-x_j^2},
\]

which is absolutely convergent after the `\pm x_j` pairing.

**Consequence:** no finite-part prescription is needed for the inverse-square trace at a fixed zero. Only the global sum `\sum_k B_k` needs renormalization.

---

## 3. Exact local evolution law — PROVED

Along a simple zero branch,

\[
\frac d{dt}F_z(t,x_k(t))
=F_{zt}+\dot x_kF_{zz}
=-F_{zzz}+\frac{F_{zz}^2}{F_z}.
\]

Therefore

\[
\frac d{dt}\log|F_z(t,x_k)|
=-\frac{F_{zzz}}{F_z}+\left(\frac{F_{zz}}{F_z}\right)^2.
\]

Using

\[
\frac{F_{zz}}{F_z}=2A_k,
\qquad
\frac{F_{zzz}}{F_z}=3(A_k^2-B_k),
\]

we obtain

\[
\boxed{
\frac d{dt}\log|F_z(t,x_k)|=A_k^2+3B_k.
}
\]

Summing over a finite zero cluster gives

\[
\boxed{
\frac d{dt}\log|\mathcal D_I(t)|
=\sum_{k\in I}(A_k^2+3B_k).
}
\]

If all zeros of `F` are real, then `B_k>0` and `A_k^2\ge0`, so every local factor `|F_z(t,x_k)|` and hence `|\mathcal D_I|` is strictly increasing forward in heat time as long as the zeros stay simple.

This is a forward statement only; it does not prevent `\mathcal D_I` from reaching zero when time is run backward.

---

## 4. Collision locality — PROVED

In a zero chart containing exactly the cluster `I`, factor

\[
F(t,z)=A(t,z)\prod_{k=1}^m(z-x_k(t)),
\]

where `A` is analytic and nonvanishing in the chart.

Then

\[
F_z(t,x_k)=A(t,x_k)\prod_{\ell\neq k}(x_k-x_\ell).
\]

Multiplying over `k` gives

\[
\prod_{k=1}^mF_z(t,x_k)
=(-1)^M
\left(\prod_{i<j}(x_i-x_j)^2\right)
\left(\prod_{k=1}^mA(t,x_k)\right).
\]

Hence

\[
\boxed{
\mathcal D_I(t)=\Delta_I(t)\,A_{\rm tail}(t),
}
\]

where

\[
\Delta_I(t):=\prod_{i<j}(x_i-x_j)^2,
\qquad
A_{\rm tail}(t):=\prod_{k=1}^mA(t,x_k(t))\neq0.
\]

Thus a finite core collision cannot be cancelled by the tail. This is exactly the collision-locality gate, obtained without a global regularized product.

---

## 5. Cutoff / chart independence as a divisor cocycle — PROVED locally

Let `I\subset J` be two finite simple zero charts and suppose the added zeros `J\setminus I` remain simple and collision-free on the time neighborhood under consideration. Then

\[
\frac{\mathcal D_J}{\mathcal D_I}
=(-1)^{M_J-M_I}\prod_{k\in J\setminus I}F_z(t,x_k(t)),
\]

which is analytic and nonvanishing there.

Therefore `\mathcal D_I` and `\mathcal D_J` define the same local collision divisor for collisions occurring in the common core. Different cutoffs change the section only by a nonvanishing transition factor.

This is the correct form of cutoff independence for collision detection. A globally normalized scalar is not required.

**Interpretation:** the canonical object is an equivalence class of local sections under multiplication by nonvanishing analytic factors.

---

## 6. Phase-current shadow — PROVED

Set

\[
G=F+iF_z,
\qquad
J=\Im(\overline G\,G_z)=FF_{zz}-F_z^2.
\]

At every real simple zero `x_k`,

\[
-J(t,x_k)=F_z(t,x_k)^2.
\]

Hence for every finite cluster,

\[
\boxed{
\mathcal D_I(t)^2=\prod_{k\in I}[-J(t,x_k(t))].
}
\]

So the phase-current factors are exactly the squared local discriminant-section factors. No new current has been invented here; rather, the old current acquires an exact role as the local norm-square of the collision divisor section.

---

## 7. Finite polynomial recovery — PROVED

For a monic polynomial

\[
P_t(z)=\prod_{k=1}^N(z-x_k(t)),
\]

and `I` equal to all roots, the nonvanishing factor `A` is identically one. Therefore

\[
\mathcal D_I=\Delta_t:=\prod_{i<j}(x_i-x_j)^2.
\]

Also

\[
A_k=\sum_{j\neq k}\frac1{x_k-x_j},
\qquad
B_k=\sum_{j\neq k}\frac1{(x_k-x_j)^2}.
\]

The finite identity

\[
\sum_kA_k^2=\sum_kB_k
\]

follows by expanding the squares: all three-distinct-index cross terms cancel by

\[
\frac1{(x_i-x_j)(x_i-x_\ell)}
+\frac1{(x_j-x_i)(x_j-x_\ell)}
+\frac1{(x_\ell-x_i)(x_\ell-x_j)}=0.
\]

Thus the local evolution law becomes

\[
\frac d{dt}\log\Delta_t
=4\sum_kB_k
=4\sum_{i\neq j}\frac1{(x_i-x_j)^2},
\]

which exactly recovers the finite prototype.

---

## 8. Generic double collision and topological charge — PROVED

Suppose `(t_c,x_c)` is a generic double collision:

\[
F=F_z=0,\qquad c:=F_{zz}(t_c,x_c)\neq0.
\]

The heat equation gives `F_t=-c`. With `tau=t-t_c` and `y=x-x_c`,

\[
F(t,x)=\frac c2(y^2-2\tau)+O(|y|^3+|\tau y|+\tau^2).
\]

Hence on the real side `tau>0`,

\[
x_\pm(t)=x_c\pm\sqrt{2\tau}+O(\tau),
\]

and

\[
(x_+-x_-)^2=8\tau+O(\tau^{3/2}).
\]

For the two-zero oriented local section,

\[
\boxed{
\mathcal D_{\{-,+\}}(t)=2c^2(t-t_c)+O((t-t_c)^{3/2}).
}
\]

Meanwhile for the collision map

\[
\Gamma(t,x)=(F,F_z)
\]

we have

\[
\det D_{(t,x)}\Gamma(t_c,x_c)
=F_tF_{zz}-F_zF_{zt}
=-c^2<0.
\]

Therefore

\[
\boxed{
\mathcal D_{\{-,+\}}'(t_c)
=-2\det D\Gamma(t_c,x_c)=2c^2>0.
}
\]

This is an exact bridge between the local discriminant section and the oriented topological collision index.

---

## 9. Universal logarithmic blow-up at a generic collision — PROVED

For the colliding pair,

\[
B_-+B_+=\frac1{4(t-t_c)}+O((t-t_c)^{-1/2}),
\]

and

\[
A_-^2+A_+^2=\frac1{4(t-t_c)}+O((t-t_c)^{-1/2}).
\]

Hence

\[
\boxed{
\frac d{dt}\log|\mathcal D_{\{-,+\}}(t)|
=\frac1{t-t_c}+O((t-t_c)^{-1/2}).
}
\]

Equivalently, a generic finite collision is characterized by a universal logarithmic divergence of the integrated local gap energy. This is the local finite-cluster analogue of the global energy picture, but it requires no renormalization.

---

## 10. Application to the Riemann de Bruijn–Newman family

The Polymath setup gives `H_t` as an even entire function of order one satisfying

\[
\partial_tH_t=-H_t''.
\]

Therefore every statement above applies to every finite simple real zero cluster of `H_t` on any time interval where the cluster remains simple.

For `H_t`, the root-wise quantity

\[
B_k(t)=\sum_{\rho\neq x_k(t)}(x_k(t)-\rho(t))^{-2}
\]

is canonical and absolutely convergent. This sharply separates two issues:

- **local collision geometry:** no regularization needed;
- **global energy obtained by summing over all roots:** divergent and must be mollified/renormalized, as in Rodgers–Tao.

This separation should replace the previous attempt to regularize the collision object globally at the start.

---

## 11. Gate table

| Gate | Status | Reason |
|---|---|---|
| C1 well-definedness | **PROVED locally** | finite product of derivatives on a simple zero chart |
| C2 collision locality | **PROVED** | `D_I = Delta_I A_tail`, `A_tail != 0` |
| C3 cutoff independence | **PROVED as divisor/gauge equivalence** | nested charts differ by nonvanishing factor |
| C4 finite recovery | **PROVED** | monic full polynomial chart gives classical discriminant |
| C5 evolution identity | **PROVED** | exact `sum(A_k^2+3B_k)` law |
| C6 Riemann-specific no-go | **OPEN** | no backward lower bound / source exclusion yet |

---

## 12. What this refutes

### REFUTED as a necessary starting point
The claim that one first needs a canonical global regularized pairwise discriminant before any exact unification is possible.

A local collision-divisor section already gives exact C1–C5 information and glues across cutoffs by nonvanishing transition factors.

### NOT refuted
A useful global regularized scalar may still exist and may still encode additional Riemann-specific information. It is simply no longer structurally necessary for local collision detection or local evolution.

---

## 13. Smallest next lemma

The next target should be **one** lemma only:

> For the Riemann heat family in a real-zero interval, obtain an arithmetic/kernel-side upper bound on the backward integral
> \[
> \int_{t_0}^{t_1}\left(A_k(t)^2+3B_k(t)\right)dt
> \]
> (or on a finite cluster sum) that is uniform enough to prevent `log|D_I|` from tending to `-infinity` at a finite backward time.

A bound merely equivalent to assuming all zeros remain real is rejected. The input must come from the Riemann kernel, explicit formula, or an independently controlled zero-density/spacing estimate.

This is now the narrow C6 bottleneck.

---

## 14. Novelty audit

**NOVELTY UNVERIFIED.** Classical singularity theory already has local discriminant varieties, and the polynomial identity expressing the discriminant through the product of derivatives at the roots is classical. No novelty claim is made for those components.

The potentially distinctive contribution is the exact package:

1. local oriented collision section for an entire backward-heat family;
2. exact heat evolution `d log|D_I|/dt = sum(A_k^2+3B_k)`;
3. identification of `B_k` as an absolutely convergent root-wise inverse-square trace for order-one entire functions;
4. phase-current norm identity `D_I^2=prod(-J(x_k))`;
5. generic-collision relation `D_I'(t_c)=-2 det D Gamma`;
6. interpretation of cutoff changes as nonvanishing divisor transition functions.

This package must be literature-checked before being called new.

## RH status

**RH remains open.** This round establishes a cleaner collision geometry and isolates the remaining hard step, but it supplies no Riemann-specific backward no-collision estimate.