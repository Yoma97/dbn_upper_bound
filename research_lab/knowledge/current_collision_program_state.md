# Current Collision Program State

**Updated:** 2026-08-15 after Round 14.

## Core local geometry

For a finite simple real-zero cluster of a real entire backward-heat family,

\[
\partial_tF=-F_{xx},
\]

the local collision section

\[
\mathcal D_I(t)=(-1)^{m(m-1)/2}\prod_{k\in I}F_x(t,x_k(t))
\]

has the local factorization

\[
\mathcal D_I=\Delta_I A_{\rm tail},\qquad A_{\rm tail}\ne0,
\]

and exact evolution

\[
\frac d{dt}\log|\mathcal D_I|
=\sum_{k\in I}(A_k^2+3B_k),
\]

with

\[
A_k=\frac{F_{xx}}{2F_x}(x_k),
\qquad
B_k=A_k^2-\frac{F_{xxx}}{3F_x}(x_k).
\]

At a simple real zero in the real-rooted order-one setting,

\[
B_k=\sum_{j\ne k}(x_k-x_j)^{-2},
\]

and

\[
R_k:=\frac d{dt}\log|F_x(t,x_k(t))|
=\frac14(\partial_x\log L_1)^2+3\frac{L_2}{L_1}.
\]

**Status:** PROVED under the stated hypotheses.

---

## Positive-threshold compactness correction

Polymath Theorem 1.5 rules out loss of real-rootedness escaping solely to infinite height when a hypothetical threshold is positive.

If \(\Lambda>0\), high zeros are uniformly real and simple on

\[
t\in[\Lambda/2,\Lambda]
\]

outside a safe finite cutoff

\[
X_\Lambda=\exp(2C/\Lambda).
\]

Compactness and Rouche continuation then imply

\[
\boxed{\Lambda>0\Longrightarrow H_\Lambda\text{ has a multiple real zero at finite height}.}
\]

Thus the previous Round-12 assertion that C6 must begin with a height-uniform \(R_k\) bound is **REFUTED for the Riemann family at a positive threshold**.

Together with Rodgers--Tao \(\Lambda\ge0\),

\[
\boxed{
RH\iff \Lambda=0
\iff H_t,H_t'\text{ have no common real zero for all }t>0.
}
\]

This is an **RH-EQUIVALENT reduction**, not a proof input.

---

## Universal collision residue

At a zero of exact multiplicity \(m\ge2\) at \((t_c,x_c)\), on the forward real-rooted side,

\[
F_{t_c+\tau}(x_c+\sqrt\tau X)
=a\tau^{m/2}Q_m(X)+O(\tau^{(m+1)/2}),
\]

where

\[
Q_m=e^{-D^2}X^m=H_m(X/2).
\]

For each local branch,

\[
\boxed{
R_k(t)=\frac{m-1}{2(t-t_c)}+O((t-t_c)^{-1/2}),
}
\]

so

\[
\boxed{
\lim_{t\downarrow t_c}(t-t_c)R_k(t)=\frac{m-1}{2}.
}
\]

**Status:** PROVED local theorem; novelty unverified.

---

## Monotone Riemann kernel-ratio interface

Let

\[
\psi_t(u)=e^{tu^2}\Phi(u),\quad
w_t(u)=u\psi_t(u),\quad
q(u)=-\frac{\Phi'(u)}{u\Phi(u)}.
\]

The established strict concavity of

\[
r\mapsto\log\Phi(\sqrt r)
\]

implies

\[
\boxed{q'(u)>0\quad(u>0).}
\]

Define

\[
S_0(t,x)=\int_0^\infty w_t(u)\sin(xu)\,du=-H_t'(x),
\]

\[
S_1(t,x)=\int_0^\infty q(u)w_t(u)\sin(xu)\,du.
\]

Then

\[
\boxed{S_1=xH_t-2tH_t'.}
\]

Thus a collision is a common zero of two sine transforms whose positive kernels have a strictly increasing, time-independent ratio q.

At a critical point \(H_t'(x)=0\), with

\[
M_{t,x}(v)=\int_0^v w_t(u)\sin(xu)\,du,
\]

one has

\[
\boxed{
xH_t(x)=-\int_0^\infty q'(u)M_{t,x}(u)\,du.}
\]

---

## Round-14 falsification

The proposed lemma

\[
H_t'(x)=0\Longrightarrow M_{t,x}(v)\ge0\ \forall v
\]

is **REFUTED rigorously**.

At \(t=1/2\), \(H_{1/2}\) has infinitely many simple real zeros. Between consecutive zeros its sign alternates, so there are positive critical extrema. At such a critical point,

\[
xH_{1/2}(x)>0
\]

and hence

\[
\int q'M<0,
\]

forcing \(M<0\) somewhere. Thus cumulative overshoot is ordinary behavior, not a collision detector.

---

## Current single target: half-wave shape theorem

For fixed \(x>0\), set

\[
I_n=[n\pi/x,(n+1)\pi/x]
\]

and define

\[
a_n(t,x)=\int_{I_n}w_t(u)|\sin(xu)|\,du,
\]

\[
b_n(t,x)=\int_{I_n}q(u)w_t(u)|\sin(xu)|\,du.
\]

Then

\[
S_0=\sum_{n\ge0}(-1)^n a_n,
\qquad
S_1=\sum_{n\ge0}(-1)^n b_n.
\]

Because q is strictly increasing and the half-wave intervals are ordered,

\[
\boxed{\frac{b_{n+1}}{a_{n+1}}>\frac{b_n}{a_n}}
\]

for all nonzero masses.

This monotone-likelihood-ratio fact is **PROVED**, but by itself does not prevent both alternating sums from vanishing.

### Single next research question

Find or refute a **strict discrete shape/sign-regularity theorem** for the half-wave mass sequence \(a_n(t,x)\), derived from the special Riemann density

\[
w_t(u)=u e^{tu^2}\Phi(u),
\]

that, together with the increasing ratios \(b_n/a_n\), prevents

\[
\sum(-1)^n a_n=\sum(-1)^n b_n=0.
\]

The theorem must not assume real-rootedness, interlacing, the sign of H between zeros, global L1 positivity, or an all-n positive-definite-kernel criterion.

Preferred structural input:

\[
K_t(r)=e^{tr}\Phi(\sqrt r),
\qquad
\log K_t(r)=tr+\log\Phi(\sqrt r),
\]

which is strictly concave for every real t.

---

## Status table

- Local collision divisor geometry: **PROVED**.
- Laguerre/gap reduction: **PROVED**.
- Positive-threshold finite collision attainment: **PROVED**.
- Universal Hermite collision residue: **PROVED**.
- Monotone q kernel ratio: **PROVED**.
- Simple cumulative nonnegative-balance lemma: **REFUTED**.
- Half-wave ratio monotonicity: **PROVED**.
- Sufficient half-wave shape theorem: **OPEN**.
- Independent C6 no-collision theorem: **OPEN**.
- RH: **OPEN**.
- Novelty: **UNVERIFIED**.
