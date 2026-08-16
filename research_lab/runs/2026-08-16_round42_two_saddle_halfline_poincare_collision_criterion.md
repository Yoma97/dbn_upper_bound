# Round 42 — Two-saddle gauge and a half-line Poincare collision criterion

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / TWO-SADDLE RENORMALIZATION / ALL-MULTIPLICITY NECESSARY CONDITION / NOVELTY UNVERIFIED.

## 0. Executive theorem

Round 41 showed that a constant coherent displacement cannot cancel the two reflected Archimedean lobes of `xi`. This round introduces the symmetric two-saddle gauge

\[
\boxed{
g_c(a):=e^{-c|a|}\xi\!\left(\frac12+a+i\gamma\right),\qquad c>0,}
\]

with positive even weight

\[
\boxed{W_{c,t}(a):=G_t(a)e^{c|a|}.}
\]

Because

\[
W_{c,t}(a)g_c(a)=G_t(a)\xi(1/2+a+i\gamma),
\]

the first two collision moments are unchanged exactly.

If `H_t` has a multiple zero of **any multiplicity at least two** at `x=2 gamma`, then

\[
\int_{\mathbb R}W_{c,t}g_c=0,
\qquad
\int_{\mathbb R}W_{c,t}a g_c=0.
\]

Using the functional-equation reflection, these become separate half-line constraints on the real and imaginary parts. A strongly log-concave half-line Gaussian Poincare inequality then yields the explicit collision necessary condition

\[
\boxed{
\mathcal Q_{c,t}(\gamma)
:=t\frac{\int_{\mathbb R}G_t(a)e^{-c|a|}
\left|\xi'(s(a))-c\,\operatorname{sgn}(a)\xi(s(a))\right|^2\,da}
{\int_{\mathbb R}G_t(a)e^{-c|a|}|\xi(s(a))|^2\,da}
\ge
\frac{2}{1+2/(c^2t)}.
}
\]

Thus if for some `c>0`

\[
\mathcal Q_{c,t}(\gamma)
<\frac{2}{1+2/(c^2t)},
\]

then `H_t` cannot have a multiple zero at `x=2 gamma`.

As `c^2 t -> infinity`, the threshold tends to `2`, while the gauge removes opposite real exponential slopes on the two half-lines. This is the first positive two-saddle renormalization in the program that survives the interface audit.

---

## 1. Collision moments survive the two-saddle gauge exactly

Let

\[
f(a):=\xi\!\left(\frac12+a+i\gamma\right).
\]

A multiple zero of `H_t` at `x=2 gamma` implies, from Round 32,

\[
\int_{\mathbb R}G_t(a)f(a)\,da=0
\]

and

\[
\int_{\mathbb R}G_t(a)a f(a)\,da=0.
\]

(The second identity differs from the first Hermite moment only by a nonzero scalar.)

For `c>0`, define

\[
g_c(a)=e^{-c|a|}f(a),
\qquad
W_{c,t}(a)=G_t(a)e^{c|a|}.
\]

Then pointwise

\[
W_{c,t}g_c=G_tf.
\]

Hence exactly

\[
\boxed{
\int W_{c,t}g_c=0,
\qquad
\int W_{c,t}a g_c=0.
}
\]

No contour shift and no approximation is used.

For multiplicity `m>2`, the same two equations remain necessary because the first two Hermite moments are among the vanishing moments. Therefore everything below excludes **all** real multiplicities at once.

---

## 2. Reflection splits the two constraints

The functional equation gives

\[
f(-a)=\overline{f(a)}.
\]

Since the gauge is real and even,

\[
\boxed{g_c(-a)=\overline{g_c(a)}.}
\]

Write on `a>=0`

\[
g_c(a)=U(a)+iV(a),
\]

with real `U,V`. The reflection says that the full-line real part is even and the imaginary part is odd. In particular

\[
V(0)=0.
\]

Because `W_{c,t}` is even,

\[
\int_{\mathbb R}W_{c,t}g_c
=2\int_0^\infty W_{c,t}(a)U(a)\,da.
\]

Thus the zeroth collision moment is equivalent to

\[
\boxed{
\int_0^\infty W_{c,t}U=0.
}
\]

Similarly

\[
\int_{\mathbb R}W_{c,t}a g_c
=2i\int_0^\infty W_{c,t}(a)aV(a)\,da,
\]

so the first collision moment is equivalent to

\[
\boxed{
\int_0^\infty W_{c,t}(a)aV(a)\,da=0.
}
\]

The collision therefore gives one coercive constraint for each real component.

---

## 3. The positive-half weight is an exact shifted Gaussian

For `a>0`,

\[
W_{c,t}(a)
=\frac1{\sqrt{\pi t}}\exp\!\left(-\frac{a^2}{t}+ca\right).
\]

Complete the square:

\[
-\frac{a^2}{t}+ca
=-\frac{(a-h)^2}{t}+\frac{c^2t}{4},
\]

where

\[
\boxed{h:=\frac{ct}{2}.}
\]

Thus, after normalization on `[0,infinity)`, the half-line probability density is a Gaussian of variance `t/2` centered at `h`, truncated only at the convex boundary `a=0`.

Its potential

\[
\mathcal V(a)=\frac{(a-h)^2}{t}
\]

has

\[
\mathcal V''(a)=\frac2t.
\]

Therefore the one-dimensional Brascamp--Lieb/Bakry--Emery Poincare inequality on the convex half-line gives

\[
\boxed{
\operatorname{Var}_\nu(F)
\le\frac t2\int_0^\infty |F'(a)|^2\,d\nu(a),
}
\]

where `nu` is the normalized half-line measure proportional to `W_{c,t}(a) da`.

Only this standard strong-convexity inequality is used below.

---

## 4. Real component — direct Poincare coercivity

The collision condition gives

\[
\mathbb E_\nu U=0.
\]

Hence

\[
\mathbb E_\nu U^2
=\operatorname{Var}_\nu(U)
\le\frac t2\mathbb E_\nu |U'|^2.
\]

Equivalently

\[
\boxed{
\mathbb E_\nu |U'|^2
\ge\frac2t\mathbb E_\nu U^2.
}
\]

---

## 5. Imaginary component — first-moment coercivity with the interface included

The second collision constraint is

\[
\mathbb E_\nu[aV]=0.
\]

Recall

\[
h=ct/2,
\qquad
\frac{W'}W=-\frac{2(a-h)}t.
\]

Because `V(0)=0` and the Gaussian weight kills the boundary at infinity, integration by parts gives

\[
\begin{aligned}
\mathbb E_\nu[(a-h)V]
&=-\frac t2\mathbb E_\nu\left[V\frac{W'}W\right]\\
&=\frac t2\mathbb E_\nu[V'].
\end{aligned}
\]

Using `E[aV]=0`,

\[
0=h\mathbb E_\nu V+\frac t2\mathbb E_\nu V'.
\]

Therefore

\[
\boxed{
\mathbb E_\nu V
=-\frac{t}{2h}\mathbb E_\nu V'
=-\frac1c\mathbb E_\nu V'.
}
\]

By Cauchy--Schwarz,

\[
|\mathbb E_\nu V|^2
\le\frac1{c^2}\mathbb E_\nu|V'|^2.
\]

Also Poincare gives

\[
\operatorname{Var}_\nu(V)
\le\frac t2\mathbb E_\nu|V'|^2.
\]

Hence

\[
\mathbb E_\nu V^2
=\operatorname{Var}_\nu(V)+|\mathbb E_\nu V|^2
\le
\left(\frac t2+\frac1{c^2}\right)
\mathbb E_\nu|V'|^2.
\]

Thus

\[
\boxed{
\mathbb E_\nu|V'|^2
\ge
\frac{1}{t/2+1/c^2}\mathbb E_\nu V^2
=
\frac{2/t}{1+2/(c^2t)}\mathbb E_\nu V^2.
}
\]

This is the weaker of the two component estimates and therefore controls the full complex function.

---

## 6. Full two-saddle spectral inequality

Combining the real and imaginary parts,

\[
\int_0^\infty W_{c,t}|g_c'|^2
\ge
\frac{2/t}{1+2/(c^2t)}
\int_0^\infty W_{c,t}|g_c|^2.
\]

By reflection, the same ratio is the full-line ratio. Thus

\[
\boxed{
t\frac{\int_{\mathbb R}W_{c,t}|g_c'|^2}
{\int_{\mathbb R}W_{c,t}|g_c|^2}
\ge
\frac{2}{1+2/(c^2t)}.
}
\]

Away from the measure-zero interface `a=0`,

\[
g_c'(a)=e^{-c|a|}
\left[f'(a)-c\,\operatorname{sgn}(a)f(a)\right].
\]

Therefore

\[
W_{c,t}|g_c'|^2
=
G_t(a)e^{-c|a|}
\left|\xi'(s(a))-c\,\operatorname{sgn}(a)\xi(s(a))\right|^2,
\]

while

\[
W_{c,t}|g_c|^2
=
G_t(a)e^{-c|a|}|\xi(s(a))|^2.
\]

This proves

\[
\boxed{
\mathcal Q_{c,t}(\gamma)
\ge
\frac{2}{1+2/(c^2t)}
}
\]

at every real multiple heat collision.

---

## 7. Why the interface does not hide a delta singularity

The function `exp(-c|a|)` is Lipschitz. Therefore `g_c` belongs locally to `H^1` whenever `f` is smooth, and its weak first derivative is the displayed piecewise formula almost everywhere. The derivative jump at `a=0` produces a delta only in the **second** distributional derivative, not in the first-derivative energy used here.

Moreover the imaginary component obeys `V(0)=0` exactly by the functional equation, which is why the integration-by-parts step in Section 5 has no uncontrolled interface boundary term.

No boundary term was discarded.

---

## 8. Natural high-height choice of `c`

The explicit Archimedean slope from Polymath is

\[
u_0(\gamma)
:=\Re\alpha(1/2+i\gamma)
=\frac12\log\frac\gamma{2\pi}+O(\gamma^{-2}).
\]

The natural two-saddle choice is therefore

\[
\boxed{c=u_0(\gamma).}
\]

On `a>0`, the operator

\[
\partial_a-c
\]

subtracts the positive real Archimedean slope; on `a<0`,

\[
\partial_a+c
\]

subtracts its reflected negative counterpart.

Unlike Round 40, the sign now tracks the functional-equation reflection.

For this choice,

\[
c^2t\sim\frac t4\log^2\frac\gamma{2\pi}.
\]

When this parameter is large, the collision threshold tends to

\[
\boxed{2.}
\]

The remaining derivative is expected to contain only the bounded Archimedean phase, Stirling curvature, and the arithmetic variation of `zeta`. This expectation must be proved quantitatively before promotion.

---

## 9. Circularity/source audit

Used:

- the unconditional Gaussian-Hermite collision moments;
- the exact functional equation and conjugation symmetry of `xi`;
- a positive even gauge;
- the standard Poincare inequality for a strongly log-concave one-dimensional measure on a convex half-line;
- elementary integration by parts.

Not used:

- RH;
- `Lambda<=0`;
- any all-real-zero statement;
- a zero gap lower bound;
- `L_1>=0`;
- Hermite--Biehler stability;
- negative-time Rodgers--Tao local equilibrium;
- division by `zeta` at its zeros.

The criterion is a genuine independent necessary condition for a collision.

---

## 10. Round-43 target

Insert

\[
\xi(s)=P(s)\zeta(s)
\]

into the two-sided quotient with

\[
c=\Re\alpha(1/2+i\gamma).
\]

On the positive half-line,

\[
\xi'-c\xi
=P\left[\zeta'+(A-c)\zeta\right].
\]

The task is to obtain a rigorous upper bound for the positive-half quotient using the absolutely convergent Dirichlet series once the effective saddle lies in `Re s>1`, while controlling the shoulder `0<=a<=1/2+delta`. The negative half is identical by reflection and need not be estimated separately.

A successful theorem need only beat

\[
\frac{2}{1+2/(c^2t)},
\]

not the old threshold `4`.

If the shoulder contribution cannot be controlled without an RH-strength lower bound, record that obstruction explicitly and do not hide it inside a denominator estimate.

---

## 11. Status

- two-saddle gauge preserving first two collision moments: **PROVED**;
- interface/reflection decomposition: **PROVED**;
- half-line Poincare coercivity: **PROVED**;
- explicit all-multiplicity collision threshold: **PROVED**;
- threshold tends to `2` for `c^2t -> infinity`: **PROVED**;
- natural choice `c=Re alpha(1/2+i gamma)`: **UNCONDITIONAL / heuristic optimality only**;
- arithmetic upper bound beating the threshold: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
