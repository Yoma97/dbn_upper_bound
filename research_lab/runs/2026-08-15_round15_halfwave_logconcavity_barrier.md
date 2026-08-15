# Round 15 — Half-wave log-concavity and a rigorous TP2 insufficiency barrier

**Date:** 2026-08-15

**RH status:** OPEN.

---

## 1. Quantitative monotonicity of the heat-weighted Riemann density

Let

\[
K(r)=\Phi(\sqrt r),\qquad f(r)=\log K(r),
\]

and

\[
K_t(r)=e^{tr}K(r).
\]

The established Csordas--Varga inequality gives

\[
f''(r)<0\qquad(r>0).
\]

Recall

\[
q(u)=-\frac{\Phi'(u)}{u\Phi(u)}=-2f'(u^2).
\]

Hence \(q'(u)>0\).

We also need only the very crude quantitative fact \(q(0)>1\). This follows directly from the defining theta series, without RH.

Write \(a=\pi n^2\). At \(u=0\), termwise differentiation gives

\[
\Phi(0)=\sum_{n\ge1}a(2a-3)e^{-a},
\]

and, using evenness \(\Phi'(0)=0\),

\[
\Phi''(0)=\sum_{n\ge1}a(32a^3-224a^2+330a-75)e^{-a}.
\]

The n=1 contribution to \(\Phi''(0)\) is less than \(-34.87\). The n=2 contribution is less than \(1.412\). For \(n\ge3\), since

\[
32a^3-224a^2+330a-75<32a^3,
\]

the tail is bounded by

\[
32\pi^4\sum_{n\ge3}n^8e^{-\pi n^2}<1.1\times10^{-5}.
\]

Thus

\[
\Phi''(0)<-33.45.
\]

Similarly the positive series for \(\Phi(0)\) gives the crude bound \(0<\Phi(0)<1\). Therefore

\[
q(0):=\lim_{u\downarrow0}q(u)
=-\frac{\Phi''(0)}{\Phi(0)}>33>1.
\]

Since q is increasing,

\[
q(u)>1\qquad(u\ge0).
\]

Consequently, for every \(0\le t\le1/2\),

\[
\frac d{dr}\log K_t(r)
=t+f'(r)
=t-\frac12q(\sqrt r)<0,
\]

while

\[
\frac{d^2}{dr^2}\log K_t(r)=f''(r)<0.
\]

Hence

\[
\boxed{K_t(r)=e^{tr}\Phi(\sqrt r)\text{ is strictly decreasing and strictly log-concave on }(0,\infty).}
\]

All estimates here are independent of RH.

---

## 2. Strict log-concavity of the sine weight

Recall

\[
w_t(u)=u e^{tu^2}\Phi(u)=uK_t(u^2).
\]

Let \(F_t(r)=\log K_t(r)\). Then

\[
\log w_t(u)=\log u+F_t(u^2).
\]

Differentiating twice,

\[
\frac{d^2}{du^2}\log w_t(u)
=-\frac1{u^2}+2F_t'(u^2)+4u^2F_t''(u^2).
\]

All three terms on the right are strictly negative for \(u>0\). Therefore

\[
\boxed{w_t\text{ is strictly log-concave on }(0,\infty),\quad 0\le t\le1/2.}
\]

This is a genuine structural theorem for the heat-weighted Riemann density.

---

## 3. Half-wave mass sequence is log-concave

Fix \(x>0\) and write

\[
h=\frac\pi x.
\]

Define

\[
a_n(t,x)=\int_{nh}^{(n+1)h}w_t(u)|\sin(xu)|\,du.
\]

On \(0<s<h\), set

\[
g_x(s)=\sin(xs),
\]

and extend \(g_x\) by zero outside \([0,h]\). Because

\[
\frac{d^2}{ds^2}\log\sin(xs)=-x^2\csc^2(xs)<0,
\]

\(g_x\) is log-concave in the extended sense.

Define the continuous half-wave mass function

\[
A(y)=\int_0^h w_t(y+s)g_x(s)\,ds.
\]

The integrand is log-concave jointly in \((y,s)\): \(\log w_t(y+s)\) is concave because \(y+s\) is affine, and \(\log g_x(s)\) is concave. By the Prekopa--Leindler marginal theorem, \(A(y)\) is log-concave. Since

\[
a_n=A(nh),
\]

we obtain

\[
\boxed{a_n^2\ge a_{n-1}a_{n+1}\qquad(n\ge1).}
\]

Equivalently, the ratios

\[
\rho_n=\frac{a_{n+1}}{a_n}
\]

are non-increasing.

**Status:** PROVED.

---

## 4. Companion masses have a monotone likelihood ratio

Define

\[
b_n(t,x)=\int_{nh}^{(n+1)h}q(u)w_t(u)|\sin(xu)|\,du.
\]

Because q is strictly increasing and adjacent half-wave intervals are ordered,

\[
\boxed{
r_n:=\frac{b_n}{a_n}\text{ is strictly increasing in }n.
}
\]

Thus the collision equations

\[
S_0=\sum_{n\ge0}(-1)^na_n=0,
\qquad
S_1=\sum_{n\ge0}(-1)^nb_n=0
\]

would require simultaneous vanishing of two alternating sums where:

1. \((a_n)\) is positive and log-concave;
2. \(b_n/a_n\) is strictly increasing.

This looks strong, but it is not strong enough.

---

## 5. Exact abstract counterexample: TP2-level data do not exclude double cancellation

### Proposition 15.1

There exist an infinite positive log-concave sequence \((a_n)\) and a strictly increasing positive sequence \((r_n)\) such that

\[
\sum_{n\ge0}(-1)^na_n=0
\]

and

\[
\sum_{n\ge0}(-1)^nr_na_n=0.
\]

### Construction

Set \(s=1/20\), and define

\[
a_0=1,\qquad a_1=10,\qquad a_2=10,
\]

and for \(n\ge3\),

\[
a_n=(1+s)s^{n-3}.
\]

The consecutive ratios are

\[
10,\quad 1,\quad \frac{1+s}{10},\quad s,\quad s,\dots,
\]

which are non-increasing; hence \((a_n)\) is positive log-concave.

Its alternating sum is

\[
1-10+10-(1+s)\sum_{k\ge0}(-s)^k
=1-\frac{1+s}{1+s}=0.
\]

Now define

\[
r_0=1,\quad r_1=2,\quad r_2=3,
\]

and, for \(k\ge0\),

\[
r_{3+k}=R+k,
\qquad
R=11+\frac{s}{1+s}.
\]

This sequence is strictly increasing. The first three terms of the weighted alternating sum give

\[
1-20+30=11.
\]

The tail gives

\[
-(1+s)\sum_{k\ge0}(-s)^k(R+k).
\]

Using

\[
\sum_{k\ge0}(-s)^k=\frac1{1+s},
\qquad
\sum_{k\ge0}k(-s)^k=-\frac{s}{(1+s)^2},
\]

the tail equals

\[
-R+\frac{s}{1+s}=-11.
\]

Hence the weighted alternating sum also vanishes.

This proves the proposition. ∎

---

## 6. Structural conclusion

The independently provable Riemann-kernel facts

- strict log-concavity of \(w_t\),
- log-concavity of the half-wave masses \((a_n)\), and
- strict monotone-likelihood-ratio ordering \(b_n/a_n\),

are **not sufficient as abstract axioms** to rule out a collision.

Therefore any C6 proof based only on TP2/log-concavity plus monotone reweighting is structurally incomplete.

This is a useful no-go result: it prevents the program from incorrectly promoting kernel log-concavity to a hidden RH proof.

---

## 7. Connection with prior determinantal/sign-regularity work

Nuttall's determinantal program (arXiv:1111.1128) explicitly relates log-concavity to order-2 sign-reverse regularity of the kernel \(\Phi(u+v)\), and studies higher compound determinants/sign-regularity. That work reports rigorous progress at low orders and warns that the most direct sign-regular extension does not persist indefinitely.

Our half-wave calculation reaches the same conceptual boundary from a different direction: **order-2 sign regularity controls the shape of the masses but cannot forbid the two oscillatory cancellations required at a collision.**

Accordingly, simply asking for more consequences of log-concavity is no longer a priority.

---

## 8. New single target

A surviving C6 mechanism must introduce structure beyond TP2. The narrow target is now:

### CANDIDATE 15-A — finite oscillatory sign-regularity bridge

Find the weakest finite-order determinant/variation-diminishing property of the specific tilted kernel

\[
K_t(r)=e^{tr}\Phi(\sqrt r)
\]

that controls the two functions

\[
\sin(x\sqrt r),\qquad q(\sqrt r)\sin(x\sqrt r)
\]

strongly enough to prevent their \(K_t(r)dr\)-integrals from vanishing simultaneously, **without requiring sign-regularity of all orders**.

The theorem must have a fixed finite complexity independent of x; otherwise the required order grows with the number of sine oscillations and the route collapses back toward an all-orders/RH-equivalent criterion.

### Promotion gate

A candidate is promoted only if it proves a nontrivial finite-order determinant inequality for \(\Phi\) and has an application not logically equivalent to RH.

---

## 9. Status

- \(q(0)>1\) and q increasing: **PROVED**.
- \(K_t(r)\) decreasing/log-concave for \(0\le t\le1/2\): **PROVED**.
- \(w_t(u)\) strictly log-concave: **PROVED**.
- half-wave masses \(a_n\) log-concave: **PROVED**.
- half-wave likelihood ratios \(b_n/a_n\) increasing: **PROVED**.
- TP2/log-concavity + MLR suffices for no collision: **REFUTED by exact abstract counterexample**.
- finite-order oscillatory sign-regularity bridge: **CANDIDATE / OPEN**.
- independent C6: **OPEN**.
- RH: **OPEN**.
- novelty: **UNVERIFIED**.
