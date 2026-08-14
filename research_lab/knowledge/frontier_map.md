# Riemann Hypothesis Frontier Map

**As of:** 2026-08-14

This file is the research baseline for the invention lab. It contains no private/project progress. It records only externally established or explicitly tagged provisional results.

## Global status

RH remains unsolved. The Clay Mathematics Institute still lists it as an unsolved Millennium Prize Problem.

A computational verification, however rigorous and high, is not a proof of RH.

---

## F1. Critical-line proportion via Levinson–Conrey mollification

### KNOWN
Pratt–Robles–Zaharescu–Zeindler proved unconditionally that slightly more than 5/12 (about 41.7%) of the nontrivial zeros lie on the critical line. The 2026 Goldston–Suriajaya exposition records about 40.7% as both simple and critical.

Reference: arXiv:1802.10521; Res. Math. Sci. 7 (2020).

Conrey–Farmer–Kwan–Lin–Turnage-Butterbaugh (arXiv:2508.11108) introduced a variational optimization of linear combinations of derivatives in Levinson's method. Their result shows that optimizing the derivative combination can yield a positive critical-line proportion even for arbitrarily short mollifiers.

### LIMITATION
A positive or improved proportion is not RH. The arithmetic input controlling mollified moments, especially as mollifier length grows, remains the hard part.

Bettin–Gonek proved that the theta=infinity mollifier conjecture implies RH (arXiv:1604.02740). Therefore simply assuming arbitrary-length mollifier control risks repackaging a condition already strong enough to imply RH.

### MISSING-THEOREM TARGETS
1. Find a new structural moment theorem that extends mollifier length/control without assuming a theta=infinity-strength statement.
2. Jointly optimize derivative combinations and mollifiers under arithmetic estimates that are actually provable.
3. Identify a strictly weaker, provable subclass of long-mollifier estimates that forces all off-line zeros to disappear, rather than merely raising a proportion.

### EQUIVALENCE RISK
HIGH for any target that simply asks for theta=infinity or an unrestricted mollified second-moment bound.

---

## F2. Pair correlation and horizontal multiplicity

### KNOWN
Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh obtained an unconditional form of Montgomery's pair-correlation theorem (arXiv:2306.04799).

Goldston–Suriajaya's 2026 exposition isolates a precise RH-free horizontal-multiplicity quantity. If

    sum_{rho,rho': 0<gamma,gamma'<=T, gamma=gamma'} 1
      <= (C+o(1)) (T/(2*pi)) log T,

with 1 <= C < 2, then asymptotically at least 2-C of the zeros are simple and at least 2-C are on the critical line; if C<3/2, at least 3-2C are both simple and critical.

Reference: arXiv:2511.20059, Theorem 2.

Under the narrow-box hypothesis

    |beta-1/2| < b/(2 log T),  T < gamma <= 2T,

with b=0.3185, pair-correlation methods give at least 2/3 simple, at least 2/3 critical, and at least 1/3 both simple and critical.

Reference: arXiv:2501.14545 and arXiv:2511.20059.

Goldston–Lee–Schettler–Suriajaya prove that the Pair Correlation Conjecture, without assuming RH, implies asymptotically 100% of zeros are simple and on the critical line (arXiv:2503.15449). Their mechanism passes through an Essential Simplicity (ES) near-pair count.

### LIMITATION
"Asymptotically 100% on the critical line" still does not logically imply RH: a zero-density exceptional set of off-line zeros could remain.

The unconditional Montgomery-type theorem currently does not provide the C=1 horizontal-multiplicity conclusion needed for density-one critical zeros, nor does it eliminate a sparse exceptional set.

### MISSING-THEOREM TARGETS
1. Prove an unconditional horizontal-multiplicity bound with C<2; stretch target C=1.
2. Replace the all-zeros narrow-box hypothesis by a weighted tail/density condition that can plausibly be proved.
3. Invent a **Sparse-Exception Amplification/Rigidity Theorem**: prove that even one (or a sufficiently sparse family of) off-critical zero(s) forces a quantitatively detectable excess in horizontal/near-pair statistics, a zero-density statistic, or another established observable.
4. Find a new pair statistic that sees horizontal displacement beta-1/2 directly while retaining an unconditional explicit-formula evaluation.

### EQUIVALENCE RISK
MEDIUM. PCC itself is conjectural and very strong. A useful new theorem must not merely assume PCC or ES; it should derive a weaker decisive consequence from established inputs or create a bridge to another frontier.

---

## F3. Zero-density and Dirichlet-polynomial large values

### KNOWN
Guth–Maynard proved

    N(sigma,T) <= T^{30(1-sigma)/13 + o(1)}

using new large-value estimates for Dirichlet polynomials.

Reference: arXiv:2405.20552 (current revision 2026).

### LIMITATION
This exponent becomes power-saving relative to the total zero scale only for sigma > 17/30 approximately 0.5667. Thus, by itself, it does not localize all zeros into the O(1/log T) neighborhood of 1/2 used by the narrow-box pair-correlation theorem. This is an elementary inference from the exponent, not a statement of Guth–Maynard.

Recent explicit zero-free regions near sigma=1 (e.g. Bellotti–Trudgian–Yang, arXiv:2603.21490) are important for prime-number applications but are not horizontal localization near sigma=1/2.

### MISSING-THEOREM TARGETS
1. Convert zero-density tail information into a horizontal-multiplicity/near-pair bound rather than trying to prove an all-zeros narrow box.
2. Invent a weighted pair-correlation identity where off-line zeros are penalized by their horizontal displacement and the error is controllable by current large-value estimates.
3. Find a bootstrapping mechanism: a modest improvement in horizontal concentration strengthens pair correlation, which then feeds back to stronger concentration.

### EQUIVALENCE RISK
LOW-to-MEDIUM if the theorem genuinely starts from current zero-density estimates; HIGH if it simply assumes an O(1/log T) localization for every zero.

---

## F4. de Bruijn–Newman heat flow

### KNOWN
For

    H_t(z) = integral_0^infinity exp(t u^2) Phi(u) cos(zu) du,

there is a constant Lambda such that H_t has only real zeros iff t >= Lambda. RH is equivalent to Lambda <= 0.

Rodgers–Tao proved Lambda >= 0 (arXiv:1801.05914; Forum Math. Pi).

D.H.J. Polymath proved Lambda <= 0.22 using effective heat-flow estimates, a barrier argument, and rigorous numerical verification (arXiv:1904.12438). The Tao optimization/ExpDB record incorporates the later Platt–Trudgian zero verification and lists the established bound Lambda <= 0.2.

Platt–Trudgian rigorously verified RH up to 3*10^12 (arXiv:2004.09765; Bull. LMS 2021).

### LIMITATION
The Polymath barrier mechanism uses finite-height RH verification plus an asymptotic barrier. It produces a positive upper bound on Lambda; driving that strategy to 0 by computation alone would require unbounded verification and is not an analytic proof of RH.

Since Rodgers–Tao gives Lambda >= 0, proving RH in this framework requires a structural argument establishing Lambda <= 0, equivalently real-rootedness for H_t for every t>0 (with endpoint closure at t=0).

### MISSING-THEOREM TARGETS
1. Invent a global monotonicity, invariant, convexity, positivity, or non-collision principle that proves H_t is in the Laguerre–Polya class for every t>0 without finite-height RH input.
2. Find a theorem that propagates real-rootedness downward in t under extra structure specific to the Riemann kernel Phi, overcoming the fact that ordinary de Bruijn monotonicity only propagates in the easier direction (toward larger t).
3. Connect heat-flow zero dynamics to a proven statistic (pair correlation, zero density, or prime-side positivity) so that an off-real zero at t>0 forces a contradiction with an established theorem.

### EQUIVALENCE RISK
HIGH if the proposed invariant is just a disguised characterization of Laguerre–Polya membership. Prefer a quantity with an independently provable evolution law and applications to other heat-evolved entire functions.

### PROVISIONAL RECORDS
The Tao optimization constants page currently lists June-2026 certificate packages claiming Lambda <= 0.1965 and Lambda <= 0.1875. These are not to be treated by the lab as Tier-A mathematical theorems until provenance, proof, and certificates are independently audited. They may be mined as computational methodology only.

---

## F5. Jensen polynomials / Laguerre–Polya theory

### KNOWN
RH is equivalent to hyperbolicity of all Jensen polynomials associated with the xi Taylor coefficients.

Griffin–Ono–Rolen–Zagier proved that for every fixed degree d, all sufficiently large shifts n are hyperbolic, and proved all n for d<=8. Their normalized Jensen polynomials converge to Hermite polynomials in the fixed-degree/large-shift regime.

Reference: PNAS 2019; arXiv version of "Jensen polynomials for the Riemann zeta function and other sequences".

A very recent preprint by Jonathan Holland (arXiv:2608.08682, submitted 2026-08-09) claims/proves in the preprint a joint wedge

    n^3 log^2(n+2) >= K d^5  =>  J^{d,n} hyperbolic.

Because this preprint is only days old, the lab must tag it PROVISIONAL until independently checked.

### LIMITATION
RH includes the difficult low-shift/high-degree region, in particular n=0 for unbounded d. Fixed-d large-n asymptotics and the new joint wedge do not cover that frontier.

The full family of generalized Laguerre inequalities characterizes Laguerre–Polya membership; simply asking to prove all of them is therefore essentially an equivalent reformulation, not a new route.

### MISSING-THEOREM TARGETS
1. Invent a nontrivial propagation theorem from a structured finite/mesoscopic set of inequalities or coefficient constraints to full hyperbolicity for this kernel class.
2. Find a degree-shift renormalization or finite-free convolution mechanism that genuinely reaches low n/high d rather than only enlarging the large-n wedge.
3. Extract techniques from the 2026 wedge (after independent verification) that can be abstracted to a new hyperbolicity-preserver theorem.

### EQUIVALENCE RISK
VERY HIGH if the target simply asks for hyperbolicity of J^{d,0} for all d or all generalized Laguerre inequalities. The invention must be a provable propagation mechanism with independent content.

---

## F6. Cross-frontier bridge program (highest invention priority)

The lab should preferentially invent results that connect two established partial theories. Examples:

1. **Horizontal multiplicity <-> zero-density:** turn Guth–Maynard-type horizontal tail control into C<2 or an ES-type statistic.
2. **Pair correlation <-> heat flow:** show that a non-real H_t zero or collision produces a forbidden near-pair/horizontal-multiplicity signature at t=0.
3. **Mollification <-> horizontal multiplicity:** construct a mollified moment whose defect term counts off-line symmetric pairs at equal ordinate.
4. **Laguerre positivity <-> heat dynamics:** find a finite/evolving positivity quantity whose PDE evolution propagates enough of the Laguerre–Polya structure toward t=0.
5. **Sparse-exception rigidity:** prove that a single off-line zero cannot remain asymptotically invisible to every known global statistic.

The program should reward a rigorously proved bridge lemma more than a new RH-equivalent criterion.

---

## Priority order for invention rounds

**P0:** Cross-frontier bridge / sparse-exception amplification.

**P1:** Unconditional horizontal-multiplicity improvement and weighted horizontal pair statistics.

**P2:** Structural de Bruijn–Newman endpoint mechanism independent of finite-height verification.

**P3:** Long-mollifier / variational Levinson mechanisms that add genuinely new arithmetic control.

**P4:** Jensen/Laguerre propagation into low-shift/high-degree territory.

Pure constant optimization and larger finite zero verification are useful verification work but are not invention priorities for an RH proof.
