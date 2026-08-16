# Low-shoulder certificate bundle — strict vs unrestricted state

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Referee verification:** PENDING.  
**Novelty:** UNVERIFIED.

This directory now tracks **two logically different proof policies**. They must not be conflated.

---

## 1. Strict project track — canonical for this research program

The user's research constitution forbids finite-height verification of RH from entering the global proof dependency closure.

Under that rule, the strongest currently certified shoulder theorem is Round 76:

\[
\boxed{
0<t\le\frac12,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge6.90
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\]

Thus

\[
\boxed{C_{\rm strict}=6.90.}
\]

Status:

- `INTERNALLY_PROVED`;
- `512/768-BIT DIRECTED-ROUNDING CERTIFIED`;
- direct/transitive dependency audit currently passes the no-finite-height-RH-verification rule;
- `REFEREE_VERIFIED: PENDING`;
- RH remains OPEN.

Canonical strict ingredients:

- unconditional analytic effective Riemann--Siegel estimates of D.H.J. Polymath (Theorem 1.3 / Corollary 6.5 and explicit error bounds), not the paper's global `Lambda<=0.22` theorem;
- Round 64 exact-weight moment collapse;
- Round 65 scaled PSC limit;
- Round 66 true-weight convex tails;
- Round 74 anchored phase-velocity certificate (APVC) and its soft cutoff-slope addendum;
- MPFR 512/768-bit finite covers from Round 76.

Round-76 strict proof cover:

1. `0<t<=0.01`, `6.90<=lambda<=7.08`: old PSC scalar audit;
2. `0.01<=t<=0.40`, `6.90<=lambda<=7.08`: old PSC full box cover;
3. `0.40<=t<=0.50`, `6.90<=lambda<=7.08`: hybrid PSC/APVC cover;
4. `lambda>=7.08`: previously certified strict shoulder theorem.

Key Round-76 certificates:

- `small_time_lambda690_audit.c`;
- `small_time_lambda690_audit_512.txt`;
- `small_time_lambda690_audit_768.txt`;
- `convex_tail_psc_box_mpfr.c`;
- `make_hybrid_apvc_verifier.py`;
- `soften_hybrid_apvc.py`;
- `adaptive_psc_lambda_tiler.py`.

The high-time hybrid cover at `K=512` had, identically at 512 and 768 bits:

- `409` certified leaves;
- `0` unresolved;
- exact area `0.0180`;
- minimum lower margin `0.000013123697123932965`;
- certified-manifest SHA256  
  `d2d632971fcc3f0bbfcecc41e674005e1aeaa4cc48ed58b9ed70572a2bc12734`.

The lower-time cover had:

- `3301` certified leaves;
- `0` unresolved;
- exact area `0.0702`;
- minimum lower margin `0.0083044035209287551`;
- certified-manifest SHA256  
  `d09a13b1fb2d17cba892d2bf6975b2ce002c405a240f09a999c90ee7a04fef0c`.

The next strict target is

\[
\boxed{C_{\rm strict,target}=6.85.}
\]

---

## 2. Unrestricted published-input track — useful but noncanonical here

If every mathematically unconditional published theorem is allowed as a black-box input regardless of its computational proof ancestry, Rounds 73/75 establish

\[
\boxed{C_{\rm unrestricted}=6.19.}
\]

using the published Polymath theorem

\[
\Lambda\le0.22
\]

to discard all times `t>0.22`, plus a K=2048 PSC certificate on `0<t<=0.22`.

The associated numerical certificate is substantial and remains valuable:

- direct rectangle `0<t<=0.22`, `6.19<=lambda<=7.08`;
- 2848 exact rational boxes;
- 512/768-bit reruns;
- weakest margin `0.049218384939129022`;
- no failed boxes.

Canonical unrestricted files include:

- `convex_tail_psc_lambda619_mpfr.c`;
- `lambda619_error_audit.c`;
- `lambda619_error_512.txt`;
- `lambda619_error_768.txt`;
- `extend_lambda619_to708.py`;
- `convex_tail_psc_lambda619_to708_512.txt`;
- `convex_tail_psc_lambda619_to708_768_chunks.txt`.

Original K=2048 source SHA256:

`2f3baa98f8c8e289fe6ee7aa270196c2fc4757a8230378c2a6ca861c4164f040`.

Generated `[6.19,7.08]` verifier SHA256:

`376b2d065089da19c3f878c432fbf265e51d2567130ca729972835930b89196d`.

---

## 3. Why `6.19` is not canonical on the strict track

The earlier hostile audit incorrectly stated that the `6.19` dependency graph did not use finite-height verification of RH.

That statement was correct only for the **direct** Round-73 code and false for the **transitive** dependency graph.

D.H.J. Polymath's proof of Theorem 1.1 (`Lambda<=0.22`) explicitly uses an upper-bound criterion whose hypothesis (i) is titled

`Numerical verification of RH at initial time 0`.

The paper applies the criterion with `X` close to `6 x 10^10` and explicitly explains that this choice is near the limit of the known numerical verification of RH needed for that hypothesis.

Therefore

\[
\text{finite-height RH verification}
\to
\Lambda\le0.22
\to
\text{time reduction}
\to
C=6.19.
\]

This does **not** make `Lambda<=0.22` conditional or mathematically circular. It is an unconditional published theorem. But it violates the stricter project rule that finite-height RH verification not appear anywhere in the proof ancestry.

The correction is formalized in:

`research_lab/runs/2026-08-16_round77_transitive_dependency_audit_lambda619.md`.

---

## 4. Interior simplicity lemma

The local lemma used on the unrestricted track remains valid:

\[
t>\Lambda
\Longrightarrow
\text{every zero of }H_t\text{ is simple}.
\]

If a real zero at `t_0>Lambda` had multiplicity `m>=2`, a sufficiently small backward heat step has scaled local leading model

\[
e^{+\partial_w^2}w^m=i^{-m}Q_m(iw),
\]

where `Q_m=e^{-\partial_w^2}w^m` has distinct real Hermite zeros. The backward model therefore has a nonreal zero, and Rouche/Hurwitz transfers it to the exact function at a nearby time still greater than `Lambda`, contradicting the definition of `Lambda`.

The lemma is not the problem; only the strict admissibility of the numerical value `0.22` is.

---

## 5. Current research frontier

For the canonical strict program:

\[
\boxed{C_{\rm strict}=6.90.}
\]

The immediate target is `6.85` using the hierarchy:

1. old exact-weight PSC for small and lower times;
2. Round-74 soft APVC for the finite-time upper corner;
3. Round-75 convex-secant APVC if residual boxes are due to majorant loss;
4. joint invariant `J` / exact joint-jet only after a genuine pointwise APVC obstruction is localized.

The deeper asymptotic sign floor of the unchanged triangle PSC remains

\[
\lambda_*=4.914588956\ldots,
\]

which is not a collision threshold.

RH remains OPEN.
