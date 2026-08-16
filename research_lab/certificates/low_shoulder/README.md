# Low-shoulder certificate bundle — strict vs unrestricted state

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Referee verification:** PENDING.  
**Novelty:** UNVERIFIED.

This directory tracks two logically distinct proof policies. They must not be conflated.

---

## 1. Canonical strict track

The project constitution forbids finite-height verification of RH anywhere in the global proof dependency closure.

The strongest currently certified strict shoulder theorem is Round 78:

\[
\boxed{
0<t\le\frac12,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge6.85
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\]

Hence

\[
\boxed{C_{\rm strict}=6.85.}
\]

Status:

- `INTERNALLY_PROVED`;
- `512/768-BIT DIRECTED-ROUNDING CERTIFIED`;
- strict direct/transitive dependency audit passed internally;
- `REFEREE_VERIFIED: PENDING`;
- `NOVELTY_UNVERIFIED`;
- RH remains OPEN.

### Round-78 proof cover

1. `0<t<=0.01`, `6.85<=lambda<=6.90`: old PSC scalar audit;
2. `0.01<=t<=0.39`, `6.85<=lambda<=6.90`: old PSC finite box cover;
3. `0.39<=t<=0.40`, `6.85<=lambda<=6.90`: one-box hybrid PSC/APVC bridge;
4. `0.40<=t<=0.50`, `6.85<=lambda<=6.90`: hybrid PSC/soft-APVC finite cover;
5. `lambda>=6.90`: Round 76.

Small-time 512/768 outputs both give

\[
A_0\le0.79029481144039537,
\quad
A_1\le1.1024916858605442,
\]

\[
S_0\ge0.20970518855960468,
\]

\[
E_0<9.66030175757482\times10^{-189},
\quad
E_1<8.2364361699484526\times10^{-165},
\]

with final margin

\[
70.715136308661144>0.
\]

Lower compact cover `0.01<=t<=0.39`:

- 3550 certified leaves;
- 0 unresolved;
- exact area `0.0190`;
- min margin `0.001044027968617486`;
- identical 512/768 certified SHA  
  `49ce2af659a22dbcf1785f563753f90f3bcc7e2d1629e3943628625b0a810dc6`.

Narrow APVC bridge `0.39<=t<=0.40`:

- 1 certified leaf at both precisions;
- 0 unresolved;
- exact area `0.0005`;
- margin `0.045343087717464883`;
- identical certified SHA  
  `25ef22025eee18a222e973ee58c5419f651a8a3afad2181e39822fa0768e4145`.

Upper compact cover `0.40<=t<=0.50`:

- 2491 certified leaves;
- 0 unresolved;
- exact area `0.0050`;
- min margin `0.000052714776399973518`;
- identical certified SHA  
  `cc3cb2434f76519df67a68fc4b7653ea87919c88122eb91ce55353d59e570d13`.

Canonical strict tools:

- `small_time_lambda685_audit.c`;
- `strict_small_time_lambda685_512.txt`;
- `strict_small_time_lambda685_768.txt`;
- `convex_tail_psc_box_mpfr.c`;
- `adaptive_psc_lambda_tiler.py`;
- `make_hybrid_apvc_verifier.py`;
- `soften_hybrid_apvc.py`;
- `lower_apvc_activation.py`;
- Round 74 APVC and soft cutoff-slope addendum;
- Round 75 convex-secant APVC (reserved sharpening).

The next strict target is

\[
\boxed{C_{\rm strict,target}=6.83.}
\]

A 512/768 diagnostic has been launched with old PSC on lower time and soft APVC on the upper corner. `6.83` is not proved unless and until a complete cover and small-time audit pass.

---

## 2. Unrestricted unconditional published-input track

If all mathematically unconditional published results are admitted regardless of their computational proof ancestry, the project also has

\[
\boxed{C_U=6.19.}
\]

This route uses the published D.H.J. Polymath theorem

\[
\Lambda\le0.22
\]

to remove all `t>0.22`, together with a K=2048 direct PSC certificate on `0<t<=0.22`.

The `6.19` theorem is mathematically unconditional in the usual sense, but it is **not canonical on the strict track** because the proof of Polymath Theorem 1.1 uses a finite-height numerical verification of RH as an ingredient in its upper-bound criterion. Round 77 records the transitive dependency audit.

Thus:

\[
\boxed{C_U=6.19,\qquad C_{\rm strict}=6.85.}
\]

The distinction is methodological, not a claim that the published `Lambda<=0.22` theorem is conditional.

---

## 3. Strict admissible analytic inputs

The strict route uses the analytic effective Riemann--Siegel estimates in D.H.J. Polymath Theorem 1.3 / Corollary 6.5. Their analytic proof is separate from the finite-height numerical-verification hypothesis used for Theorem 1.1.

The strict route does **not** use, directly or transitively:

- RH;
- `Lambda<=0` or `Lambda=0`;
- Polymath Theorem 1.1 `Lambda<=0.22`;
- finite-height RH verification;
- all-real zeros of `H_0`;
- GUE/pair correlation as proof facts;
- Laguerre--Polya membership;
- negative-time Rodgers--Tao estimates whose proof starts inside a `Lambda<0` contradiction setup.

---

## 4. Current mathematical frontier

The old triangle PSC has small-time asymptotic sign floor

\[
\lambda_*=4.914588956\ldots,
\]

which is not a collision threshold.

The active finite-time obstruction occurs much higher, near `t=1/2`. Round 74's anchored phase-velocity certificate materially improved this corner. Its pointwise diagnostic boundary at `t=1/2` is near `lambda≈6.8188`; this number is **heuristic/diagnostic, not a theorem**.

The current execution order is:

1. test strict `6.83` with old PSC + soft APVC;
2. if only majorant/interval losses remain, deploy Round-75 convex-secant APVC;
3. if a genuine pointwise APVC failure persists, stop subdivision and move to the phase-sensitive invariant `J` or exact joint-jet certificate;
4. keep the Round-65 small-time PSC as the stronger singular-limit mechanism.

RH remains OPEN.
