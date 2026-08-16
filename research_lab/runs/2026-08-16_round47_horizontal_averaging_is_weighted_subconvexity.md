# Round 47 — Horizontal shoulder averaging creates no new oscillation: exact reduction to weighted subconvexity

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED STRUCTURAL REDUCTION / NO FREE AVERAGING GAIN / CROSS-FRONTIER BOTTLENECK / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 44 left two apparent ways to beat the critical-line pointwise bottleneck: improve the critical-line subconvexity exponent itself, or exploit an **averaged horizontal shoulder estimate**. Rounds 45--46 removed two naive variants of the second idea.

This round identifies exactly what horizontal averaging does to the Dirichlet-polynomial side.

At fixed ordinate `gamma`, varying the horizontal variable `a=Re(s)-1/2` changes

\[
n^{-s}=n^{-1/2-a-i\gamma}
\]

only through the positive amplitude `n^{-a}`. The oscillatory phase

\[
\boxed{e^{-i\gamma\log n}}
\]

is completely independent of `a`.

Consequently every horizontal integral against a positive kernel is merely a **positive smooth Mellin/Laplace reweighting of the same exponential sum**. It does not generate a new oscillatory variable and it does not diagonalize the mean square.

Thus a successful averaged-shoulder theorem would require a genuinely stronger uniform estimate for a family of smooth weighted sums

\[
\sum_n w_t(n) n^{-1/2-i\gamma},
\]

or their derivative-weighted analogues. This is a weighted subconvexity problem at a single ordinate, not a free consequence of averaging.

---

## 1. Linear horizontal averaging

Let

\[
D_\gamma(a)
:=\sum_{n\le N}c_n n^{-a}e^{-i\gamma\log n},
\]

where the coefficients `c_n` do not depend on `a`.

Let `K(a)>=0` be integrable on `[0,infinity)`. Define its Laplace transform

\[
\mathcal L K(y)
:=\int_0^\infty K(a)e^{-ay}\,da.
\]

Fubini gives exactly

\[
\boxed{
\int_0^\infty K(a)D_\gamma(a)\,da
=
\sum_{n\le N}c_n e^{-i\gamma\log n}
\mathcal L K(\log n).
}
\]

If `K>=0`, then

\[
\mathcal L K(\log n)>0.
\]

Hence the horizontal integration changes only the real positive magnitude assigned to each frequency `log n`; it creates no new phase cancellation in the integration variable.

---

## 2. Boundary-layer scaling

The critical shoulder in Rounds 43--46 lives on the scale

\[
a=O(t),
\qquad
\log\gamma\asymp1/t.
\]

Write a normalized boundary-layer kernel as

\[
K_t(a)=\frac1t k(a/t),
\qquad k\ge0.
\]

Then

\[
\mathcal L K_t(\log n)
=
\int_0^\infty k(y)e^{-t y\log n}\,dy
=\mathcal L k(t\log n).
\]

For the approximate-functional-equation range

\[
n\le \gamma^{1/2+o(1)},
\]

one has

\[
0\le t\log n\le\frac\lambda2+o(1).
\]

Thus horizontal averaging produces a smooth multiplier on a **fixed compact scale** in the normalized logarithmic variable `t log n`. It does not force the high frequencies to zero and does not introduce a rapidly oscillating transform.

For the simplest exponential shoulder kernel

\[
k(y)=q e^{-qy},
\]

one obtains explicitly

\[
\boxed{
\mathcal L k(t\log n)
=\frac{q}{q+t\log n}.
}
\]

This is positive, monotone, and of order one throughout the main Dirichlet-polynomial range.

---

## 3. Horizontal mean square does not diagonalize

The distinction from vertical mean-value theory is even clearer for the square.

Expanding,

\[
|D_\gamma(a)|^2
=
\sum_{m,n\le N}
c_n\overline{c_m}
(mn)^{-a}
 e^{-i\gamma\log(n/m)}.
\]

Therefore

\[
\boxed{
\int_0^\infty K(a)|D_\gamma(a)|^2da
=
\sum_{m,n\le N}
c_n\overline{c_m}
 e^{-i\gamma\log(n/m)}
\mathcal L K(\log(mn)).
}
\]

The horizontal kernel depends on

\[
\boxed{\log(mn),}
\]

not on the frequency difference

\[
\log(n/m).
\]

Hence it does not suppress the off-diagonal terms `m != n` by Fourier orthogonality.

By contrast, averaging in the ordinate variable `gamma` would introduce a Fourier transform in `log(n/m)` and can diagonalize or nearly diagonalize Dirichlet-polynomial mean squares. That mechanism is absent here because collision localization fixes `gamma`.

---

## 4. Derivative energies remain the same phase problem

Horizontal differentiation gives

\[
\partial_aD_\gamma(a)
=-\sum_{n\le N}c_n(\log n)
 n^{-a}e^{-i\gamma\log n}.
\]

Thus derivative factors merely insert real weights `log n`. More generally, every fixed derivative order inserts a polynomial in `log n` but leaves the phase `e^{-i gamma log n}` unchanged.

The Round-42 operator

\[
\partial_a-c
\]

similarly replaces the coefficient by

\[
-(\log n+c)c_n
\]

on the elementary Dirichlet terms, again without any new horizontal oscillation.

Therefore the numerator of the two-saddle quotient is governed by the same fixed-ordinate exponential-sum cancellation as the zeta value itself, with smooth logarithmic weights.

---

## 5. Approximate functional equation

The actual zeta function in the shoulder is represented by an approximate functional equation with two Dirichlet polynomials whose phases are functions of `gamma log n` together with the explicit functional-equation phase.

When `a` varies horizontally at fixed `gamma`, the Dirichlet phases remain fixed; only their amplitudes change smoothly. The functional-equation/gamma phase varies with `a`, but on the endpoint layer `a=O(t)` its variation is only `O(t)` after the dominant real slope has been handled by the two-saddle gauge. This variation is not a new large oscillatory parameter.

Hence the same structural conclusion persists for the full approximate functional equation: horizontal averaging is a smooth family of weighted fixed-ordinate exponential sums.

---

## 6. No generic cancellation gain from positivity of the horizontal kernel

Suppose the coefficient phases in a finite exponential sum happen to be aligned on a subset of indices. Since the horizontal multipliers

\[
\mathcal L K(t\log n)
\]

are positive, horizontal averaging preserves rather than destroys that alignment.

Thus no theorem based only on

- positivity of the horizontal kernel;
- its localization width;
- smoothness of the multiplier;
- the length of the Dirichlet polynomial

can guarantee a power-saving cancellation absent an additional arithmetic/exponential-sum estimate.

This is the correct sense in which the averaged-shoulder route offers **no free averaging gain**.

---

## 7. What a successful arithmetic theorem would now have to prove

After boundary-layer rescaling, the desired input is schematically a uniform estimate

\[
\boxed{
\left|
\sum_{n\le \gamma^{1/2+o(1)}}
\frac{e^{-i\gamma\log n}}{\sqrt n}
W(t\log n)
\right|
\le
\gamma^{\eta+o(1)}
}
\]

for the specific smooth weights `W` generated by the collision quotient, together with analogous bounds after insertion of logarithmic derivative weights.

To beat the current collision threshold through this channel, one needs an effective exponent at the dangerous endpoint strictly below

\[
\boxed{
\theta_*\approx0.153580904875.
}
\]

or a coupled estimate for the weighted value and derivative combination which is stronger than bounding them separately by the Bourgain exponent.

This is a legitimate target because a special smooth weight might admit an estimate stronger than the completely general pointwise zeta bound. But such a result would constitute new exponential-sum/subconvexity input; it is not supplied automatically by the horizontal integral.

---

## 8. Relation to current literature input

The lab currently uses Bourgain's established critical-line exponent

\[
\theta=13/84
\]

as the strongest asymptotic pointwise input. Andrew Yang's interior-strip lines improve the exponent away from the critical line, but Round 44 proves that they cannot move the endpoint-dominated pointwise gate.

The smooth weighted sums arising here have the same fixed-ordinate phase `-gamma log n` that underlies classical subconvexity/exponential-sum methods. Therefore any claim of a better exponent must be independently proved; it must not be inferred merely from the existence of the smoothing kernel.

---

## 9. Program decision

The Rayleigh/two-saddle route has now achieved a genuine cross-frontier theorem, but its current closure bottleneck is explicit:

\[
\boxed{
\text{collision exclusion below }\lambda_*
\Longrightarrow
\text{new weighted fixed-ordinate exponential-sum control}
}
\]

within the present architecture.

Freeze generic claims that 'horizontal averaging should give cancellation'. It does not introduce an oscillatory averaging variable.

The route should be retained as a **conditional arithmetic bridge** rather than the sole primary route until a special weighted exponential-sum estimate is discovered.

The next invention round should therefore return to the broader P0 cross-frontier program and ask whether a collision/off-real defect forces an observable in pair correlation, horizontal multiplicity, or the explicit formula that is already controlled unconditionally, rather than trying another universal kernel inequality.

---

## 10. Status

- exact Laplace multiplier identity for horizontal averaging: **PROVED**;
- horizontal mean square diagonalizes Dirichlet polynomials: **REFUTED**;
- horizontal averaging creates a new oscillatory variable: **REFUTED**;
- shoulder smoothing reduces to smooth weighted fixed-ordinate exponential sums: **PROVED**;
- automatic power saving from smoothing alone: **REFUTED**;
- special weighted exponential-sum improvement beyond Bourgain: **OPEN**;
- Rayleigh/two-saddle route: **VALID CONDITIONAL BRIDGE / arithmetic bottleneck exposed**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
