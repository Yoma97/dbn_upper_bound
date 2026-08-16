# Round 86 — Piecewise `beta(alpha)` singular-wedge theorem and the published threshold `2.540788...`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED relative to the literature-recorded published beta bounds listed below; exact assembly arithmetic independently machine-audited.  
**Strict-program admissibility:** PASSED current direct/transitive audit.  
**Primary-source line audit:** PARTIAL — exact statements are independently recorded in ANTEDB/Trudgian--Yang and traced to the cited published Huxley/Sargos/Bourgain sources; not every paywalled original line has been directly opened.  
**Referee status:** PENDING.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Main result

Let

\[
L=\log\frac{x}{4\pi},\qquad \lambda=tL,
\qquad x=4\pi e^{\lambda/t}.
\]

Define the exact rational number

\[
\boxed{
C_{\beta,\mathrm{pub}}
=
\frac{1818938190755}{715895297312}
=
2.540788014091779\ldots .
}
\tag{86.1}
\]

Then for every `epsilon>0` there exists `t_epsilon>0` such that

\[
\boxed{
0<t\le t_\varepsilon,
\qquad
\lambda\ge C_{\beta,\mathrm{pub}}+\varepsilon
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\tag{86.2}

The proof uses only:

- D.H.J. Polymath's analytic effective Riemann--Siegel theorem and explicit errors;
- published one-dimensional logarithmic exponential-sum bounds as recorded in the ANTEDB beta tables;
- the Sargos published exponent pair and Bourgain published bounds;
- Euler-product nonvanishing in `Re s>1`;
- the fixed-cutoff collision transversality already audited in Rounds 82--85.

No RH, finite-height RH verification, upper bound for `Lambda`, pair correlation, zero density, or negative-time local equilibrium is used.

The number in (86.1) is **not** a collision threshold. It is the present frontier of the specific `absolutely-convergent zeta core + best audited published piecewise beta tail` architecture.

---

## 2. Why Round 85 was not optimal

Round 85 fixes a single exponent pair `(k,l)` on the entire tail and therefore majorizes

\[
\beta(\alpha)
\le
k+(\ell-k)\alpha
\]

by one affine line for all values of

\[
\alpha=\frac{\log M}{\log T}.
\]

But the dyadic heat tail sweeps through a whole interval of `alpha`, and classical exponential-sum literature supplies different sharper bounds on different subintervals.

The Analytic Number Theory Exponent Database defines `beta(alpha)` so that, for the logarithmic phase in particular,

\[
\sum_{n\in I}n^{-iT}
\ll
T^{\beta(\alpha)+o(1)},
\qquad
N=T^{\alpha+o(1)},\quad I\subset[N,2N].
\tag{86.3}
\]

Thus `beta(alpha)` is exactly the literature object needed by the heat-weighted half-sum. No conversion through full zeta values is required.

---

## 3. Weighted beta rate

As before, on a dyadic block

\[
M=e^{u/t},
\qquad
T:=\frac{|\tau|}{2\pi}=e^{\lambda/t+o(1)},
\]

put

\[
\alpha=\frac{u}{\lambda}.
\]

The heat-weight amplitude has exponential rate

\[
W_\lambda(u)
=
\frac{u^2}{4}
-\left(\frac12+\frac\lambda4\right)u.
\]

A beta bound

\[
\beta(\alpha)\le B(\alpha)
\]

therefore gives the weighted dyadic rate

\[
G_{\lambda,B}(\alpha)
=
W_\lambda(\lambda\alpha)
+\lambda B(\alpha).
\tag{86.4}
\]

Dividing by positive `lambda`, define

\[
\boxed{
h_{\lambda,B}(\alpha)
=
\frac\lambda4(\alpha^2-\alpha)
-\frac\alpha2
+B(\alpha).
}
\tag{86.5}
\]

A strict negative upper bound for (86.5) on the tail interval yields an exponentially small weighted half-sum, and an extra logarithmic factor remains harmless for the derivative moment.

---

## 4. Core boundary

The absolutely convergent zeta core may extend up to

\[
u_0<\lambda-2,
\]

because

\[
p-\frac{u_0}{4}>1,
\qquad
p=\frac12+\frac\lambda4.
\]

In alpha coordinates the limiting lower edge of the oscillatory tail is therefore

\[
\boxed{
\alpha_{\rm core}(\lambda)
=1-\frac2\lambda.
}
\tag{86.6}

For a theorem with strict epsilon slack one chooses the actual split a fixed small amount below this limiting edge. Thus it suffices to obtain strict negativity of (86.5) on a compact neighborhood of

\[
[1-2/\lambda,1/2].
\]

---

## 5. Uniformization lemma for moving alpha

A pointwise statement about `beta(alpha)` cannot simply be inserted into `O(1/t)` dyadic blocks without an audit, because the block exponent `alpha` moves with `t`.

We use the following elementary compactness lemma.

### Lemma 86.1

Let `J` be a compact alpha interval and let `B(alpha)` be continuous on `J`. Suppose

\[
\beta(\alpha)\le B(\alpha)
\qquad(\alpha\in J).
\]

Then for every `eta>0`, uniformly for logarithmic model phases and for all sufficiently large `T`, whenever

\[
\alpha_T:=\frac{\log N}{\log T}\in J,
\]

one has

\[
\sum_{n\in I}n^{-iT}
\ll_{J,\eta}
T^{B(\alpha_T)+\eta}.
\tag{86.7}
\]

### Proof

If not, there is a sequence `T_j->infinity`, `alpha_j in J`, and intervals `I_j subset [N_j,2N_j]` violating (86.7). Pass to a subsequence with

\[
\alpha_j\to\alpha_*\in J.
\]

Then

\[
N_j=T_j^{\alpha_*+o(1)}.
\]

By the definition of `beta(alpha_*)`,

\[
\sum_{n\in I_j}n^{-iT_j}
\ll
T_j^{\beta(\alpha_*)+o(1)}
\le
T_j^{B(\alpha_*)+o(1)}.
\]

Continuity gives

\[
B(\alpha_j)=B(\alpha_*)+o(1),
\]

contradicting the fixed `eta` violation.

The same argument is applied separately on finitely many closed affine pieces of a piecewise beta envelope.

This step is what makes the literature beta table legitimate for the moving heat-tail blocks.

---

## 6. Convexity reduces each literature piece to two rational checks

If on an interval

\[
B(\alpha)=A+B\alpha,
\]

then

\[
h_{\lambda,B}''(\alpha)=\frac\lambda2>0.
\]

Hence `h` is convex, so its maximum on each closed literature interval occurs at one of the two endpoints.

Therefore a finite piecewise-affine beta envelope can be audited entirely by exact rational endpoint arithmetic.

This is implemented in

`research_lab/certificates/singular_wedge/verify_round86_published_beta_threshold.py`.

No numerical optimizer participates in the proof.

---

## 7. The binding published kink

The binding lower beta line is the published Sargos exponent pair

\[
P_S=
\left(
\frac{1959}{21656},
\frac{16135}{21656}
\right).
\]

It gives the global exponent-pair beta line

\[
B_S(\alpha)
=
\frac{1959}{21656}
+rac{1772}{2707}\alpha.
\tag{86.8}
\]

The adjacent sharper published Huxley table-19.2 line is

\[
B_H(\alpha)
=
\frac{569}{2800}
+rac{1053}{2800}\alpha.
\tag{86.9}
\]

They meet exactly at

\[
\boxed{
\alpha_*
=
\frac{854633}{2111129}
=
0.4048227275547823\ldots
}
\tag{86.10}
\]

with

\[
\boxed{
\beta_*
=
\frac{6003317}{16889032}
=
0.3554565471839949\ldots .
}
\tag{86.11}

Solving

\[
h_{\lambda,B}(\alpha_*)=0
\]

gives

\[
\lambda
=
\frac{4(\beta_*-\alpha_*/2)}{\alpha_*(1-\alpha_*)}
=
\boxed{
\frac{1818938190755}{715895297312}
}.
\tag{86.12}

This is (86.1).

---

## 8. Exact published envelope used in the audit

The rational verifier covers

\[
\alpha\in
[1-2/C_{\beta,\mathrm{pub}},1/2]
\]

with 20 contiguous affine pieces drawn only from:

- Huxley's published Tables 17.1 and 19.2;
- standard `A`/`A^2` transforms of Bourgain's published exponent pair;
- the published Sargos exponent pair (86.8);
- Bourgain's published piecewise beta bounds on the upper-alpha range.

The new Trudgian--Yang exponent pair `(18/199,593/796)` is **not** used in this published-envelope certificate.

For each segment the verifier checks exactly

\[
h_{C_{\beta,\mathrm{pub}},B}(\alpha_{\rm left})\le0,
\qquad
h_{C_{\beta,\mathrm{pub}},B}(\alpha_{\rm right})\le0.
\]

All are strict except the two descriptions of the single common kink `alpha_*`, where equality holds exactly.

Since increasing `lambda` makes

\[
\frac\lambda4(\alpha^2-\alpha)
\]

strictly smaller for `0<alpha<1`, every `lambda>C_beta,pub` has a uniform negative rate margin after the core split is moved an arbitrarily small amount inward.

---

## 9. Completion of the collision argument

The finite lower core is handled exactly as in Rounds 84--85:

\[
S_t^{\rm core}
=
\zeta\left(\frac12+\frac\lambda4+i\tau\right)+o(1),
\]

\[
T_t^{\rm core}
=
-\zeta'\left(\frac12+\frac\lambda4+i\tau\right)+o(1).
\]

The piecewise-beta tail is exponentially small because every weighted beta rate has a strict negative margin.

Since the threshold is greater than 2,

\[
p=\frac12+\frac\lambda4>1,
\]

so the elementary Euler product gives

\[
|\zeta(p+i\tau)|\ge\frac{\zeta(2p)}{\zeta(p)}>0
\]

uniformly on compact lambda intervals bounded away from the threshold.

The logarithmic moment is uniformly bounded. The shrinking Cauchy-radius Polymath error audit of Rounds 84--85 gives

\[
E_0\to0,
\qquad
tE_1\to0.
\]

At a hypothetical collision the normalized real component of `e^{i phi}S_t` is `O(E0)`, so the imaginary component inherits the positive zeta amplitude. Since

\[
t|\phi_x|\to\lambda/4>0,
\]

while the logarithmic-moment correction becomes `o(1/t)` after scaling, the derivative cannot vanish simultaneously.

This proves (86.2).

---

## 10. Current-preprint refinement

The current Trudgian--Yang combined beta table contains the new line

\[
B_{TY}(\alpha)
=
\frac{18}{199}
+rac{521}{796}\alpha
\]

on

\[
\frac{1508}{3825}
\le\alpha\le
\frac{62831}{155153}.
\]

Using the full current-preprint table shifts the binding point to

\[
\alpha_{TY}
=
\frac{62831}{155153}
\]

and gives

\[
\boxed{
C_{\beta,TY}
=
\frac{4911678521}{1933561194}
=
2.5402239847600088\ldots .
}
\tag{86.13}

This improvement is real but tiny.

**Status:** CURRENT-PREPRINT FRONTIER, not canonical published-envelope constant. It is not needed for (86.2).

---

## 11. Why this is much stronger than a single exponent pair

Round 85's best audited single-pair thresholds were approximately

\[
2.89655\quad\text{(Bourgain)},
\]

and a literature-pair convex-combination candidate near

\[
2.70035.
\]

The piecewise-beta method reaches `2.540788...` because it uses a different optimal exponential-sum estimate at different dyadic scales. The binding point is not at the core boundary and not at the Riemann--Siegel cutoff; it is an interior kink of the published beta envelope.

Thus Round 85 remains a useful conceptual theorem but is no longer the best literature-assisted singular-wedge implementation.

---

## 12. Architectural floor remains lambda=2

If the exponent-pair conjecture were true, equivalently

\[
\beta(\alpha)=\alpha/2
\qquad(0\le\alpha\le1),
\]

then

\[
h_{\lambda}(\alpha)
=
\frac\lambda4(\alpha^2-\alpha)<0
\]

throughout the interior tail for every `lambda>0`.

Nevertheless the present core reference requires

\[
p=\frac12+\frac\lambda4>1,
\]

hence

\[
\boxed{\lambda>2.}
\]

So improving exponential-sum estimates alone can, at best within this architecture, move the small-time frontier toward 2. Crossing 2 requires a new core mechanism replacing the absolutely convergent Euler-product anchor.

---

## 13. Source audit

The exact beta normalization and logarithmic-phase specialization are recorded in the current ANTEDB blueprint. The same database records the old Huxley table bounds with original-source references, Bourgain's 2017 beta bounds, and the Sargos/Huxley--Kolesnik exponent pairs.

Independent cross-checks were made against Trudgian--Yang's exponent-pair survey and the official bibliographic pages of the Sargos and Huxley--Kolesnik publications.

Because the original Huxley monograph tables and all exact paywalled Sargos/Huxley--Kolesnik theorem lines were not directly opened in this run, the project labels the source-line audit **PARTIAL** rather than pretending complete primary-line access.

The exact rational combination and every endpoint inequality, however, are independently machine-verifiable from the source statements recorded in the database.

---

## 14. Circularity audit

### Used

- Polymath analytic Riemann--Siegel theorem and explicit errors;
- published exponential-sum/beta bounds;
- Euler product only in `Re s>1`;
- fixed-cutoff collision-conditioned derivative identity.

### Not used

- RH or finite-height RH verification;
- any numerical upper bound on `Lambda`;
- pair correlation/GUE;
- zeta zero-density estimates;
- full-zeta subconvexity substituted for a half-sum;
- `H_0` real-rootedness;
- Laguerre--Polya membership as an input;
- negative-time Rodgers--Tao local equilibrium.

**RH remains OPEN.**
