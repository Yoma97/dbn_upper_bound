# Round 36 — The horizontal xi norm satisfies an exact positive subheat identity

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / POSITIVE SCALAR PDE BRIDGE / NON-CIRCULAR / NOVELTY UNVERIFIED.

## 0. Executive theorem

Define the positive horizontal Gaussian norm

\[
\mathcal N_t(\gamma)
:=\int_{\mathbb R}G_t(a)
\left|\xi\!\left(\frac12+a+i\gamma\right)\right|^2da,
\qquad
G_t(a)=\frac1{\sqrt{\pi t}}e^{-a^2/t}.
\]

Round 35 showed that a multiplicity-`m` heat collision at `x=2 gamma` forces

\[
 t\int G_t(a)|\xi'(1/2+a+i\gamma)|^2da
 \ge2m\mathcal N_t(\gamma).
\]

This round eliminates the logarithmic derivative entirely. One has the exact scalar PDE identity

\[
\boxed{
\left(\partial_t+\frac14\partial_\gamma^2\right)
\mathcal N_t(\gamma)
=
\int_{\mathbb R}G_t(a)
\left|\xi'\!\left(\frac12+a+i\gamma\right)\right|^2da
\ge0.
}
\]

Consequently a multiplicity-`m` collision necessarily satisfies

\[
\boxed{
 t\,
 \frac{\left(\partial_t+\frac14\partial_\gamma^2\right)\mathcal N_t(\gamma)}
 {\mathcal N_t(\gamma)}
 \ge2m.
}
\]

For a double collision the threshold is `4`.

Thus collision exclusion can be reduced to a differential estimate on a strictly positive scalar function `mathcal N_t`, with no pointwise `xi'/xi` singularities.

---

## 1. Heat-semigroup representation of the norm

For fixed `gamma`, set

\[
f_\gamma(a)
:=\left|\xi\!\left(\frac12+a+i\gamma\right)\right|^2.
\]

The kernel

\[
G_t(a)=\frac1{\sqrt{\pi t}}e^{-a^2/t}
\]

is the heat kernel for diffusivity `1/4`:

\[
\boxed{\partial_tG_t=\frac14\partial_a^2G_t.}
\]

Hence

\[
\mathcal N_t(\gamma)
=\left(e^{(t/4)\partial_a^2}f_\gamma\right)(0).
\]

The Gaussian dominates the order-one growth of xi, so all differentiations and integrations by parts below are justified for fixed positive `t`.

---

## 2. Time derivative

Differentiate under the integral:

\[
\partial_t\mathcal N_t
=\int (\partial_tG_t)f_\gamma\,da
=\frac14\int G_t\partial_a^2f_\gamma\,da.
\]

Thus

\[
\boxed{
\partial_t\mathcal N_t
=\frac14\int_{\mathbb R}G_t(a)
\partial_a^2|\xi(1/2+a+i\gamma)|^2da.
}
\]

---

## 3. Subharmonic identity for an analytic function

Let

\[
F(a,\gamma)
:=\xi\!\left(\frac12+a+i\gamma\right).
\]

Because `F` is holomorphic in `a+i gamma`, the standard identity is

\[
\boxed{
(\partial_a^2+\partial_\gamma^2)|F|^2
=4|F'|^2.
}
\]

For completeness, write `F=U+iV`. The Cauchy--Riemann equations imply

\[
\Delta(U^2+V^2)
=2(|\nabla U|^2+|\nabla V|^2)
=4|F'|^2.
\]

Therefore

\[
\partial_a^2|F|^2
=4|F'|^2-\partial_\gamma^2|F|^2.
\]

---

## 4. Exact subheat identity

Insert Section 3 into the time derivative:

\[
\partial_t\mathcal N_t
=
\int G_t|F'|^2da
-\frac14\int G_t\partial_\gamma^2|F|^2da.
\]

Since the Gaussian does not depend on `gamma`,

\[
\int G_t\partial_\gamma^2|F|^2da
=\partial_\gamma^2\mathcal N_t.
\]

Hence

\[
\boxed{
\left(\partial_t+\frac14\partial_\gamma^2\right)
\mathcal N_t(\gamma)
=\int G_t(a)|\xi'(1/2+a+i\gamma)|^2da.
}
\]

The right-hand side is nonnegative, so

\[
\boxed{
\left(\partial_t+\frac14\partial_\gamma^2\right)\mathcal N_t\ge0.
}
\]

This unconditional scalar positivity holds regardless of RH.

---

## 5. Strict positivity of the norm

For every `t>0` and real `gamma`,

\[
\mathcal N_t(\gamma)>0.
\]

Indeed, the integrand is nonnegative. If the integral vanished, the entire function

\[
a\mapsto\xi(1/2+a+i\gamma)
\]

would vanish for almost every real `a`, hence identically by analyticity, impossible.

Thus division by `mathcal N_t` is always legitimate.

---

## 6. Collision criterion as a scalar differential inequality

Round 35 gives, at a multiplicity-at-least-`m` collision,

\[
t\int G_t|\xi'|^2\ge2m\mathcal N_t.
\]

Using the exact PDE identity,

\[
\boxed{
 t\left(\partial_t+\frac14\partial_\gamma^2\right)\mathcal N_t
 \ge2m\mathcal N_t.
}
\]

Equivalently,

\[
\boxed{
 t\frac{(\partial_t+\frac14\partial_\gamma^2)\mathcal N_t}
 {\mathcal N_t}\ge2m.
}
\]

Thus any unconditional estimate

\[
 t(\partial_t+\tfrac14\partial_\gamma^2)\mathcal N_t
 <4\mathcal N_t
\]

rules out a double collision at that point.

---

## 7. Logarithmic form

Because `mathcal N_t>0`, write

\[
u(t,\gamma):=\log\mathcal N_t(\gamma).
\]

Then

\[
\frac{\partial_\gamma^2\mathcal N_t}{\mathcal N_t}
=u_{\gamma\gamma}+u_\gamma^2.
\]

Hence the Rayleigh observable of Round 35 is

\[
\boxed{
\mathcal R_{1,t}(\gamma)
=t\left(
 u_t+\frac14u_{\gamma\gamma}+\frac14u_\gamma^2
\right).
}
\]

A multiplicity-`m` collision requires

\[
\boxed{
 u_t+\frac14u_{\gamma\gamma}+\frac14u_\gamma^2
 \ge\frac{2m}{t}.
}
\]

This formulation may be convenient if one can prove horizontal log-convexity or mean-value bounds for `mathcal N_t`. No such sign is assumed here.

---

## 8. Initial value at t=0

In the approximate-identity sense,

\[
\boxed{
\lim_{t\downarrow0}\mathcal N_t(\gamma)
=|\xi(1/2+i\gamma)|^2.
}
\]

At ordinates where the critical-line xi function is nonzero, the scalar norm therefore starts from a positive explicit boundary value. At a critical-line zero the initial value is zero, but for every `t>0` Gaussian horizontal smoothing makes `mathcal N_t` strictly positive.

This distinction may be useful in localizing which ordinates can generate a large collision Rayleigh quotient.

---

## 9. Relation to Round 34 derivative series

Round 34 gives

\[
\mathcal N_t(\gamma)
=64\sum_{k\ge0}\frac{(2t)^k}{k!}|H_t^{(k)}(2\gamma)|^2.
\]

Thus the scalar subheat identity is simultaneously an evolution law for this positive derivative-energy generating function.

This supplies an independent consistency check: differentiating the series and using the backward heat equation must reproduce the positive `xi'` norm on the right.

---

## 10. Why this improves the analytic target

The pointwise logarithmic derivative

\[
\xi'/\xi
\]

has poles at zeros, making any uniform horizontal estimate delicate and potentially circular.

The scalar observable

\[
\mathcal N_t
\]

has no such singularities. It is positive and smooth for every `t>0` and real `gamma`.

Therefore the preferred analytic-number-theory task is now:

> Obtain upper bounds for the scalar differential ratio
> \[
> t(\partial_t+\tfrac14\partial_\gamma^2)\mathcal N_t/\mathcal N_t
> \]
> directly from an explicit/mean-square representation of `mathcal N_t`, rather than through pointwise estimates for `xi'/xi`.

---

## 11. Circularity audit

Used:

- analyticity of xi;
- Gaussian heat kernel calculus;
- Cauchy--Riemann/subharmonic identity;
- Round-35 spectral-gap condition.

Not used:

- RH or `Lambda<=0`;
- real-zero assumptions;
- Laguerre positivity;
- zero-free regions around the Gaussian horizontal window.

---

## 12. Status

- heat-semigroup representation of `mathcal N_t`: **PROVED**;
- exact scalar subheat identity: **PROVED**;
- unconditional positivity `(partial_t+1/4 partial_gamma^2)N>=0`: **PROVED**;
- collision scalar differential threshold: **PROVED**;
- useful unconditional upper bound below threshold `4`: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
