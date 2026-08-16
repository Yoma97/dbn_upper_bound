# Round 82 — Complex zeta envelope and the singular-wedge transition at `lambda = 4`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED, pending independent reconstruction.  
**Strict-program admissibility:** PASSED current direct/transitive audit.  
**Referee status:** PENDING.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Main theorem

Put

\[
L=\log\frac{x}{4\pi},\qquad \lambda=tL,\qquad x=4\pi e^{\lambda/t}.
\]

Let

\[
K=[a,b]\subset(4,\infty).
\]

Then there exists `t_K>0` such that

\[
\boxed{
0<t\le t_K,\qquad \lambda\in K
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\tag{82.1}
\]

Consequently, after splicing with the current strict global shoulder theorem `lambda>=6.50`, for every `epsilon>0` there is `t_epsilon>0` such that

\[
\boxed{
0<t\le t_\varepsilon,
\qquad
\lambda\ge4+\varepsilon
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\tag{82.2}
\]

This is a strict-track result: no finite-height RH verification, no upper bound on `Lambda`, and no zero-statistics input are used.

The number `4` is **not claimed to be a collision threshold**. It is the transition at which the present absolute perturbation of the moving heat-weighted Dirichlet polynomial by an absolutely convergent zeta series ceases to be uniformly small.

---

## 2. Why the previous `lambda_* = 4.914588956...` floor was artificial

Rounds 64--65 used

\[
|S|\ge1-A_0,
\]

where

\[
S=\sum_{n\le N}a_ne^{-i\tau\log n},
\qquad
A_0=\sum_{n=2}^N a_n.
\]

In the fixed-lambda limit,

\[
A_0\to\zeta\left(\frac12+\frac\lambda4\right)-1,
\]

so that this triangle lower bound has limiting sign

\[
1-A_0\to2-\zeta\left(\frac12+\frac\lambda4\right),
\]

whose zero is the old

\[
\lambda_*\approx4.914588956.
\]

Round 82 does **not** lower this triangle floor numerically. It removes that triangle compression altogether by retaining the oscillatory Dirichlet sum as a complex object.

---

## 3. Exact complex heat-weighted sum

On the real axis use the notation of the PSC note:

\[
s_*=\sigma+i\tau,
\qquad
S_t=\sum_{n\le N}a_ne^{-i\tau\log n},
\]

\[
a_n=
\exp\left(\frac t4\log^2 n-\sigma\log n\right).
\]

Let

\[
p=p(\lambda):=\frac12+\frac\lambda4.
\]

Round 64 proves the exact decomposition

\[
\sigma=p+\eta,
\qquad
-\frac{t}{2x^2}\le\eta\le0,
\]

and hence

\[
a_n=n^{-p}e^{r_n},
\qquad
r_n=\frac t4\log^2n-\eta\log n\ge0.
\]

Therefore

\[
S_t
=\sum_{n\le N}n^{-p-i\tau}e^{r_n}.
\tag{82.3}
\]

The key point is that the proof of Round 64 bounds **absolute values** of the perturbations. It therefore extends verbatim from the positive moment `A0` to the complex sum `S_t`; no phase information is discarded.

---

## 4. Uniform zeta approximation for `lambda>4`

Set

\[
q=1+\frac{a-4}{16}>1.
\]

For the fixed cutoff

\[
N_-(t,\lambda;\rho)
=
\left\lfloor
\sqrt{e^{\lambda/t}-\frac\rho{4\pi}+\frac t{16}}
\right\rfloor,
\]

the same estimates as Round 64 give, uniformly in the real phase parameter `tau`,

\[
\boxed{
\left|
S_t-\zeta(p+i\tau)
\right|
\le R_0(t,\lambda),
}
\tag{82.4}
\]

where

\[
R_0(t,\lambda)
=
\frac t4 Z_2(q)
+\frac{t}{2x^2}Z_1(q)
+\frac{N_-^{1-p}}{p-1}.
\tag{82.5}
\]

Here

\[
Z_k(q)=\sum_{n=2}^{\infty}(\log n)^k n^{-q}.
\]

Indeed

\[
S_t-\zeta(p+i\tau)
=
\sum_{n\le N_-}n^{-p-i\tau}(e^{r_n}-1)
-
\sum_{n>N_-}n^{-p-i\tau},
\]

and taking absolute values gives exactly the Round-64 majorants.

Thus

\[
\boxed{
\sup_{\lambda\in K}\sup_{\tau\in\mathbb R}
|S_t-\zeta(p+i\tau)|\to0
}
\tag{82.6}
\]

as `t->0+`.

This uniformity in `tau` is essential: in the singular wedge `tau` itself is of order `-x/2` and has no finite limit.

Similarly, if

\[
T_t:=\sum_{n\le N_-}a_n\log n\,e^{-i\tau\log n},
\]

then

\[
\boxed{
|T_t+\zeta'(p+i\tau)|\le R_1(t,\lambda),
}
\tag{82.7}
\]

with the Round-64 logarithmic-moment remainder

\[
R_1
=
\frac t4 Z_3(q)
+\frac{t}{2x^2}Z_2(q)
+N_-^{1-p}
\left(
\frac{\log N_-}{p-1}
+\frac1{(p-1)^2}
\right).
\tag{82.8}
\]

Only the boundedness of `T_t` will be needed below.

---

## 5. An unconditional lower bound for the zeta envelope

For `p>1`, the Euler product converges absolutely and

\[
|\zeta(p+i\tau)|
=
\prod_{\ell\ \mathrm{prime}}
|1-\ell^{-p-i\tau}|^{-1}.
\]

Since

\[
|1-\ell^{-p-i\tau}|\le1+\ell^{-p},
\]

we obtain

\[
|\zeta(p+i\tau)|
\ge
\prod_\ell(1+\ell^{-p})^{-1}
=
\frac{\zeta(2p)}{\zeta(p)}.
\tag{82.9}
\]

In particular, if

\[
p_a=\frac12+\frac a4>\frac32,
\]

then for every `lambda in K` and every real `tau`,

\[
\boxed{
|\zeta(p+i\tau)|\ge m_K,
\qquad
m_K:=\frac1{\zeta(p_a)}>0.
}
\tag{82.10}
\]

The last bound is deliberately weakened: `zeta(2p)>1` and `zeta(p)<=zeta(p_a)`.

Combining (82.4) and (82.10),

\[
\boxed{|S_t|\ge m_K-R_0(t,\lambda).}
\tag{82.11}
\]

No information about zeros of zeta is used; (82.9) lives entirely in the classical half-plane of absolute convergence.

---

## 6. The Cauchy-radius correction near `lambda=4`

Round 65 fixed `rho=0.1`. That choice is insufficient to pass all the way down to arbitrary `a>4`, because on the upper half of the Cauchy disk the worst Polymath positive sum has asymptotic exponent

\[
\frac{1-\rho}{2}+\frac a8.
\]

To dominate it by a summable power we need

\[
\frac{1-\rho}{2}+\frac a8>1,
\quad\text{i.e.}\quad
\rho<\frac{a-4}{4}.
\tag{82.12}
\]

Choose once and for all for `K=[a,b]`

\[
\boxed{
\rho_K
=
\min\left\{
\frac1{10},
\frac{a-4}{8},
\frac{a}{4b}
\right\}.
}
\tag{82.13}
\]

Then

\[
\mu_K
:=
\frac{1-\rho_K}{2}+\frac a8-1
\ge
\frac{a-4}{16}>0.
\tag{82.14}
\]

Set

\[
q_E=1+\frac{\mu_K}{2}>1.
\]

The derivation of Round 65, Sections 4--8, is symbolic in the disk radius and therefore applies with `rho_K` in place of `0.1`. The local cutoff can still change by at most one because `rho_K<=0.1`.

The value remainder therefore obeys

\[
E_0\to0
\]

uniformly on `K`.

For the Cauchy derivative error, the normalization ratio is bounded by

\[
R_K(t)
\le
\exp\left(\rho_K\left(\frac bt+2\right)\right).
\]

The three exponential channels in Round 65 remain decaying because (82.13) gives

\[
a-\rho_K b\ge\frac{3a}{4}>0,
\tag{82.15}
\]

\[
\frac{a(4+a)}{16}-\rho_Kb
\ge
\frac{a^2}{16}>0,
\tag{82.16}
\]

and

\[
\frac{q_Ea}{2}-\rho_Kb
\ge
\frac a4>0.
\tag{82.17}
\]

Hence the normalized fixed-cutoff remainder can be chosen so that

\[
\boxed{
E_0\to0,
\qquad
 tE_1\to0
}
\tag{82.18}
\]

uniformly on `K`.

This radius adaptation is mandatory. Keeping `rho=0.1` while claiming all `lambda>4` would leave an actual gap for `4<lambda<=4.4`.

---

## 7. Collision-conditioned transversality without the triangle floor

As in the PSC note, write

\[
p_t(x)=2\Re(e^{i\phi}S_t)
\]

for the normalized fixed-cutoff approximation, and put

\[
e^{i\phi}S_t=X+iY.
\]

At a hypothetical multiple zero of `H_t`, the normalized remainder bounds force

\[
|X|\le\frac{E_0}{2},
\qquad
|p_t'(x)|\le E_1.
\tag{82.19}
\]

By (82.11),

\[
|Y|
\ge
\sqrt{
(m_K-R_0)^2-(E_0/2)^2
}
\tag{82.20}
\]

once the radicand is positive.

Differentiating the fixed-cutoff sum gives

\[
S_x
=-(\sigma_x+i\tau_x)T_t.
\tag{82.21}
\]

Let

\[
\Phi=|\phi_x|,
\qquad
d=\sqrt{\sigma_x^2+\tau_x^2}.
\]

Then

\[
\frac{p_t'}2
=-\phi_xY+\Re(e^{i\phi}S_x),
\]

and therefore

\[
|p_t'|
\ge
2\left[
\Phi\sqrt{(m_K-R_0)^2-(E_0/2)^2}
-d|T_t|
\right].
\tag{82.22}
\]

The exact real-axis formulas from Round 65 give

\[
\boxed{t\Phi\to\lambda/4}
\tag{82.23}
\]

uniformly on `K`, while

\[
d\to\frac12.
\]

Moreover (82.7), or simply the positive logarithmic-moment bound of Round 64, gives

\[
\sup_{\lambda\in K}|T_t|=O_K(1).
\]

Thus

\[
\boxed{td|T_t|\to0.}
\tag{82.24}
\]

Combining (82.18), (82.20), (82.22), (82.23), and (82.24),

\[
\liminf_{t\to0^+}
\inf_{\lambda\in K}
 t\left(
2\left[
\Phi\sqrt{(m_K-R_0)^2-(E_0/2)^2}
-d|T_t|
\right]-E_1
\right)
\ge
\boxed{\frac{a\,m_K}{2}>0}.
\tag{82.25}
\]

Therefore the bracketed collision lower bound is strictly positive for all sufficiently small `t`, uniformly on `K`, proving (82.1).

---

## 8. Splicing to the current strict shoulder theorem

Round 81 already proves on the strict track

\[
0<t\le1/2,
\qquad
\lambda\ge6.50
\Longrightarrow
(H_t,H_t')\ne(0,0).
\]

Fix `epsilon>0`.

If `4+epsilon<6.50`, apply Theorem (82.1) to

\[
K=[4+\varepsilon,6.50].
\]

For sufficiently small `t` this removes that entire compact lambda interval, while Round 81 removes `lambda>=6.50` for all `t<=1/2`. This proves (82.2).

If `4+epsilon>=6.50`, Round 81 alone suffices.

---

## 9. Why `lambda=4` is the natural absolute-mass transition

Write

\[
u=t\log n.
\]

Ignoring exponentially tiny Archimedean corrections, the heat amplitude is

\[
a_n
\approx
\exp\left[
\frac1t\left(
\frac{u^2}{4}
-\left(\frac12+\frac\lambda4\right)u
\right)
\right].
\]

When the discrete sum is approximated on exponential scale, the density of integers contributes `e^{u/t}`. The absolute-mass rate is therefore

\[
F_\lambda(u)
=
\frac{u^2}{4}
+\left(\frac12-\frac\lambda4\right)u,
\qquad
0\le u\le\frac\lambda2.
\tag{82.26}
\]

At the moving cutoff,

\[
F_\lambda(\lambda/2)
=
\frac{\lambda(4-\lambda)}{16}.
\tag{82.27}
\]

Hence:

- `lambda>4`: endpoint absolute mass is exponentially suppressed;
- `lambda=4`: endpoint is critical at exponential scale;
- `lambda<4`: endpoint absolute mass grows exponentially and absolute perturbation by the full zeta Dirichlet series cannot be small by this mechanism.

This explains the new boundary without interpreting it as a zero-collision boundary.

---

## 10. Hostile audit

### Audit A — huge `tau`

No limit of `tau` is assumed. Equations (82.4) and (82.7) are uniform in every real `tau` because the proof uses absolute convergence and absolute-value remainders.

### Audit B — hidden RH through zeta nonvanishing

No RH information is used. The only zeta zero-free fact is the elementary Euler product in `Re s>1`.

### Audit C — normalization derivative

The derivative is taken after switching to the symmetric nonvanishing normalization. At an exact zero of `H_t`, `G_t'=H_t'/D_t`, so a multiple zero still forces both normalized value and normalized derivative to vanish. The fixed-cutoff discrepancy is exactly the `E0,E1` remainder already controlled by Round 65.

### Audit D — moving cutoff

A fixed cutoff valid over the Cauchy disk is used. The possible one-term local Riemann--Siegel cutoff jump is assigned to the remainder as in Round 65. No derivative of a floor function is taken.

### Audit E — the `rho=0.1` trap

A constant `rho=0.1` would only give the required summable error power for `lambda>4.4`. Round 82 explicitly avoids this mistake through (82.13).

### Audit F — exact `lambda=4`

The theorem requires `a>4`. It makes no assertion at `lambda=4`. The majorant parameter `q` tends to `1`, and the absolute perturbation argument loses summability there.

### Audit G — below `lambda=4`

Nothing in Round 82 excludes collisions for `lambda<4`. In that region the moving-cutoff mass is exponentially large in absolute value. Any continuation below 4 must exploit genuine oscillatory cancellation or a different collision-conditioned structure.

---

## 11. Program consequence

The small-time singular-wedge program is now sharply split:

### Region SW-A

\[
\lambda>4
\]

is asymptotically collision-free for sufficiently small positive `t`, uniformly away from `4`.

### Critical layer SW-B

\[
\lambda=4
\]

requires a separate boundary analysis.

### Region SW-C

\[
0\le\lambda<4
\]

is the genuine remaining singular-wedge invention zone.

The next primary mathematical target should therefore be **not** another global threshold reduction. It should be a phase-correlated analysis of the cutoff layer `u=t log n` for `lambda<=4`, beginning with the critical case `lambda=4`.

Natural candidates are:

1. endpoint/Airy-or-Fresnel-type scaling of the heat-weighted Dirichlet polynomial near `u=lambda/2`;
2. prime-fiber or multiplicative block grouping before taking norms;
3. a collision-conditioned joint value/derivative transform preserving oscillatory cancellation;
4. only after those fail, return to the prime-side connected-correlation program of Rounds 48--61.

---

## 12. Logical status

**PROVED internally:** complex zeta-envelope approximation (82.4), Euler-product lower bound (82.9), radius-adapted small-time transversality on every compact `K subset (4,infinity)`, and the splice to a small-time theorem for all `lambda>=4+epsilon`.

**NOT proved:** collision exclusion at `lambda=4`, collision exclusion below `4`, a global strict shoulder constant below `6.50`, or RH.

**RH remains OPEN.**
