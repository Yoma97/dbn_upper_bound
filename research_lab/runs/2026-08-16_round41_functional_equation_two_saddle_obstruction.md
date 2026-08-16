# Round 41 — Functional-equation symmetry and the two-saddle obstruction to constant displacement

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / MODEL NO-GO / CORRECTION / NOVELTY UNVERIFIED.

## 0. Executive correction

Round 40 proved a valid one-parameter family of collision necessary conditions

\[
\mathcal R_{c,t}(\gamma)\ge2m
\]

for every real constant `c`. It was tempting to choose `c` near the large positive Archimedean horizontal slope and thereby remove the high-height background.

That expectation is incomplete for the Riemann function because the functional equation creates **two symmetric horizontal saddles**. A constant gauge can cancel the slope of one lobe only by penalizing it in the transformed weight and favoring the opposite lobe, whose slope has the opposite sign.

This round proves:

1. for the actual `xi`,
   \[
   \boxed{\mathcal R_{c,t}(\gamma)=\mathcal R_{-c,t}(\gamma)};
   \]
2. in the exact symmetric two-exponential model `f(a)=cosh(u a)`, which captures the leading pair of Archimedean lobes, the global minimum over all real `c` occurs at `c=0`;
3. hence constant coherent displacement cannot be assumed to remove the high-height background. A successful renormalization must be **two-sided / two-saddle**, not a single constant exponential gauge.

Round 40 remains mathematically valid; its proposed high-height use is demoted.

---

## 1. Functional-equation reflection on a horizontal line

Put

\[
f_\gamma(a):=\xi\!\left(\frac12+a+i\gamma\right).
\]

The functional equation and conjugation symmetry give

\[
\xi(s)=\xi(1-s),
\qquad
\overline{\xi(s)}=\xi(\overline s).
\]

Therefore

\[
\boxed{f_\gamma(-a)=\overline{f_\gamma(a)}.}
\]

Differentiating with respect to `a`,

\[
\boxed{f_\gamma'(-a)=-\overline{f_\gamma'(a)}.}
\]

Consequently

\[
|f_\gamma(-a)|=|f_\gamma(a)|,
\qquad
|f_\gamma'(-a)|=|f_\gamma'(a)|.
\]

---

## 2. The shifted quotient is even in `c` — PROVED

Recall

\[
\mathcal R_{c,t}(\gamma)
=t\frac{N(c)}{D(c)},
\]

where

\[
D(c)=\int_{\mathbb R}G_t(a)e^{-ca}|f_\gamma(a)|^2\,da
\]

and

\[
N(c)=\int_{\mathbb R}G_t(a)e^{-ca}|f_\gamma'(a)-cf_\gamma(a)|^2\,da.
\]

Changing `a` to `-a` and using the reflection identities,

\[
D(c)=D(-c).
\]

For the numerator,

\[
\begin{aligned}
N(c)
&=\int G_t(a)e^{ca}
|-\overline{f_\gamma'(a)}-c\overline{f_\gamma(a)}|^2\,da\\
&=\int G_t(a)e^{ca}|f_\gamma'(a)+cf_\gamma(a)|^2\,da\\
&=N(-c).
\end{aligned}
\]

Thus

\[
\boxed{\mathcal R_{c,t}(\gamma)=\mathcal R_{-c,t}(\gamma).}
\]

In particular `c=0` is always a stationary point whenever differentiation in `c` is justified.

This symmetry was absent in the one-lobe heuristic used after Round 40 and must be kept in every future optimization.

---

## 3. Why two saddles are unavoidable

At large positive ordinate and positive horizontal displacement, the completed factor has leading modulus

\[
|P(1/2+a+i\gamma)|
\asymp
|P(1/2+i\gamma)|
\exp\!\left(
\frac a2\log\frac\gamma{2\pi}
\right)
\]

on bounded/moderate windows, up to lower-order Stirling variation.

By the functional equation the modulus on the negative side is the reflected copy. Thus the Gaussian horizontal mass has two symmetric leading lobes, schematically

\[
\exp(-a^2/t+2ua)
\quad\text{and}\quad
\exp(-a^2/t-2ua),
\qquad
u\sim\frac12\log\frac\gamma{2\pi}.
\]

The two peaks occur near `a=+t u` and `a=-t u`.

A single constant gauge `c` cannot cancel both slopes `+u` and `-u` simultaneously.

---

## 4. Exact symmetric two-exponential model

Consider

\[
f(a)=\cosh(ua),
\qquad u>0,
\]

with the same Gaussian

\[
G_t(a)=\frac1{\sqrt{\pi t}}e^{-a^2/t}.
\]

This is the simplest exact model containing two reflected exponential lobes.

For the shifted quotient

\[
R_c^{\rm model}
:=t\frac{\int G_t(a)e^{-ca}|f'(a)-cf(a)|^2\,da}
{\int G_t(a)e^{-ca}|f(a)|^2\,da},
\]

the Gaussian moment identity

\[
\int G_t(a)e^{qa}\,da=e^{tq^2/4}
\]

gives, after elementary expansion,

\[
\boxed{
\frac{R_c^{\rm model}}t
=
\frac{
E\big((c^2+u^2)\cosh(tcu)+2cu\sinh(tcu)\big)
+(c^2-u^2)
}{1+E\cosh(tcu)},
}
\]

where

\[
E:=e^{tu^2}.
\]

At `c=0`,

\[
\boxed{
R_0^{\rm model}
=tu^2\frac{E-1}{E+1}
=tu^2\tanh\frac{tu^2}{2}.
}
\]

Thus for `tu^2 >> 1`, the unshifted background is asymptotic to `tu^2`.

---

## 5. Global minimizer in the two-saddle model — PROVED

Set

\[
T:=\frac{E-1}{E+1}=\tanh\frac{tu^2}{2}.
\]

Subtract the value at `c=0` from the normalized quotient. After bringing to a common positive denominator, the numerator of the difference is

\[
\boxed{
 c^2\big(E\cosh(tcu)+1\big)
+2Ecu\sinh(tcu)
+\frac{2Eu^2}{E+1}\big(\cosh(tcu)-1\big).
}
\]

Every term is nonnegative for real `c`, because

\[
c\sinh(tcu)\ge0,
\qquad
\cosh(tcu)-1\ge0.
\]

Hence

\[
\boxed{
R_c^{\rm model}\ge R_0^{\rm model}
\quad\text{for all }c\in\mathbb R,
}
\]

with equality only at `c=0` when `u>0`.

Therefore the constant coherent shift does **not** remove the two-saddle Archimedean background even in the ideal leading model; it increases the Rayleigh quotient.

---

## 6. Consequence for the collision program

The Round-40 theorem remains a correct family of necessary conditions. However:

\[
\boxed{
\text{constant }c\text{ is not a credible generic high-height baseline remover for }\xi.
}
\]

Any future use must be justified quantitatively for the actual `xi`, not by the one-lobe exponential heuristic.

The correct structural target is a **two-saddle renormalization** that removes opposite real slopes on the two reflected half-lines while preserving enough positivity and enough of the Hermite collision orthogonality to retain a spectral-gap theorem.

A schematic desired first-order operator is

\[
\partial_a-u_0\,\operatorname{sgn}(a),
\]

or a smooth odd replacement tied to the exact Archimedean slope

\[
u(a)=\Re\alpha(1/2+a+i\gamma).
\]

But multiplying by `exp(-u_0|a|)` breaks the global analytic coherent-state translation used in Round 40 and introduces a boundary/interface at `a=0`. It must therefore be derived from a new half-line/vector-valued Hermite formulation rather than assumed.

---

## 7. Circularity audit

The two-saddle obstruction uses only:

- the exact functional equation and conjugation symmetry of `xi`;
- elementary Gaussian integration;
- a model calculation.

It does not use RH, real-rootedness, zero gaps, or Laguerre positivity.

The model theorem is **not** claimed to be an asymptotic theorem for the full `xi` without additional error estimates. Its role is an adversarial test that refutes the heuristic assertion that a constant shift automatically removes the high-height background.

---

## 8. Round-42 target

Construct a rigorous half-line or two-component Hermite formulation adapted to

\[
f(-a)=\overline{f(a)}
\]

and investigate whether the collision moment conditions imply a spectral gap after an **odd/two-saddle gauge**. The construction must:

1. keep a positive Hilbert-space norm;
2. track the interface term at `a=0` exactly;
3. preserve enough of the first-`m` collision orthogonality;
4. avoid assuming the sign/interlacing of unknown zeros;
5. reduce to the ordinary Hermite criterion when the odd gauge is zero.

If the interface term destroys coercivity or merely reproduces `L_1`, record the failure and freeze the Rayleigh route.

---

## 9. Status

- functional-equation reflection: **PROVED**;
- `R_c=R_{-c}` for actual `xi`: **PROVED**;
- constant shift removes both high-height lobes: **REFUTED in exact two-saddle model**;
- two-exponential model has global minimizer `c=0`: **PROVED**;
- constant-shift Round-40 theorem: **VALID but DEMOTED as high-height mechanism**;
- two-saddle/half-line renormalized spectral gap: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
