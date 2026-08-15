# Unified Collision Geometry Program

**Purpose:** Give a small group of agents a single tightly constrained opportunity to turn the finite collision identities into correct new mathematics for the de Bruijn--Newman/Riemann heat family.

This is a focused program, not a claim that the sought object exists.

## A. Finite prototype that must be reproduced exactly

For a real-rooted monic heat polynomial

\[
P_t(z)=\prod_{j=1}^N(z-x_j(t)),\qquad \partial_tP_t=-P_t'',
\]

while the roots are simple and real,

\[
\dot x_k=2\sum_{j\ne k}\frac1{x_k-x_j}.
\]

Define

\[
\Delta_t=\prod_{i<j}(x_i-x_j)^2.
\]

Then

\[
\frac{d}{dt}\log\Delta_t
=4\sum_{i\ne j}\frac1{(x_i-x_j)^2}.
\]

For

\[
G=P+iP',\qquad J=\Im(\overline G G'),
\]

one has

\[
J=PP''-(P')^2=-L_1(P),
\]

and at a simple root `x_k`,

\[
-J(x_k)=P'(x_k)^2.
\]

Hence

\[
\Delta_t^2=\prod_k[-J(x_k)].
\]

At a generic double collision `P=P'=0`, `P''!=0`, the Jacobian of `(P,P')` in `(t,x)` is negative:

\[
\det D_{(t,x)}(P,P')=-(P'')^2<0.
\]

These finite identities are the mandatory prototype. Agents must rederive them and check constants/sign conventions before extrapolation.

---

## B. Central conjectural object

Seek a canonical **relative collision functional**

\[
\mathscr C_t
\]

for the Riemann heat family `H_t` or for a natural wider class of order-one real-entire backward-heat families.

Do **not** assume that `Disc_reg(H_t)` exists canonically. The job is to construct it or prove that the proposed unification fails.

A successful object should have compatible manifestations:

1. **Global/divisor:** a relative determinant/resultant/discriminant-like quantity.
2. **Local:** a transversality/phase observable near a zero.
3. **Spectral/metric:** a regularized inverse-square gap trace or pair energy.
4. **Topological:** a collision index/charge in the `(t,x)` plane.

The four manifestations need not be literally equal; precise transforms, logarithmic derivatives, or local factorizations are acceptable if proved.

---

## C. Mandatory gates

### Gate C1: Well-definedness
Specify the natural class, zero enumeration, genus/Hadamard convention, admissible cutoffs, and all convergence/subtraction terms. A divergent formal product is not an object.

### Gate C2: Collision locality
For any compact core containing a finite collision and a collision-free tail, prove a local factorization of the schematic form

\[
\mathscr C_t=\Delta_{\rm core}(t)A_{\rm tail}(t),\qquad A_{\rm tail}(t)\ne0
\]

or an equivalent local statement. Tail regularization must not be able to cancel a genuine finite collision.

### Gate C3: Cutoff/renormalization independence
Two admissible cutoff/renormalization schemes must differ only by a controlled nonvanishing factor or an explicitly classified gauge term. If the zero/singularity set depends on the scheme, reject the construction.

### Gate C4: Finite-model recovery
For finite real-rooted heat polynomials, recover the classical discriminant, inverse-square gap trace, phase/Laguerre factorization, and local collision index with correct constants.

### Gate C5: Evolution identity
Seek and prove one of:

\[
\frac d{dt}\log\mathscr C_t=\mathcal F_t,
\]

or a relative version, monotonicity law, differential inequality, or distributional continuity equation. Every exchange of infinite sum/limit/derivative must be justified.

### Gate C6: No-go mechanism
Only after C1--C5 may the lab ask whether the Riemann kernel gives a sign, coercivity, conservation, or source-exclusion law preventing the collision set from being reached for `t>0`.

A universal heat-flow no-collision law is impossible because polynomial heat flows collide. The final no-go input must be Riemann-specific or belong to a natural class that genuinely excludes known colliding examples.

---

## D. Phase-current subproject

For the baseline choice

\[
W=H+iH',
\]

record explicitly that

\[
J=\Im(\overline W W')=HH''-(H')^2=-L_1(H).
\]

Therefore this `J` is not new by itself.

The subproject succeeds only if it obtains additional independent mathematics, for example:

- a kernel double-integral representation with a new sign mechanism;
- a weighted-integrated sign theorem where the integrand changes sign but the full Riemann-kernel integral has a forced sign;
- a new companion field `W` whose current detects transversality but is not merely a rewritten generalized Laguerre coefficient.

Destroy any proposed current that only renames `L_1` or another RH-equivalent endpoint.

---

## E. Gap-trace subproject

Seek a relative finite-part quantity

\[
\mathcal T_t=\operatorname{FP}\sum_{j\ne k}\frac1{(x_j-x_k)^2}
\]

or a more natural trace/resolvent object.

Success requires:

1. subtraction dictated by the known asymptotic zero density, not a fitted counterterm;
2. cutoff independence;
3. local divergence at a finite collision with the correct coefficient;
4. compatibility with a logarithmic derivative of the global collision functional;
5. a proof that the tail remains controlled uniformly in the regime used.

If the regularized trace exists but has no canonical relation to a collision functional, record it as a separate tool rather than forcing unification.

---

## F. Collision charge / analytic flux subproject

Let the collision map be

\[
\Gamma(t,x)=(H_t(x),H_t'(x)).
\]

A collision is `Gamma=0`.

Tasks:

1. derive the local Brouwer degree/Jacobian at generic and higher-multiplicity collisions;
2. classify how the degree changes under splitting/merging;
3. derive any distributional current `j^mu` for the zero set;
4. determine the exact source term rather than assuming conservation;
5. isolate what special Riemann-kernel property would be needed to force the source to vanish or have forbidden sign.

The topology is bookkeeping unless tied to an analytic flux estimate.

---

## G. Independent backup: localized arithmetic separator

This route must remain logically independent of the unified collision geometry.

Assume one off-critical zero, construct a localized test family, and derive an amplified negative/signature contribution. Then seek a prime-side/operator-side estimate independent of RH.

Every proposal must be compared against Weil, Li, Bombieri--Lagarias, Essential Simplicity, and known equivalent criteria. If the final estimate is itself RH-equivalent, classify the construction as a microscope, not a proof mechanism.

---

## H. Required output of every invention agent

For each candidate:

1. FORMAL DEFINITION
2. NATURAL DOMAIN / CLASS
3. FINITE PROTOTYPE RECOVERY
4. WELL-DEFINEDNESS PROOF OR EXACT GAP
5. COLLISION-LOCALITY PROOF OR EXACT GAP
6. CUTOFF/GAUGE DEPENDENCE
7. EVOLUTION IDENTITY OR PROPOSED IDENTITY
8. RELATION TO THE OTHER THREE SHADOWS
9. FASTEST COUNTEREXAMPLE MODEL
10. WHETHER IT USES ANY RH-EQUIVALENT INPUT
11. NON-RH APPLICATION TARGET
12. STATUS: REFUTED / PARTIAL / CANDIDATE only

No agent may call the unified object established until C1--C5 are proved.

---

## I. Promotion rule

The program has succeeded mathematically even without RH if it produces a genuinely new theorem satisfying at least one of the following:

- a canonical relative discriminant/resultant theory for an order-one entire heat class;
- a rigorous regularized identity linking logarithmic discriminant derivative to inverse-square gap trace;
- a new weighted-integrated phase-current sign theorem for a natural kernel class;
- a distributional collision-charge/flux theorem with explicit source;
- a cutoff-independent collision-locality theorem;
- a new theorem showing why such a unification is impossible under natural axioms.

A rigorous impossibility theorem counts as progress because it prevents further search in a false architecture.
