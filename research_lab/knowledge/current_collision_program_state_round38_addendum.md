# Collision Program State — Round 38 addendum

**Date:** 2026-08-16

**RH status:** OPEN.

## Executive update

Rounds 30--38 materially change the active frontier.

The justified strategic ranking remains

\[
\boxed{A\gtrsim B\gg C,}
\]

but `A` must now be split:

- **generic/local entropy-kernel A:** structurally exhausted/frozen unless a genuinely new Riemann-specific input appears;
- **Riemann-specific/cross-frontier A:** active, now centered on a positive horizontal Gaussian-Hermite/Rayleigh observable;
- **B:** local all-multiplicity degree remains valid, but global winding remains a real-zero-count spectral-flow observable and is secondary;
- **C:** tertiary.

The current preferred target is no longer a raw `L_1` positivity proof, raw theta diagonal dominance, or global horizontal sign-change count. It is an independent upper bound for a normalized horizontal kinetic Rayleigh quotient.

---

## 1. Theta route corrections: Rounds 30--31

The raw Riemann theta mode expansion

\[
\Phi(u)=\sum_{n\ge1}a_n(u)
\]

cannot be split into a finite positive diagonal associated-kernel main term plus an off-diagonal perturbation.

Round 30 proves:

\[
|\widehat a_n(\xi)|\asymp_\xi n^{-1/2},
\]

and the formal diagonal first-associated-kernel mass obeys

\[
\int s^2a_n(s)^2ds
\asymp\frac{(\log n)^2}{n},
\]

so the diagonal sum diverges even though the true `K_1(0)` is finite. Finiteness itself requires cancellation between theta modes.

Round 31 proves a stronger obstruction. If any nonempty finite block of raw modes is repaired by even reflection, some odd endpoint jet remains nonzero. The resulting algebraic Fourier tail forces

\[
L_1(x)<0
\]

for all sufficiently large `x`. Therefore no finite reflected theta block can be a termwise positive-definite building block.

**Status:** raw/finite theta-block strategy **FROZEN**. Only genuinely infinite modular/Ewald resummations remain admissible.

---

## 2. Cross-frontier Gaussian-Hermite bridge: Round 32

Using Polymath's unconditional heat representation, define

\[
G_t(a)=\frac1{\sqrt{\pi t}}e^{-a^2/t}.
\]

Then for every `k>=0`,

\[
\boxed{
H_t^{(k)}(2\gamma)
=\frac{i^k}{8(2\sqrt t)^k}
\int_{\mathbb R}G_t(a)H_k(a/\sqrt t)
\xi(1/2+a+i\gamma)da.
}
\]

Hence multiplicity at least `m` at `x=2 gamma` is exactly the vanishing of the first `m` horizontal Gaussian-Hermite coefficients of xi.

This bridge is unconditional and does not use RH, Laguerre positivity, or real-rootedness at the unknown time.

---

## 3. Round 33 theorem retained but demoted by Round 37

Moment orthogonality implies that an `m`-fold collision forces at least

\[
\lceil m/2\rceil
\]

sign changes of the horizontal real part and at least

\[
\lfloor m/2\rfloor
\]

of the horizontal imaginary part.

The theorem is mathematically correct. However Round 37 shows that for every fixed `gamma!=0`, Stirling's formula gives

\[
\arg\xi(\sigma+i\gamma)
=\frac\gamma2\log\frac\sigma{2\pi}+o(1)
\]

as `sigma->infinity`. Thus both horizontal components already change sign infinitely often far to the right, independently of collision.

Therefore Round 33 is **globally non-discriminating**. It becomes useful only after a localization theorem or archimedean phase normalization.

---

## 4. Positive Parseval energy: Round 34

Define

\[
\mathcal N_t(\gamma)
:=\int_{\mathbb R}G_t(a)|\xi(1/2+a+i\gamma)|^2da.
\]

Hermite Parseval gives the exact identity

\[
\boxed{
\mathcal N_t(\gamma)
=64\sum_{k=0}^{\infty}
\frac{(2t)^k}{k!}|H_t^{(k)}(2\gamma)|^2.
}
\]

If multiplicity is at least `m`, the sum starts at `k=m`.

The low-mode energy

\[
\mathcal L_{m,t}(\gamma)
=64\sum_{k=0}^{m-1}\frac{(2t)^k}{k!}|H_t^{(k)}(2\gamma)|^2
\]

is a manifestly positive collision detector:

\[
\mathcal L_{m,t}(\gamma)=0
\iff
\text{multiplicity at least }m.
\]

Unlike `L_1`, this is not a signed Laguerre expression.

---

## 5. Gaussian spectral-gap hierarchy: Round 35

At a multiplicity-at-least-`m` collision, for every `1<=q<=m`,

\[
\boxed{
 t^q\int G_t(a)|\xi^{(q)}(1/2+a+i\gamma)|^2da
 \ge
 2^q\frac{m!}{(m-q)!}\mathcal N_t(\gamma).
}
\]

In particular the first Rayleigh quotient

\[
\boxed{
\mathcal R_{1,t}(\gamma)
:=t\frac{\int G_t|\xi'|^2}{\int G_t|\xi|^2}
}
\]

satisfies

\[
\text{multiplicity at least }m
\Longrightarrow
\mathcal R_{1,t}(\gamma)\ge2m.
\]

Thus a double collision requires

\[
\boxed{\mathcal R_{1,t}(\gamma)\ge4.}
\]

Any unconditional upper bound below `4` yields a no-double-collision region.

---

## 6. Scalar positive PDE: Round 36

The horizontal norm satisfies

\[
\boxed{
\left(\partial_t+\frac14\partial_\gamma^2\right)
\mathcal N_t(\gamma)
=
\int G_t(a)|\xi'(1/2+a+i\gamma)|^2da
\ge0.
}
\]

Therefore the collision threshold is equivalently

\[
\boxed{
 t\frac{(\partial_t+\frac14\partial_\gamma^2)\mathcal N_t}
 {\mathcal N_t}
\ge2m.
}
\]

This formulation avoids pointwise poles of `xi'/xi` and packages the problem into a smooth positive scalar function.

---

## 7. Archimedean ground-state normalization: Round 38

Polymath's nowhere-zero Stirling normalizer `M_0` has

\[
\alpha(s)=\frac{M_0'}{M_0}
=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}.
\]

For

\[
s(a)=1/2+a+i\gamma,
\qquad
\rho(a)=|M_0(s(a))|,
\qquad
u(a)=\Re\alpha(s(a)),
\]

put

\[
Y(a)=\frac{\xi(s(a))}{\rho(a)},
\qquad
w_t(a)=G_t(a)\rho(a)^2.
\]

Then exactly

\[
\boxed{
\int G_t|\xi'|^2
=
\int w_t|Y'|^2
+
\int w_tV_t|Y|^2,
}
\]

with

\[
\boxed{
V_t(a)=-u'(a)+\frac{2a}{t}u(a)-u(a)^2.
}
\]

Hence

\[
\boxed{
\mathcal R_{1,t}
=t\frac{\int w_t|Y'|^2}{\int w_t|Y|^2}
+t\langle V_t\rangle.
}
\]

The first term is a nonnegative normalized **arithmetic kinetic channel**. The potential is explicit archimedean data.

At large ordinate,

\[
u(a)=\frac12\log\frac\gamma{2\pi}+O((1+a^2)/\gamma^2),
\]

and the effective weight is centered near

\[
\boxed{
a_*\sim\frac t2\log\frac\gamma{2\pi}.}
\]

Thus the previous scale

\[
\lambda=t\log(x/4\pi)
\]

reappears as twice the horizontal saddle displacement. This explains why the large-`lambda` regime is tractable and why the low shoulder remains the hard region.

---

## 8. Current admissible target

The new primary problem is:

\[
\boxed{
\mathcal K_t(\gamma)
:=t\frac{\int w_t(a)|Y'(a)|^2da}
{\int w_t(a)|Y(a)|^2da}.
}
\]

Seek an unconditional upper bound for

\[
\mathcal K_t+t\langle V_t\rangle
\]

strictly below `4` in a region not already covered trivially by Polymath's high-`x` simple-zero theorem.

The proof must tolerate zeros of zeta inside the horizontal window and therefore should not rely on a pointwise zero-free estimate for `zeta'/zeta`.

Potential legitimate inputs:

- direct mean-square estimates for the normalized residual;
- Dirichlet-polynomial representations after the saddle enters a right half-plane;
- a new weighted horizontal large-value inequality;
- a cross-frontier zero-density estimate controlling the kinetic channel in average or pointwise after an amplification step.

---

## 9. Frozen/rejected targets

Do not spend new rounds on the following without genuinely new structure:

- global discriminant;
- flux-integrability alone;
- raw global winding of `H+iH'`;
- Polymath-renormalized winding `g-N_real`;
- generic kernel positivity/log-concavity;
- raw `L_1>=0` as an unexplained target;
- finite/raw theta diagonal dominance;
- finite reflected theta blocks;
- global horizontal component sign-change counts.

---

## 10. Circularity guard

Still unsafe for proving `Lambda<=0`:

- Rodgers--Tao estimates whose proof assumes `Lambda<0`;
- global LP/all-real-zero hypotheses on the unknown slice;
- generalized Laguerre positivity hierarchy;
- a lower gap assumed rather than derived;
- zero-free critical-strip tubes strong enough to exclude the target event.

Safe:

- exact heat identities;
- unconditional Polymath positive-time normalizers/asymptotics in their stated ranges;
- functional equation and standard completion formula;
- Gaussian/Hermite Hilbert-space identities;
- unconditional analytic-number-theory mean-value/zero-density inputs used with exact hypotheses.

## 11. Current status

- RH: **OPEN**.
- Local collision geometry: **largely resolved**.
- Global topological route: **secondary / count-equivalent barrier**.
- Generic entropy/kernel route: **frozen**.
- Positive horizontal Gaussian-Rayleigh bridge: **ACTIVE / HIGHEST PRIORITY**.
- Missing theorem: **independent upper control of normalized kinetic energy in the low/intermediate lambda regime**.
- Novelty of Rounds 30--38: **UNVERIFIED pending literature search**.
