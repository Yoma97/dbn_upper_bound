# Round 79 — Literature-reduction audit and program refocus

**Date:** 2026-08-16

**RH status:** OPEN.

## Executive conclusion

The proposed literature reduction is mathematically insightful but mixes two proof policies that must be separated.

### Unrestricted published-input track U
If one admits all unconditional published theorems, including those whose proofs use finite-height verification of RH, then Polymath's theorem `Lambda <= 0.22` may be used. Together with a strict heat-operator simplicity theorem for Laguerre–Polya functions, this removes `t>0.22` from any multiple-zero search. For every fixed epsilon>0, Polymath Theorem 1.5 then makes the large-x part of `epsilon<=t<=0.22` finite, leaving only a compact validated-computation problem. On this track the genuinely noncompact analytic regime is indeed the singular wedge `t->0+`, `log x ~ 1/t`.

### Strict project track S
The project constitution forbids finite-height RH verification anywhere in the proof ancestry. Polymath Theorem 1.1 `Lambda<=0.22` fails this stricter admissibility test because its proof uses Theorem 1.2 hypothesis (i), numerical verification of RH at time zero. Therefore `t>0.22` cannot be declared finished on the strict track by that theorem.

However, this does **not** destroy the main strategic insight. Polymath Theorem 1.5 is an unconditional analytic large-x theorem and is admissible independently of Theorem 1.1. Hence for every fixed epsilon>0, the large-x region `epsilon<=t<=1/2` is already controlled by literature, leaving a compact finite rectangle plus the same singular wedge as epsilon tends to zero. Thus the singular wedge remains the correct place for new uniform analysis even on the strict track; only the numerical top time is `1/2` rather than `0.22` unless an admissible strict upper bound for Lambda is supplied.

## Corrections to individual claims

1. **`Lambda<=0.22`**: unconditional in the ordinary mathematical sense, but not admissible under the project's transitive no-finite-height-RH-verification policy. Keep it only on Track U.

2. **Heat operator and simplicity**: the Craven–Csordas theorem does provide a ready-made strict simplicity result: if `f` is in the Laguerre–Polya class and has order less than two, then `exp(-alpha D^2) f` has only real simple zeros for `alpha>0`. This can replace the project's custom local backward-Hermite proof of interior simplicity on Track U, once the hypotheses for `H_s` are explicitly checked. In particular, do not merely infer `H_s in LP` from “all zeros real” without checking the growth/genus hypothesis; for the de Bruijn–Newman family this check should be recorded explicitly.

3. **Ki–Kim–Lee**: the useful statement is fixed-time asymptotic simplicity/reality: for each fixed positive deformation parameter, all but finitely many zeros are real and simple. It is not by itself a uniform theorem as `t->0`; the threshold may escape rapidly. Therefore it motivates the reduction but does not remove the singular wedge.

4. **Polymath Theorem 1.5**: this is the effective uniform replacement needed by the program. For `0<t<=1/2`, sufficiently large zeros are controlled once `x>=exp(C/t)` for an absolute C. Its proof improves/makes effective the Ki–Kim–Lee asymptotics. The argument-principle part yields uniqueness counting multiplicity in the relevant large-x boxes, so simplicity is available there, not merely reality.

5. **Compact reduction**: for each fixed epsilon>0, `exp(C/t)<=exp(C/epsilon)`. Thus the complement of the large-x theorem inside `epsilon<=t<=Tmax` is compact. This is a valid structural reduction. It does **not** mean one finite computation settles all positive t, because `X(epsilon)` diverges exponentially as epsilon->0.

6. **Singular wedge**: the natural scale is `lambda=t log(x/(4 pi))=O(1)`. This is exactly the noncompact boundary layer left by `x~exp(C/t)`. The existing exact-weight PSC, APVC, and Riemann–Siegel work should be reinterpreted as tools for this wedge, not as a need to rebuild all fixed-positive-time asymptotics.

7. **de Bruijn strip contraction**: useful for zero-strip geometry and the definition/monotonicity of Lambda, but not a substitute for simplicity. Keep as background/reduction machinery.

8. **Laguerre inequality L1**: `L1=f'^2-ff''`. Positivity of L1 is a necessary LP inequality and is useful as a local collision diagnostic, but L1 alone does not characterize LP or globally exclude all nonreal zeros. Generalized Laguerre inequalities require all orders.

9. **Zero-motion ODEs**: use only after simplicity is already known. Polymath explicitly points to the Ki–Kim–Lee verification in the regime `t>Lambda`; these ODEs must not be used to prove the simplicity needed to justify themselves.

10. **PF5 obstruction**: the 2026 preprint arXiv:2602.20313 gives a certified negative 5x5 Toeplitz minor for the original de Bruijn–Newman kernel, proving it is not PF5. This kills the direct strategy “prove the original kernel is PF-infinity”. It does not rule out every total-positivity-inspired transformed-kernel argument. Also, the preprint's global PF4 status is not the same as its certified Toeplitz configuration statement; do not overstate it.

11. **Platt–Trudgian height 3e12**: their published theorem rigorously verifies RH up to height `3*10^12` and simplicity there. This can improve a Polymath-style upper-bound computation on Track U, but the exact resulting Lambda bound must be independently certified from the Polymath criterion; do not simply import an approximate `0.20` as a theorem of Platt–Trudgian themselves.

## Program changes

### Archive / stop developing as primary routes

- Global “invent a collision barrier for every `0<t<=1/2` at once”.
- Direct PF-infinity / total positivity of the original de Bruijn–Newman kernel.
- Re-derivation of the effective Riemann–Siegel approximation already supplied by Polymath.
- Zero-motion ODE as a pre-simplicity proof mechanism.
- Using first Laguerre inequality alone as a global LP criterion.

### Keep, but change role

- Old PSC / exact weights: singular-wedge asymptotic certificate.
- APVC / secant APVC / joint invariant J: singular-wedge transversality tools when the scalar PSC loses sign.
- Validated finite-box computation: compact middle-region closer, not the main asymptotic theory.
- Boundary-collision compactness argument: logical bridge showing why global positive-time no-collision would imply RH.
- de Bruijn strip theorem: background geometry and compactness control.

### Literature-completed modules

- Effective large-x fixed-positive-time asymptotics: Polymath Theorem 1.5.
- Fixed-time qualitative eventual real/simple zeros: Ki–Kim–Lee.
- Strict heat smoothing of an LP function to simple real zeros: Craven–Csordas, after explicit hypothesis check.
- Effective Riemann–Siegel representation and errors: Polymath Theorem 1.3 / Corollary 6.5.

## New canonical strict architecture

For every chosen epsilon>0:

1. **Large x**: invoke Polymath Theorem 1.5 on `epsilon<=t<=1/2`; no new asymptotic proof is needed there.
2. **Compact middle**: certify the finite rectangle left below the effective threshold by validated computation or stronger analytic certificates.
3. **Singular wedge**: seek a theorem uniform as `t->0+` with `lambda=t log(x/(4pi))` bounded. This is the primary innovation target.
4. **Match/overlap** the wedge theorem to the fixed-positive-time large-x theorem and compact certificates.

On unrestricted Track U, replace `1/2` above by `0.22`, and use Craven–Csordas plus `Lambda<=0.22` to remove all `t>0.22` entirely.

## Immediate research task

Before pushing the numerical shoulder from 6.85 toward 6.83 further, pause the brute-force frontier campaign and perform a dedicated literature survey for the singular scaling

` t -> 0+, x = exp(lambda/t + O(1)), lambda=O(1) `.

Search specifically for:

- uniform saddle-point / steepest-descent expansions of `H_t` in the double-scaling regime;
- Ki–Kim–Lee asymptotics with explicit dependence on t;
- Polymath Proposition 9.1 / Theorem 1.5 constants and whether their `exp(C/t)` threshold can be sharpened in the lambda coordinate;
- Stokes transitions and two-saddle interference for the Riemann xi heat deformation;
- uniform asymptotics of the heat-weighted Riemann–Siegel sum when `t log x` is fixed;
- entire-function zero-exclusion criteria adapted to a dominant term plus conjugate saddle;
- any existing transversality/simple-zero theorem uniform in this scaling;
- rigorous asymptotic control of the exact weights `b_n^t n^{-s_*}` as `t->0` at fixed lambda.

The research question is no longer “how do we control all positive times?” but:

> Can the singular double-scaling wedge be given a uniform no-multiple-zero theorem whose constants overlap the already literature-controlled fixed-positive-time region?

That is the canonical innovation target after this audit.
