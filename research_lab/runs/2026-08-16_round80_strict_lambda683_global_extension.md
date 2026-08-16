# Round 80 — Strict global shoulder extension to `lambda >= 6.83`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Status:** INTERNALLY_PROVED + independent 512/768-bit directed-rounding reruns.  
**Strict dependency policy:** no finite-height RH verification in the proof closure.

## Theorem

Let

`lambda = t log(|x|/(4 pi))`.

Then on the strict track

`0<t<=1/2` and `lambda>=6.83` imply `(H_t(x),H_t'(x)) != (0,0)`.

Hence the strict shoulder constant is now

`C_strict = 6.83`.

## Proof cover for the new strip `6.83<=lambda<=6.85`

### Small time: `0<t<=0.01`

Independent scalar old-PSC audit at 512 and 768 bits gives identical outward decimal projections:

- `A0 <= 0.7958361914458113`;
- `A1 <= 1.1140900271690237`;
- `S0 >= 0.20416380855418878`;
- `E0 <= 7.1380464216595624e-188`;
- `E1 <= 6.085944849914031e-164`;
- final lower margin `68.601539137861025 > 0`.

Canonical files:

- `small_time_lambda683_audit.c`;
- `strict_small_time_lambda683_512.txt`;
- `strict_small_time_lambda683_768.txt`.

### Lower compact time: `0.01<=t<=0.35`

Old exact-weight PSC with `K=128` closes the whole rectangle at both 512 and 768 bits:

- `3001` certified leaves;
- `0` unresolved;
- exact area `0.0068`;
- minimum projected lower margin `0.0018935088778644768`;
- certified CSV SHA256 `dba70fe15d56b232ab4da5677fa9fbb6b2ca2c10f04faf2841079d19c15fc2f3`;
- empty unresolved SHA256 `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

### Upper compact time: `0.35<=t<=0.50`

The soft APVC cover itself succeeds at 512/768 bits with zero unresolved leaves. An independent Round-75 convex-secant APVC rerun is substantially smaller and is adopted as the preferred certificate.

Round-75 secant APVC, `K=900`, both precisions:

- `6022` certified leaves;
- `0` unresolved;
- exact area `0.0030`;
- minimum projected lower margin `0.0000065899209774973451`;
- certified CSV SHA256 `852d8a9e5c78bcd41f88d6b8f43e721bf6d706c6e8ec6a5a41db570008d083c8`;
- empty unresolved SHA256 `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

The corresponding soft-APVC cover had `12862` leaves and minimum margin `3.7037303430001485e-6`, so the secant certificate roughly halves the leaf count while improving the weakest displayed margin.

## Union

Round 80 covers `6.83<=lambda<=6.85`. Round 78 covers `lambda>=6.85`. Therefore every `lambda>=6.83` is covered for `0<t<=1/2`.

## Dependency audit

Used:

- unconditional analytic Polymath Theorem 1.3 / Corollary 6.5 estimates;
- exact heat weights;
- PSC;
- anchored phase-velocity certificate;
- Round-75 convex-secant derivative-tail majorant;
- directed MPFR arithmetic;
- exact finite partition accounting.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- Polymath Theorem 1.1 `Lambda<=0.22`;
- finite-height RH verification;
- real-rootedness of `H_0`;
- zero-motion ODE in an unknown-simplicity regime;
- PF/total positivity assumptions.

## Consequence for program design

Together with Polymath Theorem 1.5 / Ki--Kim--Lee, this confirms that the real analytic frontier is the singular scaling

`t->0+`, `x->infinity`, `lambda=t log(x/(4pi))` bounded.

The current explicit strict certificate already removes the entire escaping region `lambda>=6.83`. Future invention should target the remaining bounded lambda window rather than rebuild global large-x theory.

`REFEREE_VERIFIED: PENDING`.  
`NOVELTY_UNVERIFIED`.  
`RH: OPEN`.
