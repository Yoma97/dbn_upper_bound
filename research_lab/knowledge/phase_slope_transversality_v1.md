# Phase-slope transversality certificate for the de Bruijn-Newman heat flow

**Status:** PROVED certificate relative to the unconditional effective D.H.J. Polymath approximation. **RH status: OPEN.**

This note integrates the independently developed phase-slope collision certificate into the research lab. It does not assume RH, `Lambda <= 0`, numerical RH verification, or a zero-motion ODE in a regime where simplicity is not already known.

## 1. Normalized fixed-cutoff approximation

Fix `t>0`, real `x`, and `rho>0`. On `|z-x|<=rho`, choose a fixed cutoff `N0` not exceeding every local Polymath cutoff and write

\[
H_t=P_{t,N_0}+R_{t,N_0}.
\]

Use the symmetric nonvanishing normalization

\[
D_t(z)=\exp\left(\frac{\log M_t((1-iz)/2)+\log M_t((1+iz)/2)}2\right),
\]

and put `G_t=H_t/D_t`, `p_t=P_{t,N0}/D_t`, `r_t=R_{t,N0}/D_t`.
If

\[
|r_t(x)|\le E_0,
\qquad
\sup_{|z-x|=\rho}|r_t(z)|\le M,
\]

then Cauchy gives

\[
|r_t'(x)|\le E_1:=M/\rho.
\]

Hence a multiple zero forces

\[
|p_t(x)|\le E_0,
\qquad
|p_t'(x)|\le E_1.
\tag{1}
\]

## 2. Phase-amplitude decomposition

For real `x`, put `s=(1-ix)/2` and write

\[
s_*(x,t)=\sigma(x,t)+i\tau(x,t),
\qquad
\phi(x,t)=\Im\log M_t(s).
\]

For the fixed cutoff,

\[
p_t(x)=2\Re(e^{i\phi}S),
\]

where

\[
S=\sum_{n\le N_0}a_ne^{-i\tau\log n},
\qquad
a_n=\exp\left(\frac t4\log^2n-\sigma\log n\right)>0.
\]

Define

\[
A_0=\sum_{n=2}^{N_0}a_n,
\qquad
S_0=1-A_0,
\qquad
A_1=\sum_{n=2}^{N_0}a_n\log n.
\]

Since the `n=1` term equals one,

\[
|S|\ge S_0.
\tag{2}
\]

Differentiating,

\[
S_x=\sum_{n\le N_0}a_n(-\sigma_x-i\tau_x)\log n\,e^{-i\tau\log n}.
\]

With

\[
d=\sqrt{\sigma_x^2+\tau_x^2},
\]

we have

\[
|S_x|\le dA_1.
\tag{3}
\]

Write `e^{i phi}S=X+iY`. Then `p=2X`; under (1), `|X|<=E0/2`. If `S0>E0/2`,

\[
|Y|\ge\sqrt{S_0^2-(E_0/2)^2}.
\tag{4}
\]

Also

\[
\frac{p_x}{2}=-\phi_xY+\Re(e^{i\phi}S_x).
\]

Therefore, whenever `|phi_x|>=Phi0`,

\[
|p_x|\ge
2\left(
\Phi_0\sqrt{S_0^2-(E_0/2)^2}-dA_1
\right).
\tag{5}
\]

## 3. Phase-slope collision criterion (PSC)

A sufficient condition for absence of a multiple real zero at `(t,x)` is

\[
S_0>E_0/2
\]

and

\[
\boxed{
2\left(
\Phi_0\sqrt{S_0^2-(E_0/2)^2}-dA_1
\right)>E_1.
}
\tag{PSC}
\]

This proof deliberately uses no cancellation between the terms of `S`; this makes it stable on wide `x`-boxes, but also creates the structural tail-mass floor analyzed in the Low-Shoulder program.

## 4. Exact real-axis derivative data

For `s=(1-ix)/2`, write `alpha=A+iB` and `alpha'=C+iD`. Then

\[
A=-\frac1{1+x^2}+\frac14\log(1+x^2)-\frac12\log(4\pi),
\]

\[
B=\frac{3x}{1+x^2}-\frac12\arctan x,
\]

\[
C=\frac{7x^2-5}{(1+x^2)^2},
\qquad
D=\frac{x(x^2+5)}{(1+x^2)^2}.
\]

The quantities entering PSC are

\[
\sigma=\frac12+\frac t2A,
\qquad
\sigma_x=\frac t4D,
\qquad
\tau_x=-\frac12\left(1+\frac t2C\right),
\]

and, with `beta_t=alpha+(t/2)alpha alpha'`,

\[
\phi_x=-\frac12\Re\beta_t.
\]

## 5. Wide-box certified regressions

On

\[
t\in[0.3415,0.3416],
\qquad
x\in[10^{10},2\cdot10^{10}],
\qquad
\rho=0.10,
\]

512-bit directed-rounding MPFR gives

- `N0=28209`, `Ntop=39894`,
- `A0 <= 0.63995814245982885`,
- `S0 >= 0.36004185754017121`,
- `A1 <= 1.3869830552573847`,
- `|phi_x| >= 5.1237066707432097`,
- `d <= 0.50000000000000011`,
- `E0 <= 0.031404279189471529`,
- `E1 <= 0.53647480174340556`,
- PSC margin `>=1.7625294856772962>0`.

The same projected bounds are reproduced at 768 bits. A second box `t in [0.3293,0.3294]`, `x in [10^10,2*10^10]` is also certified with margin `>=0.50462474829799575`.

## 6. Logical audit

PSC proves only

\[
(H_t(x),H_t'(x))\ne(0,0)
\]

on the certified region. It does not assert `H_t(x) != 0` or global real-rootedness.

Inputs: unconditional Polymath effective approximation; explicit `M_t` normalization and derivatives; Schwarz symmetry; Cauchy derivative estimate; triangle inequalities and positive amplitude sums; directed-rounding arithmetic.

No RH-equivalent assertion is used as an input.
