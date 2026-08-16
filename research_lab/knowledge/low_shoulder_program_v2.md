# Low-Shoulder Program V2 — collision exclusion toward `Lambda <= 0`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Purpose:** Replace the broad low-shoulder checklist by a proof-oriented program with explicit promotion gates, structural stop conditions, and a clean split between the currently effective phase-slope mechanism and the genuinely new mathematics needed below its natural floor.

---

## 0. Logical target and dependency lock

The final reduction is:

\[
\boxed{
(H_t(x),H_t'(x))\ne(0,0)
\ \forall\,0<t\le1/2,\ x\in\mathbb R
\Longrightarrow \Lambda\le0.
}
\]

Together with Rodgers--Tao `Lambda>=0`, this gives `Lambda=0` and RH.

This reduction is safe, but the universal no-collision statement is therefore RH-strength and may not be assumed in any intermediate lemma.

The unconditional high-shoulder theorem already integrated into the lab is

\[
\boxed{
\lambda:=t\log\frac{|x|}{4\pi}\ge10.52
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0)
}
\]

for `0<t<=1/2`.

Thus the remaining unbounded region is `lambda<10.52`, together with a separate bounded-`x` sector where `lambda` is not a useful positive scale.

---

## 1. Main adjudication: what to invest in now

### Track A — exact-weight phase-slope compression

**PRIMARY / highest near-term value.**

Reason: the theorem `lambda>=10.52` is already certified, and its own boundary regression shows an enormous gap between the global power-majorant proof and the true heat weights.

At the worst high-shoulder endpoint, the global proof uses

\[
a_n\le n^{-1.814},
\]

which gives

\[
A_0\le0.861634072184451,
\qquad
A_1\le1.444773803962031,
\qquad
S_0\ge0.138365927815549.
\]

The full actual-weight regression at the same boundary instead certifies

\[
A_0\le0.20955042280644084,
\quad
A_1\le0.22794011633558037,
\quad
S_0\ge0.79044957719355913,
\]

with phase margin `>=8.0875893307159448`, versus only `0.005178422349...` in the uniform majorant proof.

This identifies the first obstruction quantitatively: **the dominant present loss is the worst-edge power replacement of the quadratic heat weights.**

### Track B — below-floor mechanism invention

**SECONDARY NOW / becomes PRIMARY after Track A reaches its structural floor.**

The unchanged triangle-envelope PSC cannot be expected to cover all `lambda>0`. Its small-`t` limit has a sharp tail-mass transition described below. Once Track A reaches this floor, further effort must change the certificate rather than sharpen intervals.

### Track C — sparse-exception / prime-side all-orders program

**LONG-HORIZON PARALLEL TRACK.**

Rounds 48--61 remain valid and important. In particular, extremal zero-side isolation is solved and the remaining difficulty is prime-side connected/variance control. But this route currently requires genuinely new arithmetic structure and has a much larger invention risk than exploiting the certified phase-slope slack.

It should not be deleted; it is the main backstop if the low-low shoulder resists every collision-side finite mechanism.

---

## 2. Loss ledger for the proved threshold `10.52`

| Quantity | Current uniform proof | Actual-weight boundary diagnostic | Priority |
|---|---:|---:|---|
| `A0` | `<=0.861634072184451` | `<=0.20955042280644084` | **dominant loss** |
| `S0=1-A0` | `>=0.138365927815549` | `>=0.79044957719355913` | **dominant consequence** |
| `A1` | `<=1.444773803962031` | `<=0.22794011633558037` | **dominant loss** |
| `|phi_x|` | `>5.25` | `>=5.2600000000084099` | already sharp |
| `d` | `<0.501` | approximately `1/2` | already sharp |
| `E0` | `<=2.7089628056e-8` | `<=6.1712779628e-9` | small, not leading |
| `E1` | `<=4.6814403660e-7` | `<=1.0503801241e-7` | small, not leading |
| PSC margin | `>=0.005178422349...` | `>=8.0875893307...` | exposes majorant slack |

The diagnostic column is not itself a uniform theorem below `10.52`; it is evidence locating the loss.

**Immediate decision:** do not spend the next round on affine arithmetic, finer Cauchy disks, or tiny improvements to `E0/E1`. First remove the `n^{-p}` edge majorant from `A0,A1`.

---

## 3. Correct singular scaling

Put

\[
L=\log\frac{x}{4\pi},
\qquad
\lambda=tL,
\qquad
x=4\pi e^{\lambda/t}.
\]

For the real-axis phase sum,

\[
a_n(t,\lambda)
=\exp\left(\frac t4(\log n)^2-\sigma(t,\lambda)\log n\right),
\]

and the exact formula for `sigma` gives

\[
\sigma(t,\lambda)
=\frac12+\frac\lambda4+o(1)
\qquad(t\to0^+)
\]

uniformly on compact positive `lambda` intervals.

The cutoff satisfies

\[
\log N=\frac{L}{2}+o(1/t)
=\frac\lambda{2t}+o(1/t).
\]

Hence, for fixed `n`,

\[
\boxed{
a_n(t,\lambda)\to n^{-p(\lambda)},
\qquad
p(\lambda):=\frac12+\frac\lambda4.}
\]

The full logarithmic exponent in the scaled variable `u=t log n` is

\[
\frac1{4t}\left(u^2-(\lambda+2)u\right)+o(1/t),
\qquad
0\le u\le\lambda/2+o(1),
\]

which is strictly decreasing in `u` throughout the cutoff range. For the counting-measure integral the endpoint exponent is

\[
\frac{\lambda(4-\lambda)}{16t}.
\]

Therefore `lambda>4` is the natural domain in which the moving-cutoff tail can be made exponentially small and a uniform fixed-`n` zeta limit is plausible and should be proved explicitly.

---

## 4. Primary theorem target LS-A1: exact-weight moment collapse

### Frozen target statement

For every compact interval

\[
K=[\lambda_0,\lambda_1]\subset(4,\infty),
\]

prove explicit functions `R0(t,K), R1(t,K)->0` as `t->0+` such that, uniformly for `lambda in K`,

\[
\boxed{
A_0(t,\lambda)
=\zeta\!\left(\frac12+\frac\lambda4\right)-1
+O_{\le}(R_0(t,K)),
}
\]

and

\[
\boxed{
A_1(t,\lambda)
=-\zeta'\!\left(\frac12+\frac\lambda4\right)
+O_{\le}(R_1(t,K)).
}
\]

The proof must use the true quadratic heat weight and the moving cutoff. A suggested decomposition is:

1. `log n <= eta(t)/t`: dominated convergence / Taylor control;
2. intermediate range: monotonicity plus integral comparison;
3. near-cutoff range: Laplace endpoint bound using the negative exponent `lambda(4-lambda)/(16t)`.

Euler--Maclaurin is optional, not mandatory, unless it materially improves the explicit remainder.

**Promotion gate:** no numerical plot counts. The theorem requires a uniform analytic remainder with explicit constants.

---

## 5. Primary theorem target LS-A2: renormalized PSC limit

The raw transversality margin

\[
\mathcal T
=2\left[
\Phi_0\sqrt{S_0^2-(E_0/2)^2}-dA_1
\right]-E_1
\]

does **not** converge to a finite function at fixed `lambda`: `Phi0` grows like `1/t`.

The correct scaled observable is

\[
\boxed{\widetilde{\mathcal T}(t,\lambda):=t\mathcal T(t,\lambda).}
\]

From the exact phase formula,

\[
t\Phi_0\to\frac\lambda4,
\qquad
d\to\frac12.
\]

Track A must also prove from the effective Polymath errors that

\[
tE_1\to0,
\qquad E_0\to0
\]

uniformly on every compact `K subset (4,infinity)`.

Combining these with LS-A1 gives the candidate limiting identity

\[
\boxed{
\widetilde{\mathcal T}(t,\lambda)
\longrightarrow
\mathcal T_0(\lambda)
:=\frac\lambda2
\left[
2-\zeta\!\left(\frac12+\frac\lambda4\right)
\right].
}
\tag{LS-limit}
\]

This must be independently reconstructed before promotion to PROVED.

---

## 6. Structural floor of the unchanged PSC certificate

Let `p0` be the unique real root

\[
\zeta(p_0)=2,
\]

and define

\[
\boxed{
\lambda_*:=4\left(p_0-\frac12\right)
=4.914588956\ldots.
}
\]

Then the candidate limit satisfies

\[
\mathcal T_0(\lambda)>0
\iff \lambda>\lambda_*.
\]

Thus `lambda_*` should be treated as:

\[
\boxed{
\text{structural floor of the current triangle-envelope PSC architecture},
}
\]

not as a proved zero-free/collision-free threshold and not as evidence that a collision exists below it.

In particular, if `lambda<lambda_*`, then asymptotically

\[
S_0=1-A_0\to2-\zeta(p(\lambda))<0,
\]

so the basic lower bound `|S|>=S0` becomes useless. No amount of interval refinement can repair that exact logical failure.

---

## 7. Corollary target LS-A3: small-time exclusion above the floor

After LS-A1 and LS-A2, prove:

> For every `epsilon>0`, there exists an explicit `t_epsilon>0` such that
> \[
> 0<t\le t_\epsilon,
> \qquad
> \lambda\ge\lambda_*+\epsilon
> \]
> implies PSC and therefore no multiple real zero.

This is the main analytic milestone. It turns the unbounded `x`-problem above `lambda_*+epsilon` into a compact finite certification problem.

The theorem must give an explicit computable `t_epsilon`, not merely existence by an unspecified `o(1)`.

---

## 8. Compact certification LS-A4

Once `t_epsilon` is explicit, rigorously cover

\[
t\in[t_\epsilon,1/2],
\qquad
\lambda\in[\lambda_*+\epsilon,10.52]
\]

using directed-rounding interval arithmetic.

### Required evaluator outputs

For every box record

- `t`, `lambda`, `L`, and the induced `x` interval;
- cutoff range `N0,Ntop`;
- exact-weight `A0,A1`;
- comparison majorants and their slack ratios;
- `S0`, `Phi0`, `d`, `E0`, `E1`;
- `T` and `t*T`;
- minimum PSC margin;
- dominant error/loss channel;
- precision and partition depth.

### Arithmetic protocol

- outward/directed rounding;
- at least 512 bits;
- independent rerun at 768 bits or higher;
- explicit tails;
- partition audit;
- no ordinary floating point in a proof edge.

Taylor models, centered forms, affine arithmetic and local phase recentering are **conditional tools**: deploy them only if the loss ledger shows interval dependency is actually dominant.

---

## 9. Proof cover after Track A

The intended cover is:

### H — proved high shoulder

\[
\lambda\ge10.52.
\]

Already closed.

### M1 — asymptotic middle shoulder

\[
0<t\le t_\epsilon,
\qquad
\lambda\ge\lambda_*+\epsilon.
\]

Target LS-A3.

### M2 — compact middle shoulder

\[
t_\epsilon\le t\le1/2,
\qquad
\lambda_*+\epsilon\le\lambda<10.52.
\]

Target LS-A4.

### L — genuine low-low shoulder

\[
0\le\lambda<\lambda_*+\epsilon.
\]

Requires a different mechanism. Do not continue the unchanged `S0=1-A0` triangle certificate here.

### B — bounded spatial core

The variable `lambda` is not useful when `|x|<4pi` (and can be negative). The bounded-`x` core must be covered separately by direct analytic/validated methods after a compactness reduction. Finite verification here is legitimate because the region is genuinely compact; finite RH verification is not used as a global substitute.

The final proof must explicitly audit all overlaps and show no uncovered boundary remains.

---

## 10. Below-floor invention track LS-B

Only start this as the main track after LS-A1/LS-A2 have fixed the PSC floor rigorously.

### B1. Exact-head / convex-tail joint-jet certificate

Instead of bounding every non-`n=1` term adversarially, split

\[
S=S_{\le K}+R_K,
\qquad
S_x=(S_x)_{\le K}+R_{K,x}.
\]

Certify the two-dimensional joint vector

\[
\left(
2\Re(e^{i\phi}S_{\le K}),
\ 2\Re\bigl(e^{i\phi}(i\phi_xS_{\le K}+(S_x)_{\le K})\bigr)
\right)
\]

against a rigorous convex enclosure for the tail.

This can beat the scalar `S0` floor on compact/moderate-time boxes because the first terms are used constructively rather than thrown into a total-mass adversary.

**Warning:** at `t->0` the phases vary extremely rapidly with `x`; a finite-head numerical certificate is not a global asymptotic mechanism unless one proves a uniform phase theorem.

### B2. Collision-conditioned phase-velocity theorem

Seek a theorem that uses the condition `p≈0` itself to lower-bound `|p'|`, rather than first lower-bounding `|S|` by `1-A0`.

Any generic arbitrary-phase theorem must be falsified first: positive-coefficient trigonometric sums can have stationary zeros. A surviving theorem must exploit special logarithmic phases, the exact heat weights, or a Riemann-specific relation.

### B3. Previously investigated mechanisms — restrictions

- `H,H',H''` Wronskian proposals must be checked against the previously identified Laguerre barrier; do not relabel `L1`.
- global winding is secondary because it reduces to real-zero-count spectral flow.
- entropy/Vandermonde is retained diagnostically but lacks an independent finite budget.
- raw theta decompositions and finite theta blocks are frozen by Rounds 30--31.
- Gaussian-Hermite/Rayleigh remains a valid conditional bridge, but current subconvexity gives a gate near `4.95238`, slightly *above* `lambda_*`; with present arithmetic input it does not solve the below-floor region.

---

## 11. Prime-side Track C — retained, reprioritized

Rounds 48--61 are not discarded. They identified a legitimate longer-horizon mechanism for sparse off-line zeros:

- extremal Laplace--Cesaro zero-side isolation is available;
- scalar long-range pair correlation is blocked by prime-side error and positivity/bandwidth tradeoffs;
- sparse-complete Poisson-scale variance is RH-strength if simply postulated;
- pair data fail to generate fourth cumulants;
- the highest invention target is a finite prime-side all-orders factorization/operator that controls connected correlations without assuming the full Hardy--Littlewood hierarchy.

### Current role

Track C should run in parallel at lower allocation while Track A exploits the proven `10.52` theorem. It becomes a primary candidate only if:

1. Track A reaches `lambda_*` and LS-B produces no finite Riemann-specific mechanism; or
2. Track C produces an independently useful all-orders theorem passing its fourth-order falsification gate.

---

## 12. Failure taxonomy

Every failed box or analytic estimate receives exactly one primary label:

- `I_PHENOMENON`: evidence the true joint jet is approaching collision;
- `II_INTERVAL`: true margin strong, enclosure too wide;
- `III_REMAINDER`: `E0/E1` dominate;
- `IV_PHASE_AMPLITUDE`: `Phi0,d,A0,A1` architecture dominates;
- `V_CUTOFF`: cutoff jump/partition dominates;
- `VI_STRUCTURAL_FLOOR`: `S0` triangle lower bound has lost sign near/below `lambda_*`;
- `VII_UNKNOWN`: none of the above yet justified.

`VI_STRUCTURAL_FLOOR` is not a numerical failure and must not trigger finer subdivision.

---

## 13. Progress metrics

Maintain four constants separately:

\[
C_{\rm proved},
\quad C_{\rm certified\ numerical},
\quad C_{\rm asymptotic},
\quad C_{\rm heuristic}.
\]

Current status:

\[
\boxed{C_{\rm proved}=10.52.}
\]

The number

\[
4.914588956\ldots
\]

is currently a **structural/asymptotic PSC target only**, not `C_proved`.

A smaller proved constant is real progress, but repeated constant shaving without a new mechanism is lower priority than LS-A1/LS-A2, because those theorems explain the entire gap and expose the exact point where a new certificate is needed.

---

## 14. Immediate execution order

### Round LS-1 — loss decomposition and true-weight theorem

1. Reproduce the `10.52` certificate from the imported knowledge files.
2. Derive explicit exact-weight formulas in `(t,lambda)`.
3. Prove LS-A1 with an explicit uniform remainder.
4. Record a machine-readable loss ledger.

### Round LS-2 — renormalized transversality limit

1. Prove `t Phi0 -> lambda/4` uniformly.
2. Prove the required `E0,E1,d` limits.
3. Prove `(LS-limit)` with explicit remainder.
4. Derive an explicit `t_epsilon` for at least one nontrivial `epsilon`.

### Round LS-3 — compact certified bridge

Cover `[t_epsilon,1/2] x [lambda_*+epsilon,10.52]` with audited 512/768-bit boxes. Do not optimize precision before optimizing the analytic envelope.

### Round LS-4 — below-floor falsification tournament

Compare only a small number of mechanisms:

1. exact-head / convex-tail joint jet;
2. collision-conditioned phase-velocity separator;
3. one genuinely new Riemann-specific harmonic/heat identity.

Reject any candidate that reduces to Laguerre positivity, global winding, an assumed gap lower bound, or an RH-equivalent endpoint.

### Parallel Round C-1

Continue the Round-62 prime-side fourth-cumulant/factorization falsification at lower priority; promote it only if it produces a finite structural theorem beyond pair data.

---

## 15. Final success condition

The Low-Shoulder program is complete only after a finite proof cover establishes

\[
(H_t(x),H_t'(x))\ne(0,0)
\qquad
\forall\,0<t\le1/2,\ x\in\mathbb R.
\]

Only then apply the boundary-collision reduction and Rodgers--Tao.

Until every regime is closed, the project status remains

\[
\boxed{\mathrm{RH\ OPEN}.}
\]
