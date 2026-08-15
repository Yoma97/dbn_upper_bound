# Round 29 — Associated-kernel autocorrelation decomposition and the unique spectral-curvature defect

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / STRUCTURAL REDUCTION / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 28 showed that the differential Riemann-kernel coupling lands on the first Laguerre expression and its associated kernel `K_1`. This round decomposes `K_1` into an automatically positive-definite autocorrelation plus one explicit curvature defect.

Let

\[
\psi_t(u)=e^{tu^2}\Phi(u)
\]

and define

\[
K_{0,t}(r)
:=\int_{\mathbb R}\psi_t(s+r)\psi_t(s-r)\,ds,
\]

\[
K_{1,t}(r)
:=\int_{\mathbb R}\psi_t(s+r)\psi_t(s-r)s^2\,ds.
\]

Put

\[
g_t(u):=u\psi_t(u)
\]

and

\[
C_{g,t}(r)
:=\int_{\mathbb R}g_t(s+r)g_t(s-r)\,ds.
\]

Then exactly

\[
\boxed{
K_{1,t}(r)=C_{g,t}(r)+r^2K_{0,t}(r).
}
\]

Both `K_{0,t}` and `C_{g,t}` are autocorrelations and hence positive definite. Thus the only obstruction to positive definiteness of `K_{1,t}` is the spectral effect of multiplying the already positive-definite kernel `K_{0,t}` by `r^2`.

In Fourier space this is exactly the Laguerre curvature defect

\[
(H_t')^2-H_tH_t''.
\]

Therefore an exact theta-series expansion will be useful only if it controls this **spectral curvature**, not merely if it expresses `K_1` as a sum of positive pointwise terms.

---

## 1. Correlation normalization

For a real `L^2` function `f`, define the symmetric correlation

\[
C_f(r):=\int_{\mathbb R}f(s+r)f(s-r)\,ds.
\]

By the change of variables `y=s-r`,

\[
C_f(r)=\int_{\mathbb R}f(y+2r)f(y)\,dy.
\]

Thus `C_f` is a rescaled autocorrelation.

Under the full Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(u)e^{-i\xi u}\,du,
\]

one has

\[
\boxed{
\widehat{C_f}(\omega)
=\frac12\left|\widehat f(\omega/2)\right|^2\ge0.
}
\]

Hence `C_f` is positive definite by Bochner.

For the even kernel `psi_t`,

\[
K_{0,t}=C_{\psi_t}.
\]

Therefore

\[
\boxed{
\widehat K_{0,t}(\omega)
=\frac12|\widehat\psi_t(\omega/2)|^2\ge0.
}
\]

Since

\[
\widehat\psi_t(x)=2H_t(x)
\]

under the half-line cosine normalization,

\[
\boxed{
\widehat K_{0,t}(2x)=2H_t(x)^2.
}
\]

This is the automatically positive `n=0` associated kernel in the Csordas theory.

---

## 2. Exact `K_1` decomposition — PROVED

By definition

\[
C_{g,t}(r)
=\int_{\mathbb R}
(s+r)(s-r)
\psi_t(s+r)\psi_t(s-r)\,ds.
\]

Because

\[
(s+r)(s-r)=s^2-r^2,
\]

we obtain

\[
C_{g,t}(r)
=K_{1,t}(r)-r^2K_{0,t}(r).
\]

Thus

\[
\boxed{
K_{1,t}(r)
=C_{g,t}(r)+r^2K_{0,t}(r).
}
\]

The first term is another autocorrelation, so

\[
\boxed{
\widehat C_{g,t}(\omega)
=\frac12|\widehat g_t(\omega/2)|^2\ge0.
}
\]

Since

\[
\widehat g_t(\xi)
=i\,\partial_\xi\widehat\psi_t(\xi),
\]

for real even `psi_t`,

\[
\widehat C_{g,t}(2x)
=2H_t'(x)^2.
\]

Thus one entire part of the `K_1` spectrum is manifestly nonnegative.

---

## 3. The second term is the unique spectral-curvature defect

Multiplication by `r^2` corresponds to minus two Fourier derivatives:

\[
\widehat{r^2K_{0,t}}(\omega)
=-\partial_\omega^2\widehat K_{0,t}(\omega).
\]

Using

\[
\widehat K_{0,t}(\omega)
=\frac12 h(\omega/2)^2,
\qquad
h:=\widehat\psi_t,
\]

we compute

\[
\partial_\omega^2\widehat K_{0,t}(\omega)
=\frac14\left(h'(\omega/2)^2+h(\omega/2)h''(\omega/2)\right).
\]

Also

\[
\widehat C_{g,t}(\omega)
=\frac12 h'(\omega/2)^2.
\]

Therefore

\[
\boxed{
\widehat K_{1,t}(\omega)
=\frac14\left(
h'(\omega/2)^2
-h(\omega/2)h''(\omega/2)
\right).
}
\]

Putting `omega=2x` and `h=2H_t`,

\[
\boxed{
\widehat K_{1,t}(2x)
=(H_t'(x))^2-H_t(x)H_t''(x)
=L_1(H_t)(x).
}
\]

This recovers the Csordas associated-kernel formula with the present full-Fourier normalization and makes the sign obstruction completely explicit.

---

## 4. Heat-time derivative relation — PROVED

Because

\[
\partial_t\psi_t(u)=u^2\psi_t(u),
\]

we have

\[
\begin{aligned}
\partial_tK_{0,t}(r)
&=\int_{\mathbb R}
\bigl((s+r)^2+(s-r)^2\bigr)
\psi_t(s+r)\psi_t(s-r)\,ds\\
&=2\int_{\mathbb R}(s^2+r^2)
\psi_t(s+r)\psi_t(s-r)\,ds.
\end{aligned}
\]

Hence

\[
\boxed{
\partial_tK_{0,t}
=2K_{1,t}+2r^2K_{0,t}.
}
\]

Equivalently

\[
\boxed{
K_{1,t}
=\frac12\partial_tK_{0,t}-r^2K_{0,t}.
}
\]

Combining with Section 2 also gives

\[
\partial_tK_{0,t}
=2C_{g,t}+4r^2K_{0,t}.
\]

Pointwise, every term on the right is positive for the Riemann kernel. Therefore

\[
\partial_tK_{0,t}(r)>2r^2K_{0,t}(r).
\]

But this pointwise time-growth inequality does **not** imply the Fourier sign of `K_{1,t}`, because the Fourier transform is not order preserving for arbitrary pointwise inequalities.

---

## 5. A useful local curvature identity at the origin — PROVED

For any positive smooth strictly log-concave even `psi`, let

\[
K_1(r)=\int\psi(s+r)\psi(s-r)s^2\,ds.
\]

Then `K_1` is even, so `K_1'(0)=0`. Differentiating twice,

\[
\begin{aligned}
K_1''(0)
&=2\int_{\mathbb R}
\bigl(\psi(s)\psi''(s)-\psi'(s)^2\bigr)s^2\,ds\\
&=2\int_{\mathbb R}
\psi(s)^2(\log\psi)''(s)s^2\,ds.
\end{aligned}
\]

Thus strict log-concavity gives

\[
\boxed{K_1''(0)<0.}
\]

So `K_1` has a strict local maximum at the origin and is locally concave there.

This immediately rules out a naive application of the elementary Pólya criterion that would require global convexity on the positive axis. The associated kernel lies in a subtler positive-definiteness regime.

---

## 6. Why a positive theta-series decomposition is not enough

Suppose one expands the Riemann theta kernel into positive summands on the positive half-axis and obtains

\[
K_{1,t}(r)=\sum_\nu A_{\nu,t}(r),
\qquad
A_{\nu,t}(r)\ge0.
\]

This proves only pointwise positivity, which is already known directly from the defining integral.

To deduce

\[
L_1(H_t)(x)=\widehat K_{1,t}(2x)\ge0,
\]

one needs either:

1. each summand `A_{nu,t}` to be positive definite; or
2. a cancellation theorem showing that the total Fourier transform remains nonnegative; or
3. a spectral-curvature inequality controlling
   \[
   -\partial_\omega^2\widehat K_{0,t}
   \]
   by the manifestly positive autocorrelation spectrum `widehat C_{g,t}`.

Thus the useful target is not “find positive theta terms.” It is

\[
\boxed{
\widehat C_{g,t}(\omega)
\ge
\partial_\omega^2\widehat K_{0,t}(\omega)
}
\]

in the exact range needed, which is simply the `L_1>=0` inequality written in defect form.

A theta decomposition is progress only if it supplies an **independent estimate of this defect**.

---

## 7. Collision interpretation

At a critical point `H_t'(x)=0`,

\[
L_1(H_t)(x)
=-H_t(x)H_t''(x)
=H_t(x)\partial_tH_t(x),
\]

because `H_t=-H_t''` under backward heat flow.

Hence

\[
\boxed{
L_1(H_t)(x)
=\frac12\partial_t(H_t(x)^2)
\qquad\text{whenever }H_t'(x)=0.
}
\]

A collision is a critical point at which this spectral transversality quantity also vanishes because `H_t=0`.

Again, the associated-kernel problem is exactly the problem of preventing the critical value from crossing zero.

---

## 8. Consequence for the immediate theta target

Round 28 proposed an exact theta-series decomposition of `K_{1,t}`. Round 29 sharpens the acceptance criterion.

A theta decomposition is promoted only if it yields one of:

- a positive-definite decomposition of `C_{g,t}+r^2K_{0,t}`;
- a rigorous sign bound on the Fourier curvature of `K_{0,t}`;
- a defect term that can be bounded using an independent arithmetic/theta identity.

If it merely rewrites `K_{1,t}` as a sum of positive functions of `r`, it is rejected as collision-blind pointwise positivity.

---

## 9. Program status

The local kernel route has now reached a one-channel bottleneck:

\[
\boxed{
\text{automatic PD autocorrelations}
+\text{one }r^2K_0\text{ spectral-curvature defect}.
}
\]

This is a cleaner target than the undifferentiated request “prove `L_1>0`,” but it is mathematically equivalent unless extra Riemann-specific structure controls the defect.

The next local calculation should therefore use the explicit theta/Poisson structure specifically on `K_{0,t}` and its curvature term. If no sign-separating identity emerges, the local kernel route should be frozen and the program should pivot to a cross-frontier bridge.

---

## 10. Status

- `K_0` autocorrelation positive definite: **PROVED**;
- `C_g` autocorrelation positive definite: **PROVED**;
- exact decomposition `K_1=C_g+r^2K_0`: **PROVED**;
- exact time law `partial_t K_0=2K_1+2r^2K_0`: **PROVED**;
- Fourier defect equals `L_1`: **PROVED**;
- strict local concavity `K_1''(0)<0` for strictly log-concave kernel: **PROVED**;
- elementary convexity/Pólya route for `K_1`: **BLOCKED**;
- theta-specific control of the spectral-curvature defect: **OPEN / NEXT TEST**;
- RH: **OPEN**;
- novelty of this decomposition/packaging: **UNVERIFIED**.
