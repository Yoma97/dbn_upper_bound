# High-shoulder certificate bundle

This directory contains the reproducibility artifacts for the project theorem

\[
0<t\le 1/2,\qquad \lambda=t\log(|x|/(4\pi))\ge 10.52
\quad\Longrightarrow\quad
(H_t(x),H_t'(x))\neq(0,0).
\]

## Scalar global audit

- `high_shoulder_lambda1052_audit.c`: directed-rounding MPFR scalar verifier. Compile once with the default `PREC=512` and once with `-DPREC=768`.
- `high_shoulder_lambda1052_audit_512.txt`
- `high_shoulder_lambda1052_audit_768.txt`

Both runs return `AUDIT_RESULT pass=1` and the same outward-projected lower margin

`0.0051784223492658803`.

## Positive Dirichlet moments

- `dirichlet_tail_moments_mpfr_512.c`
- `dirichlet_tail_moments_p1814_512.txt`

The verifier sums positive terms through `M=10^6` with MPFR upward rounding and bounds the remaining tail by an explicit decreasing integral.

## Actual-weight boundary regression

- `phase_lambda1052_boundary_512.txt`
- `phase_lambda1052_boundary_768.txt`

These are independent regression outputs at the boundary box near
`t=0.5`, `x≈4π exp(21.04)`. They use the full finite heat-flow amplitudes and return phase margin

`8.0875893307159448`.

The full dynamic-`N` joint-jet verifier that generated these outputs belongs to the joint-jet certificate suite. The scalar theorem above does not depend on the boundary regression; the regression is diagnostic evidence locating the quantitative loss in the global `n^-1.814` majorant.

## Source and circularity

The analytic input is only the unconditional effective Riemann--Siegel approximation in D.H.J. Polymath Theorem 1.3 / Corollary 6.5, elementary complex analysis, and directed-rounding finite arithmetic. No RH assumption, no `Lambda<=0`, no `Lambda=0`, and no finite-height RH verification are used in this certificate.

Status: `PROJECT-PROVED HIGH-SHOULDER`; RH remains OPEN.
