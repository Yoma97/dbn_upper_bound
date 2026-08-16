# Round 74 — `n=1` anchored phase-velocity collision certificate

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Introduces a collision-conditioned positive-weight certificate tailored to the finite-time PSC-core obstruction localized below `lambda=7.08` near `t=1/2`.

---

## 1. Setup

Use exactly the normalized fixed-cutoff notation of `phase_slope_transversality_v1.md`:

\[
p(x)=2\Re(e^{i\phi}S),
\qquad
S=\sum_{n\le N}a_ne^{-i\tau\log n},
\]

with

\[
a_n=\exp\left(\frac t4\log^2n-\sigma\log n\right)>0,
\qquad a_1=1.
\]

Write

\[
\theta_n=\phi-\tau\log n.
\]

Then

\[
\frac p2=\sum_{n\le N}a_n\cos\theta_n
=\cos\phi+\sum_{n=2}^N a_n\cos\theta_n.
\tag{74.1}
\]

Set

\[
A_0=\sum_{n=2}^N a_n,
\qquad
A_1=\sum_{n=2}^N a_n\log n.
\]

At a hypothetical true multiple zero, the Polymath remainder bounds imply

\[
|p|\le E_0,
\qquad
|p_x|\le E_1.
\tag{74.2}
\]

No information about zeros of `H_0` is used.

---

## 2. Value anchoring at the exact `n=1` term

From (74.1)--(74.2),

\[
|\cos\phi|
\le
A_0+\frac{E_0}{2}.
\tag{74.3}
\]

Define

\[
U:=A_0+\frac{E_0}{2}.
\]

Whenever `U<1`,

\[
\boxed{
|\sin\phi|\ge Q:=\sqrt{1-U^2}.
}
\tag{74.4}
\]

This is fundamentally different from the old triangle lower bound

\[
|S|\ge1-A_0.
\]

For `A_0` moderately close to one,

\[
\sqrt{1-A_0^2}
\]

can be much larger than `1-A_0`. The collision value condition is being used before the derivative estimate rather than after a phase-blind lower bound for `|S|`.

---

## 3. Exact derivative decomposition

Differentiating a single summand gives

\[
\frac{p_x}{2}
=
-\phi_x\sin\phi
+
\sum_{n=2}^N
 a_n\left[
 -\sigma_x\log n\cos\theta_n
 -(\phi_x-\tau_x\log n)\sin\theta_n
 \right].
\tag{74.5}
\]

For each `n>=2`, Cauchy--Schwarz in `R^2` yields

\[
\left|
-\sigma_x\log n\cos\theta_n
-(\phi_x-\tau_x\log n)\sin\theta_n
\right|
\le \omega_n,
\]

where

\[
\boxed{
\omega_n:=
\sqrt{(\sigma_x\log n)^2+
(\phi_x-\tau_x\log n)^2}.
}
\tag{74.6}
\]

Define the positive derivative-tail moment

\[
B_1:=\sum_{n=2}^N a_n\omega_n.
\tag{74.7}
\]

Combining (74.4)--(74.7) gives

\[
\boxed{
|p_x|
\ge
2\left(
|\phi_x|\sqrt{1-(A_0+E_0/2)^2}-B_1
\right).
}
\tag{74.8}
\]

Therefore:

### Theorem 74.1 — Anchored Phase-Velocity Certificate (APVC)

If

\[
A_0+E_0/2<1
\tag{74.9}
\]

and

\[
\boxed{
2\left(
|\phi_x|\sqrt{1-(A_0+E_0/2)^2}-B_1
\right)>E_1,
}
\tag{APVC}
\]

then `H_t(x)` and `H_t'(x)` cannot vanish simultaneously.

This theorem is exact apart from the already rigorous remainder bounds `E0,E1`.

---

## 4. Phase-free linear compression of `B_1`

On the real axis in the large positive-`x` regime used by the shoulder proof,

\[
\phi_x<0,
\qquad
\tau_x<0,
\qquad
\sigma_x\ge0.
\]

Put

\[
\Phi:=-\phi_x=|\phi_x|,
\qquad
T:=-\tau_x>0.
\]

Assume

\[
\boxed{
\Phi\ge T\log N
}
\tag{74.10}
\]

and

\[
T\ge\sigma_x.
\tag{74.11}
\]

Then for every `n<=N`,

\[
\phi_x-\tau_x\log n=-\Phi+T\log n\le0.
\]

Consequently

\[
\begin{aligned}
\omega_n
&=\sqrt{(\sigma_x\log n)^2+(\Phi-T\log n)^2}\\
&\le \sigma_x\log n+\Phi-T\log n\\
&=\Phi-(T-\sigma_x)\log n.
\end{aligned}
\tag{74.12}
\]

Summing with the positive amplitudes gives the key closed-form estimate

\[
\boxed{
B_1
\le
\Phi A_0-(T-\sigma_x)A_1.
}
\tag{74.13}
\]

Thus a simpler sufficient condition is

\[
\boxed{
2\left[
\Phi\left(
\sqrt{1-(A_0+E_0/2)^2}-A_0
\right)
+(T-\sigma_x)A_1
\right]
>E_1.
}
\tag{APVC-linear}
\]

The sign of the `A1` contribution is the crucial structural change: the old scalar PSC pays `d A1` as a fully adversarial loss, whereas APVC uses the fact that the total phase slope of the high-`n` terms is already cancelling the outer phase slope.

---

## 5. Why this is genuinely stronger than the old PSC in the finite-time corner

The old PSC uses

\[
|S|\ge1-A_0
\]

and

\[
|S_x|\le dA_1,
\]

so it discards both:

1. the value constraint's direct information on the `n=1` phase;
2. the correlation between `phi_x` and `tau_x log n` in the derivative of each term.

APVC retains both while remaining completely phase-free after (74.13).

It is **not** obtained by assuming cancellation in the oscillatory sum. Every estimate after the exact decomposition is a positive-term inequality.

---

## 6. Relation to the proposed invariant `J`

A second exact collision-conditioned quantity is

\[
J=\phi_x|S|^2+\Im(\overline S S_x).
\]

If `Z=e^{i\phi}S=X+iY`, then the exact identity

\[
J=X\,\Im Z_x-\frac Y2p_x
\]

holds. Thus at a true collision one obtains a small error budget for `J`.

However, certifying `J` sharply requires phase-sensitive information about `S` and `S_x`. In the present corner the map `(t,lambda)->x` magnifies phase variation enormously. APVC obtains a strong improvement using only positive moments, so it is the preferred first new tool. The `J` route is retained only if APVC reaches its own finite-time floor.

---

## 7. Asymptotic floor — important limitation

APVC is designed for the finite-time obstruction near `t=1/2`; it does not replace Round 65 in the singular small-time regime.

For fixed `lambda>4` as `t->0+`, Round 64 gives

\[
A_0\to\zeta(p)-1,
\qquad p=\frac12+\frac\lambda4.
\]

Also `Phi~lambda/(4t)`, while `T` remains asymptotic to `1/2`, so the positive `A1` correction in (APVC-linear) is lower order relative to `Phi`. The limiting sign condition becomes

\[
\sqrt{1-A_0^2}>A_0,
\]

i.e.

\[
A_0<\frac1{\sqrt2}.
\]

Equivalently the APVC asymptotic floor is the unique value

\[
\lambda_{\rm APVC,*}=4(p_{\rm A}-1/2),
\qquad
\zeta(p_{\rm A})=1+\frac1{\sqrt2},
\]

numerically

\[
\lambda_{\rm APVC,*}\approx5.7521220846.
\]

This is **higher** than the old triangle-PSC asymptotic floor

\[
\lambda_*\approx4.914588956.
\]

Therefore the correct architecture is a union of certificates:

- old exact-weight PSC for the small-time regime;
- APVC for the finite-time upper corner where old PSC loses sign first.

No single certificate is being forced beyond its natural regime.

---

## 8. Diagnostic only — target selection

A high-precision, non-interval evaluation of the exact positive sums at `t=1/2` gives approximately:

- at `lambda=7.06`, APVC derivative margin `~1.14`;
- at `lambda=6.90`, margin `~0.42`;
- at `lambda=6.85`, margin `~0.17`;
- the pointwise sign transition is near `lambda~6.819`, with small cutoff-dependent jumps.

These are **HEURISTIC/DIAGNOSTIC ONLY** and are not proof thresholds.

The first global certification target is deliberately conservative:

\[
\boxed{C_{\rm target}=6.90.}
\]

The existing PSC should continue to certify most of the rectangle; APVC is intended only for leaves that fail PSC near the finite-time edge.

---

## 9. Circularity audit

Inputs:

- unconditional Polymath effective approximation and its `E0,E1` bounds;
- exact finite Riemann--Siegel positive amplitudes;
- exact real-axis formulas for `sigma_x,tau_x,phi_x`;
- elementary trigonometry and Cauchy--Schwarz;
- positive-term directed-rounding sums in the intended implementation.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- real-rootedness of `H_0`;
- finite-height RH verification;
- zero-spacing assumptions;
- pair correlation / GUE;
- Laguerre--Polya membership;
- Rodgers--Tao negative-time contradiction estimates.

No desired collision-exclusion statement is used as an input.

---

## 10. Next implementation

1. Add an APVC branch to the existing rectangular MPFR verifier.
2. Keep the old PSC as the first cheap gate.
3. On a PSC-failed leaf, certify (74.10)--(74.11), an upper bound for `A0`, a lower bound for `A1`, and the APVC-linear margin.
4. Use an exact directed finite head for the `A1` lower bound; add a tangent/integral lower tail only if the finite head is insufficient.
5. Run `lambda>=6.90` first at 512 bits; rerun every accepted cover at 768 bits.
6. Record separately whether each leaf was closed by old PSC or APVC.
7. If 6.90 succeeds, lower the target adaptively until APVC rather than interval width becomes the dominant failure channel.
