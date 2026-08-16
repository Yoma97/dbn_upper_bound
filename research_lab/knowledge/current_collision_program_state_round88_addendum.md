# Collision Program State — Round 88 Addendum

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Canonical policy:** the strict track excludes finite-height RH verification anywhere in the proof ancestry.

---

## 1. Full-time strict shoulder remains 6.50

The strongest current theorem valid for the entire time interval is still Round 81:

\[
\boxed{
0<t\le1/2,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge6.50
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\]

This is an internally proved 512/768-bit certified project theorem; referee verification remains pending.

Do not confuse the much lower constants below with a new global full-time shoulder threshold.  They are **small-time singular-wedge thresholds** of the quantified form `for every epsilon>0 there exists t_epsilon>0`.

---

## 2. Small-time singular-wedge frontier: published piecewise-beta architecture

Rounds 82--86 progressively replace absolute/triangle control by direct logarithmic exponential-sum control of the individual Riemann--Siegel half-sum.

The strongest current published-envelope theorem is Round 86.

Define

\[
\boxed{
C_{\beta,\mathrm{pub}}
=
\frac{1818938190755}{715895297312}
=
2.540788014091779\ldots .
}
\]

Then

\[
\boxed{
\forall\varepsilon>0\ \exists t_\varepsilon>0:\quad
0<t\le t_\varepsilon,
\quad
\lambda\ge C_{\beta,\mathrm{pub}}+\varepsilon
\Longrightarrow
(H_t,H_t')\ne(0,0).
}
\]

Status:

- `INTERNALLY_PROVED` relative to the exact published beta bounds recorded in the literature map;
- exact finite rational assembly verified independently by GitHub Actions;
- `PRIMARY_SOURCE_LINE_AUDIT: PARTIAL` for some old paywalled Huxley/Sargos lines;
- `REFEREE_VERIFIED: PENDING`;
- `NOVELTY_UNVERIFIED`.

The exact binding kink is

\[
\alpha_*=rac{854633}{2111129},
\qquad
\beta_*=rac{6003317}{16889032},
\]

where the published Sargos exponent-pair line meets the adjacent Huxley beta line.

The exact verifier is

`research_lab/certificates/singular_wedge/verify_round86_published_beta_threshold.py`.

It checks 20 contiguous rational beta segments on

\[
\alpha\in
\left[1-\frac{2}{C_{\beta,\mathrm{pub}}},\frac12\right]
\]

and verifies all endpoint weighted-rate inequalities exactly.  The CI run `31957365800` completed successfully.

---

## 3. Current-preprint beta refinement is not canonical

The current Trudgian--Yang combined beta table gives a slightly better frontier candidate

\[
C_{\beta,TY}
=
\frac{4911678521}{1933561194}
=
2.5402239847600088\ldots .
\]

This is **CURRENT-PREPRINT FRONTIER**, not the canonical published-envelope constant.  The improvement is too small to justify weakening source standards.

---

## 4. Historical singular-wedge milestones

### Round 82 — complex zeta envelope

For every compact `K subset (4,infinity)`, the exact heat-weighted half-sum satisfies

\[
S_t
=
\zeta\left(\frac12+\frac\lambda4+i\tau\right)+o_K(1)
\]

uniformly in the unbounded phase `tau`, and Euler-product nonvanishing closes collisions for sufficiently small `t`.  This removed the old triangle floor `4.914588956...`.

### Round 84 — explicit third-derivative tail

Arias de Reyna's explicit `d=3` van der Corput theorem controls the individual half-sum directly, yielding small-time exclusion for every

\[
\lambda>3+\varepsilon.
\]

### Round 85 — general exponent-pair theorem

For any limiting exponent pair `(k,l)`, define

\[
C_{EP}(k,\ell)
=
\max\left\{
2,
\frac{2(1+k-\ell)}{1-\ell},
8(k+\ell)-4
\right\}.
\]

Then the singular wedge is collision-free for sufficiently small time above `C_EP+epsilon`.  Bourgain's published pair gives `84/29≈2.89655`.

### Round 86 — piecewise beta

Using different published exponential-sum bounds at different dyadic scales improves the frontier to `2.540788...`.

---

## 5. The architecture has a genuine core barrier at lambda=2

The tail estimates can improve further, but the Rounds 82--86 core is anchored by

\[
S_t^{core}
\approx
\zeta\left(p+i\tau\right),
\qquad
p=\frac12+\frac\lambda4,
\]

followed by Euler-product nonvanishing in `p>1`.

This reaches the boundary `p=1` exactly at

\[
\boxed{\lambda=2.}
\]

Round 87 proves the methodological no-go:

> A continuation below 2 that simply replaces the Euler-product bound by an unexplained positive uniform lower bound for `|zeta(p+iT)|` would be a hidden zero-free assertion in the critical strip and is not an admissible independent estimate.

Likewise, a generic positive lower bound for `|zeta|+|zeta'|` would import an unresolved zero-simplicity/derivative problem.

Thus improving beta/exponent-pair estimates alone cannot cross the present core architecture's `lambda=2` floor.

---

## 6. Round 88: naive joint-core positivity is false

The phase-invariant joint quantity

\[
\mathfrak D_t
=\phi_x|S|^2
-\sigma_x\Im(\overline ST)
-\tau_x\Re(\overline ST)
\]

has leading scaled kernel

\[
-4t\mathfrak D_t
\approx
\sum_{m,n}
(\lambda-u_m-u_n)z_n\overline{z_m},
\qquad
u_n=t\log n.
\]

Although every scalar entry is nonnegative to leading order inside the Riemann--Siegel cutoff, the kernel is not positive semidefinite:

\[
\det
\begin{pmatrix}
\lambda-2u_1&\lambda-u_1-u_2\\
\lambda-u_1-u_2&\lambda-2u_2
\end{pmatrix}
=-(u_1-u_2)^2<0.
\]

Therefore a diagonal/entrywise positivity argument is **REFUTED**.

---

## 7. New collision-conditioned target: endpoint-moment transversality

Define

\[
S_0
=
\sum_{n\le N}a_ne^{-i\tau\log n},
\]

\[
S_1
=
\sum_{n\le N}
\left(\frac\lambda2-t\log n\right)
a_ne^{-i\tau\log n}.
\]

Round 88 shows that a hypothetical collision forces asymptotically

\[
\boxed{
\Re(e^{i\phi}S_0)=0,
\qquad
\Im(e^{i\phi}S_1)=0,
}
\]

with explicit Polymath `E0,tE1` perturbations in the exact statement.

The second sum retains the distance of each term from the moving Riemann--Siegel cutoff.  It is not merely the old scalar `A1` moment.

The next primary theorem target is therefore:

> **EMT — Endpoint-Moment Transversality:** prove, in a nonempty range `lambda<=2`, that the two rotated conditions above cannot hold simultaneously, with rigorous approximation errors.

This target tolerates possible zeros of zeta in the critical strip and therefore avoids the hidden-nonvanishing trap of Round 87.

---

## 8. Preferred EMT attack order

1. Derive a two-component Riemann--Siegel/saddle transform for `(S0,S1)` retaining the fractional saddle parameter.
2. Inspect whether `S1` becomes a derivative of the classical saddle correction; if so, test a Wronskian/nondegeneracy condition.
3. If the transformed system depends on a compact fractional parameter only, build a rigorous interval certificate for the joint determinant.
4. Use beta/exponent-pair estimates only for the remaining remote tail.
5. If the two-component transform reduces to uncontrolled shifted correlations, compare explicitly with the prime-side no-go results of Rounds 48--61 before inventing a renamed version of the same problem.

Do not attempt generic positivity of the Round-88 kernel; it is algebraically false.

---

## 9. Current program hierarchy

### Full-time certified zone

\[
\boxed{\lambda\ge6.50}
\]

for all `0<t<=1/2`.

### Small-time published-beta zone

\[
\boxed{
\lambda>2.540788014091779\ldots
}
\]

in the quantified sufficiently-small-time sense.

### Tail-optimization zone

\[
2<\lambda\le2.540788\ldots
\]

may improve using stronger published/current beta bounds, but this is no longer the deepest structural obstacle.

### Core-invention zone

\[
\boxed{0<\lambda\le2.}
\]

requires EMT or an equivalent collision-conditioned core mechanism.

The bounded-spatial/core region outside the singular scaling remains a separate compact/global-closure problem after the singular wedge is solved.

---

## 10. Circularity status

No result in Rounds 82--88 uses:

- RH;
- finite-height RH verification;
- a numerical upper bound on `Lambda`;
- pair correlation/GUE;
- zeta nonvanishing in `1/2<Re s<1`;
- Laguerre--Polya membership of `H_0`;
- negative-time Rodgers--Tao local equilibrium.

Published logarithmic exponential-sum bounds are used only to control the individual Riemann--Siegel half-sum, not as hidden zeta zero-free assertions.

**RH remains OPEN.**
