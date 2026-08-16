# Round 73 — Global project-certified shoulder extension to `lambda >= 7.08`

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED + independent 512/768-bit certified arithmetic/box reruns.  
**Referee status:** PENDING.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Theorem

Let

\[
\lambda=t\log\frac{|x|}{4\pi}.
\]

For every real `x` and

\[
0<t\le\frac12,
\qquad
\lambda\ge 7.08,
\]

one has

\[
\boxed{(H_t(x),H_t'(x))\ne(0,0).}
\tag{73.1}
\]

Within the project this replaces the previous proved shoulder constant `7.10` by

\[
\boxed{C_{\rm project-proved}=7.08.}
\tag{73.2}
\]

It does **not** prove RH. The region below `lambda=7.08`, together with the bounded/core regimes needed for global collision exclusion, remains open.

---

## 2. Three-piece cover

The proof is the union of three independently controlled regimes.

### Regime A — analytic small time

\[
0<t\le0.01,
\qquad
7.08\le\lambda\le10.52.
\]

This is a direct adaptation of Round 70 with all constants weakened monotonically for the new left endpoint.

### Regime B — compact certified strip

\[
0.01\le t\le0.5,
\qquad
7.08\le\lambda\le7.10.
\]

This is covered by the same rectangular true-weight PSC verifier and hardened adaptive tiler used in the `7.10` theorem, rerun independently at 512 and 768 bits.

### Regime C — previously proved region

\[
0<t\le0.5,
\qquad
\lambda\ge7.10.
\]

This is Round 71 / Round 72, which already includes the `lambda>=10.52` high-shoulder theorem and the `7.10<=lambda<=10.52` low-shoulder bridge.

The three regimes overlap at their boundaries and leave no gap above `7.08`.

---

## 3. Small-time analytic constants at `lambda=7.08`

Put

\[
L=\lambda/t.
\]

For `t<=0.01` and `lambda>=7.08`,

\[
L\ge708.
\]

The geometry audit used in Round 70 still has overwhelming slack: `e^7>1000` gives `e^{700}>10^{300}`, so the whole radius-`0.1` Cauchy disk lies at astronomically large real part. Every correction previously padded by `10^{-4}` remains much smaller than that padding.

On the real axis

\[
\sigma=\frac12+\frac\lambda4+\eta,
\qquad -10^{-4}<\eta\le0.
\tag{73.3}
\]

Split the true heat weights

\[
a_n=\exp\!\left(\frac t4\log^2n-\sigma\log n\right)
\]

using `u=t log n`.

For `u<=1`,

\[
\sigma-\frac t4\log n
>
\frac12+\frac{7.08}{4}-\frac14-10^{-4}
=2.0199,
\]

so the deliberately weakened power

\[
\boxed{a_n\le n^{-2.019}}
\tag{73.4}
\]

is valid.

For `u>1`, the moving-cutoff inequality gives

\[
\sigma-\frac t4\log n
>
\frac12+\frac{7.08}{8}-2\cdot10^{-4}
=1.3848,
\]

hence

\[
\boxed{a_n\le n^{-1.384}.}
\tag{73.5}
\]

Also `u>1` implies `log n>1/t>=100`.

The directed scalar sums then give

\[
A_0\le0.73098651914361068,
\]

\[
A_1\le0.98190929449905862,
\]

and therefore

\[
\boxed{S_0=1-A_0\ge0.26901348085638938.}
\tag{73.6}
\]

---

## 4. Small-time Polymath error channels

On the upper Cauchy semicircle, the first positive Polymath series has effective power greater than `1.384`, and after the `n^y` factor the second has effective power greater than `1.334`:

\[
\frac12+\frac{7.08}{8}-2\cdot10^{-4}=1.3848>1.384,
\]

\[
\frac{1-0.1}{2}+\frac{7.08}{8}-2\cdot10^{-4}=1.3348>1.334.
\]

Using `zeta(s)<=1+1/(s-1)` and the same large-height bounds as Round 70, the common prefactor remains below `8`. Consequently

\[
 e_A+e_B<128e^{-7.08/t}.
\tag{73.7}
\]

The `e_{C,0}` estimate uses only the weaker inequality `tL'>7`, which is still valid, and remains

\[
 e_{C,0}<e^{1-4.8125/t}.
\tag{73.8}
\]

For the one possible disk-local cutoff jump, the weaker exponent `1.334` gives

\[
\frac{1.334\cdot7.08}{2}=4.72236,
\]

so

\[
 E_{\rm jump}<6e^{-4.72236/t}.
\tag{73.9}
\]

The symmetric-normalization estimate is unchanged because it was derived uniformly with the upper lambda endpoint `10.52`:

\[
\left|\frac{B_t}{D_t}\right|<e^{0.526/t+0.2}.
\tag{73.10}
\]

Thus define

\[
E_0(t)=128e^{-7.08/t}+e^{1-4.8125/t}+6e^{-4.72236/t},
\tag{73.11}
\]

\[
E_1(t)=10e^{0.526/t+0.2}E_0(t).
\tag{73.12}
\]

All net decay exponents are positive. Both error envelopes increase with `t` on `(0,0.01]`, so it suffices to audit `t=0.01`.

The independent 512/768-bit MPFR runs give identical outward decimal projections:

\[
E_0<4.8829945288638576\times10^{-205},
\]

\[
E_1<4.1632729250572989\times10^{-181}.
\tag{73.13}
\]

The real-axis phase speed satisfies, from `L>=708`,

\[
\Phi>176.99,
\]

and as before

\[
d<0.501.
\]

Hence the phase-slope contradiction lower side is

\[
2\left[
\Phi\sqrt{S_0^2-(E_0/2)^2}-dA_1
\right]
\ge94.241518840456663.
\tag{73.14}
\]

Subtracting `E_1` leaves the certified positive margin

\[
\boxed{94.241518840456663>0.}
\tag{73.15}
\]

Therefore Regime A is closed.

Canonical source and outputs:

- `research_lab/certificates/low_shoulder/small_time_lambda708_audit.c`
- `research_lab/certificates/low_shoulder/small_time_lambda708_audit_512.txt`
- `research_lab/certificates/low_shoulder/small_time_lambda708_audit_768.txt`

GitHub Actions run `31924049344` independently compiled the same source at 512 and 768 bits and both jobs returned `AUDIT_RESULT pass=1`.

---

## 5. Certified compact strip `7.08 <= lambda <= 7.10`

The existing rectangular verifier was run on

\[
0.01\le t\le0.5,
\qquad
7.08\le\lambda\le7.10,
\]

with `K=128`, maximum quadtree depth `10`, and radius `rho=0.1`.

At both 512 and 768 bits the hardened tiler returned exactly

- `5572` certified leaves;
- `0` unresolved leaves;
- exact covered area `0.0098`;
- coverage fraction `1`;
- minimum outward-projected leaf margin
  \[
  \boxed{0.000070306587867159615>0};
  \]
- identical certified-leaf SHA256
  `af319fc74b08f293a39a0966dabc636bbe41d89cd5911d9ce724a183f081e9df`;
- identical empty/unresolved manifest SHA256
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

This is a finite box proof, not point sampling. Each accepted leaf is a directed-rounding enclosure theorem for the entire parameter rectangle represented by that leaf.

Therefore Regime B is closed.

---

## 6. Why `7.06` is not the next brute-force target

The same verifier was run diagnostically over

\[
0.01\le t\le0.5,
\qquad
7.06\le\lambda\le7.10.
\]

At depth `10`, `99.5807647705078125%` of the exact area was certified, but `4396` terminal boxes remained unresolved. Every terminal failure had status `PSC_CORE`, not a weight-monotonicity or geometry gate.

The unresolved boxes are highly localized:

\[
0.490908203125\le t\le0.5,
\]

and approximately

\[
7.06\le\lambda\le7.077891.
\]

Thus the failure is concentrated at the finite-time upper edge `t≈1/2`. It is not evidence that the theorem is false, but it is strong evidence that mere global subdivision is no longer the efficient way to improve the threshold. The present PSC lower core is approaching its own finite-time sign boundary.

This is classified as

\[
\boxed{\text{TYPE IV / PSC-core limitation, not generic interval inflation.}}
\]

The next improvement should therefore change the certificate near `t≈1/2` rather than merely increase the quadtree depth globally.

---

## 7. Circularity audit

Used:

1. unconditional D.H.J. Polymath effective Riemann--Siegel approximation;
2. the established phase-slope transversality algebra;
3. true positive heat weights and convex-tail upper envelopes;
4. Cauchy's derivative estimate with fixed pointwise base cutoff and explicit one-term cutoff bridge;
5. Schwarz symmetry for the symmetric normalization;
6. MPFR directed rounding at 512 and 768 bits;
7. finite partition completeness from the adaptive tiler.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- all-real zeros of `H_0`;
- finite-height verification of RH;
- zero-spacing or GUE assumptions;
- pair correlation as a proof input;
- Laguerre--Polya membership;
- Rodgers--Tao estimates whose contradiction argument assumes negative `Lambda`.

No dependency edge assumes the desired collision exclusion.

---

## 8. Status and next mathematical target

The strongest current shoulder statement in the project is now

\[
\boxed{
0<t\le1/2,\quad \lambda\ge7.08
\Longrightarrow
(H_t,H_t')\ne(0,0).
}
\]

Status labels:

- `INTERNALLY_PROVED`;
- `512/768-BIT CERTIFIED`;
- `CIRCULARITY AUDIT PASSED INTERNALLY`;
- `REFEREE_VERIFIED: PENDING`;
- `NOVELTY_UNVERIFIED`;
- `RH: OPEN`.

The next high-value target is **not** `lambda=7.06` by deeper uniform tiling. It is a new local certificate for the narrow corner

\[
t\approx1/2,
\qquad
7.06\lesssim\lambda\lesssim7.08,
\]

preferably one that exploits the hypothetical collision conditions jointly rather than the triangle estimate `|S|>=1-A_0` alone.
