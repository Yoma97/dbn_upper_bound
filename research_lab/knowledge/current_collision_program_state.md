# Current Collision Program State

**Updated:** 2026-08-15 after Round 15.

## 1. Local collision geometry

For a finite simple real-zero cluster of a real entire backward-heat family

\[
\partial_tF=-F_{xx},
\]

the local collision section

\[
\mathcal D_I(t)=(-1)^{m(m-1)/2}\prod_{k\in I}F_x(t,x_k(t))
\]

satisfies

\[
\mathcal D_I=\Delta_I A_{\rm tail},\qquad A_{\rm tail}\ne0,
\]

and

\[
\frac d{dt}\log|\mathcal D_I|=\sum_{k\in I}(A_k^2+3B_k).
\]

At a simple real zero in the real-rooted order-one regime,

\[
R_k:=\frac d{dt}\log|F_x(t,x_k(t))|
=\frac14(\partial_x\log L_1)^2+3\frac{L_2}{L_1}.
\]

**Status:** PROVED under stated hypotheses.

---

## 2. Positive-threshold compactness

Using Polymath Theorem 1.5, if \(\Lambda>0\) then all sufficiently high zeros are uniformly real and simple on \([\Lambda/2,\Lambda]\). Compactness and Rouche continuation imply

\[
\boxed{\Lambda>0\Longrightarrow H_\Lambda\text{ has a multiple real zero at finite height}.}
\]

Hence the old Round-12 requirement of a height-uniform C6 estimate is not primary for the Riemann family.

Together with Rodgers--Tao,

\[
\boxed{RH\iff \Lambda=0\iff H_t,H_t'\text{ have no common real zero for all }t>0.}
\]

This is RH-equivalent and may be used only as a reduction.

---

## 3. Universal collision residue

At a multiplicity-m collision,

\[
\boxed{
R_k(t)=\frac{m-1}{2(t-t_c)}+O((t-t_c)^{-1/2})
}
\]

on the forward real-rooted side, equivalently

\[
\lim_{t\downarrow t_c}(t-t_c)R_k(t)=\frac{m-1}{2}.
\]

**Status:** PROVED local theorem; novelty unverified.

---

## 4. Riemann kernel ratio

Set

\[
K(r)=\Phi(\sqrt r),\quad K_t(r)=e^{tr}K(r),
\]

\[
q(u)=-\frac{\Phi'(u)}{u\Phi(u)}.
\]

The established strict concavity of \(\log\Phi(\sqrt r)\) implies \(q'(u)>0\). Direct bounds from the defining theta series give the conservative estimate

\[
q(0)>33>1.
\]

Therefore for \(0\le t\le1/2\), \(K_t\) is strictly decreasing and strictly log-concave.

With

\[
w_t(u)=u e^{tu^2}\Phi(u)=uK_t(u^2),
\]

one has

\[
\boxed{w_t\text{ strictly log-concave on }(0,\infty).}
\]

---

## 5. Half-wave theorem

For \(h=\pi/x\), define

\[
a_n(t,x)=\int_{nh}^{(n+1)h}w_t(u)|\sin(xu)|\,du,
\]

\[
b_n(t,x)=\int_{nh}^{(n+1)h}q(u)w_t(u)|\sin(xu)|\,du.
\]

Prekopa--Leindler applied to the convolution with \(\sin(xs)1_{(0,h)}\) gives

\[
\boxed{a_n^2\ge a_{n-1}a_{n+1}.}
\]

Thus \((a_n)\) is positive log-concave. Also monotonicity of q gives

\[
\boxed{b_n/a_n\text{ strictly increasing in }n.}
\]

Both are independent kernel facts.

---

## 6. TP2/log-concavity barrier

Round 15 gives an exact infinite abstract counterexample showing that

1. positive log-concavity of \((a_n)\), and
2. strict increase of \(b_n/a_n\),

**do not imply** that the two alternating sums

\[
\sum(-1)^na_n,\qquad \sum(-1)^nb_n
\]

cannot vanish simultaneously.

Therefore TP2/log-concavity plus monotone likelihood-ratio reweighting is **provably insufficient as an abstract C6 mechanism**.

This prevents further attempts to derive RH from kernel log-concavity alone.

---

## 7. Current single target

### Finite oscillatory sign-regularity bridge

Seek the weakest fixed finite-order determinant/variation-diminishing property of

\[
K_t(r)=e^{tr}\Phi(\sqrt r)
\]

that controls simultaneously

\[
\sin(x\sqrt r),\qquad q(\sqrt r)\sin(x\sqrt r)
\]

and forbids their \(K_t(r)dr\)-integrals from vanishing together.

Mandatory requirements:

- fixed finite complexity independent of x;
- independently provable from the Riemann kernel;
- not an all-orders sign-regularity/LP criterion;
- not global L1 positivity;
- must survive known low-order determinantal limitations in the literature;
- must have a non-RH application or a natural kernel-class theorem.

If the required determinant order necessarily grows with the number of sine oscillations, classify the route as **REFUTED/structurally circular** and abandon it.

---

## 8. Status

- local collision geometry: **PROVED**;
- positive-threshold finite collision attainment: **PROVED**;
- Hermite collision residue: **PROVED**;
- q monotonicity and heat-weighted density log-concavity: **PROVED**;
- half-wave mass log-concavity: **PROVED**;
- half-wave likelihood-ratio ordering: **PROVED**;
- cumulative nonnegative-balance lemma: **REFUTED**;
- TP2/log-concavity alone as C6: **REFUTED**;
- finite oscillatory sign-regularity bridge: **OPEN / CANDIDATE**;
- independent C6 theorem: **OPEN**;
- RH: **OPEN**;
- novelty: **UNVERIFIED**.
