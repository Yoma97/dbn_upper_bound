# Round 71 — Global positive-time shoulder improvement to `lambda >= 7.10`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED + 512/768-BIT CERTIFIED.  
**Referee status:** NOT YET REFEREE_VERIFIED under the project's two-independent-reconstruction rule.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Theorem 71.1

Let

\[
\lambda=t\log\frac{|x|}{4\pi}.
\]

Then the project now has a complete internal proof/certificate of

\[
\boxed{
0<t\le\frac12,
\qquad
\lambda\ge7.10
\Longrightarrow
(H_t(x),H_t'(x))\neq(0,0).
}
\tag{71.1}
\]

Equivalently, no real multiple zero of the de Bruijn--Newman heat family occurs in the positive-time shoulder `lambda>=7.10`.

This is a strict improvement over the previously certified constant `10.52`.

It is **not** a proof of RH, because the region below `lambda=7.10` and the bounded spatial core remain open.

---

## 2. Proof cover

The proof is the union of three independently defined regimes.

### Regime A — small time

Round 70 proves analytically

\[
0<t\le0.01,
\qquad
7.10\le\lambda\le10.52
\Longrightarrow
(H_t,H_t')\neq(0,0).
\tag{71.2}
\]

The terminal scalar arithmetic was rerun at 512 and 768 bits. The PSC contradiction margin is larger than `96.25`.

### Regime B — compact middle rectangle

Rounds 68--69, read with the Round-69 absolute-log correction, give a box-safe directed-rounding certificate.

The adaptive tiler covers

\[
0.01\le t\le0.5,
\qquad
7.10\le\lambda\le10.52.
\tag{71.3}
\]

At both 512 and 768 bits:

- certified terminal leaves: `7219`;
- unresolved leaves: `0`;
- exact rectangle area: `1.6758`;
- exact certified area: `1.6758`;
- smallest outward-projected PSC margin:  
  \[
  \boxed{0.018395736848899086>0};
  \]
- SHA256 of the full projected certified-leaf CSV in both runs:  
  `e95a62f0555efa04b9156363c1c986587da90b715113f02ec97dc91f134dc104`.

The identical projected leaf file is not used as a substitute for the 768-bit run: both runs independently execute all MPFR inequalities; the identical hash is an additional reproducibility check.

The weakest certified leaf is

\[
t\in[0.47703125,0.4846875],
\qquad
\lambda\in[7.10,7.1534375],
\]

where both precisions certify the displayed minimum margin.

### Regime C — previous high shoulder

The corrected Round-67 V2 certificate proves

\[
0<t\le0.5,
\qquad
\lambda\ge10.52
\Longrightarrow
(H_t,H_t')\neq(0,0).
\tag{71.4}
\]

Its corrected 512/768-bit scalar contradiction margin is

\[
0.0051784077356494497>0.
\]

The three regimes overlap at `t=0.01` and `lambda=10.52`; hence their union is exactly the domain in (71.1).

---

## 3. Exact partition audit for Regime B

The tiler uses only exact `Decimal` dyadic bisection of the root rectangle. Every failed nonterminal box is replaced by its four exact children; every certified box is terminal.

The compact manifest records all terminal leaves by depth using the flattened index

\[
I=t_{\rm index}2^d+\lambda_{\rm index}.
\]

Expanding those terminal ranges onto the finest depth-9 grid gives

\[
262144
\]

cells, of which

\[
262144
\]

are covered exactly once, with

\[
0
\]

missing cells and

\[
0
\]

overlaps.

This is stronger than checking only the total area.

---

## 4. The rectangular certificate used in Regime B

For a box

\[
B=[t_-,t_+]\times[\lambda_-,\lambda_+],
\]

Round 68 constructs one true-weight majorant

\[
F_B(n)=
\exp\left(
\frac{t_+}{4}\log^2n-\sigma_B\log n
\right)
\]

that dominates every real phase amplitude in the box.

An exact finite head (`K=128`) is combined with the convex-secant tail of

\[
g_B(v)=\frac{t_+}{4}v^2-(\sigma_B-1)v.
\]

Round 69 supplies a matching box envelope for the unconditional Polymath value error, the one-term pointwise cutoff bridge, the symmetric-normalization ratio, and the Cauchy derivative error.

A box is accepted only if all monotonicity/domain gates pass and

\[
2\left[
\Phi_B^{\rm lo}
\sqrt{(S_{0,B}^{\rm lo})^2-(E_{0,B}^{\rm up}/2)^2}
-d_B^{\rm up}A_{1,B}^{\rm up}
\right]
>E_{1,B}^{\rm up}.
\tag{71.5}
\]

No sampled value is promoted to a box theorem; every accepted leaf is certified by interval-directed analytic envelopes.

---

## 5. Why the cutoff treatment is legitimate

The parameter-box cutoff may vary by many integers. We never force one integer cutoff across the whole parameter rectangle.

At each parameter point, Cauchy's theorem uses its own fixed base cutoff

\[
N_0(t,\lambda)
=
\left\lfloor
\sqrt{
\frac{x_c-\rho}{4\pi}+rac t{16}}
\right\rfloor.
\]

Only within that one Cauchy disk can the local Polymath cutoff change, and the real-coordinate variation is

\[
\frac{2\rho}{4\pi}<0.016,
\]

so at most one Riemann--Siegel square threshold can be crossed. The possible one-term contribution is explicitly included in `E0` before applying Cauchy's derivative estimate.

This removes a major potential interval-dependency/cutoff error.

---

## 6. Directed-rounding audit

The canonical executable source is

`research_lab/certificates/low_shoulder/convex_tail_psc_box_mpfr.c`.

Every decimal box endpoint is read twice, downward for lower endpoints and upward for upper endpoints. The code keeps separate lower/upper values of `pi`, the Cauchy radius, logarithms, moving-cutoff bounds, exponents, and denominators.

The old high-shoulder artifact had previously revealed how easy it is to misuse one directed logarithm in both a positive and a negative term. Round 71 uses only the corrected V2 high-shoulder code and the independently written low-shoulder box verifier.

The box source compiles cleanly with `-Wall -Wextra` in the audit environment.

---

## 7. Falsification checks

### Lowest-margin box

The weakest leaf was rerun explicitly at both 512 and 768 bits and remains positive by

\[
0.018395736848899086.
\]

### Direct finite-sum sanity check

At the boundary point

\[
t=0.5,
\qquad
\lambda=7.10,
\]

the real Riemann--Siegel cutoff is only `N=1211`, so the true positive moments can be evaluated directly as a non-proof sanity check:

\[
A_0\approx0.7315318980,
\qquad
A_1\approx1.6587196963.
\]

They lie below the neighboring rigorous box envelopes, as required. This check is diagnostic only; it is not an input to (71.1).

### Attempted lowering

Pointwise exploration at `t=0.5` shows the present certificate still succeeds near `lambda=7.08` but fails near `7.06`; the transition for a tiny boundary box is approximately `7.07585`.

This is **heuristic/diagnostic only**. It shows that `7.10` is close to the current finite-time phase-slope limit and that pushing immediately to the asymptotic floor `4.914...` by the same coarse certificate is unrealistic.

---

## 8. Circularity audit

Theorem 71.1 uses only:

1. unconditional Polymath Theorem 1.3 / Corollary 6.5;
2. exact elementary formulas for the Polymath phase and amplitude derivatives;
3. the phase-slope contradiction inequality;
4. positive-series/integral estimates;
5. convexity of a quadratic exponent;
6. Schwarz symmetry and Cauchy's estimate;
7. MPFR directed rounding for finite scalar/box subproblems.

It does **not** use:

- RH;
- `Lambda<=0` or `Lambda=0`;
- real-rootedness of `H_0`;
- any finite-height verification of RH as a global proof input;
- pair correlation or GUE;
- zero-spacing lower bounds;
- Laguerre--Polya membership;
- any Rodgers--Tao estimate whose proof assumes `Lambda<0` for contradiction.

The proof never assumes simplicity of the zero whose existence it is excluding.

---

## 9. Status of the threshold

Within the project, the previous proved shoulder constant

\[
10.52
\]

can now be replaced by

\[
\boxed{C_{\rm project-proved}=7.10.}
\]

The exact status label is important:

- mathematical truth status: **INTERNALLY_PROVED**;
- finite certificate status: **512/768-BIT CERTIFIED**;
- circularity audit: **PASSED internally**;
- independent referee reconstruction: **PENDING**;
- novelty/literature audit: **NOVELTY_UNVERIFIED**.

Therefore this result must not yet be described as externally verified, published, or community-established.

---

## 10. What remains for RH

The global target is still

\[
(H_t(x),H_t'(x))\neq(0,0)
\qquad
\forall\,0<t\le1/2,\ x\in\mathbb R.
\]

Round 71 closes only the region

\[
\lambda\ge7.10.
\]

The remaining work contains:

1. the lower shoulder `lambda<7.10`, where the current finite-time PSC approaches its phase/amplitude limit near `t=1/2`;
2. eventually the asymptotic triangle-envelope floor `lambda_*=4.914588956...`, below which the unchanged `S0=1-A0` lower bound loses its fixed-lambda small-time sign;
3. the bounded spatial core where `lambda` is not an appropriate positive coordinate.

RH remains OPEN.
