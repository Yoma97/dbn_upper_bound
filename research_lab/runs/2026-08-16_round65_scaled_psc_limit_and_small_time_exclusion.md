# Round 65 — Scaled PSC limit and small-time exclusion above the triangle floor

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Closes LS-A2 analytically and gives the non-numerical existence mechanism for LS-A3 on compact lambda intervals above the triangle-envelope floor. Independent proof reconstruction is still required before `REFEREE_VERIFIED` promotion.

---

## 1. Setup

Fix

\[
\rho=0.1.
\]

Let

\[
K=[a,b]\subset(\lambda_*,10.52],
\qquad
\lambda_*=4(p_*-1/2),
\qquad
\zeta(p_*)=2.
\]

Put

\[
L=\frac\lambda t,
\qquad
x=4\pi e^L,
\qquad
p(\lambda)=\frac12+\frac\lambda4.
\]

Use the fixed Cauchy-disk base cutoff

\[
N_-(t,\lambda)
=
\left\lfloor
\sqrt{e^{\lambda/t}-\frac\rho{4\pi}+\frac t{16}}
\right\rfloor.
\]

Let `A0,A1,S0=1-A0` be the exact positive moments of Round 64 with this cutoff.

Define the real-axis PSC quantities exactly as in `phase_slope_transversality_v1.md`:

\[
\Phi=|\phi_x|,
\qquad
 d=\sqrt{\sigma_x^2+\tau_x^2}.
\]

Let `E0` be a rigorous real-axis bound for the normalized fixed-cutoff remainder and `E1` a rigorous derivative bound obtained by Cauchy on `|z-x|=rho`, including any local Riemann--Siegel cutoff jump in the remainder.

The PSC lower margin is

\[
\mathcal T
=
2\left[
\Phi\sqrt{S_0^2-(E_0/2)^2}-dA_1
\right]-E_1,
\tag{65.1}
\]

whenever `S0>E0/2`.

---

## 2. Exact phase-speed limit

On the real axis write

\[
\alpha=A+iB,
\qquad
\alpha'=C+iD,
\]

where

\[
A=\frac L2+\delta_A,
\qquad
-x^{-2}\le\delta_A\le0,
\]

\[
B=\frac{3x}{1+x^2}-\frac12\arctan x,
\]

\[
C=\frac{7x^2-5}{(1+x^2)^2},
\qquad
D=\frac{x(x^2+5)}{(1+x^2)^2}.
\]

For `x` sufficiently large, `A>0,B<0,C>0,D>0`. With

\[
\beta_t=\alpha+\frac t2\alpha\alpha',
\]

we have

\[
\Phi=\frac12\Re\beta_t
=\frac12A+\frac t4(AC-BD).
\tag{65.2}
\]

Since

\[
0<C\le\frac7{x^2},
\qquad
0<D\le\frac1x+\frac5{x^3},
\]

and

\[
|B|\le\frac\pi4+\frac3x,
\]

(65.2) gives the explicit estimate

\[
\left|t\Phi-\frac\lambda4\right|
\le
\frac{t}{2x^2}
+
\frac{t^2}{4}
\left[
\left(\frac L2+\frac1{x^2}\right)\frac7{x^2}
+\left(\frac\pi4+\frac3x\right)
\left(\frac1x+\frac5{x^3}\right)
\right].
\tag{65.3}
\]

Therefore

\[
\boxed{t\Phi\to\lambda/4}
\tag{65.4}
\]

uniformly for `lambda in K`.

---

## 3. Exact amplitude-derivative limit

The real-axis formulas are

\[
\sigma_x=\frac t4D,
\qquad
\tau_x=-\frac12\left(1+\frac t2C\right).
\]

Thus

\[
d
=
\sqrt{\left(\frac t4D\right)^2+
\frac14\left(1+\frac t2C\right)^2}.
\]

Since `C,D>=0`,

\[
\frac12\le d
\le
\frac12+\frac t4(C+D),
\tag{65.5}
\]

where the upper bound uses `sqrt(u^2+v^2)<=u+v` for `u,v>=0`.

Hence

\[
\boxed{d\to1/2}
\tag{65.6}
\]

uniformly on `K`.

Together with Round 64,

\[
A_1\to-\zeta'(p)
\]

uniformly, so

\[
\boxed{t\,dA_1\to0.}
\tag{65.7}
\]

---

## 4. Uniform collapse of the Polymath value error

We now audit Theorem 1.3 / Corollary 6.5 on the upper half of the Cauchy disk

\[
|z-x|\le\rho,
\qquad 0\le\Im z\le\rho.
\]

The lower exponent for the second, worst, positive sum in Polymath (23) has the asymptotic core

\[
\frac{1-\rho}{2}+\frac\lambda8.
\]

Because `a>lambda_*>4.4`, define

\[
m_K:=\frac{1-\rho}{2}+\frac a8-1>0,
\qquad
q_E:=1+\frac{m_K}{2}>1.
\tag{65.8}
\]

Let

\[
x_0(t)=4\pi e^{a/t}.
\]

A direct use of `log(1+u)<=u`, `-log(1-u)<=u/(1-u)`, and Polymath (21) gives the following explicit geometry loss:

\[
\begin{aligned}
g_K(t):={}&
\frac{t\rho}{4(x_0-\rho)}
+
\frac t8\left(\frac\rho{x_0}+\frac t{16}e^{-a/t}\right)\\
&+
\frac{t}{2(x_0-\rho)^2}
\left(1+\frac{4\rho(1+\rho)}{(x_0-\rho)^2}\right).
\end{aligned}
\tag{65.9}
\]

Thus, whenever

\[
g_K(t)\le m_K/2,
\tag{65.10}
\]

all positive summands in (23), including the `n^y` term, are bounded by a constant multiple of `n^{-q_E}`.

More precisely, Polymath (20), (22) give

\[
G_K(t)
:=
\exp\left(
0.02\rho+
\frac{t\rho}{2(x_0-\rho-6)}
\left(\frac b{2t}+1\right)
\right),
\tag{65.11}
\]

so the entire positive prefactor sum is at most

\[
(1+G_K(t))\zeta(q_E).
\tag{65.12}
\]

For the exponential factor in Polymath (23), a uniform upper bound is

\[
h_K(t)
=
\frac{(b+1)^2/16+0.627}{x_0(t)-\rho-6.66}.
\tag{65.13}
\]

Therefore

\[
\boxed{
e_A+e_B
\le
(1+G_K(t))\zeta(q_E)(e^{h_K(t)}-1).
}
\tag{65.14}
\]

Since `x0(t)=4 pi exp(a/t)`, the right side is

\[
O_K(e^{-a/t}).
\tag{65.15}
\]

No RH information occurs in this estimate.

---

## 5. Uniform collapse of e_C,0

Set

\[
\delta_L(t)=\frac{\rho}{x_0(t)-\rho},
\qquad
L_-(t)=\frac a t-\delta_L(t),
\]

and

\[
N_{\min}(t)=
\left\lfloor
\sqrt{e^{a/t}-\frac\rho{4\pi}}
\right\rfloor.
\]

Polymath (24), with `0<=y<=rho`, gives the explicit upper bound

\[
\boxed{
e_{C,0}
\le
\exp\left(
-\frac{L_-}{4}-\frac{tL_-^2}{16}+c_K(t)
\right),
}
\tag{65.16}
\]

where

\[
\begin{aligned}
c_K(t):={}&
\frac{1.24(3^\rho+3^{-\rho})}{N_{\min}(t)-0.125}\\
&+
\frac{3\sqrt{(b/t+1)^2+\pi^2/4}+10.44}
{x_0(t)-\rho-12}.
\end{aligned}
\tag{65.17}
\]

Thus

\[
e_{C,0}
=
O_K\left(
\exp\left[-\frac{a(4+a)}{16t}+o(1/t)\right]
\right).
\tag{65.18}
\]

---

## 6. Cutoff-jump error

Across a disk of real width `2rho`, the Riemann--Siegel argument

\[
\frac{\Re z}{4\pi}+\frac t{16}
\]

changes by

\[
\frac{2\rho}{4\pi}<0.016.
\]

Hence the local integer cutoff can change by at most one.

Under (65.10), the one added positive normalized term satisfies

\[
\boxed{
E_{\rm jump}(t,\lambda)
\le
(1+G_K(t))N_-^{-q_E}.
}
\tag{65.19}
\]

Since, uniformly on `K`,

\[
N_-\ge\frac12e^{a/(2t)}
\]

for small `t`,

\[
E_{\rm jump}
=O_K(e^{-q_Ea/(2t)}).
\tag{65.20}
\]

---

## 7. Value-error conclusion

Define the explicit common upper envelope

\[
\mathcal E_K(t)
:=(1+G_K)\zeta(q_E)(e^{h_K}-1)
+
\exp\left(-\frac{L_-}{4}-\frac{tL_-^2}{16}+c_K\right)
+
(1+G_K)N_{\min}^{-q_E}.
\tag{65.21}
\]

Then the normalized fixed-cutoff real-axis error can be chosen so that

\[
\boxed{E_0\le\mathcal E_K(t),}
\tag{65.22}
\]

and

\[
\boxed{\mathcal E_K(t)\to0}
\tag{65.23}
\]

uniformly on `K`.

---

## 8. Normalization ratio and Cauchy derivative error

The logarithmic derivative of `M_t` is

\[
\frac{M_t'}{M_t}
=\beta_t
=\alpha+\frac t2\alpha\alpha'.
\]

The elementary Polymath bounds for `alpha,alpha'` on the same disk imply, for sufficiently small `t`, the deliberately loose estimate

\[
|\beta_t|\le L+2.
\tag{65.24}
\]

Integrating `log M_t` along the short segment joining the two symmetric normalization points gives

\[
\boxed{
\left|\frac{B_t}{D_t}\right|
\le
R_K(t):=\exp\left(\rho\left(\frac bt+2\right)\right).
}
\tag{65.25}
\]

This is intentionally much weaker than the numerical `exp(0.026L)` bound used at `lambda=10.52`, but it is adequate for the asymptotic proof.

Cauchy's derivative estimate therefore gives

\[
\boxed{
E_1
\le
\frac{R_K(t)}{\rho}\mathcal E_K(t).
}
\tag{65.26}
\]

Each of the three channels in (65.21) still decays exponentially after multiplication by `R_K` because

\[
a-\rho b>0,
\tag{65.27}
\]

\[
\frac{a(4+a)}{16}-\rho b>0,
\tag{65.28}
\]

and

\[
\frac{q_Ea}{2}-\rho b>0
\tag{65.29}
\]

throughout

\[
a>\lambda_*=4.9145\ldots,
\qquad b\le10.52,
\qquad \rho=0.1.
\]

At the worst allowed endpoint these inequalities retain large positive slack.

Hence

\[
\boxed{E_0\to0,\qquad tE_1\to0}
\tag{65.30}
\]

uniformly on every compact `K subset (lambda_*,10.52]`.

---

## 9. Scaled transversality limit

Round 64 gives

\[
A_0\to\zeta(p)-1,
\qquad
A_1\to-\zeta'(p)
\]

uniformly on `K`. Therefore

\[
S_0=1-A_0
\to
2-\zeta(p).
\tag{65.31}
\]

Since `a>lambda_*`, the limiting right side is uniformly positive on `K`. Equations (65.4), (65.6), (65.7), and (65.30) can therefore be inserted into (65.1), yielding

\[
\boxed{
\lim_{t\to0^+}
 t\mathcal T(t,\lambda)
=
\mathcal T_0(\lambda)
:=
\frac\lambda2
\left[
2-\zeta\left(\frac12+\frac\lambda4\right)
\right]
}
\tag{65.32}
\]

uniformly for `lambda in K`.

This is the corrected scaling law. The unscaled `T` generally grows like `1/t` and does not have a finite fixed-lambda limit.

---

## 10. Small-time collision exclusion on compact intervals

For `lambda>lambda_*`,

\[
\mathcal T_0(\lambda)>0.
\]

Indeed `zeta(s)` is strictly decreasing for `s>1`, because

\[
\zeta'(s)=-\sum_{n\ge2}(\log n)n^{-s}<0.
\]

Moreover

\[
\mathcal T_0'(\lambda)
=
\frac12(2-\zeta(p))
-\frac\lambda8\zeta'(p)>0
\]

above `lambda_*`. Thus the minimum on `K=[a,b]` is

\[
M_K
=
\frac a2
\left[
2-\zeta\left(\frac12+\frac a4\right)
\right]>0.
\tag{65.33}
\]

Because every error term above is explicit, one may define `t_K` to be any positive number satisfying simultaneously:

1. Round-64 domination condition (64.1);
2. `g_K(t)<=m_K/2` for `0<t<=t_K`;
3. the explicit Round-64 moment remainders keep `S0>E0/2`;
4. the explicit difference between the left side of (65.32) and `T0(lambda)` is `<M_K/2`.

All four conditions contain only elementary functions and positive Dirichlet-series moments at real arguments `>1`; they are therefore unconditionally computable by directed rounding.

For every such `t_K`,

\[
\boxed{
0<t\le t_K,
\quad
\lambda\in K
\Longrightarrow
\mathcal T(t,\lambda)>0
\Longrightarrow
(H_t(x),H_t'(x))\neq(0,0).
}
\tag{65.34}
\]

This is an analytic small-time collision-exclusion theorem on every compact interval strictly above `lambda_*`.

**Important scope correction:** Round 65 does not by itself claim one uniform `t_K` for all `lambda>=lambda_*+epsilon` without an upper endpoint. In the global program, the compact asymptotic interval is

\[
[\lambda_*+\epsilon,10.52],
\]

and the already proved high-shoulder theorem handles `lambda>=10.52` separately.

---

## 11. Correct interpretation of lambda_*

The result now rigorously shows that `lambda_*` is the zero of the **limiting lower certificate** generated by the unchanged `n=1` triangle envelope:

\[
S_0\to2-\zeta(p).
\]

Thus the precise terminology is:

\[
\boxed{
\lambda_*\text{ is the asymptotic sign floor of the unchanged }n=1
\text{ triangle-envelope PSC in the fixed-lambda }t\to0^+\text{ regime}.}
\]

It is not a universal phase-slope floor and not a collision threshold.

---

## 12. Circularity audit

Inputs:

- unconditional Polymath Theorem 1.3 / Corollary 6.5;
- exact elementary real-axis formulas for `alpha,alpha'`;
- Cauchy's derivative estimate;
- Round-64 positive moment theorem;
- positive real Dirichlet series at arguments `>1`.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- all-real zeros of `H_0`;
- finite-height RH verification;
- zero-spacing assumptions;
- GUE/pair correlation;
- Rodgers--Tao estimates proved under a negative-Lambda contradiction setup;
- Laguerre--Polya membership.

No dependency edge assumes the desired no-collision conclusion.

---

## 13. Adversarial audit / limitations

1. `a downarrow lambda_*`: `M_K` tends to zero. The theorem gives no uniform quantitative `t_K` at the endpoint itself.
2. `a<=lambda_*`: the proof intentionally stops; the triangle lower bound loses asymptotic sign.
3. `lambda>10.52`: not needed here; the independent high-shoulder theorem already closes it.
4. The deliberately loose normalization bound (65.25) is adequate only because the Polymath remainder channels have much stronger exponential decay. Improving it changes constants, not the mechanism.
5. The theorem does not cover the bounded spatial core where `lambda` is nonpositive or not a useful scale.
6. `t_K` is explicit/computable through displayed inequalities, but no optimized decimal value is claimed in this round. Producing a certified useful decimal `t_epsilon` is the next numerical-analytic task.

---

## 14. New state of the Low-Shoulder program

- LS-A1 exact-weight moment collapse: **INTERNALLY_PROVED** (Round 64).
- LS-A2 scaled PSC limit: **INTERNALLY_PROVED** (this round).
- LS-A3 qualitative small-time exclusion on `[lambda_*+epsilon,10.52]`: **INTERNALLY_PROVED**, with explicit computable but not yet optimized `t_epsilon`.
- Next task: calculate and certify a practical `t_epsilon`, then construct the compact 512/768-bit bridge from `t_epsilon` to `1/2`.
- Below `lambda_*+epsilon`: still OPEN and requires a changed certificate.

RH remains OPEN.
