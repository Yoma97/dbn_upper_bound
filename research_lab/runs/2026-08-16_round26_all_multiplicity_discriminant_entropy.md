# Round 26 — All-multiplicity discriminant order, entropy residue, and resultant barrier

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / STRUCTURAL OBSTRUCTION / CONDITIONAL APPLICATION / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 25 proved the logarithmic entropy trilemma for a generic double collision. This round extends the singularity calculation to **every multiplicity** and identifies the exact algebraic object behind any one-sided entropy budget.

Let `F(t,x)` be a nontrivial real-analytic backward-heat family

\[
\partial_tF=-\partial_x^2F
\]

with an isolated real multiplicity-`m` collision at `(t_c,c)`, `m>=2`. On the real-simple side `t>t_c`, put `tau=t-t_c` and let `x_1(t),...,x_m(t)` be the local roots.

Then the local monic Weierstrass discriminant satisfies

\[
\boxed{
\Delta_{\rm loc}(t)
=\Delta(Q_m)\,\tau^{N_m}(1+O(\tau)),
\qquad
N_m:=\binom m2=\frac{m(m-1)}2,
}
\]

where

\[
Q_m(X):=e^{-\partial_X^2}X^m=H_m(X/2)
\]

is the monic Hermite collision polynomial and

\[
\boxed{
\Delta(Q_m)=2^{N_m}\prod_{k=1}^m k^k>0.
}
\]

Consequently

\[
\boxed{
\partial_t\log\Delta_{\rm loc}
=\frac{N_m}{\tau}+O(1),
}
\]

and the hard-window inverse-square energy has the exact leading singularity

\[
\boxed{
E_{\rm ord,loc}(t)
=\frac{m(m-1)}{8\tau}+O(1).
}
\]

The hard-window external flux remains `O(1)` for every fixed multiplicity.

Thus the collision-sensitive logarithmic entropies do not merely detect a double gap: for multiplicity `m` their singular coefficient is the vanishing order of the local **discriminant/resultant**. Any finite one-sided entropy budget with bounded spectators is therefore locally equivalent to a quantitative lower bound on that discriminant, equivalently to local transversality of `(F,F_x)`.

This does not make such a theorem illegitimate if the lower bound is derived from independent Riemann-specific structure. It does show that the entropy budget is not a softer topological/energetic target by itself.

---

## 1. Parabolic Hermite splitting

Translate the collision to `(t_c,c)=(0,0)` for the local calculation. Suppose

\[
F(0,x)=a x^m+O(x^{m+1}),
\qquad a\ne0.
\]

By analyticity and the backward heat equation, under

\[
t=\tau,
\qquad x=\sqrt\tau X,
\]

one has

\[
\frac{F(\tau,\sqrt\tau X)}{a\tau^{m/2}}
=Q_m(X)+O(\sqrt\tau)
\]

locally uniformly, with

\[
Q_m(X)
=m!\sum_{k=0}^{\lfloor m/2\rfloor}
\frac{(-1)^kX^{m-2k}}{k!(m-2k)!}
=H_m(X/2).
\]

Let

\[
\xi_1<\cdots<\xi_m
\]

be the distinct real roots of `Q_m`. Then the local real root branches satisfy

\[
\boxed{
x_j(\tau)=\sqrt\tau\,\xi_j+O(\tau).}
\]

Undoing the translation gives the same formula with `c+` on the right.

---

## 2. Weierstrass discriminant order — PROVED

Factor locally

\[
F(t,z)=a(t,z)P(t,z),
\qquad a(t,z)\ne0,
\]

where `P(t,z)` is the monic degree-`m` Weierstrass polynomial whose roots are precisely the local branches `x_j(t)`.

Define

\[
\Delta_{\rm loc}(t)
:=\operatorname{Disc}_z P(t,z)
=\prod_{1\le i<j\le m}(x_i(t)-x_j(t))^2.
\]

From the Hermite splitting,

\[
(x_i-x_j)^2
=\tau(\xi_i-\xi_j)^2(1+O(\sqrt\tau)).
\]

Multiplying over the `N_m=binom(m,2)` unordered pairs gives initially

\[
\Delta_{\rm loc}(t)
=\tau^{N_m}\Delta(Q_m)(1+O(\sqrt\tau)).
\]

But the discriminant of a monic polynomial is a polynomial in its coefficients, and the Weierstrass coefficients are analytic in `tau`. Hence `Delta_loc(t)` is analytic in `tau`. Since its leading coefficient `Delta(Q_m)` is nonzero, no half-integer correction can occur. Therefore

\[
\boxed{
\Delta_{\rm loc}(t)
=\Delta(Q_m)\tau^{N_m}(1+O(\tau)).
}
\]

and

\[
\boxed{
\partial_t\log\Delta_{\rm loc}
=\frac{N_m}{\tau}+O(1).
}
\]

This sharpens the naive `O(tau^{-1/2})` remainder obtained from root-by-root expansions.

---

## 3. Exact Hermite discriminant constant — PROVED

The monic collision polynomials satisfy

\[
Q_m'(X)=mQ_{m-1}(X)
\]

and the recurrence

\[
Q_m(X)=XQ_{m-1}(X)-2(m-1)Q_{m-2}(X).
\]

Let

\[
R_m:=|\operatorname{Res}(Q_m,Q_{m-1})|.
\]

Evaluating the recurrence at the roots of `Q_{m-1}` gives

\[
R_m=[2(m-1)]^{m-1}R_{m-1},
\qquad R_1=1.
\]

Thus

\[
R_m=\prod_{k=1}^{m-1}(2k)^k.
\]

For a monic polynomial,

\[
\Delta(Q_m)
=|\operatorname{Res}(Q_m,Q_m')|
=m^mR_m.
\]

Therefore

\[
\boxed{
\Delta(Q_m)
=2^{m(m-1)/2}\prod_{k=1}^m k^k.
}
\]

Checks:

- `m=2`: `Q_2=X^2-2`, `Delta=8`;
- `m=3`: `Q_3=X^3-6X`, `Delta=864`.

---

## 4. All-multiplicity hard-window flux remains bounded — PROVED

Let

\[
A_i^I:=\sum_{j\in I,\,j\ne i}\frac1{x_i-x_j}
\]

for the local `m`-root cluster and

\[
A_i^{\rm ext}=b(t,x_i),
\qquad b:=a_z/a,
\]

with `b` analytic near the collision.

The hard-window flux is

\[
\mathcal F_I
=4\sum_iA_i^IA_i^{\rm ext}.
\]

Expand

\[
b(t,x_i)=b_0+b_1(x_i-c)+O(\tau).
\]

Two exact finite-cluster identities are

\[
\boxed{\sum_iA_i^I=0}
\]

and

\[
\boxed{
\sum_i(x_i-c)A_i^I
=\binom m2=N_m.
}
\]

The second follows pairwise from

\[
\frac{x_i-c}{x_i-x_j}
+\frac{x_j-c}{x_j-x_i}=1.
\]

Since `A_i^I=O(tau^{-1/2})`, the Taylor remainder contributes only `O(sqrt(tau))`. Therefore

\[
\sum_iA_i^IA_i^{\rm ext}
=b_1N_m+O(\sqrt\tau),
\]

and hence

\[
\boxed{\mathcal F_I=O(1).}
\]

So the bounded-flux phenomenon from the double collision is universal for every finite multiplicity.

---

## 5. Universal local inverse-square energy residue — PROVED

Round 16 gives

\[
\partial_t\log\Delta_I
=4E_{\rm ord}(I)+\mathcal F_I.
\]

Combining Sections 2 and 4,

\[
\frac{N_m}{\tau}+O(1)
=4E_{\rm ord}(I)+O(1).
\]

Therefore

\[
\boxed{
E_{\rm ord}(I)
=\frac{N_m}{4\tau}+O(1)
=\frac{m(m-1)}{8\tau}+O(1).
}
\]

Equivalently the monic Hermite roots obey the exact identity

\[
\boxed{
\sum_{i\ne j}\frac1{(\xi_i-\xi_j)^2}
=\frac{m(m-1)}8.
}
\]

For `m=2` this gives `1/4`, agreeing with `xi=+-sqrt(2)`.

---

## 6. Relative log-Vandermonde entropy residue — PROVED

Assume the pair weights are locally constant and equal to `w>0` on the colliding cluster, with fixed nonzero ordered reference spacings of matching orientation.

The local ordered contribution to the Round-18 relative logarithmic entropy is

\[
\mathscr C_{\log,\rm loc}
=w\sum_{i\ne j}
\log\left|\frac{x_i-x_j}{\xi_i^{\rm ref}-\xi_j^{\rm ref}}\right|.
\]

Since

\[
\sum_{i\ne j}\log|x_i-x_j|
=\log\Delta_{\rm loc},
\]

the reference denominator contributes only `O(1)`. Hence

\[
\boxed{
\mathscr C_{\log,\rm loc}
=wN_m\log\tau+O(1)
\longrightarrow-\infty.
}
\]

Its derivative has leading term

\[
\boxed{
\partial_t\mathscr C_{\log,\rm loc}
=\frac{wN_m}{\tau}+O(1).
}
\]

Thus the singular coefficient is exactly the order of vanishing of the local discriminant.

For nonconstant smooth positive weights, the coefficient is

\[
\frac12\sum_{i\ne j}w_{ij}(t_c)
\]

provided the weights have positive limits at the collision; time derivatives of the weights produce only integrable `O(|log tau|)` terms.

---

## 7. Bregman entropy residue — PROVED

For the Round-17 pair entropy

\[
L(r)=-\log r+r-1,
\]

a locally constant unit cutoff gives

\[
\mathcal C_{\rm Breg,loc}
=\sum_{i\ne j}L(r_{ij}).
\]

At collision `r_{ij}=O(sqrt(tau))`, so

\[
L(r_{ij})=-\log r_{ij}+O(1).
\]

Therefore

\[
\boxed{
\mathcal C_{\rm Breg,loc}
=-\log\Delta_{\rm loc}+O(1)
=-N_m\log\tau+O(1)
\longrightarrow+\infty.
}
\]

Thus the missing Bregman budget is an upper bound whose exact singular coefficient is again `N_m`.

---

## 8. Resultant/discriminant interpretation — PROVED

For the monic Weierstrass polynomial,

\[
\operatorname{Disc}P
=(-1)^{N_m}\operatorname{Res}(P,P_z).
\]

For the original entire function, Round 12/16 gives the gauge-completed local section

\[
\mathcal D_I
=(-1)^{N_m}\prod_{i=1}^mF_x(t,x_i)
=\Delta_I\prod_{i=1}^ma(t,x_i).
\]

Because `a` is analytic and nonvanishing, the gauge factor stays bounded above and below near the collision. Consequently

\[
\boxed{
|\mathcal D_I|\asymp\Delta_I
\asymp\tau^{N_m}.
}
\]

Hence the following are quantitatively equivalent in a fixed local chart, up to bounded constants:

1. a lower bound on the relative log-Vandermonde entropy;
2. an upper bound on the Bregman entropy;
3. a positive lower bound on the local discriminant;
4. a positive lower bound on the gauge-completed local resultant/product `prod |F_x(x_i)|`;
5. quantitative transversality of the local root branches away from the multiple-zero divisor.

Thus the entropy budget is not an independent algebraic invariant. It is a logarithmic coordinate on the local resultant/discriminant.

---

## 9. Relation to the Round-19 Brouwer charge

For the same multiplicity `m`, Round 19 gives

\[
\boxed{
\deg_{\rm loc}(F,F_x)
=-\left\lfloor\frac m2\right\rfloor.
}
\]

Round 26 gives the discriminant vanishing order

\[
\boxed{
\operatorname{ord}_{t_c}\Delta_{\rm loc}
=\binom m2.
}
\]

These are distinct collision invariants:

- the Brouwer charge counts real/nonreal pair spectral flow and grows linearly in `m`;
- the discriminant/entropy residue counts all pairwise separations inside the cluster and grows quadratically in `m`.

Neither invariant cancels between collisions at the local level, but their global closure problems are different.

---

## 10. Consequence for Program A

Round 25's phrase “find an independent finite entropy budget” can now be sharpened.

A successful theorem must produce an independent Riemann-specific quantitative lower bound on the local discriminant/resultant, directly or indirectly. Merely renaming that bound as entropy coercivity does not reduce the difficulty.

The acceptable architecture is

\[
\boxed{
\text{independent kernel/arithmetic law}
\Longrightarrow
|\operatorname{Res}_{\rm loc}(H_t,H_t')|>0
\Longrightarrow
\text{no positive-time collision}.
}
\]

The first implication is the only genuinely new gate.

Unacceptable hidden inputs include:

- a pre-assumed lower gap;
- global real-rootedness/LP membership;
- global Laguerre positivity strong enough to imply the same transversality;
- negative-time Rodgers--Tao gap/local-equilibrium estimates proved under `Lambda<0`.

---

## 11. Next admissible target

The next test should therefore be phrased as **normalized transversality**, not as a generic entropy estimate:

> Find a Riemann-specific quantity, computable from the Fourier/theta kernel or unconditional positive-time asymptotics, that gives a lower bound on the local resultant of `(H_t,H_t')` after removing the known exponentially small amplitude normalization, without assuming real-rootedness or a gap bound.

Before attempting such a theorem globally, one must classify which natural kernel observables are collision-blind: any observable that remains analytic and finite through a multiple zero cannot by itself supply the logarithmic/discriminant lower bound unless an additional nontrivial inequality links it to the resultant.

This collision-blindness classification is the next round.

---

## 12. Status

- all-multiplicity discriminant order `binom(m,2)`: **PROVED**;
- sharp analytic remainder `Delta=tau^N(C+O(tau))`: **PROVED**;
- explicit Hermite discriminant constant: **PROVED**;
- all-multiplicity hard-window flux `O(1)`: **PROVED**;
- all-multiplicity raw-energy residue: **PROVED**;
- relative-log and Bregman entropy residues: **PROVED**;
- entropy budget locally equivalent to resultant/discriminant transversality: **PROVED in a fixed local Weierstrass chart with bounded spectators**;
- independent Riemann-specific resultant lower bound: **OPEN**;
- RH: **OPEN**;
- novelty of this packaging: **UNVERIFIED**.
