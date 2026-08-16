# Round 55 — Mellin diagonalization of the triangular prime weight and the zero-resolvent barrier

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED EXACT TRANSFORM / STRUCTURAL REDUCTION / CIRCULARITY BARRIER / NEW QUADRATIC TOOL TARGET / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 54 identified the long-range obstruction as cancellation in

\[
P_x(t)-I_x(t),
\]

where the prime polynomial uses the triangular multiplicative weight

\[
W(y)=\min(y,y^{-1}).
\]

This round shows that this weight is not merely convenient: it is **exactly diagonalized by Mellin transform**.

For

\[
P_x(t)=\sum_{n\ge1}\frac{\Lambda(n)}{n^{1/2+it}}W(n/x),
\]

one has, in the common domain `1/2<Re z<1`,

\[
\boxed{
\int_0^\infty x^{-z-1}P_x(t)\,dx
=-\frac{2}{1-z^2}
\frac{\zeta'}{\zeta}\!\left(\frac12+it+z\right).}
\]

The pole-prime cancellation of Round 54 is therefore the inverse-Mellin manifestation of the pole of `zeta` at `s=1`. After that pole is subtracted, the next Mellin singularities occur exactly at

\[
\boxed{
z=\rho-\left(\frac12+it\right),}
\]

with real parts `beta-1/2`.

Thus horizontal zero displacement is literally a Mellin singularity abscissa for the centered prime transform.

This gives a very clean resolvent formulation of the sparse-exception problem, but also a severe circularity warning: proving linear analytic continuation of the pole-subtracted transform throughout `Re z>0` is essentially zero-freeness of `zeta` there. The new mathematics cannot be merely a better contour shift. It must use the **quadratic/mean-square arithmetic structure** before analytic continuation is invoked.

---

## 1. The triangular multiplicative kernel

Define

\[
W(y):=\min(y,y^{-1}),\qquad y>0.
\]

Then

\[
W(y)=
\begin{cases}
y,&0<y\le1,\\
y^{-1},&y\ge1.
\end{cases}
\]

It is invariant under inversion:

\[
\boxed{W(y)=W(1/y).}
\]

This is exactly the weight appearing in the RH-free Montgomery explicit formula used in Rounds 49 and 54.

---

## 2. Exact Mellin transform of `W`

For `-1<Re z<1`,

\[
\begin{aligned}
\mathcal MW(z)
&:=\int_0^\infty y^{-z-1}W(y)\,dy\\
&=\int_0^1y^{-z}\,dy
+\int_1^\infty y^{-z-2}\,dy\\
&=\frac1{1-z}+\frac1{1+z}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal MW(z)=\frac{2}{1-z^2}.}
\]

The poles at `z=+-1` encode the two linear pieces of the triangular weight.

---

## 3. Mellin transform of one prime mode

For every integer `n>=1`, substitute `x=ny`. Since `W(n/x)=W(1/y)=W(y)`,

\[
\begin{aligned}
\int_0^\infty x^{-z-1}W(n/x)\,dx
&=n^{-z}\int_0^\infty y^{-z-1}W(y)\,dy\\
&=\boxed{\frac{2n^{-z}}{1-z^2}}.
\end{aligned}
\]

This identity is exact for `-1<Re z<1`.

---

## 4. Exact prime-polynomial transform

Recall

\[
P_x(t)
=\sum_{n\ge1}
\frac{\Lambda(n)}{n^{1/2+it}}W(n/x).
\]

For

\[
\frac12<\Re z<1,
\]

the Dirichlet series

\[
\sum_{n\ge1}\frac{\Lambda(n)}{n^{1/2+it+z}}
\]

converges absolutely and equals

\[
-\frac{\zeta'}{\zeta}\!\left(\frac12+it+z\right).
\]

Therefore Fubini is justified and gives

\[
\boxed{
\int_0^\infty x^{-z-1}P_x(t)\,dx
=-\frac{2}{1-z^2}
\frac{\zeta'}{\zeta}\!\left(\frac12+it+z\right).}
\]

This is the exact Mellin linearization of the prime side.

---

## 5. Pole term as the first Mellin singularity

The logarithmic derivative has the local expansion near the pole `s=1`:

\[
\frac{\zeta'}{\zeta}(s)
=-\frac1{s-1}+O(1).
\]

With

\[
s=\frac12+it+z,
\]

the corresponding Mellin pole lies at

\[
\boxed{z_p=\frac12-it.}
\]

Thus

\[
-\frac{2}{1-z^2}\frac{\zeta'}{\zeta}\left(\frac12+it+z\right)
\]

has principal part

\[
\frac{2}{1-z_p^2}\frac1{z-z_p}.
\]

When the inverse Mellin contour is moved across this pole, its residue produces exactly the continuous/PNT main term identified in Round 54:

\[
I_x(t)
=x^{1/2-it}
\left(
\frac1{3/2-it}+\frac1{1/2+it}
\right).
\]

Indeed

\[
\frac{2}{1-z_p^2}
=
\frac1{3/2-it}+\frac1{1/2+it}.
\]

Hence

\[
\boxed{
\text{Round-54 pole--prime cancellation}
=\text{ordinary Mellin residue subtraction}.}
\]

---

## 6. Non-trivial zeros are the next resolvent singularities

If

\[
\rho=\beta+i\gamma
\]

is a non-trivial zero of multiplicity `m`, then

\[
\frac{\zeta'}{\zeta}(s)
=\frac{m}{s-\rho}+O(1).
\]

Therefore the Mellin transform has a pole at

\[
\boxed{
z_\rho
=\rho-\left(\frac12+it\right)
=\left(\beta-\frac12\right)+i(\gamma-t).}
\]

Its real part is exactly the horizontal displacement

\[
\boxed{
\Re z_\rho=\beta-\frac12.}
\]

Thus the rightmost nontrivial zero controls the rightmost post-pole singularity of the centered Mellin transform.

This is the linear-resolvent counterpart of Round 53's pair-correlation growth-exponent formula.

---

## 7. A regularized centered transform

Let

\[
z_p=\frac12-it.
\]

Define the pole-subtracted meromorphic function

\[
\boxed{
\mathfrak E_t(z)
:=-\frac{2}{1-z^2}
\left(
\frac{\zeta'}{\zeta}\!\left(\frac12+it+z\right)
+\frac1{z-z_p}
\right).}
\]

The singularity corresponding to the pole of `zeta` is removed. The remaining singularities in the critical-strip range are precisely the nontrivial zeros, together with known trivial/gamma-side singularities farther left.

Schematically, `mathfrak E_t` is the Mellin transform of `P_x-I_x` after a standard choice of one-sided/regularized inverse-Mellin convention.

The exact convention at `x=0` and `x=infinity` is not important for the structural conclusion below; any admissible regularization must preserve the nontrivial-zero poles.

---

## 8. Circularity barrier

Suppose one attempted to prove directly that `mathfrak E_t(z)` is holomorphic throughout

\[
\Re z>0
\]

for every real `t`.

By the pole formula above, this would exclude every zero with

\[
\beta>\frac12.
\]

The functional equation would then exclude zeros with `beta<1/2`, proving RH.

Therefore

\[
\boxed{
\text{linear analytic continuation of the centered transform to Re z>0}
\text{ is RH-strength}.}
\]

It is not a new independent lemma merely because it is written on the prime side.

Any proof of such continuation must expose an arithmetic mechanism strictly stronger than formal Mellin inversion but not equivalent by assumption to zero-freeness.

---

## 9. Why the quadratic level is different

The pair-correlation statistic is not the linear transform `mathfrak E_t`; it is a positive mean square built from the same prime/zero resolvent.

Quadratic averaging introduces information unavailable to a pointwise meromorphic continuation argument:

- orthogonality in the vertical parameter `t`;
- bilinear correlations of `Lambda(m)Lambda(n)`;
- positivity of a Gram norm;
- the possibility of proving estimates from average arithmetic cancellation rather than pointwise zero-freeness.

Thus the legitimate new target is not

\[
\mathfrak E_t(z)\text{ holomorphic in Re z>0},
\]

but a theorem controlling a **quadratic Mellin/Dirichlet series** built from `|E_x(t)|^2` or its centered variant.

---

## 10. Mellin kernel for the quadratic prime weight

The same triangular weight can be diagonalized partially at the quadratic level.

For positive integers `m<=n`, set

\[
r:=\frac mn\in(0,1].
\]

For `-2<Re z<2`, split the `x`-integral at `m` and `n` to obtain

\[
\begin{aligned}
&\int_0^\infty x^{-z-1}W(m/x)W(n/x)\,dx\\
&\quad=n^{-z}
\left[
\frac{r^{1-z}}{2-z}
+\frac{r^{1-z}-r}{z}
+\frac{r}{z+2}
\right].
\end{aligned}
\]

The apparent singularity at `z=0` is removable, with middle term tending to `-r log r`.

By symmetry the formula for `m>n` is obtained by interchanging the variables.

Hence Mellin transforming the quadratic prime mean produces an explicit two-variable Dirichlet kernel depending on the ratio `m/n`.

This is the concrete object on which new arithmetic cancellation has to act.

---

## 11. New mathematical tool target: QMR

### Quadratic Mellin Resolvent theorem

Construct and control a two-variable Dirichlet series / quadratic form obtained from

\[
\int_0^T|E_x(t)|^2dt
\]

and Mellin transformation in `x`, with the following properties:

1. its initial domain follows from absolute convergence and present mean-value estimates;
2. it admits continuation/boundary control into a larger half-plane by **averaged arithmetic cancellation**, not by assuming zero-freeness;
3. the continuation yields a growth bound for long-range `F(x,T)` strong enough to combine with Round 53;
4. the proof uses only established or newly proved prime-correlation estimates, with no hidden RH-equivalent pointwise PNT assumption.

Possible realizations include:

- a shifted-prime-correlation double Dirichlet series;
- a dispersion-type bilinear form in `Lambda`;
- a spectral decomposition of the ratio kernel above;
- a Selberg-integral transform that controls the same quadratic Mellin object.

---

## 12. Program decision

- Triangular weight Mellin diagonalization: **PROVED EXACTLY**.
- Round-54 `I_x` term: **IDENTIFIED AS THE ZETA-POLE RESIDUE**.
- Horizontal zero displacement: **IDENTIFIED AS THE REAL PART OF THE NEXT MELLIN RESOLVENT POLE**.
- Linear continuation into `Re z>0`: **REJECTED AS RH-EQUIVALENT TARGET unless an independent arithmetic mechanism is supplied**.
- Quadratic/mean-square Mellin continuation: **LEGITIMATE NEW TOOL TARGET**.

The next round should compare this QMR target with the Selberg integral for primes in short intervals. The key question is whether currently proved short-interval variance bounds already control a nontrivial region of the quadratic Mellin resolvent, or whether a genuinely new averaged prime-pair theorem is unavoidable.

**No proof of RH is claimed. Novelty remains unverified.**