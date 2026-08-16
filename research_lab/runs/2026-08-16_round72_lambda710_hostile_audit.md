# Round 72 — Hostile audit of the `lambda >= 7.10` shoulder theorem

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Object audited:** Round 71 Theorem 71.1.  
**Audit outcome:** NO FATAL DEFECT FOUND; one orchestration hardening was required and the complete 512/768-bit computation was rerun afterward.  
**Referee status:** still NOT an independent-referee reconstruction.

---

## 1. Attack matrix

The theorem

\[
0<t\le1/2,
\qquad
\lambda\ge7.10
\Longrightarrow
(H_t,H_t')\neq(0,0)
\]

was attacked along the following independent failure channels:

1. theorem-domain mismatch in the Polymath approximation;
2. incorrect use of one cutoff over a parameter rectangle;
3. more than one cutoff jump on a Cauchy disk;
4. nonanalytic moving-cutoff remainder under Cauchy's theorem;
5. wrong normalization ratio for the derivative error;
6. interval dependency in the true heat weights;
7. wrong convex-chord direction;
8. directed-rounding sign errors;
9. incomplete dyadic partition;
10. finite sampling masquerading as a box theorem;
11. loss of the `t->0` endpoint;
12. hidden use of RH, `Lambda<=0`, or zero simplicity.

Each item is adjudicated below.

---

## 2. Polymath theorem domain — PASS

Every low-shoulder box satisfies

\[
0<t\le1/2,
\qquad
0\le y\le\rho=0.1<1.
\]

At the smallest height in the finite rectangle,

\[
L=\lambda/t\ge7.10/0.5=14.2,
\]

so

\[
x=4\pi e^L>10^7>200.
\]

The entire Cauchy disk remains in `x>200`. Hence the unconditional Polymath Theorem-1.3 region is respected with large slack.

---

## 3. Parameter-box cutoff — PASS after explicit redesign

A single integer cutoff is **not** fixed across a `(t,lambda)` rectangle.

At each parameter point the analytic Cauchy remainder uses its own base cutoff

\[
N_0(t,\lambda)
=
\left\lfloor
\sqrt{
\frac{x_c-\rho}{4\pi}+rac t{16}}
\right\rfloor.
\]

The rectangular theorem bounds the positive sums uniformly over all possible pointwise cutoffs; it does not pretend that the cutoff is constant in parameter space.

This is the correct architecture and avoids a potentially fatal moving-cutoff dependency.

---

## 4. Disk-local jump count — PASS

Across one Cauchy disk the Riemann--Siegel argument changes by

\[
\frac{2\rho}{4\pi}<0.016.
\]

The cutoff changes when this argument crosses an integer square. Consecutive nonnegative integer squares are separated by at least one, and in the actual large-`N` range by much more. Therefore at most one cutoff term can appear/disappear on the disk.

The one possible extra term is explicitly included in `E0`.

---

## 5. Cauchy analyticity — PASS

Cauchy's derivative estimate is applied to the remainder obtained after **freezing the pointwise base cutoff** on the disk. The finite main sum is then analytic in `z`; the dynamic local-cutoff discrepancy is transferred into the analytic-error envelope before differentiation.

Thus the proof never differentiates a floor function or a moving finite sum.

---

## 6. Symmetric normalization — PASS after prior correction

One must not compare the functional-equation partner points `s_+` and `s_-` directly; they are separated by the large imaginary height.

Round 65's normalization audit instead uses Schwarz symmetry

\[
\Re\log M_t(s_-)
=
\Re\log M_t(\overline{s_-})
\]

and compares `s_+` with `overline{s_-}` along a short real segment of length `y<=rho`.

Hence

\[
|B_t/D_t|
\le
\exp\left(
\frac y2\sup|M_t'/M_t|
\right).
\]

The low-shoulder executable uses a deliberately weaker upper envelope, so the derivative error remains valid.

---

## 7. True-weight interval dependency — PASS

The dangerous combination is that a wide box can mix

- the heaviest heat coefficient `t_+`, and
- the longest cutoff produced by `lambda_+/t_-`.

Round 68 handles this explicitly with one rectangular dominating weight

\[
F_B(n)=
\exp\left(
\frac{t_+}{4}\log^2n-\sigma_B\log n
\right).
\]

The monotonicity quantity

\[
\mu_B=\sigma_B-\frac{t_+}{2}V_B
\]

is a hard gate. If the mixed box is too wide, the box is rejected and subdivided; no positivity conclusion is drawn.

The large number of early `WEIGHT_MONOTONICITY_GATE` failures in the tiling summaries is therefore expected proof behavior, not missing coverage.

---

## 8. Convex-chord direction — PASS

After `u=e^v`, the tail counting exponent is quadratic with

\[
g_B''(v)=t_+/2>0.
\]

For a convex function the graph lies **below** the secant chord between the endpoints. Therefore replacing `g_B(v)` by its secant gives an upper bound for `e^{g_B(v)}` and hence for both the value and logarithmic-moment tails.

For negative secant slope the implementation uses

\[
\frac{1-e^{-aD}}a,
\qquad
\frac{1-e^{-aD}(1+aD)}{a^2}
\]

rather than the earlier crude `D,D^2/2` envelopes. This was necessary for practical small-`t` boxes but does not change the theorem direction.

---

## 9. Round-69 absolute logarithm — PASS only with correction note

The first draft of Round 69 included an unnecessary tiny formula for the negative part of

\[
\log(x'/(4\pi n^2)).
\]

It is superseded by the explicit correction

\[
U_B=\lambda_++t_+h_\rho^+,
\]

which controls both signs of the logarithm. The canonical executable implements this corrected formula.

The uncorrected equation must not be cited independently.

---

## 10. Directed rounding — PASS with a historical warning

The project previously found genuine direction-of-rounding mistakes in the first imported `10.52` scalar helper. That experience was used as an explicit attack template here.

The low-shoulder verifier keeps lower and upper endpoints separate for:

- `t,lambda,rho`;
- `pi`;
- logarithms;
- cutoff extrema;
- positive and negative exponents;
- denominators;
- phase lower bounds and error upper bounds.

The weakest leaf was rerun at 512 and 768 bits and retains margin

\[
0.018395736848899086>0.
\]

No mixed-direction defect analogous to the old high-shoulder issue was found in the reviewed low-shoulder operations.

---

## 11. Tiler exit-code attack — FIXED AND RERUN

The first tiler accepted a leaf when the executable output parsed as

`RESULT status=CERTIFIED`.

Although the C verifier returns exit code zero exactly in that case, the orchestration layer should not assume the consistency of two independent channels.

The tiler was hardened to require simultaneously:

1. parsed status `CERTIFIED`;
2. process exit code `0`.

The complete rectangle was rerun at both 512 and 768 bits **after** this change.

Both hardened reruns again produce

- `7219` certified leaves;
- `0` unresolved;
- exact full area;
- the same minimum margin;
- the same certified-leaf SHA256.

Thus the hardening reveals no hidden computational failure.

---

## 12. Partition completeness — PASS

The compact leaf manifest was expanded independently to the uniform depth-9 grid.

Result:

\[
262144\text{ cells total},
\]

\[
262144\text{ covered exactly once},
\]

\[
0\text{ missing},
\qquad
0\text{ overlap}.
\]

Therefore the certificate is a true finite cover, not a collection of sampled boxes.

---

## 13. `t->0` endpoint — PASS via analytic theorem, not numerics

The finite tiler begins at `t=0.01`. Round 70 separately proves the full continuum

\[
0<t\le0.01,
\qquad
7.10\le\lambda\le10.52
\]

using explicit head/tail power bounds and exponentially decaying Polymath errors.

The geometry addendum removes the only compressed step in that proof by bounding each disk correction explicitly.

Thus no limiting sequence of numerical boxes is being mistaken for a proof at `t=0`.

---

## 14. Collision assumption and simplicity — PASS

The PSC is a direct contradiction argument from

\[
H_t(x)=H_t'(x)=0.
\]

It does not invoke the root-motion ODE and does not require the zero to be simple before excluding multiplicity.

Higher multiplicity is also excluded because it still satisfies the same common-zero condition.

---

## 15. Circularity attack — PASS internally

No proof edge uses:

- RH;
- `Lambda<=0`;
- `Lambda=0`;
- all-real zeros of `H_0`;
- a finite-height RH verification;
- zero-gap lower bounds;
- GUE or pair correlation;
- Laguerre--Polya membership;
- Rodgers--Tao estimates whose derivation assumes `Lambda<0` for contradiction.

The only use of `Lambda>=0` belongs to the eventual global RH reduction and is not used to prove the shoulder theorem.

---

## 16. Falsification below 7.10

A tiny-box exploratory scan at `t=0.5` gives:

- present certificate succeeds at `lambda=7.08`;
- present certificate fails at `lambda=7.06`;
- estimated pointwise transition near `7.07585`.

Therefore the `7.10` proof is not merely benefiting from an enormous unused finite-time margin. It lies within a few hundredths of the current finite-time PSC edge.

These numbers are diagnostic only; they do not alter the theorem.

---

## 17. Audit verdict

No fatal mathematical, interval, cutoff, or circularity defect was found after the required corrections and reruns.

The strongest justified status is therefore

\[
\boxed{
C_{\rm project-proved}=7.10
}
\]

with labels

- `INTERNALLY_PROVED`;
- `512/768-BIT CERTIFIED`;
- `CIRCULARITY AUDIT PASSED INTERNALLY`;
- `REFEREE_VERIFIED: PENDING`;
- `NOVELTY_UNVERIFIED`.

This is genuine progress on the chosen route, but RH remains OPEN.
