# Round 84 — Explicit van der Corput control of the self-dual cutoff layer and the transition at `lambda = 3`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED, pending independent reconstruction.  
**Strict-program admissibility:** PASSED current direct/transitive audit.  
**Referee status:** PENDING.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Main theorem

Write

\[
L=\log\frac{x}{4\pi},
\qquad
\lambda=tL,
\qquad
x=4\pi e^{\lambda/t}.
\]

Then for every `epsilon>0` there exists `t_epsilon>0` such that

\[
\boxed{
0<t\le t_\varepsilon,
\qquad
\lambda\ge3+\varepsilon
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\tag{84.1}
\]

No RH, finite-height RH verification, bound on the de Bruijn--Newman constant, zero-density theorem, or zeta subconvexity estimate is used.

The only new external analytic input beyond the already audited Polymath approximation is the explicit `d=3` van der Corput derivative theorem of Juan Arias de Reyna, arXiv:2407.02094. The needed corollary is reconstructed below directly from its stated theorem.

The number `3` is **not** claimed to be a collision threshold. It is the point at which the present two-zone proof — absolutely convergent zeta core plus a third-derivative exponential-sum tail — loses overlap.

---

## 2. Input: explicit third-derivative exponential-sum theorem

Arias de Reyna proves the following explicit `d`-th derivative estimate. If

\[
0<\lambda_d\le f^{(d)}(u)\le\Lambda_d
\]

on an interval `(X,X+Y]`, `floor(Y)>d`, and `D=2^d`, then

\[
\left|
\frac1Y\sum_{X<n\le X+Y}e(f(n))
\right|
\le
\max\left\{
A_d\left(\frac{\Lambda_d}{\lambda_dY}\right)^{2/D},
B_d\left(\frac{\Lambda_d^2}{\lambda_d}\right)^{1/(D-2)},
C_d(\lambda_dY^d)^{-2/D}
\right\},
\tag{84.2}
\]

with explicit finite constants; the paper records, in particular, `A_d<7.5`, `B_d<5.8`, `C_d<10.9`.

For our phase, since `tau<0` at large positive `x`, put

\[
f(u)=\frac{|\tau|}{2\pi}\log u.
\]

Then

\[
e(f(n))=e^{i|\tau|\log n}=e^{-i\tau\log n}
\]

and

\[
f'''(u)=\frac{|\tau|}{\pi u^3}>0.
\]

On a dyadic interval contained in `[M,2M]`,

\[
\frac{|\tau|}{8\pi M^3}
\le f'''(u)\le
\frac{|\tau|}{\pi M^3}.
\tag{84.3}
\]

Applying (84.2) with `d=3`, and using the trivial estimate on subintervals of length at most four, gives a uniform maximal partial-sum estimate

\[
\boxed{
\sup_{M<V\le2M}
\left|
\sum_{M<n\le V}e^{-i\tau\log n}
\right|
\le
C
\left(
M^{3/4}
+|\tau|^{1/6}M^{1/2}
+M|\tau|^{-1/4}
+1
\right),
}
\tag{84.4}
\]

for an absolute explicit constant `C`.

Indeed, for a subinterval of length `Y<=M`, the three terms in (84.2), after multiplying by `Y`, are bounded respectively by constant multiples of

\[
Y^{3/4}\le M^{3/4},
\]

\[
Y\left(\frac{|\tau|}{M^3}\right)^{1/6}
\le |\tau|^{1/6}M^{1/2},
\]

and

\[
\left(\frac{M^3}{|\tau|}\right)^{1/4}Y^{1/4}
\le M|\tau|^{-1/4}.
\]

This controls the **individual Riemann--Siegel half-sum**, not merely the reflected full zeta combination. That distinction is why Round 83's rejection of a free `16 theta` shortcut does not apply here.

---

## 3. Heat-weighted half-sum

On the real axis use

\[
s_*=\sigma+i\tau,
\qquad
S_t=\sum_{n\le N}a_ne^{-i\tau\log n},
\]

\[
a_n=
\exp\left(
\frac t4\log^2n-\sigma\log n
\right),
\qquad
N=\left\lfloor\sqrt{e^{\lambda/t}+t/16}\right\rfloor.
\]

As in Round 64,

\[
\sigma=p+\eta,
\qquad
p=\frac12+\frac\lambda4,
\qquad
-\frac{t}{2x^2}\le\eta\le0.
\tag{84.5}
\]

Also

\[
|\tau|=\frac x2+O(t)
=2\pi e^{\lambda/t}+O(t),
\tag{84.6}
\]

uniformly on fixed compact lambda intervals.

---

## 4. Core-tail split

Fix

\[
3<a\le4,
\qquad
\delta:=\frac{a-3}{4}>0,
\]

and consider first

\[
\lambda\in K_a:=[a,4+\delta].
\]

Set

\[
u_0(\lambda):=\lambda-2-\delta,
\qquad
M_0:=\left\lfloor e^{u_0/t}\right\rfloor.
\tag{84.7}
\]

For the whole interval `K_a`,

\[
0<u_0<\lambda/2,
\]

because the upper endpoint was chosen as `4+delta<4+2delta`.

Decompose

\[
S_t=S_t^{\rm core}+S_t^{\rm tail},
\]

where

\[
S_t^{\rm core}
=\sum_{n\le M_0}a_ne^{-i\tau\log n},
\qquad
S_t^{\rm tail}
=\sum_{M_0<n\le N}a_ne^{-i\tau\log n}.
\]

---

## 5. The core remains in an absolutely convergent zeta half-plane

For `n<=M0`,

\[
t\log n\le u_0,
\]

and

\[
a_n=n^{-p}e^{r_n},
\qquad
r_n=\frac t4\log^2n-\eta\log n.
\]

Since

\[
p-\frac{u_0}{4}
=1+\frac\delta4,
\]

for sufficiently small `t`, the exponentially tiny `eta` in (84.5) gives a common exponent

\[
q\ge1+\frac\delta8>1
\]

such that

\[
n^{-p}e^{r_n}\le n^{-q}.
\]

Using `e^r-1<=r e^r`, exactly as in Round 64,

\[
\sum_{n\le M_0}
 n^{-p}|e^{r_n}-1|
\le
\frac t4 Z_2(q)+|\eta|Z_1(q),
\tag{84.8}
\]

where `Z_j(q)=sum_{n>=2}(log n)^j n^{-q}`.

The omitted unheated zeta tail obeys

\[
\sum_{n>M_0}n^{-p}
\le
\frac{M_0^{1-p}}{p-1}.
\tag{84.9}
\]

Therefore

\[
\boxed{
S_t^{\rm core}
=
\zeta(p+i\tau)
+O_a(t)+O_a(e^{-c_a/t}),
}
\tag{84.10}
\]

uniformly for `lambda in K_a` and arbitrary real `tau`.

The same argument with an extra `log n` gives

\[
\boxed{
T_t^{\rm core}:=
\sum_{n\le M_0}a_n\log n\,e^{-i\tau\log n}
=
-\zeta'(p+i\tau)
+O_a(t)+O_a(e^{-c_a/t}).
}
\tag{84.11}

---

## 6. Monotonicity of the heat weights

For `n<=N`,

\[
\frac{d}{d\log n}\log a_n
=
\frac t2\log n-\sigma.
\]

At the moving cutoff the first term is `lambda/4+o(1)`, while

\[
\sigma=\frac12+\frac\lambda4+o(1).
\]

Thus, uniformly on `K_a`,

\[
\frac{d}{d\log n}\log a_n
\le-\frac13
\]

for all sufficiently small `t`.

Hence `a_n` is decreasing throughout the terminal range. Also `a_n log n` is decreasing there for small `t`, because the additional logarithmic derivative `1/log n=O_a(t)` is negligible.

Abel summation therefore allows (84.4) to control both the value tail and its logarithmic-moment tail.

---

## 7. Exponential rates on a dyadic tail block

Let

\[
M=e^{u/t},
\qquad
u_0\le u\le\lambda/2.
\]

Ignoring only uniform `e^{o(1/t)}` factors, the weight at the beginning of the block has rate

\[
W_\lambda(u)
=
\frac{u^2}{4}
-\left(\frac12+\frac\lambda4\right)u.
\tag{84.12}
\]

By (84.6), the three terms of (84.4) have exponential rates

\[
\frac{3u}{4},
\qquad
\frac\lambda6+\frac u2,
\qquad
u-\frac\lambda4.
\]

Thus the three weighted block rates are

\[
G_A(u)=W_\lambda(u)+\frac{3u}{4},
\]

\[
G_B(u)=W_\lambda(u)+\frac\lambda6+\frac u2
=
\frac{u^2}{4}-\frac\lambda4u+\frac\lambda6,
\]

\[
G_C(u)=W_\lambda(u)+u-\frac\lambda4.
\tag{84.13}
\]

At the lower split point `u0=lambda-2-delta`,

\[
G_A(u_0)
=
\frac{(\delta+1)(\delta-\lambda+2)}{4}<0,
\tag{84.14}
\]

\[
G_B(u_0)
=
\frac{3\delta^2-3\delta\lambda+12\delta-4\lambda+12}{12},
\tag{84.15}
\]

\[
G_C(u_0)
=
\frac{\delta^2-\delta\lambda+2\delta-\lambda}{4}<0.
\tag{84.16}
\]

The worst case for (84.15) is `lambda=a`. Writing `a=3+epsilon_a` and `delta=epsilon_a/4`,

\[
G_B(u_0)
\le
-\frac{\epsilon_a(9\epsilon_a+52)}{192}<0.
\tag{84.17}
\]

For `G_A` and `G_C`, convexity shows that it is enough also to inspect the upper endpoint `u=lambda/2`, where

\[
G_A(\lambda/2)
=\frac{\lambda(2-\lambda)}{16}<0,
\]

\[
G_B(\lambda/2)
=\frac{\lambda(8-3\lambda)}{48}<0,
\]

\[
G_C(\lambda/2)
=-\frac{\lambda^2}{16}<0.
\tag{84.18}
\]

(`G_B` is decreasing on the whole tail interval.)

Consequently there is an explicit `c_a>0` such that every dyadic terminal block satisfies

\[
\left|
\sum_{M<n\le\min(2M,N)}
a_ne^{-i\tau\log n}
\right|
\le
C_a e^{-c_a/t}.
\tag{84.19}
\]

The number of dyadic blocks is `O_a(1/t)`, so

\[
\boxed{
S_t^{\rm tail}=O_a(t^{-1}e^{-c_a/t})=o_a(1).
}
\tag{84.20}
\]

For the logarithmic moment an additional factor `O_a(1/t)` is harmless:

\[
\boxed{
T_t^{\rm tail}=O_a(t^{-2}e^{-c_a/t})=o_a(1).
}
\tag{84.21}

---

## 8. Uniform complex zeta envelope now crosses `lambda=4`

Combining core and tail,

\[
\boxed{
S_t
=
\zeta\left(\frac12+\frac\lambda4+i\tau\right)
+o_a(1),
}
\tag{84.22}
\]

and

\[
\boxed{
T_t
=
-\zeta'\left(\frac12+\frac\lambda4+i\tau\right)
+o_a(1),
}
\tag{84.23}

uniformly for `lambda in K_a`.

Since

\[
p\ge p_a:=\frac12+\frac a4>1,
\]

the elementary Euler product gives

\[
|\zeta(p+i\tau)|
\ge
\frac{\zeta(2p)}{\zeta(p)}
\ge
\frac1{\zeta(p_a)}=:m_a>0.
\tag{84.24}
\]

Also

\[
|\zeta'(p+i\tau)|
\le
\sum_{n\ge2}\frac{\log n}{n^{p_a}}<\infty.
\tag{84.25}
\]

Hence

\[
|S_t|\ge m_a-o_a(1),
\qquad
|T_t|=O_a(1).
\tag{84.26}

---

## 9. Hostile audit of the Polymath approximation error below 4

This is the point at which a false proof can easily arise.

The exact printed bound in Polymath Theorem 1.3, equation (23), is

\[
e_A+e_B
\le
\sum_{n\le N}
(1+|\gamma|N^{|\kappa|}n^y)
\frac{b_n^t}{n^{\Re s_*}}
\left[
\exp\left(
\frac{
\frac{t^2}{16}\log^2\frac{x}{4\pi n^2}+0.626
}{x-6.66}
\right)-1
\right].
\tag{84.27}
\]

The entire numerator is divided by `x-6.66`. This is essential.

Round 65's use of an exponentially small `h_K(t)` is therefore correct; an alternative reading in which the logarithmic square is outside the denominator would invalidate that round, but it is not the formula in the source.

For the present compact `K_a`, use a shrinking Cauchy radius

\[
\rho_t:=t/100.
\tag{84.28}
\]

On the upper half of this disk, `0<=y<=rho_t`.

For all `n<=N` and sufficiently small `t`, the basic positive heat weight in (84.27) is at most `1`, while

\[
|\gamma|N^{|\kappa|}n^y=O_a(1).
\]

Therefore the positive prefactor sum is `O_a(N)`. Also

\[
N\le C_a e^{(4+\delta)/(2t)}.
\]

The numerator in (84.27) is `O_a(1)` because

\[
t\left|\log\frac{x}{4\pi n^2}\right|=O_a(1),
\]

while

\[
x^{-1}=O_a(e^{-a/t}).
\]

Thus

\[
\boxed{
e_A+e_B
\le
C_a
\exp\left[-\frac{a-(4+\delta)/2}{t}\right]
=o_a(1),
}
\tag{84.29}
\]

and the exponent is strictly positive because `a>3` and `delta=(a-3)/4`.

Polymath (24) gives independently

\[
e_{C,0}
\le
\exp\left[-\frac{c'_a}{t}+O_a(1)\right]
=o_a(1).
\tag{84.30}
\]

The one-term local cutoff jump is exponentially small because the individual heat weight at the moving cutoff has rate

\[
-\frac\lambda4-\frac{\lambda^2}{16}<0.
\tag{84.31}
\]

Hence a common normalized value-error envelope on the shrinking disk satisfies

\[
\boxed{E_0^{\rm disk}=O_a(e^{-c''_a/t}).}
\tag{84.32}
\]

The symmetric-normalizer comparison over a disk of radius `rho_t` costs only a bounded factor, because

\[
\rho_tL=O_a(1).
\]

Cauchy's estimate therefore yields

\[
E_1
\le
C_a\rho_t^{-1}E_0^{\rm disk}
\le
C_a t^{-1}e^{-c''_a/t},
\]

so

\[
\boxed{E_0\to0,
\qquad
tE_1\to0.}
\tag{84.33}
\]

This shrinking-radius step replaces Round 82's fixed-radius argument and is what makes the derivative audit stable while crossing `lambda=4`.

---

## 10. Collision transversality

Use the same symmetric fixed-cutoff normalization as Rounds 65 and 82:

\[
p_t(x)=2\Re(e^{i\phi}S_t).
\]

At a hypothetical multiple zero,

\[
|\Re(e^{i\phi}S_t)|\le E_0/2,
\qquad
|p_t'(x)|\le E_1.
\]

Writing

\[
e^{i\phi}S_t=X+iY,
\]

(84.26) gives

\[
|Y|
\ge
\sqrt{(m_a-o(1))^2-(E_0/2)^2}
=m_a-o(1).
\tag{84.34}
\]

Moreover

\[
S_x=-(\sigma_x+i\tau_x)T_t,
\]

and the exact real-axis formulas give

\[
t|\phi_x|\to\lambda/4,
\qquad
\sqrt{\sigma_x^2+\tau_x^2}\to1/2.
\tag{84.35}
\]

Since `T_t=O_a(1)`, the logarithmic-moment correction disappears after multiplication by `t`. Therefore

\[
\liminf_{t\to0^+}
\inf_{\lambda\in K_a}
 t\left(
|p_t'(x)|-E_1
\right)
\ge
\boxed{\frac{a m_a}{2}>0}
\tag{84.36}
\]

under the hypothetical collision constraints, a contradiction for sufficiently small `t`.

Thus `K_a` is collision-free for small positive time.

---

## 11. Splicing to all `lambda>=3+epsilon`

Given `epsilon>0`, if `3+epsilon>=6.50`, Round 81 already suffices.

Otherwise choose

\[
a=3+\min(\varepsilon,1),
\qquad
\delta=(a-3)/4.
\]

Round 84 handles

\[
[a,4+\delta].
\]

Round 82 handles, for sufficiently small `t`, the overlapping compact interval

\[
[4+\delta/2,6.50],
\]

and Round 81 handles

\[
[6.50,\infty)
\]

for all `0<t<=1/2`.

Taking the minimum of the finitely many small-time cutoffs proves (84.1).

---

## 12. Why the present method stops at 3

At the lower edge of the oscillatory tail, letting `delta->0`, the decisive middle van-der-Corput rate is

\[
G_B(\lambda-2)
=1-\frac\lambda3.
\tag{84.37}
\]

The zeta core requires its split to satisfy

\[
u_0<\lambda-2
\]

in order to remain in a half-plane of absolute convergence. The `d=3` exponential-sum tail requires

\[
G_B(u_0)<0.
\]

These two open regions overlap exactly when

\[
\lambda>3.
\]

Therefore `3` is the frontier of **this specific core + third-derivative-tail architecture**.

It is not evidence that collisions occur at or below `3`.

---

## 13. What comes next

The next target is no longer the old `lambda=4` critical layer; Round 84 crosses it.

The active singular-wedge invention zone becomes

\[
\boxed{0<\lambda\le3.}
\]

The most promising immediate refinement is to replace the classical third-derivative `M^{5/6}`-type half-sum bound by a stronger **direct exponent-pair bound for the individual logarithmic half-sum**, with its precise normalization and range taken from a primary source.

Huxley's 2005 paper proves that `(32/205+eps,269/410+eps)` is an exponent pair, but this has not yet been inserted into the proof because the exact exponent-pair normalization required for our weighted dyadic blocks must first be audited. A formal substitution without that audit is forbidden.

If such a direct exponent-pair estimate is inserted in the standard form

\[
\sum_{M<n\le2M}n^{-iT}
\ll
(T/M)^\kappa M^\ell,
\]

then the core/tail overlap condition becomes

\[
\lambda>
\frac{2(1+\kappa-\ell)}{1-\ell},
\]

but this formula is **CONDITIONAL BOOKKEEPING ONLY** until the precise theorem is sourced and reconstructed.

---

## 14. Circularity and source audit

### Used

- Polymath Theorem 1.3 and its explicit error formulas (23),(24);
- exact real-axis saddle/phase derivatives already audited in the repository;
- Euler product only in `Re s>1`;
- Arias de Reyna's unconditional explicit third-derivative exponential-sum theorem.

### Not used

- RH;
- finite-height RH verification;
- `Lambda<=0`, `Lambda=0`, or any positive upper bound for `Lambda`;
- Bourgain/subconvexity;
- pair correlation/GUE;
- real-rootedness of `H_0`;
- generalized Laguerre positivity;
- negative-time Rodgers--Tao estimates.

**RH remains OPEN.**
