# Singular-wedge literature survey V1

Target scaling:

` t -> 0+,  x = 4 pi exp(lambda/t),  lambda = O(1). `

## Questions the survey must answer

1. What is the sharpest published uniform asymptotic for `H_t(x+iy)` when `t->0` and `lambda=t log(x/(4pi))` stays in a compact interval?
2. Which Polymath Theorem-1.3 error terms have nontrivial scaled limits in `(t,lambda)` and which are exponentially negligible?
3. Can Proposition 9.1 / Theorem 1.5 be rewritten with an explicit lambda threshold rather than an unspecified `x>=exp(C/t)`?
4. What exactly do Ki–Kim–Lee prove for fixed positive t: reality, simplicity, spacing, counting, and with what effectiveness/uniformity?
5. Which de Bruijn strip-contraction estimates survive uniformly in the singular scaling, and do they add anything beyond reality control?
6. Are there published saddle-point or steepest-descent expansions of the heat-deformed xi function in this double scaling that predate or sharpen Polymath?
7. Are there uniform asymptotics for derivatives `H_t'`, `H_t''` sufficient for collision transversality, rather than merely for `H_t`?
8. Is there a published phase-amplitude or two-saddle formulation whose correlation information dominates scalar triangle bounds?
9. Which Laguerre/Turan inequalities yield genuinely new information for `H_t` in this scaling without assuming LP?
10. Which zero-motion estimates are unconditional before simplicity and which are only valid in `t>Lambda`?
11. Does any published result rule out multiple real zeros in a subrange of bounded lambda uniformly as `t->0`?
12. What is the strongest known obstruction to total positivity/PF approaches for the original kernel after the certified `not PF_5` result?

## Already established from current sources

- Polymath Theorem 1.3 supplies an explicit effective Riemann–Siegel approximation with positive computable errors.
- Polymath Theorem 1.5 supplies effective large-x control for `x>=exp(C/t)` and explicitly refines KKL's non-uniform ineffective fixed-t asymptotics.
- Polymath remarks that the numerical complexity of pushing an upper bound toward zero is expected to be `exp(O(1/Lambda_0))` and heuristically difficult to improve without RH-level progress.
- Craven–Csordas Theorem 3.10 gives strict heat-flow simplicity: `g in LP`, order `<2`, `alpha>0` implies `exp(-alpha D^2)g` has only simple real zeros.
- Therefore, on the unrestricted published-input track, `Lambda<=0.22` plus strict heat simplicity closes all `t>0.22`.
- The strict project track cannot use that shortcut because `Lambda<=0.22` has finite-height RH verification in its proof ancestry.
- The original de Bruijn–Newman kernel is not `PF_5` by a 2026 certified-computation preprint; hence original-kernel `PF_infinity` is impossible.

## Search priority

Priority A: Polymath Section 9 and all cited predecessors, especially KKL 2009 and the papers behind Proposition 9.1.

Priority B: Craven–Csordas/Cardon–de Gaston strict heat-flow simplicity and LP preservation, to make the `t>Lambda` closure citation-complete.

Priority C: explicit saddle-point/Riemann–Siegel derivative asymptotics in the double scaling.

Priority D: modern work after 2019 on de Bruijn–Newman effective asymptotics, interval methods, and total positivity obstructions.

## Rule

Do not invent a new global certificate until this survey establishes that no published theorem already supplies the needed bounded-lambda singular-wedge statement.
