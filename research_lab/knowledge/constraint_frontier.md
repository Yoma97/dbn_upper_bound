# Constraint-First / No-Go Frontier for RH

**As of:** 2026-08-14

This frontier implements an exclusion-first research strategy:

> Do not primarily ask which zero configuration is correct. Search for a law that the genuine zeta/xi structure must satisfy, prove that law independently, and then prove that every RH-false admissible configuration violates it.

The target proof architecture is

    ESTABLISHED STRUCTURE  =>  CONSTRAINT C
    RH-FALSE CONFIGURATION =>  VIOLATION OF C
    -----------------------------------------
                         RH

The two arrows are separate research problems. A known RH-equivalent criterion supplies only the second logical shape unless its positivity/constraint can be proved independently.

---

## C1. Weil / Li positivity: the canonical exclusion template

### KNOWN
Li proved that RH is equivalent to nonnegativity of all Li coefficients. Bombieri and Lagarias showed that Li's criterion follows from general inequalities for multisets of complex numbers and related Li positivity, through the Guinand-Weil explicit formula, to Weil's positivity criterion.

Voros proved an asymptotic dichotomy: under RH the Li coefficients have tempered n(A log n+B)-type growth, while if RH is false they have non-tempered oscillatory asymptotics. This is a genuine **violation-amplification model**: an off-critical defect cannot remain asymptotically invisible in the Li observable.

### LIMITATION
The missing step is not another proof that Li/Weil positivity is equivalent to RH. The missing step is an **independent reason for positivity** that can be proved from structure already known unconditionally (or from a genuinely weaker new theorem).

### INVENTION TARGET
Construct a new representation

    Q_W(f) = ||T f||^2 + R(f)

or

    lambda_n = PositivePart_n - ControlledDefect_n

where the positive part is manifestly nonnegative and the defect is proved nonpositive/zero/smaller by established prime-side, trace, heat-flow, zero-density, or other inputs. The key requirement is that the proof of the sign not use RH-equivalent information.

### FAST REJECTION TEST
If the proposed proof of positivity uses a statement equivalent to all zeros lying on the line, all generalized Laguerre inequalities, unrestricted long-mollifier control, PCC/ES, or another endpoint criterion, reject as circular/repackaged.

---

## C2. Moment / Hankel positivity and the screw-function program

### KNOWN
Suzuki's published screw-function work gives RH-equivalent positivity conditions including nonnegativity of families of Hankel determinants built from moments, and develops a linear-system/operator viewpoint. In RH-false scenarios the framework produces degeneracy identities. This turns the zero-location problem into a positivity/definiteness problem for structured matrices/operators.

A 2026 Suzuki preprint recasts Weil's quadratic form through the screw function without assuming RH and formulates a self-adjoint operator limit conjecture. Treat the recent preprint as mechanism-level input until independently audited.

### LIMITATION
Showing that all required determinants/forms are nonnegative directly is again endpoint-equivalent. The hard missing theorem is a lower-level structural reason for total/moment positivity.

### INVENTION TARGETS
1. Find a finite-step recurrence, continued-fraction law, total-positivity mechanism, or moment representation by a **manifestly positive measure** derived unconditionally from prime-side data.
2. Prove a propagation theorem: a tractable subset of principal minors plus a structural recurrence forces all minors positive.
3. Find an operator factorization A^*A + K where K has a rigorously controlled sign from existing arithmetic input.
4. Identify a stability/variation law under a deformation (heat flow, truncation, scale parameter) that prevents the first eigenvalue/minor from crossing zero.

### EXCLUSION REQUIREMENT
The completeness auditor must show that *any* off-line zero configuration forces a failed minor/eigenvalue/sign condition, including zeros arbitrarily close to the line and sparse high zeros.

---

## C3. Function-field model: geometry constrains all eigenvalues at once

### KNOWN MODEL
For zeta functions of curves over finite fields, Weil/Bombieri proofs use geometric structure on a product of curves (intersection theory or related function-theoretic machinery) to obtain global bounds. The successful proof does not locate every zero by independent search; the geometry supplies an inequality that forces the allowed spectral size.

### LESSON, NOT A PREMISE
This is an analogy, not a bridge to the classical zeta function. It suggests searching for the classical analogue of the missing positive/intersection form rather than searching zero-by-zero.

### INVENTION TARGET
Construct an analytic, operator, trace, moment, or heat-flow pairing for classical xi with three properties:

1. it is defined and positive/definite for reasons independent of RH;
2. the explicit formula identifies its spectral contribution with the zeta zeros;
3. the positivity inequality forces Re(rho)=1/2 for every rho.

A useful candidate should have a life beyond xi, for example for a class of completed L-functions.

---

## C4. Constraint discovery by minimal false configuration

Do not start from an arbitrary large false zero set. Start from the smallest RH-false configuration allowed by the known symmetries:

    rho = beta + i gamma, beta != 1/2,

along with its forced conjugation / functional-equation partners.

Then ask systematically:

1. Which exact observables change sign or growth class?
2. Which observables are immune to cancellation by additional zeros?
3. Can a positive kernel/test function be tailored to isolate this orbit while retaining an explicit prime-side evaluation?
4. Can the defect be amplified with scale n, T, t, degree d, or a test-function parameter until it dominates every known error?
5. Can one prove that any attempted cancellation creates a different forbidden signature?

This is the **Violation Amplification Program**.

Promising observable families:

- Weil quadratic forms / optimized test functions;
- Li coefficients and generalized Li transforms;
- Hankel/moment determinants;
- horizontally weighted pair statistics;
- zero-density weighted tails;
- de Bruijn-Newman heat-flow energies / collision discriminants;
- mollified moments whose defect explicitly contains symmetric off-line pairs;
- prime-side explicit-formula quantities with manifest sign constraints.

---

## C5. Complete exclusion versus density-one exclusion

A recurring logical trap is

    bad configurations are rare  =>  no bad configuration exists.

This is false without a rigidity theorem.

The lab therefore prioritizes a **Sparse-Exception No-Hiding Theorem** of the schematic form

    one off-line zero
      => amplified defect of size A(parameter)
      => contradiction with a proven upper/sign bound.

The amplification must survive:

- arbitrarily large height;
- arbitrarily small horizontal displacement beta-1/2 != 0;
- multiplicity;
- cancellation among multiple off-line orbits;
- a zero-density exceptional set;
- all asymptotic error terms uniformly.

A theorem that only excludes a positive-density family of off-line zeros is not complete enough for RH.

---

## C6. Priority conjecture templates for invention agents

These are templates, not claims.

### Template A: Prime-side positive representation
Find a transform/test-function family f_a such that the explicit formula gives

    Q(f_a) = PrimePositive(a) - ArchimedeanControlled(a),

prove Q(f_a) >= 0 unconditionally for a complete/dense family of tests, and prove that any off-line zero produces Q(f_a)<0 for some a.

### Template B: First-crossing impossibility
Construct a continuous deformation of a positive matrix/operator/form M(t) from a regime where positivity is known. Prove that a first eigenvalue crossing through zero would force an auxiliary identity forbidden by a separate established theorem. Then positivity cannot be lost.

### Template C: Local defect -> global spectral excess
For an off-line orbit O(rho), prove a lower bound

    Defect(T or n or a) >= F(distance_from_line, height)

and prove an unconditional upper bound with smaller order. The lower bound must account for cancellation.

### Template D: Constraint basis / completeness theorem
Find a countable or finite-parameter family of constraints C_a such that:

1. each C_a is independently provable;
2. every RH-false zero configuration violates at least one C_a;
3. the completeness proof is structural, not numerical enumeration.

### Template E: New Hodge-index analogue
Invent a bilinear/hermitian pairing B(X,Y) for arithmetic/analytic correspondences associated with xi, prove a Cauchy-Schwarz/Hodge-index-type inequality for B from an independent functional-analytic or arithmetic theorem, then derive the critical-line bound from the explicit-formula/spectral interpretation.

---

## C7. Promotion rule for a genuine new mathematical tool

A constraint/no-go mechanism can be promoted toward NEW_TOOL only if:

1. the constraint is well-defined on a natural class wider than xi;
2. SOUNDNESS is proved independently of the target root-location conclusion;
3. EXCLUSION COMPLETENESS is proved for the stated class;
4. at least one non-RH theorem/application follows from the same mechanism;
5. novelty search shows it is not merely Weil/Li/Laguerre/de Branges/Suzuki under a change of variables;
6. the proof survives adversarial and, where feasible, formal verification.

The research goal is therefore not merely a new equivalent criterion. It is a **new independently provable structural law whose violation set contains every RH-false configuration**.
