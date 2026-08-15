# Current Collision Program State

**Updated:** 2026-08-15 after Round 16.

## Executive pivot

The primary program is now

\[
\boxed{\text{Local Relative Vandermonde/Hamiltonian Renormalization + Explicit Flux}.}
\]

We do **not** assume that a canonical finite global regularized discriminant exists. The infinite-volume problem is treated only after exact finite-window identities have been established.

Round 15 finite-order oscillatory sign-regularity is retained as an auxiliary kernel program but is no longer the main path.

---

## 1. Exact local collision section — PROVED

For a finite simple real-zero cluster `I` of a real entire backward-heat family

\[
\partial_tF=-F_{xx},
\]

define

\[
\mathcal D_I(t)=(-1)^{m(m-1)/2}\prod_{i\in I}F_x(t,x_i(t)).
\]

In a zero chart

\[
F(t,z)=a(t,z)\prod_{i\in I}(z-x_i(t)),\qquad a\ne0,
\]

one has

\[
\mathcal D_I=\Delta_I\prod_{i\in I}a(t,x_i),
\qquad
\Delta_I=\prod_{i<j\in I}(x_i-x_j)^2.
\]

Thus `D_I` is a gauge-completed local collision section. As a scalar it depends on the entire-function normalization; its vanishing divisor is invariant under multiplication by zero-free factors.

---

## 2. Fixed-root local trace versus global energy — PROVED / CORRECTED

At a simple root,

\[
A_i=\frac{F_{xx}}{2F_x}(t,x_i),
\qquad
B_i=A_i^2-\frac{F_{xxx}}{3F_x}(t,x_i).
\]

For an order-one entire divisor,

\[
\boxed{B_i=\sum_{\rho\ne x_i}\frac1{(x_i-\rho)^2}}
\]

is absolutely convergent at fixed `i`.

The first-order velocity field requires a principal-value / canonical-pairing interpretation in the infinite system. The actual divergence problem is the global positive pair energy

\[
\sum_i\sum_{j\ne i}\frac1{(x_i-x_j)^2},
\]

which is the quantity Rodgers–Tao mollify and renormalize.

---

## 3. Finite factor conventions — PROVED

For a finite monic heat polynomial let

\[
E_{\rm unord}=\sum_{i<j}\frac1{(x_i-x_j)^2},
\qquad
E_{\rm ord}=\sum_{i\ne j}\frac1{(x_i-x_j)^2}=2E_{\rm unord}.
\]

Then

\[
\boxed{\partial_t\log\Delta=8E_{\rm unord}=4E_{\rm ord}.}
\]

With the ordered Rodgers–Tao Hamiltonian

\[
\mathcal H=\sum_{i\ne j}\log\frac1{|x_i-x_j|},
\]

\[
\boxed{\mathcal H=-\log\Delta,\qquad \dot{\mathcal H}=-4E_{\rm ord}.}
\]

Thus finite discriminant and finite inverse-square energy are literally the same gradient-flow object.

---

## 4. Exact hard-window Vandermonde flux identity — PROVED

For a finite window `I`, define the internal field

\[
A_i^I=\sum_{j\in I,\,j\ne i}\frac1{x_i-x_j},
\]

and the external field

\[
A_i^{\rm ext}=A_i-A_i^I.
\]

Since `dot x_i=2A_i`,

\[
\boxed{
\frac d{dt}\log\Delta_I
=4E_{\rm ord}(I)+\mathcal F_I,
}
\]

where

\[
E_{\rm ord}(I)=\sum_{i\in I}\sum_{j\in I,\,j\ne i}\frac1{(x_i-x_j)^2},
\]

and

\[
\boxed{
\mathcal F_I=4\sum_{i\in I}A_i^I A_i^{\rm ext}.
}
\]

From the zero-chart factorization,

\[
\boxed{A_i^{\rm ext}=\frac{a_z}{a}(t,x_i).}
\]

Therefore `F_I` is an explicit coupling of the internal Vandermonde field to the analytic nonvanishing complement of the cluster. For a finite polynomial with `I` equal to all roots, the flux vanishes exactly.

---

## 5. Collision singularity versus flux — PROVED LOCALLY

At an isolated collision, the internal fields are of size `O((t-t_c)^(-1/2))`, while the analytic external field has a regular expansion. Because

\[
\sum_{i\in I}A_i^I=0,
\]

the constant external term cancels, giving

\[
\boxed{\mathcal F_I=O(1)}
\]

near the collision.

For a generic double collision,

\[
g(t)^2=8(t-t_c)+O((t-t_c)^{3/2}),
\]

hence

\[
E_{\rm ord}(I)=\frac{2}{g(t)^2}
=\frac1{4(t-t_c)}+O((t-t_c)^{-1/2}),
\]

so

\[
\boxed{
4E_{\rm ord}(I)=\frac1{t-t_c}+O((t-t_c)^{-1/2}),
\qquad
\mathcal F_I=O(1).
}
\]

Thus the logarithmic collision divergence is an internal bulk-energy singularity and cannot be cancelled by a regular local boundary flux.

---

## 6. Rodgers–Tao layer — PARTIAL / NEXT TARGET

The natural background is the non-uniform reference configuration `xi_j`, not a fixed lattice. Rodgers–Tao use pairwise convex renormalizations such as

\[
L(r)=\log\frac1{|r|}+|r|-1,
\qquad
V(r)=\frac1{|r|^2}-1+2(|r|-1),
\]

with

\[
r=\frac{x_i-x_j}{\xi_i-\xi_j},
\]

and smooth index cutoffs.

We therefore do not ask first for a global scalar or for an exhaustion limit.

The immediate theorem target is to construct a smoothly localized relative entropy and derive an **exact decomposition**

\[
\boxed{
\partial_t\mathscr C_{\psi,t}
=\mathscr B_{\psi,t}
+\mathscr F_{\partial\psi,t}
+\mathscr R_{\psi,t},
}
\]

where:

- `B_psi` is the bulk pair term;
- `F_{partial psi}` is the genuine cutoff/boundary flux;
- `R_psi` is the reference-density/background commutator or gauge term created by the non-uniform `xi_j` and counterterms.

Then prove a rigorous comparison between `B_psi` and the nonnegative Rodgers–Tao renormalized `V`-energy.

Only if `R_psi` is shown to be canonically absorbable may the identity be simplified to “energy + flux”.

---

## 7. What has actually been unified — CORRECTED

Do not say that one global invariant unifies all four proposed shadows.

The correct statement is:

- finite discriminant and finite inverse-square energy are exactly the same gradient-flow object;
- the phase current `J=-L1` is a local differential/Laguerre shadow and is not an independent path;
- the local collision section `D_I` is a gauge completion of the zero-set Vandermonde;
- the Brouwer degree detects the same collision locus but adds topological information not extracted from the scalar energy alone.

Hence

\[
\boxed{\text{the objects form an exact local compatibility network around collision geometry, not yet one global invariant.}}
\]

---

## 8. Laguerre normalization — CORRECTED

For

\[
W=H+iH',
\]

\[
J=\Im(\overline W W')=HH''-(H')^2=-L_1.
\]

Thus phase current is permanently removed as an independent route.

Near a generic double collision

\[
H(t,x)=a(t,x)\left((x-c(t))^2-\frac{g(t)^2}{4}\right),
\]

raw `L1` scales as `a^2 g^2`; the scale-normalized collision coordinate is

\[
\boxed{\frac{L_1(x_\pm)}{H''(c)^2}\sim\frac{g^2}{4}.}
\]

`L1>=0` on the real axis is only necessary in general. Complete Laguerre–Polya characterizations include the full generalized real Laguerre hierarchy and a complex Laguerre criterion.

---

## 9. Collision degree — SECONDARY

For

\[
\Gamma(t,x)=(H_t(x),H_t'(x)),
\]

a generic isolated double collision has

\[
\det D\Gamma=-(H'')^2<0,
\]

hence local Brouwer index `-1`.

This does not extend automatically to multiplicity at least three, where the Jacobian may vanish. A global degree argument must use a bounded domain and control all boundary faces. A nowhere-vanishing complex normalizer preserves local index but does not automatically control boundary winding.

Program B is therefore:

\[
\boxed{\text{Renormalized Collision Degree with Full Boundary Flux Control}.}
\]

---

## 10. Arithmetic separator — TERTIARY

A proper subset of Weil test functions may still be dense. Any restricted family must therefore have a genuine low-complexity constraint and a proved non-density / non-equivalence property.

The argument must split into:

1. geometric separation of a hypothetical off-line point at the transform level;
2. global domination showing the signal survives all other zeros and the arithmetic side.

---

## 11. Round 13–15 status after pivot

The positive-threshold finite-collision reduction and universal Hermite collision residue remain useful diagnostics and are retained.

The kernel monotonicity/log-concavity and half-wave results remain valid auxiliary theorems.

The cumulative nonnegative-balance proposal is **REFUTED**.

TP2/log-concavity plus monotone likelihood-ratio ordering is **REFUTED as a sufficient abstract C6 mechanism**.

The finite oscillatory sign-regularity bridge is **FROZEN / AUXILIARY**, not the primary target.

---

## 12. Program ranking

\[
\boxed{A\gg B>C.}
\]

### A — PRIMARY
Local Relative Vandermonde/Hamiltonian Renormalization + Explicit Flux.

### B — SECONDARY
Renormalized Brouwer Degree with Full Boundary Flux Control.

### C — TERTIARY
Low-complexity Arithmetic Separator.

---

## 13. Status

- local collision divisor geometry: **PROVED**;
- local fixed-root inverse-square trace: **PROVED**;
- global finite scalar regularized discriminant: **NOT ASSUMED / OPEN**;
- exact hard-window Vandermonde flux identity: **PROVED**;
- bounded local flux across isolated collision: **PROVED locally**;
- universal collision-energy logarithmic divergence: **PROVED**;
- smooth relative entropy decomposition: **OPEN — NEXT TARGET**;
- comparison with Rodgers–Tao positive renormalized energy: **OPEN — NEXT TARGET**;
- exhaustion / thermodynamic renormalization: **OPEN**;
- independent no-collision theorem: **OPEN**;
- RH: **OPEN**;
- novelty of the flux packaging: **NOVELTY UNVERIFIED**.
