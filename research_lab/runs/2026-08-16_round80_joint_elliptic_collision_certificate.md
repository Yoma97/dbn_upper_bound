# Round 80 — Joint Elliptic Collision Certificate (JECC)

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Couples the value and derivative collision equations in a single Euclidean norm. It is strictly cheaper computationally than APVC and has a much lower finite-time diagnostic frontier.

---

## 1. Setup

Use the same normalized fixed-cutoff approximation as the PSC/APVC rounds:

\[
p(x)=2\Re\left(e^{i\phi}S\right),
\qquad
S=\sum_{n\le N}a_n e^{-i\tau\log n},
\]

\[
a_n=
\exp\left(\frac t4\log^2n-\sigma\log n\right)>0,
\qquad a_1=1.
\]

Put

\[
\theta_n=\phi-\tau\log n.
\]

On the real positive shoulder write

\[
\Phi:=-\phi_x=|\phi_x|>0,
\qquad
T:=-\tau_x>0,
\qquad
s:=\sigma_x\ge0.
\]

At a hypothetical true multiple zero the effective Polymath approximation gives

\[
|p|\le E_0,
\qquad
|p_x|\le E_1.
\tag{80.1}
\]

Define the positive moments

\[
A_0=\sum_{n=2}^N a_n,
\qquad
A_1=\sum_{n=2}^N a_n\log n.
\tag{80.2}
\]

---

## 2. Exact normalized joint vector

Differentiating one term gives

\[
\frac{p_x}{2}
=
\sum_{n\le N}a_n
\left[
-s\log n\cos\theta_n
+(\Phi-T\log n)\sin\theta_n
\right].
\tag{80.3}
\]

Normalize the derivative coordinate by `Phi`:

\[
V:=
\begin{pmatrix}
p/2\\[2mm]
p_x/(2\Phi)
\end{pmatrix}.
\tag{80.4}
\]

For `n=1`, because `log 1=0`, the contribution is exactly

\[
\boxed{
v_1=\begin{pmatrix}\cos\phi\\ \sin\phi\end{pmatrix},
\qquad \|v_1\|_2=1.}
\tag{80.5}
\]

This is the key normalization: the distinguished first term becomes a unit vector for **every phase**, so no value-anchor or lower bound for `sin(phi)` is needed.

For `n>=2`, let

\[
\ell_n=\log n,
\qquad
r_n=\frac{s\ell_n}{\Phi},
\qquad
q_n=\frac{T\ell_n}{\Phi}.
\]

Then the `n`th normalized contribution is

\[
v_n
=a_nM_nu_n,
\qquad
u_n=
\begin{pmatrix}\cos\theta_n\\\sin\theta_n\end{pmatrix},
\qquad
\|u_n\|_2=1,
\tag{80.6}
\]

where

\[
\boxed{
M_n=
\begin{pmatrix}
1&0\\
-r_n&1-q_n
\end{pmatrix}.}
\tag{80.7}
\]

Thus

\[
V=v_1+\sum_{n=2}^Nv_n.
\tag{80.8}
\]

---

## 3. Contraction bound for each tail term

Assume

\[
0\le q_n\le2.
\tag{80.9}
\]

Then

\[
|1-q_n|\le1.
\]

Split

\[
M_n=
\begin{pmatrix}1&0\\0&1-q_n\end{pmatrix}
+
\begin{pmatrix}0&0\\-r_n&0\end{pmatrix}.
\]

The first matrix has Euclidean operator norm at most `1`, and the second has norm exactly `r_n`. Therefore

\[
\boxed{\|M_n\|_2\le1+r_n.}
\tag{80.10}
\]

Consequently

\[
\left\|\sum_{n=2}^Nv_n\right\|_2
\le
\sum_{n=2}^Na_n(1+r_n)
=
A_0+\frac{s}{\Phi}A_1.
\tag{80.11}
\]

No cancellation among phases has been used.

A sufficient global condition for (80.9) is simply

\[
\boxed{T\log N\le2\Phi.}
\tag{80.12}
\]

The lower inequality `q_n>=0` follows from `T>0`.

---

## 4. Collision error disk

At a true collision, (80.1) gives

\[
\|V\|_2
\le
\frac12
\sqrt{
E_0^2+
\left(\frac{E_1}{\Phi}\right)^2
}.
\tag{80.13}
\]

From (80.8), the reverse triangle inequality, (80.5), and (80.11),

\[
1
=\|v_1\|_2
\le
\left\|\sum_{n=2}^Nv_n\right\|_2+\|V\|_2.
\]

Hence every hypothetical collision must satisfy

\[
\boxed{
1\le
A_0+
\frac{s}{\Phi}A_1+
\frac12
\sqrt{
E_0^2+
\left(\frac{E_1}{\Phi}\right)^2
}.
}
\tag{80.14}
\]

This yields the certificate.

### Theorem 80.1 — JECC

Assume on the point under consideration

\[
\Phi>0,
\qquad
T>0,
\qquad
s\ge0,
\qquad
T\log N\le2\Phi.
\]

If

\[
\boxed{
A_0+
\frac{s}{\Phi}A_1+
\frac12
\sqrt{
E_0^2+
\left(\frac{E_1}{\Phi}\right)^2
}<1,
}
\tag{JECC}
\]

then `H_t(x)` and `H_t'(x)` cannot vanish simultaneously.

---

## 5. Box-safe form

Suppose a parameter box provides rigorous enclosures

\[
\Phi\ge\Phi_L>0,
\qquad
0\le s\le s_U,
\qquad
0<T\le T_U,
\]

and an upper logarithmic cutoff

\[
\log N\le L_{N,U}.
\]

If

\[
\boxed{T_UL_{N,U}\le2\Phi_L,}
\tag{80.15}
\]

then (80.9) holds for every term at every point in the box.

Using upper moment/error enclosures gives the rigorous box upper quantity

\[
\boxed{
\mathcal J_U
=
A_{0,U}
+
\frac{s_U}{\Phi_L}A_{1,U}
+
\frac12
\sqrt{
E_{0,U}^2+
\left(\frac{E_{1,U}}{\Phi_L}\right)^2
}.
}
\tag{80.16}
\]

Thus

\[
\boxed{\mathcal J_U<1}
\tag{80.17}
\]

certifies the whole box.

Every quantity required by (80.16) is already computed by the existing true-weight PSC verifier. In particular JECC needs **no favorable lower `A1` sum** and therefore no large finite head.

---

## 6. Exact operator-norm sharpening

The simple estimate (80.10) is not the best possible one. For future use, with

\[
b_n=1-q_n,
\]

we have

\[
M_n^TM_n=
\begin{pmatrix}
1+r_n^2&-r_nb_n\\
-r_nb_n&b_n^2
\end{pmatrix}.
\]

If

\[
\Theta_n=1+r_n^2+b_n^2,
\]

then

\[
\boxed{
\|M_n\|_2^2
=
\frac{
\Theta_n+\sqrt{\Theta_n^2-4b_n^2}
}{2}.
}
\tag{80.18}
\]

The current shoulder has `r_n` astronomically small, so the moment-compressed bound (80.11) is expected to be nearly optimal. The exact singular-value form should only be introduced if a genuine loss from `1+r_n` is later detected.

---

## 7. Structural interpretation

PSC and APVC treated the two collision equations sequentially:

- value information restricted the allowed phase;
- derivative information then had to dominate an adversarial tail.

JECC instead treats the value and phase-normalized derivative as a single two-dimensional vector. The `n=1` mode is exactly the unit circle, while the high modes are contractions in the derivative coordinate because their phase velocities interpolate from the outer speed toward zero at the Riemann--Siegel cutoff.

This is why the large derivative scale `Phi` ceases to be a loss: after normalization it becomes the geometry that contracts the tail.

---

## 8. Relation to the small-time floor

In the fixed-lambda limit `t->0+`,

\[
\frac{s}{\Phi}A_1\to0,
\qquad
E_0\to0,
\qquad
E_1/\Phi\to0,
\]

while Round 64 gives

\[
A_0\to
\zeta\left(\frac12+\frac\lambda4\right)-1.
\]

Therefore the limiting JECC condition is simply

\[
\zeta\left(\frac12+\frac\lambda4\right)-1<1,
\]

i.e.

\[
\boxed{\lambda>\lambda_*=4.914588956\ldots.}
\tag{80.19}
\]

Thus, unlike APVC, JECC retains the **same optimal asymptotic sign floor as the old exact-weight triangle PSC** while being substantially stronger at finite time.

This makes it a natural candidate to unify the small-time and finite-time shoulder mechanisms above `lambda_*`.

---

## 9. Diagnostic frontier — NOT a proof threshold

A direct high-precision evaluation of the true positive moments, ignoring only the already tiny effective errors, gives at `t=1/2` a JECC sign transition near

\[
\boxed{\lambda\approx6.4581.}
\]

For comparison, the Round-74/75 APVC pointwise transition is near `6.8188`.

Further pointwise diagnostics give approximate JECC transitions decreasing with `t`:

- `t=0.50`: `lambda≈6.458`;
- `t=0.45`: `lambda≈6.388`;
- `t=0.40`: `lambda≈6.302`;
- `t=0.35`: `lambda≈6.200`;
- `t=0.30`: `lambda≈6.077`;
- `t=0.25`: `lambda≈5.931`;
- `t=0.20`: `lambda≈5.757`.

These values are **HEURISTIC/DIAGNOSTIC ONLY** and are not used as proof constants.

The first deliberately conservative certification target is

\[
\boxed{C_{\rm JECC,target}=6.50.}
\]

---

## 10. Circularity audit

Used:

- exact normalized finite Riemann--Siegel main sum;
- exact derivative formulas;
- positivity of the amplitudes;
- Euclidean triangle inequality and operator norms;
- the same unconditional Polymath error bounds `E0,E1` already used by the strict PSC route.

Not used:

- RH;
- any numerical verification of RH;
- any upper bound for `Lambda`;
- real-rootedness of `H_0`;
- zero locations or spacings;
- phase cancellation;
- pair correlation/GUE;
- Laguerre--Polya membership;
- Rodgers--Tao negative-time contradiction estimates.

No desired collision-exclusion conclusion is assumed.

---

## 11. Immediate implementation

Patch JECC as a second gate after the old PSC using the **same** verified box quantities:

1. `A0_U,A1_U` from Round-66 true-weight bounds;
2. `Phi_L` from the existing phase lower bound;
3. `s_U=t_U D_U/4`;
4. `T_U=1/2+t_U C_U/4`;
5. `L_N,U` from the upper moving-cutoff geometry;
6. existing `E0_U,E1_U`.

Run `lambda>=6.50` first at 512 bits, then independently at 768 bits if complete. Only if JECC itself develops a pointwise obstruction should the project return to phase-sensitive `J` / exact joint-jet machinery.
