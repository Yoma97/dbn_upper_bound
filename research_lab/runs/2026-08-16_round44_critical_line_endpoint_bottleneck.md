# Round 44 — The critical-line endpoint is the exact bottleneck for pointwise exponent-profile improvements

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED NO-GO / CROSS-FRONTIER BOTTLENECK / SOURCE-GROUNDED / NOVELTY UNVERIFIED.

## 0. Executive theorem

Round 43 showed that a pointwise zeta exponent profile

\[
|\zeta(1/2+a+iT)|\ll T^{\mu(a)+o(1)},\qquad 0\le a\le1/2,
\]

feeds the two-saddle collision route through the variational rate

\[
\mathfrak S_\lambda(a)
:=-a^2+\frac\lambda2a+2\lambda\mu(a).
\]

The safe saddle has rate `lambda^2/16`, so the pointwise route closes only if

\[
\sup_{0\le a\le1/2}\mathfrak S_\lambda(a)
<\frac{\lambda^2}{16}.
\]

This round proves a sharp structural obstruction:

> If the critical-line exponent is `theta >= 1/8`, and the interior profile is any pointwise improvement of the ordinary Phragmen--Lindelof interpolation
> \[
> \mu(a)\le\theta(1-2a),
> \qquad \mu(0)=\theta,
> \]
> then
> \[
> \boxed{
> \sup_{0\le a\le1/2}\mathfrak S_\lambda(a)
> =2\theta\lambda.
> }
> \]
> Hence **no improvement strictly inside the critical strip can improve the Round-43 gate**. The endpoint `a=0`, i.e. the critical line itself, remains the unique bottleneck for this entire class of pointwise arguments.

Consequently the threshold remains exactly

\[
\boxed{\lambda>32\theta.}
\]

with Bourgain's `theta=13/84`, regardless of inserting the sharper Yang interior-strip lines.

To beat the existing collision threshold

\[
\lambda_*\approx4.914588956
\]

by this pointwise-profile architecture would require

\[
\boxed{
\theta<\frac{\lambda_*}{32}
\approx0.153580904875.
}
\]

Bourgain gives

\[
\frac{13}{84}\approx0.154761904762,
\]

so the exact exponent gap is approximately

\[
\boxed{0.001180999887.}
\]

The next route must therefore either improve critical-line subconvexity itself or replace pointwise shoulder control by an averaged/localized estimate that exploits the shrinking Gaussian window.

---

## 1. Baseline interpolation profile

Assume

\[
|\zeta(1/2+iT)|\ll T^{\theta+o(1)}
\]

and the standard subpolynomial bound on the `1`-line. Phragmen--Lindelof gives the baseline exponent

\[
\boxed{
\mu_{\rm PL}(a)=\theta(1-2a),
\qquad 0\le a\le1/2.
}
\]

For this profile the Round-43 rate is

\[
\begin{aligned}
\mathfrak S^{\rm PL}_\lambda(a)
&=-a^2+\frac\lambda2a+2\theta\lambda(1-2a)\\
&=2\theta\lambda-a^2
+\lambda\left(\frac12-4\theta\right)a.
\end{aligned}
\]

If

\[
\theta\ge\frac18,
\]

then

\[
\frac12-4\theta\le0.
\]

Therefore for every `a>=0`,

\[
\boxed{
\mathfrak S^{\rm PL}_\lambda(a)
\le \mathfrak S^{\rm PL}_\lambda(0)
=2\theta\lambda,
}
\]

with strict inequality for every `a>0` unless the degenerate boundary case `theta=1/8` is combined with `a=0`.

Thus the baseline profile is already bottlenecked at the critical line.

---

## 2. Interior pointwise improvements cannot move the maximum

Let `mu(a)` be any improved profile satisfying

\[
\mu(0)=\theta
\]

and

\[
\mu(a)\le\mu_{\rm PL}(a)=\theta(1-2a)
\qquad(0\le a\le1/2).
\]

Then pointwise

\[
\mathfrak S_\lambda(a)
\le\mathfrak S^{\rm PL}_\lambda(a)
\le2\theta\lambda.
\]

At `a=0`, equality is forced:

\[
\mathfrak S_\lambda(0)
=2\lambda\mu(0)
=2\theta\lambda.
\]

Hence exactly

\[
\boxed{
\sup_{0\le a\le1/2}
\mathfrak S_\lambda(a)
=2\theta\lambda.
}
\]

This proves the no-go theorem.

The statement is independent of how strong the interior improvements are. Even a hypothetical perfect bound `mu(a)=0` for every fixed `a>0` would not alter the supremum as long as the critical-line endpoint remains `mu(0)=theta` and the argument estimates the shoulder pointwise.

---

## 3. Yang's interior lines are genuinely sharper but irrelevant to this gate

Andrew Yang proves for every integer `k>=4`

\[
\sigma_k:=1-\frac{k}{2^k-2}
\]

and

\[
\boxed{
|\zeta(\sigma_k+iT)|
\le1.546\,T^{1/(2^k-2)}\log T
\qquad(T\ge3).
}
\]

In the horizontal coordinate

\[
a=\sigma-\frac12,
\]

the anchor points are

\[
\boxed{
 a_k=\frac12-\frac{k}{2^k-2},
\qquad
\mu_k=\frac1{2^k-2}.
}
\]

For example,

\[
k=4:\qquad
\sigma_4=\frac57,
\quad a_4=\frac3{14},
\quad \mu_4=\frac1{14}.
\]

With Bourgain's

\[
\theta=\frac{13}{84},
\]

the straight Phragmen--Lindelof interpolation between the critical line and the `1`-line would instead give at `a=3/14`

\[
\theta(1-2a_4)
=\frac{13}{147}
>\frac1{14},
\]

so Yang's result is a real pointwise improvement.

Nevertheless it satisfies the hypotheses of Section 2: it only lowers `mu(a)` away from `a=0`. Therefore it cannot change the variational supremum controlling Round 43.

The same conclusion applies to the complete family of Yang anchor lines and to any convex envelope generated from them together with Bourgain and the `1`-line.

---

## 4. Exact critical-line exponent required to beat the current lambda barrier

The pointwise-profile gate is

\[
\lambda>32\theta.
\]

To improve upon the separate collision-program threshold

\[
\lambda_*\approx4.914588956,
\]

one therefore needs

\[
32\theta<\lambda_*.
\]

Equivalently,

\[
\boxed{
\theta<\theta_*:=\frac{\lambda_*}{32}
\approx0.153580904875.
}
\]

The best currently established asymptotic critical-line exponent used by the lab is Bourgain's

\[
\boxed{
\theta_B=\frac{13}{84}
\approx0.154761904762.
}
\]

Thus

\[
\boxed{
\theta_B-\theta_*
\approx0.001180999887.
}
\]

Equivalently, in lambda-space,

\[
\boxed{
\frac{104}{21}-\lambda_*
\approx0.03779199638.
}
\]

This is the precise arithmetic miss for the current pointwise subconvexity bridge.

---

## 5. What kind of improvement can still work without a new critical-line exponent?

The no-go theorem applies only to arguments which dominate the shoulder **pointwise** by

\[
|\zeta(1/2+a+iT)|\le T^{\mu(a)+o(1)}
\]

and then take a supremum in `a`.

It does **not** rule out exploiting the fact that the Round-42 quotient contains an integral. Near the endpoint `a=0`, the exponent has a nonzero negative right derivative when `theta>1/8`. Hence the dangerous endpoint mass is concentrated in a horizontal boundary layer whose scale is much smaller than an `O(1)` interval.

This suggests a genuinely different next target:

> replace the pointwise `sup` estimate at `a=0` by a Gaussian-weighted horizontal mean-square estimate for `zeta` and `zeta'` on the shrinking shoulder layer.

A mean estimate can in principle gain a power or exponential factor even while the best pointwise value at the exact critical line remains Bourgain's exponent.

The theorem required must be local enough in the **real direction** and uniform in the ordinate. Ordinary vertical mean-square theorems do not automatically apply because the integration variable here is `sigma`, not `t`.

---

## 6. Anti-circularity audit

The no-go theorem is algebraic/variational and uses no root-location hypothesis.

The source inputs are only:

- an established critical-line subconvexity exponent;
- Phragmen--Lindelof interpolation;
- Yang's unconditional interior-strip bounds;
- the Round-43 rate functional already derived from the collision criterion.

It does not use RH, Lindelof, zero-free neighborhoods of the critical line, a lower zero gap, or Laguerre--Polya positivity.

---

## 7. Program decision after Round 44

The following target is now **FROZEN**:

> improve Round 43 merely by inserting sharper pointwise bounds at fixed interior values `sigma>1/2`.

Such improvements cannot move the gate while the critical-line endpoint exponent remains unchanged.

The two live possibilities are:

1. **critical-line route:** a genuine improvement of the asymptotic exponent below
   \[
   0.153580904875\ldots;
   \]
2. **averaged-shoulder route:** derive a weighted horizontal integral estimate which avoids replacing the shoulder by its pointwise supremum.

The second is the preferred internal research target because it does not require solving a famous standalone subconvexity record problem first.

---

## 8. Status

- Yang interior exponent anchors: **ESTABLISHED SOURCE INPUT**;
- interior bounds improve the pointwise profile: **YES**;
- interior pointwise bounds improve the Round-43 lambda gate: **REFUTED**;
- exact pointwise gate remains `lambda>32 theta`: **PROVED**;
- critical-line exponent needed to beat `lambda_*`: **theta < 0.153580904875...**;
- current Bourgain miss: **about 0.001181 in theta / 0.037792 in lambda**;
- averaged horizontal shoulder theorem: **OPEN / next target**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
