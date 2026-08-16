# Collision Program State — Round 67 addendum

**Date:** 2026-08-16  
**RH status:** OPEN.

## Executive update

Rounds 63--67 materially change the allocation of the project.

The high-shoulder theorem

\[
\lambda=t\log\frac{|x|}{4\pi}\ge10.52
\Longrightarrow
(H_t,H_t')\neq(0,0)
\]

has survived a hostile directed-rounding re-audit and is now backed by corrected 512/768-bit V2 artifacts.

The main short-horizon route is the exact-weight phase-slope Low-Shoulder program. The prime-side all-orders program from Rounds 48--61 remains a logically separate long-horizon backstop.

---

## 1. Corrected high-shoulder foundation

The first imported scalar/moment MPFR helpers contained formal mixed-direction rounding defects. Round 67 corrected them and reran both 512-bit and 768-bit audits.

Canonical corrected scalar contradiction margin:

\[
\boxed{0.0051784077356494497>0.}
\]

Thus

\[
\boxed{C_{\rm proved}=10.52}
\]

remains valid.

Canonical files:

- `certificates/high_shoulder/high_shoulder_lambda1052_audit.c`
- `certificates/high_shoulder/high_shoulder_lambda1052_audit_512.txt`
- `certificates/high_shoulder/high_shoulder_lambda1052_audit_768.txt`
- `certificates/high_shoulder/dirichlet_tail_moments_mpfr_512.c`
- `certificates/high_shoulder/dirichlet_tail_moments_p1814_512.txt`
- `certificates/high_shoulder/dirichlet_tail_moments_p1814_768.txt`

Knowledge correction:

- `knowledge/high_shoulder_lambda1052_v2_correction.md`

The old decimal values in `high_shoulder_lambda1052_proposition.md` are superseded by this correction; the theorem statement is unchanged.

---

## 2. Round 64 — exact-weight moment collapse

**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.

For every compact `K subset (4,infinity)`, the true heat weights satisfy explicit uniform estimates yielding

\[
A_0(t,\lambda)\to
\zeta\left(\frac12+\frac\lambda4\right)-1,
\]

\[
A_1(t,\lambda)\to
-\zeta'\left(\frac12+\frac\lambda4\right)
\]

as `t->0+` at fixed `lambda`.

The proof is direct: a summable power majorant plus `e^r-1<=r e^r` gives an explicit `O(t)` moment error and an exponentially small moving-cutoff tail.

---

## 3. Round 65 — scaled transversality law

**Truth status:** INTERNALLY_PROVED, with a separate hostile normalization-ratio audit.  
**Novelty:** NOVELTY_UNVERIFIED.

The correct scaled observable is

\[
\widetilde{\mathcal T}=t\mathcal T.
\]

On every compact

\[
K\subset(\lambda_*,10.52],
\]

Round 65 obtains

\[
t\Phi\to\lambda/4,
\qquad
d\to1/2,
\qquad E_0\to0,
\qquad tE_1\to0,
\]

and therefore

\[
\boxed{
 t\mathcal T(t,\lambda)
\to
\frac\lambda2
\left[
2-\zeta\left(\frac12+\frac\lambda4\right)
\right]
}
\]

uniformly on `K`.

The symmetric normalization comparison was rederived correctly using Schwarz conjugation and a short horizontal segment. The deliberately looser exponential ratio used in Round 65 remains safe.

---

## 4. Correct meaning of lambda_*

Let `p_*` solve

\[
\zeta(p_*)=2
\]

and

\[
\lambda_*=4(p_*-1/2)=4.914588956\ldots.
\]

The only justified interpretation is:

\[
\boxed{
\lambda_*\text{ is the asymptotic sign floor of the unchanged }n=1
\text{ triangle-envelope component of PSC in fixed-lambda small time}.}
\]

It is not a collision threshold, not a universal PSC floor, and not a finite-time obstruction.

---

## 5. Round 66 — practical convex-tail engine

**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.

Round 64 is excellent for the limit but conservative for practical constants near `lambda_*`, because its global `q>1` moment majorant produces large `Z_2(q),Z_3(q)`.

Round 66 replaces it by:

1. an exact finite head;
2. a closed-form tail bound obtained from convexity of the counting-measure exponent
   \[
   g(v)=\frac t4v^2-(\underline\sigma-1)v;
   \]
3. `O(K)` evaluation cost independent of the astronomical Riemann--Siegel cutoff.

This is now the preferred engine for practical threshold improvement.

A floating/high-precision exploratory scan suggests `lambda=7.10` as the first target, but

\[
\boxed{7.10\text{ is NOT proved}.}
\]

No project status may call it a certified or proved threshold until a complete cover is obtained.

---

## 6. Canonical program

Future execution follows

`knowledge/low_shoulder_program_v2_1.md`.

The old V2 is superseded.

Current proof cover:

### H — CLOSED

\[
\lambda\ge10.52.
\]

### M1 — ANALYTICALLY REDUCED

For every fixed `epsilon>0`, sufficiently small `t` on

\[
\lambda_*+\epsilon\le\lambda\le10.52
\]

is collision-free by Rounds 64--65. A practical certified decimal `t_epsilon` is still needed.

### M2 — OPEN FINITE CERTIFICATION

\[
t_\epsilon\le t\le1/2,
\qquad
\lambda_*+\epsilon\le\lambda<10.52.
\]

### L — OPEN NEW-MECHANISM REGION

Below the triangle floor, the scalar `S0=1-A0` certificate must be changed rather than indefinitely refined.

### B — OPEN BOUNDED SPATIAL CORE

Requires a separate compact analytic/validated cover.

---

## 7. Immediate next execution

### P0 — theorem reconstruction

Before promoting Rounds 64--65 beyond `INTERNALLY_PROVED`, perform a fresh proof reconstruction from only:

- frozen theorem statements;
- Polymath Theorem 1.3 definitions and inequalities;
- convention lock.

### P1 — first real threshold attack

Implement a directed-rounding `(t,lambda)` evaluator using Round 66.

First falsification/certification target:

\[
\boxed{\lambda\ge7.10.}
\]

The evaluator must return, per box:

- `A0,A1,S0`;
- `Phi,d`;
- `E0,E1`;
- cutoff bridge data;
- PSC margin;
- dominant loss channel.

Run 512 bits first and independently rerun every accepted leaf at 768 bits.

### P2 — promotion rule

Only if the exact union of certified leaves covers

\[
0<t\le1/2,
\qquad
7.10\le\lambda\le10.52
\]

with the small-time analytic bridge covering the singular end, may the project update

\[
C_{\rm proved}:10.52\to7.10.
\]

Failure must be classified rather than hidden by deeper subdivision.

---

## 8. Circularity lock

The Low-Shoulder Track A may use unconditional Polymath effective approximation, elementary complex analysis, positive-series bounds, and certified arithmetic.

It may not use:

- RH;
- `Lambda<=0` or `Lambda=0`;
- real-rootedness of `H_0`;
- finite-height RH verification as a global input;
- pair correlation/GUE as proof facts;
- negative-time Rodgers--Tao estimates whose proof assumes `Lambda<0` for contradiction;
- an unexplained Laguerre/LP positivity statement strong enough to imply the target.

RH remains OPEN.
