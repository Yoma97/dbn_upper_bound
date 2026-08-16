# Round 61 — The fourth connected prime cumulant is not determined by pair correlation

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED ALGEBRAIC NO-GO / PRIME-SPECIFIC GAP / OPERATOR TARGET REFINED / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 60 proposed the lowest-order falsification test for an all-orders connected-correlation tool: determine whether the fourth connected cumulant could be generated entirely from a second-order pair kernel, for example through `Tr(K^2)`.

The answer is **no at the algebraic level**.

After the three pair contractions are removed, the fourth cumulant of a centered prime statistic contains an irreducible four-shift correlation

\[
\boxed{
\sum_n
(\Lambda(n+h_1)-1)
(\Lambda(n+h_2)-1)
(\Lambda(n+h_3)-1)
(\Lambda(n+h_4)-1).}
\]

For four distinct shifts this is genuine prime quadruple information. Pair-correlation data do not determine it.

This is not merely a limitation of a particular formula. Two processes can have identical covariance kernels and different fourth cumulants. Therefore no universal construction depending only on the pair kernel can recover the fourth connected term.

Consequently, any successful all-orders operator/factorization must use arithmetic information richer than pair correlation. The most plausible source is a **local-prime/Euler-product cluster generator** or another structure that encodes all prime correlations simultaneously.

---

## 1. Centered arithmetic field

Let

\[
\boxed{b(n):=\Lambda(n)-1.}
\]

For a finite family of weights `w_h`, define a local centered statistic

\[
Y(n):=\sum_h w_h b(n+h).
\]

Use normalized averaging over a long interval as the expectation functional,

\[
\mathbb E_X F
:=\frac1X\sum_{X<n\le2X}F(n),
\]

or a smooth equivalent. Lower-order mean corrections can be inserted exactly and do not affect the structural conclusion below.

---

## 2. Fourth cumulant identity

For a centered scalar statistic,

\[
\boxed{
\kappa_4(Y)
=\mathbb E(Y^4)-3\mathbb E(Y^2)^2.}
\]

More generally, for four centered variables,

\[
\boxed{
\begin{aligned}
\kappa_4(X_1,X_2,X_3,X_4)
&=\mathbb E(X_1X_2X_3X_4)\\
&\quad-\mathbb E(X_1X_2)\mathbb E(X_3X_4)\\
&\quad-\mathbb E(X_1X_3)\mathbb E(X_2X_4)\\
&\quad-\mathbb E(X_1X_4)\mathbb E(X_2X_3).
\end{aligned}}
\]

Thus pair data remove exactly the three disconnected pair partitions and no more.

---

## 3. Prime four-shift term survives

Expand

\[
Y^4
=\sum_{h_1,h_2,h_3,h_4}
 w_{h_1}w_{h_2}w_{h_3}w_{h_4}
 b(n+h_1)b(n+h_2)b(n+h_3)b(n+h_4).
\]

Hence

\[
\kappa_4(Y)
=\sum_{h_1,\ldots,h_4}
 w_{h_1}\cdots w_{h_4}
 C_4(h_1,h_2,h_3,h_4),
\]

where, for centered variables,

\[
\boxed{
\begin{aligned}
C_4(h_1,h_2,h_3,h_4)
&:=\mathbb E_X\prod_{j=1}^4 b(n+h_j)\\
&\quad-\sum_{\text{three pairings}}
C_2(h_i,h_j)C_2(h_k,h_\ell).
\end{aligned}}
\]

For four distinct shifts, the first term is a genuine four-point correlation of `Lambda` after expansion of `b=Lambda-1`.

There is no algebraic identity forcing it to equal the three pair products.

Therefore

\[
\boxed{
C_4\text{ contains arithmetic information not present in }C_2.}
\]

---

## 4. Abstract covariance counterexample

The insufficiency of pair data is universal.

Let `G` be a standard real Gaussian variable and `R` a Rademacher variable taking values `+-1` with probability `1/2`.

Both satisfy

\[
\mathbb E G=\mathbb E R=0,
\qquad
\mathbb E G^2=\mathbb E R^2=1.
\]

Thus their one-point covariance data agree.

But

\[
\mathbb E G^4=3,
\qquad
\mathbb E R^4=1.
\]

Hence

\[
\boxed{
\kappa_4(G)=3-3=0,}
\]

while

\[
\boxed{
\kappa_4(R)=1-3=-2.}
\]

Taking independent copies gives two stochastic fields with the same covariance kernel and different fourth connected correlations.

Therefore no functional of the covariance kernel alone can universally recover the fourth cumulant.

---

## 5. Consequence for a `Tr(K^2)` closure

Suppose `K` is constructed solely from the pair covariance / pair-correlation kernel. Then any quantity such as

\[
\operatorname{Tr}(K^2),
\quad
\det(I+zK),
\quad
\|K\|_{HS}^2
\]

is determined by pair data.

Section 4 proves that a general fourth connected cumulant is not.

Thus an identity

\[
\boxed{
\kappa_4=\operatorname{Tr}(K^2)+\text{known universal correction}}
\]

cannot hold solely from second-order information.

For primes, any such identity would itself encode an additional nontrivial arithmetic theorem about four-point correlations.

---

## 6. Relation to prime short-interval Gaussianity

Montgomery--Soundararajan's high-moment analysis of primes in short intervals supports an approximately Gaussian law in mesoscopic regimes. The arithmetic mechanism uses strong quantitative Hardy--Littlewood prime `k`-tuple information (or sufficiently strong averaged forms) to evaluate high moments.

The fourth-moment case already reflects exactly the obstruction above: Gaussian Wick factorization

\[
\mathbb E(Y^4)\approx3\mathbb E(Y^2)^2
\]

is not a consequence of the second moment alone; it is a new four-point statement.

Therefore existing Gaussian heuristics do not give an unconditional fourth connected bound for the RH program.

---

## 7. What arithmetic structure could still generate all orders

The no-go applies only to operators built from pair covariance alone. It leaves open a stronger prime-specific generator whose input already contains more structure.

Promising possibilities:

### 7.1 Local-prime factorization

Construct a generating functional as an Euler product or product over local prime states,

\[
\mathcal Z[J]
=\prod_p \mathcal Z_p[J],
\]

so that

\[
\log\mathcal Z[J]
=\sum_p\log\mathcal Z_p[J]
\]

generates connected correlations automatically.

The challenge is that primality correlations are not independent local events after the global integer average; a naive product model only reproduces singular-series heuristics.

### 7.2 Sieve/dispersion cluster generator

Find a decomposition in which connected prime clusters are represented by a convergent sum of bilinear forms controlled uniformly in cluster order.

### 7.3 Arithmetic transfer operator

Construct a transfer/trace operator from prime powers whose Fredholm determinant has logarithmic derivatives equal to connected explicit-formula statistics.

Such an operator would have to be derived from established arithmetic identities, not postulated from the zero set.

---

## 8. New-tool target refined

Round 60's all-orders generator target is now sharpened.

### APFG — Arithmetic Prime Factorization Generator

Find a finite structural construction `G` with the properties:

1. `G` is defined from primes/prime powers without using zeta-zero locations;
2. derivatives of `log G` generate centered connected prime correlations of all orders;
3. one norm/convergence theorem controls those derivatives uniformly in order;
4. the corresponding zero-side transform has the connected off-line amplifier of Round 60;
5. the construction is not merely the Euler product for `zeta` followed by an RH-equivalent analytic-continuation assertion.

This is substantially more demanding than pair correlation but is now the correct specification if the cumulant route is to remain alive.

---

## 9. Program decision

- Pair data determine the fourth connected cumulant: **REFUTED**.
- `Tr(K^2)` from pair covariance alone as fourth-cumulant closure: **REFUTED GENERICALLY**.
- Genuine prime four-point information enters at order four: **PROVED ALGEBRAICALLY**.
- High-order connected amplification: **still potentially powerful**.
- Order-by-order Hardy--Littlewood route: **too strong / not a finite new mechanism**.
- Prime-specific all-orders factorization/operator: **OPEN / NEW TOOL TARGET**.

The next research choice is now sharp:

1. attempt to build APFG from local prime/Euler-product data and falsify it quickly if it reduces to ordinary zeta analytic continuation; or
2. abandon all-orders cumulants and search for a finite-dimensional positivity/factorization theorem that amplifies one off-line orbit without increasing prime correlation order.

The second route may be lower risk and should be explored in parallel.

**No proof of RH is claimed. Novelty remains unverified.**