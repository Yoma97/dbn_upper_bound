# Round 33 — Heat-collision multiplicity forces horizontal sign-change amplification of xi

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / CROSS-FRONTIER AMPLIFICATION / NON-CIRCULAR / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 32 proved that an `m`-fold real collision of `H_t` at `x=2 gamma` is equivalent to the vanishing of the first `m` horizontal Gaussian-Hermite coefficients of

\[
X_\gamma(a):=\xi\!\left(\frac12+a+i\gamma\right).
\]

This round converts those moment identities into an actual geometric consequence on the classical xi function.

Let

\[
q_+(m):=\left\lceil\frac m2\right\rceil,
\qquad
q_-(m):=\left\lfloor\frac m2\right\rfloor.
\]

If `H_t` has a real zero of multiplicity at least `m>=2` at `x=2 gamma` with `gamma>0`, then, on the horizontal half-line `a>0`,

\[
\boxed{
\Re\xi(1/2+a+i\gamma)
\text{ has at least }q_+(m)\text{ sign changes},
}
\]

and

\[
\boxed{
\Im\xi(1/2+a+i\gamma)
\text{ has at least }q_-(m)\text{ sign changes}.
}
\]

Thus a heat-flow collision cannot be horizontally invisible: it forces an alternating sequence of real-axis and imaginary-axis crossings of the classical xi curve at the same ordinate.

For a double collision (`m=2`) this gives at least one sign change of each component. For `m=4` it gives at least two sign changes of each component, etc.

This does not yet force an actual off-critical zero, because the real and imaginary crossings need not occur at the same horizontal location. It is nevertheless a genuine sparse-defect amplification statement derived without RH or Laguerre positivity.

---

## 1. Input from Round 32

Let

\[
G_t(a)=\frac1{\sqrt{\pi t}}e^{-a^2/t}
\]

and let `H_k` be the physicists' Hermite polynomial.

At a multiplicity-`m` collision at `x=2 gamma`, Round 32 gives

\[
\int_{\mathbb R}
G_t(a)H_k(a/\sqrt t)
X_\gamma(a)\,da=0,
\qquad 0\le k<m.
\]

The functional equation and conjugation symmetry give

\[
X_\gamma(-a)=\overline{X_\gamma(a)}.
\]

Hence

\[
R_\gamma(a):=\Re X_\gamma(a)
\]

is even and

\[
I_\gamma(a):=\Im X_\gamma(a)
\]

is odd.

---

## 2. Even Hermite moments constrain the real part

For even index `k=2j`, the polynomial `H_{2j}` is even. Therefore the imaginary part of the full-line integral is odd and vanishes automatically, while the real part gives

\[
\boxed{
\int_0^\infty
G_t(a)
H_{2j}(a/\sqrt t)
R_\gamma(a)\,da=0
}
\]

for every

\[
0\le j<q_+(m).
\]

The polynomial `H_{2j}(y)` is a polynomial of degree `j` in `y^2` with nonzero leading coefficient. Thus

\[
\{H_0(a/\sqrt t),H_2(a/\sqrt t),\ldots,H_{2(q_+-1)}(a/\sqrt t)\}
\]

spans exactly the polynomials in `a^2` of degree at most `q_+-1`.

Consequently

\[
\boxed{
\int_0^\infty
G_t(a)P(a^2)R_\gamma(a)\,da=0
}
\]

for every real polynomial `P` of degree `<q_+`.

---

## 3. Odd Hermite moments constrain the imaginary part

For odd index `k=2j+1`, `H_{2j+1}` is odd and has the factorization

\[
H_{2j+1}(y)=yQ_j(y^2),
\]

where `Q_j` is a polynomial of degree `j` with nonzero leading coefficient.

The real part of the full-line moment is odd and vanishes automatically. The imaginary part yields

\[
\boxed{
\int_0^\infty
G_t(a)
H_{2j+1}(a/\sqrt t)
I_\gamma(a)\,da=0
}
\]

for

\[
0\le j<q_-(m).
\]

Equivalently, because `H_{2j+1}(a/\sqrt t)=a` times a nonzero polynomial in `a^2`, the conditions span

\[
\boxed{
\int_0^\infty
G_t(a)aP(a^2)I_\gamma(a)\,da=0
}
\]

for every polynomial `P` of degree `<q_-`.

---

## 4. Moment-orthogonality sign-change lemma

We use the following elementary Chebyshev-system fact.

### Lemma

Let `mu` be a positive measure on `(0,infinity)` assigning positive mass to every nonempty open interval, and let `f` be continuous, not identically zero. If

\[
\int_0^\infty r^j f(r)\,d\mu(r)=0,
\qquad j=0,1,\ldots,N-1,
\]

with all integrals convergent, then `f` has at least `N` sign changes on `(0,infinity)`.

### Proof

Assume instead that `f` has at most `N-1` sign changes, at points

\[
0<r_1<\cdots<r_q,
\qquad q\le N-1.
\]

Choose the polynomial

\[
P(r)=\pm\prod_{j=1}^q(r-r_j)
\]

with the overall sign selected so that

\[
P(r)f(r)\ge0
\]

throughout `(0,infinity)`. Because `f` is not identically zero and `mu` is positive on open intervals,

\[
\int P(r)f(r)\,d\mu(r)>0.
\]

But `deg P=q<=N-1`, contradicting the assumed orthogonality to all polynomials of degree `<N`. ∎

---

## 5. Application to the real part

In Section 2, substitute

\[
r=a^2.
\]

Since

\[
da=\frac{dr}{2\sqrt r},
\]

the moment conditions become

\[
\int_0^\infty
P(r)
R_\gamma(\sqrt r)
\frac{G_t(\sqrt r)}{2\sqrt r}\,dr=0
\]

for all `deg P<q_+`.

The measure

\[
d\mu_+(r)
:=\frac{G_t(\sqrt r)}{2\sqrt r}\,dr
\]

is strictly positive on `(0,infinity)`.

Therefore the sign-change lemma gives at least `q_+` sign changes of

\[
R_\gamma(\sqrt r)
\]

as `r` increases, equivalently of

\[
\boxed{R_\gamma(a)=\Re\xi(1/2+a+i\gamma)}
\]

on `a>0`.

---

## 6. Application to the imaginary part

For the odd moments, again put `r=a^2`. Since

\[
a\,da=\frac12dr,
\]

the conditions become

\[
\int_0^\infty
P(r)
I_\gamma(\sqrt r)
\frac{G_t(\sqrt r)}2\,dr=0
\]

for all `deg P<q_-`.

The measure

\[
d\mu_-(r)
:=\frac{G_t(\sqrt r)}2\,dr
\]

is strictly positive. Hence

\[
\boxed{I_\gamma(a)=\Im\xi(1/2+a+i\gamma)}
\]

has at least `q_-` sign changes on `a>0`.

---

## 7. Nontriviality of the horizontal components

For `gamma>0`, neither horizontal component can vanish identically on an interval unless xi acquires an impossible horizontal-line symmetry.

Indeed, if `Im X_gamma(a)=0` for all real `a` in an interval, analyticity and Schwarz reflection would imply a translated conjugation symmetry for xi. Combined with the usual real-entire symmetry this would force a nontrivial imaginary period `2i gamma`, incompatible with the standard growth/asymptotic behavior of the completed zeta function.

Thus the sign-change lemma applies nontrivially at every positive ordinate relevant to a collision. Also `gamma=0` cannot host a collision because the positive Riemann kernel gives `H_t(0)>0` for real `t` in the relevant positive-time range.

---

## 8. Concrete multiplicities

### `m=2`

\[
q_+=1,\qquad q_-=1.
\]

A double collision forces at least one sign change of `Re xi` and at least one sign change of `Im xi` as `sigma=1/2+a` moves right from the critical line.

### `m=3`

\[
q_+=2,\qquad q_-=1.
\]

The real part must change sign at least twice; the imaginary part at least once.

### `m=4`

\[
q_+=2,\qquad q_-=2.
\]

Both horizontal components must undergo at least two sign changes.

In general, the total forced component sign-change count is at least

\[
q_++q_-=m.
\]

---

## 9. Relation to local degree

Round 19 gives local collision degree

\[
\deg_{\rm loc}(H_t,H_t')=-\lfloor m/2\rfloor.
\]

Round 33 supplies a different but compatible measure of complexity: the same multiplicity forces

\[
\lceil m/2\rceil
\]

real-part horizontal sign changes and

\[
\lfloor m/2\rfloor
\]

imaginary-part horizontal sign changes.

Thus the topological local charge has an exact horizontal-oscillation counterpart in the classical completed zeta function.

This relationship is structural; no claim of novelty in the literature is made without a dedicated search.

---

## 10. What this does and does not prove

It **does prove** that a positive-time collision creates a finite horizontal oscillation signature at a single ordinate of xi.

It **does not prove** that one of the crossings is an actual xi zero. The zeros of the real and imaginary parts may occur at distinct horizontal coordinates.

It also does not yet bound how far to the right the required sign changes occur. Because the Gaussian moments can in principle be balanced by a distant tail, a quantitative localization theorem is still needed.

---

## 11. Smallest next quantitative target

The next bridge lemma should localize the forced sign changes.

A useful form would be:

> If the first `N` Gaussian-Hermite moments vanish, then at least one of the forced sign changes occurs in `0<a<=A(t,gamma)`, where `A` is explicit and small enough that unconditional estimates for `xi(sigma+i gamma)` control the horizontal phase/sign behavior there.

To prove such a statement one needs an independent tail bound comparing

\[
\int_A^\infty G_t(a)|X_\gamma(a)|\,da
\]

with the interior weighted mass. A mere Gaussian tail estimate is insufficient unless combined with a rigorous horizontal growth bound for xi.

This is now the preferred cross-frontier target.

---

## 12. Circularity audit

Used:

- exact Round-32 Gaussian-Hermite collision identities;
- functional equation/conjugation symmetry;
- elementary polynomial moment/sign-change theory.

Not used:

- RH or `Lambda<=0`;
- any real-rootedness assertion at the unknown time;
- Laguerre positivity;
- zero-gap assumptions;
- Rodgers--Tao contradiction-regime estimates.

---

## 13. Status

- even/odd Hermite moment separation: **PROVED**;
- moment orthogonality implies sign changes: **PROVED**;
- `m`-fold collision forces `ceil(m/2)` real-part sign changes: **PROVED**;
- `m`-fold collision forces `floor(m/2)` imaginary-part sign changes: **PROVED**;
- localization of those sign changes to a controlled horizontal strip: **OPEN**;
- conversion of separate component crossings into an actual off-critical xi zero: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
