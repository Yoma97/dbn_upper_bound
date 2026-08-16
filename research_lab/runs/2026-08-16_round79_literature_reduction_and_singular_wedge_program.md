# Round 79 — Literature reduction audit and singular-wedge refocus

**Date:** 2026-08-16

**RH status:** OPEN.

## Executive correction

The proposed literature reduction contains a powerful idea, but two proof policies must be separated.

### Unrestricted published-input track

If the published unconditional theorem `Lambda <= 0.22` is admitted as a black box, then every `t>0.22` is indeed in the all-real regime. Simplicity for strictly later heat time can be obtained from standard Laguerre–Polya / strict heat-operator results, or from the local backward-splitting lemma already audited in this project. Hence no collision search is needed for `t>0.22` on this track.

### Canonical strict project track

The project constitution forbids finite-height RH verification anywhere in the proof dependency closure. Polymath Theorem 1.1 is mathematically unconditional, but its proof explicitly uses Theorem 1.2 hypothesis (i), numerical verification of RH at time zero. Therefore `Lambda<=0.22` cannot be used in the canonical strict proof graph.

Thus the sentence “we only need 0<t<=0.22” is correct on the unrestricted track, but inadmissible on the strict track.

## Existing literature reductions that ARE strict-admissible

Polymath Theorem 1.5 is the key unconditional asymptotic input. It controls the zeros for `x >= exp(C/t)` uniformly enough to show that, for every fixed positive epsilon, the large-x portion of

`epsilon <= t <= 1/2`

is already theoretically controlled. In particular, the only noncompact geometry as `t -> 0+` occurs at exponential height

`x = exp(O(1/t))`.

Theorem 1.5 refines Ki–Kim–Lee, whose fixed-t results had constants depending on t in a non-uniform and ineffective fashion. Therefore KKL should be treated as historical/structural support, while Polymath Theorem 1.5 is the operative effective theorem.

The project already proved a strict explicit collision-exclusion shoulder, now

`lambda = t log(|x|/(4 pi)) >= 6.85`,

using only the analytic effective Polymath approximation and directed arithmetic. This is stronger for our collision problem than a merely qualitative fixed-t “all but finitely many zeros” statement because it supplies an explicit uniform scaled boundary.

## Important logical distinction: real versus simple

A theorem that sufficiently large zeros are real is not automatically a theorem that they are simple. When using Polymath Theorem 1.5 for collision exclusion, the exact multiplicity statement must be read from the relevant part/proof (argument-principle uniqueness counting multiplicity), not inferred from “real” alone.

Similarly, Laguerre–Polya membership guarantees real zeros but not simplicity. Strict heat-operator simplicity requires its own hypotheses. The project will cite a precise operator theorem or use the already-audited local backward-splitting lemma rather than silently merging the two claims.

## Platt–Trudgian

Platt–Trudgian rigorously verified RH through height `3*10^12` and simplicity of those zeros. This may improve numerical inputs to a Polymath-style upper-bound criterion, but the statement “therefore the bound becomes about 0.20” is NOT adopted as a theorem until the full Theorem-1.2 barrier hypotheses are independently rerun and certified. A larger verified height only settles hypothesis (i); it does not by itself establish hypotheses (ii) and (iii) with new parameters.

Moreover this route is outside the strict project track because it deliberately uses finite-height RH verification.

## de Bruijn strip contraction

The strip-contraction theorem is valuable for locating nonreal zeros and for boundary/compactness arguments. It does not by itself prove collision exclusion or simplicity. It is therefore retained as background infrastructure, not as the new core certificate.

## Laguerre inequalities

`L_1=f'^2-ff''` is useful only when positivity can be proved independently. At a multiple real zero it vanishes, so a positive lower bound would exclude collisions. But global Laguerre positivity is closely tied to Laguerre–Polya real-rootedness and must not be assumed in the unknown region. Keep it as a possible local certificate, not a global premise.

## Zero-motion ODE

Rodgers–Tao / Csordas–Smith–Varga zero dynamics are retained only after simplicity and the relevant real-rooted regime are already established. They are not an admissible tool to prove the missing simplicity in the unknown regime.

## PF / total positivity route

The 2026 preprint exhibiting a rigorously certified negative 5x5 Toeplitz minor for the original de Bruijn–Newman kernel shows that the kernel is not PF_5. Therefore any direct strategy requiring PF_infinity, or even PF_5, for the original kernel is impossible. This route is removed from the active program. The preprint does not rule out PF_4, nor does it rule out transformed kernels or weaker variation-diminishing structures.

## New canonical research decomposition

For the strict track, do NOT use `0.22` as a cutoff. Instead use an arbitrary fixed `epsilon>0` plus strict-admissible large-x theory/certificates:

1. **Compact positive-time core:** `epsilon <= t <= 1/2` and `|x| <= X(epsilon)`. This is, in principle, a validated-computation problem once an explicit effective `X(epsilon)` is fixed.
2. **Large-x positive-time region:** remove with Polymath Theorem 1.5 and/or the project's explicit shoulder theorem.
3. **Singular wedge:** `t -> 0+`, `x -> infinity`, with `lambda=t log(x/(4 pi))=O(1)`. This is the genuine noncompact analytic frontier.

The project’s current strict theorem already removes

`lambda >= 6.85`.

Therefore the remaining singular wedge is sharpened to bounded scaled lambda below the certified shoulder.

## What can be retired or demoted

- Retire the goal “invent one collision certificate for all 0<t<=1/2”.
- Retire PF_infinity/PF_5 of the original kernel as an active route.
- Demote KKL to structural/history; use Polymath Theorem 1.5 for effective uniform work.
- Demote direct bounded-x joint-jet scans to a compact-core validation module, not the conceptual main theorem.
- Keep the exact-weight PSC / APVC / joint invariant machinery because it is precisely adapted to the singular scaling and has already produced strict explicit shoulders.
- Keep Polymath Theorem 1.3 / Corollary 6.5 as the principal analytic approximation; do not rederive Riemann–Siegel from scratch.
- Keep de Bruijn strip contraction and boundary-collision compactness as global logical infrastructure.

## Dedicated literature-survey target

Before further lowering `6.85`, search specifically for prior results in the double-scaling regime

`t -> 0+`, `log x ~ lambda/t`,

including equivalent variables in saddle-point/Riemann–Siegel analyses. Search terms must include:

- uniform small-time asymptotics of `H_t` with `t log x` fixed;
- de Bruijn–Newman heat flow in exponential-height scaling;
- uniform Riemann–Siegel expansions with moving heat parameter;
- saddle coalescence / steepest descent for `xi` heat deformation;
- Jensen polynomials / Hermite limits only where the scaling genuinely matches;
- explicit transversality or simplicity of zeros under small backward heat time;
- effective versions of Ki–Kim–Lee in joint `(t,x)` scaling;
- asymptotics of the Polymath phase/amplitude variables when `t log(x/(4pi))` is fixed.

The purpose is not bibliography accumulation. It is to determine whether the Round-64/65 exact-weight limit and the PSC/APVC singular-wedge machinery reproduce a known theorem, can import a sharper known asymptotic, or identify a genuinely new missing invariant.

## Next execution rule

Pause broad lowering of the finite-time shoulder until the singular-wedge literature survey is complete. The current strict certified constant remains `C_strict=6.85`; `6.83` is diagnostic only until a complete certificate is finished.

The primary mathematical question is now:

**Can one prove collision transversality uniformly as `t->0+` with `lambda=t log(x/(4pi))` in a fixed compact interval below 6.85, using existing uniform asymptotics plus only the minimal new phase-sensitive ingredient?**
