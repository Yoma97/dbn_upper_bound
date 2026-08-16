# Round 69 correction — absolute logarithm in the Polymath error factor

**Date:** 2026-08-16  
**Status:** correction required for canonical use of Round 69.  
**RH status:** OPEN.

Round 69 equation (69.13) included an unnecessary tiny term intended to control the negative part of

\[
\log\frac{x'}{4\pi n^2}
\]

near the moving cutoff. Written with `exp(-lambda_-/t_+)` alone, that term did not explicitly account for the `-rho` displacement in the smallest disk real part. The fix is simpler and stronger.

Let

\[
A=\frac{x'}{4\pi}.
\]

For every Polymath summand, the local cutoff condition gives

\[
n^2\le A+\frac t{16}.
\]

If `n^2>A`, then

\[
0<\log\frac{n^2}{A}
\le
\log\left(1+\frac{t}{16A}\right).
\]

Since the whole disk lies in `x'>200`,

\[
A>\frac{200}{4\pi}>15,
\qquad 0<t\le1/2,
\]

and therefore

\[
t\log\left(1+\frac{t}{16A}\right)
<0.002.
\tag{C1}
\]

On the other hand, if `n^2<=A`, then

\[
t\log\frac{A}{n^2}
\le t\log A
\le
\lambda_+ +t_+h_\rho^+.
\tag{C2}
\]

Because `lambda_->4`, the right side of (C2) is greater than `4`, hence it also dominates the negative-part bound (C1).

Thus the canonical replacement for Round 69 equation (69.13) is simply

\[
\boxed{
U_B:=\lambda_+ +t_+h_\rho^+,
}
\tag{C3}
\]

and one has rigorously

\[
\boxed{
 t\left|
\log\frac{x'}{4\pi n^2}
\right|
\le U_B
}
\tag{C4}
\]

for every summand in every disk over the box.

Consequently Round 69 equation (69.14) is to be read as

\[
\boxed{
H_B=
\frac{U_B^2/16+0.627}{X_- -6.66}
}
\tag{C5}
\]

with `U_B` from (C3).

All later uses of Round 69 must incorporate this correction. No theorem status is promoted from the uncorrected formula.

**Circularity:** elementary cutoff geometry only; no zero information is used.
