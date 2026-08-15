# Rigorous Arb Verification Protocol

## Purpose

Arb/FLINT is a **falsification and finite-certification layer**, not a theorem generator.
No finite computation may be used to infer an infinite RH statement.

## Current connected capability surface

The currently exposed Arb_Riemann_Lab interface provides only:

1. rigorous enclosure of `sqrt(value)`;
2. rigorous complex enclosure of `zeta(s)`;
3. rigorous enclosure of an indexed nontrivial zeta zero.

These operations are useful but insufficient for the lab's intended verification role.
Any claim requiring a capability not on this list must be marked
`ARB_CAPABILITY_MISSING`, never silently approximated with ordinary floating point.

## Required future server capabilities

The Arb server should eventually expose rigorous ball-enclosure endpoints for:

- `xi(s)` and derivatives `xi^(k)(s)`;
- canonical `H_t(z)` and derivatives under the Convention Lock;
- generalized Laguerre coefficients/expressions `L_n(x; F)` for supported F;
- real and complex ball arithmetic primitives;
- rigorous interval integration for the Riemann kernel and heat-deformed kernel;
- rigorous interval extrema/sign certification on compact boxes;
- matrix eigenvalue and inertia enclosures for real symmetric/Hermitian interval matrices;
- determinant and smallest-singular-value enclosures;
- optional interval Newton/Krawczyk zero isolation for finite-dimensional local models.

Every endpoint must return:

- input convention/version identifier;
- precision bits;
- rigorous enclosure (midpoint-radius or interval form);
- whether the enclosure proves sign/nonvanishing/containment;
- any convergence/truncation theorem used internally;
- failure state when certification cannot be obtained at requested precision.

## Numerical evidence classes

### N0 — heuristic only
Ordinary floating point, plots, numerical fitting, non-rigorous optimization.
May inspire conjectures. Cannot certify anything.

### N1 — rigorous point enclosure
A single Arb ball evaluation.
Can refute a universal statement if it rigorously exhibits a counterexample.
Cannot prove a universal statement.

### N2 — rigorous finite compact certification
A finite interval/box is certified by interval arithmetic plus a stated covering or interval theorem.
Can prove a finite subproblem only.

### N3 — analytic reduction + finite certification
An analytic theorem reduces the original claim to finitely many certified compact cases, all of which are verified by Arb.
This may participate in a theorem proof, but the analytic reduction is mandatory and must be independently proved.

## Mandatory claim fields for any numerical use

Every claim using computation must record:

- `numerical_role`: REFUTE | DISCOVER | FINITE_CERTIFY;
- exact mathematical quantity evaluated;
- domain certified;
- precision used;
- rigorous enclosure returned;
- analytic theorem reducing any infinite claim to the finite domain;
- whether the computation is logically necessary or merely diagnostic.

## Hard rejection rules

Reject any proof that contains one of the following transitions:

- many sampled points => global sign;
- many verified zeta zeros => RH;
- very high finite height => no later exception;
- floating-point near-zero => exact zero;
- visually stable eigenvalues => convergent spectrum;
- numerical monotonicity => monotonicity theorem;
- interval result on a compact set => unbounded-domain theorem without analytic tail control.

## Counterexample-first policy

Before spending high precision on confirmation, use Arb to attack:

1. lowest polynomial degrees;
2. parity/multiplicity collision models;
3. parameter endpoints;
4. first prime/pole thresholds;
5. scaling extremes;
6. points suggested by symbolic sign changes;
7. candidate equality cases.

A single rigorous counterexample closes the candidate immediately and is more valuable than a large amount of confirming evidence.
