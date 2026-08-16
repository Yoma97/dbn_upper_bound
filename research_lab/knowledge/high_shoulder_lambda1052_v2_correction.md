# Canonical correction to the lambda >= 10.52 high-shoulder proposition

**Date:** 2026-08-16  
**Status:** PROVED / unconditional relative to the cited Polymath theorem and the corrected V2 directed-rounding certificate.  
**RH status:** OPEN.

This note supersedes the **finite decimal audit values and executable-rounding claims** in `high_shoulder_lambda1052_proposition.md`. The theorem statement itself is unchanged:

\[
0<t\le\frac12,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge10.52
\Longrightarrow
(H_t(x),H_t'(x))\neq(0,0).
\]

A hostile audit found direction-of-rounding defects in the first imported MPFR helper programs. The defects were at MPFR-ulp scale and did not threaten the analytic slack, but the old executables are not canonical proof artifacts.

The corrected canonical files are in

`research_lab/certificates/high_shoulder/`.

The corrected positive-moment audit at both 512 and 768 bits certifies

\[
A_0\le0.86163407260348712,
\qquad
A_1\le1.4447738087713327.
\]

The scalar proof uses the padded values

\[
A_0\le0.861634073,
\qquad
A_1\le1.44477381,
\qquad
S_0\ge0.138365927.
\]

The corrected scalar theorem audit at both 512 and 768 bits certifies

\[
E_0\le2.7089645820749954\times10^{-8},
\]

\[
E_1\le4.6814434358897312\times10^{-7},
\]

\[
\sqrt{S_0^2-(E_0/2)^2}
\ge0.13836592699999933,
\]

and

\[
2\left[
5.25\sqrt{S_0^2-(E_0/2)^2}
-0.501A_1
\right]
\ge0.0051788758799930388.
\]

Therefore the corrected contradiction margin is

\[
\boxed{0.0051784077356494497>0.}
\]

Both runs return `AUDIT_RESULT pass=1`.

For all future work, cite this correction, Round 67, and the V2 certificate directory rather than the superseded decimal values in the original proposition note.

Circularity status is unchanged: no RH, `Lambda<=0`, finite-height RH verification, Laguerre--Polya membership, pair correlation, or negative-time Rodgers--Tao contradiction estimates are used.
