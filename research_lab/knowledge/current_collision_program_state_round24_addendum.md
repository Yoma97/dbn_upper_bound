# Collision Program State — Round 24 addendum

**Date:** 2026-08-16

**RH status:** OPEN.

## New adjudication

Rounds 23--24 attack the proposed promotion of Program B to primary status.

The all-multiplicity local theorem remains valid:

\[
\deg_{\rm loc}(F,F_x)=-\lfloor m/2\rfloor<0.
\]

However the horizontal winding of

\[
W=F+iF_x
\]

is exactly a real-zero counting observable. On a collision-free slice,

\[
\Delta_a^b\arg W
=
\arctan\frac{F'(b)}{F(b)}
-
\arctan\frac{F'(a)}{F(a)}
-
\pi N_F(a,b).
\]

For even `F` on `[-X,X]`,

\[
\frac1{2\pi}\Delta_{-X}^{X}\arg W
=
\frac1\pi\arctan\frac{F'(X)}{F(X)}
-N_F^+(X).
\]

Therefore, on a rectangle with no spatial zero crossing,

\[
\deg(F,F_x)
=-\frac12\Delta N_{\mathbb R}.
\]

Thus Program B's global winding is not yet an independent integer budget; it is the topological spectral flow of the real-zero count.

Renormalizing the winding by the Polymath smooth counting model `g(X,t)` leaves exactly

\[
g(X,t)-N_t^+(X),
\]

so high-`X` asymptotics alone do not remove the unknown lower-time-face real-zero census.

## Correct ranking

The justified ranking is

\[
\boxed{A\gtrsim B\gg C.}
\]

### A — PRIMARY
Exact relative Vandermonde/Bregman/Rodgers--Tao `V`-energy balances plus cutoff/reference control. Remaining gate: an independent one-sided finite entropy/coercive budget, or an impossibility theorem showing natural such budgets are equivalent to no-collision.

### B — CONDITIONAL SECONDARY
All-multiplicity negative local degree remains a useful theorem and diagnostic. Promote B only if a boundary observable can be computed from Riemann-specific information genuinely weaker than the real-zero census/LP positivity.

### C — TERTIARY
Low-complexity arithmetic separator.

## Source guard

Safe for a proof of `Lambda<=0`:

- unconditional positive-time Polymath asymptotics in their proved ranges;
- heat-flow local normal forms;
- exact argument-principle identities;
- algebraic Rodgers--Tao `L,V,xi_j,psi_T` structures.

Unsafe without independent reproof:

- Rodgers--Tao negative-time local-equilibrium estimates derived under their contradiction hypothesis `Lambda<0`;
- any global `L1>=0`, Hermite--Biehler, or all-real-zero assumption on the unknown slice;
- lower-gap bounds equivalent to no collision.

## Immediate next target

Program A: classify possible one-sided entropy budgets. Either construct one from Riemann-kernel/entire-function data independent of RH, or prove a structural impossibility/trilemma showing that every natural pairwise logarithmic entropy either diverges at collision, cancels its own collision detector, or requires an RH-equivalent input.

Program B: only pursue a renormalized boundary observable if it can be proved not algebraically reducible to `g-N_real`.

**No proof of RH is claimed.**
