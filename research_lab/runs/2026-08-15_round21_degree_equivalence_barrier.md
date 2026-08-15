# Round 21 — Degree route audit: local theorem validated, global tautology barrier exposed

**Date:** 2026-08-15

**RH status:** OPEN.

**Status labels:** PROVED / CONDITIONAL / CANDIDATE / REFUTED / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 19's local formula

\[
\deg_{\rm loc}(F,F_x)=-\left\lfloor\frac m2\right\rfloor
\]

survives independent rederivation. However, in the finite polynomial heat model this integer is **exactly the change in the number of nonreal conjugate root pairs across the collision**.

Therefore the global Brouwer-degree route is not automatically an independent no-collision mechanism. In finite dimension it is a topological encoding of real-rootedness defect.

The correct status is:

\[
\boxed{
\text{local collision degree: genuine theorem};\qquad
\text{global degree zero: potentially a disguised real-rootedness assertion}.
}
\]

Program B remains useful only if the boundary winding can be computed from an independently provable Riemann-specific estimate that is genuinely weaker than the desired no-collision conclusion.

---

## 1. Independent validation of the local degree formula — PROVED

Translate the collision to \((0,0)\) and assume exact multiplicity \(m\ge2\):

\[
F(0,x)=a x^m+O(x^{m+1}),\qquad a\ne0.
\]

The parabolic blow-up is

\[
P_m(T,X)=e^{-T\partial_X^2}X^m.
\]

Under

\[
t=r^2T,\qquad x=rX,
\]

and the positive-determinant output rescaling

\[
G_r(T,X)=
\left(
\frac{F(r^2T,rX)}{ar^m},
\frac{F_x(r^2T,rX)}{ar^{m-1}}
\right),
\]

one has \(C^1_{\rm loc}\) convergence

\[
G_r\to(P_m,\partial_XP_m).
\]

For \(T>0\),

\[
P_m(T,X)=T^{m/2}H_m(X/(2\sqrt T)),
\]

and all \(m\) roots are real simple. For \(T<0\), there are no real roots when \(m\) is even, and exactly the root \(X=0\) when \(m\) is odd.

Using the small regular value \((0,\varepsilon)\), the positive-time root branches with positive derivative each contribute \(-1\), and there are \(\lceil m/2\rceil\) such branches. For odd \(m\), the unique negative-time real branch contributes \(+1\). Hence

\[
\boxed{
\deg_{\rm loc}(F,F_x)
=-\left\lfloor\frac m2\right\rfloor.
}
\]

This validates the Round-19 sign and multiplicity factor.

---

## 2. Stronger isolation proof — PROVED

Round 19 argued that an accumulating common-zero set would force an analytic curve. A cleaner proof follows directly from the parabolic model and avoids any real-analytic-set classification.

Assume, for contradiction, there are common zeros

\[
(t_n,x_n)\ne(0,0),
\qquad
(t_n,x_n)\to(0,0).
\]

Set

\[
r_n:=\max\{|x_n|,\sqrt{|t_n|}\}>0,
\]

and

\[
T_n=t_n/r_n^2,
\qquad
X_n=x_n/r_n.
\]

Then \((T_n,X_n)\) lies on the compact parabolic unit shell

\[
\max\{|X|,\sqrt{|T|}\}=1.
\]

Pass to a subsequence

\[
(T_n,X_n)\to(T_*,X_*),
\]

where \((T_*,X_*)\ne(0,0)\). Since

\[
G_{r_n}(T_n,X_n)=0
\]

and \(G_{r_n}\to(P_m,P_{m,X})\) uniformly on compact sets,

\[
P_m(T_*,X_*)=P_{m,X}(T_*,X_*)=0.
\]

But the Hermite model has no common real zero except \((0,0)\). Contradiction.

Thus every finite-multiplicity collision of a nontrivial analytic backward-heat family is locally isolated.

---

## 3. Finite polynomial pair-count theorem — PROVED

Let

\[
P_t(z)=e^{-t\partial_z^2}P_0(z)
\]

be a real polynomial heat family of fixed degree \(N\). Consider an isolated multiplicity-\(m\) collision at \(t=t_c\), and choose a sufficiently small spatial neighborhood containing no other roots.

For \(\tau=t-t_c>0\), the local Hermite model has \(m\) real roots.

For \(\tau<0\):

- if \(m=2n\) is even, there are no local real roots; hence there are \(n\) nonreal conjugate pairs;
- if \(m=2n+1\) is odd, there is one local real root and \(n\) nonreal conjugate pairs.

Therefore the number \(C(t)\) of local nonreal conjugate pairs changes by

\[
\boxed{
C(t_c+)-C(t_c-)
=-\left\lfloor\frac m2\right\rfloor.
}
\]

Comparing with Round 19,

\[
\boxed{
\deg_{\rm loc}(P_t,P_t')
=C(t_c+)-C(t_c-).
}
\]

Thus the local Brouwer charge is exactly the local loss of nonreal conjugate pairs under forward heat time.

---

## 4. Global finite-dimensional identity — PROVED under generic boundary avoidance

Choose times \(t_-<t_+\) containing finitely many collision times and assume neither endpoint contains a multiple real root. Since the polynomial degree is fixed, let

\[
C(t)=\frac{N-R(t)}2,
\]

where \(R(t)\) is the number of real roots counted with multiplicity at a regular time.

Summing the local collision formula gives

\[
\boxed{
\sum_{p:\,t_-<t_p<t_+}
\deg_{\rm loc}(P,P_x;p)
=C(t_+)-C(t_-).
}
\]

Equivalently,

\[
\boxed{
-\sum_p\left\lfloor\frac{m_p}{2}\right\rfloor
=C(t_+)-C(t_-).
}
\]

Thus, if \(P_{t_+}\) is real-rooted, the total negative collision degree between \(t_-\) and \(t_+\) is exactly minus the number of nonreal conjugate pairs present at \(t_-\).

This is not merely analogous to real-rootedness; in the finite heat model it is an exact reformulation of the pair-count defect.

---

## 5. Consequence for Program B

The proposed global implication

\[
\deg(\Gamma,D,0)=0
\Longrightarrow
\text{no collision in }D
\]

is correct because every local degree is negative. But the finite polynomial theorem shows why this does not by itself create a new proof mechanism.

Computing the boundary degree as zero can be as hard as proving that the lower-time configuration contains no nonreal conjugate pairs.

Hence the boundary theorem must be classified as **independent progress only if** its proof uses information not already equivalent to real-rootedness/LP membership.

Examples of unacceptable hidden inputs include:

- a Hermite--Biehler stability statement already equivalent to real-rootedness;
- global \(L_1\ge0\) or all-order Laguerre positivity at the unknown time;
- a boundary phase monotonicity whose proof assumes the absence of nonreal zeros;
- a zero-free half-plane statement for \(H+iH'\) equivalent to the desired real-rootedness.

---

## 6. Relation to \(H+iH'\) and Hermite--Biehler danger

On the real boundary define

\[
G_t(x)=H_t(x)+iH_t'(x).
\]

Its phase derivative is

\[
\partial_x\arg G_t
=rac{H_tH_t''-(H_t')^2}{H_t^2+(H_t')^2}
=-\frac{L_1(H_t)}{H_t^2+(H_t')^2}.
\]

Thus any attempt to compute the horizontal winding by proving monotone phase through \(L_1\ge0\) returns directly to a Laguerre/Hermite--Biehler real-rootedness criterion.

This is a **circularity warning**, not a proof that every possible boundary estimate is circular.

---

## 7. Normalization fact — PROVED

If \(a(t,x)\in\mathbb C\setminus\{0\}\) is continuous and nowhere zero on a bounded domain \(D\), replacing the collision field

\[
G=H+iH'
\]

by

\[
\widetilde G=aG
\]

does not change the Brouwer degree on \(D\). Indeed, multiplication by \(a\) is an orientation-preserving real-linear map pointwise with determinant \(|a|^2>0\), and the boundary winding contributed by \(a\) is zero because \(a\) extends nonvanishingly through \(D\).

Therefore a Polymath-style nowhere-zero normalizer may simplify amplitude estimates for the **field \(G\) itself** without changing its degree.

Caution: normalizing \(H\) first and then forming \(\widetilde H+i\widetilde H'\) is a different operation because differentiation introduces the derivative of the normalizer.

---

## 8. Updated route ranking

The local degree theorem remains valuable as a precise collision-counting invariant. But after the finite polynomial audit it should not outrank Program A merely because all local charges have the same sign.

The updated ranking is

\[
\boxed{A\gtrsim B\gg C.}
\]

### A — PRIMARY STRUCTURAL

Exact relative \(V\)-energy / Bregman / flux identities, now supplemented by the Round-20 reference-force asymptotic. Missing: an independent finite entropy/coercive budget.

### B — SECONDARY BUT LIVE

All-multiplicity negative degree. Missing: a boundary winding theorem whose proof is demonstrably weaker than real-rootedness.

### C — TERTIARY

Low-complexity arithmetic separator.

---

## 9. Status

- Round-19 local degree \(-\lfloor m/2\rfloor\): **VALIDATED / PROVED**;
- collision isolation: **PROVED by blow-up, strengthened**;
- local degree = change in nonreal conjugate-pair count for heat polynomials: **PROVED**;
- global finite polynomial degree = pair-count defect change: **PROVED**;
- “same-sign local charges automatically make B easier than RH”: **REFUTED**;
- independent Riemann boundary-winding theorem: **OPEN**;
- Program B circularity risk: **HIGH** unless an independent boundary mechanism is found;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
