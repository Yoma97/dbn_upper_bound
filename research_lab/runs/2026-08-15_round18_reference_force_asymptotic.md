# Round 18 — Classical-location reference force tends to \(-\pi/8\)

**Date:** 2026-08-15

**Status labels:** PROVED / CONDITIONAL / CANDIDATE / REFUTED / NOVELTY UNVERIFIED.

**RH status:** OPEN.

## 0. Purpose

Round 17 produced the exact relative Bregman balance

\[
\partial_t\mathcal C_\psi
=-\mathscr B_\psi+\mathscr F_{\partial\psi}+\mathscr R_{\xi,\psi},
\]

with

\[
\mathscr R_{\xi,\psi}
=-4\sum_j\psi_jD_j^\psi S_j^\xi,
\qquad
S_j^\xi:=\operatorname{PV}\sum_{k\ne j}\frac1{\xi_j-\xi_k}.
\]

The present round computes the asymptotic of the reference force for the Rodgers--Tao classical locations. The result is

\[
\boxed{
S_j^\xi=-\frac\pi8+O\!\left(\frac{\log j}{\sqrt j}\right)
\qquad(j\to+\infty).
}
\]

The constant drift cancels exactly from the relative entropy law, leaving only a small reference inhomogeneity.

**Novelty of this asymptotic/packaging:** NOVELTY UNVERIFIED.

---

## 1. Rodgers--Tao classical locations

Define

\[
\Psi(x)
:=\frac{x}{4\pi}\log\frac{x}{4\pi}-\frac{x}{4\pi}
=\frac{x}{4\pi}\left(\log\frac{x}{4\pi}-1\right).
\]

For \(j\ge1\), Rodgers--Tao define \(\xi_j\) as the unique solution of

\[
\Psi(\xi_j)=j,
\]

and set

\[
\xi_{-j}=-\xi_j.
\]

Let

\[
x_0:=4\pi e.
\]

Then \(\Psi(x_0)=0\), \(\Psi\) is strictly increasing on \([x_0,\infty)\), and we write

\[
\phi:=\Psi^{-1}:[0,\infty)\to[x_0,\infty).
\]

Thus

\[
\phi(j)=\xi_j.
\]

Writing

\[
L(x):=\log\frac{x}{4\pi},
\]

we have

\[
\Psi'(x)=\frac{L(x)}{4\pi},
\]

and hence, at \(x=\phi(u)\),

\[
\boxed{
\phi'(u)=\frac{4\pi}{L(x)}.
}
\]

Differentiating again,

\[
\boxed{
\phi''(u)
=-\frac{16\pi^2}{xL(x)^3}<0.
}
\]

In particular,

\[
\boxed{
\frac{|\phi''(u)|}{\phi'(u)^2}
=\frac1{xL(x)}.
}
\]

Also, since

\[
u=\Psi(x)=\frac{x}{4\pi}(L(x)-1),
\]

for large \(u\)

\[
x\asymp\frac{u}{\log u},
\qquad
L(x)\asymp\log u.
\]

These are elementary consequences of the definition and agree with the spacing estimates recorded by Rodgers--Tao.

---

## 2. The reference force as an absolutely paired positive-index sum

For \(j>0\), set

\[
x:=\xi_j=\phi(j).
\]

The symmetric principal value over \(\mathbb Z^*=\mathbb Z\setminus\{0\}\) can be paired using \(\xi_{-k}=-\xi_k\):

\[
S_j^\xi
=\frac1{2x}
+\sum_{\substack{k\ge1\\k\ne j}}
\left(
\frac1{x-\xi_k}+\frac1{x+\xi_k}
\right).
\]

Define

\[
g_x(u):=rac{2x}{x^2-\phi(u)^2}.
\]

Then

\[
\boxed{
S_j^\xi
=\frac1{2x}+\sum_{\substack{k\ge1\\k\ne j}}g_x(k).
}
\]

The paired tail is absolutely convergent because

\[
g_x(k)=O\!\left(\frac{x}{\xi_k^2}\right)
=O\!\left(\frac{x\log^2k}{k^2}\right).
\]

Thus no summation ambiguity remains after the \(\pm k\) pairing.

---

## 3. Continuum principal-value model — PROVED

Define

\[
I(x):=\operatorname{PV}\int_0^\infty g_x(u)\,du.
\]

Substitute \(y=\phi(u)\), so that

\[
du=\Psi'(y)dy
=\frac1{4\pi}\log\frac y{4\pi}\,dy.
\]

Therefore

\[
I(x)
=\frac{x}{2\pi}\operatorname{PV}
\int_{4\pi e}^\infty
\frac{\log(y/4\pi)}{x^2-y^2}\,dy.
\]

Now set \(y=xv\), with

\[
a:=\frac{4\pi e}{x}.
\]

Then

\[
\boxed{
I(x)
=\frac1{2\pi}\operatorname{PV}
\int_a^\infty
\frac{\log(xv/4\pi)}{1-v^2}\,dv.
}
\]

The standard principal-value identities are

\[
\operatorname{PV}\int_0^\infty\frac{dv}{1-v^2}=0,
\]

and

\[
\int_0^\infty\frac{\log v}{1-v^2}\,dv
=-\frac{\pi^2}{4}.
\]

For the second identity, split at \(1\). On \((0,1)\),

\[
\int_0^1\frac{\log v}{1-v^2}\,dv
=-\sum_{n\ge0}\frac1{(2n+1)^2}
=-\frac{\pi^2}{8},
\]

and the substitution \(v\mapsto1/v\) gives the same value on \((1,\infty)\).

Consequently the full lower-limit-zero integral equals

\[
-\frac\pi8.
\]

The omitted interval \((0,a)\) contributes at most

\[
O\!\left(\frac{\log x}{x}\right),
\]

so

\[
\boxed{
I(x)=-\frac\pi8
+O\!\left(\frac{\log x}{x}\right).
}
\]

(The lower-limit error can be sharpened further because \(a=4\pi e/x\), but this is not needed.)

---

## 4. Discrete-to-continuum estimate — PROVED

We prove

\[
\sum_{\substack{k\ge1\\k\ne j}}g_x(k)
-I(x)
=O\!\left(\frac{\log j}{\sqrt j}\right).
\]

Let

\[
M:=\lfloor\sqrt j\rfloor,
\qquad
h:=\phi'(j)=\frac{4\pi}{L(x)}.
\]

For large \(j\), throughout \(|u-j|\le M\) one has

\[
\phi(u)\asymp x,
\qquad
\phi'(u)\asymp h,
\qquad
\frac{|\phi''(u)|}{h^2}\ll\frac1{xL(x)}.
\]

These follow directly from the formulas in Section 1 and \(M=o(j)\).

### 4.1 Far region

A direct differentiation gives

\[
g_x'(u)
=\frac{4x\phi(u)\phi'(u)}{(x^2-\phi(u)^2)^2}>0
\]

for \(u\ne j\). Hence \(g_x\) is monotone on each of

\[
[0,j-M],\qquad[j+M,\infty).
\]

The elementary sum-integral comparison for a monotone function therefore gives a total far-region error bounded by endpoint terms. Since

\[
x-\phi(j-M)\asymp hM,
\qquad
\phi(j+M)-x\asymp hM,
\]

we have

\[
|g_x(j\pm M)|\ll\frac1{hM}+\frac1x
\ll\frac{\log j}{M}.
\]

Thus

\[
\boxed{
\text{far error}
\ll\frac{\log j}{M}+rac1x.
}
\]

### 4.2 Near singular region

For \(0<s\le M\), put

\[
a_s:=x-\phi(j-s)>0,
\qquad
b_s:=\phi(j+s)-x>0.
\]

Using

\[
\frac{2x}{a(2x-a)}=\frac1a+\frac1{2x-a},
\]

and

\[
-\frac{2x}{b(2x+b)}=-\frac1b-\frac1{2x+b},
\]

we obtain

\[
g_x(j-s)+g_x(j+s)
=\left(\frac1{a_s}-\frac1{b_s}\right)
+\left(\frac1{2x-a_s}-\frac1{2x+b_s}\right).
\]

Taylor's theorem in symmetric difference form gives

\[
|a_s-b_s|
\le s^2\sup_{|u-j|\le M}|\phi''(u)|.
\]

Also

\[
a_s,b_s\gg hs.
\]

Therefore

\[
\left|\frac1{a_s}-\frac1{b_s}\right|
\ll\frac1{xL(x)}.
\]

Since \(a_s+b_s\ll hs\) and \(a_s,b_s\le x/2\) for large \(j\),

\[
\left|
\frac1{2x-a_s}-\frac1{2x+b_s}
\right|
\ll\frac{hs}{x^2}.
\]

Hence uniformly for \(0<s\le M\),

\[
\boxed{
|g_x(j-s)+g_x(j+s)|
\ll\frac1{xL(x)}+\frac{hs}{x^2}.
}
\]

Summing over integer \(s=1,\dots,M\),

\[
\sum_{s=1}^M
|g_x(j-s)+g_x(j+s)|
\ll
\frac{M}{xL(x)}+rac{hM^2}{x^2}.
\]

The identical pointwise estimate integrated over \(0<s<M\) gives

\[
\left|
\operatorname{PV}\int_{j-M}^{j+M}g_x(u)du
\right|
\ll
\frac{M}{xL(x)}+rac{hM^2}{x^2}.
\]

Thus the local discrete-continuum discrepancy is bounded by the same order.

Using

\[
xL(x)\asymp j,
\qquad
h\asymp\frac1{\log j},
\qquad
x\asymp\frac j{\log j},
\]

we obtain

\[
\boxed{
\text{near error}
\ll
\frac Mj+rac{M^2\log j}{j^2}.
}
\]

### 4.3 Optimize the split

Combining the near and far regions, plus the harmless \(1/(2x)\) self-negative-root term,

\[
S_j^\xi-I(x)
\ll
\frac{\log j}{M}
+rac Mj
+rac{M^2\log j}{j^2}
+rac1x.
\]

With \(M=\lfloor\sqrt j\rfloor\),

\[
\boxed{
S_j^\xi-I(\xi_j)
=O\!\left(\frac{\log j}{\sqrt j}\right).
}
\]

Together with Section 3,

\[
\boxed{
S_j^\xi
=-\frac\pi8
+O\!\left(\frac{\log j}{\sqrt j}\right).
}
\]

This proves the claimed reference-force asymptotic.

---

## 5. Interpretation as collective drift

If the particle configuration were exactly the classical locations \(x_j=\xi_j\), the zero ODE would formally give

\[
\dot x_j=2S_j^\xi
=-\frac\pi4+o(1).
\]

Thus the slowly varying Riemann--von Mangoldt background is not a static equilibrium; it has an asymptotic collective left drift \(-\pi/4\).

This is independently consistent with the Polymath high-positive-time asymptotic for real zeros in the solid region,

\[
\dot x(t)=-\frac\pi4+O(x^{-ct}).
\]

This consistency is a check, not an ingredient of the proof above.

---

## 6. Exact cancellation of the constant drift in Round 17

Recall

\[
D_j^\psi
=\sum_{k\ne j}\psi_k\delta_{jk},
\qquad
\delta_{jk}=-\delta_{kj}.
\]

For a finite-support cutoff (or any justified absolutely convergent version),

\[
\boxed{
\sum_j\psi_jD_j^\psi
=\sum_{j,k}\psi_j\psi_k\delta_{jk}=0.
}
\]

Therefore for any constant \(c\),

\[
\mathscr R_{\xi,\psi}
=-4\sum_j\psi_jD_j^\psi(S_j^\xi-c).
\]

Taking

\[
c=-\frac\pi8,
\]

we obtain the canonical drift-subtracted form

\[
\boxed{
\mathscr R_{\xi,\psi}
=-4\sum_j\psi_jD_j^\psi
\left(S_j^\xi+\frac\pi8\right).
}
\]

Thus the asymptotic collective drift does not contribute to the relative entropy production.

---

## 7. High-window bound for the reference channel — PROVED

Suppose the cutoff is supported on a positive-index window

\[
J\le j\le CJ
\]

for fixed \(C>1\), and set

\[
N_\psi:=\sum_j\psi_j.
\]

The theorem gives

\[
\varepsilon_J
:=\sup_{j\in[J,CJ]}
\left|S_j^\xi+\frac\pi8\right|
\ll_C\frac{\log J}{\sqrt J}.
\]

By Cauchy--Schwarz and

\[
\mathscr B_\psi=4\sum_j\psi_j(D_j^\psi)^2,
\]

\[
\boxed{
|\mathscr R_{\xi,\psi}|
\le
2\varepsilon_J\sqrt{N_\psi\mathscr B_\psi}.
}
\]

Therefore for every \(\eta>0\), Young's inequality gives

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
\varepsilon_J^2N_\psi
\ll (\log J)^2.
}
\]

Thus the reference-force channel costs only a polylogarithmic additive error on a macroscopic high-index window, while an arbitrary small fraction of the bulk dissipation can absorb its mixed term.

This is much smaller than the large energy scales that arise in the Rodgers--Tao exhaustion argument. However, no claim is made here for their exact cutoff \(\psi_T\) until its support/decay is inserted explicitly.

---

## 8. Circularity audit

The proof uses only:

1. the explicit definition of the classical locations \(\Psi(\xi_j)=j\);
2. elementary calculus for \(\Psi^{-1}\);
3. principal-value / paired sum algebra;
4. elementary sum-integral comparison;
5. standard integral identities.

It does **not** use:

- RH;
- \(\Lambda\le0\);
- actual zeros of \(H_t\);
- pair correlation;
- Laguerre positivity;
- any lower gap estimate for the actual zero process.

Hence the reference asymptotic is logically independent of RH.

---

## 9. Status and next target

- reference-force asymptotic \(S_j^\xi=-\pi/8+O((\log j)/\sqrt j)\): **PROVED**;
- constant-drift cancellation in the relative entropy: **PROVED**;
- high-window reference-channel absorption estimate: **PROVED**;
- identification with Polymath \(-\pi/4\) velocity: **CONSISTENCY CHECK ONLY**;
- novelty: **UNVERIFIED**;
- RH: **OPEN**.

The remaining difficult channel in Round 17 is now primarily the boundary flux

\[
\boxed{
\mathscr F_{\partial\psi}
=-4\sum_j\psi_jD_j^\psi F_j^\psi.
}
\]

The next target is an explicit estimate of the form

\[
|\mathscr F_{\partial\psi}|
\le
\eta\mathscr B_\psi
+\eta^{-1}\,\mathcal E_{\rm boundary}(\psi),
\]

where \(\mathcal E_{\rm boundary}\) is expressed in terms of cutoff variation and a relative defect/energy already controlled by the Rodgers--Tao machinery, not by an assumed no-collision bound.
