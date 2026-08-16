# Collision Program State — Round 61 addendum

**Date:** 2026-08-16

**RH status:** OPEN.

## Executive update

Rounds 48--61 move the project from local heat-collision identities into a sharply defined sparse-exception / explicit-formula program.

The main achievement is not an RH proof. It is a sequence of reductions and no-go theorems that identify where genuinely new mathematics is required.

The current architecture is

\[
\boxed{
\text{off-line orbit}
\longrightarrow
\text{amplified Hermitian spectral defect}
\longrightarrow
\text{prime-side connected/variance statistic}.}
\]

The zero-side localization problem is solved in one important sense by Round 53. The remaining difficulty is arithmetic cancellation. Several apparently simpler prime-side closures have now been proved RH-strength or structurally insufficient.

## Core results through Round 61

### Round 48 — adaptive modified Li

For `a=1/2-h` and `rho=1/2+delta+i gamma`, the Möbius-amplitude optimum is

\[
\boxed{h_*=\sqrt{\gamma^2+\delta^2}},
\]

with

\[
\log|Z_{h_*}(\rho)|
=\operatorname{artanh}\frac{\delta}{\sqrt{\gamma^2+\delta^2}}
=\frac\delta\gamma+O(\delta^3/\gamma^3).
\]

Thus the natural amplification scale improves from `gamma^2/delta` to `gamma/delta`. But the exact conformal-disk theorem shows that a Jensen disk whose reflected image stays wholly in `Re s>1` cannot contain a nontrivial critical-strip zero. Absolute Euler-product closure is refuted.

### Rounds 49--50 — pair amplifier and positivity-bandwidth tradeoff

RH-free pair correlation contains the horizontal factor

\[
\frac{2\cosh(2\delta\log x)}{1-\delta^2}.
\]

The published unconditional range `alpha<=1` is too short for one sparse orbit, and global Tsang-strip positivity forces effective Fourier scale `alpha=O(1/log T)`, killing polynomial amplification.

### Rounds 51--53 — Hermitian defect and exact zero-side isolation

The ideal finite-height defect is

\[
\mathcal V(T)=\sum_{0<\gamma\le T}m_\rho(\beta-1/2)^2\ge0.
\]

Exact horizontal projection cannot be implemented by one universal nonconstant holomorphic test, so a Hermitian/two-variable object is required.

The RH-free pair statistic is an exact Gram norm with diagonal

\[
\|v_{\rho,x}\|^2=\frac{x^{2\delta}}{1-\delta^2}.
\]

Raw fixed-width frame domination fails for close ordinates, but Round 53 bypasses the issue completely. If

\[
\delta_*(T)=\max_{0<\gamma\le T}(\beta-1/2),
\]

then

\[
\boxed{
\lim_{A\to\infty}\frac1A\int_0^A
T^{-2\alpha\delta_*}F(T^\alpha,T)d\alpha
=
\frac1{1-\delta_*^2}
\sum_{\substack{\rho:\delta=\delta_*\\0<\gamma\le T}}m_\rho^2>0,}
\]

and hence

\[
\boxed{
\delta_*(T)=\frac12\limsup_{\alpha\to\infty}
\frac{\log F(T^\alpha,T)}{\alpha\log T}.}
\]

Thus the zero-side sparse-localization problem is solved spectrally for extremal displacement.

### Rounds 54--55 — corrected prime decomposition and Mellin resolvent

The prime polynomial

\[
P_x(t)=\sum_n\frac{\Lambda(n)}{n^{1/2+it}}W(n/x),
\qquad W(y)=\min(y,y^{-1}),
\]

has exact continuous/pole main term

\[
\boxed{
I_x(t)=x^{1/2-it}
\left(\frac1{3/2-it}+\frac1{1/2+it}\right).}
\]

**Correction:** the complete `O(x)` barrier in the published finite-height proof does not arise only from this pole/prime separation. There is an independent `O(x)` zero-window truncation term when the all-zero resolvent is cut at `Z=T log^2T`, together with a zero-free-region-dependent transfer error.

Round 55 proves

\[
\boxed{
\int_0^\infty x^{-z-1}P_x(t)dx
=-\frac2{1-z^2}\frac{\zeta'}{\zeta}\left(\frac12+it+z\right),
\qquad 1/2<\Re z<1.}
\]

The zeta pole is the first Mellin residue and nontrivial zeros are the next poles. Therefore direct linear continuation through `Re z>0` is RH-strength; the legitimate opportunity is quadratic/averaged arithmetic structure.

### Round 56 — holomorphic soft height window

The test

\[
\boxed{h_{c,L}(z)=e^{-cLz^2+iLz}}
\]

assigns a zero `z_rho=gamma-i delta` the score

\[
\boxed{q_c(\rho)=\delta-c(\gamma^2-\delta^2).}
\]

The quadratic height penalty makes the maximum finite and removes the need for a hard zero cutoff. Its Fourier transform is the exact log-Gaussian prime window

\[
\widehat h_{c,L}(u)=\sqrt{\frac\pi{cL}}
\exp\left(-\frac{(u-L)^2}{4cL}\right).
\]

The price is a new Gaussian-centered prime-cancellation problem not solved by classical pointwise PNT bounds.

### Round 57 — Selberg variance dictionary

For a dyadic prime block `n asy X` and vertical averaging length `T`, the natural short interval is `H=X/T`, and at Gallagher/Parseval scale

\[
\int_{-T}^{T}|E_X(t)|^2dt
\ll\frac{T^2}{X^2}J(X,H).
\]

If

\[
J(X,H)\ll H^{2-\kappa}X^{1+o(1)},
\]

then

\[
\boxed{
\int|E_X|^2\ll T^\kappa X^{1-\kappa+o(1)}.}
\]

For `X=T^alpha`, the `X`-exponent is `1-kappa+kappa/alpha`. A fixed `kappa<1` can only exclude `delta>(1-kappa)/2`; sparse completeness needs essentially `kappa=1`.

### Rounds 58--59 — amplification no-go and RH-strength variance endpoint

Fixed powers, tensor moments, and scale iteration do not improve the signal/noise exponent ratio. Polynomial conformal amplification returns to modified Li.

Moreover, the natural sparse-complete Poisson-scale PNT variance is itself RH-strength. If for one fixed `lambda>1` and every `epsilon>0`

\[
\boxed{
\int_X^{2X}|R(\lambda x)-R(x)|^2dx
\ll_{\lambda,\epsilon}X^{2+\epsilon},
\qquad R(x)=\psi(x)-x,}
\]

then RH follows by Mellin continuation. Therefore the final variance bound cannot be promoted as an unexplained missing lemma.

### Rounds 60--61 — connected-correlation amplification and the fourth-order barrier

Connected `2r`-point statistics can in principle produce an off-line phase-free factor `X^(2r delta)` and thereby escape the homogeneous no-go if connected arithmetic background grows sublinearly in `r`.

But order-by-order implementation requires prime correlations of order `2r`. Pair data fail already at fourth order. The fourth cumulant contains the irreducible four-shift term

\[
\sum_n\prod_{j=1}^4(\Lambda(n+h_j)-1)
\]

minus the three pair contractions. Covariance does not determine this term; Gaussian and Rademacher fields provide an abstract counterexample with equal variance and different fourth cumulants.

Thus pair correlation cannot generate the connected hierarchy by itself.

## Source status corrections

- Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh `arXiv:2306.04799` is published in *Acta Arithmetica* 214 (2024), 357--376, DOI `10.4064/aa230612-20-3`, and is Tier A.
- Montgomery--Soundararajan, *Primes in Short Intervals*, CMP 252 (2004), is Tier A and is used only as structural evidence for the cumulant/high-moment barrier; its Gaussian program is not an unconditional all-orders theorem.
- Modern unconditional almost-all short-interval prime results must not be substituted for the global Selberg `L^2` estimate required by Round 57 without quantitative exceptional-tail control.

## Current new-tool map

### A — fractional Selberg / long-DP variance

**LEGITIMATE PARTIAL TARGET.** A fixed positive saving `kappa` could yield a genuine horizontal zero-free band. This would be real progress even though it is not RH-complete.

### B — sparse-complete Poisson variance

**RH-STRENGTH ENDPOINT.** Benchmark only unless derived from a lower-level independent structure.

### C — Gaussian-window prime cancellation

**OPEN.** Removes hard zero-window transfer but requires a new arithmetic cancellation theorem for exact log-Gaussian weights.

### D — connected correlations order by order

**AMPLIFICATION VALID, IMPLEMENTATION DEMOTED.** Pair data fail at order four and an unbounded prime-tuple hierarchy is not a finite mechanism.

### E — one finite all-orders arithmetic factorization/operator

**HIGHEST INVENTION PRIORITY.** Seek one prime-side structural theorem generating or controlling connected correlations of all orders without assuming Hardy--Littlewood for every tuple.

Admissible shapes include an Euler/local-prime cluster generator with a rigorous global-coupling correction, a trace/Fredholm determinant from a prime-side operator, a convergent cluster expansion, a martingale/dependency decomposition, or a Hermitian explicit-formula factorization with an RH-independent contraction estimate.

Every proposal must be rejected if it is merely Euler-product analytic continuation, Weil positivity, modified Li, generalized Laguerre positivity, or the full prime-tuple hierarchy in new notation.

## Invention ranking

For invention value, not theorem strength,

\[
\boxed{E>A_{\rm partial}\gtrsim C>D_{\rm order-by-order}.}
\]

The older local heat-flow routes remain valid diagnostics but are no longer the primary invention target.

## Round 62 invention gate

The next round must start prime-side, not by postulating an operator whose spectrum is the zero set.

Construct the lowest-complexity generating functional from local prime/divisor variables and compare its logarithmic fourth coefficient with the exact four-shift cumulant of `Lambda`.

Mandatory falsification test:

> If the local/Euler-product predicted fourth connected coefficient differs from the true von-Mangoldt fourth cumulant by a main-order term, naive local independence is refuted. Isolate that mismatch and ask whether it is a bilinear/dispersion correction already controlled by sieve or large-sieve technology.

Promotion gate:

1. the construction must be defined prime-side without unknown zero locations;
2. its second and fourth connected coefficients must be derived, not postulated;
3. any mismatch at fourth order must be bounded using a theorem weaker than Hardy--Littlewood for all quadruples;
4. the same structure must plausibly generate higher connected orders from one uniform estimate;
5. it must have an application outside RH, for example to long Dirichlet-polynomial variance or short-interval prime fluctuations.

If the fourth-order mismatch is main order and irreducible to controlled bilinear/dispersion input, the naive local-prime generator is rejected and the precise missing global-coupling correction becomes the next new-tool target.

A parallel lower-risk branch should seek a fixed fractional `kappa>0` variance saving for the exact triangular/Gaussian weights, since even a partial horizontal zero-free band would be a genuine theorem and a useful testbed.

**No proof of RH is claimed. Novelty remains unverified.**