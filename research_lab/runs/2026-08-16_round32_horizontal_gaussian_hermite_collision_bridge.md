# Round 32 — Collision multiplicity as horizontal Gaussian-Hermite orthogonality of the Riemann xi function

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED IDENTITY / CROSS-FRONTIER BRIDGE / NON-CIRCULAR / NOVELTY UNVERIFIED.

## 0. Executive verdict

Rounds 30--31 show that a local theta-mode decomposition of the associated kernel cannot be made into a finite positive-main/error argument without a genuinely infinite modular resummation. Rather than continue repackaging the same Laguerre barrier, this round changes frontier.

Polymath gives the exact Gaussian heat representation

\[
H_t(z)
=\frac1{8\sqrt\pi}
\int_{\mathbb R}
\xi\!\left(
\frac{1+iz}{2}+\sqrt t\,v
\right)e^{-v^2}\,dv.
\]

For a real point `z=2 gamma`, this is a Gaussian average of `xi(sigma+i gamma)` in the **horizontal sigma direction** around the critical line.

Define

\[
G_t(a):=\frac1{\sqrt{\pi t}}e^{-a^2/t}
\]

and let `H_k` denote the physicists' Hermite polynomial, normalized by

\[
\frac{d^k}{dy^k}e^{-y^2}=(-1)^kH_k(y)e^{-y^2}.
\]

Then for every integer `k>=0`,

\[
\boxed{
H_t^{(k)}(2\gamma)
=\frac{i^k}{8(2\sqrt t)^k}
\int_{\mathbb R}
G_t(a)
H_k\!\left(\frac a{\sqrt t}\right)
\xi\!\left(\frac12+a+i\gamma\right)\,da.
}
\]

Consequently a real zero of `H_t` at `x=2 gamma` has multiplicity at least `m` if and only if

\[
\boxed{
\int_{\mathbb R}
G_t(a)H_k(a/\sqrt t)
\xi(1/2+a+i\gamma)\,da=0,
\qquad k=0,1,\ldots,m-1.
}
\]

Thus an `m`-fold heat-flow collision is exactly the vanishing of the first `m` horizontal Gaussian-Hermite coefficients of the completed zeta function at ordinate `gamma`.

This is a genuine cross-frontier interface: the heat-flow collision problem is converted into a finite set of weighted horizontal identities for the classical xi function, with no assumption about real-rootedness.

---

## 1. Source input: Polymath heat representation

D.H.J. Polymath derives

\[
H_t(z)
=\int_{\mathbb R}
\frac18\xi\!\left(
\frac{1+iz}{2}+\sqrt t\,v
\right)
\frac{e^{-v^2}}{\sqrt\pi}\,dv.
\]

The formula follows from the backward heat kernel identity and is unconditional.

For `z=2 gamma` real, substitute

\[
a=\sqrt t\,v.
\]

Then

\[
\boxed{
H_t(2\gamma)
=\frac18
\int_{\mathbb R}
G_t(a)
\xi\!\left(\frac12+a+i\gamma\right)\,da.
}
\]

No RH or statement about the zeros is used.

---

## 2. Horizontal symmetry of xi

Put

\[
X_\gamma(a):=\xi\!\left(\frac12+a+i\gamma\right).
\]

The functional equation and conjugation symmetry give

\[
\xi(s)=\xi(1-s),
\qquad
\xi(\overline s)=\overline{\xi(s)}.
\]

Therefore for real `a,gamma`,

\[
\boxed{
X_\gamma(-a)=\overline{X_\gamma(a)}.
}
\]

Hence

- `Re X_gamma(a)` is even in `a`;
- `Im X_gamma(a)` is odd in `a`.

This explains why the Gaussian integral above is real.

---

## 3. Derivative transfer from ordinate to horizontal variable

Since `xi` is entire,

\[
\partial_\gamma X_\gamma(a)
=i\,\xi'\!\left(\frac12+a+i\gamma\right)
=i\,\partial_aX_\gamma(a).
\]

Let

\[
I_t(\gamma):=
\int_{\mathbb R}G_t(a)X_\gamma(a)\,da.
\]

Then

\[
H_t(2\gamma)=\frac18I_t(\gamma).
\]

Repeated differentiation gives

\[
\partial_\gamma^k I_t(\gamma)
=i^k\int_{\mathbb R}G_t(a)\partial_a^kX_\gamma(a)\,da.
\]

The Gaussian dominates the standard xi growth on horizontal lines, so integration by parts `k` times is justified and yields

\[
\partial_\gamma^k I_t(\gamma)
=(-i)^k
\int_{\mathbb R}G_t^{(k)}(a)X_\gamma(a)\,da.
\]

---

## 4. Hermite form of the Gaussian derivatives

Write

\[
y=\frac a{\sqrt t}.
\]

Because

\[
G_t(a)=\frac1{\sqrt{\pi t}}e^{-y^2},
\]

we have

\[
\boxed{
G_t^{(k)}(a)
=(-1)^kt^{-k/2}
H_k(y)G_t(a).
}
\]

Thus

\[
\partial_\gamma^k I_t(\gamma)
=i^kt^{-k/2}
\int_{\mathbb R}
G_t(a)H_k(a/\sqrt t)X_\gamma(a)\,da.
\]

On the other hand,

\[
\frac{d^k}{d\gamma^k}H_t(2\gamma)
=2^kH_t^{(k)}(2\gamma)
=\frac18\partial_\gamma^kI_t(\gamma).
\]

Combining the two identities proves

\[
\boxed{
H_t^{(k)}(2\gamma)
=\frac{i^k}{8(2\sqrt t)^k}
\int_{\mathbb R}
G_t(a)H_k(a/\sqrt t)
X_\gamma(a)\,da.
}
\]

---

## 5. Collision-multiplicity theorem — PROVED

A real point `x=2 gamma` is a zero of exact multiplicity `m` of `H_t` precisely when

\[
H_t^{(k)}(2\gamma)=0
\quad(k=0,1,\ldots,m-1),
\]

and

\[
H_t^{(m)}(2\gamma)\ne0.
\]

By Section 4 this is equivalent to

\[
\boxed{
\int_{\mathbb R}
G_t(a)H_k(a/\sqrt t)
X_\gamma(a)\,da=0
\quad(k<m),
}
\]

while the `k=m` moment is nonzero.

Therefore multiplicity is exactly the number of initial horizontal Gaussian-Hermite coefficients that vanish.

---

## 6. Double collision in real/imaginary form

For `m=2`, `H_0(y)=1` and `H_1(y)=2y`.

The zeroth condition is

\[
\int_{\mathbb R}G_t(a)X_\gamma(a)\,da=0.
\]

Using horizontal conjugation symmetry,

\[
\boxed{
\int_0^\infty
G_t(a)
\Re\xi(1/2+a+i\gamma)\,da=0.
}
\]

The first condition is

\[
\int_{\mathbb R}aG_t(a)X_\gamma(a)\,da=0.
\]

The real part is odd and drops out, while the imaginary part is even after multiplication by `a`. Hence

\[
\boxed{
\int_0^\infty
aG_t(a)
\Im\xi(1/2+a+i\gamma)\,da=0.
}
\]

Thus a double collision is exactly the simultaneous cancellation of

1. a Gaussian-weighted even horizontal real part; and
2. a first-moment Gaussian-weighted horizontal imaginary part.

This formulation does not refer to unknown zero trajectories.

---

## 7. The first nonzero moment measures the collision jet

At an exact multiplicity-`m` collision, define

\[
M_k(t,\gamma)
:=
\int_{\mathbb R}
G_t(a)H_k(a/\sqrt t)
X_\gamma(a)\,da.
\]

Then

\[
M_0=\cdots=M_{m-1}=0
\]

and

\[
\boxed{
M_m
=8(2\sqrt t)^m i^{-m}H_t^{(m)}(2\gamma)\ne0.
}
\]

Therefore Round 19's local multiplicity and Round 26's discriminant order can be read directly from the first nonzero horizontal Hermite coefficient.

This gives an exact interface between local collision geometry and horizontal analytic-number-theory data.

---

## 8. Gaussian-Hermite Parseval viewpoint

The physicists' Hermite polynomials are orthogonal for the weight `e^{-y^2}`:

\[
\int_{\mathbb R}e^{-y^2}H_j(y)H_k(y)\,dy
=\sqrt\pi\,2^kk!\,\delta_{jk}.
\]

Thus, whenever the horizontal slice belongs to the corresponding Gaussian `L^2` space, its expansion

\[
X_\gamma(\sqrt t\,y)
=\sum_{k\ge0}c_k(t,\gamma)H_k(y)
\]

has coefficients proportional to the moments `M_k`.

A multiplicity-`m` collision means exactly

\[
\boxed{c_0=c_1=\cdots=c_{m-1}=0.}
\]

Hence all horizontal Gaussian energy lies in Hermite modes `k>=m`.

This suggests a genuinely new class of possible collision-exclusion inequalities: prove that the first one or two Hermite modes cannot simultaneously vanish because they must capture a nonzero portion of a separately controlled horizontal norm.

No such inequality is claimed here.

---

## 9. Why a naive uniform spectral-gap inequality is unlikely

One might hope for a uniform bound

\[
|M_0|^2+|M_1|^2
\ge c\int G_t(a)|X_\gamma(a)|^2\,da
\]

with an absolute `c>0`.

This is too strong to promote without evidence. The Riemann heat family has infinitely many ordinary real zeros, at which `M_0=0`, and near unusually close zero configurations the derivative channel `M_1` can be very small. The known Lehmer-pair phenomenon warns against assuming a height-uniform spectral gap.

Therefore the bridge is useful only if the lower bound is allowed to depend quantitatively on `t,gamma` and is proved from independent analytic-number-theory information.

---

## 10. Cross-frontier research targets generated by the identity

The collision problem is now equivalent to excluding simultaneous vanishing of finitely many explicit horizontal Gaussian-Hermite transforms of `xi`.

Three legitimate targets are:

### Target GH-A — horizontal low-mode concentration

Find an explicit positive function `delta(t,gamma)` such that

\[
|M_0|^2+|M_1|^2
\ge
\delta(t,\gamma)\,\mathcal N_t(\gamma),
\]

where `N_t(gamma)>0` is an independently controlled horizontal norm. Any strictly positive `delta` excludes a double collision.

### Target GH-B — Dirichlet-polynomial evaluation

Derive a rigorously convergent representation of `M_0,M_1` or a positive quadratic combination of them in a region where current Dirichlet-polynomial/large-value technology applies. The representation must not assume a zero-free critical line.

### Target GH-C — sparse-exception amplification

Show that simultaneous vanishing of `M_0,M_1` forces a quantitatively large horizontal excursion of `xi` away from the critical line, and then compare that excursion with unconditional zero-density or large-value estimates.

These are cross-frontier tasks rather than restatements of Laguerre positivity.

---

## 11. Circularity audit

Safe inputs used here:

- Polymath's unconditional Gaussian heat representation;
- the functional equation and conjugation symmetry of `xi`;
- analyticity and Gaussian integration by parts;
- Hermite orthogonality.

Not used:

- RH;
- `Lambda<=0`;
- real-rootedness of the unknown `H_t` slice;
- Laguerre positivity;
- Rodgers--Tao negative-time estimates under `Lambda<0`;
- any lower-gap assumption.

The statement `M_0=M_1=0 never occurs for t>0` is of course RH-equivalent after the finite-threshold reduction; it is **not** assumed. The new content is the exact Hermite-Gaussian representation that exposes possible independent analytic inputs.

---

## 12. Status

- horizontal Gaussian representation: **SOURCE-ESTABLISHED**;
- all-derivative Hermite-Gaussian identity: **PROVED**;
- multiplicity `m` iff first `m` horizontal Hermite coefficients vanish: **PROVED**;
- double-collision real/imaginary moment pair: **PROVED**;
- collision jet equals first nonzero Hermite moment: **PROVED**;
- positive horizontal low-mode concentration theorem: **OPEN**;
- Dirichlet-polynomial bridge: **OPEN**;
- sparse-exception amplification from the moment pair: **OPEN**;
- RH: **OPEN**;
- novelty of this packaging: **UNVERIFIED**.
