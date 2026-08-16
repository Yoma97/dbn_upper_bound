# Round 79 — Literature audit for the singular wedge `t -> 0+`, `lambda = t log(x/4pi) = O(1)`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Purpose:** determine what is already available in the literature before inventing further collision certificates.  
**Novelty status of project conclusions:** NOVELTY_UNVERIFIED.

---

## 1. Main conclusion

The literature search supports a substantial reduction of the research program, but it does **not** locate a published theorem that closes the singular boundary layer

\[
t\to0^+,
\qquad
x=4\pi e^{\lambda/t},
\qquad
\lambda=O(1).
\]

The evidence currently points to this as the genuinely noncompact positive-time regime not already handled by fixed-time asymptotics plus effective large-`x` theory.

The project should therefore stop trying to rebuild all positive-time theory from first principles. Existing results should be used as reduction lemmas, and new invention should be concentrated on a uniform `(t,lambda)` transversality theorem in this wedge.

---

## 2. Ki--Kim--Lee (2009): useful, but fixed-time and non-effective for our purpose

Ki, Kim and Lee, *On the de Bruijn--Newman constant*, Adv. Math. 222 (2009), prove that for every fixed positive deformation parameter, all but finitely many zeros are real and simple.

This is an important qualitative fact:

\[
\forall t>0\text{ fixed},
\qquad
\text{only finitely many zeros of }H_t\text{ can fail real simplicity.}
\]

However, this does **not** by itself furnish the uniform threshold needed as `t -> 0+`. The exceptional radius can depend badly on `t`.

D.H.J. Polymath explicitly describes Theorem 1.5 as improving and making effective the Ki--Kim--Lee asymptotic results.

**Program status:**

- use KKL as qualitative background;
- do not use it as the quantitative wedge-closing theorem;
- do not rebuild its fixed-`t` saddle-point result.

---

## 3. D.H.J. Polymath (2019): the principal positive-time source

Theorem 1.3 gives an effective Riemann--Siegel type approximation for `H_t(x+iy)` at positive time, based on the heat weights

\[
b_n^t=\exp\left(\frac t4\log^2 n\right)
\]

and the saddle-shifted exponent `s_*`.

Theorem 1.5 / Proposition 9.1 then show that for

\[
x\ge \exp(C/t)
\]

all sufficiently large zeros are real, with one-zero localization and simplicity obtained through a local winding/argument-principle argument.

The asymptotic two-saddle formula in Proposition 9.1 is

\[
H_t(x+iy)
=
(1+O(x^{-ct}))M_t(s_+)
+
(1+O(x^{-ct}))M_t(s_-).
\]

In the singular scaling

\[
x=4\pi e^{\lambda/t},
\]

one has

\[
x^{-ct}=\exp(-c\lambda+o(1)).
\]

Therefore this two-term theorem is powerful for **large lambda**, but its relative error does not automatically tend to zero when `t -> 0+` with a bounded fixed `lambda`.

This is the precise reason Theorem 1.5 does not itself close the low shoulder.

By contrast, the full Theorem-1.3 finite Dirichlet sum retains the terms needed in the fixed-`lambda` boundary layer and is the correct source for the new uniform analysis.

Polymath Remark 9.3 / 9.4 also explicitly predicts the exponential complexity scale `exp(O(1/Lambda_0))` and explains heuristically why substantially beating the `1/log T` relationship would require RH-level new information.

**Program status:**

- Theorem 1.3: LIVE PRIMARY INPUT;
- Proposition 9.1 / Theorem 1.5: reduction and far-tail theorem;
- do not rederive the Riemann--Siegel approximation from scratch.

---

## 4. Natural boundary-layer coordinate is already encoded in Polymath

At `y=0`, the real part of the saddle-shifted exponent satisfies asymptotically

\[
\Re s_*
=\frac12+\frac{\lambda}{4}+o(1)
\]

when

\[
\lambda=t\log\frac{x}{4\pi}
\]

is fixed.

Consequently, for fixed `n`, the normalized heat-weight amplitude tends to

\[
\exp\left(\frac t4\log^2 n-\Re(s_*)\log n\right)
\longrightarrow
n^{-1/2-\lambda/4}.
\]

This exactly matches the Round-64 moment limit

\[
A_0\to\zeta(1/2+\lambda/4)-1,
\qquad
A_1\to-\zeta'(1/2+\lambda/4).
\]

Thus `lambda` is not an ad hoc coordinate invented by the project: it is the intrinsic saddle coordinate of the effective Polymath approximation.

**Program consequence:** retain and deepen Rounds 64--66 rather than replacing them.

---

## 5. Cardon / Craven--Csordas: strict heat smoothing settles simplicity after entering LP

The available entire-function literature gives the following ready-made lemma.

If `g in LP` has order `<2` and `alpha>0`, then

\[
e^{-\alpha D^2}g
\]

has only simple real zeros (Craven--Csordas Theorem 3.10 as quoted in Cardon--de Gaston).

Hence, whenever `s>Lambda`, `H_s` is in LP and has order 1, and for `t>s`,

\[
H_t=e^{-(t-s)D^2}H_s
\]

has simple real zeros.

Therefore

\[
\boxed{t>\Lambda\Longrightarrow H_t\text{ has only simple real zeros}.}
\]

This should be cited rather than reproved locally in future writeups.

### Methodological split

If one admits Polymath's unconditional published theorem `Lambda<=0.22` as a black box, then all `t>0.22` are immediately finished.

Under the project's stricter policy forbidding finite-height RH verification anywhere in the proof ancestry, `Lambda<=0.22` remains excluded from the canonical proof graph because Polymath Theorem 1.1 uses finite-height RH verification in its proof.

Thus:

- unrestricted published-input track: `t>0.22` CLOSED;
- strict track: the simplicity theorem is retained, but `0.22` cannot be used as the cutoff.

---

## 6. Dobner (2021; revised arXiv version 2026): not a positive-wedge shortcut

Dobner proves Newman's conjecture by constructing for **negative** `t` an approximation

\[
\xi_t(J_t(s))
\approx
\text{gamma-like factor}\cdot
\zeta_t(s),
\]

where

\[
\zeta_t(s)=\sum_{n\ge1}e^{(t/4)\log^2n}n^{-s}
\]

is absolutely convergent for `t<0`.

The mechanism is designed precisely for the negative-time side and produces off-critical-line zeros there. It does not provide a theorem eliminating collisions for bounded positive `lambda`.

The revised 2026 version does not change this basic direction.

**Program status:** useful conceptual comparison only; do not import it as a positive-time wedge theorem.

---

## 7. Rodgers--Tao zero dynamics: post-simplicity tool, not a collision certificate

The zero ODE / repulsion machinery is valid when the tracked zeros are simple, and Polymath explicitly cites verification in the regime `t>Lambda`.

Therefore it may be used after simplicity is already secured, but not to prove simplicity in the unknown positive-time region without an independent argument.

**Program status:** SECONDARY / POST-SIMPLICITY.

---

## 8. Laguerre inequalities: diagnostic, not closure

The ordinary inequality

\[
L_1=f'^2-ff''\ge0
\]

is only a necessary condition in general; it is not sufficient for LP membership or global real-rootedness. The uploaded Csordas source gives explicit counterexamples.

The full generalized Laguerre hierarchy can characterize LP under hypotheses, but using the entire hierarchy as an assumption in the present problem risks restating the desired real-rootedness property.

**Program status:** DIAGNOSTIC ONLY; no primary hierarchy program.

---

## 9. PF / total positivity route: direct PF-infinity strategy is closed

A 2026 preprint by W. Michalowski gives an interval-certified negative `5x5` Toeplitz minor for the original de Bruijn--Newman kernel and therefore proves

\[
K\notin PF_5.
\]

Consequently any direct plan that requires the original kernel to be `PF_infinity` (or `PF_r` for every `r>=5`) is refuted.

The global `PF_4` question is reported as open, so one must not overstate the negative result as ruling out every finite-order positivity idea.

**Program status:** `PF_infinity` DIRECT ROUTE = FROZEN/REFUTED.

---

## 10. 2025 paper “The generalized Riemann zeta heat flow” is a different PDE

Castillo--Munoz--Poblete--Salinas, J. Funct. Anal. 288 (2025), study

\[
\partial_tu=\Delta u+\lambda\zeta(u)
\]

(and analogous Dirichlet-L nonlinearities).

This is a semilinear PDE whose equilibria include zeta zeros. It is **not** the linear de Bruijn--Newman deformation

\[
\partial_tH_t=-\partial_x^2H_t.
\]

It does not currently supply a theorem for the singular de Bruijn--Newman wedge.

**Program status:** NOT DIRECTLY RELEVANT.

---

## 11. Romik / Hermite and orthogonal polynomial expansions

Romik's orthogonal-polynomial expansions of `Xi` make a genuine conceptual connection with the de Bruijn--Newman flow and derive asymptotics for expansion coefficients.

However the theorems concern coefficient asymptotics / polynomial bases, not a uniform positive-time collision-exclusion theorem in

\[
t\to0^+,
\quad
\lambda=O(1).
\]

They may be useful later if a basis adapted to the heat semigroup gives a phase-sensitive finite-dimensional model, but they do not presently shorten the core wedge problem.

**Program status:** WATCHLIST, not primary.

---

## 12. Unreliable / unusable claimed shortcut located in search

A 2022 arXiv preprint titled *On the de Bruijn-Newman constant: a new approach* states the Newman conjecture incorrectly as all zeros being real for all deformation parameters, and claims all such deformations have purely imaginary/real zeros for every real parameter. This conflicts with the standard transition definition of `Lambda` and with established negative-time results.

It is not an admissible input to this project without a complete independent correction of its argument.

**Program status:** EXCLUDED.

---

## 13. What the literature has actually reduced

### Unrestricted published-input track

If `Lambda<=0.22` is admitted:

\[
t>0.22
\quad\Longrightarrow\quad
\text{simple real zeros by strict heat smoothing}.
\]

For every fixed `epsilon>0`, Polymath Theorem 1.5 gives a finite large-`x` threshold on

\[
epsilon\le t\le0.22,
\]

so the remaining region is compact in `(t,x)`.

Thus the only noncompact regime as one attempts to force the upper bound to zero is the singular wedge.

### Strict track

The same analytic conclusion applies conceptually, but one cannot use the numerical value `0.22` because of its proof ancestry. The project's certified strict shoulder theorem currently gives

\[
\lambda\ge6.85
\]

collision-free for `0<t<=1/2`, so the strict noncompact research frontier is already confined to

\[
0\le\lambda<6.85,
\qquad t\to0^+.
\]

---

## 14. The actual missing theorem

The literature audit suggests that the next theorem should **not** be another global fixed-time asymptotic.

The missing object is a uniform collision/transversality expansion in the singular coordinate.

### Target SW-1

For each compact `K subset (4,infinity)` (and eventually for lower lambda with a different mechanism), derive jointly

\[
\frac{H_t(x)}{D_t(x)}
=
P_0(t,\lambda,\theta)+R_0(t,\lambda,\theta),
\]

\[
\frac{H_t'(x)}{D_t(x)}
=
\frac1t P_1(t,\lambda,\theta)+R_1(t,\lambda,\theta),
\]

where

\[
x=4\pi e^{\lambda/t},
\]

`theta` is the fast phase, `P_0,P_1` have explicit limiting Dirichlet-series models, and the remainders are **uniform in lambda and phase**.

The theorem must preserve the joint correlation between value and derivative; scalar triangle bounds alone have structural floors.

### Target SW-2

Prove a limiting no-common-zero statement for the limiting joint model:

\[
P_0^{(0)}(\lambda,\theta)=0
\quad\Longrightarrow\quad
P_1^{(0)}(\lambda,\theta)\ne0
\]

through the desired lambda range.

Only after SW-2 is understood should a computer-assisted compact perturbation theorem be built around it.

---

## 15. Recommended program reset

### Keep active

1. Polymath Theorem 1.3 and explicit errors.
2. Rounds 64--66 exact-weight / scaled-boundary-layer analysis.
3. PSC/APVC/secant/J/joint-jet as **joint transversality tools** inside the wedge.
4. Polymath Theorem 1.5 only as far-tail / compactness reduction.
5. Cardon / Craven--Csordas for simplicity once `t>Lambda` is already known.

### Freeze as primary

1. brute-force lowering `6.85 -> 6.83 -> ...` without first deriving the uniform limiting joint model;
2. raw PF-infinity / total-positivity route;
3. generalized Laguerre hierarchy as a closure strategy;
4. zero-motion ODE before simplicity;
5. negative-time Dobner/Rodgers--Tao estimates as positive-wedge inputs;
6. unrelated nonlinear zeta heat PDEs.

### Immediate research priority

\[
\boxed{
\text{derive the full uniform }(t,\lambda,\theta)\text{ joint asymptotic from Polymath Theorem 1.3.}
}
\]

This is more valuable than another small numerical reduction of the currently certified strict constant.

---

## 16. Circularity audit

The literature reduction and proposed SW-1/SW-2 program do not use RH, `Lambda<=0`, `Lambda=0`, finite-height RH verification on the strict track, GUE, or negative-time equilibrium estimates.

The unrestricted `t>0.22` shortcut is kept explicitly separate because its numerical cutoff depends transitively on the published Polymath `Lambda<=0.22` theorem, whose proof uses finite-height RH verification.

**RH remains OPEN.**
