# Singular-Wedge Program V2 — after Round 82

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Canonical policy:** strict proof track excludes finite-height RH verification from the full dependency closure.

---

## 1. Current proven infrastructure

### Strict finite-time shoulder

Round 81 gives

\[
\boxed{
0<t\le1/2,
\qquad
\lambda\ge6.50
\Longrightarrow
(H_t,H_t')\ne(0,0).
}
\]

Status: internally proved, independently rerun with 512/768-bit directed arithmetic; referee verification pending.

### Singular-wedge small-time theorem

Round 82 gives, for every `epsilon>0`, some `t_epsilon>0` such that

\[
\boxed{
0<t\le t_\varepsilon,
\qquad
\lambda\ge4+\varepsilon
\Longrightarrow
(H_t,H_t')\ne(0,0).
}
\]

This uses the complex zeta envelope of the exact heat-weighted Polymath main sum and the elementary Euler product in `Re s>1`; it does not use RH or finite-height RH verification.

Thus the old asymptotic triangle floor

\[
4.914588956\ldots
\]

is no longer a structural frontier of the singular-wedge program. It was only the zero of the `n=1` triangle lower envelope.

---

## 2. Correct singular-wedge partition

Write

\[
x=4\pi e^{\lambda/t}.
\]

The genuinely noncompact small-time problem now splits into three regimes.

### SW-A — perturbative zeta regime

\[
\boxed{\lambda>4.}
\]

On every compact set bounded away from `4`, the exact weighted Dirichlet polynomial is a uniform absolute perturbation of

\[
\zeta\left(\frac12+\frac\lambda4+i\tau\right),
\]

and Euler-product nonvanishing supplies a uniform amplitude lower bound. This regime is analytically closed for sufficiently small `t`.

### SW-B — critical cutoff layer

\[
\boxed{\lambda=4.}
\]

The absolute endpoint mass is critical at exponential scale. The Round-82 perturbation parameter tends to the divergent Dirichlet-series boundary `q=1`, so the zeta-envelope error need not vanish.

This regime requires its own local asymptotic analysis.

### SW-C — oscillatory cutoff regime

\[
\boxed{0<\lambda<4.}
\]

The absolute mass near the moving Riemann--Siegel cutoff grows like

\[
\exp\left(\frac{\lambda(4-\lambda)}{16t}\right)
\]

on exponential scale. Therefore every proof based solely on absolute summation of the cutoff layer must fail here.

Any progress must retain cancellation in the phase

\[
e^{-i\tau\log n},
\qquad |\tau|\asymp x/2.
\]

---

## 3. What not to do below 4

Do **not** assume a generic square-root cancellation estimate for

\[
\sum_{n\asymp N}e^{-i\tau\log n}
\]

with

\[
N\asymp e^{\lambda/(2t)},
\qquad |\tau|\asymp e^{\lambda/t}.
\]

At the endpoint one has the self-dual relation

\[
N^2\asymp |\tau|/(2\pi),
\]

which is precisely the Riemann--Siegel saddle scale. A naive second-derivative van der Corput bound gives no uniform strong cancellation at this scale; Poisson/saddle transformation produces a dual sum of comparable length.

Thus any theorem below `4` must use a genuine Riemann--Siegel/exponent-pair mechanism with its constants and parameter range audited, not an informal oscillation heuristic.

---

## 4. Immediate next target: SW-B at lambda=4

The first priority is the exact critical layer, because it determines what replaces the vanished absolute perturbation.

Let

\[
R=e^{\lambda/t}=x/(4\pi),
\qquad
N\sim\sqrt R.
\]

At `lambda=4`, the individual cutoff amplitude satisfies

\[
a_N
\asymp
\exp(-2/t),
\]

while the number of terms is of order

\[
N\asymp e^{2/t}.
\]

Thus the absolute cutoff block is order one at exponential scale.

The phase is

\[
-\tau\log n,
\qquad
-\tau=2\pi R+O(t),
\]

and the cutoff relation is

\[
N^2\le R+t/16<(N+1)^2.
\]

The new object to derive is therefore a **uniform critical Riemann--Siegel cutoff profile**, retaining the fractional saddle displacement

\[
\omega=R+t/16-N^2
\]

(or a normalized equivalent), rather than suppressing the final block by absolute values.

Target form:

\[
S_t
=
\zeta\left(\frac32+i\tau\right)
+
\mathcal C(\omega,\vartheta)
+
o(1),
\]

or, if zeta is not the correct reference at the critical point, an equivalent two-component saddle profile with an explicit uniform remainder.

No claim is made yet that this exact displayed ansatz is correct; deriving the correct profile from Polymath's contour/Riemann--Siegel formula is SW-B1.

---

## 5. SW-B1 derivation protocol

1. Start from Polymath Theorem 1.3 / its contour proof, not from an ad hoc discrete approximation.
2. Set `lambda=4` before discarding endpoint terms.
3. Keep the exact fractional cutoff/saddle parameter.
4. Apply Euler--Maclaurin or the Riemann--Siegel local contour transform only to the terminal window whose absolute mass is order one.
5. Derive the value and derivative profiles **jointly**.
6. Audit the profile under the collision conditions, not just for nonvanishing of the value.
7. Require a uniform remainder in the fractional saddle parameter.

---

## 6. SW-C after the critical profile

Only after SW-B is understood should `lambda<4` be attacked.

The likely reusable inputs are:

- Riemann--Siegel self-duality / saddle transform;
- explicit exponential-sum bounds or exponent pairs for the logarithmic phase;
- phase-correlated value/derivative certificates (JECC/J-type) applied **after** grouping terms into saddle blocks;
- multiplicative/prime-fiber grouping if generic exponential-sum estimates lose too much.

A useful conditional bookkeeping lemma may express how an exponent-pair bound changes the exponential cutoff rate, but no exponent-pair threshold is to be promoted until the precise primary theorem and its normalization are inserted.

---

## 7. Compact versus singular work

For every fixed `epsilon>0`, once the small-time theorem has removed

\[
0<t\le t_\varepsilon,
\qquad
\lambda\ge4+\varepsilon,
\]

the remaining region above `4+epsilon` and below the current finite-time shoulder is compact in `(t,lambda)`.

It may be attacked with JECC / exact joint-jet / validated computation. However, this is no longer the primary invention target; the primary analytic novelty lies at and below `lambda=4`.

---

## 8. Literature reductions retained

Do not rebuild:

- fixed-positive-time eventual reality/simplicity (Ki--Kim--Lee qualitative; Polymath effective);
- Polymath effective Riemann--Siegel approximation;
- strict heat-smoothing simplicity once `t>Lambda`;
- zero-motion ODE before simplicity;
- direct PF-infinity route for the original kernel.

On the unrestricted track only, the current published/certified upper bounds for `Lambda` may further shorten the time interval, but they are not inputs to the strict track because of their finite-height RH-verification ancestry.

---

## 9. Current priority order

1. **SW-B1:** derive the exact `lambda=4` critical cutoff profile.
2. **SW-B2:** derive the corresponding derivative/joint-jet profile and test collision transversality.
3. **SW-C1:** insert a rigorously sourced logarithmic exponential-sum estimate below `4` and compute its true lambda range.
4. **Compact bridge:** use JECC/joint-jet only where needed after the singular analysis.
5. **Prime-side connected route:** remain frozen unless the direct saddle/exponential-sum program hits a structural arithmetic barrier.

---

## 10. Status

\[
\boxed{
C_{\rm strict,global}=6.50
}
\]

remains the current full-time strict shoulder constant.

Separately,

\[
\boxed{
C_{\rm strict,small-time}=4+\varepsilon
\text{ for every }\varepsilon>0
}
\]

in the quantified sense of Round 82.

Neither statement proves RH. The critical and subcritical singular wedge remains open.
