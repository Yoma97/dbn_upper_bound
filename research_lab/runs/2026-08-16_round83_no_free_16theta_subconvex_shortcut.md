# Round 83 — No free `16 theta` shortcut from zeta subconvexity below `lambda=4`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Status:** STRUCTURAL WARNING / REFUTED SHORTCUT.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. The tempting but invalid shortcut

Round 82 identifies the absolute cutoff rate

\[
F_\lambda(\lambda/2)
=\frac{\lambda(4-\lambda)}{16}.
\]

A naive large-deviation calculation may suggest that if one imports a critical-line pointwise bound

\[
|\zeta(1/2+iT)|\ll T^{\theta+o(1)},
\]

then the critical contribution should have a rate resembling

\[
-\frac{\lambda^2}{16}+\theta\lambda,
\]

which is negative for

\[
\lambda>16\theta.
\]

With Bourgain's `theta=13/84`, this formal threshold would be

\[
16\theta=\frac{52}{21}\approx2.47619.
\]

**This is not presently a valid collision theorem.**

---

## 2. Exact Gaussian identity explains why the critical line appears

For every integer `n>=1`,

\[
e^{(t/4)\log^2 n}
=
\frac1{\sqrt{\pi t}}
\int_{\mathbb R}
 e^{-a^2/t}n^a\,da.
\tag{83.1}
\]

Hence the heat-weighted half-sum may be written exactly as a Gaussian average of **truncated** Dirichlet polynomials shifted horizontally in the complex `s`-plane.

At the moving cutoff

\[
\log N\sim\frac\lambda{2t},
\]

the large-deviation saddle in (83.1) is

\[
a\sim\frac t2\log N\sim\frac\lambda4.
\]

Since the base real part is

\[
p=\frac12+\frac\lambda4,
\]

the large-deviation saddle indeed reaches

\[
p-a\sim\frac12.
\]

Thus the appearance of critical-line zeta growth in the cutoff layer is genuine, not an artefact.

---

## 3. Why a pointwise bound for full zeta is insufficient

The Polymath real-axis Riemann--Siegel model is a two-saddle / reflected construction. The collision certificates isolate a complex half-sum

\[
S_t=\sum_{n\le N}a_ne^{-i\tau\log n}
\]

and combine it with its reflected contribution after normalization.

A subconvexity estimate controls the **full zeta/Riemann--Siegel combination**. It does not imply a comparable bound for one half-sum in isolation at the self-dual length

\[
N\asymp\sqrt{|\tau|/(2\pi)}.
\]

At this length the Riemann--Siegel transformation sends a main sum to a dual sum of comparable length. The two pieces may each be substantially larger than their final combination and may cancel.

Therefore an estimate of the form

\[
|\zeta(1/2+iT)|\ll T^\theta
\]

cannot simply be substituted for

\[
|S_t|\ll T^\theta
\]

or for the heat-weighted cutoff correction. Such a substitution would be an unjustified loss of the two-saddle cancellation structure.

---

## 4. Collision conditioning makes this distinction essential

At a hypothetical collision, the normalized value condition already asserts that the two reflected contributions nearly cancel in the real direction.

Thus precisely the situation in which the full Riemann--Siegel combination is small is **not exceptional** for the collision analysis; it is the condition being tested.

What must remain nonzero is a joint value/derivative direction. Consequently any use of critical-line subconvexity below `lambda=4` must control a joint object that survives this reflected cancellation.

This is why Round 43 worked with a positive two-saddle Rayleigh quotient and obtained the genuine `32 theta` rate gate rather than a half-sum `16 theta` gate.

---

## 5. What would make a `16 theta`-type gate legitimate

One would need an additional theorem, for the **specific heat-weighted Riemann--Siegel halves**, of one of the following forms:

1. an upper bound on each half-sum individually that has the desired subconvex exponent;
2. a joint bound on the half-sum and its logarithmic derivative that is stable under reflected cancellation;
3. an exact saddle transform showing that the dangerous half-sum component cancels internally before the collision certificate takes a norm;
4. a positive Hermitian form whose prime/Dirichlet side is controlled by known subconvexity but whose spectral side retains the collision signal.

No such theorem is currently present in the project sources.

---

## 6. Generic van der Corput is also not a free replacement

For

\[
\sum_{n\asymp N}e^{-i\tau\log n},
\qquad
N^2\asymp|\tau|/(2\pi),
\]

the second derivative of the phase is of order one. A naive second-derivative estimate does not furnish square-root cancellation. The local saddle is exactly the Riemann--Siegel self-dual scale, so Poisson/saddle transformation produces a dual block rather than removing it.

Therefore statements such as

> `the endpoint terms alternate, so the block is O(sqrt(N))`

are heuristic and may fail near resonant fractional saddle positions.

---

## 7. Correct consequence for the program

Round 82 remains valid and closes every compact `lambda` interval strictly above `4` for sufficiently small `t`.

Below `4`, the next step is **not** to insert Bourgain's exponent mechanically. It is to derive the exact critical Riemann--Siegel cutoff profile, including the reflected half and the derivative, and only then ask which known zeta/exponential-sum bounds control that profile.

Thus the current hierarchy is:

\[
\boxed{
\lambda>4:\ \text{Round 82 closed for small }t;
}
\]

\[
\boxed{
\lambda=4:\ \text{critical two-saddle profile OPEN};
}
\]

\[
\boxed{
0<\lambda<4:\ \text{oscillatory/self-dual analysis OPEN}.
}
\]

The formal number `16 theta` is **not** a proved threshold and must not be quoted as one.

RH remains OPEN.
