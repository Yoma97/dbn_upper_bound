# Convention Lock — Riemann Research Lab

All agents and all proof cards must use these conventions unless a claim explicitly declares a conversion map and checks it algebraically.

## Riemann xi and the Polymath H-family

\[
\xi(s)=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Use the Polymath/Rodgers–Tao normalization

\[
H_0(z)=\frac18\,\xi\!\left(\frac12+\frac{iz}{2}\right),
\qquad
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\]

so that

\[
\partial_t H_t=-\partial_z^2H_t.
\]

The Riemann Hypothesis is equivalent to all zeros of \(H_0\) being real, and to \(\Lambda\le0\). Together with the established Rodgers–Tao result \(\Lambda\ge0\), RH is equivalent to \(\Lambda=0\).

Do not switch silently to \(\Xi(x)=\xi(1/2+ix)\). If that notation is used, write the explicit scaling relation to \(H_0\).

## Fourier transform

Default convention:

\[
\widehat f(\xi)=\int_{\mathbb R} f(x)e^{-2\pi i x\xi}\,dx.
\]

Any source using another convention must be converted explicitly, including all \(2\pi\) factors.

## Generalized Laguerre coefficients

For a real entire function \(F\), define \(L_n(x;F)\) by

\[
F(x+iy)F(x-iy)=\sum_{n\ge0}L_n(x;F)y^{2n}.
\]

Equivalently,

\[
L_n(x;F)=\frac1{(2n)!}\left.\partial_y^{2n}|F(x+iy)|^2\right|_{y=0}.
\]

Thus

\[
L_1=(F')^2-FF'',
\]

and

\[
L_2=\frac1{12}FF^{(4)}-\frac13F'F^{(3)}+\frac14(F'')^2.
\]

Every paper/source using a different normalization for generalized Laguerre expressions must be converted before comparison.

## Heat-time direction

Increasing \(t\) in \(H_t\) is the de Bruijn–Newman direction in which real-rootedness, once obtained, persists. Do not call \(\partial_tH=-H_{zz}\) the ordinary forward heat equation without noting the sign convention.

## Zero symmetries

For \(\xi\), always include the forced symmetry orbit

\[
\rho,\quad \bar\rho,\quad1-\rho,\quad1-\bar\rho.
\]

For the \(H_t\) variable, use the corresponding even/conjugation symmetries explicitly.

## Asymptotics and big-O

Every \(O(\cdot)\), \(o(\cdot)\), or asymptotic equivalence must state:
- the variable tending to its limit;
- all other parameters;
- whether the estimate is uniform in those parameters;
- the domain on which the estimate holds;
- whether constants are absolute or parameter-dependent.

## Equality and scaling audits

Before using a new identity in an RH implication, verify it under:
1. multiplication \(F\mapsto cF\);
2. translation/scaling when meaningful;
3. the simplest monomial/Gaussian/polynomial toy models;
4. a known real-rooted example and a known non-real-rooted example.

A factor-of-two, \(2\pi\), sign, or time-direction mismatch is a hard failure, not a cosmetic issue.
