# Low-Shoulder Program V2.1 — corrected executable plan

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Canonical status:** supersedes `low_shoulder_program_v2.md` for future execution.  
**Goal:** Exclude real multiple zeros of `H_t` for `0<t<=1/2`, then use the already established boundary-collision reduction plus `Lambda>=0`.

---

## 0. Logical lock

The project may use the implication

\[
(H_t,H_t')\neq(0,0)
\quad\forall\,0<t\le1/2,\ x\in\mathbb R
\Longrightarrow
\Lambda\le0,
\]

because an assumed `Lambda>0` is attained by a finite multiple real zero at `t=Lambda`, and the known unconditional bound gives `Lambda<1/2`.

This implication is RH-strength. It is a target, never an admissible intermediate hypothesis.

Current proved global shoulder:

\[
\boxed{
\lambda=t\log\frac{|x|}{4\pi}\ge10.52
\Longrightarrow
(H_t,H_t')\neq(0,0)
}
\]

for `0<t<=1/2`.

The complete MPFR scalar certificate and 512/768-bit outputs are now stored in `research_lab/certificates/high_shoulder/`.

---

## 1. Current allocation

### Track A — exact-weight phase-slope

**PRIMARY.**

Reason: the `10.52` theorem is proved, and its own actual-weight boundary regression shows that the old global `n^-1.814` majorant is enormously weaker than the true heat weights.

### Track B — below-floor new certificate

**SECONDARY until Track A reaches its asymptotic sign floor.**

### Track C — prime-side all-orders / sparse-exception amplification

**PARALLEL LONG-HORIZON TRACK.**

Rounds 48--61 remain useful, but they currently demand a new all-orders connected prime-side theorem beyond pair data, whereas Track A already has a proved analytic mechanism with measurable slack.

---

## 2. What the 10.52 audit actually says

Uniform proof at the endpoint:

\[
A_0\le0.861634072184451,
\qquad
A_1\le1.444773803962031,
\]

\[
S_0=1-A_0\ge0.138365927815549,
\]

\[
E_0\le2.708962805629476\times10^{-8},
\qquad
E_1\le4.681440365960625\times10^{-7},
\]

with PSC margin

\[
\ge0.0051784223492658803.
\]

The same boundary with the true finite heat weights gives

\[
A_0\le0.20955042280644084,
\qquad
A_1\le0.22794011633558037,
\]

and phase margin

\[
\ge8.0875893307159448.
\]

Therefore the first quantitative loss is the global edge-power replacement, not `E0`, `E1`, `phi_x`, or interval dependency.

The actual-weight boundary run is a diagnostic, not by itself a global theorem below `10.52`.

---

## 3. Correct scale

Set

\[
L=\log\frac{x}{4\pi},
\qquad
\lambda=tL,
\qquad
x=4\pi e^{\lambda/t}.
\]

The raw PSC margin

\[
\mathcal T
=2\left[
\Phi\sqrt{S_0^2-(E_0/2)^2}-dA_1
\right]-E_1
\]

is naturally of order `1/t` at fixed `lambda`.

The correct scaled observable is

\[
\boxed{\widetilde{\mathcal T}=t\mathcal T.}
\]

Do not search for a finite limit of unscaled `T`.

---

## 4. LS-A1 is no longer open

**Status: INTERNALLY_PROVED — Round 64.**

For every compact

\[
K=[\lambda_0,\lambda_1]\subset(4,\infty),
\]

put

\[
p(\lambda)=\frac12+\frac\lambda4,
\qquad
q=1+\frac{\lambda_0-4}{16}>1.
\]

For the fixed Cauchy-disk base cutoff

\[
N_-(t,\lambda;\rho)
=
\left\lfloor
\sqrt{e^{\lambda/t}-\frac\rho{4\pi}+\frac t{16}}
\right\rfloor,
\]

Round 64 proves explicit remainders:

\[
\left|A_0-(\zeta(p)-1)\right|
\le
\frac t4Z_2(q)
+\frac{t}{2x^2}Z_1(q)
+\frac{N_-^{1-p}}{p-1},
\]

\[
\left|A_1+\zeta'(p)\right|
\le
\frac t4Z_3(q)
+\frac{t}{2x^2}Z_2(q)
+N_-^{1-p}
\left(
\frac{\log N_-}{p-1}+
\frac1{(p-1)^2}
\right),
\]

under an explicit small-`t` domination condition.

Thus

\[
A_0\to\zeta(p)-1,
\qquad
A_1\to-\zeta'(p)
\]

uniformly on compact subsets of `(4,infinity)`.

**Correction to V2:** the three-region split is unnecessary for LS-A1. A single summable power majorant plus `e^r-1<=r e^r` gives `O(t)` plus exponentially small cutoff tails.

---

## 5. LS-A2 is analytically closed, pending independent reconstruction

**Status: INTERNALLY_PROVED — Round 65.**

On every compact

\[
K\subset(\lambda_*,10.52],
\]

Round 65 proves

\[
t\Phi\to\frac\lambda4,
\qquad
d\to\frac12,
\]

and, from unconditional Polymath errors plus the fixed-cutoff jump bridge,

\[
E_0\to0,
\qquad
tE_1\to0
\]

uniformly.

Therefore

\[
\boxed{
 t\mathcal T(t,\lambda)
\longrightarrow
\mathcal T_0(\lambda)
=
\frac\lambda2
\left[
2-\zeta\left(\frac12+\frac\lambda4\right)
\right]
}
\]

uniformly on `K`.

The symmetric-normalization ratio was separately attacked in `round65_normalization_ratio_audit.md`; the comparison is made after Schwarz conjugation along a short horizontal segment, not directly between the distant functional-equation partners.

No claim receives `REFEREE_VERIFIED` status until the project protocol performs independent proof reconstruction.

---

## 6. Exact meaning of lambda_*

Let `p_*` be the unique real solution of

\[
\zeta(p_*)=2
\]

and define

\[
\lambda_*=4(p_*-1/2)=4.914588956\ldots.
\]

The correct statement is:

\[
\boxed{
\lambda_*\text{ is the asymptotic sign floor of the unchanged }n=1
\text{ triangle-envelope component of PSC in the fixed-lambda }t\to0^+\text{ regime}.}
\]

Do **not** call it:

- a collision threshold;
- a universal PSC floor;
- a finite-`t` obstruction;
- evidence that collisions exist below it.

For `lambda<lambda_*`, the limiting scalar lower bound

\[
S_0=1-A_0\to2-\zeta(p)
\]

is negative, so that particular triangle bound has no content. This says the certificate must change; it says nothing about the true joint jet.

---

## 7. LS-A3 — corrected scope

For each `epsilon>0`, define the compact asymptotic shoulder

\[
K_\epsilon=[\lambda_*+\epsilon,10.52].
\]

Round 65 gives an explicit-computable small-time criterion. The next task is to turn it into a practical certified decimal `t_epsilon>0` satisfying

\[
0<t\le t_\epsilon,
\qquad
\lambda\in K_\epsilon
\Longrightarrow
(H_t,H_t')\neq(0,0).
\]

The separate high-shoulder theorem supplies all `lambda>=10.52`.

**Correction to V2:** LS-A3 is not to be stated as a consequence of compact convergence uniformly on an unbounded interval `lambda>=lambda_*+epsilon`. The proof cover is compact up to `10.52` plus the independent high-shoulder theorem.

---

## 8. Immediate numerical-analytic task LS-A3N

Choose a descending sequence, for example

\[
\epsilon=1,\ 1/2,\ 1/4,\ 1/8,\ldots
\]

and for each value:

1. evaluate the explicit Round-64 moment remainders by directed rounding;
2. evaluate the Round-65 Polymath error envelope;
3. solve rigorously for a usable `t_epsilon`;
4. rerun at 768 bits;
5. record the dominant loss channel.

Stop decreasing `epsilon` when the resulting compact bridge becomes computationally unreasonable or when the triangle-floor loss dominates. Do not compensate for `S0` sign loss with subdivision.

---

## 9. LS-A4 — compact bridge

For each certified pair `(epsilon,t_epsilon)`, cover

\[
t\in[t_\epsilon,1/2],
\qquad
\lambda\in[\lambda_*+\epsilon,10.52]
\]

with directed-rounding boxes.

Every accepted box must record:

- exact rational/decimal endpoints in `(t,lambda)`;
- induced `x` interval and `L` interval;
- `Nbase,Ntop` and proof of the cutoff range;
- exact-weight `A0,A1`;
- `S0,Phi,d,E0,E1`;
- raw and scaled margins;
- dominant loss channel;
- 512-bit result and independent 768-bit rerun;
- exact partition audit.

Ordinary floating point may guide sampling only; it is not a proof edge.

---

## 10. Failure taxonomy

Use exactly one primary label per failed analytic region/box:

- `I_PHENOMENON`: validated evidence that the true joint jet itself is small;
- `II_INTERVAL`: enclosure inflation dominates;
- `III_REMAINDER`: Polymath/Cauchy remainder dominates;
- `IV_PHASE_AMPLITUDE`: phase/amplitude envelope dominates;
- `V_CUTOFF`: cutoff bridge dominates;
- `VI_TRIANGLE_FLOOR`: unchanged `S0=1-A0` lower bound has lost sign;
- `VII_UNKNOWN`: not yet diagnosed.

`VI_TRIANGLE_FLOOR` is analytic, not numerical; never respond by brute-force subdivision.

---

## 11. Below-floor Track B

Start as the main collision-side invention track only after the middle shoulder is practically compressed.

Priority order:

### B1. Exact-head / convex-tail joint jet

Keep the first `K` terms with their true phases and amplitudes, enclose only the tail, and certify the vector `(p,p_x)` jointly. This may beat `S0=1-A0` because early terms cease to be treated as adversarial mass.

### B2. Collision-conditioned phase velocity

Exploit the condition `p≈0` itself to force `|p_x|` large. Any arbitrary-phase analogue must first be falsified, because positive trigonometric sums can have stationary zeros.

### B3. One new Riemann-specific heat/harmonic identity

Accept only a mechanism not equivalent to ordinary `L_1` positivity, global winding, a hidden gap bound, or full Laguerre--Polya membership.

Frozen as primary mechanisms unless materially changed:

- generic log-concavity / MLR alone;
- ordinary Laguerre positivity;
- global winding/zero-count defect;
- entropy/Vandermonde without an independent one-sided budget;
- raw theta-mode positivity;
- finite theta blocks;
- finite-moment large-deviation amplification.

---

## 12. Track C — prime-side all-orders

Retain Rounds 48--61 as a logically separate backstop.

Current frontier:

\[
\text{off-line orbit}
\to
\text{amplified spectral defect}
\to
\text{connected prime statistic}.
\]

Pair information is insufficient at fourth cumulant; a viable continuation must create an all-orders connected factorization/operator without assuming the Hardy--Littlewood hierarchy or another RH-strength statement.

Promote Track C only after it passes a finite fourth-order falsification gate.

---

## 13. Bounded spatial core

`lambda` is not a useful positive coordinate for `|x|<4pi` and is negative there.

Treat the bounded spatial core separately after choosing a genuinely compact `(t,x)` reduction. Direct validated computation is legitimate only after that analytic compactness reduction; finite RH verification is not a global substitute.

---

## 14. Current proof cover

### CLOSED H

\[
\lambda\ge10.52.
\]

### ANALYTICALLY REDUCED M1

For every fixed `epsilon>0`, sufficiently small `t` on

\[
\lambda_*+\epsilon\le\lambda\le10.52
\]

is collision-free by Rounds 64--65. The practical directed-rounding `t_epsilon` remains to be certified.

### NEXT M2

\[
t_\epsilon\le t\le1/2,
\qquad
\lambda_*+\epsilon\le\lambda<10.52.
\]

Requires the compact certificate LS-A4.

### OPEN L

\[
0\le\lambda<\lambda_*+\epsilon.
\]

Requires a changed certificate.

### OPEN B

bounded spatial core.

No union is yet complete; RH remains OPEN.

---

## 15. Promotion discipline

Maintain separately:

\[
C_{\rm proved},
\quad C_{\rm certified\ numerical},
\quad C_{\rm asymptotic},
\quad C_{\rm heuristic}.
\]

At present

\[
\boxed{C_{\rm proved}=10.52.}
\]

Rounds 64--65 are analytic progress but do not yet replace `C_proved` by `lambda_*` or any number near it. A new global constant `C<10.52` is promoted only after the small-time theorem and its complementary compact bridge cover **all** `0<t<=1/2` for `lambda>=C`.

Truth status also remains distinct from novelty status. `INTERNALLY_PROVED` is not `REFEREE_VERIFIED`.

---

## 16. Immediate execution order

1. **DONE:** import the 10.52 reproducibility bundle.
2. **DONE / internally proved:** Round 64 exact-weight moment collapse.
3. **DONE / internally proved:** Round 65 scaled PSC limit and qualitative compact small-time exclusion.
4. **NEXT:** independent reconstruction/audit of Rounds 64--65.
5. **NEXT:** certify a practical `t_epsilon` for one nontrivial epsilon, first at 512 bits then 768 bits.
6. **NEXT:** build the compact `(t,lambda)` bridge to `t=1/2`.
7. Only then lower epsilon and repeat.
8. At the triangle floor, switch certificate rather than spending indefinitely on interval refinement.

---

## 17. Success condition

The project closes the chosen de Bruijn--Newman route only after proving

\[
(H_t(x),H_t'(x))\neq(0,0)
\qquad
\forall\,0<t\le1/2,\ x\in\mathbb R.
\]

Then the finite-threshold collision reduction yields `Lambda<=0`; Rodgers--Tao yields `Lambda>=0`; hence `Lambda=0` and RH.

Until every region above is closed:

\[
\boxed{\mathrm{RH\ OPEN}.}
\]
