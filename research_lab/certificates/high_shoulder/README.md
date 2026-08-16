# High-shoulder certificate bundle

This directory contains the canonical reproducibility artifacts for the project theorem

\[
0<t\le 1/2,\qquad \lambda=t\log(|x|/(4\pi))\ge 10.52
\quad\Longrightarrow\quad
(H_t(x),H_t'(x))\neq(0,0).
\]

## Canonical directed-rounding audit V2

The first imported audit was subjected to a hostile rounding-direction review. Two formal issues were found: a value of `pi` rounded upward had been reused in a quantity intended as a lower bound, and a logarithm rounded upward had been reused in a negative exponent that required its lower enclosure. The original Dirichlet-moment helper had an analogous mixed-direction multiplication issue.

Those issues were at roughly MPFR-ulp scale and did not threaten the numerical slack, but they invalidated the old files as literal directed-rounding proof artifacts. The files in this directory have now been replaced by the corrected V2 sources and rerun outputs.

### Scalar global audit

- `high_shoulder_lambda1052_audit.c`
- `high_shoulder_lambda1052_audit_512.txt`
- `high_shoulder_lambda1052_audit_768.txt`

Compile the same source at `PREC=512` and `PREC=768`. Both corrected runs return

`AUDIT_RESULT pass=1`

and the same outward-projected lower contradiction margin

`0.0051784077356494497`.

The corrected audit maintains separate lower/upper enclosures for `pi`, `L`, `rho`, and `log N`, and uses each according to the monotonicity of the expression being bounded.

## Positive Dirichlet moments

- `dirichlet_tail_moments_mpfr_512.c`
- `dirichlet_tail_moments_p1814_512.txt`
- `dirichlet_tail_moments_p1814_768.txt`

The corrected verifier computes the upper bound for `n^{-p}` from a downward enclosure of `p log n`, while using an upward enclosure of `log n` in the logarithmic moment. The integral tail also uses separate lower/upper logarithms according to sign.

At `p=1.814`, `M=100000`, both 512-bit and 768-bit runs give

\[
A_0\le0.86163407260348712,
\qquad
A_1\le1.4447738087713327.
\]

The scalar high-shoulder audit deliberately pads these to

\[
A_0\le0.861634073,
\qquad
A_1\le1.44477381.
\]

## Actual-weight boundary regression

- `phase_lambda1052_boundary_512.txt`
- `phase_lambda1052_boundary_768.txt`

These are independent diagnostic regressions at the boundary box near
`t=0.5`, `x≈4π exp(21.04)`. They use the full finite heat-flow amplitudes and return phase margin

`8.0875893307159448`.

The boundary regression is not used by itself to prove the global `lambda>=10.52` theorem; it diagnoses how much slack is lost by replacing the true quadratic heat weights with the global `n^-1.814` majorant.

## Analytic source and circularity

The analytic input is only the unconditional effective Riemann--Siegel approximation in D.H.J. Polymath Theorem 1.3 / Corollary 6.5, elementary complex analysis, positive-series tail bounds, and directed-rounding finite arithmetic.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- finite-height RH verification;
- Laguerre--Polya membership;
- Rodgers--Tao estimates whose proof starts from `Lambda<0`.

Status after the V2 rerun: `PROJECT-PROVED HIGH-SHOULDER`; RH remains OPEN.

## Local source SHA256 values used for the V2 rerun

The corrected files were compiled and rerun before committing. Their local byte-level hashes were:

- corrected scalar source: `f803397faa88e440783e1bd337ec12e2e9556059c1a2fe651b86cf61d304aabe`
- 512 scalar output: `de8a5eb160fa9bc6bc973a95bfa6d276cca9bdb50c660e0d91c384e03d5b0ced`
- 768 scalar output: `337d00903510f79a3b78b9d8f731b8360452e06498361b4a6a904b15c42da843`
- corrected moment source: `f4bf65388b01c6544f5d87b93f13d3f46cf8f4a353c97fff495e32a1c698e1ef`
- 512 moment output at `M=100000`: `e1be5739f4eb68d1dd5b0289d5ca82831781b1907123fe78357b1ec6d4fe1e64`
- 768 moment output at `M=100000`: `7ebfd97247829a73eeeb49d2e2429508ca2a10d09647a90435f94f95375ac46d`
