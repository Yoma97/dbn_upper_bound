# Round 68 — Certified extension from `lambda=7.10` to `lambda=7.04`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED + directed-rounding certification at 512 and 768 bits.  
**Novelty:** NOVELTY_UNVERIFIED.

## Theorem

For every real `x` and

\[
0<t\le\frac12,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge7.04,
\]

one has

\[
\boxed{(H_t(x),H_t'(x))\ne(0,0).}
\]

The new strip `7.04<=lambda<=7.10` is certified here. Round 67 covers `7.10<=lambda<=10.52`, and the earlier high-shoulder theorem covers `lambda>=10.52`.

## Why a new grid was needed

At `t=1/2`, the `K=128` convex-tail envelope used for the `7.10` theorem has its own artificial sign transition near `lambda=7.0745`. This is not a failure of the actual PSC. Increasing the exact finite head moves that envelope floor sharply:

\[
K=256:\ 7.0499\ldots,
\qquad
K=512:\ 7.0393\ldots,
\qquad
K=1024:\ 7.03708\ldots.
\]

Thus the previous `7.10` threshold was partly an enclosure artifact. The present certification uses `K=1024`.

## Global error audit

For `lambda>=7.04`, `t<=1/2`, one has

\[
L\ge14.08,
\qquad
x\ge4\pi e^{14.08}>1.6371\times10^7.
\]

The same unconditional Polymath error decomposition and normalization audit as in Round 67, with the safe edge exponent `1.378`, gives by directed rounding

\[
e_A+e_B\le1.878431151090433\times10^{-6},
\]

\[
e_{C,0}\le6.049827029894499\times10^{-5},
\]

\[
E_{\rm jump}\le1.854344836031237\times10^{-4}.
\]

Therefore

\[
E_0\le2.478111850531591\times10^{-4}<3\times10^{-4},
\]

and, using the safe normalization ratio `exp(0.026L)`,

\[
E_1\le3.573612252303242\times10^{-3}<4\times10^{-3}.
\]

The 512- and 768-bit audits agree outward.

## True-weight box envelope

The analytic envelope is exactly the one proved in Round 67:

- exact finite head;
- cutoff constraint
  \[
  \lambda\ge\max(\lambda_a,2t\log n)-2\times10^{-6};
  \]
- optimized three-branch exponent in `u=log n`;
- convex secant for the first counting-measure branch;
- exact exponential integral for the second;
- decreasing finite-segment bound for the third.

The only changes are:

1. `K=1024`;
2. the lambda interval is `7.04<=lambda<=7.10`;
3. the grid is adaptively refined near `t=1/2`, where the true finite-time obstruction is located.

The time partition has 83 boxes:

- `(0,0.45]` in steps of `0.01`;
- `[0.45,0.49]` in steps of `0.002`;
- `[0.49,0.498]` in steps of `0.001`;
- `[0.498,0.5]` in steps of `0.0002`.

The lambda interval is divided into 60 boxes of width `0.001`. Thus

\[
83\times60=4980
\]

boxes cover the full new strip.

## 512-bit result

```text
boxes=4980 fail=0
minimum_margin_lower=0.00040963841947196192
worst_t=[0.499800,0.500000]
worst_lambda=[7.040000,7.041000]
worst_A0_upper=0.75326441340950723
worst_A1_upper=1.7291497771607698
GRID_RESULT pass=1
```

## 768-bit independent precision rerun

Because `K=1024` makes a monolithic 768-bit run unnecessarily slow in the execution environment, the identical source was compiled with four disjoint `ILO/IHI` ranges. The four chunks cover all 83 time boxes exactly:

- `[0,25)`: 1500 boxes, `fail=0`;
- `[25,50)`: 1500 boxes, `fail=0`;
- `[50,73)`: 1380 boxes, `fail=0`;
- `[73,83)`: 600 boxes, `fail=0`.

Total: 4980 boxes, no overlap gap, total `fail=0`. The global minimum is again

\[
\boxed{0.00040963841947196192>0}
\]

in the final chunk and the same worst box.

## Reproducibility

Canonical files:

- `research_lab/certificates/low_shoulder/convex_tail_psc_lambda704_mpfr.c`
- `research_lab/certificates/low_shoulder/convex_tail_psc_lambda704_512.txt`
- `research_lab/certificates/low_shoulder/convex_tail_psc_lambda704_768_chunks.txt`
- `research_lab/certificates/low_shoulder/lambda704_error_audit.c`
- `research_lab/certificates/low_shoulder/lambda704_error_512.txt`
- `research_lab/certificates/low_shoulder/lambda704_error_768.txt`

The convex-tail source supports compile-time `ILO/IHI`, so the chunked 768 audit is reproducible from exactly the same program.

## Circularity audit

No RH-equivalent statement is used. Inputs are the unconditional positive-time Polymath approximation, the elementary PSC implication, explicit Gamma-factor derivatives, elementary convexity/monotonicity, and directed-rounding arithmetic. No zero-spacing, global real-rootedness, GUE/pair correlation, generalized Laguerre positivity, or finite RH verification enters.

## Interpretation

The project certified threshold is now

\[
\boxed{C_{\rm certified}=7.04.}
\]

This is a genuine improvement from `10.52` and then `7.10`. It is still far above the small-time triangle-envelope transition `lambda_*=4.914588956...`.

The next obstruction is now visibly **finite-time**, concentrated at `t=1/2`. Finer interval subdivision alone cannot cross the pointwise `K=1024` PSC envelope floor near `7.0371`; to go materially lower one must either enlarge/replace the exact head or use a stronger joint `(p,p')` certificate. This is a different obstruction from the asymptotic `lambda_*` floor.
