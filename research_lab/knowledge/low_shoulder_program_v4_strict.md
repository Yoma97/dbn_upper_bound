# Low-Shoulder Program V4 — strict dependency policy

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Canonical policy:** finite-height verification of RH is forbidden anywhere in the global proof dependency closure.

---

## 1. Current strict theorem

The canonical strict shoulder result is Round 76:

\[
\boxed{
0<t\le1/2,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge6.90
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\]

Hence

\[
\boxed{C_{\rm strict}=6.90.}
\]

The mathematically unconditional `6.19` result based on the published Polymath bound `Lambda<=0.22` is retained on a separate unrestricted track only, because the proof ancestry of that published theorem contains finite-height RH verification.

---

## 2. Completed analytic infrastructure

### Exact weights — Round 64

For fixed lambda on compact subsets of `(4,infinity)`,

\[
A_0\to\zeta(1/2+\lambda/4)-1,
\qquad
A_1\to-\zeta'(1/2+\lambda/4),
\]

with explicit uniform remainders.

### Scaled PSC — Round 65

\[
 t\mathcal T(t,\lambda)
\to
\frac\lambda2\left[2-\zeta(1/2+\lambda/4)\right].
\]

The asymptotic sign floor of the unchanged triangle envelope is

\[
\lambda_*=4.914588956\ldots,
\]

not a collision threshold.

### Practical tails — Round 66

Finite true-weight heads plus convex/secant positive tails provide rigorous parameter-box bounds without summing to the astronomical Riemann--Siegel cutoff.

### Finite-time stronger certificate — Round 74

At a hypothetical collision,

\[
|\cos\phi|\le A_0+E_0/2,
\]

and therefore

\[
|\sin\phi|\ge\sqrt{1-(A_0+E_0/2)^2}.
\]

The derivative tail can be bounded by the soft APVC estimate

\[
B_1\le(\Phi+2\delta_N)A_0-(T-\sigma_x)A_1,
\]

where

\[
\Phi=|\phi_x|,
\qquad T=-\tau_x,
\qquad
\delta_N=(T\log N-\Phi)_+.
\]

This is the active finite-time complement to the old PSC.

### Secant sharpening — Round 75

For

\[
\omega(\ell)=\sqrt{(\sigma_x\ell)^2+(\Phi-T\ell)^2},
\]

convexity gives a sharper affine secant majorant and hence a stronger APVC derivative-tail bound. Use it only when the simpler soft APVC leaves residual boxes.

---

## 3. Strict Round-76 proof cover

The theorem `C_strict=6.90` is the union of:

1. `0<t<=0.01`, `6.90<=lambda<=7.08`: directed scalar old-PSC audit;
2. `0.01<=t<=0.40`, `6.90<=lambda<=7.08`: old PSC finite cover;
3. `0.40<=t<=0.50`, `6.90<=lambda<=7.08`: hybrid PSC/soft-APVC finite cover;
4. `lambda>=7.08`: previously certified strict shoulder theorem.

All compact covers were independently rerun at 512 and 768 bits with zero unresolved leaves.

---

## 4. Active target

The next target is

\[
\boxed{C_{\rm target}=6.85.}
\]

Do not claim it until all three required pieces are certified:

### A. Small time

Prove `0<t<=0.01`, `6.85<=lambda<=6.90` by the old PSC with conservative positive power bounds and a separate 512/768-bit scalar audit.

### B. Lower compact time

Attempt the old PSC first on

\[
0.01\le t\le0.40,
\qquad
6.85\le\lambda\le6.90.
\]

If any terminal failures remain, classify them before invoking APVC.

### C. Upper compact time

Use the hybrid PSC/soft-APVC verifier on

\[
0.40\le t\le0.50,
\qquad
6.85\le\lambda\le6.90.
\]

Start with a finite lower `A1` head no larger than the minimum cutoff; `K=768` is expected to remain safe in the worst corner, but the minimum cutoff must be certified rather than assumed.

If soft APVC leaves only interval/majorant failures, deploy Round-75 secant APVC. If pointwise APVC fails under shrinking boxes, stop subdividing and change the certificate.

---

## 5. Failure taxonomy

Every unresolved leaf must be classified as one of:

- `TYPE II`: interval enclosure inflation;
- `TYPE III`: Polymath remainder dominates;
- `TYPE IV-A`: value anchor `A0+E0/2<1` fails;
- `TYPE IV-B`: APVC velocity majorant dominates;
- `TYPE IV-C`: pointwise APVC core tends to zero/negative;
- `TYPE V`: cutoff or partition artifact;
- `TYPE VI`: not yet identified.

A failure of a certificate is never evidence of a collision by itself.

---

## 6. Invention gate after APVC

If a genuine pointwise APVC obstruction is localized, the next candidate is not deeper blind subdivision.

Use the exact collision-conditioned invariant

\[
J=\phi_x|S|^2+\Im(\overline S S_x),
\]

or the already established exact joint-jet criterion. These retain complex phase correlations discarded by scalar positive majorants.

Only if the collision-side program reaches a structural floor should the prime-side connected/factorization route from Rounds 48--61 return to primary status.

---

## 7. Forbidden dependencies on the strict track

Do not use, directly or transitively:

- RH;
- `Lambda<=0` or `Lambda=0`;
- finite-height verification of RH as a global proof dependency;
- real-rootedness of `H_0`;
- GUE or pair correlation as proof facts;
- generalized Laguerre positivity equivalent to Laguerre--Polya membership;
- Rodgers--Tao estimates whose local proof begins inside a `Lambda<0` contradiction setup.

The published theorem `Lambda<=0.22` is mathematically unconditional but is excluded from the strict track because its proof uses finite-height RH verification. See Round 77.

The analytic effective Riemann--Siegel estimates of Polymath remain admissible when their own proof does not use that finite-height verification input.

---

## 8. Governing execution rule

\[
\boxed{
\text{prove with existing certificate}
\to
\text{localize genuine pointwise failure}
\to
\text{invent only the missing structure}
\to
\text{certify at 512/768 bits}
\to
\text{audit the full dependency closure}.
}
\]

Current strict status:

\[
\boxed{C_{\rm strict}=6.90,\qquad C_{\rm target}=6.85,\qquad RH\text{ OPEN}.}
\]
