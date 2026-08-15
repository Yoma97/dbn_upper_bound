# Round 18 — Exact V-energy flux law and the entropy-budget obstruction

**Date:** 2026-08-15

**Status labels:** PROVED / CONDITIONAL / CORRECTED / OBSTRUCTION / OPEN / NOVELTY UNVERIFIED.

**RH status:** OPEN.

## 0. Executive adjudication

Round 16 identified the correct finite-window Vandermonde flux identity. Round 17 then produced a valid exact Bregman balance law. Both are structurally useful, but neither by itself is a no-collision mechanism.

This round makes three corrections/advances.

1. The generic double-collision expansion for the raw pair energy can be sharpened from
   \[
   g(t)^2=8\tau+O(\tau^{3/2})
   \]
   to
   \[
   \boxed{g(t)^2=8\tau+O(\tau^2)},\qquad \tau=t-t_c\downarrow0,
   \]
   because the square of the gap is the analytic discriminant of the local Weierstrass quadratic.

2. There is an **exact smooth pair-cutoff identity whose bulk is Rodgers--Tao's nonnegative \(V\)-renormalized pair energy itself**, not merely a quadratic/Hessian approximation to it.

3. Most importantly, **integrable boundary/reference flux does not rule out collision**. The entropy/log-Vandermonde term itself has the matching logarithmic singularity. Thus the true missing gate is an independent finite-budget/coercive bound on the localized entropy (or another quantity), not merely a flux estimate.

The polynomial \(P_t(z)=z^2-2t\) is the decisive sanity check: it has zero external flux, exact bulk blow-up, and nevertheless collides at \(t=0\).

---

## 1. Setup and conventions

Let \((x_j(t))\) be a finite ordered real-simple configuration, or an infinite ordered real-simple configuration for which all sums below are justified by a stated principal-value/absolute-convergence convention.

Assume the zero ODE

\[
\dot x_j=2A_j,
\qquad
A_j:=\operatorname{PV}\sum_{i\ne j}\frac1{x_j-x_i}.
\]

Let \((\xi_j)\) be a fixed strictly ordered reference configuration. Set

\[
d_{jk}:=x_j-x_k,
\qquad
s_{jk}:=\xi_j-\xi_k,
\qquad
\eta_j:=x_j-\xi_j,
\]

and

\[
a_{jk}:=\frac1{d_{jk}},
\qquad
b_{jk}:=\frac1{s_{jk}}.
\]

Let \(w_{jk}=w_{kj}\ge0\), \(w_{jj}=0\), be a fixed symmetric pair weight. For rigorous finite algebra one may take finite pair support. The Rodgers--Tao choice is modeled by

\[
w_{jk}=\psi_T(j)\psi_T(k)\chi_T(j,k),
\]

where \(\chi_T\) is the near-pair cutoff corresponding to \(j\sim_T k\).

All pair sums in this note are **ordered** sums over \(j\ne k\).

---

## 2. Exact relative log-Vandermonde balance — PROVED

Define the additive relative log-Vandermonde

\[
\boxed{
\mathscr C_w(t)
:=\sum_{j\ne k}w_{jk}
\log\left|\frac{x_j-x_k}{\xi_j-\xi_k}\right|.
}
\]

The reference denominator is static, so

\[
\begin{aligned}
\partial_t\mathscr C_w
&=\sum_{j\ne k}w_{jk}\frac{\dot x_j-\dot x_k}{x_j-x_k}\\
&=2\sum_j\dot x_j\sum_{k\ne j}w_{jk}a_{jk}.
\end{aligned}
\]

Define

\[
A_j^w:=\sum_{k\ne j}w_{jk}a_{jk}.
\]

Using \(\dot x_j=2A_j\),

\[
\boxed{
\partial_t\mathscr C_w
=4S_w(x),
\qquad
S_w(x):=\sum_jA_jA_j^w.
}
\]

This identity is exact.

With Rodgers--Tao's Hamiltonian sign convention \(\log(1/|d|)\), the sign is reversed.

---

## 3. Exact bulk plus discrete boundary commutator — PROVED

Define the weighted raw inverse-square energy

\[
E_w(x):=\sum_{j\ne k}w_{jk}a_{jk}^2.
\]

Expanding \(A_jA_j^w\) into the diagonal term \(i=k\) and the off-diagonal terms gives

\[
\boxed{
S_w(x)=E_w(x)+K_w(x),
}
\]

where

\[
\boxed{
K_w(x):=
\sum_j
\sum_{\substack{i,k\ne j\\ i\ne k}}
 w_{jk}a_{ji}a_{jk}.
}
\]

The term \(K_w\) is a genuine cutoff/boundary commutator. To see this, fix an unordered triple \(\{i,j,k\}\) and set

\[
P_i:=\frac1{(x_i-x_j)(x_i-x_k)},
\quad
P_j:=\frac1{(x_j-x_i)(x_j-x_k)},
\quad
P_k:=\frac1{(x_k-x_i)(x_k-x_j)}.
\]

The elementary partial-fraction identity gives

\[
P_i+P_j+P_k=0.
\]

The contribution of this triple to \(K_w\) is

\[
(w_{ij}+w_{ik})P_i
+(w_{ij}+w_{jk})P_j
+(w_{ik}+w_{jk})P_k.
\]

Hence it vanishes whenever the three edge weights agree. Equivalently, it can be written entirely in terms of differences of the three edge weights. Thus interior triples cancel; only variation of the pair cutoff survives.

For a hard window

\[
w_{jk}=1_{\{j,k\in I\}},
\]

one recovers exactly

\[
K_w(x)=\sum_{i\in I}A_i^I A_i^{\rm ext},
\]

so Section 2 reduces to the Round-16 identity

\[
\partial_t\log\Delta_I
=4E_{\rm ord}(I)+4\sum_{i\in I}A_i^IA_i^{\rm ext}.
\]

---

## 4. Exact Rodgers--Tao \(V\)-bulk decomposition — PROVED

For the same weight define the reference fields

\[
B_j:=\operatorname{PV}\sum_{i\ne j}b_{ji},
\qquad
B_j^w:=\sum_{k\ne j}w_{jk}b_{jk},
\]

and

\[
S_w(\xi):=\sum_jB_jB_j^w
=E_w(\xi)+K_w(\xi).
\]

Use Rodgers--Tao's convex modified potential

\[
V(r)=\frac1{r^2}-1+2(r-1),
\qquad r>0.
\]

Define the weighted modified pair energy

\[
\boxed{
\widetilde E_w^V(x\mid\xi)
:=\sum_{j\ne k}w_{jk}\frac1{s_{jk}^2}
V\!\left(\frac{d_{jk}}{s_{jk}}\right)\ge0.
}
\]

Since \(d_{jk}-s_{jk}=\eta_j-\eta_k\), pairwise

\[
\frac1{s_{jk}^2}V\!\left(\frac{d_{jk}}{s_{jk}}\right)
=a_{jk}^2-b_{jk}^2
+2\frac{\eta_j-\eta_k}{s_{jk}^3}.
\]

Set the linear tangent/reference counterterm

\[
\boxed{
\Lambda_w(\eta)
:=\sum_{j\ne k}w_{jk}
\frac{\eta_j-\eta_k}{s_{jk}^3}.
}
\]

Then exactly

\[
E_w(x)-E_w(\xi)
=\widetilde E_w^V-2\Lambda_w(\eta).
\]

Combining this with Sections 2--3 gives the exact balance law

\[
\boxed{
\partial_t\mathscr C_w
=4\widetilde E_w^V
+4\mathscr F_w
+4\mathscr R_w,
}
\]

where

\[
\boxed{
\mathscr F_w:=K_w(x)-K_w(\xi)
}
\]

is the dynamic cutoff/boundary commutator relative to the reference, and

\[
\boxed{
\mathscr R_w:=S_w(\xi)-2\Lambda_w(\eta)
}
\]

is the explicit reference/tangent defect.

Thus the bulk can be chosen to be **exactly** the Rodgers--Tao \(V\)-renormalized pair energy. No Hessian approximation is required for this identity.

This is the precise realization of the anticipated scheme

\[
\partial_t\mathscr C
=\mathscr B+\mathscr F+\mathscr R
\]

with

\[
\boxed{\mathscr B=4\widetilde E_w^V.}
\]

**Novelty of this packaging:** UNVERIFIED. It is an exact reorganization of the same algebraic ingredients that appear in the Rodgers--Tao truncated Hamiltonian calculation and should not be advertised as a new theorem until the literature is checked carefully.

---

## 5. Relation to Round 17 — CORRECTED

Round 17 defines the positive Bregman entropy

\[
\sum_{j\ne k}\psi_j\psi_k
\left(-\log r_{jk}+r_{jk}-1\right)
\]

and obtains an exact positive bulk

\[
4\sum_j\psi_j(D_j^\psi)^2.
\]

That theorem is correct. However, its bulk is a **squared defect force**, not the pairwise Rodgers--Tao \(V\)-energy. The equality with \(V\)-energy proved there is only quadratic around an exact arithmetic lattice.

Therefore Round 17 is retained as a useful coercive/gradient formulation, but it does **not** by itself complete the original Round-16 target of identifying an exact \(V\)-pair-energy bulk under a general pair cutoff and the non-uniform reference \(\xi_j\).

The present log-Vandermonde identity supplies that exact pairwise bulk. The two entropies should be kept distinct:

- **Bregman entropy:** positive, exact force-square dissipation;
- **relative log-Vandermonde:** signed, exact Rodgers--Tao \(V\)-pair-energy bulk plus explicit commutators.

Neither should be renamed to hide this distinction.

---

## 6. Sharpened generic double-collision asymptotics — CORRECTED

Let \(\tau=t-t_c\downarrow0\) and suppose an isolated generic double collision occurs at \((t_c,c)\).

By Weierstrass preparation, after absorbing a nonvanishing analytic factor, the two local roots are the roots of a monic quadratic whose coefficients are analytic in \(\tau\). Hence its discriminant, which equals the square of the local gap, is analytic in \(\tau\).

The backward heat equation fixes the first derivative of this discriminant at the collision, giving

\[
\boxed{
g(\tau)^2=8\tau+O(\tau^2).}
\]

Consequently the ordered contribution of the colliding pair to the raw energy is

\[
\boxed{
E_{\rm pair,ord}
=\frac2{g^2}
=\frac1{4\tau}+O(1),
}
\]

and therefore

\[
\boxed{
4E_{\rm pair,ord}
=\frac1\tau+O(1).
}
\]

For a hard window containing the isolated pair, the analytic external field is regular and the constant part cancels between the two branches, so

\[
\boxed{\mathcal F_I=O(1).}
\]

For the exact \(V\)-energy, the colliding pair likewise contributes

\[
\widetilde E^V_{\rm pair,ord}
=\frac2{g^2}+O(1)
=\frac1{4\tau}+O(1).
\]

With a genuinely smooth/nonconstant pair cutoff, the triple commutator may contain an integrable \(O(g^{-1})=O(\tau^{-1/2})\) transition contribution unless the weights are locally constant on the colliding cluster.

---

## 7. Decisive obstruction: bounded flux does not prevent collision — PROVED

Consider

\[
P_t(z)=z^2-2t.
\]

Then

\[
\partial_tP_t=-2=-P_t'',
\]

so this is an exact backward-heat polynomial. For \(t>0\) its two zeros are

\[
x_\pm(t)=\pm\sqrt{2t},
\]

and they collide at \(t_c=0\).

Take the window containing both roots. It is the entire zero set, hence

\[
A_i^{\rm ext}=0,
\qquad
\mathcal F_I=0
\]

identically.

The gap satisfies

\[
g^2=8t,
\qquad
\Delta_I=g^2=8t,
\]

and

\[
E_{\rm ord}=rac2{g^2}=rac1{4t}.
\]

Therefore

\[
\boxed{
\partial_t\log\Delta_I
=4E_{\rm ord}
=\frac1t,
\qquad
\mathcal F_I=0,
}
\]

while the collision still occurs.

Thus

\[
\boxed{
\text{non-integrable bulk} + \text{integrable (even zero) flux}
\not\Rightarrow \text{no collision}.
}
\]

The reason is elementary but fundamental:

\[
\log\Delta_I(t)=\log(8t)\to-\infty,
\]

so the left-hand entropy itself carries exactly the divergent budget required by the bulk integral.

The same phenomenon occurs for the positive Bregman entropy, which tends to \(+\infty\) at collision.

Therefore the Round-17 proposed next question — controlling only

\[
\int(\mathscr F+\mathscr R)\,dt
\]

so that the bulk divergence cannot be “hidden” there — is **insufficient**. The divergence need not be hidden in flux; it is already accounted for by the entropy variation.

---

## 8. The correct next gate — OPEN

A genuine no-collision argument from Program A now requires an additional input of one of the following types.

### Gate A1 — finite entropy budget

Prove, from Riemann-specific information independent of RH/no-collision, that the relevant localized relative entropy obeys a bound

\[
|\mathscr C_w(t)|\le M_w
\]

(or a one-sided bound in the collision-divergent direction) on the whole candidate interval down to the first positive collision time.

This bound must not be equivalent to a lower gap bound or to \(\Lambda\le0\) in disguise.

### Gate A2 — cancellation-free compensated quantity

Construct a compensated functional

\[
\mathscr Q_w=\mathscr C_w+\text{explicit reference/boundary correction}
\]

whose collision singularity is absent or has a sign incompatible with its independently controlled time evolution, while retaining a positive bulk term.

A correction that simply subtracts the local \(\log g\) singularity by hand is not acceptable unless that subtraction has an independent global/analytic meaning.

### Gate A3 — finite global budget from the entire function

Use a normalization-sensitive but analytically controlled object (for example a carefully chosen local entire-function section) to bound the zero-set entropy. Any such step must expose the zero-free gauge explicitly and prove that its contribution cannot itself supply the missing logarithmic divergence.

Without one of A1--A3, Program A is a **diagnostic collision balance law**, not a proof mechanism excluding collision.

---

## 9. Circularity / hidden-RH audit

The finite identities in Sections 2--4 require only a real-simple interval on which the zero ODE is valid.

For an RH proof by contradiction one may assume

\[
\Lambda>0
\]

and work on \(t>\Lambda\), where the zeros are in the real-rooted regime. This does **not** assume RH.

However, the quantitative estimates in Rodgers--Tao's proof of \(\Lambda\ge0\) are developed under the opposite contradiction hypothesis

\[
\Lambda<0,
\]

which implies RH and provides a negative-time real-simple interval extending to \(t=0\). Those estimates cannot simply be imported into a proof of \(\Lambda\le0\).

What can be imported without circularity is:

- the algebraic form of the zero ODE where justified;
- the definitions of \(\xi_j\), \(L\), \(V\), cutoffs, and renormalized energies;
- purely algebraic/truncated identities.

Any asymptotic bound used in the \(\Lambda>0\) contradiction regime must be re-proved there or taken from an unconditional positive-time result such as the Polymath upper-bound analysis.

---

## 10. Relation to Rodgers--Tao Proposition 22

Rodgers--Tao use

\[
\psi_T(j)=\left(1+\frac{|j|}{T\log T}\right)^{-100}
\]

and a near-pair relation \(j\sim_T k\), then define a truncated relative Hamiltonian and the modified \(V\)-energy. Their Proposition 22 proves

\[
\partial_t\widetilde H_T
=-4\widetilde E_T
+o_{T\to\infty}(T\log^3T+\widetilde E_T).
\]

In the present notation, the exact algebra behind that statement is the decomposition

\[
\partial_t\mathscr C_w
=4\widetilde E_w^V
+4\mathscr F_w+4\mathscr R_w,
\]

with the Hamiltonian sign reversed. Their detailed estimates show, in their regime and for their particular \(w\), that the combined commutator/reference terms are negligible at the required scale.

Thus the new packaging is best viewed as an **exact bookkeeping identity underneath Proposition 22**, not as a replacement for its analytic estimates.

---

## 11. Updated program verdict

The ranking remains provisionally

\[
A>B>C,
\]

but the meaning of Program A changes.

### A — PRIMARY STRUCTURAL PROGRAM

**Exact local/relative Vandermonde identities + explicit \(V\)-bulk + search for an independent finite entropy budget.**

Flux control alone is no longer the main gate.

### B — SECONDARY

Renormalized Brouwer degree with full boundary control. This remains potentially valuable precisely because a degree may provide a finite topological budget that a divergent entropy lacks.

### C — TERTIARY

Low-complexity arithmetic separator, with non-density/non-equivalence proved before positivity is used.

Round 15 sign-regularity remains FROZEN / AUXILIARY.

---

## 12. Status table

- hard-window Vandermonde flux identity: **PROVED**;
- analytic meaning \(A_i^{\rm ext}=a_z/a\): **PROVED locally**;
- sharpened generic double-collision law \(g^2=8\tau+O(\tau^2)\): **PROVED under generic analytic double collision**;
- raw hard-window flux \(O(1)\) at isolated double collision: **PROVED locally**;
- Round-17 Bregman force-square law: **PROVED and retained**;
- exact symmetric-pair-cutoff log-Vandermonde law: **PROVED**;
- exact bulk identification with Rodgers--Tao \(V\)-energy: **PROVED algebraically**;
- explicit cutoff triple commutator: **PROVED**;
- exact reference/tangent remainder: **PROVED**;
- “integrable flux prevents collision”: **REFUTED** by \(z^2-2t\);
- independent finite entropy/coercive budget: **OPEN — NEW PRIMARY GATE**;
- infinite Riemann exhaustion estimates in the \(\Lambda>0\) contradiction regime: **OPEN**;
- no-collision theorem: **OPEN**;
- RH: **OPEN**;
- novelty of exact packaging: **UNVERIFIED**.
