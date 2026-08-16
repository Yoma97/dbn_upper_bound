# Round 79 — Literature-reduction audit and program refocus

**Date:** 2026-08-16  
**RH status:** OPEN.

## Executive conclusion

The proposed literature reduction is substantially correct as a mathematical strategy, but it mixes two proof policies that must remain separate.

1. **Unrestricted published-input track U.** If the published unconditional theorem `Lambda <= 0.22` is admitted as a black box, then the region `t>0.22` is finished: choose `Lambda<s<t`; `H_s` has only real zeros, and strict forward heat evolution rules out multiple zeros. Our backward-heat/Hermite argument already proves the needed implication `t>Lambda => all zeros of H_t are simple`.

2. **Strict project track S.** The project constitution forbids finite-height RH verification anywhere in the dependency closure. Polymath Theorem 1.1 (`Lambda<=0.22`) is mathematically unconditional but its proof uses finite-height RH verification. Therefore `t>0.22 is finished` is **not admissible on Track S**. It is a valid Track-U simplification only.

This distinction is mandatory.

## Claims confirmed from the literature

### Polymath Theorem 1.5

For `0<t<=1/2`, sufficiently large absolute `C`, and `x>=exp(C/t)`, every zero `H_t(x+iy)=0` has `y=0` and lies `O(x^{-ct})` from an explicit real location `x_n`. Conversely, for sufficiently large `n` there is exactly one zero, counting multiplicity, in a small disk around `x_n`; hence that large zero is real and simple.

This is an unconditional effective refinement of Ki--Kim--Lee and is directly useful on the strict track.

### Ki--Kim--Lee (2009)

For every fixed positive heat parameter, all but finitely many zeros are real and simple. This is qualitatively strong but not by itself uniform as `t->0`; Polymath Theorem 1.5 supplies the effective scale `x>=exp(C/t)`.

### Platt--Trudgian

They rigorously verified RH up to height `3*10^12`. This can strengthen numerical-verification inputs in upper-bound criteria, but any such use is excluded from Track S by policy. A `~0.20` de Bruijn--Newman upper bound must not be promoted here without an independent derivation through the full Polymath criterion.

### PF5 obstruction

The 2026 preprint by Wojciech Michalowski gives a certified negative 5x5 Toeplitz minor for the classical de Bruijn--Newman kernel, proving it is not PF5. Therefore any route requiring the original kernel to be PF_infinity (or even PF5) is impossible. The global PF4 question remains open, so the correct conclusion is to archive **PF_infinity / total positivity of the original kernel as a direct route**, not every finite-order positivity idea.

## Corrections to the proposed reduction

### Correction 1: Theorem 1.5 does not hand us a small explicit numerical `C`

The theorem states existence of sufficiently large absolute constants `C,c`. For a formal validated-computation rectangle one must extract/instantiate constants from the proof, or use our stronger explicit shoulder certificate.

### Correction 2: the remaining singular region is a compact lambda window

Theorem 1.5 removes `x>=exp(C/t)`, i.e. `lambda=t log(x/(4pi)) >= C+o(1)`. Our explicit strict shoulder certificate is numerically sharper: Round 80 records `lambda>=6.83`. Thus the unresolved escaping wedge is explicitly `lambda<6.83`, together with the bounded-x/core region.

The singular difficulty is therefore the compact scaled window in lambda as `t->0+`, not arbitrary `x->infinity`.

### Correction 3: fixed-epsilon reduction is logically finite, not automatically computationally cheap

For every `epsilon>0`, Theorem 1.5 gives a finite large-x cutoff, so `[epsilon,0.22]` on Track U or `[epsilon,1/2]` on Track S reduces to a bounded x-region plus an asymptotic tail. But the cutoff can be exponentially large in `1/epsilon`; this is a compactness reduction, not yet a practical computation.

### Correction 4: de Bruijn strip contraction is localization, not the missing singular proof

The strip-shrinking theorem is an important global structural input. It does not eliminate the need to control the transition as `t->0`, where the relevant bounds degenerate.

### Correction 5: Laguerre inequalities are not free positivity

`L1=f'^2-ff''` is an exact identity/functional. But asserting its global nonnegativity for the relevant entire function can encode real-rootedness/Laguerre--Polya information. It must not be imported as automatic in the unknown region.

### Correction 6: zero-motion ODEs remain downstream tools

Use them only where simplicity has already been established (for example `t>Lambda`), not to prove simplicity in the unknown region. Polymath explicitly flags this restriction.

## Program decision

### Archive as primary research routes

- rebuilding the Polymath Riemann--Siegel approximation from scratch;
- PF_infinity / total positivity of the original de Bruijn--Newman kernel;
- global zero-motion ODE as a simplicity proof;
- trying to invent one monolithic certificate over all `(t,x)`;
- on Track U only: any work devoted to `t>0.22`.

### Retain as infrastructure

- Polymath Theorem 1.3 / Corollary 6.5 explicit approximation and errors;
- Theorem 1.5 / KKL for far-tail structure and compactness;
- de Bruijn strip contraction for global localization;
- local LP/heat-flow simplicity theorem or the equivalent backward-Hermite proof for already-real-rooted times;
- PSC/APVC/secant/joint-jet certificates as local tools;
- validated computation for compact rectangles;
- dependency/circularity auditing.

### New primary analytic target

Study the singular double scaling

` t -> 0+,   x -> infinity,   lambda=t log(x/(4pi)) in a fixed compact interval.`

The current strict shoulder theorem means the only escaping wedge that can still contain a positive-time multiple real zero is `lambda<6.83`. The next literature survey should therefore target **uniform asymptotics in this double scaling**, not general de Bruijn--Newman theory.

Search themes:

- uniform steepest descent / saddle-point asymptotics with `t log x` fixed;
- uniform Riemann--Siegel expansions under heat flow;
- transition asymptotics for the two conjugate saddle contributions `A+B-C`;
- uniform derivative asymptotics (`H_t,H_t'`) in the scaled variable;
- entire-function zero simplicity under small Gaussian heat perturbations;
- logarithmic-derivative and phase-velocity asymptotics in the lambda scaling;
- whether Ki--Kim--Lee or later refinements contain uniform constants in this regime;
- strong universal factors and strip contraction with quantitative small-time constants.

## Policy

Track U and Track S are both mathematically useful, but only Track S is canonical under the user's no-finite-height-RH-verification rule.

Do not silently use `Lambda<=0.22` in Track S.
