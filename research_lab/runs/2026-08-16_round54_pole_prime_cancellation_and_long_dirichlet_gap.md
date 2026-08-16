# Round 54 — The `O(x)` term is pole–prime cancellation: reduction to a long Dirichlet-polynomial mean square

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED SOURCE DECOMPOSITION / CIRCULARITY GUARD / ARITHMETIC GAP / NOVELTY UNVERIFIED.

## 0. Executive verdict

Round 53 solved sparse localization on the zero side and left one question: why does the unconditional explicit-formula proof lose an `O(x)` term that dominates every off-line signal `x^{2delta}` with `delta<1/2`?

The answer is precise.

The apparent `O(x)` is the square of an `O(x^{1/2})` term arising from the pole at `s=1` **after that pole term has been separated from a prime Dirichlet polynomial of the same leading size**. The continuous main term of the prime polynomial equals the pole contribution exactly.

Thus the true long-range arithmetic object is the cancellation

\[
\boxed{
E_x(t)=P_x(t)-I_x(t),}
\]

where

\[
P_x(t)
:=\sum_{n\ge1}\frac{\Lambda(n)}{n^{1/2+it}}
\min\!\left\{\frac nx,\frac xn\right\}
\]

and

\[
\boxed{
I_x(t)
=x^{1/2-it}
\left(\frac1{3/2-it}+\frac1{1/2+it}\right).}
\]

The current short-range proof can afford to bound `I_x` separately because `x<=T`. Sparse long-range detection cannot.

However, asking for a pointwise subpower bound on `E_x(t)` would merely repackage RH-strength cancellation. The non-circular target is therefore a **long Dirichlet-polynomial mean-square theorem in the `t`-variable**, strong for `x=T^alpha` with `alpha>1`.

---

## 1. Source explicit formula

The RH-free Montgomery lemma used in the unconditional pair-correlation theorem states, schematically and with the source's precise smooth weight,

\[
\sum_\rho
\frac{2x^{\delta+i(\gamma-t)}}
{1+((t-\gamma)+i\delta)^2}
=
-P_x(t)
+x^{-1}(\log(|t|+2)+O(1))
+O\!\left(\frac{x^{1/2}}{1+t^2}\right)
+O\!\left(\frac{x^{-5/2}}{|t|+2}\right).
\]

The source obtains this from Landau's explicit formula by taking `s=sigma+it`, reflecting `sigma` to `1-sigma`, subtracting, and finally taking `sigma=3/2`.

The `x^{1/2}` term comes from the `s=1` pole contribution; it is not a zero-density term.

---

## 2. Exact pole term before absolute-value bounding

Start from the pole term in Landau's formula

\[
-\frac{x^{1-s}}{1-s}.
\]

After multiplying the `sigma` equation by `x^{sigma-1/2}`, the pole contribution is

\[
-\frac{x^{1/2-it}}{1-\sigma-it}.
\]

The reflected `1-sigma` equation contributes

\[
-\frac{x^{1/2-it}}{\sigma-it}.
\]

Subtracting reflected from original and setting `sigma=3/2` gives

\[
\begin{aligned}
I_x(t)
&=-x^{1/2-it}
\left(
\frac1{-1/2-it}
-
\frac1{3/2-it}
\right)\\
&=x^{1/2-it}
\left(
\frac1{1/2+it}
+
\frac1{3/2-it}
\right).
\end{aligned}
\]

Hence

\[
\boxed{
I_x(t)
=x^{1/2-it}
\left(
\frac1{3/2-it}
+
\frac1{1/2+it}
\right).}
\]

Its crude size is

\[
I_x(t)=O\!\left(\frac{x^{1/2}}{1+t^2}\right),
\]

which is exactly the source error channel.

---

## 3. The same term is the continuous main term of the prime polynomial

Let

\[
W(y):=\min(y,y^{-1}),
\]

so

\[
P_x(t)=\int_{1^-}^{\infty}
 u^{-1/2-it}W(u/x)\,d\psi(u),
\]

where

\[
\psi(u)=\sum_{n\le u}\Lambda(n).
\]

Replace `d psi(u)` by its continuous prime-number-theorem main term `du`:

\[
I_x^{\rm cont}(t)
:=\int_0^\infty u^{-1/2-it}W(u/x)\,du.
\]

Split at `u=x`.

For `u<=x`, `W(u/x)=u/x`, so

\[
\frac1x\int_0^x u^{1/2-it}du
=\frac{x^{1/2-it}}{3/2-it}.
\]

For `u>=x`, `W(u/x)=x/u`, so

\[
x\int_x^\infty u^{-3/2-it}du
=\frac{x^{1/2-it}}{1/2+it}.
\]

Therefore

\[
\boxed{
I_x^{\rm cont}(t)=I_x(t).}
\]

This identity is exact.

Thus the large pole term is not an independent nuisance; it is precisely the continuous main term of the prime sum.

---

## 4. The correct residual

Write

\[
R(u):=\psi(u)-u.
\]

Then

\[
\boxed{
E_x(t)
:=P_x(t)-I_x(t)
=\int_{1^-}^{\infty}
 u^{-1/2-it}W(u/x)\,dR(u),}
\]

up to the harmless lower-end convention at `u=1`.

After Stieltjes integration by parts, `E_x(t)` is a smoothed Mellin transform of the PNT error `R(u)`.

The long-range pair-correlation problem is therefore an arithmetic cancellation problem for `R(u)`, not a problem of estimating the pole term separately.

---

## 5. Why the published proof produces `O(x)`

If one bounds the pole channel only by

\[
|I_x(t)|\ll\frac{x^{1/2}}{1+t^2},
\]

then

\[
\int_0^T|I_x(t)|^2dt
\ll x.
\]

This is exactly the scale of the `O(x)` term that appears when the square-integral zero statistic is compared with the prime-side mean square.

For `x<=T`, this is harmless compared with the `T`-scale errors of Montgomery's theorem. For `x>>T`, it is fatal for sparse horizontal detection.

Thus

\[
\boxed{
O(x)\text{ is a short-range bookkeeping bound on a cancellation pair, not an intrinsic zero-side main term}.}
\]

---

## 6. Why merely subtracting `I_x` does not solve the problem

One might try to define a pole-subtracted zero sum. This does not create a small object automatically.

The exact equality says schematically

\[
\text{zero sum}
=-(P_x-I_x)+\text{smaller explicit channels}.
\]

The required cancellation has simply become `E_x=P_x-I_x`.

Moreover, for fixed `t`, a hypothetical off-line zero with displacement `delta>0` naturally generates a normalized Mellin contribution of size `x^delta`. Therefore a theorem such as

\[
E_x(t)=x^{o(1)}
\]

uniformly pointwise in fixed `t` is already of RH strength.

Such a bound cannot be adopted as a new lemma without an independent mechanism.

---

## 7. Why the `t`-average is the non-circular opportunity

The pair-correlation identity does not ask for pointwise control. It asks for an integral over a long vertical parameter range, schematically

\[
\boxed{
\int_0^T|E_x(t)+\text{small explicit terms}|^2dt.}
\]

This opens the possibility of cancellation unavailable pointwise.

When `x=T^alpha`, the prime polynomial has effective length about `x`. For `alpha<=1`, classical mean-value technology is strong enough and yields the unconditional Montgomery theorem.

For `alpha>1`, the polynomial is longer than the `t`-averaging interval. Its mean square contains substantial off-diagonal terms involving correlations of the von Mangoldt function.

Thus extending RH-free pair correlation beyond `alpha=1` is equivalent in difficulty to controlling a genuinely long prime Dirichlet polynomial, not merely refining a contour estimate.

---

## 8. Prime-correlation form of the new gap

Expanding the mean square of `P_x` gives terms of the form

\[
\sum_{m,n}
\frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
W(m/x)W(n/x)
\int_0^T e^{it\log(m/n)}dt.
\]

The time integral is

\[
\frac{e^{iT\log(m/n)}-1}{i\log(m/n)},
\]

with size

\[
\ll\min\left(T,\frac1{|\log(m/n)|}\right).
\]

When `x<=T`, only a relatively thin near-diagonal regime is dangerous. When `x=T^alpha` with `alpha>1`, many pairs with

\[
|m-n|\lesssim x/T
\]

remain coherent.

Consequently the required arithmetic input is a weighted average of shifted-prime correlations

\[
\boxed{
\sum_n\Lambda(n)\Lambda(n+h)\,\omega_{x,T}(n,h)}
\]

uniformly for shifts reaching roughly

\[
\boxed{|h|\lesssim x/T=T^{\alpha-1}.}
\]

This is the concrete prime-side meaning of the long-range pair-correlation gap.

---

## 9. Relation to extended pair-correlation work

Long-range pair-correlation conjectures are already known to have strong consequences for prime-number-theorem errors and primes in short intervals. Published work explicitly studies hypotheses of the form

\[
F(x,T)\ll T\log x
\]

uniformly in ranges far beyond `x=T`, in some formulations reaching powers or much longer ranges, and notes that such estimates are currently out of reach.

This is fully consistent with the reduction above: long-range control is measuring nontrivial cancellation in long von-Mangoldt Dirichlet polynomials.

The present project differs in purpose: we need an **RH-free horizontal-weighted** long-range theorem because Round 53 shows that its growth exponent measures the rightmost horizontal zero displacement.

---

## 10. New-tool specification: LDP-MS

### Long Dirichlet Polynomial Mean-Square theorem

Seek a theorem for

\[
E_x(t)=
\sum_n\frac{\Lambda(n)}{n^{1/2+it}}W(n/x)-I_x(t)
\]

in a range `x=T^alpha`, `alpha>1`, of the form

\[
\boxed{
\int_0^T|E_x(t)|^2dt
\le \mathfrak B(x,T)}
\]

with `B` small enough, after the exact explicit-formula reconstruction, to rule out a zero-side contribution `x^{2delta}`.

The theorem must be proved from arithmetic structure and cannot simply assume RH-equivalent pointwise PNT error.

Promising inputs would be:

- cancellation in averaged `Lambda(n)Lambda(n+h)` beyond current diagonal mean-value estimates;
- dispersion/large-sieve mechanisms adapted to the triangular Mellin weight `W`;
- bilinear decompositions of `Lambda` that exploit averaging jointly in `t` and `h`;
- a new positivity/duality argument converting known large-value estimates for Dirichlet polynomials into a long mean-square bound.

---

## 11. Program decision

- The `O(x)` barrier is **NOT a fundamental pole term**; it comes from estimating pole and prime main terms separately.
- Exact pole--prime main cancellation: **PROVED**.
- Pointwise subpower residual bound: **REJECTED as RH-strength repackaging unless independently derived**.
- Long `t`-mean-square residual: **LEGITIMATE NEW ARITHMETIC TARGET**.
- The next mathematical tool is now concrete: a long von-Mangoldt Dirichlet-polynomial mean-square / shifted-prime-correlation theorem in the regime `x>T`.

The next round should quantify exactly what shifted-prime estimate would suffice for a hypothetical off-line displacement `delta`, and compare that requirement with the strongest unconditional averaged prime-correlation technology. This will show whether LDP-MS is merely another form of Hardy--Littlewood or whether a weaker averaged theorem could already close the sparse orbit.

**No proof of RH is claimed. Novelty remains unverified.**