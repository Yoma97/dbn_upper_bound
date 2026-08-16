# Round 64 — Exact-weight moment collapse in the fixed-lambda shoulder

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Proves the first analytic gate LS-A1 of the Low-Shoulder program with explicit remainders. It does not prove collision exclusion below `lambda=10.52` by itself.

---

## 1. Statement and conventions

Fix `rho=0.1`. Put

\[
L=\log\frac{x}{4\pi},\qquad \lambda=tL,\qquad x=4\pi e^{\lambda/t},
\]

and, on the real axis,

\[
A(x)=-\frac1{1+x^2}+\frac14\log(1+x^2)-\frac12\log(4\pi),
\]

\[
\sigma(t,x)=\frac12+\frac t2A(x).
\]

For a fixed holomorphic base cutoff `N` satisfying

\[
1\le N\le \sqrt{\frac{x+\rho}{4\pi}+\frac t{16}},
\]

define

\[
a_n(t,\lambda)=
\exp\!\left(\frac t4(\log n)^2-\sigma(t,x)\log n\right),
\]

\[
A_0(t,\lambda;N)=\sum_{n=2}^{N}a_n,
\qquad
A_1(t,\lambda;N)=\sum_{n=2}^{N}a_n\log n.
\]

The natural fixed-cutoff choice for the Cauchy-disk PSC is

\[
N_-(t,\lambda;\rho)
=
\left\lfloor
\sqrt{e^{\lambda/t}-\frac{\rho}{4\pi}+\frac t{16}}
\right\rfloor,
\]

which is no larger than every local Polymath cutoff on `|z-x|<=rho`.

Let

\[
p(\lambda)=\frac12+\frac\lambda4.
\]

For `s>1` define positive logarithmic moments

\[
Z_k(s)=\sum_{n=2}^{\infty}(\log n)^k n^{-s}
=(-1)^k\zeta^{(k)}(s),\qquad k\ge1,
\]

and `Z_0(s)=zeta(s)-1`.

### Theorem 64.1 — explicit exact-weight moment collapse

Let

\[
4<\lambda_0\le\lambda\le\lambda_1<\infty,
\qquad
\Delta=\lambda_0-4,
\]

and put

\[
q=1+\frac{\Delta}{16}
=\frac34+\frac{\lambda_0}{16}>1.
\]

Assume

\[
0<t\le t_0(\lambda_0):=
\min\left\{\frac12,\pi^2\Delta,2\sqrt\Delta\right\}.
\tag{64.1}
\]

Then for every admissible cutoff `N` above,

\[
\boxed{
\left|
A_0(t,\lambda;N)-\left(\zeta(p)-1\right)
\right|
\le
\frac t4 Z_2(q)
+\frac{t}{2x^2}Z_1(q)
+\frac{N^{1-p}}{p-1}.
}
\tag{64.2}
\]

If `N>=2`, then

\[
\boxed{
\left|
A_1(t,\lambda;N)+\zeta'(p)
\right|
\le
\frac t4 Z_3(q)
+\frac{t}{2x^2}Z_2(q)
+N^{1-p}
\left(
\frac{\log N}{p-1}+\frac1{(p-1)^2}
\right).
}
\tag{64.3}
\]

For `N=N_-(t,lambda;rho)`, both right sides tend to zero uniformly for

\[
\lambda\in[\lambda_0,\lambda_1]
\]

as `t->0+`. In particular,

\[
A_0(t,\lambda;N_-)
\to
\zeta\!\left(\frac12+\frac\lambda4\right)-1,
\]

\[
A_1(t,\lambda;N_-)
\to
-\zeta'\!\left(\frac12+\frac\lambda4\right)
\]

uniformly on every compact subinterval of `(4,infinity)`.

---

## 2. Exact decomposition of the heat weight

Since

\[
\log(1+x^2)=2L+2\log(4\pi)+\log(1+x^{-2}),
\]

we have the exact identity

\[
A(x)=\frac L2+\delta_A(x),
\]

where

\[
\delta_A(x)=\frac14\log(1+x^{-2})-\frac1{1+x^2}.
\tag{64.4}
\]

For `x>=1`, set `u=x^{-2}`. Then `0<u<=1` and

\[
\delta_A=\frac14\log(1+u)-\frac{u}{1+u}.
\]

The derivative of the right side with respect to `u` is

\[
\frac{u-3}{4(1+u)^2}<0,
\]

and its value at `u=0` is zero. Therefore

\[
-x^{-2}\le\delta_A(x)\le0.
\tag{64.5}
\]

Thus

\[
\sigma
=
\frac12+\frac{tL}{4}+\frac t2\delta_A
=p+\eta,
\qquad
-\frac{t}{2x^2}\le\eta\le0.
\tag{64.6}
\]

Consequently

\[
a_n
=n^{-p}e^{r_n},
\]

where

\[
r_n
=\frac t4(\log n)^2-\eta\log n
\]

satisfies

\[
0\le r_n
\le
\frac t4(\log n)^2+\frac{t}{2x^2}\log n.
\tag{64.7}
\]

This is the exact point at which the previous global proof lost most of its strength: replacing the quadratic expression by one edge exponent discards the small-`n` suppression encoded in (64.7).

---

## 3. A uniform summable majorant

For every admissible `n<=N`,

\[
\log n
\le
\frac12\log\left(e^L+\frac t{16}\right)
=
\frac L2+rac12\log\left(1+\frac t{16}e^{-L}\right).
\]

Using `log(1+v)<=v`, (64.5), and `L=lambda/t`,

\[
\begin{aligned}
\sigma-\frac t4\log n
&\ge
\frac12+\frac\lambda4
-\frac{t}{2x^2}
-\frac\lambda8
-\frac{t^2}{128}e^{-L}\\
&=
\frac12+\frac\lambda8-\varepsilon_*(t,\lambda),
\end{aligned}
\]

with

\[
\varepsilon_*(t,\lambda)
=
\frac{t}{32\pi^2}e^{-2\lambda/t}
+\frac{t^2}{128}e^{-\lambda/t}.
\tag{64.8}
\]

Uniformly for `lambda>=lambda_0`,

\[
\varepsilon_*(t,\lambda)
\le
\frac{t}{32\pi^2}+\frac{t^2}{128}.
\]

Condition (64.1) implies separately

\[
\frac{t}{32\pi^2}\le\frac\Delta{32},
\qquad
\frac{t^2}{128}\le\frac\Delta{32},
\]

and hence

\[
\varepsilon_*\le\frac\Delta{16}.
\]

Since

\[
\frac12+\frac{\lambda_0}{8}
=1+\frac\Delta8,
\]

we conclude

\[
\sigma-\frac t4\log n
\ge
1+\frac\Delta{16}=q.
\]

Therefore

\[
\boxed{a_n\le n^{-q}}
\tag{64.9}
\]

uniformly over the entire moving cutoff and over `lambda in [lambda_0,lambda_1]`.

This is the key direct domination step. No three-region splitting, Euler--Maclaurin formula, or Laplace endpoint argument is needed for LS-A1.

---

## 4. Proof of the A0 estimate

Since `r_n>=0`,

\[
0\le e^{r_n}-1\le r_ne^{r_n}.
\]

Hence, by (64.7) and (64.9),

\[
\begin{aligned}
0\le a_n-n^{-p}
&=n^{-p}(e^{r_n}-1)\\
&\le
\left[
\frac t4(\log n)^2
+\frac{t}{2x^2}\log n
\right]n^{-q}.
\end{aligned}
\tag{64.10}
\]

Summing from `2` to `N` gives

\[
0\le
A_0-\sum_{n=2}^N n^{-p}
\le
\frac t4Z_2(q)+\frac{t}{2x^2}Z_1(q).
\tag{64.11}
\]

Since `p>1`, the decreasing integral test yields

\[
0\le
\sum_{n>N}n^{-p}
\le
\int_N^\infty u^{-p}\,du
=\frac{N^{1-p}}{p-1}.
\tag{64.12}
\]

Combining (64.11) and (64.12) proves (64.2).

---

## 5. Proof of the A1 estimate

Multiplying (64.10) by `log n` and summing,

\[
0\le
A_1-\sum_{n=2}^N(\log n)n^{-p}
\le
\frac t4Z_3(q)+\frac{t}{2x^2}Z_2(q).
\tag{64.13}
\]

Also

\[
\sum_{n=2}^{\infty}(\log n)n^{-p}=-\zeta'(p).
\]

For `p>3/2` and `N>=2`, the function

\[
u\mapsto (\log u)u^{-p}
\]

is decreasing on `[N,infinity)` because `log 2>1/p`. Therefore

\[
\begin{aligned}
0\le
\sum_{n>N}(\log n)n^{-p}
&\le
\int_N^\infty(\log u)u^{-p}\,du\\
&=N^{1-p}
\left(
\frac{\log N}{p-1}+\frac1{(p-1)^2}
\right).
\end{aligned}
\tag{64.14}
\]

Equations (64.13) and (64.14) prove (64.3).

---

## 6. Uniform decay of the moving-cutoff tail

Take the Cauchy-disk base cutoff `N=N_-`. Since `lambda>=lambda_0>4` and `t<=1/2`,

\[
L=\frac\lambda t>8.
\]

Thus `e^L` is so large that

\[
e^L-\frac{\rho}{4\pi}+\frac t{16}>\frac34e^L.
\]

Hence

\[
N_-
\ge
\sqrt{\frac34}\,e^{L/2}-1
\ge
\frac12e^{L/2}
=
\frac12e^{\lambda/(2t)}.
\tag{64.15}
\]

Therefore the power tail in (64.2) is exponentially small in `1/t`; for example, if

\[
p_0=\frac12+\frac{\lambda_0}{4},
\qquad
p_1=\frac12+\frac{\lambda_1}{4},
\]

then uniformly on the compact interval,

\[
N_-^{1-p}
\le
2^{p_1-1}
\exp\left(-\frac{(p_0-1)\lambda_0}{2t}\right).
\tag{64.16}
\]

The logarithmic tail in (64.3) is the same exponential multiplied by at most a polynomial factor in `1/t`, and therefore also tends uniformly to zero.

Since `x^{-2}=(16\pi^2)^{-1}e^{-2\lambda/t}`, the `x^{-2}` terms are super-exponentially small relative to the explicit `O(t)` contribution.

Thus the leading explicit uniform errors are

\[
R_0(t;K)=\frac t4Z_2(q)+O_K(e^{-c_K/t}),
\]

\[
R_1(t;K)=\frac t4Z_3(q)+O_K(t^{-1}e^{-c_K/t}),
\]

with completely explicit versions already given by (64.2)--(64.3).

---

## 7. What this proves and what it does not

### PROVED in this round

The true positive moments entering the triangle-envelope PSC have the uniform fixed-lambda limits

\[
A_0\to\zeta(p)-1,
\qquad
A_1\to-\zeta'(p)
\]

for compact `lambda` intervals strictly above `4`, with explicit remainders.

This rigorously removes the need to replace the whole heat weight by a single `n^{-p_edge}` power in the small-time analysis.

### NOT proved in this round

We have **not** yet proved

\[
t\mathcal T(t,\lambda)
\to
\frac\lambda2\left[2-\zeta\left(\frac12+\frac\lambda4\right)\right].
\]

That requires a separate uniform audit of:

1. `t Phi0 -> lambda/4`;
2. `d -> 1/2`;
3. `E0 -> 0`;
4. `t E1 -> 0`;
5. the fixed-cutoff jump bridge and normalization ratio on the Cauchy disk.

These are the Round-65 obligations.

---

## 8. Correction to the interpretation of lambda_*

Let `p_*` solve `zeta(p_*)=2` and

\[
\lambda_*=4(p_*-1/2)=4.914588956\ldots.
\]

Round 64 justifies the statement that, in the fixed-lambda small-time limit, the unchanged `n=1` triangle lower bound

\[
S_0=1-A_0
\]

tends to

\[
2-\zeta\left(\frac12+\frac\lambda4\right).
\]

Therefore `lambda_*` is correctly described as

\[
\boxed{
\text{the asymptotic sign floor of the unchanged }n=1
\text{ triangle-envelope component of PSC}.
}
\]

It is **not** proved to be:

- a collision threshold;
- a floor for every possible phase-slope certificate;
- a floor for finite `t`;
- evidence for a collision below it.

This narrower wording replaces the earlier phrase “structural floor of PSC”, which was too broad.

---

## 9. Circularity audit

Inputs:

1. the explicit real-axis `alpha` formula from the unconditional Polymath effective approximation;
2. elementary inequalities `log(1+u)<=u` and `e^r-1<=r e^r` for `r>=0`;
3. positive Dirichlet series and decreasing integral tails;
4. no information about zeros of `H_t` or `zeta` is used.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- real-rootedness of `H_0`;
- finite-height RH verification;
- GUE/pair correlation;
- Rodgers--Tao negative-time zero estimates;
- Laguerre--Polya membership.

The theorem is therefore non-circular.

---

## 10. Dependency DAG

`Polymath explicit alpha formula`

`-> exact sigma decomposition (64.4)-(64.6)`

`-> moving-cutoff exponent domination (64.9)`

`-> positive moment comparison (64.10)`

`-> explicit zeta-moment errors (64.2)-(64.3)`

`-> uniform exact-weight moment collapse`.

No dependency edge contains the desired no-collision statement.

---

## 11. Adversarial edge cases

- `lambda_0 downarrow 4`: `q downarrow 1`, so `Z_k(q)` diverges and `t_0(lambda_0)` collapses. This is expected and is why the theorem is stated on compact subsets of `(4,infinity)`.
- `t->0`: the cutoff tends to infinity exponentially; (64.15) controls the tail rather than assuming fixed `N`.
- cutoff jumps: LS-A1 is valid for every fixed base cutoff under the displayed upper-cutoff condition; jump terms belong to the PSC remainder, not to these moment identities.
- `N=1`: `A0=A1=0`; the asymptotic theorem is not invoked there. For the low-shoulder scaling with `lambda_0>4` and small `t`, `N_->>2` automatically.
- `lambda` unbounded: no such claim is made from Round 64 alone. Uniformity is on a fixed compact `[lambda_0,lambda_1]`; the already proved high-shoulder theorem handles `lambda>=10.52` in the intended proof cover.

---

## 12. Next gate

Round 65 must prove an explicit remainder

\[
\left|
t\mathcal T(t,\lambda)
-
\frac\lambda2\left[2-\zeta\left(\frac12+\frac\lambda4\right)\right]
\right|
\le R_{\mathcal T}(t;K),
\]

with `R_T(t;K)->0` uniformly for every compact

\[
K\subset(\lambda_*,10.52].
\]

Only after that may one promote a small-time collision-exclusion theorem above `lambda_*+epsilon`.
