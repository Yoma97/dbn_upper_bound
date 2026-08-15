# Round 17 — Exact smooth-cutoff relative Bregman entropy law

**Date:** 2026-08-15

**Status labels:** PROVED / CONDITIONAL / CANDIDATE / REFUTED / NOVELTY UNVERIFIED.

**RH status:** OPEN.

## 0. Purpose

This round implements the corrected Program A:

> Local relative Vandermonde/Hamiltonian renormalization with explicit boundary flux.

The goal is not a global finite discriminant. The goal is an exact localized balance law relative to a static ordered reference configuration \(\xi_j\), with every boundary/reference term exposed.

Rodgers--Tao use the zero ODE

\[
\dot x_j=2\,\mathrm{PV}\sum_{k\ne j}\frac1{x_j-x_k}
\]

in the real-simple regime and introduce spatial cutoffs plus the reference points \(\xi_j\). Their Proposition 22 proves an asymptotic relation

\[
\partial_t\widetilde{\mathcal H}_T=-4\widetilde E_T+\text{negligible terms}.
\]

The present calculation isolates an exact algebraic precursor valid for an arbitrary static reference and arbitrary finite-support smooth index cutoff.

---

## 1. Setup

Let \(J\) be a finite index set first. Let

\[
x_j(t),\qquad j\in J,
\]

be strictly ordered real simple zero branches satisfying

\[
\dot x_j=2S_j^x,
\qquad
S_j^x:=\sum_{k\ne j}\frac1{x_j-x_k}.
\]

Let \((\xi_j)_{j\in J}\) be a fixed strictly ordered reference configuration with the same ordering. Set

\[
d_{jk}:=x_j-x_k,
\qquad
d^0_{jk}:=\xi_j-\xi_k,
\qquad
r_{jk}:=\frac{d_{jk}}{d^0_{jk}}>0.
\]

Let \(0\le \psi_j\le1\) be fixed in time. Define

\[
L(r):=-\log r+r-1\ge0
\]

and the ordered relative Bregman entropy

\[
\boxed{
\mathcal C_\psi(x\mid\xi)
:=\sum_{j\ne k}\psi_j\psi_k L(r_{jk}).
}
\]

This is zero-set invariant and independent of multiplication of the underlying entire function by a zero-free factor.

Define the reciprocal-gap defect

\[
\delta_{jk}
:=\frac1{x_j-x_k}-\frac1{\xi_j-\xi_k}.
\]

For each index \(j\), define the localized defect force

\[
D_j^\psi:=\sum_{k\ne j}\psi_k\delta_{jk},
\]

the complementary defect force

\[
F_j^\psi:=\sum_{k\ne j}(1-\psi_k)\delta_{jk},
\]

and the reference force

\[
S_j^\xi:=\sum_{k\ne j}\frac1{\xi_j-\xi_k}.
\]

Then exactly

\[
S_j^x=S_j^\xi+D_j^\psi+F_j^\psi.
\]

---

## 2. Exact balance law — PROVED

Because

\[
L'(r)=1-\frac1r,
\]

we have

\[
\frac d{dt}L(r_{jk})
=(\dot x_j-\dot x_k)
\left(\frac1{d^0_{jk}}-\frac1{d_{jk}}\right)
=-(\dot x_j-\dot x_k)\delta_{jk}.
\]

Summing with the symmetric pair weight \(\psi_j\psi_k\) and desymmetrizing,

\[
\frac d{dt}\mathcal C_\psi
=-2\sum_j\psi_j\dot x_jD_j^\psi.
\]

Using \(\dot x_j=2S_j^x\),

\[
\frac d{dt}\mathcal C_\psi
=-4\sum_j\psi_jD_j^\psi S_j^x.
\]

Substitute

\[
S_j^x=S_j^\xi+D_j^\psi+F_j^\psi.
\]

Therefore

\[
\boxed{
\partial_t\mathcal C_\psi
=-\mathscr B_\psi
+\mathscr F_{\partial\psi}
+\mathscr R_{\xi,\psi},
}
\]

where

\[
\boxed{
\mathscr B_\psi
:=4\sum_j\psi_j\left(D_j^\psi\right)^2\ge0,
}
\]

\[
\boxed{
\mathscr F_{\partial\psi}
:=-4\sum_j\psi_jD_j^\psi F_j^\psi,
}
\]

and

\[
\boxed{
\mathscr R_{\xi,\psi}
:=-4\sum_j\psi_jD_j^\psi S_j^\xi.
}
\]

This is an exact identity in the finite system.

### Interpretation

- \(\mathscr B_\psi\): positive bulk dissipation, the square of the localized reciprocal-gap defect force;
- \(\mathscr F_{\partial\psi}\): interaction of the localized defect with the complement of the cutoff;
- \(\mathscr R_{\xi,\psi}\): exact defect caused by the fact that the chosen reference is not a true stationary configuration.

Thus the previously anticipated `reference/background commutator` is not mysterious: for this Bregman choice it is exactly \(\mathscr R_{\xi,\psi}\).

---

## 3. Infinite-volume extension — CONDITIONAL but standard in form

For a countable ordered configuration, the same identity holds provided:

1. the zero velocity principal values \(S_j^x\) exist;
2. \(S_j^\xi\) exists in the same principal-value convention;
3. the difference sums \(\sum_{k\ne j}\delta_{jk}\) converge absolutely (or under a specified stronger common summation convention);
4. \(\psi\) has finite support, or sufficient decay to justify the pair summation and differentiation.

In the Rodgers--Tao regime, the velocity principal value is established for the real-simple zero process, and their comparison \(x_j-\xi_j\) together with reciprocal-gap estimates is exactly the type of input needed to justify the localized difference sums. This round does not re-prove their full dominated-convergence bookkeeping.

---

## 4. Hard-window reduction and collision singularity — PROVED

Take \(\psi=1_I\) for a finite index window \(I\). Then

\[
D_j^I=\sum_{k\in I,\,k\ne j}\delta_{jk}.
\]

Suppose two indices \(p,q\in I\) undergo an isolated generic double collision at \(t=t_c\), while the reference gap \(\xi_p-\xi_q\ne0\) stays fixed and all other zeros stay separated.

From the Polymath Hermite splitting law,

\[
g(t):=x_q-x_p
=2\sqrt{2(t-t_c)}+O(t-t_c),
\]

so

\[
g(t)^2=8(t-t_c)+O((t-t_c)^{3/2}).
\]

The two localized defect forces satisfy

\[
D_p^I=-\frac1g+O(1),
\qquad
D_q^I=\frac1g+O(1).
\]

Hence

\[
\mathscr B_I
=4\left((D_p^I)^2+(D_q^I)^2\right)+O(1)
=\frac8{g^2}+O(g^{-1}),
\]

and therefore

\[
\boxed{
\mathscr B_I(t)
=\frac1{t-t_c}+O((t-t_c)^{-1/2}).
}
\]

The flux/reference terms are at worst \(O(g^{-1})=O((t-t_c)^{-1/2})\) under an isolated collision with regular external/reference fields. Thus they are locally time-integrable, while \(\mathscr B_I\) is not.

Consequently

\[
\boxed{
\partial_t\mathcal C_I
=-\frac1{t-t_c}+O((t-t_c)^{-1/2}),
}
\]

and

\[
\boxed{
\mathcal C_I(t)=-\log(t-t_c)+O(1)
\qquad(t\downarrow t_c).
}
\]

So the non-integrable collision singularity is entirely a bulk defect-force singularity; boundary/reference terms cannot cancel it if they remain regular in the above sense.

---

## 5. Exact quadratic matching with Rodgers--Tao's V-energy at an arithmetic reference — PROVED

This is the key new structural bridge.

Let the reference be the exact lattice

\[
\xi_j=aj,
\qquad j\in\mathbb Z,
\qquad a>0,
\]

and perturb it by

\[
x_j=aj+\varepsilon q_j,
\]

where \(q\) has finite support and \(|\varepsilon|\) is small enough to preserve ordering.

The lattice reference has

\[
\mathrm{PV}\sum_{k\ne j}\frac1{a(j-k)}=0.
\]

For the full cutoff \(\psi\equiv1\),

\[
D_j
=\sum_{k\ne j}\left(
\frac1{x_j-x_k}-\frac1{a(j-k)}
\right)
=-\frac{\varepsilon}{a^2}\,\mathcal A q_j+O(\varepsilon^2),
\]

where

\[
\mathcal A q_j
:=\sum_{k\ne j}\frac{q_j-q_k}{(j-k)^2}.
\]

Hence

\[
\sum_jD_j^2
=\frac{\varepsilon^2}{a^4}\sum_j(\mathcal A q_j)^2+O(\varepsilon^3).
\]

Rodgers--Tao use

\[
V(r)=\frac1{r^2}-1+2(r-1),
\]

for which

\[
V(1+u)=3u^2+O(u^3).
\]

Their pairwise relative energy around the exact lattice has quadratic part

\[
\widetilde E_V
=\frac{3\varepsilon^2}{a^4}
\sum_{j\ne k}\frac{(q_j-q_k)^2}{(j-k)^4}
+O(\varepsilon^3).
\]

Now the following discrete Fourier identity holds for finitely supported \(q\):

\[
\boxed{
\sum_j\left(
\sum_{k\ne j}\frac{q_j-q_k}{(j-k)^2}
\right)^2
=
3\sum_{j\ne k}\frac{(q_j-q_k)^2}{(j-k)^4}.
}
\]

### Proof

On the Fourier side, the operator \(\mathcal A\) has multiplier

\[
m(\theta)
=2\sum_{n\ge1}\frac{1-\cos(n\theta)}{n^2}
=\pi|\theta|-\frac{\theta^2}{2},
\qquad |\theta|\le\pi.
\]

Also

\[
12\sum_{n\ge1}\frac{1-\cos(n\theta)}{n^4}
=\pi^2\theta^2-\pi|\theta|^3+\frac{\theta^4}{4}
=m(\theta)^2.
\]

Plancherel gives the identity.

Therefore

\[
\boxed{
\sum_jD_j^2
=\widetilde E_V+O(\varepsilon^3),
}
\]

and the exact entropy law yields

\[
\boxed{
\partial_t\mathcal C
=-4\widetilde E_V+O(\varepsilon^3)
}
\]

around an exact arithmetic equilibrium.

This explains structurally why Rodgers--Tao's renormalized \(V\)-energy is the correct quadratic dissipation near local equilibrium: it is the Hessian-level form of the exact nonlinear defect-force dissipation obtained here.

**Novelty of this packaging/identity:** NOVELTY UNVERIFIED.

---

## 6. Relation to Round 16 and Rodgers--Tao

Round 16 derived for a hard raw Vandermonde window

\[
\partial_t\log\Delta_I
=4E_{\mathrm{ord}}(I)+\text{external flux}.
\]

The present relative Bregman law is the renormalized companion:

\[
\partial_t\mathcal C_\psi
=-\mathscr B_\psi
+\mathscr F_{\partial\psi}
+\mathscr R_{\xi,\psi}.
\]

The two laws serve different purposes:

- raw Vandermonde exposes the classical positive inverse-square blow-up directly;
- relative Bregman entropy cancels the equilibrium background and produces a positive squared defect-force bulk term;
- at an exact arithmetic background, this bulk term agrees to second order with Rodgers--Tao's \(V\)-renormalized energy;
- cutoff and variable-density reference effects are isolated explicitly in \(\mathscr F_{\partial\psi}\) and \(\mathscr R_{\xi,\psi}\).

Rodgers--Tao Proposition 22 proves, after detailed asymptotic estimates, that their windowed renormalized Hamiltonian obeys

\[
\partial_t\widetilde{\mathcal H}_T
=-4\widetilde E_T+o(T\log^3T+\widetilde E_T).
\]

The present theorem does **not** replace those estimates. It supplies an exact algebraic balance law whose error channels are explicit before asymptotic estimation.

---

## 7. Circularity audit

No step above assumes:

- RH;
- \(\Lambda\le0\);
- all zeros remain real below an unknown collision time;
- global Laguerre positivity;
- a lower gap bound that already excludes collision.

The finite identity is purely algebraic once the zero ODE is valid. The Riemann application is legitimate only on a real-simple interval where the zero branches and principal-value velocities are justified.

---

## 8. What remains open

The exact balance law does **not** prevent a collision by itself. A collision sends

\[
\mathcal C_I(t)\to+\infty
\]

when approached backward, and the balance law merely identifies the non-integrable mechanism.

The next analytic question is now sharply formulated:

> For the Riemann zero process and the Rodgers--Tao variable-density reference \(\xi_j\), can one prove on an exhaustion family of cutoffs that the time integrals of
> \[
> \mathscr F_{\partial\psi}+\mathscr R_{\xi,\psi}
> \]
> remain controlled strongly enough that a bulk divergence \(\int \mathscr B_\psi dt=+\infty\) cannot be hidden by boundary/reference transport?

A global uniform bound equivalent to no-collision is rejected. The first target is a local/windowed flux estimate with explicit dependence on cutoff width and reference density.

---

## 9. Status table

- exact finite smooth-cutoff Bregman balance: **PROVED**;
- explicit bulk/flux/reference decomposition: **PROVED**;
- generic-collision non-integrable bulk vs integrable flux/reference: **PROVED under isolated-collision regularity**;
- exact quadratic lattice identity: **PROVED**;
- second-order matching to Rodgers--Tao \(V\)-energy: **PROVED**;
- infinite Riemann exhaustion estimates: **OPEN**;
- no-collision theorem: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
