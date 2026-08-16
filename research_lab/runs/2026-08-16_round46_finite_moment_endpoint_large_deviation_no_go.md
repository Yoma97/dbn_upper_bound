# Round 46 — Finite collision moments cannot change the critical-line large-deviation exponent

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED NO-GO / ENDPOINT LAPLACE PRINCIPLE / NOVELTY UNVERIFIED.

## 0. Executive theorem

Rounds 32--35 provide not only two collision moment conditions but an entire finite Hermite hierarchy at a multiplicity-`m` collision. One might hope that using more of these moments, rather than only the first two conditions used in Round 42, could lower the Round-44 pointwise subconvexity threshold.

At the large-deviation level this is impossible for every **fixed finite multiplicity**.

Suppose the dangerous shoulder contribution is bounded pointwise by an exponential rate

\[
\exp(S(a)/t)
\]

on `a>=0`, where

\[
S(0)=S_0,
\qquad
S'(0)<0.
\]

Then for every fixed integer `r>=0`,

\[
\boxed{
\int_0^\delta a^r e^{S(a)/t}\,da
=t^{r+1}e^{S_0/t}\left(C_r+o(1)\right)
}
\]

under the standard smooth nondegenerate endpoint hypotheses. In particular the exponential rate is always

\[
\boxed{S_0}
\]

independently of `r`.

Thus multiplying by finitely many powers of `a`, Hermite polynomials of fixed degree, or taking finitely many horizontal derivatives can alter only polynomial factors in `t`; it cannot lower the shoulder exponent `2 theta lambda` produced by the critical-line pointwise bound.

Consequently, with Bourgain's critical-line exponent left unchanged, **no fixed finite use of the collision moment hierarchy can move the pointwise gate below `lambda>32 theta`**.

---

## 1. Endpoint Laplace lemma

Let `S` be `C^2` on `[0,delta]` for some fixed `delta>0`, with

\[
S(0)=S_0,
\qquad
S'(0)=-q<0.
\]

Then for small positive `a`,

\[
S(a)=S_0-qa+O(a^2).
\]

Fix `r>=0`. Set

\[
a=ty.
\]

Then

\[
\begin{aligned}
I_r(t)
&:=\int_0^\delta a^r e^{S(a)/t}\,da\\
&=t^{r+1}e^{S_0/t}
\int_0^{\delta/t}
y^r
\exp\!\left(-qy+O(ty^2)\right)dy.
\end{aligned}
\]

The contribution from `y` larger than a fixed multiple of `log(1/t)` is exponentially small relative to the main endpoint contribution, and dominated convergence on the remaining range gives

\[
\boxed{
I_r(t)
\sim
\frac{r!}{q^{r+1}}
\,t^{r+1}e^{S_0/t}.
}
\]

The exact constant is less important than the invariant exponential rate.

---

## 2. Application to the Round-43 shoulder

For a critical-line exponent `theta>=1/8`, the pointwise shoulder rate is

\[
S_\theta(a;\lambda)
=-a^2+\frac\lambda2a
+2\theta\lambda(1-2a).
\]

At the endpoint,

\[
S_\theta(0;\lambda)=2\theta\lambda.
\]

Also

\[
S_\theta'(0;\lambda)
=\lambda\left(\frac12-4\theta\right).
\]

For the actual Bourgain exponent `theta=13/84>1/8`,

\[
S_\theta'(0;\lambda)<0.
\]

Hence every fixed polynomially weighted shoulder integral has exponential rate

\[
\boxed{2\theta\lambda.}
\]

For example,

\[
\int_0^\delta a^r
\exp\!\left(S_\theta(a;\lambda)/t\right)da
=t^{r+1+o(1)}
\exp\!\left(2\theta\lambda/t\right).
\]

---

## 3. Hermite moments are polynomial weights at the endpoint

The collision conditions from Round 32 have the form

\[
\int_{\mathbb R}G_t(a)
H_k(a/\sqrt t)
\xi(1/2+a+i\gamma)\,da=0,
\qquad 0\le k<m.
\]

For fixed `k`, the physicists' Hermite polynomial is a finite polynomial:

\[
H_k(a/\sqrt t)
=\sum_{j=0}^{\lfloor k/2\rfloor}
C_{k,j}\,a^{k-2j}t^{-(k-2j)/2}.
\]

Thus on the endpoint boundary layer `a=O(t)`, each fixed Hermite weight contributes only powers of `t`. It cannot modify the exponential rate inherited from the zeta bound.

The same statement holds after the two-saddle gauge: multiplication by a fixed-degree polynomial, or by any coefficient with at most `exp(o(1/t))` growth, leaves the `1/t` rate unchanged.

---

## 4. Finite horizontal derivatives also do not change the exponent

Suppose pointwise Cauchy estimates give, for fixed `j`,

\[
|\zeta^{(j)}(1/2+a+iT)|
\le T^{\theta(1-2a)+o(1)}
\times(\log T)^{O_j(1)}.
\]

In the scaling

\[
\log T\asymp1/t,
\]

the logarithmic factor is

\[
\exp(o(1/t)).
\]

Hence every fixed derivative order has the same large-deviation exponent as `zeta` itself.

Therefore combining finitely many derivatives with finitely many moments cannot lower the shoulder exponent either.

---

## 5. Consequence for fixed collision multiplicity

At a multiplicity-`m` collision, only the first `m` Hermite coefficients are forced to vanish. For any fixed finite `m`, every algebraic use of these conditions produces only a finite collection of polynomial endpoint weights.

Hence, within an argument that controls the shoulder solely through pointwise exponent bounds,

\[
\boxed{
\text{fixed finite multiplicity does not alter the critical exponent gate.}
}
\]

The safe-core rate remains

\[
\frac{\lambda^2}{16},
\]

and the shoulder rate remains

\[
2\theta\lambda.
\]

Thus the exponential comparison remains

\[
\boxed{\lambda>32\theta.}
\]

for every fixed finite `m`.

Higher multiplicity can improve polynomial prefactors and finite-`t` constants, but not the leading lambda threshold obtained from pointwise subconvexity.

---

## 6. What would be required to change the exponent without improving theta?

There are only three visible possibilities within this framework:

1. **a number of independent moment constraints growing like `1/t`**, so polynomial factors accumulate into an exponential effect; a generic finite collision does not supply this;
2. **arithmetic cancellation/phase information** inside the shoulder integral, so one does not take absolute values pointwise;
3. **a genuinely stronger critical-line amplitude theorem**, lowering `theta` itself.

Option 1 is unavailable for the target event unless one assumes unbounded multiplicity, which is not justified and would miss generic double collisions. Option 3 is the standalone subconvexity-record problem isolated in Round 44.

Therefore the only internally new route is Option 2.

---

## 7. Anti-circularity audit

This no-go theorem uses only elementary endpoint Laplace asymptotics and the already-established collision moment representation. It does not assume anything about the truth or falsity of RH, zero gaps, Laguerre positivity, or real-rootedness.

It also prevents a subtle form of overclaim: a longer finite list of RH-equivalent-looking moment vanishings at a collision must not be advertised as an exponential improvement unless one proves a mechanism that converts their number or structure into a true `1/t` gain.

---

## 8. Program decision after Round 46

Freeze:

- sharper fixed interior-strip pointwise bounds as a way to move the lambda gate (Round 44);
- delayed scalar gauges with the same Poincare mechanism (Round 45);
- using finitely many additional collision moments while still taking pointwise absolute values on the shoulder (this round).

The next legitimate target is therefore highly specific:

> retain the complex phase in the positive-half shoulder integral and derive an unconditional cancellation estimate for the actual Riemann `xi`/approximate-functional-equation Dirichlet polynomials on a horizontal window of width `O(t)`.

The estimate must be uniform in the ordinate and must not secretly assume Lindelof, RH, or a zero-free neighborhood. If horizontal phase does not oscillate on the relevant scale, prove that obstruction and freeze the averaged-shoulder route as well.

---

## 9. Status

- endpoint Laplace lemma: **PROVED**;
- finite polynomial/Hermite weights change endpoint exponent: **REFUTED**;
- finite derivative order changes endpoint exponent: **REFUTED**;
- fixed finite multiplicity improves `lambda>32 theta` under pointwise control: **REFUTED at large-deviation scale**;
- arithmetic phase-cancellation shoulder estimate: **OPEN / next target**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
