# Collision Program State — Round 28 addendum

**Date:** 2026-08-16

**RH status:** OPEN.

## Executive state after Rounds 26--28

The collision program has now resolved three additional structural questions.

### 1. Entropy singularity for every multiplicity

At an isolated multiplicity-`m` real heat collision, with `tau=t-t_c` on the real-simple side,

\[
\Delta_{\rm loc}(t)
=\Delta(Q_m)\tau^{\binom m2}(1+O(\tau)),
\]

where

\[
Q_m=e^{-\partial_X^2}X^m=H_m(X/2)
\]

and

\[
\Delta(Q_m)
=2^{\binom m2}\prod_{k=1}^m k^k.
\]

Hence

\[
\partial_t\log\Delta_{\rm loc}
=\frac{\binom m2}{\tau}+O(1),
\qquad
E_{\rm ord,loc}
=\frac{m(m-1)}{8\tau}+O(1),
\]

while the hard-window external flux stays `O(1)` for every fixed multiplicity.

Therefore the one-sided log-entropy budget is locally a quantitative lower bound on the local discriminant/resultant, not a softer independent invariant.

### 2. Generic kernel regularity cannot supply transversality

There exist positive, even, smooth, super-exponentially decaying, strictly decreasing, strictly log-concave admissible kernels whose backward-heat Fourier family has an exact double real zero at an arbitrarily prescribed positive heat time.

Therefore no collision-exclusion theorem can follow merely from:

- positivity;
- evenness;
- smoothness;
- rapid decay;
- monotone decrease;
- ordinary strict log-concavity;
- boundedness/analyticity of finitely many kernel moments, imaginary-axis values, Sobolev norms, or fixed-boundary Jensen observables.

These data are collision-blind unless an additional inequality links them to the local resultant.

### 3. The first differential Riemann-kernel coupling lands on the Laguerre barrier

For

\[
\psi_t=e^{tu^2}\Phi(u),
\qquad
q(u)=-\frac{\Phi'(u)}{u\Phi(u)},
\]

Rounds 13--15 give `q>1` and `q'>0`. Thus for `0<=t<=1/2`,

\[
(\log\psi_t)'=u(2t-q)<0,
\]

\[
(\log\psi_t)''=2t-q-uq'<0.
\]

So `psi_t` is itself an admissible strictly log-concave kernel throughout the positive interval relevant to a hypothetical positive `Lambda`.

However the first-order differential coupling gives only the already-known identity

\[
S_1=xH_t+2tS_0.
\]

The natural next determinant is

\[
L_1(H_t)=(H_t')^2-H_tH_t'',
\]

whose associated-kernel representation is the Csordas `K_1` construction. Log-concavity makes the associated kernels admissible, but the required positive definiteness / Fourier sign is the hard missing step. For the Riemann transform the basic `L_1>=0` question is already explicitly open in that theory.

The exact evolution law

\[
(\partial_t+\partial_x^2)L_1(H_t)=2L_1(H_t')
\]

also blocks the naive downward maximum-principle strategy. With `s=T-t`,

\[
\partial_sL_1
=\partial_x^2L_1-2L_1(H_{T-s}'),
\]

so even a nonnegative derivative-level Laguerre term enters with the wrong sign for preserving a lower bound while moving toward smaller `t`.

## Route adjudication

The overall ranking remains

\[
\boxed{A\gtrsim B\gg C,}
\]

but `A` must now be split conceptually.

### A-local-generic — FROZEN

No further work should be spent deriving collision exclusion from generic positivity, admissibility, ordinary log-concavity, fixed Fourier moments, or naive maximum-principle propagation of `L_1`.

### A-Riemann-specific — LIVE

A survives only through genuinely special structure, such as:

1. a theta-functional decomposition controlling the associated kernel/resultant;
2. a finite sign-regular identity stronger than the TP2 consequences already refuted;
3. an arithmetic/explicit-formula contribution with independently controlled sign;
4. a cross-frontier bridge from pair correlation/zero density/another established zeta statistic to collision transversality.

### B — CONDITIONAL DIAGNOSTIC

The all-multiplicity Brouwer charge remains valid, but raw and naturally renormalized boundary winding reduce to real-zero-count spectral flow. B returns to primary status only if a genuinely independent boundary observable is found.

### C — TERTIARY

No change.

## Circularity guard after Round 28

Reject as non-progress any proposed closure whose decisive step is one of:

- assume/prove a lower gap by an equivalent formulation;
- assume all real zeros / Laguerre--Polya membership;
- assume global strict `L_1>0` without an independent source of positivity;
- invoke all generalized Laguerre inequalities as an input;
- invoke positive definiteness of all Csordas associated kernels as an unexplained hypothesis;
- import Rodgers--Tao negative-time gap/local-equilibrium estimates proved under `Lambda<0`;
- treat pointwise positivity of an associated kernel as positive definiteness;
- claim downward maximum-principle propagation for `L_1` despite the negative forcing term.

## Immediate next target

The next local A-side test is now sharply constrained:

> Derive an exact theta-series decomposition of `K_{1,t}` or of an equivalent normalized resultant/transversality quantity and determine whether it splits into a manifestly positive main term plus a defect that can be controlled independently.

If this merely rewrites `L_1` without producing an independent sign, freeze the local kernel route completely and pivot to the cross-frontier program.

**No proof of RH is claimed. Novelty of the new local packaging remains unverified.**
