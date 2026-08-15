# Round 19 — Local Brouwer degree of every heat-flow collision multiplicity

**Date:** 2026-08-15

**Status:** PROVED locally under the stated analytic backward-heat hypotheses. Global boundary degree remains OPEN.

**RH status:** OPEN.

## 0. Main result

Let \(F(t,x)\) be a nonzero real-analytic solution of

\[
\partial_tF=-\partial_x^2F
\]

near \((t_c,c)\). Suppose

\[
F(t_c,c)=F_x(t_c,c)=\cdots=F_x^{(m-1)}(t_c,c)=0,
\qquad
F_x^{(m)}(t_c,c)\ne0,
\]

with \(m\ge2\). Define

\[
\Gamma(t,x):=(F(t,x),F_x(t,x)).
\]

Then \((t_c,c)\) is an isolated zero of \(\Gamma\), and

\[
\boxed{
\deg_{\rm loc}(\Gamma,(t_c,c))
=-\left\lfloor\frac m2\right\rfloor.
}
\]

Consequences:

- \(m=2,3\): local degree \(-1\);
- \(m=4,5\): local degree \(-2\);
- \(m=6,7\): local degree \(-3\);
- etc.

Thus the previous warning “higher multiplicities need a separate local degree analysis” was correct, but the analysis can be completed: **every isolated real multiple-zero event of a nontrivial analytic backward-heat family has strictly negative local Brouwer degree.**

The universal charge is not \(-1\); it is \(-\lfloor m/2\rfloor\).

---

## 1. Parabolic leading model

Translate \((t_c,c)\) to \((0,0)\). Write

\[
F(0,x)=a x^m+O(x^{m+1}),
\qquad a\ne0.
\]

The parabolic leading jet, with weight \(2\) for \(t\) and weight \(1\) for \(x\), is

\[
P_m(t,x):=e^{-t\partial_x^2}x^m.
\]

Explicitly,

\[
\boxed{
P_m(t,x)
=m!\sum_{k=0}^{\lfloor m/2\rfloor}
\frac{(-t)^k x^{m-2k}}{k!(m-2k)!}.
}
\]

It satisfies

\[
\partial_tP_m=-\partial_x^2P_m,
\qquad
\partial_xP_m=mP_{m-1}.
\]

Under the parabolic rescaling

\[
t=r^2T,
\qquad
x=rX,
\]

define

\[
G_r(T,X):=
\left(
\frac{F(r^2T,rX)}{a r^m},
\frac{F_x(r^2T,rX)}{a r^{m-1}}
\right).
\]

Analyticity plus the heat equation give, uniformly in \(C^1\) on compact sets,

\[
\boxed{
G_r(T,X)
\longrightarrow
\Gamma_m(T,X):=(P_m(T,X),\partial_XP_m(T,X))
}
\]

as \(r\downarrow0\).

The diagonal output rescaling has positive determinant, so it does not alter Brouwer degree.

---

## 2. The model zero is isolated

For \(T>0\),

\[
P_m(T,X)
=T^{m/2}H_m\!\left(\frac{X}{2\sqrt T}\right),
\]

where \(H_m\) is the physicists' Hermite polynomial. Hence \(P_m(T,\cdot)\) has \(m\) distinct real zeros, and

\[
\partial_XP_m=mP_{m-1}
\]

does not vanish at any of them because consecutive Hermite polynomials have no common zero.

For \(T<0\), write \(T=-S\), \(S>0\). Then

\[
P_m(-S,X)
=m!\sum_{k=0}^{\lfloor m/2\rfloor}
\frac{S^kX^{m-2k}}{k!(m-2k)!}.
\]

If \(m\) is even, every term is nonnegative and the constant term is positive, so \(P_m(-S,X)>0\) for every real \(X\).

If \(m\) is odd, factor

\[
P_m(-S,X)=XQ_m(S,X^2),
\]

where \(Q_m>0\) for \(S>0\). Thus the only real zero is \(X=0\), but there

\[
\partial_XP_m(-S,0)>0.
\]

Therefore

\[
\Gamma_m(T,X)=0
\]

only at \((T,X)=(0,0)\).

It follows that the model origin is isolated.

For the original analytic family, a non-isolated curve of common zeros of \(F\) and \(F_x\) is impossible unless \(F\equiv0\): along such a curve, differentiating \(F=F_x=0\) and using \(F_t=-F_{xx}\) successively forces

\[
F_{xx}=F_{xxx}=F_{xxxx}=\cdots=0
\]

there, and analyticity then forces local triviality. Hence the collision point is isolated for a nontrivial family.

---

## 3. Reduction of local degree to the Hermite model

Choose a bounded neighborhood \(\Omega\) of the origin in the \((T,X)\)-plane such that

\[
0\notin\Gamma_m(\partial\Omega).
\]

The \(C^1\)-convergence above implies that, for sufficiently small \(r\), the straight-line homotopy between \(G_r\) and \(\Gamma_m\) has no boundary zero. Therefore

\[
\deg(G_r,\Omega,0)
=\deg(\Gamma_m,\Omega,0).
\]

Undoing the parabolic domain scaling and positive-determinant output scaling gives

\[
\boxed{
\deg_{\rm loc}(\Gamma,(0,0))
=\deg_{\rm loc}(\Gamma_m,(0,0)).
}
\]

So it remains only to compute the model degree.

---

## 4. Model degree via the regular value \((0,\varepsilon)\)

Fix a sufficiently small \(\varepsilon>0\). Compute the degree using the regular value

\[
(0,\varepsilon).
\]

Thus we count solutions of

\[
P_m(T,X)=0,
\qquad
\partial_XP_m(T,X)=\varepsilon,
\]

with the signs of their Jacobians.

### 4.1. Positive-time preimages

For \(T>0\), let

\[
h_1<h_2<\cdots<h_m
\]

be the roots of \(H_m\). The zero branches are

\[
X_r(T)=2\sqrt T\,h_r.
\]

Along the branch,

\[
Q_r(T):=\partial_XP_m(T,X_r(T))
=\frac12T^{(m-1)/2}H_m'(h_r).
\]

Because the leading coefficient of \(H_m\) is positive,

\[
\operatorname{sgn}H_m'(h_r)=(-1)^{m-r}.
\]

Hence the number of roots with \(H_m'(h_r)>0\) is

\[
N_+=\left\lceil\frac m2\right\rceil.
\]

For each such root there is exactly one small \(T>0\) with \(Q_r(T)=\varepsilon\).

To compute its Jacobian sign, use local coordinates

\[
U=X-X_r(T).
\]

Along \(U=0\),

\[
P_m=0,
\qquad
\partial_UP_m=Q_r(T)=\varepsilon.
\]

Also

\[
Q_r'(T)=\frac{m-1}{2T}Q_r(T)>0.
\]

Therefore

\[
\det D(P_m,\partial_XP_m)
=-Q_r(T)Q_r'(T)<0.
\]

Every positive-time preimage contributes \(-1\).

Thus the total positive-time contribution is

\[
-\left\lceil\frac m2\right\rceil.
\]

### 4.2. Negative-time preimages

If \(m\) is even, \(P_m(T,X)\) has no real zero for \(T<0\), so there is no contribution.

Let

\[
m=2n+1
\]

be odd. For \(T=-S<0\), the only real zero is \(X=0\), and

\[
Q(T):=\partial_XP_m(T,0)
=\frac{m!}{n!}(-T)^n>0.
\]

For \(m\ge3\), there is exactly one small negative \(T\) such that

\[
Q(T)=\varepsilon.
\]

Moreover

\[
Q'(T)<0.
\]

Using \(U=X\) as the transverse coordinate, the same local determinant calculation gives

\[
\det D(P_m,\partial_XP_m)
=-Q(T)Q'(T)>0.
\]

Thus the negative-time branch contributes \(+1\) when \(m\) is odd.

---

## 5. Degree formula — PROVED

If \(m=2n\) is even,

\[
\deg_{\rm loc}\Gamma_m=-n.
\]

If \(m=2n+1\) is odd,

\[
\deg_{\rm loc}\Gamma_m=-(n+1)+1=-n.
\]

Therefore in all cases

\[
\boxed{
\deg_{\rm loc}(F,F_x)
=-\left\lfloor\frac m2\right\rfloor.
}
\]

This proves the main theorem.

---

## 6. Interpretation for the collision program

The local topological picture is now substantially stronger than in Round 16.

Previously only a generic double collision had a certified charge

\[
-1.
\]

Now every isolated multiplicity-\(m\) collision has strictly negative charge

\[
-\lfloor m/2\rfloor.
\]

Hence on any bounded domain \(D\) in the \((t,x)\)-plane containing finitely many collision points and no boundary collision,

\[
\boxed{
\deg(\Gamma,D,0)
=-\sum_{p\in D}\left\lfloor\frac{m_p}{2}\right\rfloor<0
}
\]

if at least one collision occurs.

Consequently, if one can independently prove

\[
\deg(\Gamma,D,0)=0,
\]

then **there are no collision points in \(D\)**, with no genericity assumption on their multiplicities.

This is a genuine advantage over the entropy balance: the degree is a finite integer budget, whereas the Vandermonde/Bregman entropy naturally diverges at collision.

---

## 7. New global target for Program B

The remaining issue is entirely on the boundary.

Choose a rectangle or smoothly rounded domain

\[
D=[t_-,t_+]\times[-X,X]
\]

and define

\[
\Gamma=(H_t,H_t').
\]

A global collision exclusion theorem would follow from:

1. **Boundary nonvanishing:** \(\Gamma\ne0\) on \(\partial D\).
2. **Boundary winding computation:** prove
   \[
   \deg(\Gamma,D,0)=0.
   \]
3. **Exhaustion:** send \(X\to\infty\) and, if needed, \(t_-\downarrow0\), controlling the vertical and horizontal boundary contributions.

Because every interior local degree is negative, no cancellation between different collision multiplicities is possible.

Thus the earlier phrase “higher multiplicities may have unknown charges that cancel generic double collisions” is now removed.

---

## 8. Circularity guard

This local theorem is purely analytic/topological and does not assume:

- RH;
- \(\Lambda\le0\);
- all zeros of \(H_t\) are real;
- a lower gap bound;
- Laguerre--Polya membership.

It applies to any real-analytic backward-heat family at an isolated real multiple zero.

For the Riemann application, the global boundary computation must still be audited separately. In particular, a normalization that is merely nonvanishing does not by itself determine the winding of \((H,H')\).

---

## 9. Updated route comparison

Round 18 showed that flux control alone cannot exclude collision because the entropy itself carries the logarithmic divergence. Round 19 shows that the degree route has a stronger local sign structure than previously known within the program.

Accordingly the working ranking should be upgraded from

\[
A>B>C
\]

to

\[
\boxed{B\gtrsim A\gg C.}
\]

Here:

- **B:** all-multiplicity negative local degree + global boundary winding problem;
- **A:** exact \(V\)-bulk/flux identities + missing independent finite entropy budget;
- **C:** low-complexity arithmetic separator.

This ranking is provisional until the boundary winding is attacked.

---

## 10. Status

- generic double-collision degree \(-1\): **subsumed**;
- all multiplicity local degree formula \(-\lfloor m/2\rfloor\): **PROVED**;
- local collision zero isolation for nontrivial analytic heat family: **PROVED**;
- same-sign/no-cancellation property for all interior collisions: **PROVED**;
- global boundary nonvanishing: **OPEN**;
- global boundary winding/degree: **OPEN — NEXT B TARGET**;
- renormalized/exhausted degree as \(X\to\infty\): **OPEN**;
- no-collision theorem: **OPEN**;
- RH: **OPEN**;
- novelty of the degree formula in the literature: **UNVERIFIED**.
