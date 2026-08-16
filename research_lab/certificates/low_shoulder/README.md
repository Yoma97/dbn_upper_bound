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

## Canonical dependency graph after hostile audit

The published unconditional Polymath theorem

\[
\Lambda\le0.22
\]

removes the whole interval `t>0.22` from the multiple-real-zero problem. A local Hermite collision argument proves that every zero is simple for every `t>Lambda`: a hypothetical multiplicity-`m>=2` real zero, evolved a sufficiently small distance backward in heat time, has local scaled model

\[
e^{+\partial_w^2}w^m=i^{-m}Q_m(iw),
\]

where `Q_m=e^{-\partial_w^2}w^m` is the monic Hermite collision polynomial with distinct real zeros; hence the backward model has a genuinely nonreal zero, contradicting real-rootedness at any time still strictly above `Lambda`.

The endpoint `t=0.22` is **not** discarded and is explicitly covered by PSC.

After Round 75's hostile dependency audit, the canonical proof is the union of exactly these three regions:

1. `0<t<=0.22`, `6.19<=lambda<=7.08`: direct K=2048 true-weight PSC certificate, independently rerun at 512 and 768 bits;
2. `0<t<=0.22`, `lambda>=7.08`: the hostile-audited robust `lambda>=7.08` shoulder theorem;
3. `0.22<t<=1/2`, every real `x`: interior simplicity from `t>Lambda` and unconditional `Lambda<=0.22`.

**No historical `lambda>=7.04` certificate is used in the canonical proof graph.**

Primary theorem/audit notes:

- `research_lab/runs/2026-08-16_round73_lambda619_via_upper_bound_reduction.md`;
- `research_lab/runs/2026-08-16_round75_lambda619_hostile_dependency_audit.md`;
- robust bridge: `research_lab/runs/2026-08-16_round73_lambda708_global_extension.md`.

Because the research history contains two files carrying the label `Round 73`, use full filenames or threshold labels rather than the bare round number.

## Canonical lambda-6.19 sources

Base K=2048 verifier and error audit:

- `convex_tail_psc_lambda619_mpfr.c`;
- `lambda619_error_audit.c`;
- `lambda619_error_512.txt`;
- `lambda619_error_768.txt`.

Hostile-audited direct bridge to `7.08`:

- `extend_lambda619_to708.py` — deterministic transformation of the committed K=2048 verifier;
- `convex_tail_psc_lambda619_to708_512.txt`;
- `convex_tail_psc_lambda619_to708_768_chunks.txt`.

Original K=2048 verifier SHA256:

`2f3baa98f8c8e289fe6ee7aa270196c2fc4757a8230378c2a6ca861c4164f040`.

Generated `[6.19,7.08]` verifier SHA256, identical in all 512/768 hostile-audit jobs:

`376b2d065089da19c3f878c432fbf265e51d2567130ca729972835930b89196d`.

Error-verifier SHA256 recorded before commit:

`bc2ea71b968e26034f502744e9871aea416617cc128f4f97b98c8cf0983de1b6`.

## Error audit at the worst geometric endpoint

At

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
\qquad
\boxed{E_1\le2.1869579473011833\times10^{-6}}.
\]

The K=2048 PSC grid deliberately uses the much weaker padded values

\[
E_0=10^{-3},
\qquad
E_1=0.02,
\]

so the final sign certificate is insensitive to microscopic error-audit changes.

## Exact hostile-audited finite cover

The time interval `[0,0.22]` is partitioned into 32 exact rational boxes:

- 18 boxes of width `0.01` on `[0,0.18]`;
- 6 boxes of width `0.005` on `[0.18,0.21]`;
- 4 boxes of width `0.002` on `[0.21,0.218]`;
- 4 boxes of width `0.0005` on `[0.218,0.22]`.

The lambda interval `[6.19,7.08]` is partitioned into 89 exact rational boxes of width `0.01`.

Total:

\[
\boxed{32\times89=2848\text{ boxes}.}
\]

Every acceptance decision is made using MPFR-directed rational endpoints. Binary floating point is used only for printed diagnostics.

### 512-bit monolithic result

```text
PSC lambda [6.19,7.08] t<=0.22 PREC=512 ibox=[0,32) boxes=2848 fail=0
minimum_margin_lower=0.049218384939129022
worst_t=[0.219500,0.220000] lambda=[6.1900,6.2000]
A0_upper=0.82853202750245358 A1_upper=2.3383369555918039
GRID_RESULT pass=1
```

### 768-bit independent rerun

The identical generated source was rebuilt at 768 bits and run in four disjoint time-index chunks. Each chunk contains 712 boxes and returns `fail=0`:

- `[0,8)`: minimum margin `12.456560911890461`;
- `[8,16)`: minimum margin `3.0034496597067775`;
- `[16,24)`: minimum margin `0.30040464591597071`;
- `[24,32)`: minimum margin `0.049218384939129022`.

Together the chunks exhaust all 2848 boxes. The global weakest box agrees exactly with the 512-bit run:

\[
t\in[0.2195,0.22],
\qquad
\lambda\in[6.19,6.20].
\]

## Historical certified layers retained only as cross-checks

The following remain useful regressions but are not needed in the canonical `6.19` dependency graph:

- corrected `lambda>=10.52` high-shoulder certificate;
- `lambda>=7.10` global PSC theorem;
- robust `lambda>=7.08` theorem (this one **is** used as the upper bridge);
- older `lambda>=7.04` / `7.039` finite-time certificates.

The old finite-time obstruction near `t=1/2` is globally irrelevant after using the unconditional `Lambda<=0.22` reduction.

## Circularity audit

The canonical `lambda>=6.19` theorem uses only:

- unconditional published `Lambda<=0.22`;
- the local heat/Hermite splitting proving simplicity for `t>Lambda`;
- unconditional D.H.J. Polymath effective Riemann--Siegel estimates on `0<t<=0.22`;
- phase-slope transversality algebra;
- true heat weights with a finite head and positive convex/exponential tail majorants;
- the fixed-cutoff one-jump bridge;
- Schwarz symmetry and Cauchy's estimate;
- MPFR directed rounding and exact finite partition accounting.

It does **not** use RH, `Lambda<=0`, `Lambda=0`, real-rootedness at any `t<=0.22`, zero-spacing assumptions, GUE/pair correlation, generalized Laguerre positivity, or Rodgers--Tao estimates whose proof begins from a negative-`Lambda` contradiction hypothesis.

Using the known coarse bound `Lambda<=0.22` is not circular with the eventual target `Lambda<=0`: it eliminates only times already known to lie strictly inside the real-rooted regime, while the boundary `t=0.22` is independently covered.

## Current project constant and open frontier

\[
\boxed{C_{\rm project-proved}=6.19.}
\]

This is an internally proved/certified shoulder theorem, **not a proof of RH**. Independent referee reconstruction remains pending and novelty is unverified.

The next quantitative bottleneck is now the terminal line `t=0.22` near `lambda=6.19`. The deeper structural frontier remains the small-time fixed-lambda sign floor

\[
\lambda_*=4.914588956\ldots,
\]

which is not itself a collision threshold and cannot be crossed by merely pretending the existing triangle-envelope sign persists.

RH remains OPEN.
