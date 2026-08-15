# Round 28 — Differential kernel coupling collapses to the Laguerre barrier

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / STRUCTURAL BARRIER / SOURCE-GROUNDED / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 27 isolated the differential coupling

\[
\frac{w_t'(u)}{w_t(u)}
=\frac1u+u(2t-q(u)),
\qquad
w_t(u)=u e^{tu^2}\Phi(u),
\qquad
q(u)=-\frac{\Phi'(u)}{u\Phi(u)},
\]

as the smallest apparently unexploited Riemann-kernel structure on the collision side.

This round attacks that coupling directly.

The result is a barrier, but a useful one:

1. the **first-order** differential use of the coupling gives exactly the already-known identity
   \[
   S_1=xH_t+2tS_0,
   \]
   so it creates no new transversality invariant;
2. the natural **second-order** collision determinant is precisely
   \[
   L_1(H_t)=(H_t')^2-H_tH_t'',
   \]
   the first Laguerre expression;
3. the heat-weighted Riemann kernel is itself strictly decreasing and strictly log-concave for `0<=t<=1/2`, so Csordas' associated-kernel theorem applies and makes the canonical kernels `K_{n,t}` admissible;
4. however, admissibility is not positive definiteness. Csordas identifies positive definiteness of `K_1` / nonnegativity of `L_1` as the genuinely difficult step, and for the Riemann transform even the basic `L_1>=0` problem is explicitly open;
5. the exact PDE
   \[
   (\partial_t+\partial_x^2)L_1(H_t)=2L_1(H_t')
   \]
   does not permit a downward-in-`t` maximum-principle propagation from the known real-rooted regime. Reversing time produces a negative forcing term.

Thus the differential coupling does **not** currently furnish the missing entropy/resultant lower bound. It lands on a known Laguerre/positive-definiteness barrier.

The correct next move is not to relabel `L_1>0` as a new proof target. It is to add structure beyond the first associated kernel: theta identities, a genuinely finite sign-regular relation, arithmetic input, or a cross-frontier bridge.

---

## 1. Setup

Put

\[
\psi_t(u):=e^{tu^2}\Phi(u),
\qquad
w_t(u):=u\psi_t(u),
\]

and

\[
q(u):=-\frac{\Phi'(u)}{u\Phi(u)}.
\]

Rounds 13--15 established, using the Riemann theta-kernel concavity recorded by Csordas, that

\[
q'(u)>0,
\qquad
q(u)>1
\quad (u>0),
\]

in fact with a much stronger crude lower bound at the origin.

The logarithmic derivative identities are

\[
\frac{\psi_t'(u)}{\psi_t(u)}
=u(2t-q(u))
\]

and

\[
\boxed{
\frac{w_t'(u)}{w_t(u)}
=\frac1u+u(2t-q(u)).
}
\]

For the Riemann heat family,

\[
H_t(x)=\int_0^\infty\psi_t(u)\cos(xu)\,du.
\]

Define

\[
S_0(t,x):=\int_0^\infty w_t(u)\sin(xu)\,du=-H_t'(x),
\]

\[
S_1(t,x):=\int_0^\infty q(u)w_t(u)\sin(xu)\,du.
\]

A collision is a point `x>0,t>0` at which `H_t=H_t'=0`.

---

## 2. First-order coupling gives no new invariant — PROVED

Since

\[
\psi_t'(u)
=u(2t-q(u))\psi_t(u),
\]

we have

\[
q(u)w_t(u)
=2t\,w_t(u)-\psi_t'(u).
\]

Therefore

\[
S_1
=2tS_0-
\int_0^\infty\psi_t'(u)\sin(xu)\,du.
\]

The boundary terms vanish because `Phi` and its derivatives are super-exponentially decaying and `sin(0)=0`. Integration by parts gives

\[
-\int_0^\infty\psi_t'(u)\sin(xu)\,du
=x\int_0^\infty\psi_t(u)\cos(xu)\,du
=xH_t(x).
\]

Hence exactly

\[
\boxed{
S_1(t,x)=xH_t(x)+2tS_0(t,x).
}
\]

Since `S_0=-H_t'`, this is exactly the Round-13 identity

\[
S_1=xH_t-2tH_t'.
\]

Thus the first differential use of `q` contains no extra information beyond `(H,H')` itself.

At a critical point `H_t'=0`,

\[
S_1=xH_t.
\]

At a collision, both `S_0` and `S_1` vanish tautologically.

---

## 3. The natural second-order determinant is exactly `L_1` — PROVED

The simplest scalar expression that vanishes at a common zero of `H_t,H_t'` but is positive at every simple real zero is

\[
\boxed{
L_1(t,x):=(H_t'(x))^2-H_t(x)H_t''(x).
}
\]

At a simple real zero `x_j`,

\[
L_1(t,x_j)=H_t'(x_j)^2>0.
\]

At a multiple real zero,

\[
H_t=H_t'=0
\quad\Longrightarrow\quad
L_1=0.
\]

Therefore a global theorem

\[
L_1(t,x)>0
\qquad(t>0,\ x\in\mathbb R)
\]

would exclude every positive-time collision.

But this target is stronger than merely saying that no collision occurs, because it constrains points away from zeros as well.

After the positive-threshold finite-collision reduction of Round 13, a proof of strict `L_1>0` for every positive time would imply `Lambda<=0`; hence it must be treated as an endpoint-strength target unless its positivity is obtained from an independent mechanism.

---

## 4. Exact associated-kernel representation — SOURCE-GROUNDED

For a real even admissible kernel `phi`, Csordas defines

\[
K_1(r)
:=\int_{\mathbb R}
\phi(s+r)\phi(s-r)s^2\,ds
\]

and proves the identity

\[
\boxed{
L_1(F)(x)
=4\int_{\mathbb R}K_1(r)\cos(2xr)\,dr,
}
\]

for the corresponding Fourier/cosine transform `F` under his normalization.

More generally, the generalized Laguerre expressions are Fourier transforms of associated kernels `K_n`, and membership in the Laguerre--Polya class is equivalent to positive definiteness of all of these associated kernels.

For the heat-weighted Riemann kernel

\[
\phi=\psi_t=e^{tu^2}\Phi(u),
\]

define

\[
K_{1,t}(r)
:=\int_{\mathbb R}
\psi_t(s+r)\psi_t(s-r)s^2\,ds.
\]

Then

\[
\boxed{
K_{1,t}(r)
=e^{2tr^2}
\int_{\mathbb R}
e^{2ts^2}\Phi(s+r)\Phi(s-r)s^2\,ds.
}
\]

The integrand is positive, so `K_{1,t}(r)>0` pointwise. This is **not** enough to make `K_{1,t}` positive definite, and therefore not enough to force `L_1>=0`.

This point must not be blurred: pointwise positivity of a kernel and positive definiteness of the kernel are different statements.

---

## 5. The heat-weighted Riemann kernel is strictly log-concave — PROVED

Round 15 established `q(u)>1` and `q'(u)>0` for `u>0` from the stronger Riemann theta-kernel concavity.

For

\[
\psi_t(u)=e^{tu^2}\Phi(u),
\]

we have

\[
(\log\psi_t)'(u)=u(2t-q(u)).
\]

If

\[
0\le t\le\frac12,
\]

then `2t<=1<q(u)`, so

\[
(\log\psi_t)'(u)<0
\qquad(u>0).
\]

Moreover

\[
(\log\psi_t)''(u)
=2t-q(u)-u q'(u)<0.
\]

Thus

\[
\boxed{
\psi_t\text{ is strictly decreasing and strictly log-concave on }(0,\infty),
\quad 0\le t\le1/2.
}
\]

It remains positive, even, smooth and super-exponentially decaying, so it is an admissible kernel in the Csordas sense.

Consequently Csordas' Theorem 3.5 applies: each associated kernel `K_{n,t}` is itself admissible.

This is a genuine strengthening of the bookkeeping in Rounds 13--15: the heat tilt preserves enough concavity on the whole positive interval relevant to a hypothetical `Lambda>0`.

---

## 6. Admissibility is exactly where the easy argument stops — SOURCE-GROUNDED BARRIER

Csordas' theory separates two levels:

1. strict log-concavity of an admissible kernel implies that the associated kernels `K_n` are themselves admissible;
2. positivity of the generalized Laguerre expressions requires **positive definiteness** of those associated kernels.

The second step is the hard one.

In particular, Csordas explicitly singles out the `n=1` case as difficult and formulates the characterization of log-concave admissible kernels for which `K_1` is positive definite as an open problem. For the Riemann theta kernel, even the basic inequality

\[
(H'(x))^2-H(x)H''(x)\ge0
\]

is explicitly posed as an open problem.

Therefore the implication

\[
\text{Riemann kernel concavity}
\Longrightarrow
L_1(H_t)\ge0
\]

cannot be inserted as a routine step. It is precisely a nontrivial missing theorem.

Round 27's admissible/log-concave collision counterexample independently shows why no theorem of this form can hold for all log-concave admissible kernels.

---

## 7. Exact heat evolution of `L_1` — PROVED

Let `F=F(t,x)` satisfy

\[
F_t=-F_{xx}.
\]

Define

\[
L_1(F):=F_x^2-FF_{xx}.
\]

Differentiate in time:

\[
\begin{aligned}
\partial_tL_1(F)
&=2F_xF_{xt}-F_tF_{xx}-F F_{xxt}\\
&=-2F_xF_{xxx}+F_{xx}^2+F F_{xxxx}.
\end{aligned}
\]

On the other hand,

\[
\partial_x^2L_1(F)
=F_{xx}^2-F F_{xxxx}.
\]

Adding gives the exact identity

\[
\boxed{
(\partial_t+\partial_x^2)L_1(F)
=2\bigl(F_{xx}^2-F_xF_{xxx}\bigr)
=2L_1(F_x).
}
\]

For `F=H_t`,

\[
\boxed{
(\partial_t+\partial_x^2)L_1(H_t)
=2L_1(H_t').
}
\]

This is the first member of a Laguerre-type hierarchy, but no unproved all-order hierarchy is invoked here.

---

## 8. Why the maximum principle does not propagate positivity downward — PROVED

Suppose one starts from a time `T>=1/2`, where de Bruijn gives real-rootedness, and wishes to propagate a Laguerre sign toward smaller `t`.

Introduce downward time

\[
s:=T-t,
\qquad
\mathcal L(s,x):=L_1(H_{T-s})(x).
\]

Then the identity of Section 7 becomes

\[
\boxed{
\partial_s\mathcal L
=\partial_x^2\mathcal L
-2L_1(H_{T-s}').
}
\]

Thus, even if one somehow knew

\[
L_1(H_{T-s}')\ge0,
\]

the source term in downward time is **nonpositive**.

The ordinary heat maximum principle therefore does not preserve a lower bound `\mathcal L>=0`; the forcing pushes in the wrong direction.

To compensate one would need a quantitative relation controlling

\[
L_1(H_t')
\]

by the diffusive part or by `L_1(H_t)` itself. Asking for positivity of `L_1(H_t')`, then of further derivatives, naturally drives the argument toward the generalized Laguerre hierarchy whose full positivity characterizes Laguerre--Polya membership.

This is exactly the circularity danger that the project must avoid.

---

## 9. Integrated positivity is also too weak — PROVED

Assume sufficient decay on the real axis for the formal integration by parts, or apply the identity on large finite intervals with controlled boundary terms. Then

\[
\int_{\mathbb R}L_1(F)(x)\,dx
=
\int F_x^2\,dx-
\int F F_{xx}\,dx
=2\int F_x^2\,dx\ge0.
\]

Thus the global integral of `L_1` is automatically nonnegative whenever these integrals make sense.

But a positive integral does not exclude isolated zeros or negative regions of `L_1`, and it remains finite through a collision. Hence this energy is collision-blind in the sense of Round 27.

The missing statement is necessarily **local/pointwise or quantitatively coercive**, not merely integrated positivity.

---

## 10. Relation to Round 26 resultant transversality

At a local simple root cluster, Round 26 showed that a finite entropy budget is a logarithmic lower bound on the local discriminant/resultant.

`L_1` supplies the rootwise identity

\[
L_1(t,x_j)=H_t'(x_j)^2.
\]

Thus a uniform lower bound on `L_1` at every real zero would be a rootwise transversality estimate.

But at a collision both sides vanish. Therefore proving such a bound is simply another form of the missing resultant theorem.

The differential-kernel coupling has not reduced this requirement; it has translated it into the associated-kernel/positive-definiteness language.

---

## 11. Adjudication of the local kernel route

The chain now reads

\[
\text{theta-kernel concavity}
\Longrightarrow
\psi_t\text{ admissible and log-concave}
\Longrightarrow
K_{n,t}\text{ admissible}
\]

but the needed next arrow is

\[
\boxed{
K_{1,t}\text{ admissible}
\stackrel{?}{\Longrightarrow}
\widehat K_{1,t}(2x)>0,
}
\]

which is false for generic admissible/log-concave kernels and open for the Riemann kernel in the relevant strength.

Hence the **purely local kernel-concavity subroute is frozen** unless one introduces an additional Riemann-specific identity beyond admissibility/log-concavity.

This is not a failure of Program A as a whole. It narrows its surviving content to one of the following:

1. a theta-functional identity that directly controls `K_{1,t}` or the local resultant;
2. a finite sign-regular/determinantal statement stronger than the TP2 data already refuted in Round 15;
3. an arithmetic/explicit-formula input;
4. a cross-frontier bridge from pair correlation, zero density, or another established zeta statistic to collision transversality.

---

## 12. Next step

The next round should no longer search for consequences of generic positivity/log-concavity.

The preferred target is:

> derive an **exact theta-series decomposition of the associated kernel `K_{1,t}` (or of a normalized rootwise transversality quantity)** and determine whether its Fourier transform admits a sign decomposition whose negative channel can be bounded independently.

This target is sharper than “prove `L_1>0`”: it asks for a structural representation with a separately controllable defect.

If the theta-series decomposition merely rewrites `L_1` without producing an independent sign, it should be rejected and the program should pivot to a cross-frontier bridge.

---

## 13. Status

- first-order differential coupling gives a new invariant: **REFUTED; it reduces exactly to the Round-13 identity**;
- strict decrease/log-concavity of `psi_t=e^{tu^2}Phi` for `0<=t<=1/2`: **PROVED**;
- associated kernels `K_{n,t}` admissible on this range: **PROVED using Csordas' theorem**;
- associated-kernel representation of `L_1`: **SOURCE-ESTABLISHED**;
- pointwise positivity/admissibility of `K_1` implies positive definiteness: **FALSE IN GENERAL / NOT AVAILABLE**;
- exact PDE `(d_t+d_x^2)L_1=2L_1(F_x)`: **PROVED**;
- downward maximum-principle propagation of `L_1>=0`: **BLOCKED by sign of the forcing**;
- independent strict `L_1>0` theorem for the Riemann heat family: **OPEN / ENDPOINT-STRENGTH**;
- pure local kernel-concavity route: **FROZEN unless new theta-specific structure is added**;
- RH: **OPEN**;
- novelty of the packaging: **UNVERIFIED**.
