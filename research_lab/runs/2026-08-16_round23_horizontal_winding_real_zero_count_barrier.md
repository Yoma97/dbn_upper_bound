# Round 23 — Horizontal winding equals real-zero count: a structural barrier for Program B

**Date:** 2026-08-16

**Status labels:** PROVED / CONDITIONAL / REFUTED-AS-INDEPENDENT-MECHANISM / NOVELTY UNVERIFIED.

**RH status:** OPEN.

## 0. Executive verdict

Program B had been upgraded after the local all-multiplicity degree theorem

\[
\deg_{\rm loc}(F,F_x)=-\lfloor m/2\rfloor.
\]

This round shows that the proposed next step — computing the global boundary winding of

\[
W(t,x)=F(t,x)+iF_x(t,x)
\]

— is not automatically an independent topological budget. On a collision-free time slice, the horizontal winding of `W` is determined exactly by the number of real zeros of `F` on that slice, up to endpoint arctangent terms. On a rectangle with no real-zero crossings through the spatial sides, the Brouwer degree is exactly one half of the change in the real-zero count.

Thus a proof that the boundary degree is zero is, in this setting, equivalent to proving that the number of real zeros does not change. For the de Bruijn--Newman flow this is essentially the same transition that collisions mediate.

Therefore Program B is **not an independent global mechanism unless one finds genuinely new boundary information that determines a renormalized winding without already controlling the real-zero census.**

---

## 1. One-dimensional winding identity

Let `F:[a,b]->R` be C^1. Assume:

1. every zero of F in `(a,b)` is simple;
2. `F(a)F(b) != 0`;
3. `W(x):=F(x)+iF'(x)` is nonzero on `[a,b]`.

Let

\[
q(x)=\frac{F'(x)}{F(x)}
\]

where defined, and let `N_F(a,b)` denote the number of real zeros of F in `(a,b)`.

Then for any continuous lift of the argument of W,

\[
\boxed{
\Delta_{a}^{b}\arg W
=
\arctan q(b)-\arctan q(a)-\pi N_F(a,b).
}
\]

### Proof

On a zero-free interval,

\[
W=F(1+iq),
\]

and `arg(1+iq)=arctan q` with values in `(-pi/2,pi/2)`.

At a simple zero `r`,

\[
F(x)=c(x-r)+O((x-r)^2),\qquad F'(x)=c+O(x-r),\qquad c\ne0,
\]

so W remains nonzero and its argument extends continuously across r. The continuous lift loses exactly `pi` at each simple zero relative to the principal `arctan q` branch. Summing over zero-free components gives the formula.

No Laguerre inequality and no sign assumption on

\[
\partial_x\arg W=-\frac{L_1(F)}{F^2+F'^2}
\]

is used.

---

## 2. Even-function specialization

If F is even and we take `[a,b]=[-X,X]`, then

\[
q(-X)=-q(X).
\]

Therefore, provided `F(\pm X) != 0`,

\[
\boxed{
\Theta_F(X):=\Delta_{-X}^{X}\arg(F+iF')
=2\arctan\frac{F'(X)}{F(X)}-\pi N_F(-X,X).
}
\]

Thus horizontal winding is already a real-zero counting observable plus a bounded endpoint phase.

---

## 3. Rectangle degree identity

Let `F(t,x)` be real analytic on a neighborhood of

\[
D=[t_-,t_+]\times[-X,X]
\]

and define

\[
\Gamma(t,x)=(F(t,x),F_x(t,x)),\qquad W=F+iF_x.
\]

Assume:

1. `W != 0` on `\partial D`;
2. the time slices `t=t_-` and `t=t_+` contain only simple real zeros in `(-X,X)`;
3. `F(t,\pm X) != 0` for all `t in [t_-,t_+]`.

Then, with the standard orientation in `(t,x)` coordinates,

\[
\boxed{
\deg(\Gamma,D,0)
=-\frac12\left(N_{t_+}(-X,X)-N_{t_-}(-X,X)\right).
}
\]

### Proof sketch

Apply the one-dimensional identity to the two `x`-faces. The endpoint arctangent variations cancel against the two time-face argument variations because `F(t,\pm X)` never vanishes and even symmetry gives

\[
W(t,-X)=\overline{W(t,X)}.
\]

The remaining boundary argument change is `-pi` times the change in the real-zero count. Division by `2pi` gives the formula.

The sign is checked by the exact heat polynomial

\[
P_t(x)=x^2-2t.
\]

Across a rectangle containing `t=0`, the real-zero count increases from 0 to 2 while the unique collision has local degree `-1`, agreeing with the formula.

---

## 4. Relation to the all-multiplicity local degree theorem

Round 19 gives for an isolated multiplicity-m collision

\[
\deg_{\rm loc}(F,F_x)=-\lfloor m/2\rfloor.
\]

Round 23 shows that globally, after summing all collisions in a rectangle without spatial zero crossings,

\[
-\sum_p\left\lfloor\frac{m_p}{2}\right\rfloor
=-\frac12\Delta N_{\mathbb R}.
\]

Thus the negative local charges are exactly the topological spectral flow by which nonreal conjugate pairs become real pairs under forward backward-heat time.

This is useful bookkeeping, but it does not create an independent conservation law.

---

## 5. Consequence for the Riemann de Bruijn--Newman family

For

\[
F=H_t,
\]

Polymath provides strong positive-time large-x asymptotics and zero-count control, and real/simple zeros hold for `t>Lambda`. These facts can help control spatial boundary faces.

However, the available positive-time counting statements are asymptotic rather than an exact equality of the real-zero counts on two time slices. An estimate of the form

\[
N_t(X)=g(X,t)+O(\log X)
\]

cannot determine the integer difference needed to prove degree zero.

Likewise, the Polymath discussion of high-x zero velocity

\[
\dot x=-\pi/4+O(x^{-ct})
\]

is stated as derivable with details left to the reader; even if made fully effective, it controls transport through spatial faces, not the unknown real-zero census on the lower time face.

Therefore the implication

\[
\text{Polymath high-x asymptotics} \Rightarrow \deg=0
\]

has a missing middle theorem: one must control the lower horizontal-face winding, which by Section 1 is equivalent to controlling its real-zero count.

---

## 6. Circularity audit

The following would be circular or near-circular as a proof of `Lambda<=0`:

- proving horizontal winding by assuming `L_1>=0` globally;
- proving equality of real-zero counts by assuming no pair leaves or enters the real axis;
- importing Rodgers--Tao negative-time local-equilibrium estimates proved under the contradiction hypothesis `Lambda<0`;
- assuming a lower gap bound that prevents collision.

Safe inputs remain:

- exact heat PDE identities;
- local Hermite collision normal forms;
- unconditional positive-time Polymath asymptotics in their stated ranges;
- argument-principle identities that do not assume unproved zero-free half-planes.

---

## 7. Program ranking after this barrier

The local degree theorem alone does not justify

\[
B\gtrsim A\gg C.
\]

The current ranking is

\[
\boxed{A\gtrsim B\gg C.}
\]

### A — PRIMARY

Exact relative V-energy / Bregman / cutoff-commutator identities, with one unresolved non-circular target: an independent one-sided finite entropy/coercive budget, or a proof that no such budget can exist in the natural class.

### B — CONDITIONAL SECONDARY

All-multiplicity collision degree is retained as a diagnostic and bookkeeping theorem. It regains primary status only if one finds boundary data weaker than real-rootedness that determines a renormalized winding.

### C — TERTIARY

Low-complexity arithmetic separator.

---

## 8. Smallest next lemma

Do not attempt a full global winding computation yet.

The next B-side test is:

> Find a boundary observable `Q_t(X)` computable from the Polymath normalized asymptotic model such that the difference of horizontal winding and `Q_t(X)` has a limit as `X->infinity`, and prove that this renormalized remainder is not merely `-1/2` times the unknown defect in the real-zero count.

If every natural renormalization reduces to real-zero count defect, Program B is structurally equivalent and should remain secondary.

On the A side, the next target remains the one-sided entropy-budget/impossibility dichotomy.

---

## 9. Status

- one-dimensional horizontal winding identity: **PROVED**;
- rectangle degree / real-zero-count identity: **PROVED under no spatial zero crossing**;
- all-multiplicity local degree: **RETAINED**;
- global degree as independent no-collision mechanism: **REFUTED IN THE FINITE-RECTANGLE FORM**;
- Polymath high-x asymptotics sufficient for exact global degree zero: **NOT ESTABLISHED**;
- renormalized winding remainder independent of real-zero census: **OPEN**;
- Program A entropy budget: **OPEN**;
- RH: **OPEN**;
- novelty of the winding-count packaging: **NOVELTY UNVERIFIED**.
