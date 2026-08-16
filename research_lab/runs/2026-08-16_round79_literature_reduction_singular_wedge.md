# Round 79 — Literature reduction and singular-wedge refocus

**Date:** 2026-08-16

## Executive correction

The proposed literature shortcut is mathematically powerful, but it must be split into two policies.

### Unrestricted published-input track U
Using the published unconditional theorem of D.H.J. Polymath, `Lambda <= 0.22`, plus strict heat-flow simplicity for Laguerre–Polya inputs, every time `t>0.22` is finished for the collision-exclusion problem.

Indeed, for `t>0.22` choose `s` with `Lambda < s < t`. Then all zeros of `H_s` are real, and `H_s` is an entire function of order one, hence is in the Laguerre–Polya class. Since

`H_t = exp(-(t-s) D^2) H_s`,

Craven–Csordas Theorem 3.10 applies: if `alpha>0` and `g in LP` has order less than two, then `exp(-alpha D^2)g` has only simple real zeros. Thus `H_t` has only simple real zeros.

So on Track U the global collision problem reduces immediately to `0<t<=0.22`.

### Strict no-finite-height-RH-verification track S
This shortcut is not admissible under the project's current strict constitution, because the proof ancestry of Polymath Theorem 1.1 uses finite-height numerical verification of RH. Round 77 records this transitive dependency.

Therefore `t>0.22` is **literature-finished on Track U**, but cannot be deleted from the logical proof graph of Track S unless the constitution is changed.

## Large-x literature reduction

D.H.J. Polymath Theorem 1.5 gives uniform effective control for `0<t<=1/2` once `x >= exp(C/t)` for an absolute constant `C`. The theorem refines Ki–Kim–Lee, whose corresponding fixed-t results had t-dependent ineffective constants and `o(1)` errors.

For any fixed `epsilon>0`, on `epsilon<=t<=0.22` the large-x threshold becomes uniformly finite:

`exp(C/t) <= exp(C/epsilon)`.

Thus, on Track U, after invoking Theorem 1.5 the remaining region at each fixed epsilon is a compact rectangle in `(t,x)`, suitable in principle for validated computation.

This means that the genuinely noncompact analytic obstruction is the singular limit

`t -> 0+`, `x -> infinity`, with `lambda = t log(x/(4 pi)) = O(1)`.

This is exactly the scaling already isolated by the shoulder program. The previous high-shoulder/PSC/APVC work is therefore not wasted; it is the beginning of the correct singular-wedge analysis.

## Important correction about Ki–Kim–Lee

Do not replace Polymath Theorem 1.5 by a vague statement that KKL alone closes the tail uniformly. Polymath explicitly says Theorem 1.5 refines KKL: the earlier constants depend on fixed `t` in a non-uniform and ineffective way. KKL is conceptual support; Polymath 1.5 is the effective uniform input needed for a certified program.

## Important correction about `Lambda <= 0.20`

Platt–Trudgian rigorously verified RH through height `3*10^12` and simplicity there. Polymath Section 10 explains how larger finite-height verification can improve its upper-bound criterion and gives conditional numerical improvements. However, the number `0.20` must not be promoted here until the exact Theorem-1.2 parameter triple `(t0,X,y0)` and hypotheses (ii),(iii) are independently revalidated against the `3*10^12` input. It is therefore a candidate auxiliary Track-U improvement, not a current theorem of this project.

## Laguerre inequalities

The first Laguerre inequality

`L1=f'^2-f f'' >=0`

is a necessary consequence of LP membership but by itself is not sufficient for LP. It may be used as a local diagnostic/certificate after suitable hypotheses, but it must not be treated as an independent shortcut to RH. Generalized Laguerre inequalities characterize LP only with the appropriate full family/hypotheses.

## Zero ODE

Rodgers–Tao/Polymath zero-motion formulas are retained only where simplicity is already established. Polymath explicitly notes verification of the interaction ODE in the regime `t>Lambda`; it is not an admissible device for proving simplicity in the unknown regime.

## PF route

The 2026 preprint by Wojciech Michalowski gives a certified negative `5 x 5` Toeplitz minor for the classical de Bruijn–Newman kernel, proving that kernel is not `PF_5`. This rules out `PF_infinity` and any route requiring PF order at least five for the original kernel. It does **not** prove that every conceivable total-positivity-inspired deformation or lower-order property is useless; in particular the paper leaves global `PF_4` open. Mark the original-kernel `PF_infinity` route CLOSED, not the entire subject of positivity.

## Program refocus

Primary research target:

`SINGULAR WEDGE: t -> 0+, x -> infinity, lambda=t log(x/(4 pi))=O(1)`.

Existing strict shoulder theorem `lambda>=6.85` remains a genuine theorem and should be retained as a certified outer boundary of this wedge. PSC/APVC/secant tools should be retained, but no longer treated as a program to cover every positive time indiscriminately.

New work order:

1. Complete a dedicated literature survey for the singular scaling `t->0`, `x=exp(O(1/t))`.
2. Extract every published uniform asymptotic in variables `(t,lambda)` from Polymath Theorem 1.3, Proposition 9.1, Theorem 1.5, KKL, de Bruijn/Newman, and related saddle-point/Riemann–Siegel literature.
3. Build a theorem map separating: exact published theorem, easy corollary, project-certified theorem, heuristic.
4. On Track U, mark `t>0.22` finished and fixed-epsilon large-x tails literature-finished; leave compact rectangles to validated computation only if needed.
5. On Track S, preserve the no-finite-height-verification proof graph; do not import `Lambda<=0.22`.
6. Concentrate invention on a uniform singular-wedge collision/transversality mechanism in bounded lambda.
7. Keep the joint invariant `J` / joint-jet as the next structural certificate only after scalar PSC/APVC reaches a genuine pointwise floor.

## Status

RH remains OPEN. No claim here proves RH.
