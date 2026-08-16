# Collision Program State — Round 47 addendum

**Date:** 2026-08-16

**RH status:** OPEN.

## Executive update

Rounds 39--47 materially sharpen the post-Round-38 program. The Gaussian-Hermite/Rayleigh bridge remains mathematically valid and has produced a genuine unconditional conversion from zeta growth estimates to collision-free positive-time regions. However, the route has now exposed a precise arithmetic bottleneck rather than a missing functional-analytic inequality.

The main live theorem is the two-saddle collision criterion from Round 42. For every `c>0`, define

\[
\mathcal Q_{c,t}(\gamma)
:=t\frac{\int_{\mathbb R}G_t(a)e^{-c|a|}
|\xi'(1/2+a+i\gamma)-c\,\operatorname{sgn}(a)\xi(1/2+a+i\gamma)|^2\,da}
{\int_{\mathbb R}G_t(a)e^{-c|a|}|\xi(1/2+a+i\gamma)|^2\,da}.
\]

If `H_t` has any multiple real zero at `x=2 gamma`, then

\[
\boxed{
\mathcal Q_{c,t}(\gamma)
\ge
\frac{2}{1+2/(c^2t)}.
}
\]

With the natural two-saddle choice

\[
c=\Re\alpha(1/2+i\gamma)
\sim\frac12\log(\gamma/2\pi),
\]

the threshold tends to `2` in the small-`t`, fixed-`lambda=t log(x/4pi)` scaling.

Round 43 converts a critical-line subconvexity exponent

\[
|\zeta(1/2+iT)|\ll T^{\theta+o(1)}
\]

into an asymptotic collision-free gate

\[
\boxed{\lambda>32\theta.}
\]

Using Bourgain's established

\[
\theta=13/84,
\]

this gives

\[
\boxed{
\lambda>104/21\approx4.95238095,
}
\]

which is close to but weaker than the separate existing program threshold

\[
\lambda_*\approx4.914588956.
\]

No improvement of the best program threshold is claimed.

---

## Round 39 — weight-only upper-bound no-go and exact zeta factorization

**PROVED.** For any positive integrable fixed weight `W`, the derivative Rayleigh quotient is unbounded over entire functions, as `Y_N(a)=e^{iNa}` gives quotient `N^2`. Therefore Poincare/log-concavity can supply lower coercivity but cannot upper-bound the Round-38 kinetic channel.

The normalized residual also admits the exact arithmetic factorization

\[
\frac{\xi(s)}{M_0(s)}=8E(s)\zeta(s),
\]

with Stirling correction

\[
\frac{E'}E
=-\frac1{6s^2}+O(|s|^{-4}).
\]

Thus the unknown kinetic channel is an exact nonsingular weighted quadratic form in `zeta` and `zeta'`, not a generic weight problem.

---

## Round 40 — constant coherent displacement

**PROVED theorem / later DEMOTED as high-height mechanism.** A multiplicity-`m` collision implies for every real constant `c`

\[
 t\frac{\int G_t e^{-ca}|\xi'-c\xi|^2}
 {\int G_t e^{-ca}|\xi|^2}
\ge2m.
\]

This follows from exact Gaussian completion and triangular Hermite translation. It is a valid family of necessary conditions.

---

## Round 41 — functional-equation two-saddle obstruction

**PROVED correction.** The functional equation gives

\[
f_\gamma(-a)=\overline{f_\gamma(a)},
\]

hence the constant-shift quotient is even in `c`.

In the exact symmetric model

\[
f(a)=\cosh(ua),
\]

the constant-shift quotient has global minimum at `c=0`. Therefore a single constant exponential gauge cannot be assumed to remove both reflected Archimedean lobes. This invalidates the one-lobe high-height heuristic, not the Round-40 theorem itself.

---

## Round 42 — two-saddle half-line Poincare criterion

**PROVED and LIVE.** The sign-adapted gauge

\[
g_c(a)=e^{-c|a|}\xi(1/2+a+i\gamma)
\]

preserves the first two collision moments exactly when paired with

\[
W_{c,t}=G_t e^{c|a|}.
\]

Reflection splits the collision constraints into a mean-zero condition for the real part and a first-moment-zero condition for the imaginary part on the positive half-line. Strong convexity of the shifted half-Gaussian gives the explicit all-multiplicity inequality

\[
\boxed{
\mathcal Q_{c,t}(\gamma)
\ge\frac{2}{1+2/(c^2t)}.
}
\]

The interface at `a=0` was audited: the gauge is Lipschitz, the first weak derivative has no delta term, and the odd imaginary component vanishes at the interface, so no boundary term is hidden.

---

## Round 43 — subconvexity-to-collision conversion

**PROVED asymptotic bridge.** Let

\[
L=\log(\gamma/2\pi),
\qquad \lambda=tL,
\qquad c=\Re\alpha(1/2+i\gamma).
\]

On the positive half-line the safe non-zeta rate is

\[
S_0(a;\lambda)=-a^2+\frac\lambda2a,
\]

with saddle

\[
a_*=\lambda/4,
\qquad
S_0(a_*)=\lambda^2/16.
\]

If

\[
|\zeta(1/2+iT)|\ll T^{\theta+o(1)}
\]

and `theta>=1/8`, Phragmen--Lindelof gives shoulder rate

\[
S_\theta(a;\lambda)
=-a^2+\frac\lambda2a+2\theta\lambda(1-2a),
\]

whose maximum on `[0,1/2]` occurs at `a=0` and equals `2 theta lambda`. Thus the safe saddle dominates iff

\[
\lambda>32\theta.
\]

For Bourgain `theta=13/84`, this gives `lambda>104/21`.

---

## Round 44 — exact critical-line endpoint bottleneck

**PROVED NO-GO.** Any pointwise interior exponent profile satisfying

\[
\mu(0)=\theta,
\qquad
\mu(a)\le\theta(1-2a)
\]

has the same variational maximum

\[
\sup_a\left(-a^2+\frac\lambda2a+2\lambda\mu(a)\right)
=2\theta\lambda.
\]

Therefore sharper fixed interior-strip pointwise bounds cannot move the collision gate while the critical-line exponent remains unchanged.

Andrew Yang's unconditional lines

\[
\sigma_k=1-\frac{k}{2^k-2},
\qquad
|\zeta(\sigma_k+iT)|\ll T^{1/(2^k-2)}\log T
\]

are genuine improvements inside the strip but do not alter this endpoint-dominated gate.

To beat the existing `lambda_*` by this architecture would require

\[
\boxed{
\theta<\lambda_*/32
\approx0.153580904875.
}
\]

Bourgain gives

\[
13/84\approx0.154761904762,
\]

so the miss is approximately `0.001180999887` in the critical-line exponent, or `0.03779199638` in lambda.

---

## Round 45 — delayed-gauge/spectral-gap tradeoff

**PROVED MODEL NO-GO.** Delaying the positive-half gauge by

\[
\phi_b(a)=c(a-b)_+
\]

raises the safe-core large-deviation rate by `lambda b/2`, apparently improving the shoulder comparison. But it creates a second well in the collision-orthogonality weight, separated from the boundary well by a barrier of depth `b^2/t`.

A direct Rayleigh test gives

\[
\lambda_1(W_{b,t})
\le t^{-O(1)}e^{-b^2/t}.
\]

Thus a fixed `b=O(1)` large enough to change the `1/t` exponent destroys the Poincare collision threshold exponentially. A delay small enough to preserve a polynomial spectral gap changes only subleading terms. This freezes the delayed scalar-gauge loophole.

---

## Round 46 — finite moment hierarchy cannot change the endpoint exponent

**PROVED NO-GO.** If an endpoint rate satisfies

\[
S(0)=S_0,
\qquad S'(0)<0,
\]

then for each fixed integer `r>=0`

\[
\int_0^\delta a^r e^{S(a)/t}da
\sim C_r t^{r+1}e^{S_0/t}.
\]

Hence fixed powers, fixed-degree Hermite weights, and finitely many fixed derivatives alter only polynomial factors in `t`, not the endpoint large-deviation exponent. Therefore using more of the finite collision moment hierarchy cannot lower `lambda>32 theta` as long as the shoulder is bounded pointwise.

---

## Round 47 — horizontal averaging is weighted subconvexity, not orthogonality

**PROVED STRUCTURAL REDUCTION.** At fixed ordinate,

\[
n^{-1/2-a-i\gamma}
=n^{-1/2}n^{-a}e^{-i\gamma\log n},
\]

so varying `a` changes only amplitudes, not phases.

For a Dirichlet polynomial

\[
D_\gamma(a)=\sum c_n n^{-a}e^{-i\gamma\log n},
\]

horizontal averaging gives exactly

\[
\int K(a)D_\gamma(a)da
=\sum c_n e^{-i\gamma\log n}\mathcal LK(\log n).
\]

For the square,

\[
\int K|D_\gamma|^2
=\sum_{m,n}c_n\overline{c_m}
 e^{-i\gamma\log(n/m)}\mathcal LK(\log(mn)).
\]

Thus horizontal averaging does not diagonalize the mean square; the kernel depends on `log(mn)`, not `log(n/m)`. It is a smooth positive reweighting of the same fixed-ordinate exponential-sum problem.

A shoulder improvement beyond Bourgain therefore requires a genuinely new smooth weighted exponential-sum/subconvexity estimate. It is not supplied for free by the Gaussian/horizontal average.

---

## Source guard update

The source registry now records:

- Bourgain's published critical-line exponent `13/84` as Tier A;
- Yang's interior-strip bounds as Tier B/current-preprint input, with an explicit note that Round 44 prevents them from moving the endpoint gate by themselves.

Rodgers--Tao negative-time local-equilibrium estimates remain unsafe for proving `Lambda<=0`, because their quantitative regime is developed under the contradiction hypothesis `Lambda<0`.

---

## Program ranking after Round 47

The old labels `A`, `B`, `C` should now be refined.

### A1 — local entropy/Vandermonde/Laguerre closure

**FROZEN as primary.** Exact identities are retained, but the independent finite entropy/resultant budget is equivalent locally to a transversality lower bound, and generic kernel/Laguerre variants have hit structural barriers.

### A2 — Gaussian-Hermite / two-saddle Rayleigh bridge

**VALID CONDITIONAL ARITHMETIC BRIDGE.** This is genuine progress: it converts any suitable zeta growth/exponential-sum theorem into a collision-free lambda region. With current input it gives `lambda>104/21`, slightly weaker than the existing `lambda_*`.

Do not spend further rounds here unless one of the following appears:

1. a critical-line exponent below `0.153580904875...`;
2. a special smooth weighted fixed-ordinate exponential-sum estimate beating Bourgain for the exact collision weights;
3. an arithmetic identity coupling the weighted value and derivative combination more strongly than separate subconvexity bounds.

### B — topological collision degree

**LOCAL theorem retained / GLOBAL route secondary.** Local degree remains `-floor(m/2)`, but raw/global winding reduces to real-zero-count spectral flow and is not an independent closure.

### P0 — cross-frontier sparse-exception/explicit-formula bridge

**PROMOTED to next invention priority.** The next round should seek an observable for which one positive-time collision or one off-critical orbit at `t=0` creates a defect that is amplified by an already controlled statistic, rather than another universal kernel inequality.

Candidate interfaces:

- horizontal multiplicity / equal-ordinate symmetric pairs;
- pair correlation with explicit horizontal displacement weights;
- Weil/explicit-formula tests localized to a single off-line quartet but with an independently controlled prime-side norm;
- heat-flow collision defect transported to an arithmetic statistic at `t=0`.

Every candidate must pass the sparse-exception test: a single off-line quartet cannot be dismissed merely because its density is zero.

---

## Immediate next step

The next invention round should start from the minimal RH-false orbit

\[
\rho=\beta+i\gamma,
\quad
1-\beta+i\gamma,
\quad
\overline\rho,
\quad
1-\overline\rho,
\qquad \beta\ne1/2,
\]

and search for a quantitatively amplified defect in a statistic that has an unconditional evaluation or upper bound.

The first rejection test is severe:

> if the statistic changes by only `O(1)` per off-line orbit while its known error is `omega(1)` or its main term grows with height, it cannot exclude a sparse exceptional orbit and must not be promoted.

**No proof of RH is claimed. Novelty remains unverified unless separately checked.**
