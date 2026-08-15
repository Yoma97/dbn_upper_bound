# Round 22 — Exact cutoff commutator, V-domination, and signed reference decomposition

**Date:** 2026-08-15

**RH status:** OPEN.

**Status labels:** PROVED / CONDITIONAL / CANDIDATE / REFUTED / NOVELTY UNVERIFIED.

## 0. Executive theorem

Round 17's relative Bregman balance can be rewritten in a sharper form in which the cutoff error is an exact discrete commutator depending only on differences \(\psi_j-\psi_k\). In addition, every reciprocal-gap defect is pointwise dominated by Rodgers--Tao's convex \(V\)-energy. For the symmetric Riemann reference, Round 20's asymptotic reference force separates into:

1. a signed constant drift \(-\frac\pi8\operatorname{sgn}j\);
2. a regular cross-origin interaction;
3. a residual reference error whose weighted square sum is only polylogarithmic for the Rodgers--Tao cutoff.

These are exact structural facts. They do **not** provide the missing finite entropy budget identified in Round 18.

---

## 1. Finite algebraic setup

Let \(J\subset\mathbb Z^*\) be a finite symmetric index set for the algebraic proof. Let

\[
x_{-j}=-x_j,\qquad \xi_{-j}=-\xi_j,\qquad x_j,\xi_j>0\ (j>0),
\]

and let \(\psi_j\in[0,1]\) be time-independent. Define

\[
\delta_{jk}
:=\frac1{x_j-x_k}-\frac1{\xi_j-\xi_k}
=-\delta_{kj}.
\]

Round 17 uses

\[
D_j:=D_j^\psi=\sum_{k\ne j}\psi_k\delta_{jk},
\]

\[
F_j:=F_j^\psi=\sum_{k\ne j}(1-\psi_k)\delta_{jk},
\]

and the fixed reference force

\[
S_j^\xi:=\sum_{k\ne j}\frac1{\xi_j-\xi_k}.
\]

Its exact Bregman balance is

\[
\partial_t\mathcal C_\psi
=-4\sum_j\psi_jD_j^2
-4\sum_j\psi_jD_jF_j
-4\sum_j\psi_jD_jS_j^\xi.
\]

---

## 2. Exact cutoff-commutator rewrite — PROVED

Define

\[
\boxed{
K_j^\psi
:=\sum_{k\ne j}(\psi_j-\psi_k)\delta_{jk}.
}
\]

Because

\[
D_j+F_j=\sum_{k\ne j}\delta_{jk},
\]

we have

\[
\begin{aligned}
K_j^\psi
&=\psi_j(D_j+F_j)-D_j\\
&=\psi_jF_j-(1-\psi_j)D_j.
\end{aligned}
\]

Therefore

\[
\boxed{
\psi_jF_j=K_j^\psi+(1-\psi_j)D_j.
}
\]

Substituting into the Round-17 balance gives

\[
\boxed{
\partial_t\mathcal C_\psi
=-4\sum_jD_j^2
-4\sum_jD_jK_j^\psi
-4\sum_j\psi_jD_jS_j^\xi.
}
\]

Thus the apparent boundary term has split into:

- a stronger unweighted positive bulk \(4\sum_jD_j^2\);
- the exact cutoff commutator \(K_j^\psi\), which vanishes identically if \(\psi\) is constant;
- the reference-force channel.

No approximation is used.

For countably infinite systems the identity remains **CONDITIONAL** on the justified summation/interchange conventions.

---

## 3. Pointwise V-domination of reciprocal-gap defect — PROVED

For a pair \(j\ne k\), put

\[
s:=\xi_j-\xi_k,\qquad d:=x_j-x_k,\qquad r:=d/s>0.
\]

Then

\[
\delta_{jk}
=\frac1s\left(\frac1r-1\right),
\]

so

\[
\delta_{jk}^2
=\frac1{s^2}\left(\frac1r-1\right)^2.
\]

Rodgers--Tao's convex pair potential is

\[
V(r)=r^{-2}-1+2(r-1)=r^{-2}+2r-3.
\]

A direct calculation gives

\[
\begin{aligned}
V(r)-\left(r^{-1}-1\right)^2
&=2\left(r+r^{-1}-2\right)\\
&=2\frac{(r-1)^2}{r}\ge0.
\end{aligned}
\]

Hence

\[
\boxed{
\delta_{jk}^2
\le
\frac1{(\xi_j-\xi_k)^2}
V\!\left(\frac{x_j-x_k}{\xi_j-\xi_k}\right)
=:\widetilde E^V_{jk}.
}
\]

This is a nonlinear pointwise inequality valid for every positive relative spacing \(r\), not merely near equilibrium.

Equality holds only at \(r=1\).

---

## 4. Finite-range commutator bound — PROVED

Fix an interaction radius \(R\ge1\), and define the near commutator

\[
K_{j,R}^\psi
:=\sum_{0<|k-j|\le R}(\psi_j-\psi_k)\delta_{jk}.
\]

Assume on these pairs that

\[
\boxed{
|\psi_j-\psi_k|
\le L_\psi |j-k|\sqrt{\psi_j\psi_k}.
}
\]

Then Cauchy--Schwarz gives

\[
\begin{aligned}
|K_{j,R}^\psi|^2
&\le
\left(
\sum_{0<|k-j|\le R}
\frac{|\psi_j-\psi_k|^2}{\psi_j\psi_k}
\right)
\left(
\sum_{0<|k-j|\le R}
\psi_j\psi_k\delta_{jk}^2
\right)\\
&\le
L_\psi^2
\left(
\sum_{0<|n|\le R}n^2
\right)
\sum_{0<|k-j|\le R}
\psi_j\psi_k\widetilde E^V_{jk}.
\end{aligned}
\]

Since

\[
\sum_{0<|n|\le R}n^2\le \frac23(R+1)^3,
\]

we obtain

\[
\boxed{
|K_{j,R}^\psi|^2
\le
\frac23 L_\psi^2(R+1)^3
\sum_{0<|k-j|\le R}
\psi_j\psi_k\widetilde E^V_{jk}.
}
\]

Summing in \(j\),

\[
\boxed{
\sum_j|K_{j,R}^\psi|^2
\le
\frac23L_\psi^2(R+1)^3
\widetilde E_{\psi,R}^{V,\rm ord},
}
\]

where

\[
\widetilde E_{\psi,R}^{V,\rm ord}
:=\sum_j\sum_{0<|k-j|\le R}
\psi_j\psi_k\widetilde E^V_{jk}.
\]

Consequently, for every \(\eta>0\),

\[
4\left|\sum_jD_jK_{j,R}^\psi\right|
\le
2\eta\sum_jD_j^2
+\frac{4}{3\eta}L_\psi^2(R+1)^3
\widetilde E_{\psi,R}^{V,\rm ord}.
\]

Thus any scale with

\[
L_\psi^2R^3\ll1
\]

makes the near cutoff commutator perturbative relative to the positive force-square / \(V\)-energy channels.

---

## 5. Rodgers--Tao cutoff scale — SOURCE-COMPATIBLE CONSEQUENCE

Rodgers--Tao use

\[
\psi_T(j)=
\left(1+\frac{|j|}{T\log T}\right)^{-100}.
\]

Write

\[
N:=T\log T.
\]

On a region where \(|j-k|=o(N)\), the logarithmic derivative bound

\[
|\partial_u\log\psi_T(u)|\le \frac{100}{N}
\]

implies

\[
|\psi_T(j)-\psi_T(k)|
\ll
\frac{|j-k|}{N}
\sqrt{\psi_T(j)\psi_T(k)}
\]

provided \(|j-k|/N\) is bounded by a sufficiently small absolute constant; the implicit constant is absolute.

In their main region \(|j|\asymp T\log T\), the nearby relation has radius of order

\[
R_T\asymp T^{0.2}
\]

up to harmless logarithmic factors, while

\[
N=T\log T.
\]

Therefore

\[
\boxed{
L_\psi^2R_T^3
\ll
\frac{T^{0.6}}{T^2\log^2T}
=\frac{1}{T^{1.4}\log^2T},
}
\]

again up to the harmless variation in the precise nearby radius.

So the **near-pair cutoff commutator is strongly perturbative at the Rodgers--Tao scales**.

This statement is algebraic/cutoff-geometric; it does not use their negative-time actual-zero estimates.

The far-pair component is a separate problem and is not declared controlled here.

---

## 6. Signed reference-force decomposition — PROVED using Round 20

Round 20 gives

\[
S_j^\xi
=-\frac\pi8\operatorname{sgn}(j)+e_j,
\]

with

\[
|e_j|\ll\frac{\log|j|}{\sqrt{|j|}}
\]

for large \(|j|\), and \(e_{-j}=-e_j\).

The reference term becomes

\[
\begin{aligned}
\mathscr R_{\xi,\psi}
&:=-4\sum_j\psi_jD_jS_j^\xi\\
&=
\frac\pi2\sum_j\psi_jD_j\operatorname{sgn}(j)
-4\sum_j\psi_jD_je_j.
\end{aligned}
\]

Assume now that \(\psi\) is even. Symmetry of the configurations implies

\[
D_{-j}=-D_j.
\]

Hence

\[
\sum_j\psi_jD_j\operatorname{sgn}(j)
=2\sum_{j>0}\psi_jD_j.
\]

Expanding \(D_j\), the positive-positive interactions cancel by antisymmetry:

\[
\sum_{j,k>0}\psi_j\psi_k\delta_{jk}=0.
\]

Therefore only cross-origin pairs remain:

\[
\boxed{
\sum_{j>0}\psi_jD_j
=
\sum_{j,l>0}
\psi_j\psi_l\delta_{j,-l}.
}
\]

Since

\[
\delta_{j,-l}
=rac1{x_j+x_l}-rac1{\xi_j+\xi_l},
\]

we obtain the exact signed decomposition

\[
\boxed{
\mathscr R_{\xi,\psi}
=
\pi\sum_{j,l>0}
\psi_j\psi_l
\left(
\frac1{x_j+x_l}-
\frac1{\xi_j+\xi_l}
\right)
-4\sum_j\psi_jD_je_j.
}
\]

Thus the nonzero asymptotic drift \(\mp\pi/8\) does **not** generate a singular local same-sign force. It becomes a regular cross-origin interaction.

A collision between two positive zeros cannot make any denominator \(x_j+x_l\) vanish.

---

## 7. V-control of the cross-origin leading term — PROVED but coarse

Define

\[
\mathcal A_{\rm cross}
:=\sum_{j,l>0}\psi_j\psi_l\delta_{j,-l}
\]

and

\[
\widetilde E^V_{\rm cross}
:=
\sum_{j,l>0}
\psi_j\psi_l
\frac1{(\xi_j+\xi_l)^2}
V\!\left(
\frac{x_j+x_l}{\xi_j+\xi_l}
\right).
\]

By Section 3,

\[
\delta_{j,-l}^2
\le \text{the corresponding cross }V\text{-energy term}.
\]

Let

\[
N_+:=\sum_{j>0}\psi_j.
\]

Cauchy--Schwarz yields

\[
\boxed{
|\mathcal A_{\rm cross}|
\le
N_+\sqrt{\widetilde E^V_{\rm cross}}.
}
\]

Therefore the signed drift contribution obeys

\[
\boxed{
|\mathscr R_{\rm lead}|
\le
\pi N_+\sqrt{\widetilde E^V_{\rm cross}}.
}
\]

This bound is intentionally classified as **coarse**; it proves regularity/control by an already natural relative energy but is not by itself small enough for a no-collision theorem.

---

## 8. Polylogarithmic bound for the residual reference error under \(\psi_T\) — PROVED

The residual is

\[
\mathscr R_{\rm err}
=-4\sum_j\psi_jD_je_j.
\]

By Cauchy--Schwarz,

\[
|\mathscr R_{\rm err}|
\le
4\left(\sum_j\psi_jD_j^2\right)^{1/2}
\left(\sum_j\psi_je_j^2\right)^{1/2}.
\]

For the Rodgers--Tao cutoff \(\psi_T(j)=(1+|j|/N)^{-100}\), \(N=T\log T\), Round 20 implies

\[
\sum_{j\in\mathbb Z^*}\psi_T(j)e_j^2
\ll 1+\sum_{1\le j\lesssim N}\frac{\log^2(2+j)}{j}
+\sum_{j\gtrsim N}\left(1+\frac jN\right)^{-100}
\frac{\log^2(2+j)}{j}.
\]

Hence

\[
\boxed{
\sum_j\psi_T(j)e_j^2
\ll \log^3(2+N).
}
\]

Therefore

\[
\boxed{
|\mathscr R_{\rm err}|
\ll
\log^{3/2}(2+N)
\left(\sum_j\psi_T(j)D_j^2\right)^{1/2}.
}
\]

Equivalently, for every \(\eta>0\),

\[
\boxed{
|\mathscr R_{\rm err}|
\le
\eta\sum_j\psi_T(j)D_j^2
+C_\eta\log^3(2+N).
}
\]

This estimate uses only Round 20's explicit reference asymptotic and the cutoff decay; it does not use any actual-zero displacement estimate.

---

## 9. What remains genuinely open

The exact commutator rewrite and the bounds above do **not** close Program A.

The unresolved pieces are:

1. **Far cutoff commutator:** control the part of \(K_j^\psi\) from large \(|j-k|\) using an input valid in the positive-time / hypothetical-\(\Lambda>0\) regime, not Rodgers--Tao's contradiction estimates for \(\Lambda<0\).
2. **Cross-origin reference budget:** improve the coarse bound on \(\mathcal A_{\rm cross}\), or absorb it into a natural compensated entropy.
3. **Entropy budget:** Round 18 proves that even perfect flux control does not rule out collision. One still needs an independent one-sided bound preventing the relevant entropy from diverging in its collision direction.

The third item is the decisive gate.

---

## 10. Circularity audit

No theorem above assumes RH, \(\Lambda\le0\), all-time real-rootedness, global Laguerre positivity, a lower gap bound, or Rodgers--Tao's negative-time contradiction estimates.

The only Riemann-specific input is the explicit classical reference asymptotic from Round 20 and the explicit form of the Rodgers--Tao cutoff.

---

## 11. Status

- exact Bregman cutoff-commutator rewrite: **PROVED**;
- nonlinear pointwise \(\delta^2\le \widetilde E^V\): **PROVED**;
- finite-range commutator estimate: **PROVED**;
- perturbative near-commutator at Rodgers--Tao cutoff scale: **PROVED at the cutoff-geometric level**;
- signed reference decomposition into cross-origin + residual: **PROVED**;
- residual reference error polylog bound: **PROVED**;
- cross-origin leading term V-control: **PROVED but coarse**;
- far commutator in the needed positive-time regime: **OPEN**;
- independent finite entropy/coercive budget: **OPEN — DECISIVE**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
