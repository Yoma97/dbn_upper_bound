# Round 70 addendum — explicit audit of every `10^-4` geometry allowance

**Date:** 2026-08-16  
**Status:** INTERNALLY_PROVED supporting lemma for Round 70.  
**RH status:** OPEN.

Round 70 deliberately used the common allowance `10^-4` for several corrections. This addendum proves that allowance channel by channel.

Throughout

\[
0<t\le0.01,
\qquad
7.10\le\lambda\le10.52,
\qquad
L=\lambda/t\ge710,
\qquad
\rho=0.1.
\]

---

## 1. Elementary exponential floor

The rational Taylor partial sum

\[
\sum_{k=0}^{11}\frac{7^k}{k!}
=
\frac{2959911103}{2851200}
>1000
\]

proves

\[
e^7>1000.
\]

Hence

\[
e^{700}>10^{300}
\]

and, since `4pi>12`,

\[
x_c=4\pi e^L>12\cdot10^{300}.
\]

For every disk point `|z-x_c|<=0.1`, its real part `x'` satisfies

\[
\boxed{x'>10^{301}.}
\tag{G1}
\]

---

## 2. Logarithmic disk displacement

Put

\[
u=\rho/x_c<10^{-302}.
\]

Then

\[
\log\frac{x_c+\rho}{x_c}
=\log(1+u)\le u<10^{-302},
\]

and

\[
\log\frac{x_c}{x_c-\rho}
=-\log(1-u)
\le\frac{u}{1-u}<2\cdot10^{-302}.
\]

Thus for every disk point

\[
\boxed{
\left|
\log\frac{x'}{4\pi}-L
\right|<2\cdot10^{-302}.
}
\tag{G2}
\]

After multiplication by `t<=0.01`, the induced change in `tL` is below `2e-304`.

---

## 3. Real-axis `sigma` correction

Round 64 gives exactly

\[
\sigma
=
\frac12+rac\lambda4+\eta,
\qquad
-\frac{t}{2x_c^2}\le\eta\le0.
\]

By (G1),

\[
|\eta|<\frac{0.01}{2\cdot10^{602}}
<10^{-603}.
\]

Therefore the `10^-4` loss in Round 70 equation (70.3) is conservative by more than 599 decimal orders:

\[
\boxed{-10^{-4}<\eta\le0.}
\tag{G3}
\]

---

## 4. Moving-cutoff logarithm correction

For every real summand before the cutoff,

\[
\log n
\le
\frac L2+rac12\log\left(1+rac t{16}e^{-L}\right).
\]

Thus

\[
0\le
\frac t8\log\left(1+rac t{16}e^{-L}\right)
\le
\frac{t^2}{128}e^{-L}.
\]

From `e^{-L}<10^{-300}` and `t<=0.01`,

\[
\boxed{
\frac{t^2}{128}e^{-L}<10^{-306}<10^{-4}.
}
\tag{G4}
\]

The same bound, enlarged by the disk displacement (G2), applies to the local complex cutoff.

---

## 5. `s_*` lower-bound correction

Polymath (21) contains

\[
R_s
=
\frac{t}{2(x')^2}
\left(
1-3y+rac{4y(1+y)}{(x')^2}
\right)_+.
\]

For `0<=y<=0.1`,

\[
R_s
\le
\frac{0.01}{2\cdot10^{602}}
\left(1+\frac{0.44}{10^{602}}\right)
<10^{-603}.
\]

Hence

\[
\boxed{R_s<10^{-603}<10^{-4}.}
\tag{G5}
\]

Combining (G2), (G4), (G5), the total power loss used in the Round-70 effective exponents is far below `2e-4`.

---

## 6. `kappa log N`

Polymath (22) gives

\[
|\kappa|
\le
\frac{t y}{2(x'-6)}
\le
\frac{0.001}{2(x'-6)}.
\]

Also

\[
\log N
\le
\frac12\log\left(
\frac{x'}{4\pi}+rac t{16}
\right)
\le
\frac12(L'+1)
\]

in the present enormous-`x` range.

Therefore

\[
|\kappa|\log N
\le
\frac{0.001(L'+1)}{4(x'-6)}.
\]

Since `x'=4pi e^{L'}` and `(L'+1)e^{-L'}` is decreasing for `L'>0`, its maximum occurs at the smallest possible `L'`, which by (G2) exceeds `709`.

Using `e^{700}>10^300`,

\[
\boxed{|\kappa|\log N<10^{-298}.}
\tag{G6}
\]

Thus

\[
N^{|\kappa|}<e^{10^{-298}}.
\]

Together with `e^{0.02y}<=e^{0.002}`, this rigorously implies the Round-70 convenient bound

\[
\boxed{|\gamma|N^{|\kappa|}<1.004.}
\tag{G7}
\]

---

## 7. Consequence for the effective powers

For the first positive Polymath sum, the exact asymptotic edge power at `lambda=7.10` is

\[
\frac12+\frac{7.10}{8}=1.3875.
\]

The combined corrections (G2)--(G6) are less than `2e-4`, so

\[
q_1>1.3873>1.387.
\]

For the second sum after the `n^y` multiplier,

\[
\frac{1-0.1}{2}+rac{7.10}{8}=1.3375,
\]

and hence

\[
q_2>1.3373>1.337.
\]

Thus the Round-70 powers `1.387` and `1.337` are rigorously safe.

---

## 8. Audit conclusion

Every use of a `10^-4` geometry allowance in Round 70 is now replaced by an explicit proved channel bound. The largest actual analytic correction in this small-time region is not remotely near `10^-4`; the allowance was chosen only to keep the proof readable.

No circular input is used in this audit.
