# Current Collision Program State

**Updated:** 2026-08-15 after Round 22.

**RH status:** OPEN.

## Executive verdict

The program has now separated three logically distinct layers:

\[
\boxed{\text{local collision geometry}}
\]

\[
\boxed{\text{relative energy / entropy / cutoff transport}}
\]

\[
\boxed{\text{topological collision count}}.
\]

The first layer is largely understood. The second has exact algebraic balance laws but still lacks an independent finite one-sided entropy/coercive budget. The third has a complete local degree formula, but Round 21 shows that its global finite-dimensional meaning is exactly the change in the number of nonreal conjugate root pairs; hence a global degree-zero theorem risks being a disguised real-rootedness theorem.

The current priority is therefore

\[
\boxed{A\gtrsim B\gg C.}
\]

where:

- **A:** relative Vandermonde / Bregman / exact Rodgers--Tao \(V\)-energy / cutoff commutator, seeking an independent finite budget;
- **B:** all-multiplicity collision degree, retained only if a boundary winding estimate can be proved from genuinely weaker Riemann-specific information;
- **C:** low-complexity arithmetic separator, tertiary.

Round-15 oscillatory sign-regularity is **FROZEN / AUXILIARY**.

---

## 1. Local collision section — PROVED

For a finite simple real-zero cluster \(I\) of a real analytic backward-heat family

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

and the oriented local collision section

\[
\mathcal D_I=(-1)^{m(m-1)/2}\prod_{i\in I}F_x(t,x_i)
\]

factorizes as

\[
\boxed{
\mathcal D_I=\Delta_I\prod_{i\in I}a(t,x_i).
}
\]

Thus \(\Delta_I\) is zero-set-only, while \(\mathcal D_I\) is a gauge-completed local entire-function section. No global canonical regularized discriminant is assumed.

At a simple zero,

\[
A_i=\frac{F_{xx}}{2F_x}(t,x_i),
\qquad
B_i=A_i^2-\frac{F_{xxx}}{3F_x}(t,x_i).
\]

For an order-one entire zero divisor,

\[
\boxed{
B_i=\sum_{\rho\ne x_i}\frac1{(x_i-\rho)^2}
}
\]

is absolutely convergent. The true divergence problem is the **global infinite-volume pair energy**, not the fixed-root inverse-square trace.

---

## 2. Finite Vandermonde / Hamiltonian conventions — PROVED

For a finite real-simple zero set,

\[
E_{\rm ord}=\sum_{i\ne j}(x_i-x_j)^{-2},
\qquad
E_{\rm unord}=\sum_{i<j}(x_i-x_j)^{-2},
\]

\[
\boxed{
\partial_t\log\Delta=4E_{\rm ord}=8E_{\rm unord}.
}
\]

With ordered Hamiltonian

\[
\mathcal H=\sum_{i\ne j}\log|x_i-x_j|^{-1},
\]

\[
\boxed{
\mathcal H=-\log\Delta,
\qquad
\dot{\mathcal H}=-4E_{\rm ord}.
}
\]

Thus finite discriminant and inverse-square energy are literally the same gradient-flow structure.

---

## 3. Hard-window boundary flux — PROVED

For a finite window \(I\),

\[
A_i^I=\sum_{j\in I,j\ne i}(x_i-x_j)^{-1},
\qquad
A_i^{\rm ext}=A_i-A_i^I,
\]

one has

\[
\boxed{
\partial_t\log\Delta_I
=4E_{\rm ord}(I)
+4\sum_{i\in I}A_i^I A_i^{\rm ext}.
}
\]

The local factorization gives

\[
\boxed{A_i^{\rm ext}=a_z/a(t,x_i).}
\]

At an isolated generic double collision, with \(\tau=t-t_c\downarrow0\),

\[
\boxed{g(\tau)^2=8\tau+O(\tau^2),}
\]

so

\[
4E_{\rm pair,ord}=\frac1\tau+O(1),
\]

while the hard-window external flux is \(O(1)\).

---

## 4. Laguerre bridge — PROVED LOCALLY

At a simple zero,

\[
L_1=F_x^2-FF_{xx},
\]

and the previously derived \(L_2\) identity gives

\[
\boxed{B_i=\frac{L_2(x_i)}{L_1(x_i)},}
\qquad
\boxed{A_i=\frac{\partial_xL_1(x_i)}{2L_1(x_i)}.}
\]

Hence

\[
\boxed{
\frac d{dt}\log|F_x(t,x_i(t))|
=\frac14(\partial_x\log L_1)^2+3\frac{L_2}{L_1}.
}
\]

The phase current is permanently removed as an independent route because

\[
\Im(\overline{(F+iF_x)}(F+iF_x)_x)=-L_1.
\]

Ordinary \(L_1\ge0\) is not a complete Laguerre--Polya criterion; complete generalized real and complex Laguerre characterizations must be distinguished from it.

---

## 5. Positive-threshold finite collision attainment — PROVED AS REDUCTION

Using Polymath high-positive-time asymptotics and compactness, if

\[
\Lambda>0,
\]

then the transition at \(t=\Lambda\) is attained by a multiple real zero at finite height. Thus a hypothetical positive threshold cannot exist solely through collisions escaping to infinity.

Together with Rodgers--Tao \(\Lambda\ge0\), this reduces RH to positive-time no-collision, but this reduction is itself RH-equivalent and is **not** counted as progress toward a proof without an independent no-collision input.

---

## 6. Round 17 Bregman balance — PROVED FINITELY

For a fixed ordered reference \(\xi_j\), cutoff \(\psi_j\),

\[
r_{jk}=\frac{x_j-x_k}{\xi_j-\xi_k}>0,
\qquad
L(r)=-\log r+r-1,
\]

let

\[
\mathcal C_\psi
=\sum_{j\ne k}\psi_j\psi_kL(r_{jk}),
\]

\[
\delta_{jk}=(x_j-x_k)^{-1}-(\xi_j-\xi_k)^{-1},
\qquad
D_j^\psi=\sum_{k\ne j}\psi_k\delta_{jk}.
\]

Round 17 gives an exact force-square balance. Round 22 sharpens its bookkeeping by introducing

\[
K_j^\psi
=\sum_{k\ne j}(\psi_j-\psi_k)\delta_{jk}.
\]

Then exactly

\[
\boxed{
\partial_t\mathcal C_\psi
=-4\sum_j(D_j^\psi)^2
-4\sum_jD_j^\psi K_j^\psi
-4\sum_j\psi_jD_j^\psi S_j^\xi.
}
\]

Thus the cutoff channel is an exact discrete commutator and vanishes for constant cutoff.

The infinite countable version remains conditional on the justified principal-value / absolute-convergence / differentiation interchange.

---

## 7. Round 18 exact Rodgers--Tao V-energy law — PROVED ALGEBRAICALLY

For any symmetric pair weight \(w_{jk}\), define

\[
\mathscr C_w
=\sum_{j\ne k}w_{jk}
\log\left|\frac{x_j-x_k}{\xi_j-\xi_k}\right|.
\]

With Rodgers--Tao

\[
V(r)=r^{-2}-1+2(r-1),
\]

there is an exact decomposition

\[
\boxed{
\partial_t\mathscr C_w
=4\widetilde E_w^V+4\mathscr F_w+4\mathscr R_w,
}
\]

where \(\widetilde E_w^V\ge0\) is exactly the weighted Rodgers--Tao pair energy, \(\mathscr F_w\) is an explicit triple cutoff commutator, and \(\mathscr R_w\) is an explicit reference/tangent term.

This is exact algebraic bookkeeping. It does not replace Rodgers--Tao's analytic estimates.

---

## 8. Entropy-budget obstruction — PROVED / DECISIVE

The heat polynomial

\[
P_t(z)=z^2-2t
\]

has a collision at \(t=0\), zero external flux, and

\[
\Delta=8t,
\qquad
E_{\rm ord}=\frac1{4t},
\qquad
\partial_t\log\Delta=\frac1t.
\]

Therefore

\[
\boxed{
\text{nonintegrable bulk + integrable/zero flux does not imply no collision}.
}
\]

The divergent bulk is paid for by the divergent entropy itself. Consequently **Program A cannot close by flux control alone**.

The decisive missing A-gate is an independently provable one-sided finite entropy/coercive budget, or a compensated quantity with an independently meaningful cancellation of the collision divergence.

Any proposed budget must be rejected if it is merely a lower-gap or real-rootedness hypothesis in disguise.

---

## 9. Round 20 reference-force asymptotic — PROVED / NOVELTY UNVERIFIED

For Rodgers--Tao classical locations

\[
\Psi(\xi_j)=j,
\qquad
\Psi(x)=\frac{x}{4\pi}\left(\log\frac{x}{4\pi}-1\right),
\qquad
\xi_{-j}=-\xi_j,
\]

the reference force satisfies

\[
\boxed{
S_j^\xi
=-\frac\pi8+O\!\left(\frac{\log j}{\sqrt j}\right),
\qquad j\to+\infty,
}
\]

and by odd symmetry

\[
S_{-j}^\xi
=+\frac\pi8+O\!\left(\frac{\log j}{\sqrt j}\right).
\]

The proof uses only the explicit reference counting map. It is independent of RH and actual zero estimates.

The induced formal collective speed

\[
2S_j^\xi\to-\pi/4
\]

is consistent with the independent Polymath high-positive-time zero-velocity asymptotic.

---

## 10. Round 22 reference and cutoff control — PROVED STRUCTURALLY

### Pointwise V-domination

For every positive relative spacing \(r=(x_j-x_k)/(\xi_j-\xi_k)>0\),

\[
\boxed{
\delta_{jk}^2
\le
\frac1{(\xi_j-\xi_k)^2}V(r)
=\widetilde E^V_{jk}.
}
\]

Indeed,

\[
V(r)-(r^{-1}-1)^2
=2(r+r^{-1}-2)\ge0.
\]

### Finite-range cutoff commutator

If

\[
|\psi_j-\psi_k|
\le L_\psi|j-k|\sqrt{\psi_j\psi_k}
\]

for \(0<|j-k|\le R\), then

\[
\boxed{
\sum_j|K_{j,R}^\psi|^2
\ll L_\psi^2R^3\widetilde E^{V,\rm ord}_{\psi,R}.
}
\]

For Rodgers--Tao's

\[
\psi_T(j)=\left(1+\frac{|j|}{T\log T}\right)^{-100}
\]

and their nearby scale in the main window, the coefficient is of size

\[
L_\psi^2R^3\ll T^{-1.4}\log^{-2}T
\]

up to harmless nearby-scale variation. Thus the **near cutoff commutator is perturbative** at the cutoff-geometric level.

The far commutator is still open in the positive-time regime relevant to proving \(\Lambda\le0\).

### Signed reference decomposition

For even \(\psi\) and symmetric zero/reference configurations,

\[
\boxed{
\mathscr R_{\xi,\psi}
=
\pi\sum_{j,l>0}\psi_j\psi_l
\left(
\frac1{x_j+x_l}-\frac1{\xi_j+\xi_l}
\right)
-4\sum_j\psi_jD_j e_j,
}
\]

where

\[
S_j^\xi=-\frac\pi8\operatorname{sgn}j+e_j.
\]

Thus the leading signed drift becomes a **regular cross-origin interaction**, not a singular same-sign collision term.

For \(\psi_T\),

\[
\boxed{
\sum_j\psi_T(j)e_j^2\ll\log^3(T\log T+2),
}
\]

so the residual reference channel is absorbable into the force-square bulk at only polylogarithmic additive cost.

---

## 11. Round 19 / 21 collision degree — PROVED LOCALLY, GLOBAL RISK IDENTIFIED

For every multiplicity-\(m\ge2\) real collision of a nontrivial analytic backward-heat family,

\[
\Gamma=(F,F_x)
\]

has local Brouwer degree

\[
\boxed{
\deg_{\rm loc}\Gamma=-\left\lfloor\frac m2\right\rfloor.
}
\]

A parabolic blow-up argument also proves local isolation directly.

However Round 21 proves that for finite polynomial heat flow this local degree equals the change in the number of nonreal conjugate root pairs across the collision. Globally,

\[
\boxed{
\sum_{p}\deg_{\rm loc}(P,P_x;p)
=C(t_+)-C(t_-),
}
\]

where \(C(t)\) counts nonreal conjugate pairs.

Therefore a global boundary theorem giving degree zero can be **exactly a topological restatement of real-rootedness defect**. Program B is independent progress only if its boundary winding is computed from an input genuinely weaker than the desired real-rootedness conclusion.

A particularly dangerous circular route is horizontal phase monotonicity, because

\[
\partial_x\arg(H+iH')
=-\frac{L_1(H)}{H^2+(H')^2}.
\]

Using global \(L_1\ge0\) to control winding simply returns to a Laguerre/Hermite--Biehler type criterion.

---

## 12. Safe and unsafe source imports

### Safe

- structural zero ODE and principal-value conventions;
- explicit Rodgers--Tao reference \(\xi_j\) and cutoff \(\psi_T\);
- purely algebraic identities involving \(V,L\), cutoffs, and finite configurations;
- unconditional Polymath positive-time asymptotics in the ranges actually proved;
- source-established kernel properties independent of RH.

### Unsafe for proving \(\Lambda\le0\)

Rodgers--Tao quantitative negative-time estimates that are proved under their contradiction hypothesis \(\Lambda<0\). That hypothesis already implies RH, so such estimates may not be imported into our positive-time no-collision argument without independent reproof.

---

## 13. Current single targets

### A1 — DECISIVE
Construct or derive an **independent one-sided entropy/coercive budget** for a localized relative entropy/compensated entropy, valid in the positive-time candidate-collision regime, that cannot diverge in the collision direction.

It must not assume a lower gap bound, real-rootedness, \(L_1\ge0\), or an RH-equivalent criterion.

### A2 — SUPPORTING
Control the **far cutoff commutator** and the regular cross-origin reference interaction using positive-time/unconditional inputs.

### B1 — AUDIT ONLY UNTIL INDEPENDENCE IS SHOWN
Seek a boundary winding estimate for \(H+iH'\) only if its proof avoids Laguerre/Hermite--Biehler/real-rootedness equivalents. Otherwise classify Program B as structurally circular and freeze it.

---

## 14. Ranking

\[
\boxed{A\gtrsim B\gg C.}
\]

- **A PRIMARY:** exact relative energy/entropy transport + missing finite one-sided budget.
- **B SECONDARY LIVE:** exact local collision count, but high global equivalence risk.
- **C TERTIARY:** low-complexity arithmetic separator.
- **Round 15 sign-regularity:** frozen auxiliary material.
- **Phase current:** permanently removed as an independent route.

---

## 15. Status table

- local collision divisor geometry: **PROVED**;
- fixed-root inverse-square trace: **PROVED**;
- global canonical regularized discriminant: **NOT ASSUMED / OPEN**;
- finite Vandermonde / energy identity: **PROVED**;
- hard-window external flux identity: **PROVED**;
- exact Bregman force-square law: **PROVED FINITELY**;
- exact relative log-Vandermonde / Rodgers--Tao \(V\)-energy law: **PROVED ALGEBRAICALLY**;
- near cutoff commutator perturbativity: **PROVED structurally**;
- far cutoff commutator in needed positive-time regime: **OPEN**;
- reference-force asymptotic \(\mp\pi/8\): **PROVED / NOVELTY UNVERIFIED**;
- residual reference channel polylog control: **PROVED**;
- regular cross-origin reference interaction: **IDENTIFIED / coarse V-control proved**;
- flux-only no-collision mechanism: **REFUTED**;
- independent finite entropy/coercive budget: **OPEN — DECISIVE A GATE**;
- all-multiplicity local degree \(-\lfloor m/2\rfloor\): **PROVED**;
- finite polynomial degree = nonreal-pair-count change: **PROVED**;
- global degree as automatically independent no-collision mechanism: **REFUTED / equivalence risk high**;
- independent Riemann boundary winding theorem: **OPEN**;
- RH: **OPEN**;
- novelty of the new packaging/results: **UNVERIFIED**.
