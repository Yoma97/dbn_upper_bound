# Round 30 — Raw theta-mode diagonal decomposition diverges and cannot be the positive main term

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / STRUCTURAL NO-GO / SOURCE-GROUNDED / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 29 reduced the first associated-kernel problem to a single spectral-curvature defect and suggested exploiting the explicit theta-series structure of the Riemann kernel. The most immediate attempt is to expand the Riemann kernel into its classical theta modes and split the resulting associated kernel into a diagonal part `n=m` plus an off-diagonal part `n!=m`, hoping for

\[
\text{positive diagonal main term} - \text{controlled off-diagonal defect}.
\]

This round proves that this raw decomposition is not legitimate: the diagonal part is not even finite.

Write the classical mode decomposition used by Csordas

\[
\Phi(u)=\sum_{n\ge1} a_n(u),
\]

with

\[
\boxed{
a_n(u)
=\pi n^2\bigl(2\pi n^2e^{4u}-3\bigr)
\exp\bigl(5u-\pi n^2e^{4u}\bigr).
}
\]

For every fixed real `u` this series converges absolutely, and the sum is the even Jacobi-theta kernel. However, the individual modes are translated copies with only `n^{-1/2}`-scale mass. Consequently:

1. the bilateral Fourier transform of a single mode is explicit,
   \[
   \boxed{
   \widehat a_n(\xi)
   =-
   \frac18(\pi n^2)^{-1/4+i\xi/4}
   (1+i\xi)
   \Gamma\!\left(\frac54-\frac{i\xi}{4}\right);
   }
   \]
2. hence
   \[
   |\widehat a_n(\xi)|\asymp_\xi n^{-1/2},
   \]
   so `sum_n |hat a_n(xi)|` diverges for every fixed real `xi`;
3. at the associated-kernel level, the diagonal contribution at the origin satisfies
   \[
   \int_{\mathbb R}s^2a_n(s)^2\,ds
   \asymp
   \frac{(\log n)^2}{n},
   \]
   and therefore
   \[
   \boxed{
   \sum_{n\ge1}\int_{\mathbb R}s^2a_n(s)^2\,ds=+\infty.
   }
   \]

But the true Riemann associated kernel

\[
K_1(0)=\int_{\mathbb R}s^2\Phi(s)^2\,ds
\]

is finite by the super-exponential decay of `Phi`.

Therefore finiteness itself depends on essential cancellation between distinct theta modes. A raw diagonal/off-diagonal split cannot furnish a finite positive main term plus a perturbative remainder.

Any useful theta/Poisson decomposition must first perform a modular/Poisson resummation or another renormalization that makes the pieces individually finite. Only after that may one ask for positive definiteness or domination.

---

## 1. Source fence

Csordas records the theta-kernel representation

\[
\Phi(u)=\sum_{n=1}^\infty
\pi n^2(2\pi n^2e^{4u}-3)
\exp(5u-\pi n^2e^{4u}),
\]

and proves that the total function `Phi` is an even admissible kernel. The same paper proves that the associated kernels

\[
K_j(r)=\int_{\mathbb R}\Phi(s+r)\Phi(s-r)s^{2j}\,ds
\]

are admissible, and identifies positive definiteness of `K_1` with the first Laguerre inequality. It explicitly states the positive-definiteness problem for `K_1` as difficult/open.

The calculations below use only the displayed mode formula and elementary Gamma integrals. No RH, no real-zero hypothesis, and no de Bruijn--Newman estimate is used.

---

## 2. Every theta mode is a translated universal profile — PROVED

Set

\[
c_n:=\pi n^2.
\]

Define

\[
A(v):=(2e^{4v}-3)e^{5v-e^{4v}}.
\]

With

\[
v=u+\frac14\log c_n,
\]

one has

\[
c_ne^{4u}=e^{4v}
\]

and

\[
e^{5u}=c_n^{-5/4}e^{5v}.
\]

Thus exactly

\[
\boxed{
a_n(u)=c_n^{-1/4}
A\!\left(u+\frac14\log c_n\right).
}
\]

Hence the modes do not become narrower with `n`; they translate toward negative `u` while their amplitude decreases only as

\[
c_n^{-1/4}=\pi^{-1/4}n^{-1/2}.
\]

This slow amplitude decay is the origin of the non-summability below.

---

## 3. Exact Fourier transform of one mode — PROVED

Use the bilateral Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(u)e^{-i\xi u}\,du.
\]

Starting from `a_n`, make the substitution

\[
y=c_ne^{4u},
\qquad
u=\frac14(\log y-\log c_n),
\qquad
du=\frac{dy}{4y}.
\]

Then

\[
\begin{aligned}
\widehat a_n(\xi)
&=
\frac14c_n^{-1/4+i\xi/4}
\int_0^\infty
(2y-3)y^{1/4-i\xi/4}e^{-y}\,dy.
\end{aligned}
\]

Put

\[
\alpha=\frac54-\frac{i\xi}{4}.
\]

The Gamma recurrence gives

\[
\begin{aligned}
\int_0^\infty
(2y-3)y^{\alpha-1}e^{-y}\,dy
&=2\Gamma(\alpha+1)-3\Gamma(\alpha)\\
&=(2\alpha-3)\Gamma(\alpha)\\
&=-\frac{1+i\xi}{2}\Gamma(\alpha).
\end{aligned}
\]

Therefore

\[
\boxed{
\widehat a_n(\xi)
=-\frac18
c_n^{-1/4+i\xi/4}
(1+i\xi)
\Gamma\!\left(\frac54-\frac{i\xi}{4}\right).
}
\]

For fixed real `xi`, the factor depending on `xi` is finite and nonzero, while

\[
|c_n^{-1/4+i\xi/4}|=c_n^{-1/4}.
\]

Thus

\[
\boxed{
|\widehat a_n(\xi)|
=C(\xi)n^{-1/2},
\qquad C(\xi)>0.
}
\]

Consequently

\[
\boxed{
\sum_{n\ge1}|\widehat a_n(\xi)|=\infty.
}
\]

The formal sum of transforms contains the critical-line Dirichlet series

\[
\sum_{n\ge1}n^{-1/2+i\xi/2},
\]

which is not an ordinarily convergent Dirichlet series. This is the Fourier-side signal that one must not interchange the bilateral `u`-integral with the raw theta-mode sum.

---

## 4. Diagonal associated-kernel mass diverges — PROVED

Consider the formal diagonal contribution to the first associated kernel at `r=0`:

\[
D_n
:=
\int_{\mathbb R}s^2a_n(s)^2\,ds.
\]

Using the translated-profile identity with

\[
\ell_n:=\frac14\log c_n,
\qquad
v=s+\ell_n,
\]

we obtain

\[
D_n
=c_n^{-1/2}
\int_{\mathbb R}(v-\ell_n)^2A(v)^2\,dv.
\]

The profile `A` is rapidly decaying at both ends, so its moments

\[
M_j:=\int_{\mathbb R}v^jA(v)^2\,dv,
\qquad j=0,1,2,
\]

are finite, and

\[
M_0>0.
\]

Thus

\[
D_n
=c_n^{-1/2}
\left(
M_0\ell_n^2-2M_1\ell_n+M_2
\right).
\]

Since

\[
c_n^{-1/2}=\frac1{\sqrt\pi\,n}
\]

and

\[
\ell_n=\frac14\log(\pi n^2)=\frac12\log n+O(1),
\]

we obtain the exact asymptotic

\[
\boxed{
D_n
=
\frac{M_0}{4\sqrt\pi}
\frac{(\log n)^2}{n}
+O\!\left(\frac{\log n}{n}\right).
}
\]

Therefore

\[
\boxed{
\sum_{n=1}^N D_n
\asymp (\log N)^3,
}
\]

and in particular

\[
\boxed{
\sum_{n\ge1}D_n=+\infty.
}
\]

---

## 5. Contrast with the true associated kernel

The total Riemann kernel `Phi` is admissible and super-exponentially decaying. Hence

\[
K_1(0)
=
\int_{\mathbb R}s^2\Phi(s)^2\,ds
<\infty.
\]

If one formally expands

\[
\Phi(s)^2
=
\sum_{n,m\ge1}a_n(s)a_m(s),
\]

the diagonal subseries already has infinite positive mass after multiplication by `s^2` and integration. Thus the double expansion cannot be separated into two absolutely convergent pieces

\[
\sum_n (n=n)
\quad\text{and}\quad
\sum_{n\ne m}(n,m).
\]

The off-diagonal sector must participate in cancellations at the same divergent scale.

Therefore the hoped-for inequality

\[
\text{off-diagonal defect}
=o(\text{diagonal main term})
\]

cannot even be formulated for the raw decomposition: both sectors are individually non-finite.

---

## 6. Positive-time heat tilt makes the raw decomposition worse

For

\[
\psi_t(u)=e^{tu^2}\Phi(u),
\qquad t>0,
\]

a raw mode would be

\[
e^{tu^2}a_n(u).
\]

The center of `a_n` lies at

\[
u\sim-\frac14\log c_n\sim-\frac12\log n.
\]

At that location the heat factor contributes roughly

\[
\exp\!\left(\frac t4(\log n)^2+O_t(\log n)\right),
\]

which overwhelms the original `n^{-1/2}` mode amplitude. The total heat-weighted Riemann kernel remains well defined because the modularly completed theta sum has super-exponential decay, but the individual raw modes become even less summable.

Thus the positive-time problem cannot be attacked by heat-tilting the individual uncompleted theta modes and then summing their positive-definiteness estimates.

---

## 7. Why this does not contradict pointwise theta convergence

For every fixed real `u`, the theta series for `Phi(u)` converges rapidly because

\[
\exp(-\pi n^2e^{4u})
\]

kills large `n`.

The obstruction arises only after integrating over the full real `u`-axis. As `n` grows, the mass of the `n`th mode moves left to

\[
u\asymp-\frac12\log n,
\]

so no fixed integrable majorant controls all modes simultaneously. This is precisely the setting in which pointwise absolute convergence does not justify Fubini/Tonelli interchange over `n` and `u`.

The evenness and rapid decay of the full `Phi` are modular/global properties of the complete theta sum, not properties of each mode separately.

---

## 8. Relation to Csordas' positive-definiteness criterion

Csordas proves that

\[
K_1(r)
=\int_{\mathbb R}\Phi(s+r)\Phi(s-r)s^2\,ds
\]

is admissible and that

\[
L_1(x)
=(H'(x))^2-H(x)H''(x)
=4\int_{\mathbb R}K_1(r)\cos(2xr)\,dr.
\]

He also states the positive definiteness of `K_1` for the Riemann kernel as an open problem and gives an equivalent sine-transform criterion through

\[
G(r)=\int_r^\infty K_1(u)\,du.
\]

Round 30 shows that trying to solve this problem by isolating the raw `n=m` theta terms is structurally invalid before a modular renormalization.

---

## 9. Promotion gate for any future theta decomposition

A theta/Poisson decomposition of `K_1` is admissible for the research program only if each proposed main/error piece is individually finite and the decomposition is justified by absolute convergence or a stated renormalization theorem.

In particular, reject any argument of the form

\[
K_1=\sum_n K_{1,n}^{\rm diag}+\sum_{n\ne m}K_{1,nm}^{\rm off}
\]

if it silently interchanges the full-line `s` integral with the uncompleted theta series.

The next legitimate theta-side operation must first use one of:

1. Poisson/modular pairing of the negative and positive tails;
2. an Ewald-type split with separately convergent primal and dual sums;
3. Mellin regularization with an explicit cancellation theorem;
4. another decomposition whose pieces are individually in `L^1` / positive-definite classes.

Only after such a renormalization can diagonal dominance or a positive-main-minus-defect estimate be meaningfully tested.

---

## 10. Program consequence

The naive theta-diagonal version of the Round-29 target is **REFUTED AS A WELL-DEFINED DECOMPOSITION**.

This does not refute all theta/Poisson approaches. It forces them into their genuinely modular form.

The remaining local-A target is now narrower:

\[
\boxed{
\text{construct a modularly completed, individually finite decomposition of }K_{1,t}
\text{ and obtain a signed spectral-curvature estimate.}
}
\]

If no such decomposition yields a sign advantage, the local kernel route should be frozen and the program should pivot to a cross-frontier collision-amplification mechanism.

---

## 11. Status

- exact single theta-mode Fourier transform: **PROVED**;
- `n^{-1/2}` non-summability of bilateral mode transforms: **PROVED**;
- diagonal `K_1(0)` mass `~ C (log n)^2/n`: **PROVED**;
- divergence of the raw diagonal associated-kernel sum: **PROVED**;
- raw diagonal/off-diagonal split as finite positive-main/error decomposition: **REFUTED**;
- modularly completed theta decomposition with useful sign: **OPEN**;
- RH: **OPEN**;
- novelty of the packaging: **UNVERIFIED**.
