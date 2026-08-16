# Singular-scaling literature survey V1

**Target regime**

` t -> 0+,  x -> infinity,  lambda=t log(x/(4 pi)) in a fixed compact interval.`

**Date:** 2026-08-16  
**RH status:** OPEN.

## Main finding

A targeted search did **not** reveal a ready-made theorem that directly supplies a uniform collision-exclusion criterion for `(H_t,H_t')` in the full fixed-lambda double scaling. The closest existing machinery is already concentrated in D.H.J. Polymath's effective heat-flow Riemann--Siegel expansion and its Section 9 asymptotics, which refine Ki--Kim--Lee.

Therefore the program should not restart from general heat-flow theory. It should extract a sharper **uniform fixed-lambda asymptotic** from the existing Polymath formula.

## Closest literature

### D.H.J. Polymath (2019/2020)

Theorem 1.3 gives the effective heat-flow Riemann--Siegel approximation with heat weights

`b_n^t = exp((t/4) log^2 n)`

and an effective shifted exponent `s_*`. Section 9 proves Theorem 1.5: for `x>=exp(C/t)` the `n=1` terms dominate and the zeros become real, simple and approximately regularly spaced.

This is precisely adjacent to the desired scaling, because `x=exp(lambda/t)` makes the shifted real exponent approach a finite lambda-dependent value rather than infinity. Thus the fixed-lambda regime is the **transition region before n=1 dominance**.

### Ki--Kim--Lee (2009)

For each fixed positive heat parameter, all but finitely many zeros are real and simple. The result is qualitative in the present singular limit; it does not give a ready uniform threshold as `t->0`.

### de Bruijn / strong universal factor theory

Strip contraction explains why positive heat flow drives zeros toward the real axis and supplies structural localization. Existing formulations do not appear to resolve the fixed-lambda transition where the spatial scale grows exponentially as time vanishes.

### Rodgers--Tao

Their detailed zero-dynamics estimates are designed for the contradiction regime `Lambda<0` and rely on already-real/simple zeros in the relevant interval. They are not an admissible black-box proof of simplicity in our unknown positive-time singular wedge.

### 2026 PF5 result

The original de Bruijn--Newman kernel is certified not PF5. Hence total positivity / PF_infinity of the original kernel cannot be the missing fixed-lambda theorem.

## Natural limiting object already exposed by our calculations

For fixed `n` and fixed lambda,

`a_n(t,lambda) -> n^{-(1/2+lambda/4)}`

as `t->0+`.

Thus the positive amplitude moments converge to zeta/Dirichlet moments. In particular the old triangle PSC has limiting sign

`t*T(t,lambda) -> (lambda/2)(2-zeta(1/2+lambda/4))`,

with its intrinsic scalar sign floor at

`lambda_* = 4.914588956...`.

This shows that a fixed-lambda asymptotic theorem is feasible, but also that **triangle-envelope information alone cannot be expected to reach lambda=0**. A successful singular theorem must retain phase/correlation information discarded by the scalar PSC.

## Recommended analytic extraction

Start from Polymath Theorem 1.3, not from the original Fourier integral. In the scaling `L=lambda/t`, derive uniform expansions on compact lambda intervals for

- `sigma(t,lambda)` and `tau(t,lambda)`;
- common phase derivative `phi_x` after multiplication by the natural `1/t` scale;
- heat amplitudes `a_n` including the first `O(t log^2 n)` correction;
- the normalized complex sum `S_t` and its derivative;
- Polymath errors after the same normalization.

The desired theorem should have the form

`scaled collision functional = limiting lambda-functional + explicit o(1)`

uniformly for lambda in a compact interval.

The limiting functional should be phase-sensitive. Candidate objects are the exact collision-conditioned invariant

`J = phi_x |S|^2 + Im(conj(S) S_x)`

and the exact joint-jet determinant/Euclidean criterion already developed in the project.

## Concrete research sequence

1. Freeze `lambda` in a compact interval, initially `[lambda0,6.83]` with `lambda0` chosen above the triangle floor.
2. Derive uniform first- and second-order expansions from the exact Polymath `s_*`, `M_t`, `alpha`, and cutoff formulas.
3. Prove a dominated-convergence/tail lemma uniform in lambda for `S_t`, `S_x`, and the relevant quadratic phase invariant.
4. Identify the limiting phase-sensitive collision functional.
5. Numerically map its sign before attempting a theorem; this tells us whether the invariant has a structural floor.
6. If positive on a lambda interval, turn the numerical map into an analytic lower bound plus explicit small-t remainder.
7. Use validated computation only for the complementary `t>=epsilon(lambda)` compact region.

## What is now considered finished infrastructure

- general effective Riemann--Siegel derivation: use Polymath;
- far-tail real/simple zeros: use Polymath Theorem 1.5 / KKL;
- strict explicit shoulder `lambda>=6.83`: Round 80;
- PF_infinity of the original kernel: impossible because not PF5;
- zero ODE as a primary simplicity proof: rejected by circularity/domain restriction.

The main invention budget should now be spent on the uniform phase-sensitive fixed-lambda limit.
