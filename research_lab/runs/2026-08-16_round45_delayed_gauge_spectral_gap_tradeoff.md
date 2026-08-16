# Round 45 — Delayed two-saddle gauges gain core mass only by collapsing the spectral gap

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED MODEL NO-GO / GAUGE-SPECTRAL TRADEOFF / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 44 showed that the current cusp gauge

\[
\phi_0(a)=c|a|
\]

is bottlenecked by the critical-line endpoint in any pointwise zeta estimate. A natural attempted repair is to **delay** the gauge: keep it flat near `a=0`, then turn on slope `c` only closer to the safe saddle. This increases the safe-core exponential weight and appears capable of lowering the `lambda>32 theta` gate.

This round proves that the gain is not free.

On the positive half-line consider

\[
\boxed{
\phi_b(a):=c(a-b)_+,
\qquad b>0,
}
\]

and the collision-orthogonality weight

\[
\boxed{
W_{b,t}(a):=G_t(a)e^{\phi_b(a)}.
}
\]

The delayed gauge creates a boundary well at `a=0` and a second Gaussian well near

\[
h=ct/2.
\]

They are separated by a barrier at `a=b`, where the weight is smaller than at the boundary by the factor

\[
\exp(-b^2/t).
\]

Consequently the Poincare/spectral gap of `W_{b,t}` obeys an exponentially small upper bound

\[
\boxed{
\lambda_1(W_{b,t})
\le t^{-O(1)}e^{-b^2/t}
}
\]

whenever the second well is present (`0<b<h`) and dominates enough that the mean correction of the boundary-well test is harmless.

Thus:

- to alter the leading `1/t` shoulder/core rate, one needs `b` of fixed `O(1)` size, but then the spectral gap collapses exponentially;
- if `b=O(\sqrt t)` so that the gap is not exponentially destroyed, the safe-core rate gain is only `O(t^{-1/2})`, subleading to the `1/t` exponent and therefore cannot change the Round-44 lambda threshold.

Hence a delayed scalar gauge cannot beat the critical-line bottleneck while retaining an `O(1)` collision threshold through the same Poincare mechanism.

---

## 1. Positive-half delayed gauge

Work on `a>=0` and put

\[
\phi_b(a)=c(a-b)_+.
\]

The collision-orthogonality weight is

\[
W_{b,t}(a)
=\frac1{\sqrt{\pi t}}
\exp\!\left(-\frac{a^2}{t}+c(a-b)_+\right).
\]

Let

\[
h:=\frac{ct}{2}.
\]

For `0<=a<=b`,

\[
W_{b,t}(a)=G_t(a)
\]

and is strictly decreasing away from the boundary maximum at `a=0`.

For `a>=b`, completing the square gives

\[
\boxed{
-\frac{a^2}{t}+c(a-b)
=-\frac{(a-h)^2}{t}
+\frac{h^2}{t}-cb.
}
\]

If

\[
0<b<h,
\]

there is a second local maximum at `a=h`.

The exponent values are

\[
\log W(0)=\text{constant},
\]

\[
\log W(b)=\text{constant}-\frac{b^2}{t},
\]

and

\[
\log W(h)=\text{constant}
+\frac{h^2}{t}-cb.
\]

Thus the barrier separating the boundary well from the interior well has depth exactly

\[
\boxed{b^2/t}
\]

relative to the boundary well.

---

## 2. Rayleigh characterization of the Poincare gap

Let `nu_{b,t}` be the probability measure obtained by normalizing `W_{b,t}(a) da` on `[0,infinity)`. Its Poincare spectral gap is

\[
\lambda_1(b,t)
:=\inf_{F\not\equiv\mathrm{const}}
\frac{\int |F'|^2\,d\nu_{b,t}}
{\operatorname{Var}_{\nu_{b,t}}(F)}.
\]

To prove an upper bound it suffices to construct one test function whose derivative is supported only near the barrier.

---

## 3. Boundary-well test function

Fix a small transition width

\[
\delta_t:=t/b
\]

for fixed `b>0` and sufficiently small `t`. Define a Lipschitz function `F_t` by

\[
F_t(a)=1
\quad(0\le a\le b-\delta_t),
\]

\[
F_t(a)=0
\quad(a\ge b+\delta_t),
\]

with linear interpolation in the transition interval. Then

\[
|F_t'|\le\frac1{2\delta_t}
=O(b/t).
\]

On the transition region,

\[
a=b+O(t/b),
\]

so

\[
W_{b,t}(a)
\le t^{-1/2}\exp\!\left(-\frac{b^2}{t}+O(1)\right)
\]

up to a constant depending on fixed `b,c t` ranges.

Therefore the **unnormalized** Dirichlet energy satisfies

\[
\begin{aligned}
\int_0^\infty W_{b,t}|F_t'|^2da
&\ll
\left(\frac{b}{t}\right)^2
\frac{t}{b}
\,t^{-1/2}
\exp\!\left(-\frac{b^2}{t}+O(1)\right)\\
&\ll
b\,t^{-3/2}
\exp\!\left(-\frac{b^2}{t}+O(1)\right).
\end{aligned}
\]

---

## 4. The boundary-well variance is not exponentially smaller than its local mass

The unnormalized mass in a `sqrt(t)`-neighborhood of the boundary is

\[
\int_0^{\sqrt t}W_{b,t}(a)da
\asymp 1
\]

with the chosen normalization of `G_t`; equivalently it is only polynomial in `t` before/after harmless fixed constants.

If the interior well dominates the total mass, then the normalized boundary mass is exponentially small, but the variance of the indicator-type test is of the same order as that normalized boundary mass. After normalization, the total mass factor cancels between Dirichlet energy and variance. Equivalently, working throughout with the unnormalized measure, subtracting the mean of `F_t` does not change its derivative and the variance denominator remains comparable to the unnormalized boundary-well mass as long as neither well has probability exactly one.

Hence, in the two-well regime,

\[
\operatorname{Var}_{W_{b,t}}(F_t)
\ge t^{O(1)}
\]

relative to the boundary-well scale, with no factor `exp(-b^2/t)`.

Combining with Section 3 gives

\[
\boxed{
\lambda_1(b,t)
\le t^{-O(1)}
\exp\!\left(-\frac{b^2}{t}\right).
}
\]

The precise polynomial power is irrelevant for the large-deviation conclusion.

---

## 5. What the delayed gauge would have gained in the collision quotient

Take the high-height scaling

\[
L=\log(\gamma/2\pi)=\lambda/t,
\qquad
c\sim L/2=\lambda/(2t).
\]

Then

\[
h=ct/2\sim\lambda/4,
\]

the same positive saddle scale as in Round 43.

For `a>b`, the quotient denominator contains the factor

\[
G_t(a)e^{-\phi_b(a)}|P(s)|^2.
\]

At the exponential scale, using `2 Re log P` slope `L`, this has rate

\[
\boxed{
S_b(a;\lambda)
=-a^2+\frac\lambda2a+\frac{\lambda b}{2}
}
\]

near the region where the gauge slope is active.

Its maximum remains at

\[
a_*=\lambda/4,
\]

but the maximal rate is raised from

\[
\frac{\lambda^2}{16}
\]

to

\[
\boxed{
\frac{\lambda^2}{16}+\frac{\lambda b}{2}.
}
\]

Thus a fixed positive `b` really would improve the shoulder/core exponential comparison.

---

## 6. The exact tradeoff

To change the leading large-deviation gate, the gain

\[
\frac{\lambda b}{2t}
\]

must be of order `1/t`. This requires

\[
\boxed{b\asymp1}
\]

on the lambda scale.

But then Section 4 gives

\[
\boxed{
\lambda_1(b,t)
\le t^{-O(1)}e^{-b^2/t},
}
\]

so the collision coercivity furnished by a Poincare argument becomes exponentially weak.

Conversely, to prevent an exponential spectral-gap collapse one must take at most

\[
b=O(\sqrt{t\log(1/t)})
\]

(up to the desired polynomial gap scale). Then

\[
\frac{\lambda b}{2t}
=O\!\left(\sqrt{\frac{\log(1/t)}t}\right)
=o(1/t),
\]

which is subleading compared with the `1/t` rate controlling the Round-44 threshold.

Therefore:

\[
\boxed{
\text{leading exponential core gain}
\Longleftrightarrow
\text{exponential spectral-gap loss}
}
\]

within this delayed scalar-gauge/Poincare architecture.

---

## 7. Relation to the cusp gauge of Round 42

The original cusp gauge corresponds to

\[
b=0.
\]

Then the boundary well and barrier disappear. On the positive half-line the collision-orthogonality weight is a single shifted Gaussian with curvature `2/t`, and its Poincare gap remains of order `1/t`.

Thus the cusp at the symmetry interface is not an arbitrary aesthetic choice: it is precisely what permits immediate subtraction of opposite slopes on the two half-lines **without creating a metastable boundary well**.

Its cost is the critical-line endpoint bottleneck identified in Round 44.

---

## 8. Scope and anti-overclaim

This round does **not** prove that every conceivable nonlinear or vector-valued renormalization must fail. It proves a no-go for the natural delayed scalar-gauge strategy when the collision exclusion is extracted through the Poincare spectral gap of the corresponding orthogonality weight.

An arithmetic estimate tailored to the actual `xi`, rather than a universal Poincare bound, could in principle behave better. Such a theorem would need genuinely new input and cannot be inferred from the weight geometry.

No RH-equivalent statement is used.

---

## 9. Program decision

Freeze the following attempted loophole:

> delay the two-saddle scalar gauge by an `O(1)` horizontal distance to increase the safe-core exponent, while retaining the same Poincare collision threshold.

This is structurally impossible: the delayed weight becomes metastable and the spectral gap collapses exponentially.

The remaining live approaches are now sharper:

1. improve the critical-line exponent below `lambda_*/32`;
2. prove a **xi-specific horizontal averaged shoulder estimate** not reducible to a universal weight Poincare inequality;
3. find a vector-valued/two-channel operator whose spectral gap is protected by functional-equation coupling rather than scalar log-concavity.

Route 2 is the smallest next target.

---

## 10. Status

- delayed gauge safe-core rate gain: **PROVED**;
- two-well barrier depth `b^2/t`: **PROVED**;
- exponentially small Poincare-gap upper bound for fixed `b>0`: **PROVED at large-deviation scale**;
- delayed scalar gauge improves Round-44 threshold while retaining `O(1/t)` gap: **REFUTED**;
- cusp gauge singled out as one-well choice: **PROVED structurally**;
- xi-specific averaged shoulder estimate: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
