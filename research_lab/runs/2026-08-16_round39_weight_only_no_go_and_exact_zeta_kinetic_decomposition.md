# Round 39 — Weight-only upper-bound no-go and exact zeta kinetic decomposition

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / NO-GO / EXACT DECOMPOSITION / SOURCE-GROUNDED / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 38 isolated the nonnegative kinetic channel

\[
\mathcal K_t(\gamma)
:=t\frac{\int_{\mathbb R}w_t(a)|Y'(a)|^2\,da}
{\int_{\mathbb R}w_t(a)|Y(a)|^2\,da},
\qquad
w_t(a)=G_t(a)|M_0(1/2+a+i\gamma)|^2,
\]

inside the collision Rayleigh quotient. This round makes two decisive corrections.

1. **No upper bound for \(\mathcal K_t\) can come from the geometry of the weight alone.** Poincare/log-concavity arguments naturally give lower coercive bounds; in fact the same fixed positive weight admits entire oscillatory test functions with arbitrarily large Rayleigh quotient.
2. For the actual Riemann function the normalized residual admits an exact arithmetic factorization. The kinetic channel becomes a Gaussian weighted quadratic form in \(\zeta\) and \(\zeta'\), with only an explicit bounded archimedean connection term.

Thus the remaining problem is genuinely arithmetic: one needs a theorem controlling a weighted \(\zeta'\)-energy relative to a weighted \(\zeta\)-mass in the moving saddle window. Weight convexity by itself cannot close the argument.

---

## 1. Weight-only upper bounds are impossible — PROVED

Let \(W:\mathbb R\to(0,\infty)\) be any integrable positive weight with

\[
0<\int_{\mathbb R}W(a)\,da<\infty.
\]

For \(N>0\), take the entire function

\[
Y_N(a):=e^{iNa}.
\]

Then

\[
|Y_N(a)|=1,
\qquad
|Y_N'(a)|=N,
\]

and hence exactly

\[
\boxed{
\frac{\int W|Y_N'|^2}{\int W|Y_N|^2}=N^2.
}
\]

Therefore

\[
\sup_{Y\ \mathrm{entire}}
\frac{\int W|Y'|^2}{\int W|Y|^2}=+\infty.
\]

This remains true if \(W\) is Gaussian, strictly log-concave, smooth, or has any fixed finite collection of derivative bounds.

### Consequence

A Poincare inequality for \(W\) has the form

\[
\int W|f-\langle f\rangle_W|^2
\le C_W\int W|f'|^2,
\]

so it supplies a **lower** bound on derivative energy in terms of variance. It cannot be inverted into the upper bound required to prove

\[
\mathcal R_{1,t}(\gamma)<4.
\]

Any successful upper bound must use an equation, a finite-frequency restriction, a Dirichlet-series representation, an approximate functional equation, or some other special property of the actual Riemann residual.

This rules out a purely Bakry--Emery/Poincare closure of Round 38.

---

## 2. Exact comparison of \(\xi\) with the Polymath Stirling normalizer

Write

\[
s=\frac12+a+i\gamma,
\qquad z=\frac s2.
\]

The completed zeta function is

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Polymath's nowhere-vanishing Stirling model is

\[
M_0(s)
=\frac{s(s-1)}{16}\pi^{-s/2}
\sqrt{2\pi}
\exp\!\left((z-\tfrac12)\Log z-z\right).
\]

Define the Stirling correction

\[
E(s):=
\frac{\Gamma(s/2)}
{\sqrt{2\pi}\exp((z-1/2)\Log z-z)}.
\]

Then the constants cancel exactly to give

\[
\boxed{
\frac{\xi(s)}{M_0(s)}=8E(s)\zeta(s).
}
\]

No RH input is used.

---

## 3. Exact logarithmic derivative of the Stirling correction

Let

\[
\alpha(s):=\frac{M_0'(s)}{M_0(s)}
=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}.
\]

Write

\[
\alpha(s)=u(s)+iv(s),
\qquad u=\Re\alpha,\quad v=\Im\alpha.
\]

The correction satisfies

\[
\boxed{
\delta(s):=\frac{E'(s)}{E(s)}
=\frac12\psi(s/2)-\frac12\Log(s/2)+\frac1{2s},
}
\]

where \(\psi=\Gamma'/\Gamma\).

By the standard Stirling expansion of the digamma function, uniformly in closed sectors away from the negative real axis,

\[
\boxed{
\delta(s)=-\frac1{6s^2}+O(|s|^{-4}).
}
\]

In particular the error between the exact gamma logarithmic derivative and the Polymath Stirling model is second order in height, not merely first order.

---

## 4. Exact arithmetic factorization of the Round-38 residual

Let

\[
M_0(s(a))=\rho(a)e^{i\theta(a)},
\qquad \rho>0,
\]

and recall

\[
Y(a)=\frac{\xi(s(a))}{\rho(a)}.
\]

Since \(\theta'(a)=v(s(a))\), the identity above gives

\[
Y(a)=8e^{i\theta(a)}E(s(a))\zeta(s(a)).
\]

Define

\[
C(a):=8e^{i\theta(a)}E(s(a)).
\]

Then

\[
\boxed{
\frac{C'(a)}{C(a)}=iv(s(a))+\delta(s(a)).
}
\]

Hence

\[
\boxed{
Y'(a)
=C(a)\Bigl[
\zeta'(s(a))+eta(s(a))\zeta(s(a))
\Bigr],
}
\]

where

\[
\boxed{
\beta(s):=i\Im\alpha(s)+\delta(s).
}
\]

This is a nonsingular identity: no pointwise \(\zeta'/\zeta\) is used.

---

## 5. The kinetic channel as an exact weighted \(\zeta,\zeta'\) quadratic form

Put

\[
P(s):=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),
\]

so that

\[
\xi(s)=P(s)\zeta(s).
\]

Because

\[
8M_0(s)E(s)=P(s),
\]

we have

\[
w_t(a)|C(a)|^2
=G_t(a)|P(s(a))|^2.
\]

Therefore the Round-38 kinetic channel is exactly

\[
\boxed{
\mathcal K_t(\gamma)
=t\,
\frac{
\int_{\mathbb R}G_t(a)|P(s(a))|^2
\left|\zeta'(s(a))+\beta(s(a))\zeta(s(a))\right|^2\,da
}{
\int_{\mathbb R}G_t(a)|P(s(a))|^2
|\zeta(s(a))|^2\,da
}.
}
\]

Thus the unknown channel is an honest weighted derivative-energy ratio for \(\zeta\), with an explicit archimedean connection \(\beta\).

At large positive ordinate and bounded horizontal displacement,

\[
\Im\alpha(s)=\frac\pi4+O(1/\gamma),
\qquad
\delta(s)=O(1/\gamma^2),
\]

so

\[
\beta(s)=i\frac\pi4+O(1/\gamma).
\]

The main large parameter \(\tfrac12\log(\gamma/2\pi)\) has already been transferred into the moving weight/saddle; it is not present in \(\beta\).

---

## 6. Circularity audit

The following are **not** used:

- RH or \(\Lambda\le0\);
- real-rootedness of any unknown positive-time slice;
- lower bounds for gaps between zeros;
- positivity of \(L_1\) or higher Laguerre inequalities;
- pointwise division by \(\zeta\) near its zeros;
- Rodgers--Tao negative-time local-equilibrium estimates.

The exact factorization is unconditional wherever the Polymath branch of \(M_0\) is defined, in particular along horizontal lines with positive ordinate.

---

## 7. What a successful Round 40 theorem must look like

The collision threshold from Rounds 35--36 is

\[
\mathcal R_{1,t}(\gamma)\ge4
\]

for a double collision. Round 38 writes

\[
\mathcal R_{1,t}=\mathcal K_t+t\langle V_t\rangle.
\]

Round 39 shows that \(\mathcal K_t\) cannot be bounded above from weight geometry alone. Hence the next admissible target is an arithmetic theorem of the form

\[
\boxed{
\int W_{t,\gamma}(a)
|\zeta'(s)+\beta(s)\zeta(s)|^2\,da
\le
\frac{C(t,\gamma)}{t}
\int W_{t,\gamma}(a)|\zeta(s)|^2\,da,
}
\]

with

\[
W_{t,\gamma}(a)=G_t(a)|P(1/2+a+i\gamma)|^2
\]

and with \(C+t\langle V_t\rangle<4\) in a nontrivial region.

The first region to attack is the high-saddle/large-\(\lambda\) regime, where the mass of \(W_{t,\gamma}\) is shifted into \(\Re s>1\) and the absolutely convergent Dirichlet series for \(\zeta\) and \(\zeta'\) becomes available. This should be treated as an unconditional consistency test against the existing Polymath high-height zero-free regime, not advertised as a new RH proof.

---

## 8. Status

- weight-only/Poincare upper bound for \(\mathcal K_t\): **REFUTED**;
- exact \(\xi/M_0=8E\zeta\) factorization: **PROVED**;
- exact nonsingular \(\zeta,\zeta'\) kinetic form: **PROVED**;
- Stirling correction \(\delta(s)=O(|s|^{-2})\): **PROVED asymptotically in the standard sector**;
- high-saddle Dirichlet-series upper bound: **OPEN / next target**;
- low-\(\lambda\) arithmetic kinetic bound: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
