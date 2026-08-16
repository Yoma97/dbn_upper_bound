# Round 65 addendum — hostile audit of the symmetric normalization ratio

**Status:** INTERNALLY_PROVED correction/clarification.  
**RH status:** OPEN.

This note corrects one potentially misleading sentence in Round 65. The bound used there remains conservative and valid, but the geometric comparison must be stated correctly.

For

\[
z=x+iy,
\qquad
s_+(z)=\frac{1+y-ix}{2},
\qquad
s_-(z)=\frac{1-y+ix}{2},
\]

the symmetric normalization is

\[
D_t(z)=
\exp\left(\frac{\log M_t(s_+)+\log M_t(s_-)}2\right).
\]

The `B` term is normalized by `M_t(s_+)`, so

\[
\left|\frac{B_t}{D_t}\right|
=
\exp\left[
\frac12\left(
\Re\log M_t(s_+)-\Re\log M_t(s_-)
\right)
\right].
\tag{A1}
\]

One must **not** compare `s_+` directly with `s_-`; those points are separated by the large imaginary displacement `x`.

By Schwarz symmetry of `M_t`,

\[
\Re\log M_t(s_-)
=
\Re\log M_t(\overline{s_-})
\]

on the branch used by the certificate, where

\[
\overline{s_-}=\frac{1-y-ix}{2}.
\]

Now `s_+` and `overline{s_-}` differ only by the real displacement `y`. Hence, writing

\[
\beta_t(s)=\frac{M_t'(s)}{M_t(s)},
\]

the fundamental theorem of calculus gives

\[
\left|
\Re\log M_t(s_+)-
\Re\log M_t(\overline{s_-})
\right|
\le
|y|\sup_{I_{x,y}}|\beta_t|,
\]

where `I_{x,y}` is the short horizontal segment joining those two points. Therefore

\[
\boxed{
\left|\frac{B_t}{D_t}\right|
\le
\exp\left(
\frac{|y|}{2}\sup_{I_{x,y}}|\beta_t|
\right).
}
\tag{A2}
\]

The explicit Polymath bounds for `alpha` and `alpha'`, together with

\[
\beta_t=\alpha+\frac t2\alpha\alpha',
\]

give, throughout the small-time fixed-lambda Cauchy rectangles used in Round 65,

\[
\sup|\beta_t|\le L+2
\]

for sufficiently small `t`. Thus the sharp-enough consequence is

\[
\left|\frac{B_t}{D_t}\right|
\le
\exp\left(\frac\rho2(L+2)\right).
\tag{A3}
\]

Round 65 deliberately used the looser envelope

\[
R_K(t)=\exp\left(\rho(b/t+2)\right),
\]

which is larger than (A3), so none of its exponential-decay conclusions are weakened by this correction.

The corresponding decay checks in Round 65 were made against the larger exponent `rho*b/t`; hence they remain valid a fortiori.

**Circularity:** only the explicit formula for `M_t`, Schwarz symmetry, the fundamental theorem of calculus, and unconditional Polymath bounds are used. No zero information enters.
