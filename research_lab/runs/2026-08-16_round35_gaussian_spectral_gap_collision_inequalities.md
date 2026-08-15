# Round 35 — Gaussian spectral-gap hierarchy forced by a heat collision

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / QUANTITATIVE CROSS-FRONTIER NECESSARY CONDITION / NON-CIRCULAR / NOVELTY UNVERIFIED.

## 0. Executive theorem

Round 34 proved the exact horizontal Hermite-Parseval identity for

\[
X_{t,\gamma}(y)
:=\xi\!\left(\frac12+\sqrt t\,y+i\gamma\right),
\qquad
d\mu(y)=\pi^{-1/2}e^{-y^2}dy.
\]

If `H_t` has a real zero of multiplicity at least `m` at `x=2 gamma`, then the first `m` Hermite coefficients of `X_{t,gamma}` vanish. The Gaussian Ornstein--Uhlenbeck spectral gap therefore forces a hierarchy of derivative-energy inequalities.

For every integer `q` with `1<=q<=m`,

\[
\boxed{
 t^q
 \int_{\mathbb R}G_t(a)
 \left|\xi^{(q)}\!\left(\frac12+a+i\gamma\right)\right|^2da
 \ge
 2^q\frac{m!}{(m-q)!}
 \int_{\mathbb R}G_t(a)
 \left|\xi\!\left(\frac12+a+i\gamma\right)\right|^2da.
}
\]

In particular,

\[
\boxed{
 t\int G_t(a)|\xi'(1/2+a+i\gamma)|^2da
 \ge 2m\int G_t(a)|\xi(1/2+a+i\gamma)|^2da.
}
\]

Thus a double collision necessarily satisfies

\[
\boxed{
 t\frac{\int G_t|\xi'|^2}{\int G_t|\xi|^2}\ge4.
}
\]

This is an independently meaningful analytic-number-theory target: any unconditional reverse estimate placing the weighted logarithmic-derivative Rayleigh quotient below `2m` excludes multiplicity `m` collisions in that regime.

---

## 1. Hermite expansion and collision constraint

With physicists' Hermite polynomials,

\[
\int H_jH_k\,d\mu=2^kk!\delta_{jk}.
\]

Write

\[
X(y)=\sum_{k=0}^{\infty}c_kH_k(y).
\]

Round 32 gives that multiplicity at least `m` is equivalent to

\[
\boxed{c_0=c_1=\cdots=c_{m-1}=0.}
\]

Hence

\[
\|X\|_{L^2(d\mu)}^2
=\sum_{k=m}^{\infty}|c_k|^22^kk!.
\]

---

## 2. First derivative energy

The Hermite derivative identity is

\[
H_k'(y)=2kH_{k-1}(y).
\]

Therefore

\[
\begin{aligned}
\|X'\|^2
&=\sum_{k\ge m}|c_k|^2(2k)^2
\|H_{k-1}\|^2\\
&=\sum_{k\ge m}|c_k|^2(2k)^2
2^{k-1}(k-1)!\\
&=\sum_{k\ge m}2k\,|c_k|^22^kk!.
\end{aligned}
\]

Since `k>=m`,

\[
\boxed{\|X'\|^2\ge2m\|X\|^2.}
\]

This is precisely the Gaussian spectral gap on the orthogonal complement of the first `m` Hermite modes.

Because

\[
X'(y)=\sqrt t\,\xi'\!\left(\frac12+\sqrt t\,y+i\gamma\right),
\]

and `dmu=G_t(a)da`, we obtain

\[
\boxed{
 t\int_{\mathbb R}G_t(a)|\xi'(1/2+a+i\gamma)|^2da
 \ge
 2m\int_{\mathbb R}G_t(a)|\xi(1/2+a+i\gamma)|^2da.
}
\]

---

## 3. Higher derivative hierarchy

For `q<=k`,

\[
\frac{d^q}{dy^q}H_k(y)
=2^q\frac{k!}{(k-q)!}H_{k-q}(y).
\]

Thus the contribution of mode `k` to `\|X^{(q)}\|^2` is

\[
|c_k|^2
\left(2^q\frac{k!}{(k-q)!}\right)^2
2^{k-q}(k-q)!.
\]

Relative to its contribution

\[
|c_k|^22^kk!
\]

to `\|X\|^2`, the factor is exactly

\[
\boxed{
2^q\frac{k!}{(k-q)!}.
}
\]

For `k>=m>=q`, this is minimized at `k=m`. Hence

\[
\boxed{
\|X^{(q)}\|^2
\ge
2^q\frac{m!}{(m-q)!}\|X\|^2.
}
\]

Since

\[
X^{(q)}(y)
=t^{q/2}\xi^{(q)}(1/2+\sqrt t\,y+i\gamma),
\]

we get the announced horizontal inequality

\[
\boxed{
 t^q\int G_t|\xi^{(q)}|^2
\ge
2^q\frac{m!}{(m-q)!}\int G_t|\xi|^2.
}
\]

---

## 4. Double-collision thresholds

For `m=2`, the first two inequalities are

\[
\boxed{
 t\int G_t|\xi'|^2
\ge4\int G_t|\xi|^2,
}
\]

and

\[
\boxed{
 t^2\int G_t|\xi''|^2
\ge8\int G_t|\xi|^2.
}
\]

Thus either inequality can be used as a no-collision test: if at a given `(t,gamma)` one proves

\[
t\int G_t|\xi'|^2<4\int G_t|\xi|^2,
\]

or

\[
t^2\int G_t|\xi''|^2<8\int G_t|\xi|^2,
\]

then a double collision is impossible there.

---

## 5. Exact Rayleigh quotient formulation

Define

\[
\mathcal R_{1,t}(\gamma)
:=
 t\frac{\int G_t(a)|\xi'(1/2+a+i\gamma)|^2da}
 {\int G_t(a)|\xi(1/2+a+i\gamma)|^2da}.
\]

The denominator is strictly positive because xi is not identically zero on a horizontal line.

Then

\[
\boxed{
\text{multiplicity at least }m
\Longrightarrow
\mathcal R_{1,t}(\gamma)\ge2m.
}
\]

In particular,

\[
\boxed{
\mathcal R_{1,t}(\gamma)<4
\Longrightarrow
\text{no collision at }(t,2\gamma).
}
\]

This is a scalar positive observable rather than a signed phase or Laguerre quantity.

---

## 6. Relation to the Ornstein--Uhlenbeck operator

Let

\[
\mathcal L=-\partial_y^2+2y\partial_y.
\]

Then

\[
\mathcal LH_k=2kH_k.
\]

Integration by parts in Gaussian space gives

\[
\langle X,\mathcal LX\rangle=\|X'\|^2.
\]

Therefore the collision condition places `X` in the spectral subspace

\[
\operatorname{spec}(\mathcal L)\subset[2m,\infty),
\]

and the first derivative inequality is simply the min--max principle

\[
\frac{\langle X,\mathcal LX\rangle}{\|X\|^2}\ge2m.
\]

This operator interpretation may be useful for importing functional inequalities or semigroup estimates that are independent of zero locations.

---

## 7. Heuristic scale and rigorous warning

For large `gamma`, the archimedean factor in `xi` suggests a horizontal logarithmic derivative of natural size `~(1/2)log gamma`, so one might heuristically expect

\[
\mathcal R_{1,t}(\gamma)
\sim \frac t4\log^2\gamma
\]

away from exceptional zeta behavior.

If this heuristic could be made into a suitable upper bound, the collision condition `R>=4` would force roughly

\[
\log\gamma\gtrsim\frac4{\sqrt t},
\]

which is qualitatively different from the `exp(C/t)` high-height scale in the unconditional Polymath zero-location theorem.

**This is only a heuristic at present.** The zeta logarithmic derivative may be large near zeros and no such upper bound is claimed without proof.

---

## 8. Why standard pointwise log-derivative estimates are not enough automatically

The quotient involves

\[
\int G_t|\xi'|^2
\]

and

\[
\int G_t|\xi|^2,
\]

not a pointwise supremum of `|xi'/xi|`. Near a zero, the pointwise ratio is singular while the weighted numerator and denominator remain finite.

Thus a useful analytic-number-theory estimate should control the **weighted derivative norm directly**, or control `xi'/xi` after splitting neighborhoods of zeros in a way that does not assume the desired zero-free region.

---

## 9. Next rigorous target

The smallest quantitative cross-frontier problem is:

> Prove an unconditional upper estimate for
> \[
> \mathcal R_{1,t}(\gamma)
> \]
> in some explicit positive-time/high-ordinate regime, using the gamma factor, the functional equation, and RH-free estimates for zeta/Dirichlet polynomials.

Any regime in which the upper bound is `<4` gives a new no-double-collision region.

A useful first step may be to decompose

\[
\frac{\xi'}{\xi}(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\frac{\Gamma'}{\Gamma}(s/2)
+\frac{\zeta'}{\zeta}(s),
\]

but the final estimate must be formulated in a way that remains integrable through zeta zeros and does not assume a zero-free horizontal tube.

---

## 10. Circularity audit

Used:

- Round-32/34 exact Hermite identities;
- Gaussian Hermite spectral theory;
- elementary min--max/Parseval.

Not used:

- RH or `Lambda<=0`;
- real-rootedness of the unknown heat slice;
- Laguerre inequalities;
- zero-gap bounds;
- zero-free assumptions near the horizontal Gaussian window.

---

## 11. Status

- Gaussian first-derivative collision spectral gap: **PROVED**;
- full `q`-derivative hierarchy: **PROVED**;
- double-collision Rayleigh threshold `R>=4`: **PROVED**;
- unconditional analytic-number-theory upper bound `R<4` in a new regime: **OPEN**;
- heuristic collision-height scale `exp(C/sqrt(t))`: **HEURISTIC ONLY**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
