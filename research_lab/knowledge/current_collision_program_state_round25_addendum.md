# Collision Program State — Round 25 addendum

**Date:** 2026-08-16

**RH status:** OPEN.

## Executive correction

The Round-19 all-multiplicity local theorem remains valid:

\[
\deg_{\rm loc}(F,F_x)=-\lfloor m/2\rfloor<0.
\]

But Rounds 21, 23, and 24 show that the proposed promotion

\[
B\gtrsim A
\]

is not justified by the global winding route. On a collision-free time slice,

\[
\Delta_a^b\arg(F+iF_x)
=
\arctan\frac{F_x(b)}{F(b)}
-
\arctan\frac{F_x(a)}{F(a)}
-
\pi N_F(a,b),
\]

and on an even finite rectangle with no spatial zero crossing,

\[
\deg(F,F_x;D)
=-\frac12\Delta N_{\mathbb R}.
\]

Therefore the raw global Brouwer degree is the topological spectral flow of the real-zero count. The natural Polymath renormalization likewise reduces exactly to the count defect `g(X,t)-N_t^+(X)`. High-`X` asymptotics control spatial transport but do not independently determine the lower horizontal-face census.

The justified ranking is therefore

\[
\boxed{A\gtrsim B\gg C.}
\]

## Round 25: entropy-budget trilemma

Let an isolated generic double collision occur at `t=t_c`, with

\[
g^2=8\tau+O(\tau^2),\qquad \tau=t-t_c\downarrow0.
\]

If an absolutely continuous state variable satisfies

\[
\dot C=\sigma\frac{\alpha}{g^2}+R,
\qquad
\alpha>0,
\qquad
\sigma\in\{\pm1\},
\qquad
R\in L^1,
\]

then necessarily

\[
\boxed{C=\sigma\frac{\alpha}{8}\log\tau+O(1).}
\]

Hence a collision-sensitive inverse-square detector with integrable errors forces logarithmic divergence of the state variable.

This yields the local trilemma:

1. **retain the detector:** the entropy diverges logarithmically and collision exclusion requires an independently proved one-sided budget;
2. **renormalize the state to remain finite:** any regular compensator must contain the opposite logarithm, and its derivative cancels the leading `1/\tau` detector;
3. **claim both a finite state and an uncancelled detector:** then some flux/reference/remainder term must be nonintegrable and carry the opposing singularity.

For the Round-18 relative log-Vandermonde, the colliding ordered pair contributes

\[
\mathscr C_{w,\rm pair}=w\log\tau+O(1)\to-\infty,
\]

so the missing independent budget is a lower bound.

For the positive Round-17 Bregman entropy with locally constant pair weight,

\[
\mathcal C_{\rm Breg,pair}=-\log\tau+O(1)\to+\infty,
\]

so the missing independent budget is an upper bound.

With bounded spectator contributions, either such one-sided logarithmic entropy bound is quantitatively equivalent locally to a positive lower bound on the colliding gap. This is not automatically circular, but it means every proposed entropy budget must be audited to ensure that the lower-gap information is proved independently rather than assumed in disguise.

## Program A after Round 25

The algebraic and cutoff structure is now strong:

- exact hard-window Vandermonde flux;
- exact relative Rodgers--Tao `V`-energy balance;
- exact Bregman force-square balance;
- near cutoff commutator perturbative at Rodgers--Tao scales;
- classical-location reference force `S_j^xi=-pi/8+o(1)` on the positive side;
- signed leading reference drift converted to a regular cross-origin interaction;
- residual reference error absorbable at polylogarithmic cost.

But these facts alone do not produce the required one-sided entropy bound.

The next admissible A-side target is therefore Riemann-specific: derive a one-sided budget from the Fourier-kernel/entire-function structure or unconditional positive-time estimates, without assuming real-rootedness, a lower gap, global Laguerre positivity, or any Rodgers--Tao estimate whose proof uses the contradiction hypothesis `Lambda<0`.

## Program B after Rounds 23--24

Program B remains a valid local collision-counting theorem and diagnostic. It returns to primary status only if one finds a boundary observable whose computable part is **not** algebraically reducible to the real-zero count defect.

The following are not independent closures:

- raw horizontal winding of `H+iH'`;
- the natural `g(X,t)`-renormalized winding;
- global `L1>=0` phase monotonicity;
- Hermite--Biehler stability already equivalent to real-rootedness;
- equality of real-zero counts assumed or derived from a no-collision gap bound.

## Circularity/source guard

Safe inputs for proving `Lambda<=0` include:

- the backward heat PDE and local Hermite collision normal forms;
- exact finite algebraic identities for `V`, `L`, cutoffs, and reference locations;
- unconditional positive-time Polymath estimates in the ranges actually proved;
- argument-principle identities not supplemented by an unproved zero-free statement.

Unsafe without a new independent proof:

- quantitative Rodgers--Tao negative-time local-equilibrium/gap estimates obtained under `Lambda<0`;
- global LP/Laguerre/Hermite--Biehler hypotheses on the unknown slice;
- lower-gap assumptions that already exclude the target collision.

## Immediate next step

The next research task should not be another raw winding computation. It is the following dichotomy:

> Search for a Riemann-specific one-sided entropy/coercive budget that survives the Round-25 trilemma; if every natural candidate reduces to a lower-gap/all-real-zero assertion, prove that impossibility for the candidate class and move to a genuinely different observable.

**No proof of RH is claimed. Novelty of the new packaging remains unverified.**
