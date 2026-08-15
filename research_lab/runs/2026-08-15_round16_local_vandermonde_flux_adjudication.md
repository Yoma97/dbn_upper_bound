# Round 16 — Local Relative Vandermonde Flux Adjudication

**Date:** 2026-08-15

**RH status:** OPEN.

**Purpose:** Adjudicate the global-discriminant / local-collision / sign-regularity programs against Rodgers–Tao, Polymath, and the uploaded Laguerre sources, and extract the strongest rigorously justified next theorem.

---

## 1. Executive verdict

The correct primary architecture is not a canonical finite global discriminant and not the Round-15 finite-order sign-regularity bridge.

The preferred hierarchy is:

1. **Exact local zero-set collision geometry** (already proved in Round 12).
2. **Local/finite-window relative Vandermonde or Hamiltonian with explicit boundary flux** (new primary program).
3. **Comparison with Rodgers–Tao renormalized window energies relative to the non-uniform reference configuration `xi_j`.**
4. Only then ask for an exhaustion / thermodynamic limit, energy density, or canonical relative increments.
5. Only after those gates ask for a Riemann-specific no-blowup estimate.

A globally finite scalar `Disc_reg(H_t)` is not assumed to exist.

The previous phrase “unification of #1–#4” is downgraded to:

> **exact local compatibility network around the common collision geometry.**

Finite discriminant and inverse-square energy are literally the same gradient-flow object; the phase current is a local Laguerre shadow; the Brouwer degree detects the same singular locus but contains additional topological information. No single invariant extracting all four has been proved.

---

## 2. Factor conventions — PROVED

For a finite monic heat polynomial

\[
P_t(z)=\prod_{k=1}^N(z-x_k(t)),\qquad \partial_tP_t=-P_t'',
\]

with simple real roots,

\[
\dot x_k=2\sum_{j\ne k}\frac1{x_k-x_j}.
\]

Set

\[
\Delta=\prod_{i<j}(x_i-x_j)^2,
\]

\[
E_{\rm unord}=\sum_{i<j}\frac1{(x_i-x_j)^2},
\qquad
E_{\rm ord}=\sum_{i\ne j}\frac1{(x_i-x_j)^2}=2E_{\rm unord}.
\]

Then

\[
\boxed{\partial_t\log\Delta=8E_{\rm unord}=4E_{\rm ord}.}
\]

With Rodgers–Tao's ordered Hamiltonian convention

\[
\mathcal H=\sum_{i\ne j}\log\frac1{|x_i-x_j|},
\]

one has exactly

\[
\boxed{\mathcal H=-\log\Delta,\qquad \dot{\mathcal H}=-4E_{\rm ord}.}
\]

This finite identity is classical/structural and is not claimed as novelty.

---

## 3. Local versus global convergence — CORRECTED

Three sums must be separated.

At a fixed root, the velocity sum

\[
\sum_{j\ne k}\frac1{x_k-x_j}
\]

requires a principal-value / canonical pairing interpretation in the infinite system.

At a fixed root, the inverse-square sum

\[
B_k=\sum_{j\ne k}\frac1{(x_k-x_j)^2}
\]

is absolutely convergent for an order-one zero divisor (Round 12).

The global positive pair energy

\[
\sum_k\sum_{j\ne k}\frac1{(x_k-x_j)^2}
\]

is the true infinite-volume divergence problem. This agrees with Rodgers–Tao's need to mollify and renormalize global/window energies.

Thus the correct slogan is

\[
\boxed{\text{local inverse-square trace is canonical; global infinite-volume energy is not finite.}}
\]

---

## 4. Exact hard-window Vandermonde flux identity — PROVED

This is the main new structural lemma of this round.

Let `I` be a finite set of labels of simple real zero branches of a backward-heat family in a real-rooted time interval. Define

\[
\Delta_I(t)=\prod_{i<j\in I}(x_i-x_j)^2.
\]

For each `i in I`, define the internal field

\[
A_i^I:=\sum_{j\in I,\,j\ne i}\frac1{x_i-x_j}.
\]

Define the total regular field intrinsically by

\[
A_i:=\frac{F_{xx}(t,x_i)}{2F_x(t,x_i)},
\]

and the external field

\[
A_i^{\rm ext}:=A_i-A_i^I.
\]

Along a simple zero branch, `dot x_i = 2 A_i`. Therefore

\[
\begin{aligned}
\frac d{dt}\log\Delta_I
&=2\sum_{i\in I}\dot x_i A_i^I\\
&=4\sum_{i\in I}A_iA_i^I\\
&=4\sum_{i\in I}(A_i^I)^2
+4\sum_{i\in I}A_i^IA_i^{\rm ext}.
\end{aligned}
\]

The finite internal algebra gives

\[
\sum_{i\in I}(A_i^I)^2
=\sum_{i\in I}\sum_{j\in I,\,j\ne i}\frac1{(x_i-x_j)^2}
=:E_{\rm ord}(I).
\]

Hence

\[
\boxed{
\frac d{dt}\log\Delta_I
=4E_{\rm ord}(I)+\mathcal F_I,
}
\]

with the exact boundary/external flux

\[
\boxed{
\mathcal F_I:=4\sum_{i\in I}A_i^I A_i^{\rm ext}.
}
\]

For a finite polynomial and `I` equal to all roots, `A_i^{ext}=0`, so the finite global identity is recovered exactly.

This is a zero-window identity. It requires no global discriminant and no thermodynamic limit.

---

## 5. Analytic meaning of the flux — PROVED locally

In a zero chart containing exactly the roots in `I`, factor

\[
F(t,z)=a(t,z)\prod_{i\in I}(z-x_i(t)),
\qquad a(t,z)\ne0.
\]

At a root `x_i`, direct differentiation gives

\[
\frac{F_{xx}}{2F_x}(t,x_i)
=\sum_{j\in I,\,j\ne i}\frac1{x_i-x_j}
+\frac{a_z}{a}(t,x_i).
\]

Thus

\[
\boxed{A_i^{\rm ext}=\frac{a_z}{a}(t,x_i).}
\]

Therefore the flux is precisely the coupling of the internal Vandermonde field to the analytic nonvanishing complement of the zero cluster.

This makes the relation to Round 12 transparent:

\[
\mathcal D_I=\Delta_I\prod_{i\in I}a(t,x_i)
\]

is a gauge-completed local collision section, while `log Delta_I` is the zero-set-only entropy whose evolution exposes the boundary flux explicitly.

So Round 12 and the present program are complementary, not competing.

---

## 6. Flux is nonsingular at an isolated collision — PROVED

Suppose a finite cluster `I` undergoes an isolated multiplicity-`m` collision at `(t_c,x_c)` while the analytic factor `a(t,z)` remains nonzero.

On the forward real-rooted side, the internal gaps scale as `O(sqrt(t-t_c))`, so

\[
A_i^I=O((t-t_c)^{-1/2}).
\]

But

\[
A_i^{ext}=\frac{a_z}{a}(t,x_i)
=c_0+O(\sqrt{t-t_c}).
\]

Since the purely internal fields satisfy

\[
\sum_{i\in I}A_i^I=0,
\]

the constant external term cancels in the flux sum. Therefore

\[
\boxed{\mathcal F_I=O(1)}
\]

as `t downarrow t_c` for an isolated collision.

For a generic double collision with gap `g(t)`, Polymath's Hermite splitting gives

\[
g(t)^2=8(t-t_c)+O((t-t_c)^{3/2}).
\]

Then

\[
E_{\rm ord}(I)=\frac{2}{g(t)^2}
=\frac1{4(t-t_c)}+O((t-t_c)^{-1/2}),
\]

and hence

\[
\boxed{
4E_{\rm ord}(I)=\frac1{t-t_c}+O((t-t_c)^{-1/2}),
\qquad
\mathcal F_I=O(1).
}
\]

Thus the logarithmic collision singularity is a genuine **bulk internal-energy singularity** and cannot be cancelled by a regular local boundary flux.

This is the cleanest rigorous bridge between the finite Vandermonde identity and the collision blow-up mechanism.

---

## 7. Relative reference configuration — PARTIAL / NEXT LAYER

Let `xi_j` denote the Rodgers–Tao reference configuration tracking the non-uniform zero density. For a finite window `I`, one may define the proto-relative zero-set entropy

\[
\mathscr C_I^{(0)}(t)
:=\log\frac{\Delta_I(t)}{\Delta_I(\xi)}.
\]

Because the reference is static, it has the same derivative as `log Delta_I`, hence the exact flux identity above.

However, this proto-relative entropy is **not yet** the correct thermodynamic renormalization as `I` expands. A growing window contains a large equilibrium background, and simply dividing by `Delta_I(xi)` need not remove all linear/background divergences.

Rodgers–Tao instead use pairwise convex renormalizations such as

\[
L(r)=\log\frac1{|r|}+|r|-1,
\qquad
V(r)=\frac1{|r|^2}-1+2(|r|-1),
\]

with `r=(x_i-x_j)/(xi_i-xi_j)`, and smooth index cutoffs.

Therefore no claim is made that

\[
\lim_{I\uparrow\mathbb Z^*}\mathscr C_I^{(0)}
\]

exists or is canonical.

---

## 8. Important correction to the desired smooth identity

The schematic target

\[
\partial_t\mathscr C_\psi
=4\mathscr E_\psi+\mathscr F_{\partial\psi}
\]

is the right **shape**, but it must not be imposed with `mathscr E_psi` pre-identified as the Rodgers–Tao positive `V`-energy.

Because the reference spacing `xi_j` is non-uniform and the pair counterterm contains a linearization, differentiating a relative entropy can generate:

1. a bulk collision-energy term;
2. a genuine boundary/cutoff flux;
3. a background-density / reference commutator (or gauge) term.

Thus the rigorous next target is

\[
\boxed{
\partial_t\mathscr C_{\psi,t}
=\mathscr B_{\psi,t}
+\mathscr F_{\partial\psi,t}
+\mathscr R_{\psi,t},
}
\]

where every term is explicit, followed by a theorem comparing the bulk term `mathscr B` with the nonnegative Rodgers–Tao renormalized energy.

Only if `mathscr R` can be absorbed canonically should one simplify the formula to “energy + flux”.

This avoids hiding the principal difficulty in notation.

---

## 9. Zero-set invariance versus entire-function normalization — CORRECTED

Two objects must be distinguished.

### Zero-set entropy

`Delta_I` and pairwise relative Vandermonde/Hamiltonian quantities depend only on the zero configuration. They are invariant under multiplication of `F` by a zero-free factor.

### Gauge-completed local collision section

\[
\mathcal D_I=(-1)^{m(m-1)/2}\prod_{i\in I}F_x(t,x_i)
\]

is not a scalar invariant under `F -> e^{az+b}F`; it changes by a nonvanishing factor. What is invariant is its **collision divisor / vanishing locus with multiplicity**, i.e. the local section modulo nonvanishing gauge.

This distinction is now mandatory terminology.

---

## 10. Laguerre and phase-current correction

For

\[
W=H+iH',
\]

\[
J=\Im(\overline W W')=HH''-(H')^2=-L_1.
\]

Hence the phase current is permanently removed as an independent invention path.

At a simple zero, `L1=(H')^2`, but raw `L1` is amplitude-dependent. Near a generic double collision written as

\[
H(t,x)=a(t,x)\left((x-c(t))^2-\frac{g(t)^2}{4}\right),
\]

one has

\[
L_1(x_\pm)\sim a^2g^2,
\qquad H''(c)\sim2a.
\]

Thus the scale-normalized collision coordinate is

\[
\boxed{
\frac{L_1(x_\pm)}{H''(c)^2}
\sim\frac{g^2}{4},
}
\]

not a bare invariant statement `L1 asymp g^2`.

Also, `L1 >= 0` on the real axis is only necessary in general. Complete characterizations include the full generalized real Laguerre hierarchy and, in the uploaded Csordas–Vishnyakova results, a complex Laguerre criterion.

---

## 11. Collision degree correction

For the collision map

\[
\Gamma(t,x)=(H_t(x),H_t'(x)),
\]

a generic isolated double collision satisfies

\[
\det D\Gamma=-(H'')^2<0,
\]

so its local Brouwer index is `-1`.

This statement is restricted to **isolated generic double collisions**. For multiplicity at least three the Jacobian can vanish, and the local degree requires a separate higher-order analysis.

Any global degree theorem must specify a bounded domain and nonvanishing on the full boundary, including both time faces and both spatial faces. Polymath's nowhere-vanishing normalizer `B_t` preserves local index under complex multiplication, but does not by itself control the boundary winding of `(H,H')`.

Therefore the degree program remains secondary:

> **Renormalized Collision Degree with Full Boundary Flux Control.**

---

## 12. Restricted arithmetic separator correction

A proper subset of Weil test functions is not automatically weaker: it may be dense in the topology in which the quadratic form is continuous. Therefore a genuinely restricted family must have a proved low-complexity obstruction (bandwidth, support, dimension, analytic form, etc.) and must not recover the full class by closure.

The separator program must be split into:

1. **geometric separation** of a hypothetical off-line point at the transform level;
2. **global domination** showing that the negative signal survives all other zeros and the prime/archimedean side.

This remains tertiary.

---

## 13. Program ranking after adjudication

\[
\boxed{A\gg B>C.}
\]

### A — PRIMARY

**Local Relative Vandermonde/Hamiltonian Renormalization + Explicit Flux**

Immediate next theorem:

> Starting from the exact hard-window flux identity, introduce the Rodgers–Tao non-uniform reference `xi_j` and a smooth cutoff `psi`; differentiate the relative pair entropy exactly and classify every term into bulk, cutoff flux, and background/reference commutator. Prove a comparison of the bulk term with the positive renormalized `V`-energy. Do not take an infinite-volume limit yet.

### B — SECONDARY

**Renormalized Brouwer Degree with Full Boundary Flux Control**

### C — TERTIARY

**Low-complexity Arithmetic Separator**, with non-density and two-stage detectability/domination audits.

### FROZEN

Round-15 finite oscillatory sign-regularity is retained as an auxiliary kernel result but is no longer the main path. The TP2 counterexample remains valuable evidence that low-order kernel positivity alone is insufficient.

---

## 14. Status

- finite discriminant/energy identity with factor conventions: **PROVED**;
- fixed-root inverse-square absolute convergence: **PROVED for order-one divisor**;
- global finite scalar discriminant: **NOT ASSUMED / OPEN**;
- exact hard-window Vandermonde flux identity: **PROVED**;
- flux bounded at an isolated collision: **PROVED locally**;
- collision bulk energy has universal logarithmic divergence: **PROVED**;
- thermodynamic/exhaustion renormalization: **OPEN**;
- smooth relative entropy exact decomposition: **OPEN — NEXT TARGET**;
- comparison with Rodgers–Tao positive renormalized energy: **OPEN — NEXT TARGET**;
- no-collision/RH: **OPEN**;
- novelty of the new flux packaging: **NOVELTY UNVERIFIED**.
