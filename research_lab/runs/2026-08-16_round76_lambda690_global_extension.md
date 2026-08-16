# Round 76 — Global shoulder extension to `lambda >= 6.90` using hybrid PSC/APVC

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED + independent 512/768-bit certified arithmetic/box reruns.  
**Referee status:** PENDING.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Theorem

Let

\[
\lambda=t\log\frac{|x|}{4\pi}.
\]

Then, within the present project proof framework,

\[
\boxed{
0<t\le\frac12,
\qquad
\lambda\ge6.90
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\tag{76.1}
\]

Thus the current certified shoulder constant becomes

\[
\boxed{C_{\rm project-proved}=6.90.}
\tag{76.2}
\]

This is a strict improvement over Round 73 (`7.08`). It does **not** prove RH; the region below `6.90`, the eventual very-low shoulder, and the bounded spatial core remain open.

---

## 2. Proof cover

The theorem is the union of four overlapping regions.

### A. Small time, new strip

\[
0<t\le0.01,
\qquad
6.90\le\lambda\le7.08.
\]

Closed analytically by the old exact-weight PSC with a separate scalar MPFR audit.

### B. Compact lower-time strip

\[
0.01\le t\le0.40,
\qquad
6.90\le\lambda\le7.08.
\]

Closed entirely by the existing true-weight PSC verifier.

### C. Compact upper-time strip

\[
0.40\le t\le0.50,
\qquad
6.90\le\lambda\le7.08.
\]

Closed by the hybrid verifier: old PSC first, then the Round-74 soft APVC on any PSC-failed box. The favorable `A1` term uses a directed lower finite head with `K=512`.

### D. Previously proved region

\[
0<t\le0.50,
\qquad
\lambda\ge7.08.
\]

Closed by Round 73.

These sets overlap on their boundaries and cover every `0<t<=1/2`, `lambda>=6.90`.

---

## 3. Small-time analytic audit at `lambda=6.90`

For `t<=0.01`,

\[
L=\lambda/t\ge690.
\]

On the real axis

\[
\sigma=\frac12+\frac\lambda4+\eta,
\qquad
-10^{-4}<\eta\le0,
\]

with enormous geometric slack because `x=4pi e^L`.

Split by `u=t log n`.

If `u<=1`, then

\[
\sigma-\frac t4\log n
>
\frac12+\frac{6.90}{4}-\frac14-10^{-4}
=1.9749,
\]

so the audit uses the weaker

\[
a_n\le n^{-1.974}.
\tag{76.3}
\]

For the remaining moving-cutoff terms,

\[
\sigma-\frac t4\log n
>
\frac12+\frac{6.90}{8}-2\cdot10^{-4}
=1.3623,
\]

so

\[
a_n\le n^{-1.362}.
\tag{76.4}
\]

The second exponent is only used beyond `log n>100`, making its contribution exponentially tiny.

The corrected 512/768-bit directed runs both give the same outward decimal projections

\[
A_0\le0.77722864068274755,
\qquad
A_1\le1.0753686876970201,
\]

and therefore

\[
\boxed{S_0\ge0.22277135931725248.}
\tag{76.5}
\]

For the Polymath remainder channels we deliberately use padded envelopes. The positive main error is bounded by

\[
 e_A+e_B<256e^{-6.90/t}.
\tag{76.6}
\]

On the radius-`0.1` disk the scaled logarithmic variable in the `e_C` exponent exceeds `6.8`: indeed the only loss from the real-axis scaled value `lambda>=6.90` is of order `t rho/(x-rho)`, which is far below `10^{-4}` for `L>=690`. Hence

\[
\frac{W}{4}+\frac{W^2}{16}>4.59,
\]

and the audit uses

\[
 e_{C,0}<e^{1-4.59/t}.
\tag{76.7}
\]

After the upper-semicircle `n^y` loss, the positive exponent remains greater than `1.312`; together with the disk cutoff lower geometry this permits the weaker jump envelope

\[
E_{\rm jump}<8e^{-4.45/t}.
\tag{76.8}
\]

The symmetric-normalization envelope remains the already audited

\[
R(t)<e^{0.526/t+0.2},
\]

so

\[
E_1<10R(t)E_0.
\tag{76.9}
\]

All net exponents after the normalization factor remain positive. The envelopes increase with `t` on `(0,0.01]`, so `t=0.01` is the scalar endpoint audit.

At 512 and 768 bits:

\[
E_0<4.3857680835574265\times10^{-193},
\]

\[
E_1<3.7393344206968593\times10^{-169}.
\]

Since `L>=690`, the real-axis phase speed is safely bounded by

\[
\Phi>172.49,
\qquad d<0.501.
\]

The final PSC lower margin is

\[
\boxed{75.774144112193341>0.}
\tag{76.10}
\]

in both precision runs.

Canonical files:

- `small_time_lambda690_audit.c`;
- `small_time_lambda690_audit_512.txt`;
- `small_time_lambda690_audit_768.txt`.

GitHub Actions run `31924777671` compiled and executed the same source independently at both precisions, with `AUDIT_RESULT pass=1` in both jobs.

---

## 4. Compact lower-time proof

For

\[
0.01\le t\le0.40,
\qquad
6.90\le\lambda\le7.08,
\]

the already audited true-weight PSC verifier was run with

- `K=128`;
- maximum quadtree depth `10`;
- radius `rho=0.1`;
- directed MPFR arithmetic.

Both 512 and 768 bits returned exactly:

- `3301` certified leaves;
- `0` unresolved leaves;
- exact root and certified area `0.0702`;
- coverage fraction `1`;
- minimum margin
  \[
  \boxed{0.0083044035209287551>0};
  \]
- identical certified-manifest SHA256  
  `d09a13b1fb2d17cba892d2bf6975b2ce002c405a240f09a999c90ee7a04fef0c`;
- identical empty unresolved-manifest SHA256  
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

This is a finite box cover, not point sampling.

Canonical Actions run: `31924873074` (`low` jobs).

---

## 5. Compact upper-time proof and the new mechanism

For

\[
0.40\le t\le0.50,
\qquad
6.90\le\lambda\le7.08,
\]

the deterministic hybrid verifier was generated from the already audited PSC source, then patched by the Round-74 soft cutoff-slope defect. Thus all existing Polymath error machinery is inherited literally; only the second collision certificate is added.

The hierarchy is:

1. old PSC;
2. if PSC fails, APVC with
   \[
   \delta_U=\max(T_U\log N_U-\Phi_L,0),
   \]
   \[
   B_1\le(\Phi_U+2\delta_U)A_{0,U}
   -(T_L-\sigma_{x,U})A_{1,L};
   \]
3. subdivide only if neither certificate closes the whole box.

The `A1` lower enclosure is obtained from the first `K=512` true positive weights, with the omitted positive tail discarded. The minimum disk cutoff throughout this strip exceeds `512`, so all head terms are genuinely present in every point of each accepted APVC box.

Independent 512/768-bit runs give identically:

- `409` certified leaves;
- `0` unresolved leaves;
- exact root and certified area `0.0180`;
- coverage fraction `1`;
- minimum certified margin
  \[
  \boxed{0.000013123697123932965>0};
  \]
- identical certified-manifest SHA256  
  `d2d632971fcc3f0bbfcecc41e674005e1aeaa4cc48ed58b9ed70572a2bc12734`;
- identical unresolved-manifest SHA256  
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

Canonical Actions run: `31924959080`.

This is the first certified threshold improvement in the project that actually requires the new APVC mechanism; old PSC alone left a nonempty finite-time failure region near the upper edge.

---

## 6. Why this is not an interval-artifact claim

Before APVC, the old PSC diagnostic over `0.01<=t<=0.45`, `6.90<=lambda<=7.08` left `15507` depth-10 boxes unresolved, all with status `PSC_CORE`, starting around `t=0.41777`. Thus the old scalar certificate genuinely approached its finite-time core boundary.

Round 74 changes the mathematics: it uses the collision value equation to anchor `sin(phi)` via the exact `n=1` term and keeps the correlation between the outer phase speed and `tau_x log n` in the derivative tail.

The successful Round-76 high-time cover therefore represents a stronger certificate, not merely more subdivision of the old one.

---

## 7. Circularity audit

Used:

- unconditional D.H.J. Polymath effective Riemann--Siegel approximation;
- exact heat weights and real-axis `alpha,alpha'` formulas;
- Round-64/66 positive weight machinery;
- old phase-slope certificate;
- Round-74 APVC and its soft cutoff-slope addendum;
- Cauchy derivative control and symmetric-normalization bounds;
- finite directed-rounding sums and tails;
- MPFR 512/768-bit arithmetic;
- exact finite partition accounting.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- all-real zeros of `H_0`;
- finite-height RH verification;
- zero-spacing assumptions;
- GUE or pair correlation as proof input;
- Laguerre--Polya membership;
- negative-time Rodgers--Tao estimates whose contradiction setup assumes `Lambda<0`.

No desired no-collision conclusion is used as an input.

---

## 8. Next target

The pointwise diagnostic APVC boundary at `t=1/2` lies near

\[
\lambda\approx6.8188,
\]

but this is not a proof threshold. The next deliberately conservative certification target is

\[
\boxed{C_{\rm target}=6.85.}
\]

Round 75's convex-secant APVC is reserved for residual boxes if the simpler soft APVC becomes the limiting majorant.

Until a complete 512/768-bit cover at a lower target is produced, the official project value is

\[
\boxed{C_{\rm project-proved}=6.90.}
\]
