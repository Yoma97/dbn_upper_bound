# Current Collision Program State

**Updated:** 2026-08-15 after Round 17.

## Executive pivot

The primary program is

\[
\boxed{\text{Local Relative Vandermonde/Hamiltonian Renormalization + Explicit Flux}.}
\]

A canonical finite global regularized discriminant is **not assumed**. The fundamental object is now a localized relative Bregman entropy of the zero configuration against the Rodgers--Tao classical locations, together with an exact bulk/flux/reference balance law.

Round 15 finite-order oscillatory sign-regularity remains frozen/auxiliary.

---

## 1. Local collision geometry — PROVED

For a finite simple real-zero cluster `I` of a real entire backward-heat family

\[
\partial_tF=-F_{xx},
\]

the local collision section

\[
\mathcal D_I=(-1)^{m(m-1)/2}\prod_{i\in I}F_x(t,x_i(t))
\]

factorizes in a zero chart as

\[
\mathcal D_I=\Delta_I\prod_{i\in I}a(t,x_i),
\qquad
\Delta_I=\prod_{i<j\in I}(x_i-x_j)^2,
\]

with `a` analytic and nonvanishing. The fixed-root inverse-square trace

\[
B_i=\sum_{\rho\ne x_i}(x_i-\rho)^{-2}
\]

is absolutely convergent for an order-one entire divisor. Global positive pair energy, not the fixed-root trace, is the infinite-volume divergence problem.

---

## 2. Finite factor conventions — PROVED

For a finite monic heat polynomial

\[
E_{\rm unord}=\sum_{i<j}(x_i-x_j)^{-2},
\qquad
E_{\rm ord}=\sum_{i\ne j}(x_i-x_j)^{-2}=2E_{\rm unord},
\]

one has

\[
\partial_t\log\Delta=8E_{\rm unord}=4E_{\rm ord}.
\]

With the ordered Hamiltonian

\[
\mathcal H=\sum_{i\ne j}\log|x_i-x_j|^{-1},
\]

\[
\mathcal H=-\log\Delta,
\qquad
\dot{\mathcal H}=-4E_{\rm ord}.
\]

Thus finite discriminant and inverse-square energy are literally the same gradient-flow object.

---

## 3. Raw hard-window flux law — PROVED

For a finite zero window `I`, with

\[
A_i^I=\sum_{j\in I,j\ne i}(x_i-x_j)^{-1},
\qquad
A_i^{\rm ext}=A_i-A_i^I,
\]

\[
\boxed{
\partial_t\log\Delta_I
=4E_{\rm ord}(I)+4\sum_{i\in I}A_i^I A_i^{\rm ext}.
}
\]

Near an isolated generic double collision the bulk term is

\[
4E_{\rm ord}(I)=\frac1{t-t_c}+O((t-t_c)^{-1/2}),
\]

while the analytic local external flux is bounded after the leading constant-field cancellation. Hence the logarithmic collision divergence is an internal bulk singularity.

---

## 4. Round 17 relative Bregman entropy — PROVED FINITELY

Let `xi_j` be any fixed strictly ordered reference configuration, `psi_j` a time-independent cutoff, and

\[
r_{jk}=\frac{x_j-x_k}{\xi_j-\xi_k}>0,
\qquad
L(r)=-\log r+r-1.
\]

Define the ordered relative entropy

\[
\boxed{
\mathcal C_\psi(x\mid\xi)
=\sum_{j\ne k}\psi_j\psi_kL(r_{jk}).
}
\]

Set

\[
\delta_{jk}=\frac1{x_j-x_k}-\frac1{\xi_j-\xi_k},
\]

\[
D_j^\psi=\sum_{k\ne j}\psi_k\delta_{jk},
\qquad
F_j^\psi=\sum_{k\ne j}(1-\psi_k)\delta_{jk},
\]

and

\[
S_j^\xi=\sum_{k\ne j}(\xi_j-\xi_k)^{-1}.
\]

Then the exact finite balance law is

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
\mathscr B_\psi=4\sum_j\psi_j(D_j^\psi)^2\ge0,
}
\]

\[
\boxed{
\mathscr F_{\partial\psi}=-4\sum_j\psi_jD_j^\psi F_j^\psi,
}
\]

and

\[
\boxed{
\mathscr R_{\xi,\psi}=-4\sum_j\psi_jD_j^\psi S_j^\xi.
}
\]

Thus the previously anticipated background/reference commutator is not an unknown artifact for this Bregman choice: it is the explicit reference-force term above.

The countable Riemann version remains **CONDITIONAL** on the justified principal-value/difference-sum limits and cutoff dominated-convergence bookkeeping.

---

## 5. Collision blow-up in the relative entropy law — PROVED LOCALLY

For a hard cutoff containing an isolated generic colliding pair, Polymath Hermite splitting gives

\[
g(t)^2=8(t-t_c)+O((t-t_c)^{3/2}).
\]

The localized reciprocal-gap defect forces satisfy

\[
D_p=-g^{-1}+O(1),
\qquad
D_q=g^{-1}+O(1),
\]

so

\[
\boxed{
\mathscr B_I(t)=\frac1{t-t_c}+O((t-t_c)^{-1/2}).
}
\]

Under isolated-collision regularity, the flux and reference terms are at worst `O((t-t_c)^(-1/2))` and are time-integrable. Hence

\[
\partial_t\mathcal C_I=-\frac1{t-t_c}+O((t-t_c)^{-1/2}),
\]

and

\[
\boxed{
\mathcal C_I(t)=-\log(t-t_c)+O(1).
}
\]

The non-integrable singularity is therefore carried by the positive bulk defect-force dissipation.

---

## 6. Exact quadratic bridge to Rodgers--Tao V-energy — PROVED

For the exact arithmetic reference

\[
\xi_j=aj,
\qquad
x_j=aj+\varepsilon q_j,
\]

with finitely supported `q`, define

\[
\mathcal A q_j=\sum_{k\ne j}\frac{q_j-q_k}{(j-k)^2}.
\]

Then

\[
D_j=-\frac{\varepsilon}{a^2}\mathcal A q_j+O(\varepsilon^2).
\]

The discrete Fourier identity

\[
\boxed{
\sum_j(\mathcal A q_j)^2
=3\sum_{j\ne k}\frac{(q_j-q_k)^2}{(j-k)^4}
}
\]

follows from the multiplier

\[
m(\theta)=2\sum_{n\ge1}\frac{1-\cos(n\theta)}{n^2}
=\pi|\theta|-\frac{\theta^2}{2}
\]

and

\[
m(\theta)^2
=12\sum_{n\ge1}\frac{1-\cos(n\theta)}{n^4}.
\]

Since Rodgers--Tao use

\[
V(r)=r^{-2}-1+2(r-1)=3(r-1)^2+O((r-1)^3),
\]

their pairwise relative `V`-energy satisfies

\[
\boxed{
\sum_jD_j^2=\widetilde E_V+O(\varepsilon^3)
}
\]

near an exact lattice. Thus their positive renormalized energy is exactly the Hessian-level dissipation of the nonlinear Bregman entropy law.

**Novelty of this packaging:** NOVELTY UNVERIFIED.

---

## 7. Actual Rodgers--Tao reference — SOURCE-LOCKED

The classical locations are defined by

\[
\Psi(T)=\frac{T}{4\pi}\log\frac{T}{4\pi}-\frac{T}{4\pi},
\qquad
\Psi(\xi_j)=j,
\qquad
\xi_{-j}=-\xi_j.
\]

They satisfy

\[
|\xi_k-\xi_j|\asymp
\frac{|k-j|}{\log_+(|\xi_j|+|\xi_k|)},
\]

and locally, for `1 <= j asymp k`,

\[
\xi_k-\xi_j
=\frac{4\pi(k-j)}{\log\xi_j}
+O\left(\frac{|k-j|^2}{j\log^2\xi_j}\right).
\]

The next task is therefore no longer algebraic. It is to estimate the exact reference force

\[
S_j^\xi=\operatorname{PV}\sum_{k\ne j}(\xi_j-\xi_k)^{-1}
\]

and then the two explicit channels `F_{partial psi}` and `R_{xi,psi}` for the actual variable-density reference and an admissible exhaustion cutoff.

---

## 8. Immediate next theorem targets

### Target A1 — Reference-force asymptotic
Derive a rigorous asymptotic or sufficiently sharp slowly-varying estimate for

\[
S_j^\xi.
\]

Exploit the exact cancellation

\[
\sum_j\psi_jD_j^\psi=0,
\]

so only the variation of `S_j^xi` across the window enters the reference term:

\[
\mathscr R_{\xi,\psi}
=-4\sum_j\psi_jD_j^\psi(S_j^\xi-c)
\]

for any constant `c`.

### Target A2 — Boundary-flux estimate
Bound

\[
\mathscr F_{\partial\psi}
=-4\sum_j\psi_jD_j^\psi F_j^\psi
\]

in terms of the bulk dissipation plus an explicitly controlled boundary cost, preferably via Cauchy--Schwarz / Young with a cutoff-gradient norm.

### Target A3 — Nonlinear comparison
Go beyond the quadratic lattice identity and seek a one-sided comparison between

\[
\sum_j\psi_j(D_j^\psi)^2
\]

and Rodgers--Tao's pairwise `V`-energy in a quantitatively specified moderate-deformation regime.

No target may assume a global lower gap bound, RH, `Lambda<=0`, or all-time real-rootedness.

---

## 9. Program ranking

\[
\boxed{A\gg B>C.}
\]

### A — PRIMARY
Relative Bregman/Vandermonde entropy + explicit bulk/flux/reference balance.

### B — SECONDARY
Renormalized collision degree with full boundary control.

### C — TERTIARY
Low-complexity arithmetic separator.

The phase-current route is permanently removed as independent (`J=-L1`). Round-15 sign-regularity remains frozen/auxiliary.

---

## 10. Status

- local collision divisor geometry: **PROVED**;
- raw hard-window Vandermonde flux identity: **PROVED**;
- exact finite smooth-cutoff Bregman balance: **PROVED**;
- explicit bulk/flux/reference decomposition: **PROVED**;
- generic-collision non-integrable bulk vs integrable lower-order channels: **PROVED locally**;
- exact quadratic lattice identity: **PROVED**;
- second-order matching to Rodgers--Tao `V`-energy: **PROVED**;
- infinite Riemann exhaustion identity: **CONDITIONAL / bookkeeping not yet closed**;
- actual-reference force asymptotic: **OPEN — NEXT**;
- boundary/reference time-integral control: **OPEN**;
- nonlinear bulk versus `V` comparison: **OPEN**;
- no-collision theorem: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
