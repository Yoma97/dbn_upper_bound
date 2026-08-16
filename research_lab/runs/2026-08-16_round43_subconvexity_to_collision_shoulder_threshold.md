# Round 43 — Subconvexity controls the collision shoulder: the `lambda > 32 theta` gate

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED ASYMPTOTIC BRIDGE / SOURCE-GROUNDED / CROSS-FRONTIER / NOVELTY UNVERIFIED.

## 0. Executive theorem

Round 42 reduced every real multiple heat collision to the two-saddle inequality

\[
\mathcal Q_{c,t}(\gamma)
\ge \frac{2}{1+2/(c^2t)}.
\]

This round connects the opposite upper bound directly to a classical subconvexity exponent for `zeta`.

Assume that for some `theta >= 1/8` one has the unconditional critical-line estimate

\[
\boxed{
|\zeta(1/2+iT)|\ll_\varepsilon T^{\theta+\varepsilon}
}
\]

for every `epsilon>0`. Put

\[
L:=\log\frac\gamma{2\pi},
\qquad
\lambda:=tL,
\qquad
c:=\Re\alpha(1/2+i\gamma),
\]

with Polymath's

\[
\alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}.
\]

Let `t -> 0+`, `gamma -> infinity`, with `lambda` confined to a compact subset of

\[
\boxed{(32\theta,\infty).}
\]

Then

\[
\boxed{
\mathcal Q_{c,t}(\gamma)\longrightarrow0,
}
\]

while

\[
\frac{2}{1+2/(c^2t)}\longrightarrow2.
\]

Consequently, for sufficiently small `t`, **no real multiple zero of `H_t` can occur in this scaling region**.

For Bourgain's currently best known exponent

\[
\theta=\frac{13}{84},
\]

the gate becomes

\[
\boxed{
\lambda>32\cdot\frac{13}{84}
=\frac{104}{21}
\approx4.95238095.
}
\]

This is slightly weaker than the previous program threshold `lambda_* approx 4.914588956`, but it is obtained by a completely different bridge. More importantly, it gives a direct conversion law:

\[
\boxed{
\text{improve critical-line subconvexity }\theta
\quad\Longrightarrow\quad
\text{improve the collision shoulder threshold }32\theta.
}
\]

---

## 1. Positive-half reduction

By the functional equation and the sign-adapted derivative in Round 42, the numerator and denominator of `Q_{c,t}` are even after reflection. Hence it suffices to work on `a>=0`:

\[
\mathcal Q_{c,t}(\gamma)
=t\frac{
\int_0^\infty G_t(a)e^{-ca}
|P(s)|^2
|\zeta'(s)+(A(s)-c)\zeta(s)|^2\,da
}{
\int_0^\infty G_t(a)e^{-ca}|P(s)|^2|\zeta(s)|^2\,da
},
\]

where

\[
s=\frac12+a+i\gamma,
\]

\[
P(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),
\]

and

\[
A(s)=\frac{P'(s)}{P(s)}.
\]

No logarithmic derivative of `zeta` is required.

---

## 2. Archimedean exponential scale

For `a` in a fixed bounded positive interval and `gamma -> infinity`, Stirling gives

\[
2\Re A(1/2+a+i\gamma)
=L+o(1)
\]

uniformly, while

\[
c=\frac L2+o(1).
\]

Therefore, after factoring out the common value at `a=0`, the non-zeta part of the positive-half measure has exponential scale

\[
G_t(a)e^{-ca}|P(s)|^2
=\exp\!\left(
\frac{S_0(a;\lambda)+o(1)}t
\right)
\times\text{common factor},
\]

where

\[
\boxed{
S_0(a;\lambda):=-a^2+\frac\lambda2 a.
}
\]

This parabola has its unique maximum at

\[
\boxed{
a_*:=\frac\lambda4}
\]

with

\[
\boxed{
S_0(a_*;\lambda)=\frac{\lambda^2}{16}.
}
\]

The point `a_*` is the positive saddle of the two-saddle gauge.

---

## 3. The safe core lies in the absolutely convergent half-plane when `lambda>2`

At the saddle,

\[
\Re s_*
=\frac12+\frac\lambda4.
\]

Thus

\[
\lambda>2
\quad\Longrightarrow\quad
\Re s_*>1.
\]

On any compact lambda interval with lower endpoint `lambda_0>2`, there is a fixed `delta>0` such that a small fixed neighborhood of `a_*` lies in

\[
\Re s\ge1+\delta.
\]

In this neighborhood the absolutely convergent Dirichlet series give uniform bounds

\[
|\zeta(s)|\le\zeta(1+\delta),
\]

\[
|\zeta(s)|\ge\frac1{\zeta(1+\delta)},
\]

and

\[
|\zeta'(s)|\le -\zeta'(1+\delta).
\]

Moreover

\[
A(s)-c=i\frac\pi4+O(1)
\]

uniformly, and in fact the real difference is much smaller. Hence on the saddle neighborhood

\[
|\zeta'(s)+(A-c)\zeta(s)|\ll_{\delta,\lambda_0,\lambda_1}1.
\]

A Laplace lower bound therefore gives

\[
\boxed{
D_{\rm core}
\ge
\exp\!\left(
\frac{\lambda^2/16-o(1)}t
\right)
\times\text{common factor},
}
\]

whereas the core numerator is only a bounded multiple of this mass. After multiplication by the prefactor `t`, the core contribution to `Q_{c,t}` tends to zero.

---

## 4. Phragmen--Lindelof propagation of the subconvex exponent

Assume

\[
|\zeta(1/2+iT)|\ll_\varepsilon T^{\theta+\varepsilon}.
\]

Using the standard polynomial/logarithmic bound on the line `Re s=1` and the Phragmen--Lindelof principle in the strip, for

\[
0\le a\le\frac12
\]

we obtain

\[
\boxed{
|\zeta(1/2+a+iT)|
\ll_\varepsilon
T^{\theta(1-2a)+\varepsilon}.
}
\]

By Cauchy's derivative estimate on a small circle, with the `epsilon` loss enlarged if necessary,

\[
\boxed{
|\zeta'(1/2+a+iT)|
\ll_\varepsilon
T^{\theta(1-2a)+\varepsilon}
\log T.
}
\]

The logarithmic factor is subexponential on the `1/t` scale and will not affect the rate function.

---

## 5. The shoulder rate function

On the critical-strip shoulder

\[
0\le a\le\frac12,
\]

the square of the zeta/subconvex bound contributes the exponential rate

\[
2\theta\lambda(1-2a).
\]

Combining with the Archimedean/Gaussian rate `S_0`, the numerator shoulder has rate at most

\[
\boxed{
S_\theta(a;\lambda)
:=-a^2+\frac\lambda2 a
+2\theta\lambda(1-2a).
}
\]

Equivalently,

\[
S_\theta(a;\lambda)
=-a^2+\lambda\left(\frac12-4\theta\right)a
+2\theta\lambda.
\]

If

\[
\theta\ge\frac18,
\]

then

\[
\frac12-4\theta\le0
\]

and hence `S_theta` is strictly decreasing on `[0,1/2]`. Therefore

\[
\boxed{
\max_{0\le a\le1/2}S_\theta(a;\lambda)
=S_\theta(0;\lambda)
=2\theta\lambda.
}
\]

Thus the hardest shoulder point is exactly the critical line `a=0`.

---

## 6. Saddle beats shoulder iff `lambda>32 theta`

The safe denominator saddle has exponential rate

\[
\frac{\lambda^2}{16}.
\]

The worst shoulder numerator has rate

\[
2\theta\lambda.
\]

Therefore the shoulder is exponentially negligible precisely when

\[
\frac{\lambda^2}{16}>2\theta\lambda,
\]

i.e. for positive `lambda`,

\[
\boxed{\lambda>32\theta.}
\]

If lambda ranges in a compact subset of `(32 theta,infinity)`, there is a fixed positive rate gap `eta` such that

\[
N_{\rm shoulder}
\le
\exp\!\left(-\frac\eta t+o(1/t)\right)
D_{\rm core}.
\]

The remaining region `a>=1/2` outside the saddle neighborhood has no positive zeta power exponent; the strict concavity of `S_0` makes it exponentially smaller than the saddle, except inside the saddle neighborhood already controlled in Section 3. Large `a` is suppressed quadratically by the Gaussian.

Consequently

\[
\boxed{
\mathcal Q_{c,t}(\gamma)=o(1).
}
\]

---

## 7. Collision exclusion

For

\[
c=\Re\alpha(1/2+i\gamma),
\]

we have

\[
c^2t
=\frac{\lambda^2}{4t}(1+o(1))\to\infty.
\]

Therefore the Round-42 collision threshold satisfies

\[
\frac{2}{1+2/(c^2t)}\to2.
\]

But Round 43 gives

\[
\mathcal Q_{c,t}(\gamma)\to0.
\]

Hence, for sufficiently small `t`, the collision inequality is violated. Thus no multiple real zero exists in this scaling region.

### Theorem 43.1

Let `theta>=1/8` be any exponent for which

\[
|\zeta(1/2+iT)|\ll_\varepsilon T^{\theta+\varepsilon}
\]

holds. Fix

\[
\lambda_0>32\theta,
\qquad
\lambda_1>\lambda_0.
\]

Then there exists `t_0>0` such that whenever

\[
0<t<t_0,
\qquad
\lambda_0\le t\log\frac{x}{4\pi}\le\lambda_1,
\]

with `x=2 gamma` sufficiently large according to this scaling, `H_t` has no multiple real zero at `x`.

**Status:** PROVED asymptotically from the stated subconvexity input and standard Stirling/Phragmen--Lindelof estimates. No RH assumption.

---

## 8. Bourgain input

Bourgain's published decoupling/exponential-sum work gives

\[
\boxed{
|\zeta(1/2+iT)|\ll_\varepsilon T^{13/84+\varepsilon}.
}
\]

Thus

\[
32\theta
=32\cdot\frac{13}{84}
=\boxed{\frac{104}{21}}
\approx4.95238095.
\]

Therefore Theorem 43.1 gives an unconditional collision-free small-`t` region

\[
\boxed{
\lambda>\frac{104}{21}+\varepsilon
}
\]

in the asymptotic scaling sense above.

This is close to, but slightly weaker than, the separate Round-20/22 program threshold

\[
\lambda_*\approx4.914588956.
\]

No improvement of the current program threshold is claimed.

---

## 9. General exponent-profile form

The argument does not fundamentally require linear Phragmen--Lindelof interpolation. Suppose instead one has a pointwise exponent profile

\[
|\zeta(1/2+a+iT)|
\ll T^{\mu(a)+o(1)},
\qquad 0\le a\le1/2.
\]

Then the exact exponential gate becomes

\[
\boxed{
\sup_{0\le a\le1/2}
\left(
-a^2+\frac\lambda2a+2\lambda\mu(a)
\right)
<\frac{\lambda^2}{16}.
}
\]

This is the correct interface for importing sharper sigma-dependent subconvexity estimates into the collision program.

A future improvement need not improve the critical-line exponent alone; it may instead lower the exponent profile at the particular shoulder point maximizing the displayed functional.

---

## 10. Circularity audit

The proof uses only:

- the Round-42 collision necessary condition;
- Stirling asymptotics for the explicit gamma/completed factor;
- absolute convergence of the zeta and reciprocal-zeta Dirichlet series for `Re s>1`;
- a genuine unconditional subconvexity bound;
- Phragmen--Lindelof interpolation;
- Cauchy's derivative estimate.

It does not use:

- RH or Lindelof;
- `Lambda<=0`;
- a zero-free region around the critical line;
- a lower zero gap;
- Laguerre positivity;
- Rodgers--Tao negative-time local equilibrium.

The subconvexity hypothesis is an established theorem when `theta=13/84`; it is not RH-equivalent.

---

## 11. Program consequence

Round 43 creates a genuine cross-frontier conversion law:

\[
\boxed{
\text{zeta growth exponent profile}
\longrightarrow
\text{positive-time collision-free lambda region}.
}
\]

With the current record exponent, this route lands just above the existing local collision threshold. Therefore the next useful task is **not** to repeat the same proof with more constants. It is to optimize the exponent profile `mu(a)` using the best known interior-strip bounds and determine whether the variational gate in Section 9 can cross below

\[
\lambda_*\approx4.914588956.
\]

If not, the exact amount by which it misses should be recorded as the new arithmetic bottleneck.

---

## 12. Status

- two-saddle quotient shoulder/core decomposition: **PROVED asymptotically**;
- general exponent-profile gate: **PROVED**;
- linear subconvexity gate `lambda>32 theta` for `theta>=1/8`: **PROVED**;
- Bourgain application `lambda>104/21`: **PROVED from established subconvexity**;
- improvement over existing `lambda_*`: **NO**;
- optimized interior-strip exponent profile: **OPEN / next target**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
