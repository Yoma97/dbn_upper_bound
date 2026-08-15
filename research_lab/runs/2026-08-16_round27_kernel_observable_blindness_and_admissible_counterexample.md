# Round 27 — Collision-blind kernel observables and an admissible log-concave counterexample

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / NO-GO / SOURCE-COMPATIBLE / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 26 shows that a collision-sensitive entropy budget is locally a quantitative lower bound on the discriminant/resultant. This round asks whether the most natural Fourier-kernel quantities can provide such a bound automatically.

The answer is negative at the generic structural level.

1. Fixed-point Fourier/kernel moments, imaginary-axis values, finite Sobolev-type norms, and Jensen-type zero-count observables are **collision-blind**: they remain finite and analytic/continuous when two real roots coalesce.
2. More strongly, there exist positive even smooth super-exponentially decaying, strictly decreasing, strictly log-concave admissible kernels whose backward-heat family has an exact positive-time double real zero.

Therefore none of the following properties, alone or in any argument valid for the whole class, can supply the missing transversality theorem:

- positivity;
- evenness;
- smoothness;
- super-exponential decay;
- monotone decrease on the positive axis;
- ordinary strict log-concavity;
- boundedness/analyticity of finitely many Fourier moments or Sobolev norms.

Any successful Riemann-kernel theorem must exploit additional special structure: for example the stronger concavity of `r -> log Phi(sqrt(r))`, the theta functional identity, a higher finite sign-regular relation not already refuted, arithmetic information, or another genuinely Riemann-specific mechanism.

---

## 1. Source fence

For the actual Riemann heat family,

\[
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\]

Polymath and Rodgers--Tao record that `Phi` is super-exponentially decaying and that `H_t` is an entire even backward-heat family. Csordas records that the Riemann theta kernel is an admissible kernel, is strictly logarithmically concave, and satisfies the stronger property

\[
r\mapsto\log\Phi(\sqrt r)\quad\text{strictly concave}.
\]

Csordas also emphasizes that ordinary Laguerre positivity is not automatic from such basic kernel properties and formulates even the `L_1` inequality for the Riemann transform as an open problem.

The counterexample below is **not** the Riemann kernel. Its purpose is a no-go theorem: it determines which generic kernel properties cannot possibly be the missing ingredient.

---

## 2. Analyticity of fixed Fourier-kernel observables — PROVED

Let `Phi` be any even `C^infty` kernel satisfying, on every compact time interval `J`, domination strong enough that

\[
u^N e^{tu^2}\Phi(u)
\]

is integrable uniformly for `t in J` and every fixed integer `N>=0`.

For fixed complex `z` and integers `p,q>=0`, define

\[
M_{p,q}(t,z)
:=\int_0^\infty
u^p e^{tu^2}\Phi(u)\partial_z^q\cos(zu)\,du.
\]

Uniform domination permits differentiation in `t` and `z` to all orders. Hence

\[
\boxed{M_{p,q}(t,z)\text{ is real-analytic in real }t\text{ and entire in }z.}
\]

In particular this covers

\[
H_t(z),\ H_t'(z),\ H_t''(z),\ldots
\]

at every fixed `z`, as well as ordinary kernel moments

\[
\int_0^\infty u^N e^{tu^2}\Phi(u)\,du.
\]

A multiple zero at `(t_c,c)` simply imposes vanishing of some of these analytic quantities at the moving point `c`; it does not create a singularity in fixed-point moments themselves.

---

## 3. Imaginary-axis positivity is collision-blind — PROVED

For a positive kernel and real `y`,

\[
H_t(iy)
=\int_0^\infty e^{tu^2}\Phi(u)\cosh(yu)\,du>0.
\]

Every such value is analytic in `t` on compact intervals allowed by the decay. The same is true for finitely many `t`- or `y`-derivatives.

Thus a real collision

\[
H_{t_c}(c)=H_{t_c}'(c)=0
\]

need not leave any singular signature on the imaginary axis.

Consequently an estimate built only from finitely many positive imaginary-axis moments can bound a collision entropy only if one proves an additional nontrivial inequality linking those moments to the local discriminant. That linking inequality, not the positivity of the moments, would be the decisive theorem.

---

## 4. Plancherel/Sobolev quantities are collision-blind — PROVED

For an even sufficiently decaying kernel, Fourier/Plancherel gives, up to the fixed transform-normalization constant,

\[
\|H_t\|_{L^2(\mathbb R)}^2
\asymp
\int_0^\infty e^{2tu^2}\Phi(u)^2\,du,
\]

and more generally

\[
\|\partial_x^kH_t\|_{L^2(\mathbb R)}^2
\asymp
\int_0^\infty u^{2k}e^{2tu^2}\Phi(u)^2\,du.
\]

The right-hand sides are finite and analytic in `t` on compact ranges for a super-exponentially decaying kernel.

Hence every fixed finite Sobolev norm remains finite through a multiple-zero event.

No universal estimate of the schematic form

\[
\mathcal C_{\rm Breg}(t)
\le G\bigl(\|H_t\|_{H^s},\ldots\bigr)
\]

with `G` locally bounded can hold on a class containing a collision family, because the left side diverges logarithmically while the fixed Sobolev data remain finite.

---

## 5. Jensen/zero-count observables are collision-blind — PROVED

Let `F_t` be an analytic family of entire functions and choose a disk whose boundary contains no zero for `t` near `t_c`. Jensen's formula and the argument principle count zeros with multiplicity.

When two simple zeros inside the disk merge into one double zero, the total multiplicity is unchanged. Boundary integrals such as

\[
\frac1{2\pi}\int_0^{2\pi}
\log|F_t(Re^{i\theta})|\,d\theta
\]

remain continuous as long as the boundary stays zero-free.

Thus ordinary zero counts and fixed-circle Jensen averages detect **how many** zeros lie inside, not the pair separation that vanishes at a collision.

This is the same structural reason that Program B's raw winding became a zero-count spectral-flow observable rather than an independent pair-separation budget.

---

## 6. Explicit admissible counterexample kernel — PROVED

We now construct a broad-class counterexample.

### 6.1 A triangular factor with a prescribed double Fourier zero

For `a>0`, define the even triangular function

\[
T_a(u):=\left(1-\frac{|u|}{a}\right)_+.
\]

It is nonnegative, even, integrable, and log-concave in the extended sense. Its full Fourier transform under

\[
\widehat f(x)=\int_{\mathbb R}f(u)e^{-ixu}\,du
\]

is

\[
\boxed{
\widehat T_a(x)
=\frac{4\sin^2(ax/2)}{a x^2}.
}
\]

Hence every nonzero point

\[
x=\frac{2\pi n}{a}
\]

is a zero of exact order two of `widehat T_a`.

### 6.2 Smooth super-Gaussian regularization preserving the double zero

Set

\[
G(u):=e^{-u^4}.
\]

Then `G` is positive, even, `C^infty`, strictly log-concave, and has super-Gaussian decay. Its Fourier transform is continuous with

\[
\widehat G(0)=\int_{\mathbb R}e^{-u^4}\,du>0.
\]

Therefore choose `x_0>0` sufficiently small that

\[
\widehat G(x_0)>0,
\]

and set

\[
a:=\frac{2\pi}{x_0}.
\]

Define

\[
K:=T_a*G.
\]

Then

\[
\widehat K=\widehat T_a\,\widehat G.
\]

At `x=x_0`, `widehat T_a` has an exact double zero and `widehat G(x_0)` is nonzero. Hence

\[
\boxed{
\widehat K(x_0)=\widehat K'(x_0)=0,
\qquad
\widehat K''(x_0)\ne0.
}
\]

Because `K` is even,

\[
\int_0^\infty K(u)\cos(xu)\,du
=\frac12\widehat K(x),
\]

so its cosine transform has an exact double real zero at `x_0`.

---

## 7. The counterexample is an admissible log-concave kernel — PROVED

### Positivity and evenness

Both factors are nonnegative and nonzero, while `G>0` everywhere. Thus

\[
K(u)>0\quad\text{for every }u\in\mathbb R,
\]

and `K` is even.

### Smoothness and super-exponential decay

Since `T_a` is compactly supported and `G` is entire smooth,

\[
K(u)=\int_{-a}^aT_a(v)e^{-(u-v)^4}\,dv
\]

is `C^infty` (indeed real analytic on the real axis). Every derivative is bounded by a polynomial times

\[
e^{-(|u|-a)^4},
\]

and therefore for every fixed derivative order there exist `c,C>0` such that

\[
|K^{(n)}(u)|\le C e^{-c|u|^4}
\]

for sufficiently large `|u|`.

### Log-concavity

`T_a` and `G` are log-concave. By the Prékopa convolution theorem, their convolution `K` is log-concave.

### Strict decrease on `(0,infinity)`

An even positive log-concave function has a nonincreasing logarithmic derivative on `(0,infinity)` and attains its maximum at zero. Hence `K'(u)<=0` for `u>0`.

If `K'(u_0)=0` for some `u_0>0`, concavity of `log K` together with `(log K)'(0)=0` forces `(log K)'=0` throughout `[0,u_0]`, making `K` constant on an interval. Real analyticity would then force `K` to be constant everywhere, contradicting decay. Therefore

\[
\boxed{K'(u)<0\qquad(u>0).}
\]

Thus `K` satisfies the standard admissible-kernel features: positive, even, smooth, strictly decreasing, and faster than `exp(-|u|^{2+epsilon})` for some `epsilon>0`.

---

## 8. Move the double zero to any positive heat time — PROVED

Fix an arbitrary target time

\[
t_c>0
\]

and define the base kernel

\[
\boxed{
\Phi_*(u):=e^{-t_cu^2}K(u).
}
\]

Then `Phi_*` is positive, even, smooth and super-exponentially decaying. Moreover

\[
\log\Phi_*(u)=\log K(u)-t_cu^2.
\]

Because `log K` is concave and `-t_cu^2` is strictly concave,

\[
\boxed{\Phi_*\text{ is strictly log-concave}.}
\]

It is also strictly decreasing on `(0,infinity)`.

Define its backward-heat family

\[
H_t^*(x)
:=\int_0^\infty e^{tu^2}\Phi_*(u)\cos(xu)\,du.
\]

At `t=t_c`,

\[
H_{t_c}^*(x)
=\int_0^\infty K(u)\cos(xu)\,du
=\frac12\widehat K(x).
\]

Hence

\[
\boxed{
H_{t_c}^*(x_0)=0,
\qquad
\partial_xH_{t_c}^*(x_0)=0,
\qquad
\partial_x^2H_{t_c}^*(x_0)\ne0.
}
\]

This is an exact generic double collision at an arbitrarily prescribed **positive** heat time.

---

## 9. No-go consequence

The counterexample proves:

### Theorem 27.1

There is no collision-exclusion theorem valid for all backward-heat Fourier families that uses only the following hypotheses on the base kernel:

1. positive;
2. even;
3. `C^infty`;
4. super-exponentially decaying;
5. strictly decreasing on `(0,infinity)`;
6. strictly log-concave.

Indeed the family constructed in Sections 6--8 satisfies all six and nevertheless has a positive-time double zero.

Therefore these properties cannot, by themselves, imply a finite entropy budget, a positive local resultant, or `L_1>0` at every positive time.

---

## 10. What remains genuinely Riemann-specific

The actual Riemann kernel possesses additional structure not used in the counterexample, notably:

- the explicit theta-series formula;
- the theta/Poisson functional symmetry;
- the stronger established concavity
  \[
  r\mapsto\log\Phi(\sqrt r);
  \]
- the special monotone ratio
  \[
  q(u)=-\frac{\Phi'(u)}{u\Phi(u)};
  \]
- the exact relation of `Phi` to the Riemann `xi` function;
- unconditional positive-time Polymath asymptotics.

Round 15 already showed that the consequences of the stronger `r`-log-concavity at the TP2/log-concavity level are still insufficient abstractly to exclude the two oscillatory cancellations required at a collision.

Thus a successful kernel proof must use structure beyond **ordinary admissibility + ordinary log-concavity**, and beyond the already-refuted TP2-level consequence of the stronger Riemann concavity.

---

## 11. Consequence for normalized transversality

Polymath's explicit nowhere-zero normalization can remove the exponentially small amplitude of `H_t` at high `x`, but multiplication by a nonvanishing normalizer cannot remove a common zero of `H_t,H_t'` without derivative correction.

Thus any normalized lower bound of the schematic form

\[
|\widetilde H_t(x)|+|\widetilde D_t(x)|\ge c(t,x)>0
\]

that genuinely excludes a common zero is itself a transversality theorem. Generic kernel norms and moments cannot furnish it automatically.

The remaining viable question is therefore not “can positivity/log-concavity bound the entropy?” but:

> Which **additional exact identity specific to the Riemann theta kernel** forces the local resultant not to vanish?

---

## 12. Next target

The next round should attack the strongest surviving special structure from Rounds 13--15 rather than generic kernel regularity.

At a collision,

\[
H_t(x)=H_t'(x)=0
\]

is equivalent to simultaneous vanishing of

\[
S_0(t,x)
=\int_0^\infty u e^{tu^2}\Phi(u)\sin(xu)\,du
\]

and

\[
S_1(t,x)
=\int_0^\infty q(u)u e^{tu^2}\Phi(u)\sin(xu)\,du,
\]

with `q` strictly increasing and tied differentially to the same Riemann kernel.

Round 15 refuted arguments using only log-concavity of half-wave masses plus monotone likelihood ratio. The next admissible test is whether the **differential coupling between `q` and the weight** supplies a stronger finite identity not present in the abstract Round-15 counterexample.

That coupling is

\[
\boxed{
\frac{w_t'(u)}{w_t(u)}
=\frac1u+u(2t-q(u)),
\qquad
w_t(u)=u e^{tu^2}\Phi(u).
}
\]

This is the smallest currently unexploited Riemann-kernel structure on the collision side.

---

## 13. Status

- analyticity of fixed kernel moments/evaluations: **PROVED**;
- imaginary-axis collision blindness: **PROVED**;
- fixed Sobolev/Fourier norm collision blindness: **PROVED**;
- Jensen/zero-count collision blindness: **PROVED**;
- explicit positive even smooth super-exponential log-concave kernel with a double Fourier zero: **PROVED**;
- placement of that collision at arbitrary `t_c>0`: **PROVED**;
- generic admissibility + ordinary strict log-concavity implies no collision: **REFUTED**;
- stronger Riemann-specific differential/oscillatory mechanism: **OPEN / NEXT**;
- RH: **OPEN**;
- novelty of the construction/packaging: **UNVERIFIED**.
