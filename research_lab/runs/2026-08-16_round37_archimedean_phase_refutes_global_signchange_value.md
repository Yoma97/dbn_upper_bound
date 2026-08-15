# Round 37 — Archimedean phase makes global horizontal sign-change counts non-discriminating

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED CORRECTION / STRUCTURAL BARRIER / ROUND-33 DEMOTION / NOVELTY UNVERIFIED.

## 0. Executive correction

Round 33 proved a mathematically correct implication: an `m`-fold heat collision at `x=2 gamma` forces at least `ceil(m/2)` sign changes of

\[
\Re\xi(1/2+a+i\gamma)
\]

and at least `floor(m/2)` sign changes of

\[
\Im\xi(1/2+a+i\gamma)
\]

on the full half-line `a>0`.

This round shows that **the global count is not a useful collision signature**. For every fixed `gamma!=0`, independently of any collision, the archimedean Gamma factor causes the horizontal phase of `xi(sigma+i gamma)` to diverge logarithmically as `sigma->+infinity`. In particular both real and imaginary parts have infinitely many sign changes on the right half-line.

More precisely,

\[
\boxed{
\arg\xi(\sigma+i\gamma)
=
\frac\gamma2\log\frac{\sigma}{2\pi}+o(1)
\qquad(\sigma\to+\infty)
}
\]

modulo a fixed continuous choice of phase. Hence for every fixed `gamma>0`,

\[
\boxed{
\Re\xi(\sigma+i\gamma)
\text{ and }
\Im\xi(\sigma+i\gamma)
\text{ each change sign infinitely often as }\sigma\to\infty.
}
\]

Therefore Round 33 remains a correct moment theorem but is **DEMOTED as a global amplification mechanism**. Only a localization theorem forcing the collision-induced moment cancellations to be realized in a bounded horizontal window can carry new information.

---

## 1. Exact factorization in the right half-plane

For

\[
s=\sigma+i\gamma,
\]

the completed xi function is

\[
\xi(s)
=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Fix a real `gamma!=0` and let `sigma->+infinity`.

The Dirichlet series gives

\[
\zeta(\sigma+i\gamma)=1+O(2^{-\sigma}),
\]

and therefore

\[
\arg\zeta(\sigma+i\gamma)=O(2^{-\sigma})
\]

on the continuous branch tending to zero.

Also

\[
\arg(s(s-1))=O_\gamma(1/\sigma).
\]

Thus the unbounded phase comes entirely from the Gamma/pi factor.

---

## 2. Stirling phase

Put

\[
z=s/2=x+iy,
\qquad
x=\sigma/2,
\qquad
y=\gamma/2.
\]

For fixed `y` and `x->infinity`, Stirling's formula gives

\[
\log\Gamma(z)
=(z-1/2)\log z-z+\frac12\log(2\pi)+O(1/z).
\]

Write

\[
\log z=\log|z|+i\arg z.
\]

Its imaginary part is

\[
\Im\log\Gamma(z)
=(x-1/2)\arg z+y\log|z|-y+O(1/x).
\]

Since

\[
\arg z=\frac yx+O(x^{-3}),
\qquad
\log|z|=\log x+O(x^{-2}),
\]

we obtain

\[
(x-1/2)\arg z-y=O(1/x),
\]

and hence

\[
\boxed{
\Im\log\Gamma(s/2)
=\frac\gamma2\log\frac\sigma2+O_\gamma(1/\sigma).
}
\]

The factor `pi^{-s/2}` contributes phase

\[
-\frac\gamma2\log\pi.
\]

Combining all factors,

\[
\boxed{
\arg\xi(\sigma+i\gamma)
=\frac\gamma2\log\frac{\sigma}{2\pi}
+O_\gamma(1/\sigma)+O(2^{-\sigma}).
}
\]

---

## 3. Infinite horizontal component oscillation

For `sigma>1`, zeta has no zeros and none of the elementary completion factors vanish. Therefore

\[
\xi(\sigma+i\gamma)\ne0.
\]

Its modulus is positive and its continuous argument from Section 2 tends to `+infinity` if `gamma>0` and to `-infinity` if `gamma<0`.

Hence the path crosses the rays

\[
\arg z=\frac\pi2+k\pi
\]

and

\[
\arg z=k\pi
\]

infinitely many times.

By continuity, these crossings yield infinitely many zeros/sign changes of the real and imaginary components respectively.

Thus

\[
\boxed{
\#\{\text{horizontal sign changes of Re xi}\}=\infty,
\qquad
\#\{\text{horizontal sign changes of Im xi}\}=\infty
}
\]

for every fixed nonzero ordinate.

---

## 4. Consequence for Round 33

Round 33's moment/Chebyshev argument is not mathematically wrong. It says that collision moment orthogonality enforces a finite minimum number of sign changes.

But because infinitely many sign changes occur unconditionally in the far right half-plane, the statement

\[
\text{collision}\Longrightarrow\text{at least }N\text{ horizontal sign changes somewhere}
\]

is globally non-discriminating.

The only potentially meaningful strengthened version is

\[
\boxed{
\text{collision}\Longrightarrow
\text{forced sign changes in a controlled window }
0<a\le A(t,\gamma).
}
\]

The window must lie before the generic archimedean phase winding makes sign changes automatic.

---

## 5. Natural archimedean phase scale

The leading phase is

\[
\theta_{\rm arch}(\sigma,\gamma)
=\frac\gamma2\log\frac\sigma{2\pi}.
\]

A phase increment of order `pi` occurs when `sigma` changes multiplicatively by

\[
\exp(2\pi/|\gamma|).
\]

For large `gamma`, this is very close to `1`. Thus at high ordinate the generic completion factor can generate horizontal component sign changes on very short relative scales once one is far enough into the right half-plane.

This reinforces that raw sign-change counts are a poor high-height observable unless the archimedean phase is first normalized away.

---

## 6. Corrected cross-frontier observable

A better horizontal object should remove the explicit nonvanishing archimedean factor before counting phase/sign behavior.

Polymath uses precisely such a philosophy: divide by a nowhere-zero Stirling-type normalizer `M_t`/`B_t` to remove the dominant Gamma-factor decay and phase in the high-height regime.

Thus if Round 33 is revived, it should be reformulated for a normalized horizontal function, schematically

\[
Z_{\rm hor}(s)
:=\frac{\xi(s)}{M_0(s)},
\]

or for an exact completion-factor normalization, and then the moment identities must be rederived with the resulting nonconstant weight. One must not simply subtract the phase after the fact without tracking its effect on Gaussian-Hermite orthogonality.

---

## 7. Relation to Rounds 35--36

The positive norm/Rayleigh route survives this correction because

\[
|\xi|^2
\]

and

\[
|\xi'|^2
\]

are not merely component sign counts.

However the same archimedean factor contributes a large, explicitly computable portion of the derivative Rayleigh quotient. A useful upper bound should therefore normalize or separate the Gamma-factor contribution before treating the zeta-dependent residual.

This is the preferred next analysis.

---

## 8. Circularity audit

Used:

- the exact completion formula for xi;
- the absolutely convergent Dirichlet series for zeta in `sigma>1`;
- Stirling asymptotics.

No RH, zero-density hypothesis, or real-rootedness is used.

---

## 9. Status correction

- Round-33 moment orthogonality theorem: **REMAINS PROVED**;
- collision forces finite global component sign-change counts: **TRUE BUT NON-DISCRIMINATING**;
- every fixed nonzero horizontal xi slice has infinitely many far-right component sign changes: **PROVED**;
- Round 33 as a standalone sparse-exception amplification mechanism: **DEMOTED**;
- localized/archimedean-normalized sign-change theorem: **OPEN**;
- Gaussian norm/Rayleigh bridge of Rounds 34--36: **REMAINS LIVE**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
