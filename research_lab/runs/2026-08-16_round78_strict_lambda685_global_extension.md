# Round 78 — Strict global shoulder extension to `lambda >= 6.85`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED + independent 512/768-bit certified arithmetic/box reruns.  
**Strict-program admissibility:** PASSED current direct/transitive audit.  
**Referee status:** PENDING.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Theorem

Let

\[
\lambda=t\log\frac{|x|}{4\pi}.
\]

On the canonical strict track, in which finite-height verification of RH is forbidden anywhere in the dependency closure,

\[
\boxed{
0<t\le\frac12,
\qquad
\lambda\ge6.85
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\tag{78.1}
\]

Hence

\[
\boxed{C_{\rm strict}=6.85.}
\tag{78.2}
\]

This improves Round 76 (`6.90`). It does not prove RH; the lower shoulder and bounded/core regimes remain open.

---

## 2. Four-piece strict proof cover

The new strip `6.85<=lambda<=6.90` is partitioned by time, then joined to Round 76.

### A. Small time

\[
0<t\le0.01,
\qquad
6.85\le\lambda\le6.90.
\]

Closed by an independent old-PSC scalar audit.

### B. Lower compact time

\[
0.01\le t\le0.39,
\qquad
6.85\le\lambda\le6.90.
\]

Closed by the old exact-weight PSC finite cover.

### C. Narrow APVC bridge

\[
0.39\le t\le0.40,
\qquad
6.85\le\lambda\le6.90.
\]

Closed by the hybrid PSC/APVC verifier after lowering the APVC activation gate to `t=0.39`. This whole rectangle is certified as a single box.

### D. Upper compact time

\[
0.40\le t\le0.50,
\qquad
6.85\le\lambda\le6.90.
\]

Closed by the previously completed hybrid PSC/soft-APVC cover with `K=768`.

Finally Round 76 covers every `lambda>=6.90`. These regions overlap on boundaries and leave no gap.

---

## 3. Small-time certificate

For `0<t<=0.01` and `lambda>=6.85`, the scalar proof uses deliberately weakened positive powers

\[
a_n\le n^{-1.962}
\quad(t\log n\le1),
\]

and

\[
a_n\le n^{-1.355}
\quad(t\log n>1)
\]

through the moving cutoff.

The Polymath remainders are enclosed by the padded channels

\[
e_A+e_B<512e^{-6.85/t},
\]

\[
e_{C,0}<e^{1-4.48/t},
\]

\[
E_{\rm jump}<8e^{-4.35/t},
\]

and the already audited symmetric-normalization bound

\[
|B_t/D_t|<e^{0.526/t+0.2}.
\]

The same source was compiled independently at 512 and 768 bits. Both runs gave the same outward decimal projections

\[
A_0\le0.79029481144039537,
\qquad
A_1\le1.1024916858605442,
\]

\[
S_0\ge0.20970518855960468,
\]

\[
E_0<9.66030175757482\times10^{-189},
\qquad
E_1<8.2364361699484526\times10^{-165},
\]

and final lower margin

\[
\boxed{70.715136308661144>0.}
\tag{78.3}
\]

Canonical files:

- `research_lab/certificates/low_shoulder/small_time_lambda685_audit.c`;
- `strict_small_time_lambda685_512.txt`;
- `strict_small_time_lambda685_768.txt`.

Actions run: `31925292154`.

---

## 4. Lower compact cover

The interval

\[
0.01\le t\le0.39,
\qquad
6.85\le\lambda\le6.90
\]

was covered by the old PSC verifier using `K=128`, directed MPFR arithmetic, and adaptive subdivision.

Both 512 and 768 bits returned identically:

- `3550` certified leaves;
- `0` unresolved leaves;
- exact root/certified area `0.0190`;
- coverage fraction `1`;
- minimum projected lower margin
  \[
  \boxed{0.001044027968617486>0};
  \]
- certified-manifest SHA256  
  `49ce2af659a22dbcf1785f563753f90f3bcc7e2d1629e3943628625b0a810dc6`;
- empty unresolved-manifest SHA256  
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

Actions run: `31925398246` (`low` jobs).

---

## 5. Why the original split at `t=0.40` was not optimal

The first old-PSC attempt on

\[
0.01\le t\le0.40,
\qquad
6.85\le\lambda\le6.90
\]

certified `99.95248317718505859375%` of the exact area but left `1993` terminal `PSC_CORE` boxes.

All were localized to

\[
0.3971435546875\le t\le0.4,
\]

\[
6.85\le\lambda\le6.8564208984375.
\]

Thus the failure was not a Polymath remainder, tail, or rounding obstruction. The administrative APVC activation boundary `t=0.40` simply sat slightly above the region where the old PSC first lost sign.

Lowering APVC activation to `t=0.39` is safe: the minimum Riemann--Siegel cutoff only grows as one moves to smaller `t` at fixed positive lambda, so the finite favorable `A1` head remains present with still larger slack.

---

## 6. Narrow APVC bridge

The new bridge

\[
0.39\le t\le0.40,
\qquad
6.85\le\lambda\le6.90
\]

was run with the same deterministic hybrid source generation, Round-74 soft cutoff-slope defect, and `K=768` favorable `A1` head.

At **both** 512 and 768 bits the entire rectangle was accepted at level zero as one certified box:

- `1` certified leaf;
- `0` unresolved;
- exact area `0.0005`;
- minimum margin
  \[
  \boxed{0.045343087717464883>0};
  \]
- certified SHA256  
  `25ef22025eee18a222e973ee58c5419f651a8a3afad2181e39822fa0768e4145`;
- unresolved SHA256  
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

Actions run: `31925456451`.

This confirms that the earlier 1993 old-PSC failures were certificate-boundary failures, not evidence of a collision or even difficult interval geometry.

---

## 7. Upper compact cover

The interval

\[
0.40\le t\le0.50,
\qquad
6.85\le\lambda\le6.90
\]

had already been certified independently at 512 and 768 bits by the hybrid PSC/soft-APVC verifier with `K=768`:

- `2491` certified leaves;
- `0` unresolved;
- exact area `0.0050`;
- minimum margin
  \[
  \boxed{0.000052714776399973518>0};
  \]
- certified SHA256  
  `cc3cb2434f76519df67a68fc4b7653ea87919c88122eb91ce55353d59e570d13`;
- unresolved SHA256  
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

Actions run: `31925300280` (`high` jobs).

---

## 8. Dependency audit

Used on the strict route:

- unconditional analytic D.H.J. Polymath effective Riemann--Siegel estimates (Theorem 1.3 / Corollary 6.5 and explicit errors);
- exact heat weights;
- old phase-slope certificate;
- Round-74 APVC and soft cutoff-slope defect;
- positive finite-head / convex-tail bounds;
- Cauchy derivative control and symmetric normalization;
- directed MPFR 512/768-bit arithmetic;
- exact finite partition accounting.

Not used, directly or transitively on this proof path:

- RH;
- `Lambda<=0` or `Lambda=0`;
- Polymath Theorem 1.1 `Lambda<=0.22`;
- finite-height verification of RH;
- all-real zeros of `H_0`;
- zero-spacing/GUE assumptions;
- Laguerre--Polya membership;
- Rodgers--Tao estimates whose proof begins inside a negative-`Lambda` contradiction setup.

Round 77 explains why the mathematically unconditional `Lambda<=0.22` shortcut belongs only to the separate unrestricted track.

---

## 9. Status

The canonical strict frontier is now

\[
\boxed{C_{\rm strict}=6.85.}
\]

Labels:

- `INTERNALLY_PROVED`;
- `512/768-BIT CERTIFIED`;
- `STRICT DEPENDENCY AUDIT PASSED INTERNALLY`;
- `REFEREE_VERIFIED: PENDING`;
- `NOVELTY_UNVERIFIED`;
- `RH: OPEN`.

The unrestricted published-input track remains at `C_U=6.19`, but is noncanonical under the project's finite-height-verification prohibition.

---

## 10. Next target

The pointwise soft-APVC diagnostic at `t=1/2` places its finite-time sign boundary near `lambda≈6.8188`. Therefore the next target should be chosen close enough to test the actual APVC frontier but with nontrivial proof slack.

The next certification target is

\[
\boxed{C_{\rm strict,target}=6.83.}
\]

Execution order:

1. certify the small-time strip by old PSC;
2. identify how far downward in `t` the old PSC remains sufficient;
3. use soft APVC on the upper corner;
4. if residual boxes are interval/majorant losses, deploy Round-75 convex-secant APVC;
5. if a genuine pointwise APVC failure appears, stop subdivision and move to the phase-sensitive invariant `J` / exact joint-jet.
