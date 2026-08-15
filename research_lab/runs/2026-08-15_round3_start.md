# RH Mathematical Invention Lab — Round 3 Start

**Date:** 2026-08-15 (Africa/Tripoli)

**Status:** Candidate reduction and proof obligations. No proof of RH is claimed.

## 1. First-principles target

Write

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Xi(z)=\xi\!\left(\frac12+iz\right).
\]

Then \(\Xi\) is a real even entire function and RH is equivalent to all zeros of \(\Xi\) being real.

The spectral-approximant program seeks entire functions \(E_j\) which are real-rooted because they arise from finite selfadjoint problems, and which converge to \(\Xi\). The finite-level real-rootedness mechanism is available in current spectral work under explicit hypotheses; the limiting convergence is the hard step.

---

## 2. General closure lemma

If \(E_j\) are entire, all zeros of every \(E_j\) are real, the family is locally bounded on \(\mathbb C\), and \(E_j\to\Xi\) on any set with a finite accumulation point, then Montel + the identity theorem give locally uniform convergence on \(\mathbb C\), and Hurwitz forces all zeros of \(\Xi\) to be real.

Thus zero-by-zero spectral convergence is unnecessary.

---

## 3. New reduction: normality from uniform exponential localization

Let the finite approximant be represented, after centering and canonical normalization, as

\[
E_j(z)=\int_{\mathbb R}\psi_j(x)e^{izx}\,dx,
\]

where \(\psi_j\) is the finite-level extremal/ground-state eigenfunction extended by zero outside its interval.

### Proposition (sufficient localization criterion)

If for every \(R>0\)

\[
\boxed{
\sup_j\int_{\mathbb R}e^{R|x|}|\psi_j(x)|\,dx<\infty,
}
\]

then \(\{E_j\}\) is locally bounded on \(\mathbb C\).

### Proof

For \(|z|\le R\),

\[
|E_j(z)|
\le\int|\psi_j(x)|e^{|\Im z||x|}\,dx
\le\int|\psi_j(x)|e^{R|x|}\,dx.
\]

Taking the supremum gives a bound independent of \(j\). ∎

This converts the abstract normal-family problem into a concrete operator/eigenfunction localization problem.

### Why ordinary normalization is insufficient

If \(\psi_j\) is merely \(L^2\)-normalized on an interval of length \(L_j\to\infty\), Paley–Wiener/Cauchy–Schwarz only gives bounds growing like \(e^{R L_j/2}\). Therefore local normality cannot be obtained from finite support and selfadjointness alone. A genuine **arithmetic confinement/localization law** is required.

---

## 4. Moment version of the same mechanism

Suppose, in addition to uniform exponential localization, there exists a limiting kernel \(\Phi\) with \(\widehat\Phi=\Xi\) such that for every nonnegative integer \(k\),

\[
\int x^k\psi_j(x)\,dx
\longrightarrow
\int x^k\Phi(x)\,dx.
\]

Then the Taylor coefficients satisfy

\[
E_j^{(k)}(0)
=i^k\int x^k\psi_j(x)\,dx
\longrightarrow
\Xi^{(k)}(0).
\]

The uniform exponential-moment bounds control the Taylor tails uniformly on compact sets, hence

\[
\boxed{E_j\to\Xi\quad\text{locally uniformly on }\mathbb C.}
\]

Therefore a second concrete formulation of the missing bridge is:

> **Uniform Exponential Localization + Spectral Moment Identification.**

This may be more accessible than direct determinant convergence because moments can potentially be expressed through traces, matrix elements, or derivatives of finite-prime determinant formulas.

**Status:** PROVED REDUCTION; MODEL-SPECIFIC HYPOTHESES NOT PROVED.

---

## 5. Smallest genuinely new theorem sought

### Arithmetic Confinement Theorem — candidate

For the canonically centered finite-prime extremal states \(\psi_{N,\lambda}\) associated with the spectral/Weil approximants, prove a parameter-independent exponential localization law

\[
\boxed{
\forall R>0\quad
\sup_{(N,\lambda)\in\mathcal C}
\int e^{R|x|}|\psi_{N,\lambda}(x)|\,dx<\infty
}
\]

along a cofinal regime \(\mathcal C\), using only the finite-prime Weil form, its archimedean term, and selfadjoint/operator estimates.

This theorem is strictly a statement about a family of eigenfunctions/operators. It does not mention zero locations of \(\zeta\) and is not formally an RH criterion by definition. It would have independent value in spectral approximation theory if proved under general hypotheses.

### Remaining independent obligation

Localization alone does not identify the limit. One must also prove an anchor/moment identification with the Riemann kernel or \(\Xi\) from the prime-side construction. This obligation must remain logically separate.

---

## 6. Counterexample pressure test

The candidate confinement theorem is not automatic for generic selfadjoint finite-interval problems. Ground states can delocalize as the interval grows. Therefore any proof must use arithmetic structure specific to the Weil/prime operator, not generic compactness rhetoric.

The main falsification task is to construct toy finite-prime/shift operators with the same formal symmetries but delocalized ground states. If such models exist, identify the additional quantitative feature of the true Weil form that prevents delocalization.

---

## 7. Round-3 proof obligations

1. Extract the exact centered eigenfunction \(\psi_{N,\lambda}\) and normalization from the current spectral construction.
2. Express its quadratic form explicitly as archimedean part plus finite prime-shift/correlation terms.
3. Derive coercive estimates strong enough to control exponential moments, or prove that such estimates cannot hold and replace them by a weaker normal-family criterion.
4. Express the first several moments of \(\psi_{N,\lambda}\) in terms of operator data/traces and compare with the inverse Fourier kernel of \(\Xi\).
5. Attack the conjectured confinement on toy models before any attempt to promote it.

The immediate research target is therefore no longer vague “spectral convergence”; it is the concrete inequality

\[
\sup_{N,\lambda}\|e^{R|x|}\psi_{N,\lambda}\|_{L^1}<\infty,
\]

or a demonstrably weaker operator estimate sufficient for Montel normality.