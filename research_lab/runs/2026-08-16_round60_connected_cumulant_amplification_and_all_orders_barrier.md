# Round 60 — Connected-cumulant amplification can beat the second-moment exponent, but order-by-order closure becomes an all-prime-tuples problem

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED ABSTRACT CUMULANT FACTS / CONDITIONAL SPECTRAL SCALING / STRUCTURAL BARRIER / NEW OPERATOR TOOL TARGET / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 58 showed that raw powers and tensor moments do not improve the sparse-detection exponent because signal and arithmetic background scale homogeneously. Connected cumulants are different: they algebraically remove products of lower-order/disconnected moments before estimation.

At spectral order `2r`, an off-line conjugate pair can produce a phase-free connected monomial with horizontal factor

\[
\boxed{X^{2r\delta}.}
\]

If the corresponding connected prime cumulant could be controlled at a Poisson/linear scale instead of the raw `r`-fold scale, the horizontal detection threshold would improve like `1/r`. In principle, letting `r` grow could detect arbitrarily small `delta`.

This is a genuine mechanism that escapes the homogeneous no-go of Round 58.

But an order-by-order implementation immediately runs into a deeper arithmetic barrier: the `2r`-th connected prime cumulant contains centered `2r`-point correlations of the von Mangoldt function. Proving the required bounds separately for all `r` amounts to an all-orders prime-correlation program of Hardy--Littlewood type.

Thus CCEF is promising only if one can invent **one structural theorem**—operator, determinant, trace, martingale, or factorization—which controls all connected orders simultaneously from lower-complexity arithmetic input.

The new-tool target is therefore no longer “prove higher prime correlations.” It is “find an all-orders generator/factorization for prime connected correlations.”

---

## 1. Cumulant algebra

For random-variable notation, the `r`-th cumulant is obtained from moments by Möbius inversion on set partitions:

\[
\boxed{
\kappa_r(X_1,\ldots,X_r)
=\sum_{\pi\in\mathcal P([r])}
(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{B\in\pi}
\mathbb E\prod_{j\in B}X_j.}
\]

The same algebra applies to deterministic averages over a scale/height parameter: replace expectation by the chosen averaging functional.

The defining property is that cumulants vanish on decompositions into independent/disconnected blocks and remove all products of lower moments.

For `r>=2`, adding a deterministic constant to one argument does not affect the connected cumulant. Thus continuous/PNT main terms can be removed algebraically at the cumulant level rather than by estimating their large raw powers.

---

## 2. Spectral toy model

Consider an exponential spectral sum

\[
Z(L)=\sum_j a_j e^{(\delta_j+i\gamma_j)L}
\]

with conjugation symmetry. A right-half off-line mode

\[
a e^{(\delta+i\gamma)L}
\]

comes with its conjugate-frequency partner

\[
\bar a e^{(\delta-i\gamma)L}.
\]

In an even connected order `2r`, the balanced monomial containing `r` copies of each has zero total vertical phase and horizontal magnitude

\[
\boxed{|a|^{2r}e^{2r\delta L}=|a|^{2r}X^{2r\delta}}
\]

when `X=e^L`.

This is the basic connected sparse amplifier.

Whether its coefficient survives a particular cumulant depends on the exact averaging/statistic and must be verified in each construction. The claim here is a **scaling mechanism**, not an already constructed zeta cumulant theorem.

---

## 3. Why this differs from raw powers

A raw `2r`-th moment contains all Wick/disconnected products. Its arithmetic background typically scales like products of second moments, so Round 58's homogeneous exponent barrier returns.

The connected cumulant subtracts exactly those partitions. In an ideal Poisson/Gaussian-type arithmetic regime, higher connected orders are far smaller than raw moments.

Hence it is possible in principle to have

\[
\text{connected spectral defect}\sim X^{2r\delta}
\]

while the connected arithmetic background grows with an exponent much smaller than `r` times the second-moment exponent.

This is the mechanism needed to beat Round 58.

---

## 4. Idealized detection threshold

Suppose a connected `2r`-point explicit-formula statistic satisfies a bound of schematic form

\[
|\mathcal C_{2r}^{\rm prime}(X)|
\ll X^{\Theta_r+o(1)},
\]

while one off-line pair forces

\[
|\mathcal C_{2r}^{\rm zero}(X)|
\gg X^{2r\delta-o(1)}.
\]

Then the orbit is excluded if

\[
\boxed{2r\delta>\Theta_r.}
\]

If

\[
\Theta_r=O(1)
\quad\text{or more generally}\quad
\Theta_r=o(r),
\]

then

\[
\frac{\Theta_r}{2r}\to0,
\]

and arbitrarily small positive `delta` become detectable by increasing `r`.

This is precisely the kind of **superlinear signal / sublinear background complexity** absent from homogeneous powers.

---

## 5. Prime-side content of a connected cumulant

Let

\[
Y_H(x)=\sum_{x<n\le x+H}\Lambda(n)-H.
\]

The `r`-th connected moment of `Y_H` expands into sums of centered products

\[
\prod_{j=1}^r(\Lambda(n+h_j)-1)
\]

with all lower set-partition contributions subtracted.

Thus a `2r`-point CCEF requires information on averaged connected correlations of the form

\[
\boxed{
\sum_n
\prod_{j=1}^{2r}
(\Lambda(n+h_j)-1)}
\]

or a smoothed/multiplicative analogue.

This is already substantially beyond pair correlation when `r>=2`.

---

## 6. Relationship with the short-interval Gaussian program

Montgomery--Soundararajan's work on primes in short intervals provides strong evidence for an approximately Gaussian distribution with variance of order

\[
H\log(N/H)
\]

in mesoscopic ranges. Their high-moment analysis is tied to strong quantitative Hardy--Littlewood prime `k`-tuple information (or averaged variants).

This is exactly the arithmetic pattern predicted by the cumulant viewpoint:

- the second cumulant is the Selberg variance;
- higher Gaussian cumulants should be small;
- proving this at arbitrary order requires control of increasingly high prime correlations.

Therefore existing Gaussian heuristics validate the architecture but do not supply an unconditional all-orders theorem for the RH application.

---

## 7. All-orders barrier

Suppose one attempts to prove the necessary connected estimate separately for every `r` by expanding into prime tuples and applying a new theorem at each order.

To detect a zero displacement `delta`, the idealized order requirement is

\[
r\gtrsim1/\delta.
\]

Since an RH-false zero could have `delta` arbitrarily small, sparse completeness requires unbounded `r`.

Thus an order-by-order CCEF proof would require an unbounded hierarchy of prime-correlation theorems.

This is structurally analogous to the earlier generalized-Laguerre hierarchy problem: proving every member individually is not a satisfactory finite new mechanism.

Hence

\[
\boxed{
\text{CCEF is viable only if all orders follow from one lower-level structural theorem}.}
\]

---

## 8. What kind of structural theorem could suffice

The desired theorem should generate connected-correlation control without evaluating every prime tuple individually.

Candidate architectures include:

### 8.1 Operator determinant / Fredholm generator

Construct an arithmetic operator `K` such that the cumulant generating function is

\[
\log\det(I+zK)
=\sum_{r\ge1}\frac{(-1)^{r+1}}r z^r\operatorname{Tr}K^r.
\]

A single norm/trace-class estimate could then control all connected orders.

### 8.2 Martingale / dependency decomposition

Represent centered prime counts as a sum of scale-local increments whose conditional cumulants admit uniform bounds, allowing all-order control from one filtration theorem.

### 8.3 Cluster expansion

Produce a convergent cluster expansion for a prime correlation generating functional, with connected cluster weights bounded by one summable majorant.

### 8.4 Positive trace formula

Find a Hermitian explicit formula in which connected zero contributions correspond to traces of powers of one positive/contraction operator, while the prime side provides a norm bound on that operator.

Any such result would be genuinely new and would have applications beyond RH.

---

## 9. Circularity/repackaging audit

The following do **not** count as the desired all-orders generator:

- assuming the full Hardy--Littlewood prime `k`-tuple conjecture for every `k`;
- assuming Gaussianity of prime counts to all moments;
- assuming the Pair Correlation Conjecture plus an unstated independence principle;
- defining an operator whose contraction property is algebraically equivalent to RH/Weil positivity;
- using generalized Li or generalized Laguerre positivity under another determinant notation.

The structural theorem must have an independently provable prime-side reason.

---

## 10. Tool hierarchy after Round 60

We now have three levels.

### Level 1 — partial unconditional progress

Any fixed fractional second-moment saving `kappa>0` can yield a genuine horizontal zero-free band in a suitable long-range architecture.

### Level 2 — sparse-complete second moment

Poisson-scale variance is strong enough but Round 59 shows that its natural global endpoint is itself RH-strength; it needs an independent mechanism.

### Level 3 — sparse-complete connected hierarchy

Connected cumulants can in principle amplify arbitrarily small `delta`, but only if all orders are controlled by one structural generator rather than an infinite list of prime-tuple estimates.

The research priority should therefore be to invent/test a **finite operator/factorization theorem that implies an all-orders connected bound**.

---

## 11. Immediate next experiment

The lowest-complexity test of the operator idea is order four.

Construct the fourth connected cumulant of a smoothed centered prime statistic and determine whether it can be written as

\[
\boxed{
\operatorname{Tr}(K^2)+\text{small explicit defect}}
\]

for a naturally occurring second-order kernel `K` already controlled by pair-correlation/large-sieve methods.

If the fourth cumulant irreducibly contains a new prime quadruple correlation after all pair contractions are removed, then the hoped-for closure from pair data alone is refuted at the first nontrivial order.

That is the next precise falsification test.

**No proof of RH is claimed. Novelty remains unverified.**