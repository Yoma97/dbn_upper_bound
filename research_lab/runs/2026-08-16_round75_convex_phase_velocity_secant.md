# Round 75 — Convex-secant compression of the APVC derivative tail

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Strengthens Round 74 without phase tracking by replacing the coordinatewise triangle bound on each derivative velocity by the exact secant majorant of a convex norm.

---

## 1. The derivative-tail function

Use Round 74 notation

\[
\Phi=|\phi_x|>0,
\qquad
T=-\tau_x>0,
\qquad
s=\sigma_x\ge0.
\]

For

\[
\ell=\log n,
\]

the absolute derivative velocity of the `n`th normalized term is

\[
\omega(\ell)
:=
\sqrt{(s\ell)^2+(\Phi-T\ell)^2}.
\tag{75.1}
\]

The APVC loss is

\[
B_1=\sum_{n=2}^Na_n\omega(\log n).
\tag{75.2}
\]

---

## 2. Convexity

Write

\[
v(\ell)=(s\ell,\Phi-T\ell)\in\mathbb R^2.
\]

Then `v` is affine and

\[
\omega(\ell)=\|v(\ell)\|_2.
\]

Because a norm is convex and the composition of a convex norm with an affine map is convex,

\[
\boxed{\omega\text{ is convex on }[0,\infty).}
\tag{75.3}
\]

Equivalently, direct differentiation gives

\[
\omega''(\ell)
=
\frac{s^2\Phi^2}{\omega(\ell)^3}\ge0
\]

whenever `omega>0`, with convexity extending through a possible zero by continuity.

---

## 3. Exact pointwise secant majorant

Put

\[
L_N=\log N,
\qquad
\Omega_N=\omega(L_N).
\]

For `0<=ell<=L_N`, convexity gives

\[
\omega(\ell)
\le
\left(1-\frac\ell{L_N}\right)\omega(0)
+
\frac\ell{L_N}\omega(L_N).
\]

Since `omega(0)=Phi`,

\[
\boxed{
\omega(\ell)
\le
\Phi+m_N\ell,
\qquad
m_N:=\frac{\Omega_N-\Phi}{L_N}.
}
\tag{75.4}
\]

Multiplying by `a_n>0` and summing yields

\[
\boxed{
B_1\le\Phi A_0+m_NA_1.
}
\tag{75.5}
\]

This is exact at both endpoints of the logarithmic interval and is never weaker than replacing the Euclidean norm by the coordinatewise `l1` norm followed by a single affine bound.

---

## 4. Secant APVC

At a hypothetical true collision define, as in Round 74,

\[
U=A_0+E_0/2.
\]

If `U<1`, the value equation gives

\[
|\sin\phi|\ge\sqrt{1-U^2}.
\]

Combining this with (75.5), a sufficient collision-exclusion condition is

\[
\boxed{
2\left[
\Phi\sqrt{1-(A_0+E_0/2)^2}
-\Phi A_0-m_NA_1
\right]>E_1.
}
\tag{75.6}
\]

Note the sign convention: in the shoulder region `Omega_N<Phi`, so typically `m_N<0`; therefore the term `-m_N A1` is favorable.

---

## 5. Box-safe common secant

For proof tiling we do not know one exact triple `(Phi,T,s)` or one exact `L_N`; we have enclosures

\[
\Phi\in[\Phi_L,\Phi_U],
\quad
T\in[T_L,T_U],
\quad
0\le s\le s_U,
\quad
0\le\log N\le L_U.
\]

For any admissible parameters define

\[
f(\ell)=\sqrt{(s\ell)^2+(\Phi-T\ell)^2}
\quad(0\le\ell\le L_U).
\]

We have

\[
f(0)=\Phi\le\Phi_U.
\tag{75.7}
\]

Also

\[
|\Phi-TL_U|
\le
D_U,
\]

where

\[
\boxed{
D_U:=
\max\left\{
|\Phi_L-T_UL_U|,
|\Phi_U-T_LL_U|
\right\}.
}
\tag{75.8}
\]

Hence

\[
f(L_U)
\le
\Omega_U
:=
\sqrt{(s_UL_U)^2+D_U^2}.
\tag{75.9}
\]

Convexity then gives the **common box majorant**

\[
\boxed{
f(\ell)\le\Phi_U+m_U\ell,}
\tag{75.10}
\]

with

\[
\boxed{
m_U:=\frac{\Omega_U-\Phi_U}{L_U}.}
\tag{75.11}
\]

for every actual term in the box.

Therefore

\[
B_1
\le
\Phi_UA_0+m_UA_1.
\tag{75.12}
\]

To make this interval-safe:

- if `m_U>=0`, use an upper enclosure `A1_U`;
- if `m_U<0`, use a lower enclosure `A1_L`.

Thus

\[
\boxed{
B_{1,U}^{\rm sec}
=
\Phi_UA_{0,U}
+
\begin{cases}
 m_UA_{1,U},&m_U\ge0,\\
 m_UA_{1,L},&m_U<0.
\end{cases}
}
\tag{75.13}
\]

is a rigorous box upper bound.

The corresponding box certificate is

\[
\boxed{
2\left[
\Phi_L\sqrt{1-(A_{0,U}+E_{0,U}/2)^2}
-B_{1,U}^{\rm sec}
\right]>E_{1,U}.
}
\tag{75.14}
\]

---

## 6. Comparison with the Round-74 soft defect

Round 74 addendum uses

\[
\sqrt{(s\ell)^2+(\Phi-T\ell)^2}
\le
s\ell+|\Phi-T\ell|,
\]

then a soft endpoint defect. Round 75 instead applies convexity to the Euclidean norm **before** replacing any coordinate.

Pointwise, the secant estimate is often nearly exact in the current finite-time corner because:

- `s=sigma_x` is tiny at large `x`;
- `Phi` is close to `T log N` at the moving cutoff;
- the velocity curve therefore runs almost linearly from `Phi` at `ell=0` toward a very small endpoint value.

No oscillatory cancellation is assumed: this remains a positive-weight majorant.

---

## 7. Diagnostic only

Non-interval evaluation at `t=1/2` shows the secant APVC margin is numerically almost indistinguishable from the exact positive sum `B1` throughout the present `lambda≈6.8--7.0` corner. The pointwise sign boundary remains near `lambda≈6.8188`.

Thus Round 75 is expected mainly to reduce **interval/majorant loss** when certifying near that boundary; it does not create a new pointwise mechanism below the APVC floor.

This diagnostic is not part of any proof threshold.

---

## 8. Circularity audit

Inputs:

- Round-74 exact derivative decomposition;
- positivity of `a_n`;
- convexity of the Euclidean norm under affine parametrization;
- interval endpoint enclosures.

Not used:

- RH;
- `Lambda<=0`;
- real-rootedness;
- zero-spacing assumptions;
- phase cancellation;
- pair correlation/GUE;
- Laguerre--Polya membership.

No desired conclusion is assumed.

---

## 9. Execution rule

Do **not** replace a successful simpler APVC certificate by Round 75 merely for elegance. The hierarchy is:

1. old PSC;
2. Round-74 soft APVC;
3. Round-75 secant APVC only for residual boxes.

This keeps the certified proof tree simple while reserving the sharper bound for the actual frontier.
