# Round 58 — Why naive higher-order amplification does not beat a variance exponent, and where a genuinely new tool must enter

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED SCALING NO-GO / ROUTE CLASSIFICATION / NEW TOOL TARGET / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 57 shows that a second-moment/short-interval variance saving

\[
J(X,H)\ll H^{2-\kappa}X^{1+o(1)}
\]

leads to an arithmetic exponent

\[
\theta_\kappa(\alpha)=1-\kappa+\kappa/\alpha,
\]

so fixed `kappa<1` cannot eliminate zeros arbitrarily close to the critical line.

A natural reaction is to amplify the sparse zero more strongly by taking higher powers, higher moments, or tensor products. This round proves that such **homogeneous amplification does not change the exponent threshold**.

If a base statistic has

\[
\text{signal}\asymp X^{\sigma},
\qquad
\text{available bound}\ll X^{\theta+o(1)},
\]

then its `r`-th power has signal `X^{r sigma}` and bound `X^{r theta+o(1)}`. The condition for separation remains `sigma>theta`.

Thus simple higher moments cannot turn a fractional Selberg saving into sparse completeness.

A genuine improvement must be **non-homogeneous**: it must cancel or compress the arithmetic background more rapidly than it cancels the off-line spectral defect. The two concrete possibilities left are:

1. Poisson-scale second-moment cancellation;
2. a connected/cumulant/determinantal explicit formula that removes disconnected prime background before estimation.

Polynomial spectral amplification is not a third free option: in the conformal setting it returns to generalized Li-type high-order coefficients and their already identified coefficient-control barrier.

---

## 1. Abstract exponent lemma

Let `Q_X>=0` be a statistic depending on a large scale `X`. Suppose a target defect forces

\[
Q_X\ge X^{\sigma+o(1)}
\]

along some parameter sequence, while established arithmetic control gives

\[
Q_X\le X^{\theta+o(1)}.
\]

For any fixed integer `r>=1`,

\[
Q_X^r\ge X^{r\sigma+o(1)}
\]

and

\[
Q_X^r\le X^{r\theta+o(1)}.
\]

Therefore

\[
\boxed{
r\sigma>r\theta
\iff
\sigma>\theta.}
\]

No fixed power changes the detection threshold.

---

## 2. Application to the horizontal pair signal

For a right-half zero of displacement `delta`, the quadratic Gram signal is

\[
\sigma=2\delta.
\]

Under the fractional Selberg-variance model of Round 57,

\[
\theta=1-\kappa+\kappa/\alpha.
\]

A tensor/power statistic of order `r` has target growth

\[
X^{2r\delta}
\]

but a bound obtained by simply taking the `r`-th power of the second-moment estimate has exponent

\[
r(1-\kappa+\kappa/\alpha).
\]

The separation condition is still

\[
\boxed{
2\delta>1-\kappa+\kappa/\alpha.}
\]

Hence the limiting barrier

\[
\delta>\frac{1-\kappa}{2}
\]

is unchanged.

---

## 3. Reparameterizing the long range is not a new amplifier

Replacing `X` by `X^r` transforms

\[
X^{2\delta}
\longmapsto
X^{2r\delta}.
\]

But it simultaneously evaluates the arithmetic theorem at a correspondingly longer scale. This is just the parameter change

\[
\alpha\mapsto r\alpha.
\]

Round 53 already permits arbitrarily long `alpha` in the zero-side projection. Therefore scale iteration supplies no new structural information; the obstruction is precisely the lack of arithmetic control at those longer scales.

---

## 4. Higher raw moments inherit disconnected background

Suppose one considers

\[
\left|\sum_n a_n n^{-it}\right|^{2r}.
\]

Its expansion contains a large family of disconnected Wick/diagonal-type contractions built from products of lower moments. Any estimate obtained by repeated Cauchy--Schwarz/Hölder from the second moment scales homogeneously and therefore cannot improve the exponent ratio.

To gain something genuinely new, one must subtract or cancel these disconnected pieces before applying absolute bounds.

This points to **connected correlations / cumulants** rather than raw moments.

---

## 5. Why conformal polynomial amplification returns to modified Li

Another possible amplifier is a polynomial `P_n` of a Möbius transform that maps the critical line to the unit circle and an off-line zero outside it.

Repeated powers then produce exponential growth in `n` for the off-line orbit.

But this is exactly the structural mechanism behind Li and modified Li coefficients:

\[
1-\left(\frac{\rho-a}{\rho+a-1}\right)^n.
\]

Round 48 optimized this mechanism and found the improved height-adaptive scale `n asy gamma/delta`, but also proved that absolute Euler-product control cannot reach the necessary conformal disk.

Thus

\[
\boxed{
\text{polynomial conformal amplification}
\approx
\text{modified-Li high-order coefficient problem}.}
\]

It is not a free independent alternative.

---

## 6. What a connected statistic would need to do

Let `M_r` denote a raw `2r`-point prime/zero moment. A connected/cumulant quantity schematically has the form

\[
\kappa_r
=M_r-\sum_{\text{nontrivial partitions}}
\prod M_{|B|}.
\]

The design goal is that the large arithmetic background lives mostly in disconnected partitions and is removed algebraically, while a coherent off-line spectral orbit survives in the connected part.

For such a mechanism to beat Round 57, one would need a scaling of the schematic form

\[
\text{off-line connected signal}
\sim X^{r\sigma},
\]

but

\[
\text{connected arithmetic error}
\ll X^{o(r)\theta}
\]

or at least with an exponent growing strictly sublinearly relative to the signal complexity.

Nothing in current raw-moment technology supplies this automatically.

---

## 7. Prime-side interpretation

For primes, connected second correlation already means centering

\[
\Lambda(n)-1.
\]

At higher order, the natural objects are centered prime `k`-tuple correlations, with singular-series main terms removed in all lower partitions.

A successful theorem would resemble a **cumulant Hardy--Littlewood estimate** averaged over shifts and scales, rather than the full pointwise prime `k`-tuple conjecture.

This could in principle be weaker than controlling every fixed tuple individually, because the explicit-formula statistic supplies substantial averaging.

But it is still genuinely new arithmetic input.

---

## 8. Two legitimate new-tool families

After the no-go above, the primary arithmetic choices are:

### Tool family A — PSV/GWPC

Obtain essentially Poisson-scale second-moment cancellation for the exact triangular or Gaussian explicit-formula weights:

\[
J_{\rm adapted}(X,H)\ll HX\,X^{o(1)}.
\]

This keeps the correlation order low but demands near-optimal variance.

### Tool family B — CCEF

Construct a **Connected-Correlation Explicit Formula** whose arithmetic background is algebraically renormalized before estimation and whose one-orbit spectral response grows faster with complexity than the connected arithmetic error.

This increases structural complexity but may relax the need for a full Poisson-scale second moment.

---

## 9. Rejection rules for future rounds

The following should not be promoted as new amplification mechanisms:

- taking a fixed power of an existing positive statistic;
- tensoring the same Gram system finitely many times;
- replacing `x` by `x^r` without new arithmetic control;
- invoking higher raw moments and estimating them solely by Hölder/Cauchy--Schwarz from existing moments;
- using a Möbius/polynomial zero amplifier without auditing whether it is just modified Li under a change of variables.

Any one of these preserves the underlying exponent ratio or returns to an already known barrier.

---

## 10. Program decision

The question “can stronger zero amplification compensate for weaker prime variance?” now has a precise answer:

\[
\boxed{
\text{not by homogeneous powers or tensor moments}.}
\]

To beat the Round-57 threshold one needs either

\[
\boxed{
\text{near-Poisson second-moment arithmetic cancellation}}
\]

or

\[
\boxed{
\text{a genuinely connected/cumulant explicit-formula tool}.}
\]

The next research phase should compare these two tool-generation problems and select the one with the weakest arithmetic premise and the strongest independent applications outside RH.

**No proof of RH is claimed. Novelty remains unverified.**