# Low-shoulder certificate bundle — canonical state

This directory contains the current finite/analytic proof layer for the project shoulder theorem

\[
0<t\le\frac12,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge6.19
\quad\Longrightarrow\quad
(H_t(x),H_t'(x))\ne(0,0).
\]

**Current status:** `INTERNALLY_PROVED + 512/768-BIT DIRECTED-ROUNDING CERTIFIED`; `REFEREE_VERIFIED: PENDING`; `NOVELTY_UNVERIFIED`; RH remains OPEN.

The key logical improvement over the older `7.08/7.04/7.039` certificates is that the published unconditional Polymath theorem

\[
\Lambda\le0.22
\]

removes the whole interval `t>0.22` from the multiple-real-zero problem. A local Hermite collision argument proves that every zero is simple for every `t>Lambda`. Therefore PSC only has to cover `0<t<=0.22`; the endpoint `t=0.22` remains included because equality `Lambda=0.22` is not excluded by the published upper bound.

The canonical proof is therefore the union of:

1. `0<t<=0.22`, `6.19<=lambda<=7.04`: the new K=2048 true-weight PSC certificate below;
2. `0<t<=0.22`, `lambda>=7.04`: the already certified historical shoulder chain;
3. `0.22<t<=1/2`, every real `x`: interior simplicity from `t>Lambda` and unconditional `Lambda<=0.22`.

The theorem and circularity audit are recorded in

- `research_lab/runs/2026-08-16_round73_lambda619_via_upper_bound_reduction.md`.

Because the research history contains two independent files carrying the label `Round 73` (`lambda708` and `lambda619`), future references should use the full filename or the threshold label rather than the bare round number.

## Canonical lambda-6.19 sources

- `convex_tail_psc_lambda619_mpfr.c` — K=2048 directed-rounding PSC verifier;
- `convex_tail_psc_lambda619_512.txt` — monolithic 512-bit run;
- `convex_tail_psc_lambda619_768_chunks.txt` — independent 768-bit run in four disjoint time chunks;
- `lambda619_error_audit.c` — directed-rounding Polymath/Cauchy error audit;
- `lambda619_error_512.txt`;
- `lambda619_error_768.txt`.

Local source SHA256 values recorded before commit:

- K=2048 PSC verifier:  
  `2f3baa98f8c8e289fe6ee7aa270196c2fc4757a8230378c2a6ca861c4164f040`;
- error verifier:  
  `bc2ea71b968e26034f502744e9871aea416617cc128f4f97b98c8cf0983de1b6`.

## Error audit

At the worst geometric endpoint

\[
t=0.22,
\qquad
\lambda=6.19,
\qquad
L=\frac{619}{22}=28.13636\ldots,
\]

both 512- and 768-bit directed-rounding audits certify

\[
e_A+e_B\le7.2420515225931095\times10^{-12},
\]

\[
e_{C,0}\le1.6509274020979614\times10^{-8},
\]

\[
E_{\rm jump}\le8.871220157240477\times10^{-8},
\]

hence

\[
\boxed{E_0\le1.0522871764490697\times10^{-7}},
\]

and, after the symmetric normalization/Cauchy factor,

\[
\boxed{E_1\le2.1869579473011833\times10^{-6}}.
\]

The PSC grid deliberately uses the much weaker padded constants

\[
E_0=10^{-3},
\qquad
E_1=0.02,
\]

so the final box certification is not sensitive to microscopic changes in the error audit.

## Exact lambda-6.19 finite cover

The time interval `[0,0.22]` is partitioned exactly into 32 rational boxes:

- 18 boxes of width `0.01` on `[0,0.18]`;
- 6 boxes of width `0.005` on `[0.18,0.21]`;
- 4 boxes of width `0.002` on `[0.21,0.218]`;
- 4 boxes of width `0.0005` on `[0.218,0.22]`.

The lambda interval `[6.19,7.04]` is partitioned into 85 rational boxes of width `0.01`.

Total:

\[
32\times85=2720
\]

boxes. Every acceptance decision uses MPFR-directed rational endpoints; binary floating point is used only for printed diagnostics.

### 512-bit result

```text
PSC lambda [6.19,7.04] t<=0.22 PREC=512 ibox=[0,32) boxes=2720 fail=0
minimum_margin_lower=0.049218384939129022
worst_t=[0.219500,0.220000] lambda=[6.1900,6.2000]
A0_upper=0.82853202750245358 A1_upper=2.3383369555918039
GRID_RESULT pass=1
```

### 768-bit result

The same source was rebuilt at 768 bits and run on four disjoint time-index chunks. Each chunk contains 680 boxes and returns `fail=0`; together they exhaust all 2720 boxes. The global minimum is again

\[
\boxed{0.049218384939129022>0}
\]

on the same terminal box

\[
t\in[0.2195,0.22],
\qquad
\lambda\in[6.19,6.20].
\]

Thus the new finite-time bottleneck has moved from the old neighborhood of `t=1/2` to the genuine terminal time `t=0.22`.

## Historical certified layers retained as cross-checks

These files remain useful for independent regression but are no longer the canonical threshold:

- `lambda>=10.52` corrected high-shoulder V2 certificate;
- `lambda>=7.10` global PSC theorem;
- `lambda>=7.08` small-time + quadtree bridge;
- `lambda>=7.04` K=1024 certified extension;
- narrow strip `[7.039,7.040]`, K=1130, with 2420 boxes and minimum margin `8.1308819976975806e-05`.

The older finite-time obstruction near `t=1/2` is now logically irrelevant to the global collision problem because `t>0.22` lies strictly above the known unconditional upper bound for `Lambda`.

## Mathematical dependency and circularity

The `lambda>=6.19` theorem uses only:

- the unconditional published bound `Lambda<=0.22`;
- the local heat/Hermite splitting of a hypothetical multiple real zero, to prove simplicity for `t>Lambda`;
- unconditional D.H.J. Polymath effective Riemann--Siegel bounds on `0<t<=0.22`;
- phase-slope transversality algebra;
- true heat weights with a finite head and convex/exponential positive-tail envelopes;
- the fixed-cutoff one-jump bridge;
- Schwarz symmetry and Cauchy's estimate;
- MPFR directed rounding and exact finite partition accounting.

It does **not** use RH, `Lambda<=0`, `Lambda=0`, real-rootedness at any `t<=0.22`, zero-spacing assumptions, GUE/pair correlation, generalized Laguerre positivity, or Rodgers--Tao estimates whose proof begins with a negative-`Lambda` contradiction hypothesis.

Using the known coarse unconditional upper bound `Lambda<=0.22` is not circular with the target `Lambda<=0`: it removes only a region already known to lie strictly inside the real-rooted regime.

## Current project constant and open frontier

\[
\boxed{C_{\rm project-proved}=6.19.}
\]

This is a genuine shoulder improvement, **not a proof of RH**.

The next quantitative PSC frontier is the terminal line `t=0.22` below `lambda=6.19`. A direct non-rigorous moment diagnostic suggests some further improvement toward roughly `lambda~6.1` may be available by enlarging the exact head/refining the terminal boxes.

The deeper structural frontier remains the small-time triangle-envelope sign floor

\[
\lambda_*=4.914588956\ldots,
\]

which is not a collision threshold. Below that value the unchanged `n=1` triangle-envelope mechanism loses its fixed-lambda asymptotic sign and a genuinely changed certificate is required.

RH remains OPEN.
