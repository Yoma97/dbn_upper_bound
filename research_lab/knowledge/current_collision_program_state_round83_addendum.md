# Collision Program State — Round 83 Addendum

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Canonical policy:** strict track excludes finite-height RH verification from the entire proof ancestry.

---

## 1. Current strict full-time theorem

Round 81 is the strongest current full-time strict shoulder certificate:

\[
\boxed{
0<t\le1/2,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge6.50
\Longrightarrow
(H_t,H_t')\ne(0,0).
}
\]

It is internally proved and independently rerun at 512/768-bit directed precision. Referee verification remains pending.

---

## 2. New singular-wedge theorem

Round 82 removes the old `lambda_*≈4.914588956` asymptotic floor by retaining the complex heat-weighted Dirichlet sum rather than applying the `n=1` triangle envelope.

For every compact

\[
K=[a,b]\subset(4,\infty)
\]

there is `t_K>0` such that

\[
0<t\le t_K,
\qquad
\lambda\in K
\Longrightarrow
(H_t,H_t')\ne(0,0).
\]

The key uniform approximation is

\[
S_t
=
\zeta\left(\frac12+\frac\lambda4+i\tau\right)
+o_K(1),
\]

uniformly in the unbounded real phase `tau`, together with the unconditional Euler-product lower bound

\[
|\zeta(p+i\tau)|
\ge\frac{\zeta(2p)}{\zeta(p)}
\ge\frac1{\zeta(p_a)}>0.
\]

After collision conditioning and differentiation, the scaled lower margin satisfies

\[
\liminf_{t\to0^+}
\inf_{\lambda\in K}
 t\mathcal T_{\zeta}(t,\lambda)
\ge
\frac{a}{2\zeta(1/2+a/4)}>0.
\]

The Cauchy radius must depend on the compact interval:

\[
\rho_K
=
\min\left\{
1/10,
(a-4)/8,
a/(4b)
\right\}.
\]

This adaptation is essential for `4<a<=4.4`.

Splicing to Round 81 gives:

\[
\boxed{
\forall\varepsilon>0\ \exists t_\varepsilon>0:\quad
0<t\le t_\varepsilon,
\ \lambda\ge4+\varepsilon
\Longrightarrow
(H_t,H_t')\ne(0,0).
}
\]

No RH, no finite-height RH verification, and no upper bound for `Lambda` enters this theorem.

---

## 3. Correct interpretation of the number 4

`lambda=4` is not a proved collision boundary.

It is the exponential-scale transition of the **absolute cutoff mass**. With `u=t log n`, the rate including integer density is

\[
F_\lambda(u)
=
\frac{u^2}{4}
+\left(\frac12-\frac\lambda4\right)u,
\qquad
0\le u\le\lambda/2,
\]

and

\[
F_\lambda(\lambda/2)
=
\frac{\lambda(4-\lambda)}{16}.
\]

Thus absolute zeta perturbation is exponentially favorable above `4`, critical at `4`, and exponentially unfavorable below `4`.

---

## 4. Refuted shortcut

Round 83 rejects the tempting claim that critical-line subconvexity immediately produces a `lambda>16 theta` collision gate.

A pointwise bound for full `zeta(1/2+iT)` controls the reflected Riemann--Siegel combination, not the individual complex half-sum needed by the Round-82 amplitude lower bound. Near a hypothetical collision, cancellation between the reflected halves is precisely the phenomenon being tested.

Therefore

\[
\lambda>16\theta
\]

is **not** a theorem of the current program.

The valid older cross-frontier bridge remains Round 43's positive two-saddle Rayleigh gate

\[
\lambda>32\theta,
\]

which is structurally different and presently weaker than Round 82 above `4`.

---

## 5. Literature audit consequence

Existing literature removes the need to reconstruct:

- fixed-positive-time eventual reality/simplicity (Ki--Kim--Lee qualitatively, Polymath effectively);
- effective Riemann--Siegel approximation (Polymath Theorem 1.3);
- strict heat-smoothing simplicity once `t>Lambda`;
- direct PF-infinity route for the original kernel.

On the unrestricted published/certified-input track one may use upper bounds on `Lambda` derived from finite-height RH verification, but these remain excluded from the canonical strict track.

The critical singular layer is not located as a solved theorem in the audited literature.

---

## 6. Active invention zone

The small-time singular wedge is now partitioned as

\[
\lambda>4:\quad \text{closed asymptotically by Round 82},
\]

\[
\lambda=4:\quad \text{critical Riemann--Siegel cutoff profile OPEN},
\]

\[
0<\lambda<4:\quad \text{oscillatory/self-dual cutoff regime OPEN}.
\]

The next primary target is SW-B1: derive the value **and derivative jointly** in the `lambda=4` critical cutoff scaling, retaining the fractional Riemann--Siegel saddle parameter.

---

## 7. Source insight for SW-B1

Arias de Reyna's rigorous general Riemann--Siegel formula explicitly retains the fractional saddle parameter

\[
a=\sqrt{T/(2\pi)},
\qquad
N=\lfloor a\rfloor,
\qquad
p_{RS}=1-2(a-N),
\]

and its leading correction is an explicit entire function `F(p_RS)` with rigorous remainder bounds.

This is the correct classical source to inspect before deriving a new critical profile from scratch. However, the heat-weighted Polymath half-sum is not identical to the ordinary Riemann--Siegel half-sum, so the Arias correction cannot simply be pasted into the argument. The heat transform of the saddle/correction structure must be derived.

---

## 8. Priority

1. SW-B1: heat-transform / Polymath-contour derivation of the `lambda=4` fractional-saddle profile.
2. SW-B2: joint derivative profile and collision transversality test.
3. SW-C1: only then import a rigorously normalized exponential-sum/exponent-pair theorem below `4`.
4. Compact finite-time bridge remains secondary; use JECC/joint-jet after the singular asymptotics identify what must be covered.
5. Prime-side connected-correlation program remains frozen unless the direct saddle route hits a genuine arithmetic barrier.

**RH remains OPEN.**
