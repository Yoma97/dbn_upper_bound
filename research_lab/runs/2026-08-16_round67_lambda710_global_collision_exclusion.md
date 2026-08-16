# Round 67 — Certified global collision exclusion for `lambda >= 7.10`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED + 512/768-bit directed-rounding certification.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Lowers the project collision-exclusion threshold from `10.52` to `7.10` by combining the phase-slope certificate with a true-weight finite-head / optimized-tail enclosure. This is not a proof of RH and does not address `lambda<7.10`.

---

## 1. Statement

Let

\[
\lambda=t\log\frac{|x|}{4\pi}.
\]

For every real `x` and

\[
0<t\le\frac12,
\qquad
\lambda\ge7.10,
\]

one has

\[
\boxed{(H_t(x),H_t'(x))\ne(0,0).}
\tag{67.1}
\]

The interval `7.10<=lambda<=10.52` is certified in this round. The already established high-shoulder theorem covers `lambda>=10.52`.

---

## 2. Source inputs

Only the following inputs are used.

1. The unconditional effective D.H.J. Polymath Riemann--Siegel approximation (Theorem 1.3 / Corollary 6.5 in the project source registry), including its explicit positive error channels `e_A,e_B,e_C0`.
2. The phase-slope transversality certificate (PSC): at a hypothetical multiple zero, the normalized fixed-cutoff main term satisfies `|p|<=E0`, `|p'|<=E1`, while
   \[
   |p'|\ge
   2\left(
   \Phi_0\sqrt{S_0^2-(E_0/2)^2}-dA_1
   \right).
   \]
3. Elementary monotonicity/convexity and the decreasing integral test.
4. Directed-rounding MPFR at 512 and 768 bits.

No RH, `Lambda<=0`, zero-spacing estimate, pair correlation, Laguerre positivity, finite-height RH verification, or Rodgers--Tao negative-time estimate is used.

---

## 3. Uniform phase and derivative bounds in the new region

By evenness take `x>0`. If `lambda>=7.10` and `t<=1/2`, then

\[
L:=\log\frac{x}{4\pi}\ge14.2,
\qquad
x\ge4\pi e^{14.2}>1.8458\times10^7.
\]

On the real axis write `alpha=A+iB`, `alpha'=C+iD`, with the exact formulas already recorded in the PSC note. We have

\[
A=\frac L2+\frac14\log(1+x^{-2})-\frac1{1+x^2}
\ge \frac L2-x^{-2}.
\]

For this range `A>0`, `B<0`, `C>0`, `D>0`. Hence

\[
\Re\left(\alpha+\frac t2\alpha\alpha'\right)
=A+\frac t2(AC-BD)>A.
\]

Therefore

\[
\boxed{
\Phi:=|\phi_x|
>\frac L4-\frac1{2x^2}
>\frac L4-10^{-6}.
}
\tag{67.2}
\]

Also

\[
C<\frac7{x^2},
\qquad
D<\frac1x+\frac5{x^3},
\]

and

\[
d=\sqrt{(tD/4)^2+\frac14(1+tC/2)^2}
\le \frac12+\frac t4(C+D)
<0.501.
\]

Thus every certification box may use

\[
\boxed{
\Phi_0=\frac{\lambda_a}{4t_b}-10^{-6},
\qquad d\le0.501.
}
\tag{67.3}
\]

---

## 4. Global effective-error envelope for `lambda>=7.10`

Set `rho=0.1`. The worst geometric point for the positive error envelopes is

\[
L=14.2,\qquad t=1/2,\qquad \lambda=7.10.
\]

For every term up to the local Riemann--Siegel cutoff, the same cutoff-edge calculation as in the high-shoulder proof gives, with generous slack,

\[
\frac{b_n^t}{n^{\Re s_*}}
\le n^{-1.386}.
\]

After the `n^y` factor in the second positive error sum we may use exponent `1.286>1`. The elementary bound `zeta(s)<=1+1/(s-1)` gives the finite constant

\[
Z_*\le8.100666582122541.
\]

At `L=14.2`, the corrected directed-rounding audit gives

\[
e_A+e_B
\le1.657861696252715\times10^{-6},
\]

\[
e_{C,0}
\le5.279579078353566\times10^{-5},
\]

and the possible one-term cutoff bridge gives

\[
E_{\rm jump}
\le1.620413512996852\times10^{-4}.
\]

Consequently

\[
\boxed{
E_0<3\times10^{-4}.
}
\tag{67.4}
\]

The symmetric normalization is handled by Schwarz symmetry and a short horizontal segment, as in the Round-65 normalization audit. For `L>=14.2`, the explicit formula

\[
\alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}
\]

and its derivative give on the `rho`-segment

\[
\sup|\beta_t(s)|<0.52L,
\qquad
\beta_t=\alpha+\frac t2\alpha\alpha'.
\]

Hence

\[
\left|\frac{B_t}{D_t}\right|
\le e^{0.026L}.
\tag{67.5}
\]

The normalized envelopes are decreasing for `L>=14.2`:

- for `e_A+e_B`, the elementary majorant has logarithmic derivative at most `0.026+2/L-1<0`;
- for `e_C0`, the net linear decay coefficient is at least
  \[
  \frac14+\frac{7.10}{16}-0.026=0.66775>0,
  \]
  while the explicit positive correction terms decrease with `L`;
- for the slowest cutoff-jump term the net rate is at least
  \[
  \frac{1.286}{2}-0.026>0.
  \]

Thus the endpoint audit controls the full region. Cauchy gives

\[
E_1\le \frac{E_0e^{0.026L}}{\rho}
<0.003132<0.005.
\]

We deliberately certify with the padded global constants

\[
\boxed{E_0\le3\times10^{-4},\qquad E_1\le5\times10^{-3}.}
\tag{67.6}
\]

The 512- and 768-bit error-audit outputs agree outward.

---

## 5. Boxwise true-weight envelope

Let a certification box be

\[
t\in(t_a,t_b],
\qquad
\lambda\in[\lambda_a,\lambda_b],
\]

with `lambda_a>=7.10`. Put

\[
u=\log n,\qquad K=128.
\]

The exact real-axis amplitude is

\[
a_n=\exp\left(\frac t4u^2-\sigma u\right),
\qquad
\sigma\ge\frac12+\frac\lambda4-\varepsilon_\sigma,
\]

and in the entire certified region

\[
\varepsilon_\sigma=10^{-10}
\]

is vastly larger than the exact correction `t/(2x^2)`.

### 5.1 Cutoff constraint

If `n<=N`, then

\[
n^2\le e^{\lambda/t}+\frac t{16}.
\]

For `n>=K=128` and `t<=1/2`,

\[
\lambda
\ge2tu-t\delta_K,
\qquad
\delta_K=-\log\left(1-\frac1{32K^2}\right).
\]

Since `t delta_K<10^{-6}`, we use the padded constant

\[
\delta=2\times10^{-6}.
\]

Thus

\[
\lambda\ge\max(\lambda_a,2tu)-\delta.
\tag{67.7}
\]

Define

\[
\eta=\frac\delta4+\varepsilon_\sigma.
\]

Then every tail exponent is bounded by

\[
\frac t4u^2-
\left(
\frac12+\frac14\max(\lambda_a,2tu)-\eta
\right)u.
\tag{67.8}
\]

### 5.2 Optimization over the time box

Put

\[
u_1=\frac{\lambda_a}{2t_b}.
\]

If `t_a>0`, also put

\[
u_2=\frac{\lambda_a}{2t_a},
\qquad
u_3=\frac{\lambda_b+\delta}{2t_a}.
\]

Optimizing (67.8) over `t in [t_a,t_b]` gives the continuous upper envelope

\[
h_1(u)=\frac{t_b}{4}u^2-
\left(\frac12+\frac{\lambda_a}{4}-\eta\right)u,
\qquad u\le u_1,
\]

\[
h_2(u)=-\left(\frac12+\frac{\lambda_a}{8}-\eta\right)u,
\qquad u_1\le u\le u_2,
\]

and, when `t_a>0`,

\[
h_3(u)=-\frac12u-\frac{t_a}{4}u^2+\eta u,
\qquad u_2\le u\le u_3.
\]

For the first time box `t_a=0`, the `h_2` branch continues to infinity.

The implementation takes an **upper enclosure** of `u_1`, so the switch `h_1 -> h_2` is downward. It likewise delays the second switch to an upper enclosure of `u_2`. Consequently the implemented weight envelope remains non-increasing.

For the logarithmic moment, throughout `u>=log 128`,

\[
h_j'(u)+\frac1u<0,
\]

because the weakest possible weight slope is `-1/2+eta` whereas `1/log128<0.207`. Hence the same decreasing-integral argument applies to `a_n log n`.

### 5.3 Integral evaluation

For the first branch the counting-measure exponent

\[
g_1(u)=h_1(u)+u
\]

is convex. Therefore its secant chord on the branch lies above it, giving a closed-form integral in terms of `exprel` and its first moment. Both functions are evaluated by directed rounding, with explicit near-zero branches.

The second branch is a pure exponential and is integrated exactly.

For the third branch

\[
g_3(u)=\left(\frac12+\eta\right)u-\frac{t_a}{4}u^2
\]

is already decreasing at `u_2`; the verifier uses the simpler rigorous bounds

\[
\int_{u_2}^{u_3}e^{g_3(u)}du
\le e^{g_3(u_2)}(u_3-u_2),
\]

\[
\int_{u_2}^{u_3}u e^{g_3(u)}du
\le e^{g_3(u_2)}
\left[u_2D+\frac{D^2}{2}\right],
\quad D=u_3-u_2.
\]

The finite head `2<=n<=128` is evaluated directly with upward amplitude rounding.

This produces certified upper bounds for `A0,A1` on the whole box without a computation proportional to the astronomical cutoff.

---

## 6. Complete certified cover

The rectangle

\[
0<t\le0.5,
\qquad
7.10\le\lambda\le10.52
\]

is partitioned into

- `100` time boxes of width `0.005`;
- `171` lambda boxes of width `0.02`.

Total:

\[
\boxed{17100\text{ boxes}.}
\]

On every box the verifier computes directed upper bounds for `A0,A1`, the lower phase bound (67.3), and applies PSC with the padded errors (67.6).

At 512 bits:

```text
boxes=17100 fail=0
minimum_margin_lower=0.007822115980988701
worst_t=[0.495000,0.500000] lambda=[7.100000,7.120000]
worst_A0_upper=0.74864794909420085
worst_A1_upper=1.7682401446754208
GRID_RESULT pass=1
```

An independent 768-bit rerun produces the same outward-projected values and again `fail=0`.

Therefore PSC holds on every box, proving (67.1) on `7.10<=lambda<=10.52`. The previous theorem covers `lambda>=10.52`.

---

## 7. Reproducibility artifacts

Canonical files:

- `research_lab/certificates/low_shoulder/convex_tail_psc_mpfr.c`
- `research_lab/certificates/low_shoulder/convex_tail_psc_grid_512.txt`
- `research_lab/certificates/low_shoulder/convex_tail_psc_grid_768.txt`
- `research_lab/certificates/low_shoulder/lambda710_error_audit.c`
- `research_lab/certificates/low_shoulder/lambda710_error_512.txt`
- `research_lab/certificates/low_shoulder/lambda710_error_768.txt`

Local SHA256 before commit:

- convex-tail source: `fb6bcc699653c9772e14b0877f5f7f1d3c6b17199d49dcc5784dfd2bc91a9c90`
- 512 grid output: `d9843ea8d10e446b5c704939d87a192c136b6b812bd2d0f3a187decc6013d40f`
- 768 grid output: `01be5e8212dd410318cb6b1e54c7bbad4be097da8e58825a6a966dc4dd88b90b`
- error source: `3fef4b8bb91b43ac2219f1b403d8e01ac693c36319488b070fd11765d54ddbb9`
- 512 error output: `834f44d10dc823db6cf6f42f4abab6105d8611399af8da506960ad01e5190d03`
- 768 error output: `91243b9f41b51ec013b64582a2951c0665310c4eeb7e401d710c1c95b9be8ffb`

Compile the same sources with `PREC=512` and `PREC=768` against MPFR/GMP.

---

## 8. Circularity audit

The conclusion is a local no-common-zero statement only in a specified `(t,lambda)` region.

Not used:

- RH or any equivalent criterion;
- `Lambda<=0` or `Lambda=0`;
- global real-rootedness of `H_t`;
- finite-height RH verification;
- zero-spacing lower bounds;
- GUE/pair correlation;
- generalized Laguerre positivity;
- Rodgers--Tao estimates whose derivation assumes `Lambda<0`.

The Polymath input is unconditional and positive-time. The new moment envelope is elementary and independent of the desired conclusion.

---

## 9. Status update

Within the project proof system, the certified collision-exclusion constant is now

\[
\boxed{C_{\rm certified}=7.10.}
\]

The asymptotic triangle-envelope floor remains

\[
\lambda_*=4.914588956\ldots,
\]

but it is **not** a certified collision-exclusion constant.

The next task is not to stop at `7.10`: rerun the same architecture with a variable lower lambda and locate the smallest threshold that survives, while preserving a strictly positive audited margin. When this architecture approaches its finite-time or asymptotic floor, the program must switch to a stronger joint certificate rather than hide failure with finer boxes.
