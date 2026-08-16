# Round 40 — Coherent-state displacement and the shifted collision Rayleigh criterion

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / CORRECTION / NEW COLLISION NECESSARY CONDITION / NOVELTY UNVERIFIED.

## 0. Executive correction

Rounds 34--36 produced the unconditional collision necessary condition

\[
\mathcal R_{0,t}(\gamma)
:=t\frac{\int G_t(a)|\xi'(1/2+a+i\gamma)|^2\,da}
{\int G_t(a)|\xi(1/2+a+i\gamma)|^2\,da}
\ge2m
\]

for a multiplicity-`m` heat collision at `x=2 gamma`.

Round 38 then showed that the large real Archimedean logarithmic slope is of size

\[
u_0\sim\frac12\log\frac\gamma{2\pi}.
\]

Consequently the **unshifted** Rayleigh quotient has a natural background of order `t u_0^2`; at sufficiently large height this is already much larger than the double-collision threshold `4`. Thus the unshifted criterion is not expected to discriminate collisions in the high-height regime.

This round removes that background exactly.

For every real displacement parameter `c`, a multiplicity-`m` collision implies

\[
\boxed{
\mathcal R_{c,t}(\gamma)
:=t\frac{\int_{\mathbb R}G_t(a)e^{-ca}
|\xi'(s(a))-c\xi(s(a))|^2\,da}
{\int_{\mathbb R}G_t(a)e^{-ca}|\xi(s(a))|^2\,da}
\ge2m,
}
\]

where `s(a)=1/2+a+i gamma`.

The statement holds **for every real c**. Hence one may optimize over `c` and obtain the stronger necessary condition

\[
\boxed{
\inf_{c\in\mathbb R}\mathcal R_{c,t}(\gamma)\ge2m.
}
\]

Choosing `c` near the real Archimedean slope removes the large exponential tilt before measuring horizontal oscillation. This is the correct renormalized version of the Round-35 bridge.

---

## 1. Starting collision moments

Round 32 established that, up to a fixed nonzero normalization depending on `k,t`,

\[
H_t^{(k)}(2\gamma)
\longleftrightarrow
M_k:=\int_{\mathbb R}G_t(a)
H_k(a/\sqrt t)\,
\xi(1/2+a+i\gamma)\,da,
\]

where `H_k` denotes the physicists' Hermite polynomial.

Thus a zero of multiplicity at least `m` at `x=2 gamma` is equivalent to

\[
M_0=M_1=\cdots=M_{m-1}=0.
\]

No real-rootedness assumption is involved.

---

## 2. Exact exponential gauge and Gaussian translation

Fix any real number `c`. Write

\[
a=b+\frac{ct}{2}
\]

and define

\[
F_c(b)
:=e^{-c(b+ct/2)}
\xi\!\left(\frac12+b+\frac{ct}{2}+i\gamma\right).
\]

Then

\[
\xi(1/2+a+i\gamma)=e^{ca}F_c(a-ct/2).
\]

The Gaussian identity

\[
\boxed{
G_t(a)e^{ca}
=e^{c^2t/4}G_t(a-ct/2)
}
\]

is exact.

Therefore

\[
M_k
=e^{c^2t/4}
\int_{\mathbb R}G_t(b)
H_k\!\left(\frac b{\sqrt t}+\frac{c\sqrt t}{2}\right)
F_c(b)\,db.
\]

---

## 3. Hermite translation is triangular

For physicists' Hermite polynomials,

\[
\boxed{
H_k(x+y)
=\sum_{j=0}^k\binom{k}{j}(2y)^{k-j}H_j(x).
}
\]

Taking

\[
y=\frac{c\sqrt t}{2}
\]

gives

\[
H_k\!\left(\frac b{\sqrt t}+\frac{c\sqrt t}{2}\right)
=\sum_{j=0}^k\binom{k}{j}(c\sqrt t)^{k-j}
H_j(b/\sqrt t).
\]

Define shifted Hermite moments

\[
N_j^{(c)}
:=\int_{\mathbb R}G_t(b)H_j(b/\sqrt t)F_c(b)\,db.
\]

Then

\[
M_k=e^{c^2t/4}
\sum_{j=0}^k\binom{k}{j}(c\sqrt t)^{k-j}N_j^{(c)}.
\]

The transformation from `(N_0,...,N_{m-1})` to `(M_0,...,M_{m-1})` is triangular with diagonal `1`. Hence

\[
\boxed{
M_0=\cdots=M_{m-1}=0
\iff
N_0^{(c)}=\cdots=N_{m-1}^{(c)}=0
}
\]

for **every real c**.

This is the central exact invariance.

---

## 4. Shifted Hermite spectral gap

Apply the same Gaussian Hermite Parseval/spectral-gap argument used in Rounds 34--35, now to `F_c`.

If

\[
N_0^{(c)}=\cdots=N_{m-1}^{(c)}=0,
\]

then

\[
\boxed{
t\int_{\mathbb R}G_t(b)|F_c'(b)|^2\,db
\ge
2m\int_{\mathbb R}G_t(b)|F_c(b)|^2\,db.
}
\]

This is exact and does not depend on the choice of `c`.

---

## 5. Return to the original horizontal variable

With

\[
a=b+ct/2,
\]

one has

\[
F_c'(b)
=e^{-ca}\left[\xi'(s(a))-c\xi(s(a))\right].
\]

Also

\[
G_t(b)e^{-2ca}
=G_t(a-ct/2)e^{-2ca}
=e^{-c^2t/4}G_t(a)e^{-ca}.
\]

The constant factor `exp(-c^2 t/4)` cancels from the quotient. Hence a multiplicity-`m` collision implies

\[
\boxed{
\mathcal R_{c,t}(\gamma)
=t\frac{\int G_t(a)e^{-ca}
|\xi'(s(a))-c\xi(s(a))|^2\,da}
{\int G_t(a)e^{-ca}|\xi(s(a))|^2\,da}
\ge2m
}
\]

for every real `c`.

Taking the infimum yields

\[
\boxed{
\mathcal R_{*,t}(\gamma)
:=\inf_{c\in\mathbb R}\mathcal R_{c,t}(\gamma)
\ge2m.
}
\]

For a generic double collision,

\[
\boxed{
\mathcal R_{*,t}(\gamma)\ge4.
}
\]

Thus any rigorous estimate

\[
\mathcal R_{c,t}(\gamma)<4
\]

for even one chosen real `c` excludes a double collision at `(t,2 gamma)`.

---

## 6. Why this fixes the high-height baseline problem

Suppose heuristically on the relevant horizontal window that

\[
\xi(1/2+a+i\gamma)\approx e^{u_0a}Z(a)
\]

with slowly varying `Z` and

\[
u_0\approx\frac12\log\frac\gamma{2\pi}.
\]

The unshifted derivative is

\[
\xi'\approx e^{u_0a}(u_0Z+Z'),
\]

so the old quotient contains a background `t u_0^2`.

Choosing

\[
\boxed{c=u_0}
\]

gives

\[
\xi'-c\xi\approx e^{u_0a}Z',
\]

and removes the dominant real exponential slope exactly in the pure exponential model.

For the actual Riemann function the canonical unconditional choice is

\[
\boxed{
c_0(\gamma):=\Re\alpha(1/2+i\gamma),
}
\]

with Polymath's explicit

\[
\alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}.
\]

Then

\[
c_0(\gamma)
=\frac12\log\frac\gamma{2\pi}+O(\gamma^{-2})
\]

as `gamma -> infinity`.

---

## 7. Exact zeta-side form of the shifted derivative

Using

\[
\xi(s)=P(s)\zeta(s),
\qquad
P(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),
\]

we have

\[
\xi'(s)-c\xi(s)
=P(s)\left[\zeta'(s)+(A(s)-c)\zeta(s)\right],
\]

where

\[
\boxed{
A(s):=\frac{P'(s)}{P(s)}
=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2).
}
\]

Therefore

\[
\boxed{
\mathcal R_{c,t}(\gamma)
=t\frac{\int G_t(a)e^{-ca}|P(s)|^2
|\zeta'(s)+(A(s)-c)\zeta(s)|^2\,da}
{\int G_t(a)e^{-ca}|P(s)|^2|\zeta(s)|^2\,da}.
}
\]

For `c=c_0(gamma)`, the large real part of `A` is cancelled at `a=0`; the remaining archimedean connection has imaginary leading term approximately `i pi/4` plus horizontal variation and a Stirling error of order `gamma^{-2}`.

This is a substantially better arithmetic target than the unshifted quotient.

---

## 8. Circularity audit

The shifted criterion uses only:

- the unconditional Gaussian-Hermite representation of the positive-time heat flow;
- an exact Gaussian exponential-completion identity;
- the Hermite translation formula;
- the Gaussian spectral gap;
- exact factorization of `xi`.

It does **not** use:

- RH;
- `Lambda<=0`;
- real-rootedness at the unknown slice;
- a lower zero-gap bound;
- Laguerre positivity;
- a zero-free neighborhood of the critical line;
- Rodgers--Tao negative-time local-equilibrium estimates.

The statement is therefore a legitimate necessary condition for collision, not an RH-equivalent assumption inserted as input.

---

## 9. New Round-41 target

The correct next target is no longer the old high-saddle estimate for the unshifted quotient. It is:

> Estimate `R_{c,t}(gamma)` with `c=c_0(gamma)=Re alpha(1/2+i gamma)`, or optimize over `c`, and seek an unconditional region where it is strictly below `4`.

The first attack should derive the exact minimizing equation in `c` and determine whether the optimum can be expressed through weighted horizontal moments of `xi` without any pointwise logarithmic derivative. Then compare the resulting centered derivative energy to Polymath's saddle/Dirichlet-polynomial approximation.

---

## 10. Status

- unshifted Rayleigh quotient as high-height discriminator: **DEMOTED / large Archimedean background**;
- shifted collision moment equivalence for every real `c`: **PROVED**;
- shifted spectral-gap collision criterion: **PROVED**;
- optimized criterion `inf_c R_{c,t} >= 2m` at collision: **PROVED**;
- canonical choice `c=Re alpha(1/2+i gamma)`: **UNCONDITIONAL / NATURAL, not claimed optimal**;
- arithmetic estimate `R_{c,t}<4` in a new region: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
