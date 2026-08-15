# Current Collision Program State

**Updated:** 2026-08-15 after Round 19.

**RH status:** OPEN.

## Executive state

Two complementary structures are now rigorously established:

\[
\boxed{\text{A: exact relative Vandermonde / V-energy / flux identities}}
\]

and

\[
\boxed{\text{B: all-multiplicity negative local collision degree}.}
\]

Round 18 proved that **flux control alone cannot exclude collision**: the entropy itself carries the logarithmic collision divergence. Round 19 then proved that every isolated multiplicity-\(m\) heat collision has local Brouwer degree

\[
\boxed{-\lfloor m/2\rfloor<0.}
\]

Thus the working priority is upgraded to

\[
\boxed{B\gtrsim A\gg C.}
\]

Round 15 finite oscillatory sign-regularity remains **FROZEN / AUXILIARY**.

---

## 1. Local collision section — PROVED

For a finite simple real-zero cluster \(I\) of

\[
\partial_tF=-F_{xx},
\]

write locally

\[
F(t,z)=a(t,z)\prod_{i\in I}(z-x_i(t)),\qquad a(t,z)\ne0.
\]

Then

\[
\Delta_I=\prod_{i<j\in I}(x_i-x_j)^2,
\]

and

\[
\mathcal D_I=(-1)^{m(m-1)/2}\prod_{i\in I}F_x(t,x_i)
=\Delta_I\prod_{i\in I}a(t,x_i).
\]

Thus \(\Delta_I\) is zero-set-only, while \(\mathcal D_I\) is a gauge-completed local entire-function section. No global canonical regularized discriminant is assumed.

---

## 2. Fixed-root trace versus infinite-volume energy — PROVED / CORRECTED

At a simple root,

\[
A_i=\frac{F_{xx}}{2F_x}(t,x_i).
\]

The fixed-root inverse-square trace

\[
\boxed{B_i=\sum_{\rho\ne x_i}\frac1{(x_i-\rho)^2}}
\]

is absolutely convergent for an order-one zero divisor. The first-order velocity field requires a principal-value/canonical-pairing convention in the infinite system. The true infinite-volume divergence is the global positive pair energy.

---

## 3. Finite Vandermonde conventions — PROVED

For a finite zero set,

\[
E_{\rm ord}=\sum_{i\ne j}(x_i-x_j)^{-2},
\qquad
E_{\rm unord}=\sum_{i<j}(x_i-x_j)^{-2}.
\]

Then

\[
\boxed{\partial_t\log\Delta=4E_{\rm ord}=8E_{\rm unord}.}
\]

For

\[
\mathcal H=\sum_{i\ne j}\log|x_i-x_j|^{-1},
\]

\[
\boxed{\mathcal H=-\log\Delta,\qquad \dot{\mathcal H}=-4E_{\rm ord}.}
\]

---

## 4. Hard-window flux — PROVED

For a finite window \(I\),

\[
A_i^I=\sum_{j\in I,j\ne i}(x_i-x_j)^{-1},
\qquad
A_i^{\rm ext}=A_i-A_i^I.
\]

Then

\[
\boxed{\partial_t\log\Delta_I=4E_{\rm ord}(I)+\mathcal F_I,}
\]

where

\[
\boxed{\mathcal F_I=4\sum_{i\in I}A_i^IA_i^{\rm ext},}
\]

and the local zero-chart factorization gives

\[
\boxed{A_i^{\rm ext}=a_z/a(t,x_i).}
\]

---

## 5. Generic double collision — SHARPENED

Let \(\tau=t-t_c\downarrow0\). For an isolated generic analytic double collision,

\[
\boxed{g(\tau)^2=8\tau+O(\tau^2).}
\]

Hence

\[
\boxed{E_{\rm pair,ord}=\frac2{g^2}=\frac1{4\tau}+O(1),}
\]

so

\[
\boxed{4E_{\rm pair,ord}=\frac1\tau+O(1).}
\]

For a hard window containing the isolated pair,

\[
\boxed{\mathcal F_I=O(1).}
\]

The older weaker \(O(\tau^{-1/2})\) remainder for the raw pair energy is superseded.

---

## 6. Round 17 Bregman entropy — PROVED / RETAINED

For a fixed ordered reference \(\xi_j\), Round 17 uses

\[
L(r)=-\log r+r-1\ge0
\]

and obtains an exact localized balance

\[
\partial_t\mathcal C_\psi
=-\mathscr B_\psi+\mathscr F_{\partial\psi}+\mathscr R_{\xi,\psi},
\]

with positive force-square bulk

\[
\boxed{\mathscr B_\psi=4\sum_j\psi_j(D_j^\psi)^2\ge0.}
\]

At an exact arithmetic lattice, this force-square bulk agrees to quadratic order with the Rodgers--Tao \(V\)-energy. It is not exactly the pairwise \(V\)-energy for a general reference.

---

## 7. Round 18 exact \(V\)-energy balance — PROVED ALGEBRAICALLY

Let \(w_{jk}=w_{kj}\ge0\), \(w_{jj}=0\), and

\[
\mathscr C_w
=\sum_{j\ne k}w_{jk}
\log\left|\frac{x_j-x_k}{\xi_j-\xi_k}\right|.
\]

Set

\[
a_{jk}=(x_j-x_k)^{-1},
\qquad
b_{jk}=(\xi_j-\xi_k)^{-1},
\qquad
\eta_j=x_j-\xi_j.
\]

Define

\[
A_j^w=\sum_{k\ne j}w_{jk}a_{jk},
\qquad
A_j=\operatorname{PV}\sum_{i\ne j}a_{ji}.
\]

Then

\[
\boxed{\partial_t\mathscr C_w=4S_w(x),\qquad S_w(x)=\sum_jA_jA_j^w.}
\]

Write

\[
S_w(x)=E_w(x)+K_w(x),
\]

with

\[
E_w(x)=\sum_{j\ne k}w_{jk}a_{jk}^2,
\]

\[
K_w(x)=\sum_j\sum_{\substack{i,k\ne j\\ i\ne k}}w_{jk}a_{ji}a_{jk}.
\]

The triple partial-fraction identity makes \(K_w\) an exact discrete cutoff commutator: an unordered triple contributes zero whenever its three edge weights agree.

For

\[
V(r)=r^{-2}-1+2(r-1),
\]

define

\[
\widetilde E_w^V
=\sum_{j\ne k}w_{jk}(\xi_j-\xi_k)^{-2}
V\left(\frac{x_j-x_k}{\xi_j-\xi_k}\right)\ge0,
\]

and

\[
\Lambda_w(\eta)
=\sum_{j\ne k}w_{jk}
\frac{\eta_j-\eta_k}{(\xi_j-\xi_k)^3}.
\]

Then exactly

\[
\boxed{
\partial_t\mathscr C_w
=4\widetilde E_w^V+4\mathscr F_w+4\mathscr R_w,
}
\]

where

\[
\boxed{\mathscr F_w=K_w(x)-K_w(\xi),}
\]

and

\[
\boxed{\mathscr R_w=S_w(\xi)-2\Lambda_w(\eta).}
\]

For the Rodgers--Tao near-pair cutoff \(w_{jk}=\psi_T(j)\psi_T(k)1_{j\sim_T k}\), this is the exact bookkeeping beneath their asymptotic truncated Hamiltonian identity, with opposite sign under the \(\log(1/|d|)\) convention.

**Novelty:** UNVERIFIED.

---

## 8. Entropy-budget obstruction — PROVED

Flux control alone cannot exclude collision.

The exact heat polynomial

\[
P_t(z)=z^2-2t
\]

has roots \(\pm\sqrt{2t}\) for \(t>0\), colliding at \(t=0\). Taking all roots gives

\[
\mathcal F_I=0,
\qquad
\Delta_I=8t,
\qquad
E_{\rm ord}=\frac1{4t},
\]

hence

\[
\boxed{\partial_t\log\Delta_I=1/t}
\]

with zero boundary flux. The divergence is carried by \(\log\Delta_I\to-\infty\).

Therefore

\[
\boxed{\text{nonintegrable bulk + integrable flux does not imply no collision}.}
\]

Program A requires an independent one-sided entropy/coercive budget. Any such bound must be audited to ensure it is not merely a lower-gap/no-collision assumption in disguise.

---

## 9. Round 19 all-multiplicity local degree — PROVED

Let \((t_c,c)\) be a multiplicity-\(m\ge2\) real zero of a nontrivial real-analytic backward-heat family. Define

\[
\Gamma(t,x)=(F(t,x),F_x(t,x)).
\]

The parabolic blow-up is the Hermite heat polynomial

\[
P_m(T,X)=e^{-T\partial_X^2}X^m
=m!\sum_{k=0}^{\lfloor m/2\rfloor}
\frac{(-T)^kX^{m-2k}}{k!(m-2k)!}.
\]

After positive-determinant input/output rescaling,

\[
(F,F_x)\to(P_m,\partial_XP_m)
\]

in \(C^1\) on compact sets. The model has only the origin as a common zero.

Computing the degree with the regular value \((0,\varepsilon)\), \(\varepsilon>0\):

- for \(T>0\), the Hermite roots with positive derivative contribute \(-1\) each; there are \(\lceil m/2\rceil\) of them;
- for \(T<0\), there is no real root when \(m\) is even;
- when \(m\) is odd, the unique negative-time real root branch \(X=0\) contributes \(+1\).

Therefore

\[
\boxed{
\deg_{\rm loc}(F,F_x;(t_c,c))
=-\left\lfloor\frac m2\right\rfloor.
}
\]

Thus **every isolated collision has strictly negative local degree**, for every multiplicity. The old restriction “only generic double collisions have known charge” is removed.

A nontrivial analytic heat family cannot have a curve of common zeros of \(F\) and \(F_x\): differentiating along such a curve and repeatedly using the heat equation forces all spatial derivatives to vanish, hence local triviality. Collision points are therefore locally isolated.

---

## 10. Program B global reduction — NEW PRIMARY TEST

For any bounded domain \(D\subset\mathbb R_t\times\mathbb R_x\) with \(\Gamma\ne0\) on \(\partial D\) and finitely many collision points inside,

\[
\boxed{
\deg(\Gamma,D,0)
=-\sum_{p\in D}\left\lfloor\frac{m_p}{2}\right\rfloor.
}
\]

Hence

\[
\boxed{\deg(\Gamma,D,0)=0\Longrightarrow\text{no collision in }D.}
\]

No cancellation among different collision multiplicities is possible.

The remaining problem is global boundary control:

1. prove \(\Gamma\ne0\) on the chosen boundary;
2. compute the winding of \(H_t+iH_t'\) on that boundary;
3. control the vertical faces as \(X\to\infty\);
4. control the horizontal faces without assuming RH or \(\Lambda\le0\).

A nowhere-vanishing normalizer may simplify amplitudes, but nonvanishing alone does not determine the winding.

---

## 11. Circularity guard

Assuming \(\Lambda>0\) for contradiction and working in the relevant positive-time region does not assume RH.

Rodgers--Tao's quantitative negative-time estimates are proved under the opposite contradiction hypothesis \(\Lambda<0\), which implies RH; they cannot be imported into a proof of \(\Lambda\le0\) without independent justification.

Safe imports are structural identities, definitions, and unconditional positive-time estimates. Polymath's positive-time asymptotics may be used only in the ranges they actually establish.

---

## 12. Laguerre status

Ordinary

\[
L_1=(H')^2-HH''\ge0
\]

is only necessary in general for Laguerre--Polya membership. The generalized real Laguerre inequalities and the complex Laguerre criterion provide the relevant complete characterizations. The phase-current route remains a local shadow because \(J=-L_1\).

---

## 13. Program ranking

\[
\boxed{B\gtrsim A\gg C.}
\]

### B — CO-PRIMARY / MOST URGENT TEST

All-multiplicity negative local degree + global boundary winding/exhaustion.

### A — CO-PRIMARY STRUCTURAL

Exact relative \(V\)-energy/flux identities + search for an independent finite entropy/coercive budget.

### C — TERTIARY

Low-complexity arithmetic separator, only after genuine non-density/non-equivalence is proved.

Round 15 sign-regularity: **FROZEN / AUXILIARY**.

---

## 14. Current status table

- local collision divisor geometry: **PROVED**;
- fixed-root inverse-square trace: **PROVED**;
- global canonical regularized discriminant: **NOT ASSUMED / OPEN**;
- hard-window Vandermonde flux identity: **PROVED**;
- sharpened generic double-collision law \(g^2=8\tau+O(\tau^2)\): **PROVED**;
- raw hard-window collision flux \(O(1)\): **PROVED locally**;
- Round-17 Bregman force-square law: **PROVED**;
- Round-18 exact smooth pair-cutoff relative log-Vandermonde law: **PROVED**;
- exact bulk equality with Rodgers--Tao \(V\)-energy: **PROVED algebraically**;
- “integrable flux prevents collision”: **REFUTED**;
- finite entropy/coercive budget: **OPEN**;
- all-multiplicity local degree \(-\lfloor m/2\rfloor\): **PROVED**;
- no local sign cancellation among collision multiplicities: **PROVED**;
- global boundary degree/winding: **OPEN — NEXT B TARGET**;
- degree exhaustion as \(X\to\infty\): **OPEN**;
- independent no-collision theorem: **OPEN**;
- RH: **OPEN**;
- novelty of Round-18/19 packaging/results in the literature: **UNVERIFIED**.
