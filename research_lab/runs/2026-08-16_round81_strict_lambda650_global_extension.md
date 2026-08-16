# Round 81 — Strict global shoulder extension to `lambda >= 6.50` via JECC

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

On the canonical strict track, which excludes finite-height verification of RH anywhere in the global dependency closure,

\[
\boxed{
0<t\le\frac12,
\qquad
\lambda\ge6.50
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\tag{81.1}
\]

Hence

\[
\boxed{C_{\rm strict}=6.50.}
\tag{81.2}
\]

This improves Round 78 (`6.85`) by using the new Round-80 Joint Elliptic Collision Certificate (JECC). It does not prove RH; the lower shoulder and bounded/core regimes remain open.

---

## 2. Clean proof cover

The proof has three pieces.

### A. Small time

\[
0<t\le0.01,
\qquad
6.50\le\lambda\le10.52.
\]

Closed by the old exact-weight PSC with a dedicated directed MPFR scalar audit at the worst endpoint `t=0.01, lambda=6.50`.

### B. Compact JECC bridge

\[
0.01\le t\le0.50,
\qquad
6.50\le\lambda\le7.08.
\]

Closed by the Round-80 JECC verifier, independently at 512 and 768 bits.

### C. Previously certified upper shoulder

\[
0<t\le0.50,
\qquad
\lambda\ge7.08.
\]

Closed by the earlier strict theorem. The older `10.52`, `7.10`, `6.90`, and `6.85` certificates remain nested historical cross-checks but are no longer needed to state the current frontier.

The three regions overlap and leave no gap above `lambda=6.50`.

---

## 3. Small-time scalar certificate

For `0<t<=0.01`, `lambda>=6.50`, put `u=t log n`.

The positive heat amplitudes are bounded using deliberately weakened powers:

\[
a_n\le n^{-1.874}
\quad (u\le1),
\]

\[
a_n\le n^{-1.311}
\quad (u>1)
\]

through the moving Riemann--Siegel cutoff.

The Polymath error channels are enclosed by padded exponential envelopes; the same symmetric-normalization bound already audited on the strict track is used. At the worst endpoint the independent 512- and 768-bit runs give the same outward decimal projections:

\[
A_0\le0.89710880510761826,
\]

\[
A_1\le1.3361223014476078,
\]

\[
S_0=1-A_0\ge0.10289119489238177,
\]

\[
E_0\le2.2738911968749703\times10^{-171},
\]

\[
E_1\le1.9387344381641930\times10^{-147}.
\]

The old PSC lower side is

\[
\boxed{32.098785970075724>0.}
\tag{81.3}
\]

Thus the small-time region is closed with overwhelming slack.

Canonical files:

- `research_lab/certificates/low_shoulder/small_time_lambda650_audit.c`;
- `strict_small_time_lambda650_512.txt`;
- `strict_small_time_lambda650_768.txt`.

Canonical Actions run: `31926284003`.

---

## 4. Round-80 JECC used on the compact bridge

Round 80 defines

\[
V=
\begin{pmatrix}
p/2\\ p_x/(2\Phi)\end{pmatrix},
\qquad
\Phi=|\phi_x|.
\]

The `n=1` contribution is exactly a unit vector:

\[
v_1=(\cos\phi,\sin\phi)^T,
\qquad \|v_1\|_2=1.
\]

For `n>=2`, with

\[
r_n=\frac{\sigma_x\log n}{\Phi},
\qquad
q_n=\frac{T\log n}{\Phi},
\qquad T=-\tau_x,
\]

the normalized tail matrix is

\[
M_n=
\begin{pmatrix}1&0\\-r_n&1-q_n\end{pmatrix}.
\]

Whenever `0<=q_n<=2`,

\[
\|M_n\|_2\le1+r_n.
\]

Therefore every hypothetical collision must satisfy

\[
1\le
A_0+
\frac{\sigma_x}{\Phi}A_1+
\frac12
\sqrt{E_0^2+
\left(\frac{E_1}{\Phi}\right)^2}.
\tag{81.4}
\]

The box-safe verifier uses

\[
T_U\log N_U\le2\Phi_L
\]

and the upward enclosure

\[
\mathcal J_U
=
A_{0,U}
+
\frac{\sigma_{x,U}}{\Phi_L}A_{1,U}
+
\frac12
\sqrt{E_{0,U}^2+
\left(\frac{E_{1,U}}{\Phi_L}\right)^2}.
\]

A box is certified whenever `mathcal J_U<1`.

No favorable lower `A1` head, no phase sampling, and no zero information are used.

---

## 5. Unified 512/768 compact certificate

The canonical unified bridge was run on

\[
0.01\le t\le0.50,
\qquad
6.50\le\lambda\le7.08,
\]

with

- true-weight head parameter `K=128`;
- radius `rho=0.1`;
- maximum quadtree depth `10`;
- directed MPFR arithmetic.

At **both** 512 and 768 bits the adaptive tiler returned identically:

- `4423` certified terminal leaves;
- `0` unresolved leaves;
- exact root area `0.2842`;
- exact certified area `0.2842`;
- coverage fraction `1`;
- minimum outward-projected lower margin
  \[
  \boxed{0.00008429498363186757>0};
  \]
- identical certified-manifest SHA256  
  `596acdf4b1442088e23afc6c2a6a4e352d3b633c9358b1f98caaa3aaa0ce3811`;
- identical empty unresolved-manifest SHA256  
  `fe704924de06b6b7332e7b92a82b4477fce3a0986e8902d45a7e5f741213d98e`.

Canonical workflow:
`.github/workflows/strict-jecc-650-to708-audit.yml`

Canonical Actions run:
`31926430064`.

The 512-bit run completed in about 17.3 seconds; the 768-bit run produced the same partition and hashes. This is a finite box proof, not point sampling.

---

## 6. Hostile implementation audit

The JECC implementation was checked for the following sign/direction issues.

1. `sigma_x` is bounded upward by `t_U D_U/4`.
2. `T=-tau_x` is bounded upward by `1/2+t_U C_U/4`.
3. The moving cutoff uses a continuous upper enclosure before taking `log N_U`; hence every actual `log n` is below the certified value.
4. The contraction gate uses
   \[
   T_U\log N_U\le2\Phi_L,
   \]
   which implies `0<=q_n<=2` for every main-sum term throughout the box.
5. Every term in
   \[
   A_{0,U}+\frac{\sigma_{x,U}}{\Phi_L}A_{1,U}
   +\frac12\sqrt{E_{0,U}^2+(E_{1,U}/\Phi_L)^2}
   \]
   is evaluated as an upper enclosure.
6. The certificate requires no lower `A1`, no cutoff-head inclusion hypothesis, and no rapidly varying phase interval.
7. Remaining early-level failures in the unified run were either weight-monotonicity geometry or coarse `JOINT_CORE` enclosures; all `JOINT_CORE` boxes disappeared before the terminal level and all terminal boxes were certified.

No rounding-direction defect was found in the JECC gate.

---

## 7. Strict dependency audit

Used:

- unconditional analytic D.H.J. Polymath effective Riemann--Siegel estimates (Theorem 1.3 / Corollary 6.5 and explicit error bounds);
- exact real-axis normalization formulas;
- Round-64/66 true-weight machinery;
- Round-80 JECC;
- Cauchy remainder control and symmetric normalization;
- MPFR 512/768-bit directed rounding;
- exact finite partition accounting.

Not used, directly or transitively on this proof path:

- RH;
- `Lambda<=0` or `Lambda=0`;
- Polymath Theorem 1.1 `Lambda<=0.22`;
- finite-height verification of RH;
- all-real zeros of `H_0`;
- zero-spacing or GUE assumptions;
- pair correlation as a proof input;
- Laguerre--Polya membership;
- Rodgers--Tao estimates whose proof begins inside a negative-`Lambda` contradiction setup.

The strict/unrestricted distinction from Round 77 remains in force.

---

## 8. Structural limit of JECC

JECC is much stronger at finite time, but its current termwise operator-norm compression has a genuine floor.

Each tail matrix has first row `(1,0)`. Hence any Euclidean operator norm satisfies

\[
\|M_n\|_2\ge1.
\]

Therefore any certificate that sums the tail termwise through independent operator norms must pay at least `A0`. Once `A0>=1`, this family cannot prove noncollision by triangle compression alone.

At `t=1/2`, direct diagnostics place the JECC `A0≈1` frontier near

\[
\lambda\approx6.458.
\]

This number is **diagnostic only**, not a theorem.

---

## 9. Next strict target

The next deliberately conservative target is

\[
\boxed{C_{\rm strict,target}=6.47.}
\]

Execution:

1. run JECC on `0.01<=t<=0.50`, `6.47<=lambda<=6.50` at 512 bits;
2. if complete, rerun independently at 768 bits;
3. certify the tiny-time strip by the old PSC;
4. if JECC develops persistent pointwise `JOINT_CORE` failures near `t=1/2`, stop subdivision rather than forcing the termwise norm beyond its structural `A0=1` floor;
5. then switch to a phase-correlated certificate, with the current leading candidates being the exact invariant `J=Im(conj(Z) Z_x)` or a prime-fiber / torus-block joint certificate that groups multiplicatively linked phases before taking norms.

Until that work is completed,

\[
\boxed{C_{\rm strict}=6.50.}
\]

RH remains OPEN.
