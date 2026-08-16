# Explicit high-shoulder collision exclusion: `lambda >= 10.52`

**Status:** PROVED / unconditional relative to the cited effective Polymath theorem and certified directed-rounding bounds. **RH status: OPEN.**

Let

\[
\lambda=t\log\frac{|x|}{4\pi}.
\]

For every real `x` and every

\[
0<t\le\frac12,
\qquad
\lambda\ge10.52,
\]

one has

\[
\boxed{(H_t(x),H_t'(x))\ne(0,0).}
\]

By evenness it is enough to consider `x>0`.

## 1. Geometry and uniform exponent

Fix `rho=0.1` and put

\[
L=\log\frac{x}{4\pi}.
\]

Since `t<=1/2` and `tL>=10.52`,

\[
L\ge21.04,
\qquad
x\ge4\pi e^{21.04}=1.72490731228124\ldots\times10^{10}.
\]

The fixed-cutoff amplitudes are

\[
a_n=\exp\left(\frac t4(\log n)^2-\sigma\log n\right),
\]

with

\[
\sigma=\frac12+\frac t2A(x),
\qquad
A(x)=\frac L2+\frac14\log(1+x^{-2})-\frac1{1+x^2}.
\]

After enlarging to the `rho`-disk and allowing the local cutoff to vary by at most one, the conservative edge estimate gives

\[
\sigma_* - \frac t4\log n
>rac12+\frac\lambda8-3\cdot10^{-11}
\ge1.81499999997.
\]

The proof deliberately weakens this to

\[
\boxed{a_n\le n^{-1.814}.}
\tag{1}
\]

This is the principal quantitative loss later targeted by the Low-Shoulder program.

## 2. Positive moment bounds

A 512-bit directed-rounding MPFR sum through `M=10^6` plus a positive decreasing integral tail certifies

\[
A_0:=\sum_{n=2}^\infty n^{-1.814}
\le0.861634072184451,
\]

\[
A_1:=\sum_{n=2}^\infty(\log n)n^{-1.814}
\le1.444773803962031.
\]

Therefore

\[
\boxed{S_0=1-A_0\ge0.138365927815549.}
\tag{2}
\]

## 3. Phase and inner derivative

Using the exact real-axis formulas for `alpha` and `alpha'`, for the whole region one has

\[
|\phi_x|>5.25,
\tag{3}
\]

and

\[
d=\sqrt{\sigma_x^2+\tau_x^2}<0.501.
\tag{4}
\]

Hence

\[
|S_x|\le dA_1\le0.501A_1.
\tag{5}
\]

## 4. Effective remainder and cutoff jump

The positive effective-error sums from the Polymath approximation give at the worst endpoint `L=21.04`

\[
e_A+e_B\le2.027674485658184\times10^{-9},
\tag{6}
\]

\[
e_{C,0}\le5.101497806643988\times10^{-9}.
\tag{7}
\]

Across the Cauchy disk the Riemann-Siegel cutoff can change by at most one, and the possible jump term satisfies

\[
E_{\rm jump}\le1.996045576399259\times10^{-8}.
\tag{8}
\]

Thus

\[
\boxed{E_0\le2.708962805629476\times10^{-8}.}
\tag{9}
\]

The symmetric normalization obeys

\[
|B_t/D_t|\le e^{0.026L},
\]

and every normalized error channel is decreasing for `L>=21.04`. Cauchy's estimate yields

\[
\boxed{E_1\le4.681440365960625\times10^{-7}.}
\tag{10}
\]

## 5. PSC contradiction

At a hypothetical multiple zero, the fixed-cutoff approximation must satisfy

\[
|p|\le E_0,
\qquad
|p'|\le E_1.
\]

The phase-slope certificate gives

\[
|p'|\ge2\left(
|\phi_x|\sqrt{S_0^2-(E_0/2)^2}-dA_1
\right).
\]

The 512-bit directed audit gives

\[
|p'|\ge0.0051788904933024764,
\]

whereas (10) forces

\[
|p'|\le0.00000046814403659606247.
\]

Thus the certified contradiction margin is

\[
\boxed{0.0051784223492658803>0.}
\]

The outward-projected values are reproduced at 768 bits.

## 6. Actual-weight boundary regression

As an independent test using the complete finite amplitudes rather than the global `n^{-1.814}` majorant, at

\[
t=0.5,
\qquad
x\in[17249073123,17249073124],
\qquad
\rho=0.1,
\]

both 512-bit and 768-bit runs certify

- `N=37049`,
- `A0 <= 0.20955042280644084`,
- `S0 >= 0.79044957719355913`,
- `A1 <= 0.22794011633558037`,
- `|phi_x| >= 5.2600000000084099`,
- `E0 <= 6.1712779628413665e-9`,
- `E1 <= 1.050380124067183e-7`,
- phase margin `>=8.0875893307159448`.

The enormous gap between this actual-weight margin and the uniform-majorant margin is direct evidence that the dominant loss at `10.52` is the replacement of the quadratic heat weights by the worst-edge power majorant, not interval dependency or the effective remainder.

## 7. Circularity audit

Inputs:

1. unconditional D.H.J. Polymath Theorem 1.3 / Corollary 6.5;
2. elementary formulas for `M_t`, `alpha`, `alpha'`;
3. Schwarz symmetry and Cauchy's estimate;
4. positive-series bounds;
5. directed-rounding MPFR.

Not used: RH; `Lambda<=0`; `Lambda=0`; numerical RH verification; Laguerre-Polya membership of `H_0`; zero-motion formulas requiring prior simplicity.

Therefore every hypothetical positive-time multiple real zero with `0<t<=1/2` must lie in

\[
\boxed{
 t\log\frac{|x|}{4\pi}<10.52.
}
\]

## 8. Structural asymptotic target

Let `p0` be the unique real solution of

\[
\zeta(p_0)=2,
\]

with the certified bracket

\[
1.72864723895<p_0<1.72864723905.
\]

Define

\[
\lambda_*:=4\left(p_0-\frac12\right)
=4.914588956\ldots.
\]

For fixed `n` in the scaling `t->0+`, `lambda=tL` fixed, the actual amplitude formally tends to

\[
n^{-(1/2+\lambda/4)}.
\]

Thus `lambda_*` is the natural tail-mass transition of the **triangle-envelope PSC certificate**. It is **not** currently a proved collision-exclusion threshold and must never be reported as one.
