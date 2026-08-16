# Round 88 — Joint-core kernel no-go and the endpoint logarithmic-moment constraint

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Status:** PROVED STRUCTURAL NO-GO + NEW COLLISION-CONDITIONED GEOMETRIC CONSTRAINT.  
**Strict-program admissibility:** PASSED.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Starting point

Round 87 identifies the phase-invariant collision quantity

\[
\mathfrak D_t
=\phi_x|S|^2
-\sigma_x\Im(\overline ST)
-\tau_x\Re(\overline ST),
\]

where

\[
S=\sum_{n\le N}a_ne^{-i\tau\log n},
\qquad
T=\sum_{n\le N}a_n\log n\,e^{-i\tau\log n}.
\]

In the singular wedge,

\[
t\phi_x\to-\frac\lambda4,
\qquad
\tau_x\to-\frac12,
\qquad
\sigma_x\to0.
\]

Hence the leading scaled form is

\[
-4t\mathfrak D_t
=
\lambda|S|^2-2t\Re(\overline ST)+o(1)\cdot\mathcal M,
\tag{88.1}
\]

where `M` denotes the corresponding quadratic amplitude scale.

---

## 2. Exact rank-two kernel and failure of naive positivity

Put

\[
u_n=t\log n,
\qquad
z_n=a_ne^{-i\tau\log n}.
\]

Then

\[
\lambda|S|^2-2t\Re(\overline ST)
=
\sum_{m,n\le N}
(\lambda-u_m-u_n)z_n\overline{z_m}.
\tag{88.2}
\]

Since

\[
u_n\le t\log N=\frac\lambda2+o(1),
\]

the scalar entries `lambda-u_m-u_n` are nonnegative to leading order.

This does **not** make the Hermitian form positive semidefinite.
For two distinct logarithmic positions `u1 != u2`, the real kernel matrix is

\[
K=
\begin{pmatrix}
\lambda-2u_1&\lambda-u_1-u_2\\
\lambda-u_1-u_2&\lambda-2u_2
\end{pmatrix},
\]

and

\[
\boxed{\det K=-(u_1-u_2)^2<0.}
\tag{88.3}
\]

Thus the leading joint-core kernel is indefinite as soon as two distinct scales are present.

**Consequence:** a proof of collision exclusion below `lambda=2` cannot be obtained by declaring (88.2) positive from entrywise positivity. Any such argument is false.

---

## 3. Factorization of the indefinite form

Define

\[
U:=tT=\sum_{n\le N}u_n z_n.
\]

Then the same form is exactly

\[
Q:=\lambda|S|^2-2\Re(\overline S U).
\tag{88.4}
\]

Equivalently, with the endpoint-centered first moment

\[
V:=\frac\lambda2S-U
=
\sum_{n\le N}
\left(\frac\lambda2-u_n\right)z_n,
\tag{88.5}
\]

one has

\[
\boxed{Q=2\Re(\overline S V).}
\tag{88.6}
\]

So the leading invariant is not a norm; it is a bilinear pairing between the value `S` and the distance-to-cutoff moment `V`.

---

## 4. Collision turns the derivative equation into an endpoint-moment constraint

Rotate by the outer phase:

\[
Z=e^{i\phi}S=X+iY,
\qquad
W=e^{i\phi}U=A+iB,
\qquad
R=e^{i\phi}V.
\]

At a hypothetical collision, after the Polymath normalized errors are inserted,

\[
X=O(E_0),
\tag{88.7}
\]

and

\[
0
=
-\phi_xY+\Re(e^{i\phi}S_x)+O(E_1).
\tag{88.8}
\]

Using

\[
S_x=-(\sigma_x+i\tau_x)T
=-\frac1t(\sigma_x+i\tau_x)U,
\]

multiply (88.8) by `t`.  Since

\[
t\phi_x=-\frac\lambda4+o(1),
\qquad
\tau_x=-\frac12+o(1),
\qquad
t\sigma_x=o(1),
\]

we obtain the leading relation

\[
\boxed{
B=\frac\lambda2Y+o(1)\,(|S|+|U|)+O(tE_1).
}
\tag{88.9}

But

\[
\Im R
=\frac\lambda2Y-B.
\]

Hence every collision forces

\[
\boxed{
\Im\left(
e^{i\phi}
\sum_{n\le N}
\left(\frac\lambda2-t\log n\right)
a_ne^{-i\tau\log n}
\right)
=o(1)\,(|S|+|U|)+O(tE_1).
}
\tag{88.10}

Together with the value equation

\[
\boxed{\Re(e^{i\phi}S)=O(E_0),}
\tag{88.11}

this is a **two-moment collision system**.

The second moment uses the nonnegative distance-to-cutoff weights

\[
\frac\lambda2-t\log n\ge-o(1),
\]

and vanishes at the terminal saddle scale.

---

## 5. Why (88.10) is stronger than the old scalar PSC description

The old PSC upper-bounds the entire logarithmic moment by an absolute scalar `A1`, losing where in the Riemann--Siegel range the derivative mass sits.

Equation (88.10) keeps the exact distance from each term to the moving cutoff.  Thus it distinguishes:

- low-index core mass, for which `lambda/2-t log n` is order one;
- near-cutoff mass, for which the same factor is small.

A collision therefore requires the phase-rotated imaginary part of the **low-index weighted core** to cancel almost exactly against the much more weakly weighted terminal layer.

This is the precise geometric content that an admissible below-2 certificate should exploit.

---

## 6. Immediate no-go for a purely diagonal proof

The diagonal part of `-4t D_t` is

\[
\sum_{n\le N}
(\lambda-2u_n)|z_n|^2
=2\sum_{n\le N}
\left(\frac\lambda2-u_n\right)a_n^2
\ge0.
\]

But because the full kernel has the negative determinant (88.3), this positive diagonal cannot dominate the off-diagonal terms by algebra alone.

Any future diagonal-dominance claim must therefore invoke a genuine arithmetic cancellation theorem for the phases

\[
e^{-i\tau\log(n/m)},
\]

not just positivity of the weights.

---

## 7. New target: endpoint-moment transversality (EMT)

Define

\[
S_0
:=
\sum_{n\le N}a_ne^{-i\tau\log n},
\]

\[
S_1
:=
\sum_{n\le N}
\left(\frac\lambda2-t\log n\right)
a_ne^{-i\tau\log n}.
\tag{88.12}
\]

The collision system is asymptotically

\[
\Re(e^{i\phi}S_0)=0,
\qquad
\Im(e^{i\phi}S_1)=0.
\tag{88.13}
\]

The next theorem target is therefore:

> **EMT:** establish, in some `lambda<=2` range, a quantitative lower bound preventing the two rotated scalar conditions in (88.13) from holding simultaneously, with the Polymath `E0,tE1` errors included.

This is strictly weaker than requiring `S_0` itself to be nonzero and strictly different from requiring a positive Hermitian quadratic form.

---

## 8. Candidate methods for EMT

The following routes are admissible and should be tested in this order.

1. **Two-component exponential-sum transform.**  Apply the same exponent-pair / beta machinery simultaneously to `S0` and the cutoff-distance weighted sum `S1`, retaining their phase relation.
2. **Riemann--Siegel saddle transform.**  Derive the dual representation of the pair `(S0,S1)`; the distance-to-cutoff factor may become a derivative of the fractional saddle correction and could provide a Wronskian-like nondegeneracy.
3. **Exact joint-jet computation on the critical compact remainder.**  If the analytic transform leaves only a compact fractional-saddle parameter, certify the determinant numerically with interval arithmetic.
4. **Prime/multiplicative grouping only if 1--3 fail.**  Do not move immediately to generic prime correlations; Rounds 48--61 show the cost of doing so.

---

## 9. Circularity audit

No positivity of `Q` or `D_t` is assumed; in fact Round 88 proves the naive positivity claim false.

The collision equations (88.10)--(88.13) are algebraic consequences of the normalized value/derivative system and the exact real-axis phase derivatives.

No RH, zeta nonvanishing in the critical strip, zero simplicity, pair correlation, or Laguerre--Polya positivity is used.

**RH remains OPEN.**
