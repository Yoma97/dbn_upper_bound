# Low-shoulder certificate bundle

This directory contains the current finite/analytic proof layer for the project shoulder theorem

\[
0<t\le1/2,
\qquad
\lambda=t\log(|x|/(4\pi))\ge7.08
\quad\Longrightarrow\quad
(H_t(x),H_t'(x))\ne(0,0).
\]

**Status:** `INTERNALLY_PROVED + 512/768-BIT CERTIFIED`; `REFEREE_VERIFIED: PENDING`; novelty unverified; RH remains open.

The proof is a finite union of three regions:

1. `0<t<=0.01`, `7.08<=lambda<=10.52`: analytic small-time certificate of Round 73, with independent 512/768-bit scalar audits;
2. `0.01<=t<=0.5`, `7.08<=lambda<=7.10`: directed-rounding rectangular certificate, rerun at 512/768 bits;
3. `lambda>=7.10`: the previously certified Round-71/72 theorem, which itself joins the `7.10--10.52` bridge to the corrected `lambda>=10.52` high-shoulder theorem.

No gap remains above `lambda=7.08`.

## Canonical sources

Current extension:

- `small_time_lambda708_audit.c`
- `convex_tail_psc_box_mpfr.c`
- `adaptive_psc_lambda_tiler.py`

Historical/cross-check source:

- `small_time_lambda710_audit.c`

The hardened tiler accepts a leaf only when the C verifier both prints `RESULT status=CERTIFIED` and exits with code zero.

## Small-time `lambda >= 7.08`

Compile the same source independently at two precisions:

```bash
cc -O2 -Wall -Wextra -DPREC=512 small_time_lambda708_audit.c -lmpfr -lgmp -o small708_512
cc -O2 -Wall -Wextra -DPREC=768 small_time_lambda708_audit.c -lmpfr -lgmp -o small708_768
```

Both GitHub Actions jobs in run `31924049344` returned `AUDIT_RESULT pass=1` with the same outward decimal projections:

\[
A_0\le0.73098651914361068,
\qquad
A_1\le0.98190929449905862,
\]

\[
S_0\ge0.26901348085638938,
\]

\[
E_0\le4.8829945288638576\times10^{-205},
\qquad
E_1\le4.1632729250572989\times10^{-181},
\]

and final PSC margin

\[
\boxed{94.241518840456663>0}.
\]

Canonical outputs:

- `small_time_lambda708_audit_512.txt`
- `small_time_lambda708_audit_768.txt`

The analytic inequalities producing the constants are recorded in Round 73. They use conservative powers `2.019` and `1.384`, not a floating-point fit.

## Compact strip `7.08 <= lambda <= 7.10`

The canonical Actions run `31923760219` executed

```bash
python adaptive_psc_lambda_tiler.py ./psc_box 0.01 0.5 7.08 7.10 10 128 lambda708-512 4
python adaptive_psc_lambda_tiler.py ./psc_box 0.01 0.5 7.08 7.10 10 128 lambda708-768 4
```

at 512 and 768 bits respectively.

Both runs produced exactly:

- `5572` certified terminal leaves;
- `0` unresolved leaves;
- exact root area `0.0098` and certified area `0.0098`;
- coverage fraction `1`;
- minimum outward-projected margin
  `0.000070306587867159615`;
- identical certified-leaf SHA256  
  `af319fc74b08f293a39a0966dabc636bbe41d89cd5911d9ce724a183f081e9df`;
- identical unresolved-manifest SHA256  
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

This is a box cover, not point sampling.

## Previously certified `lambda >= 7.10`

The earlier canonical theorem remains part of the proof chain. Its compact `7.10--10.52` run had:

- `7219` certified leaves;
- `0` unresolved;
- exact certified area `1.6758`;
- minimum margin `0.018395736848899086`;
- certified-leaf SHA256  
  `e95a62f0555efa04b9156363c1c986587da90b715113f02ec97dc91f134dc104`.

The historical scalar source/outputs remain in this directory for reproducibility.

## Diagnostic below `7.08` — not a theorem

A 512-bit diagnostic over

\[
0.01\le t\le0.5,
\qquad
7.06\le\lambda\le7.10
\]

certified `99.5807647705078125%` of the exact area at quadtree depth 10, leaving `4396` unresolved boxes. All terminal failures were `PSC_CORE` failures. They are localized near

\[
0.490908203125\lesssim t\le0.5,
\qquad
7.06\lesssim\lambda\lesssim7.077891.
\]

Therefore `7.06` is **not refuted**, but deeper global subdivision is not the favored next step. The evidence points to a finite-time PSC-core boundary near `t=1/2`, requiring a stronger local collision-conditioned certificate.

## Mathematical dependency and circularity

The certificate uses only:

- unconditional D.H.J. Polymath effective Riemann--Siegel bounds;
- phase-slope transversality algebra;
- true heat weights with convex/integral positive-tail envelopes;
- fixed-point Cauchy remainders plus the explicit one-term cutoff bridge;
- Schwarz symmetry and Cauchy's estimate;
- MPFR directed rounding;
- exact finite partition accounting.

It does **not** use RH, `Lambda<=0`, `Lambda=0`, finite-height RH verification, zero-spacing assumptions, GUE/pair correlation, Laguerre--Polya membership, or Rodgers--Tao estimates whose proof assumes negative `Lambda` in a contradiction setup.

## Current project constant

\[
\boxed{C_{\rm project-proved}=7.08.}
\]

This is a genuine improvement of the shoulder theorem, not a proof of RH. The low-shoulder region below `7.08` and the remaining bounded/core regimes are still open.
