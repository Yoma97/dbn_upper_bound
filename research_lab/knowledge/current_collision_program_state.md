# Current Collision Program State

**Updated:** 2026-08-15 after Round 13.

## 1. Local collision geometry retained from Round 12

For a finite simple real-zero cluster of a real entire backward-heat family,

\[
\partial_tF=-F_{xx},
\]

the local collision section

\[
\mathcal D_I(t)=(-1)^{m(m-1)/2}\prod_{k\in I}F_x(t,x_k(t))
\]

has local factorization

\[
\mathcal D_I=\Delta_I A_{\rm tail},\qquad A_{\rm tail}\ne0,
\]

and exact evolution

\[
\frac d{dt}\log|\mathcal D_I|
=\sum_{k\in I}(A_k^2+3B_k),
\]

where

\[
A_k=\frac{F_{xx}}{2F_x}(x_k),
\qquad
B_k=A_k^2-\frac{F_{xxx}}{3F_x}(x_k).
\]

At a simple real zero of an order-one real-rooted entire function,

\[
B_k=\sum_{j\ne k}(x_k-x_j)^{-2}.
\]

The exact Laguerre reduction is

\[
B_k=\frac{L_2(x_k)}{L_1(x_k)},
\qquad
A_k=\frac{\partial_xL_1(x_k)}{2L_1(x_k)},
\]

hence

\[
R_k(t):=\frac d{dt}\log|F_x(t,x_k(t))|
=\frac14(\partial_x\log L_1)^2+3\frac{L_2}{L_1}.
\]

These remain **PROVED under the stated local hypotheses**.

---

## 2. Round-13 correction: uniform height is not the primary C6 obstruction

The previous state file asserted that a hypothetical positive de Bruijn--Newman constant might be realized only through collision/near-collision events escaping to infinite height, so a height-uniform C6 bound was declared mandatory.

For the Riemann heat family this assertion is now **REFUTED when \(\Lambda>0\)**.

Polymath Theorem 1.5 gives absolute \(C,c>0\) such that, for every \(0<t\le1/2\), all zeros with

\[
|\Re z|\ge e^{C/t}
\]

are real and lie one-per-asymptotic-disk, hence are simple. If \(\Lambda>0\), this is uniform on

\[
t\in[\Lambda/2,\Lambda]
\]

outside

\[
X_\Lambda=\exp(2C/\Lambda).
\]

Compactness plus Rouche/implicit-function continuation then proves:

\[
\boxed{\Lambda>0\Longrightarrow H_\Lambda\text{ has a multiple real zero at finite height}.}
\]

Thus positive-threshold loss of real-rootedness cannot escape to infinity in the Riemann family.

Combining this with Rodgers--Tao \(\Lambda\ge0\) and the standard implication `multiple real zero at t0 => t0 <= Lambda` gives the exact reduction

\[
\boxed{
RH\iff \Lambda=0
\iff H_t,H_t'\text{ have no common real zero for every }t>0.
}
\]

This is **RH-EQUIVALENT**, so it is a reduction, not a proof.

---

## 3. Universal collision residue

At a zero of exact multiplicity \(m\ge2\) at \((t_c,x_c)\), on the forward real-rooted side \(\tau=t-t_c\downarrow0\),

\[
F_{t_c+\tau}(x_c+\sqrt\tau X)
=a\tau^{m/2}Q_m(X)+O(\tau^{(m+1)/2}),
\]

with

\[
Q_m(X)=e^{-D_X^2}X^m=H_m(X/2).
\]

For every local root branch,

\[
\boxed{
R_k(t)=\frac{m-1}{2(t-t_c)}+O((t-t_c)^{-1/2})
}
\]

and therefore

\[
\boxed{
\lim_{t\downarrow t_c}(t-t_c)R_k(t)=\frac{m-1}{2}.
}
\]

Equivalently, for a root \(\xi_k\) of \(Q_m\),

\[
\left(\sum_{j\ne k}\frac1{\xi_k-\xi_j}\right)^2
+3\sum_{j\ne k}\frac1{(\xi_k-\xi_j)^2}
=\frac{m-1}{2}.
\]

**Status:** PROVED local theorem; novelty unverified.

---

## 4. Preferred Riemann-kernel interface

Let

\[
\psi_t(u)=e^{tu^2}\Phi(u),\qquad
w_t(u)=u\psi_t(u),
\]

and define

\[
q(u)=-\frac{\Phi'(u)}{u\Phi(u)}.
\]

Csordas' established strict concavity of

\[
r\mapsto\log\Phi(\sqrt r)
\]

implies

\[
\boxed{q'(u)>0\quad(u>0).}
\]

The ratio \(q\) is independent of heat time.

Define

\[
S_0(t,x)=\int_0^\infty w_t(u)\sin(xu)\,du=-H_t'(x),
\]

\[
S_1(t,x)=\int_0^\infty q(u)w_t(u)\sin(xu)\,du.
\]

Integration by parts gives

\[
\boxed{S_1(t,x)=xH_t(x)-2tH_t'(x).}
\]

Hence

\[
H_t(x)=H_t'(x)=0
\iff S_0(t,x)=S_1(t,x)=0.
\]

At such a collision, with

\[
M_{t,x}(v)=\int_0^v w_t(u)\sin(xu)\,du,
\]

one has

\[
0=-\int_0^\infty q'(u)M_{t,x}(u)\,du.
\]

Since \(q'>0\) and \(M_{t,x}(v)>0\) for sufficiently small \(v>0\), every collision forces a **cumulative sine overshoot**:

\[
\boxed{\exists v>0:\ M_{t,x}(v)<0.}
\]

This is **PROVED as a necessary collision signature**.

---

## 5. Single next target

### CANDIDATE: cumulative sine-balance lemma

Attempt to prove, or rapidly refute, for the specific Riemann kernel:

if

\[
S_0(t,x)=0,
\]

then

\[
M_{t,x}(v)\ge0\quad\forall v\ge0,
\]

for \(0<t\le1/2\).

A proof would contradict the mandatory overshoot at a collision and therefore exclude positive-time collisions. However strict log-concavity alone is not enough by analogy; the lemma must be derived from additional special structure of \(\Phi\), or rejected by a counterexample/numerical test.

In the variable \(r=u^2\),

\[
S_0(t,x)=\frac12\int_0^\infty K_t(r)\sin(x\sqrt r)\,dr,
\qquad
K_t(r)=e^{tr}\Phi(\sqrt r),
\]

and

\[
\log K_t(r)=tr+\log\Phi(\sqrt r)
\]

is strictly concave for every real \(t\). This is the allowed structural input for the next attack.

---

## 6. Gate/status table

- Local collision divisor geometry: **PROVED**.
- Rootwise inverse-square trace: **PROVED in the real-rooted order-one regime**.
- Laguerre reduction: **PROVED**.
- Positive-threshold escape-to-infinity scenario: **REFUTED for the Riemann family**.
- Finite multiple-zero attainment if \(\Lambda>0\): **PROVED**.
- Universal Hermite collision residue: **PROVED**.
- Monotone kernel-ratio collision pair: **PROVED**.
- Cumulative sine overshoot necessity: **PROVED**.
- Cumulative sine-balance no-go lemma: **CANDIDATE / UNPROVED**.
- Independent C6 no-collision theorem: **OPEN**.
- RH: **OPEN**.
- Novelty of the Round-13 package: **NOVELTY UNVERIFIED**.
