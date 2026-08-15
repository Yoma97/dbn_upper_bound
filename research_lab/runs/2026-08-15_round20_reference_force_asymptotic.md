# Round 20 — Classical-location reference force tends to \(-\pi/8\)

**Date:** 2026-08-15

**Status labels:** PROVED / CONDITIONAL / CANDIDATE / REFUTED / NOVELTY UNVERIFIED.

**RH status:** OPEN.

## 0. Theorem

Let Rodgers--Tao's positive classical locations be defined by

\[
\Psi(\xi_j)=j,\qquad
\Psi(x)=\frac{x}{4\pi}\left(\log\frac{x}{4\pi}-1\right),
\qquad j\ge1,
\]

and extend by \(\xi_{-j}=-\xi_j\). Define the principal-value reference force

\[
S_j^\xi:=\operatorname{PV}\sum_{k\in\mathbb Z^*,\,k\ne j}\frac1{\xi_j-\xi_k}.
\]

Then

\[
\boxed{
S_j^\xi=-\frac\pi8+O\!\left(\frac{\log j}{\sqrt j}\right),
\qquad j\to+\infty.
}
\]

By odd symmetry,

\[
\boxed{
S_{-j}^\xi=+\frac\pi8+O\!\left(\frac{\log j}{\sqrt j}\right).
}
\]

The proof uses only the explicit reference configuration and is logically independent of RH.

**Novelty:** UNVERIFIED.

---

## 1. Inverse counting map

Let

\[
x_0=4\pi e,
\qquad
\phi:=\Psi^{-1}:[0,\infty)\to[x_0,\infty).
\]

Thus \(\phi(j)=\xi_j\). Put

\[
L(x):=\log\frac{x}{4\pi}.
\]

Since

\[
\Psi'(x)=\frac{L(x)}{4\pi},
\]

at \(x=\phi(u)\) one has

\[
\boxed{
\phi'(u)=\frac{4\pi}{L(x)}
}
\]

and

\[
\boxed{
\phi''(u)=-\frac{16\pi^2}{xL(x)^3}.
}
\]

Hence

\[
\boxed{
\frac{|\phi''(u)|}{\phi'(u)^2}=\frac1{xL(x)}.
}
\]

Moreover, from

\[
u=\frac{x}{4\pi}(L(x)-1)
\]

we have for large \(u\)

\[
x\asymp\frac u{\log u},
\qquad L(x)\asymp\log u.
\]

---

## 2. Paired form of the force

Fix \(j>0\) and write \(x=\xi_j=\phi(j)\). Pairing the \(k\) and \(-k\) terms gives

\[
S_j^\xi
=\frac1{2x}
+\sum_{\substack{k\ge1\\k\ne j}}
\left(\frac1{x-\xi_k}+\frac1{x+\xi_k}\right).
\]

Define

\[
g_x(u):=\frac{2x}{x^2-\phi(u)^2}.
\]

Then

\[
\boxed{
S_j^\xi=\frac1{2x}+\sum_{\substack{k\ge1\\k\ne j}}g_x(k).
}
\]

The paired tail is absolutely convergent because

\[
g_x(k)=O\!\left(\frac{x}{\xi_k^2}\right)
=O\!\left(\frac{x\log^2k}{k^2}\right).
\]

---

## 3. Continuum principal-value force

Set

\[
I(x):=\operatorname{PV}\int_0^\infty g_x(u)\,du.
\]

Changing variables \(y=\phi(u)\), then \(y=xv\), gives

\[
I(x)
=\frac1{2\pi}\operatorname{PV}
\int_{4\pi e/x}^{\infty}
\frac{\log(xv/4\pi)}{1-v^2}\,dv.
\]

Use

\[
\operatorname{PV}\int_0^\infty\frac{dv}{1-v^2}=0
\]

and

\[
\int_0^\infty\frac{\log v}{1-v^2}\,dv=-\frac{\pi^2}{4}.
\]

For the second identity,

\[
\int_0^1\frac{\log v}{1-v^2}\,dv
=-\sum_{n\ge0}\frac1{(2n+1)^2}
=-\frac{\pi^2}{8},
\]

and the substitution \(v\mapsto1/v\) gives the same contribution on \((1,\infty)\). Thus the lower-limit-zero model equals \(-\pi/8\). The omitted interval \((0,4\pi e/x)\) contributes

\[
O\!\left(\frac{\log x}{x}\right).
\]

Therefore

\[
\boxed{
I(x)=-\frac\pi8+O\!\left(\frac{\log x}{x}\right).
}
\]

---

## 4. Discrete-to-continuum error

Let

\[
M=\lfloor\sqrt j\rfloor,
\qquad
h=\phi'(j)=\frac{4\pi}{L(x)}.
\]

On \(|u-j|\le M\), because \(M=o(j)\),

\[
\phi(u)\asymp x,
\qquad
\phi'(u)\asymp h,
\qquad
\frac{|\phi''(u)|}{h^2}\ll\frac1{xL(x)}.
\]

### 4.1 Far region

Since

\[
g_x'(u)
=\frac{4x\phi(u)\phi'(u)}{(x^2-\phi(u)^2)^2}>0,
\]

\(g_x\) is monotone on each side of its pole. The monotone sum--integral estimate yields a far-region discrepancy bounded by the endpoint sizes. Since

\[
x-\phi(j-M)\asymp hM,
\qquad
\phi(j+M)-x\asymp hM,
\]

we obtain

\[
\boxed{
\text{far discrepancy}\ll\frac{\log j}{M}+\frac1x.
}
\]

### 4.2 Near pole: symmetric cancellation

For \(0<s\le M\), write

\[
a_s=x-\phi(j-s),
\qquad
b_s=\phi(j+s)-x.
\]

Then

\[
g_x(j-s)+g_x(j+s)
=\left(\frac1{a_s}-\frac1{b_s}\right)
+\left(\frac1{2x-a_s}-\frac1{2x+b_s}\right).
\]

Taylor's theorem gives

\[
|a_s-b_s|
\le s^2\sup_{|u-j|\le M}|\phi''(u)|,
\]

while \(a_s,b_s\gg hs\). Hence

\[
\left|\frac1{a_s}-\frac1{b_s}\right|
\ll\frac1{xL(x)}.
\]

Also \(a_s+b_s\ll hs\), so

\[
\left|\frac1{2x-a_s}-\frac1{2x+b_s}\right|
\ll\frac{hs}{x^2}.
\]

Therefore

\[
\boxed{
|g_x(j-s)+g_x(j+s)|
\ll\frac1{xL(x)}+\frac{hs}{x^2}.
}
\]

This estimate applies both to the symmetric discrete pairs and to the symmetric principal-value integral. Consequently

\[
\boxed{
\text{near discrepancy}
\ll\frac Mj+rac{M^2\log j}{j^2}.
}
\]

### 4.3 Combine

Thus

\[
S_j^\xi-I(\xi_j)
\ll
\frac{\log j}{M}
+\frac Mj
+\frac{M^2\log j}{j^2}
+\frac1x.
\]

Taking \(M=\lfloor\sqrt j\rfloor\) gives

\[
\boxed{
S_j^\xi-I(\xi_j)
=O\!\left(\frac{\log j}{\sqrt j}\right).
}
\]

Combining with Section 3 proves

\[
\boxed{
S_j^\xi=-\frac\pi8
+O\!\left(\frac{\log j}{\sqrt j}\right).
}
\]

---

## 5. Relation to the zero velocity

If one formally places the positive particles exactly at \(x_j=\xi_j\), the Calogero-type zero ODE gives

\[
\dot x_j=2S_j^\xi=-\frac\pi4+o(1).
\]

This is independently consistent with the Polymath positive-time asymptotic for sufficiently high real zeros,

\[
\dot x(t)=-\frac\pi4+O(x^{-ct}).
\]

This is a consistency check only and is not used in the proof.

---

## 6. Consequence for a one-sided positive-index Bregman window

Round 17 defines

\[
D_j^\psi=\sum_{k\ne j}\psi_k\delta_{jk},
\qquad
\delta_{jk}=\frac1{x_j-x_k}-\frac1{\xi_j-\xi_k}.
\]

For any finite or absolutely justified sum,

\[
\boxed{
\sum_j\psi_jD_j^\psi=0,
}
\]

by antisymmetry of \(\delta_{jk}\). Thus, on a cutoff supported entirely in a positive high-index window, the constant \(-\pi/8\) may be subtracted exactly:

\[
\boxed{
\mathscr R_{\xi,\psi}
=-4\sum_j\psi_jD_j^\psi
\left(S_j^\xi+\frac\pi8\right).
}
\]

If \(J\le j\le CJ\) on the support, then

\[
\varepsilon_J:=
\sup\left|S_j^\xi+\frac\pi8\right|
\ll_C\frac{\log J}{\sqrt J}.
\]

Writing

\[
N_\psi=\sum_j\psi_j,
\qquad
\mathscr B_\psi=4\sum_j\psi_j(D_j^\psi)^2,
\]

Cauchy--Schwarz gives

\[
\boxed{
|\mathscr R_{\xi,\psi}|
\le2\varepsilon_J\sqrt{N_\psi\mathscr B_\psi}.
}
\]

Hence, for every \(\eta>0\),

\[
\boxed{
|\mathscr R_{\xi,\psi}|
\le
\eta\mathscr B_\psi
+\eta^{-1}\varepsilon_J^2N_\psi.
}
\]

If \(N_\psi\asymp J\), then

\[
\boxed{
\varepsilon_J^2N_\psi\ll(\log J)^2.
}
\]

Thus the reference inhomogeneity is absorbable at only polylogarithmic additive cost on a one-sided high window.

### Symmetric-window caveat

For a symmetric cutoff containing both positive and negative indices, the leading reference force is

\[
-\frac\pi8\operatorname{sgn}(j),
\]

not a single constant. Therefore the preceding cancellation must not be applied blindly to a symmetric Rodgers--Tao cutoff. In that setting one must separate the two signs; the remaining leading term is a regular cross-origin interaction and requires its own estimate.

---

## 7. Circularity audit

The theorem uses only the explicit function \(\Psi\), calculus for \(\Psi^{-1}\), elementary paired principal-value summation, and standard integral identities. It does not assume RH, \(\Lambda\le0\), actual zero spacing, pair correlation, Laguerre positivity, or a no-collision estimate.

---

## 8. Status

- \(S_j^\xi=-\pi/8+O((\log j)/\sqrt j)\) for \(j>0\): **PROVED**;
- signed negative-index version: **PROVED**;
- positive-window drift cancellation and absorption: **PROVED**;
- symmetric-cutoff leading cross-origin term: **OPEN / NEXT ESTIMATE**;
- relation to Polymath velocity: **CONSISTENCY CHECK**;
- novelty: **UNVERIFIED**;
- RH: **OPEN**.
