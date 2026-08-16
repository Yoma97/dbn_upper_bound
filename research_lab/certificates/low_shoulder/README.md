# Low-shoulder certificate bundle — strict vs unrestricted state

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Referee verification:** PENDING.  
**Novelty:** UNVERIFIED.

This directory tracks two logically distinct proof policies.

## 1. Canonical strict track

The project forbids finite-height verification of RH anywhere in the global proof dependency closure.

Round 81 currently gives

\[
\boxed{
0<t\le1/2,
\quad
\lambda=t\log(|x|/(4\pi))\ge6.50
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\]

Thus

\[
\boxed{C_{\rm strict}=6.50.}
\]

Status: `INTERNALLY_PROVED`, `512/768-BIT DIRECTED-ROUNDING CERTIFIED`, strict dependency audit passed internally, `REFEREE_VERIFIED: PENDING`, `NOVELTY_UNVERIFIED`, RH OPEN.

### Clean Round-81 cover

1. `0<t<=0.01`, `6.50<=lambda<=10.52`: old exact-weight PSC scalar audit.
2. `0.01<=t<=0.50`, `6.50<=lambda<=7.08`: Round-80 JECC finite box cover.
3. `lambda>=7.08`: previous strict shoulder theorem.

Small-time 512/768 outputs agree:

\[
A_0\le0.89710880510761826,
\quad
A_1\le1.3361223014476078,
\]

\[
S_0\ge0.10289119489238177,
\]

\[
E_0\le2.2738911968749703\times10^{-171},
\quad
E_1\le1.9387344381641930\times10^{-147},
\]

with PSC margin

\[
32.098785970075724>0.
\]

Canonical files:

- `small_time_lambda650_audit.c`;
- `strict_small_time_lambda650_512.txt`;
- `strict_small_time_lambda650_768.txt`.

Actions run: `31926284003`.

### Unified JECC bridge

Domain:

\[
0.01\le t\le0.50,
\quad
6.50\le\lambda\le7.08.
\]

Both 512 and 768 bits returned identically:

- 4423 certified leaves;
- 0 unresolved;
- exact area `0.2842`;
- minimum lower margin `0.00008429498363186757`;
- certified-manifest SHA256  
  `596acdf4b1442088e23afc6c2a6a4e352d3b633c9358b1f98caaa3aaa0ce3811`;
- empty unresolved SHA256  
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

Canonical workflow:
`.github/workflows/strict-jecc-650-to708-audit.yml`

Actions run: `31926430064`.

### JECC

Round 80 couples value and derivative in one normalized Euclidean vector. Every collision must satisfy

\[
1\le
A_0+
\frac{\sigma_x}{\Phi}A_1+
\frac12\sqrt{E_0^2+(E_1/\Phi)^2},
\qquad
\Phi=|\phi_x|,
\]

provided `T log N <= 2 Phi`, `T=-tau_x>0`. The box verifier uses only upper enclosures and no rapidly varying phase sampling.

The current termwise operator-norm form has a structural `A0=1` floor; at `t=1/2` the diagnostic frontier is near `lambda≈6.458`, not a theorem.

The next strict target is

\[
\boxed{C_{\rm strict,target}=6.47.}
\]

## 2. Unrestricted published-input track

If all mathematically unconditional published theorems are admitted regardless of computational proof ancestry, the separate Track U has

\[
\boxed{C_U=6.19.}
\]

It uses Polymath's unconditional theorem `Lambda<=0.22`. That theorem's proof ancestry includes finite-height numerical verification of RH, so Track U is mathematically unconditional but noncanonical under the stricter project policy. See Round 77.

Thus currently

\[
\boxed{C_U=6.19,\qquad C_{\rm strict}=6.50.}
\]

## 3. Strict admissible inputs

The strict route uses the analytic effective Riemann--Siegel estimates in D.H.J. Polymath Theorem 1.3 / Corollary 6.5 and explicit error bounds. It does not use Polymath Theorem 1.1, finite-height RH verification, RH, `Lambda<=0`, `Lambda=0`, all-real zeros of `H_0`, GUE/pair correlation as proof facts, Laguerre--Polya membership, or negative-time Rodgers--Tao estimates whose proof lies inside a `Lambda<0` contradiction setup.

## 4. Current frontier

The old small-time triangle-PSC floor remains

\[
\lambda_*=4.914588956\ldots,
\]

which is not a collision threshold.

JECC dramatically improves the finite-time corner while preserving the same small-time asymptotic floor. The next step is to certify `6.47`; if persistent `JOINT_CORE` failure appears near `t=1/2`, the project must stop termwise operator-norm refinement and switch to a phase-correlated tool such as `J=Im(conj(Z) Z_x)` or a prime-fiber/torus-block joint certificate.

RH remains OPEN.
