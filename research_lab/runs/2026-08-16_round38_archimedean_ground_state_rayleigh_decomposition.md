# Round 38 — Archimedean ground-state decomposition of the horizontal collision Rayleigh quotient

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED IDENTITY / NORMALIZED CROSS-FRONTIER BRIDGE / SOURCE-GROUNDED / NOVELTY UNVERIFIED.

## 0. Executive theorem

Rounds 35--36 reduced a multiplicity-`m` heat collision at `x=2 gamma` to the necessary condition

\[
\mathcal R_{1,t}(\gamma)
:=t\frac{\int G_t(a)|\xi'(1/2+a+i\gamma)|^2da}
{\int G_t(a)|\xi(1/2+a+i\gamma)|^2da}
\ge2m.
\]

A direct estimate through `xi'/xi` is badly behaved near zeros. Polymath provides a nowhere-vanishing Stirling normalizer `M_0(s)` with logarithmic derivative

\[
\alpha(s):=\frac{M_0'(s)}{M_0(s)}
=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}.
\]

This round factors out the **modulus** of `M_0` and obtains an exact weighted Schrödinger/ground-state decomposition.

Let

\[
s(a)=\frac12+a+i\gamma,
\qquad
\rho(a):=|M_0(s(a))|>0,
\]

\[
u(a):=\frac{d}{da}\log\rho(a)=\Re\alpha(s(a)),
\]

and define the phase-normalized residual

\[
Y(a):=\frac{\xi(s(a))}{\rho(a)}.
\]

Set

\[
w_t(a):=G_t(a)\rho(a)^2.
\]

Then exactly

\[
\boxed{
\int G_t(a)|\xi'(s(a))|^2da
=
\int w_t(a)|Y'(a)|^2da
+
\int w_t(a)V_t(a)|Y(a)|^2da,
}
\]

where the explicit real potential is

\[
\boxed{
V_t(a)
=-u'(a)+\frac{2a}{t}u(a)-u(a)^2.
}
\]

Also

\[
\int G_t|\xi|^2=
\int w_t|Y|^2.
\]

Therefore

\[
\boxed{
\frac{\mathcal R_{1,t}(\gamma)}t
=
\frac{\int w_t|Y'|^2}{\int w_t|Y|^2}
+
\frac{\int w_tV_t|Y|^2}{\int w_t|Y|^2}.
}
\]

The singular pointwise zeta logarithmic derivative has disappeared. The collision observable is the sum of a nonnegative kinetic energy of a normalized residual and an explicit archimedean potential average.

At large ordinate,

\[
u(a)=\frac12\log\frac\gamma{2\pi}+O\!\left(\frac{1+|a|}{\gamma^2}\right)
\]

on bounded horizontal windows, so the weight `w_t` is a Gaussian shifted to leading order by

\[
\boxed{
a_*\sim t u\sim\frac t2\log\frac\gamma{2\pi}.}
\]

This is exactly the saddle-point scale underlying the familiar positive-time parameter `lambda=t log x`.

---

## 1. Source normalizer

Polymath introduces the nowhere-zero Stirling model

\[
M_0(s)
=\frac18\frac{s(s-1)}2\pi^{-s/2}\sqrt{2\pi}
\exp\!\left(
\left(\frac s2-\frac12\right)\Log\frac s2-\frac s2
\right)
\]

on `C\(-infinity,1]`, with a holomorphic logarithm and logarithmic derivative

\[
\boxed{
\alpha(s)
=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}.
}
\]

The precise multiplicative constants in `M_0` are irrelevant below; only nonvanishing and the logarithmic derivative matter.

For `gamma>0`, the horizontal line `s=1/2+a+i gamma` does not intersect the branch cut.

---

## 2. Remove the archimedean phase

Write

\[
M_0(s(a))=\rho(a)e^{i\theta(a)},
\qquad \rho(a)>0.
\]

Define the holomorphically normalized function

\[
R(a):=\frac{\xi(s(a))}{M_0(s(a))}.
\]

Then

\[
\xi'(s(a))
=M_0(s(a))\left(R'(a)+\alpha(s(a))R(a)\right).
\]

Now put

\[
Y(a):=e^{i\theta(a)}R(a)=\frac{\xi(s(a))}{\rho(a)}.
\]

Since

\[
\theta'(a)=\Im\alpha(s(a)),
\qquad
u(a):=\frac{\rho'}\rho=\Re\alpha(s(a)),
\]

we have

\[
R'+\alpha R
=e^{-i\theta}(Y'+uY).
\]

Therefore

\[
\boxed{
|\xi'|^2
=\rho^2|Y'+uY|^2,
\qquad
|\xi|^2=\rho^2|Y|^2.
}
\]

The large explicit archimedean phase is removed exactly, not asymptotically.

---

## 3. Weighted ground-state transform

Set

\[
w_t(a)=G_t(a)\rho(a)^2.
\]

Then

\[
\frac{w_t'}{w_t}
=-\frac{2a}{t}+2u(a).
\]

Expand

\[
|Y'+uY|^2
=|Y'|^2+u^2|Y|^2+u(|Y|^2)'.
\]

Integrating the cross term by parts,

\[
\int w_tu(|Y|^2)'
=-\int (w_tu)'|Y|^2.
\]

Since

\[
\frac{(w_tu)'}{w_t}
=u'+u\left(-\frac{2a}{t}+2u\right),
\]

we obtain

\[
\begin{aligned}
&u^2-u'-u\left(-\frac{2a}{t}+2u\right)\\
&\qquad=-u'+\frac{2a}{t}u-u^2.
\end{aligned}
\]

Thus

\[
\boxed{
\int w_t|Y'+uY|^2
=
\int w_t|Y'|^2
+
\int w_tV_t|Y|^2,
}
\]

where

\[
\boxed{
V_t(a)=-u'(a)+\frac{2a}{t}u(a)-u(a)^2.
}
\]

Boundary terms vanish by the Gaussian factor and standard order-one growth of `xi/M_0` on horizontal lines.

---

## 4. Exact Rayleigh decomposition

The denominator is

\[
\mathcal N_t(\gamma)=\int w_t|Y|^2.
\]

Hence

\[
\boxed{
\mathcal R_{1,t}(\gamma)
=t\frac{\int w_t|Y'|^2}{\int w_t|Y|^2}
+t\frac{\int w_tV_t|Y|^2}{\int w_t|Y|^2}.
}
\]

The first term is nonnegative. The second is an explicit weighted potential average.

The collision threshold becomes

\[
\boxed{
 t\frac{\int w_t|Y'|^2}{\int w_t|Y|^2}
+t\langle V_t\rangle_{w_t|Y|^2}
\ge2m.
}
\]

This is the normalized analytic-number-theory target.

---

## 5. Large-height expansion of the amplitude drift

Polymath's logarithmic derivative is

\[
\alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}.
\]

Let

\[
s=\frac12+a+i\gamma
\]

with `|a|` bounded and `gamma->infinity`. Then

\[
\Re\Log\frac{s}{2\pi}
=\log\frac{|s|}{2\pi}
=\log\frac\gamma{2\pi}+O\!\left(\frac{1+a^2}{\gamma^2}\right),
\]

while the real parts of `1/(2s)` and `1/(s-1)` are `O((1+|a|)/gamma^2)`.

Therefore

\[
\boxed{
 u(a)=\frac12\log\frac\gamma{2\pi}
+O\!\left(\frac{1+a^2}{\gamma^2}\right).
}
\]

Likewise

\[
\boxed{u'(a)=O(1/\gamma^2)}
\]

on bounded horizontal windows.

---

## 6. Shifted Gaussian saddle

If `u(a)` were exactly a constant `u_0`, then

\[
w_t(a)\propto
\exp\left(-\frac{a^2}{t}+2u_0a\right)
=
\exp\left(-\frac{(a-tu_0)^2}{t}\right)e^{tu_0^2}.
\]

Thus the weight is centered at

\[
a_*=tu_0.
\]

With the Riemann asymptotic,

\[
\boxed{
 a_*
\sim\frac t2\log\frac\gamma{2\pi}.
}
\]

If the heat-flow spatial variable is `x=2 gamma`, then, up to harmless constants inside the logarithm,

\[
2a_*\sim t\log\frac{x}{4\pi}.
\]

Thus the dimensionless parameter

\[
\lambda=t\log(x/4\pi)
\]

that already governs the high-positive-time asymptotic regime reappears automatically as the horizontal saddle displacement.

This is a structural consistency check, not an independent new asymptotic theorem.

---

## 7. Constant-drift potential model

For constant `u_0`,

\[
V_t(a)=\frac{2a}{t}u_0-u_0^2.
\]

Under the shifted Gaussian alone, the mean of `a` is `tu_0`, so

\[
\langle V_t\rangle=u_0^2.
\]

Hence the pure archimedean model contributes

\[
 t u_0^2
\sim\frac t4\log^2\frac\gamma{2\pi}
\]

to the Rayleigh quotient.

This explains the heuristic scale found in Round 35. But for the true xi function the residual factor `Y` changes the measure and adds nonnegative kinetic energy; no upper bound follows from the archimedean model alone.

---

## 8. Relation to the previous lambda-threshold program

The center of the normalized horizontal measure lies near

\[
\sigma_*
=\frac12+a_*
\sim\frac12+\frac\lambda2.
\]

When `lambda` is sufficiently large, this saddle moves into a right half-plane where Dirichlet-series methods become effective. This is exactly why positive-time/high-`x` Riemann-Siegel/Dirichlet approximations are strongest in the large-`lambda` regime.

Thus the new Rayleigh bridge does **not** magically remove the previously identified low-shoulder problem. It explains it in Hilbert-space terms:

- large `lambda`: the normalized residual is sampled in a tractable right-half-plane regime;
- low `lambda`: the weight remains centered in or near the critical strip, where no unconditional small kinetic-energy theorem is presently available.

This prevents us from falsely claiming that the heuristic `exp(C/sqrt t)` scale has already been proved.

---

## 9. Correct analytic target after normalization

To prove a new no-collision region from the Rayleigh method, it is enough to establish an upper bound

\[
 t\frac{\int w_t|Y'|^2}{\int w_t|Y|^2}
+t\langle V_t\rangle<4.
\]

The potential is explicit and accessible by Stirling calculus. The genuinely arithmetic channel is now isolated as

\[
\boxed{
\mathcal K_t(\gamma)
:=t\frac{\int w_t(a)|Y'(a)|^2da}
{\int w_t(a)|Y(a)|^2da}.
}
\]

Any advance must upper-bound `mathcal K_t` without assuming a zero-free critical-strip neighborhood.

---

## 10. Source/circularity audit

Safe source input:

- Polymath's explicit nonvanishing `M_0` and logarithmic derivative `alpha`;
- elementary Stirling asymptotics.

The decomposition itself is exact algebra/calculus.

Not used:

- RH or `Lambda<=0`;
- real-rootedness at the unknown time;
- a lower gap;
- pointwise `zeta'/zeta` boundedness through zeros;
- Rodgers--Tao negative-time contradiction estimates.

---

## 11. Status

- exact modulus/phase normalization: **PROVED**;
- exact ground-state Rayleigh decomposition: **PROVED**;
- explicit potential `V_t`: **PROVED**;
- saddle displacement `a_*~(t/2)log(gamma/2pi)`: **PROVED asymptotically**;
- structural recovery of the `lambda=t log x` scale: **PROVED interpretation**;
- unconditional upper bound on the normalized kinetic channel below the double-collision threshold: **OPEN**;
- heuristic `exp(C/sqrt t)` collision barrier: **NOT PROMOTED**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
