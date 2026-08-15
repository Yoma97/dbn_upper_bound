# Current Collision Program State

**Updated:** 2026-08-15 after Round 18.

**RH status:** OPEN.

## Executive state

The primary structural architecture remains

\[
\boxed{\text{Local/Relative Vandermonde--Hamiltonian Renormalization + Explicit Flux}.}
\]

But Round 18 corrects the main analytic gate:

\[
\boxed{\text{flux control alone is not a no-collision mechanism}.}
\]

The true missing ingredient is an **independent finite entropy/coercive budget** (or a compensated quantity with independently controlled collision behavior).

Round 15 finite oscillatory sign-regularity remains **FROZEN / AUXILIARY**.

---

## 1. Local collision section — PROVED

For a finite simple real-zero cluster \(I\) of

\[
\partial_tF=-F_{xx},
\]

write locally

\[
F(t,z)=a(t,z)\prod_{i\in I}(z-x_i(t)),
\qquad a(t,z)\ne0.
\]

Define

\[
\Delta_I=\prod_{i<j\in I}(x_i-x_j)^2,
\]

and

\[
\mathcal D_I=(-1)^{m(m-1)/2}\prod_{i\in I}F_x(t,x_i).
\]

Then

\[
\boxed{\mathcal D_I=\Delta_I\prod_{i\in I}a(t,x_i).}
\]

Thus \(\Delta_I\) is zero-set-only, while \(\mathcal D_I\) is a gauge-completed local entire-function section. No global canonical regularized discriminant is assumed.

---

## 2. Fixed-root trace versus infinite-volume energy — PROVED / CORRECTED

At a simple root,

\[
A_i=\frac{F_{xx}}{2F_x}(t,x_i).
\]

The fixed-root inverse-square trace is absolutely convergent for an order-one zero divisor:

\[
\boxed{B_i=\sum_{\rho\ne x_i}\frac1{(x_i-\rho)^2}.}
\]

The first-order velocity field requires principal-value/canonical pairing in the infinite system, while the real divergence problem is the global positive pair energy

\[
\sum_i\sum_{j\ne i}\frac1{(x_i-x_j)^2}.
\]

---

## 3. Finite factor conventions — PROVED

For a finite zero set,

\[
E_{\rm ord}=\sum_{i\ne j}\frac1{(x_i-x_j)^2},
\qquad
E_{\rm unord}=\sum_{i<j}\frac1{(x_i-x_j)^2}.
\]

Then

\[
\boxed{\partial_t\log\Delta=4E_{\rm ord}=8E_{\rm unord}.}
\]

For the ordered Hamiltonian

\[
\mathcal H=\sum_{i\ne j}\log\frac1{|x_i-x_j|},
\]

\[
\boxed{\mathcal H=-\log\Delta,\qquad \dot{\mathcal H}=-4E_{\rm ord}.}
\]

---

## 4. Hard-window Vandermonde flux — PROVED

For a finite window \(I\), define

\[
A_i^I=\sum_{j\in I,\,j\ne i}\frac1{x_i-x_j},
\qquad
A_i^{\rm ext}=A_i-A_i^I.
\]

Then

\[
\boxed{\frac d{dt}\log\Delta_I=4E_{\rm ord}(I)+\mathcal F_I,}
\]

with

\[
\boxed{\mathcal F_I=4\sum_{i\in I}A_i^IA_i^{\rm ext}.}
\]

The local factorization gives

\[
\boxed{A_i^{\rm ext}=\frac{a_z}{a}(t,x_i).}
\]

---

## 5. Generic double collision — SHARPENED

Let \(\tau=t-t_c\downarrow0\). For an isolated generic analytic double collision, the square of the gap is the analytic discriminant of the local Weierstrass quadratic. The heat equation fixes its first derivative, yielding

\[
\boxed{g(\tau)^2=8\tau+O(\tau^2).}
\]

Therefore

\[
\boxed{E_{\rm pair,ord}=\frac2{g^2}=\frac1{4\tau}+O(1),}
\]

and

\[
\boxed{4E_{\rm pair,ord}=\frac1\tau+O(1).}
\]

For a hard window containing the isolated pair,

\[
\boxed{\mathcal F_I=O(1).}
\]

The previous weaker \(O(\tau^{-1/2})\) remainder for the raw pair energy is superseded.

---

## 6. Round 17 Bregman law — PROVED / RETAINED

For a fixed reference \(\xi_j\), Round 17 defines

\[
L(r)=-\log r+r-1\ge0
\]

and a positive localized Bregman entropy. Its exact derivative decomposes as

\[
\partial_t\mathcal C_\psi=-\mathscr B_\psi+\mathscr F_{\partial\psi}+\mathscr R_{\xi,\psi},
\]

where

\[
\mathscr B_\psi=4\sum_j\psi_j(D_j^\psi)^2\ge0.
\]

This theorem is valid and useful. Its bulk is a **squared reciprocal-gap defect force**. At an exact arithmetic lattice this force-square bulk agrees to quadratic order with the Rodgers--Tao \(V\)-energy.

However, the Bregman bulk is not the pairwise \(V\)-energy exactly for a general configuration/reference.

---

## 7. Exact smooth pair-cutoff \(V\)-energy law — PROVED IN ROUND 18

Let \(w_{jk}=w_{kj}\ge0\), \(w_{jj}=0\), be a fixed symmetric pair cutoff and define

\[
\mathscr C_w=\sum_{j\ne k}w_{jk}\log\left|\frac{x_j-x_k}{\xi_j-\xi_k}\right|.
\]

Set

\[
a_{jk}=\frac1{x_j-x_k},\qquad b_{jk}=\frac1{\xi_j-\xi_k},\qquad \eta_j=x_j-\xi_j.
\]

Define

\[
A_j^w=\sum_{k\ne j}w_{jk}a_{jk},
\qquad
A_j=\operatorname{PV}\sum_{i\ne j}a_{ji}.
\]

Then exactly

\[
\boxed{\partial_t\mathscr C_w=4S_w(x),\qquad S_w(x)=\sum_jA_jA_j^w.}
\]

Write

\[
S_w(x)=E_w(x)+K_w(x),
\]

where

\[
E_w(x)=\sum_{j\ne k}w_{jk}a_{jk}^2
\]

and

\[
K_w(x)=\sum_j\sum_{\substack{i,k\ne j\\i\ne k}}w_{jk}a_{ji}a_{jk}.
\]

The triple partial-fraction identity shows that \(K_w\) vanishes on triples whose three pair weights are equal. Thus it is an exact discrete cutoff/boundary commutator.

For

\[
V(r)=r^{-2}-1+2(r-1),
\]

define

\[
\widetilde E_w^V
=\sum_{j\ne k}w_{jk}\frac1{(\xi_j-\xi_k)^2}
V\left(\frac{x_j-x_k}{\xi_j-\xi_k}\right)\ge0,
\]

and

\[
\Lambda_w(\eta)=\sum_{j\ne k}w_{jk}\frac{\eta_j-\eta_k}{(\xi_j-\xi_k)^3}.
\]

With \(S_w(\xi)=E_w(\xi)+K_w(\xi)\), one obtains

\[
\boxed{\partial_t\mathscr C_w=4\widetilde E_w^V+4\mathscr F_w+4\mathscr R_w,}
\]

where

\[
\boxed{\mathscr F_w=K_w(x)-K_w(\xi),}
\]

and

\[
\boxed{\mathscr R_w=S_w(\xi)-2\Lambda_w(\eta).}
\]

Thus the desired bulk can be identified **exactly** with the Rodgers--Tao positive \(V\)-renormalized pair energy. The reference/cutoff channels remain fully explicit.

For the Rodgers--Tao choice

\[
w_{jk}=\psi_T(j)\psi_T(k)1_{j\sim_T k},
\]

this is the exact algebraic bookkeeping underlying their asymptotic truncated Hamiltonian identity, with opposite sign under their \(\log(1/|d|)\) convention.

**Novelty of this packaging:** UNVERIFIED.

---

## 8. Fundamental obstruction — PROVED

The implication

\[
\text{non-integrable internal energy}+\text{integrable boundary flux}\Rightarrow\text{no collision}
\]

is false.

Counterexample:

\[
P_t(z)=z^2-2t,
\qquad
\partial_tP_t=-P_t''.
\]

For \(t>0\), the roots are \(\pm\sqrt{2t}\) and collide at \(t=0\). Taking the window of all roots gives

\[
\mathcal F_I=0,
\]

while

\[
\Delta_I=8t,
\qquad
E_{\rm ord}=\frac1{4t},
\]

so

\[
\boxed{\partial_t\log\Delta_I=\frac1t,\qquad \mathcal F_I=0.}
\]

The bulk divergence is absorbed by \(\log\Delta_I\to-\infty\). Likewise, the positive Bregman entropy diverges to \(+\infty\) at collision.

Therefore controlling only \(\int(\mathscr F+\mathscr R)dt\) is insufficient. The divergence does not need to be hidden in the flux; it is already carried by the entropy variation itself.

---

## 9. New primary Gate A — FINITE ENTROPY/COERCIVE BUDGET

A no-collision theorem from Program A now requires an additional independent input.

### A1. One-sided finite entropy budget

Establish, from Riemann-specific information not equivalent to no-collision, a one-sided bound preventing the relevant localized entropy from reaching its collision-divergent value in finite time.

### A2. Compensated functional

Construct

\[
\mathscr Q_w=\mathscr C_w+\text{canonical analytic/reference correction}
\]

such that the local collision logarithm cancels for a structural reason, while the evolution retains a positive/coercive bulk and controlled boundary terms. A subtraction inserted merely because it removes \(\log g\) is not acceptable.

### A3. Entire-function finite budget

Use a normalization-sensitive local section such as \(\mathcal D_I\), together with proved control of its zero-free gauge, to transfer an independent entire-function bound to the zero-set entropy. The gauge must be shown not to carry the same missing logarithmic divergence.

Without A1, A2, or A3, Program A is a diagnostic balance law rather than a collision-exclusion proof.

---

## 10. Circularity guard

For an attempted proof of RH via the de Bruijn--Newman flow, assuming

\[
\Lambda>0
\]

for contradiction and working on \(t>\Lambda\) is legitimate and does not assume RH.

However, Rodgers--Tao's quantitative negative-time estimates are developed under their contradiction hypothesis

\[
\Lambda<0,
\]

which implies RH and supplies a real-simple interval extending to \(t=0\). Those estimates cannot be transplanted into the \(\Lambda>0\) contradiction regime without independent proof.

Safe imports are algebraic definitions/identities and unconditional positive-time estimates. Every Riemann-specific estimate used toward \(\Lambda\le0\) must be checked for this direction of implication.

---

## 11. Laguerre and degree status

Ordinary

\[
L_1=(H')^2-HH''\ge0
\]

is only a necessary condition for Laguerre--Polya membership in general. The generalized real Laguerre hierarchy and complex Laguerre criterion give the relevant complete characterizations.

For

\[
\Gamma(t,x)=(H_t(x),H_t'(x)),
\]

a generic isolated double collision has local Brouwer index \(-1\). Higher multiplicity requires separate local degree analysis.

Program B remains secondary but becomes more conceptually relevant because a degree can potentially provide a finite topological budget that the divergent entropy lacks.

---

## 12. Program ranking

\[
\boxed{A>B>C}
\]

### A — PRIMARY STRUCTURAL / ANALYTIC

Exact relative Vandermonde identities, exact \(V\)-bulk, explicit boundary/reference commutators, **plus the search for an independent finite entropy/coercive budget**.

### B — SECONDARY

Renormalized Brouwer degree with full boundary control.

### C — TERTIARY

Low-complexity arithmetic separator, only after non-density/non-equivalence is proved.

Round 15 sign-regularity: **FROZEN / AUXILIARY**.

---

## 13. Current status table

- local collision divisor geometry: **PROVED**;
- fixed-root inverse-square trace: **PROVED**;
- global canonical regularized discriminant: **NOT ASSUMED / OPEN**;
- hard-window Vandermonde flux identity: **PROVED**;
- analytic external field formula \(A_i^{ext}=a_z/a\): **PROVED locally**;
- sharpened generic double-collision law \(g^2=8\tau+O(\tau^2)\): **PROVED under generic analytic double collision**;
- raw hard-window flux \(O(1)\): **PROVED locally**;
- Round-17 Bregman force-square law: **PROVED**;
- exact smooth symmetric-pair-cutoff relative log-Vandermonde law: **PROVED**;
- exact bulk equality with Rodgers--Tao \(V\)-energy: **PROVED algebraically**;
- discrete triple cutoff commutator: **PROVED**;
- explicit reference/tangent remainder: **PROVED**;
- “integrable flux prevents collision”: **REFUTED**;
- finite entropy/coercive budget: **OPEN — PRIMARY GATE**;
- Riemann-specific estimates in the \(\Lambda>0\) contradiction regime: **OPEN**;
- independent no-collision theorem: **OPEN**;
- RH: **OPEN**;
- novelty of the exact packaging: **UNVERIFIED**.
