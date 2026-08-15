# Mathematical Invention Charter

**Purpose:** Encourage genuinely new mathematics while preserving mathematical legitimacy, proof discipline, and transfer value.

The lab is allowed to invent new definitions, objects, operators, transforms, functionals, inequalities, principles, and local theories. Novelty is not restricted to recombining named classical tools. However, an invention is not promoted merely because it is unusual or useful for RH.

## I. What counts as a mathematical invention

A candidate invention may be, for example:

- a new functional or energy;
- a new positive or indefinite pairing;
- a new operator, semigroup, transform, or deformation;
- a new determinant/discriminant/Wronskian hierarchy;
- a new moment sequence or kernel;
- a new zero-interaction statistic;
- a new notion of positivity, rigidity, stability, interlacing, or hyperbolicity;
- a new propagation principle;
- a new exact identity or differential hierarchy;
- a new class of entire functions or L-function-like objects;
- a new duality or correspondence between two established structures;
- a new compactness, extremal, variational, or no-go principle;
- a new abstract theorem that creates a reusable proof technique.

The preferred inventions are those that reveal structure rather than encode the target conclusion.

---

## II. Mathematical legitimacy tests

Every new object O must pass all relevant tests before it is treated as a serious candidate.

### 1. Well-definedness
State the domain, codomain, parameters, regularity assumptions, convergence conditions, branches, normalization, and dependence on choices. Prove independence from arbitrary representations whenever invariance is claimed.

### 2. Foundation compatibility
The construction must live inside standard accepted mathematics (ordinary set-theoretic foundations plus the stated analytic/algebraic structures) unless an explicit new axiom is proposed. A new axiom is never allowed as an RH premise merely because it makes the theorem true.

### 3. Symmetry compatibility
Check compatibility with all natural symmetries of the setting, including as relevant:

- complex conjugation;
- the zeta/xi functional equation;
- evenness of Xi/H-type functions;
- scaling and translation normalizations;
- permutation of zeros;
- adjoint/unitary symmetries for operators;
- semigroup/deformation composition laws.

A useful new object may break a symmetry intentionally, but then the breaking must be mathematically motivated and tracked.

### 4. Naturality / coordinate independence
Prefer constructions that commute with natural maps or transformations of the class being studied. Penalize formulas that depend on an arbitrary coordinate, enumeration, cutoff, basis, or normalization unless the resulting quantity is proved invariant or the dependence is essential and controlled.

### 5. Homogeneity and limiting behavior
Determine how the object behaves under scaling, asymptotic limits, degeneration, coalescing zeros, high height, small horizontal displacement, and parameter endpoints. Check that limiting cases reproduce known mathematics where they should.

### 6. Nontriviality
Reject definitions for which the desired theorem follows by definition, or for which every admissible object automatically satisfies the property with no mathematical content.

### 7. Existence and examples
Produce genuine examples and non-examples. If the class is claimed nonempty, prove nonemptiness. If an extremizer, measure, operator, or transform is introduced, prove existence under stated hypotheses.

### 8. Internal theorem ecology
A serious new structure should support multiple mathematical statements, not only one RH-shaped statement. Seek:

- closure properties;
- comparison principles;
- extremal cases;
- equality cases;
- stability/perturbation theorems;
- dual formulations;
- monotonicity or conservation laws;
- compactness or convergence results;
- classification of simple examples.

### 9. Recovery test
When specialized to familiar objects, recover known identities/theorems or explain precisely why the new theory differs. Failure to match basic known cases is a strong warning sign.

### 10. Transfer test
Try the construction on at least one mathematically independent setting: another completed L-function, a general real entire function, a polynomial class, a heat-flow family, a moment problem, a spectral model, or another natural class. Transfer does not need to solve a famous problem, but it must yield a rigorous nontrivial consequence.

---

## III. How the lab should invent rather than merely recombine

The invention agents should perform systematic structural mutations of known mathematics, but each mutation must be justified and audited.

### A. Lift
Replace a scalar quantity by a matrix, operator, kernel, measure, or bilinear form so that hidden positivity or rank structure becomes visible.

### B. Dualize
Pass between zeros and primes, function and transform, moment sequence and measure, operator and quadratic form, local defect and global test function.

### C. Deform
Introduce a continuous parameter (heat, scale, mollifier length, test-function width, polynomial degree/shift) and search for an evolution law or first-crossing obstruction.

### D. Polarize
Turn a nonlinear scalar inequality into a bilinear or sesquilinear form; search for Cauchy-Schwarz, positivity, determinant, or Hodge-index-type structure.

### E. Localize / globalize
Convert one off-line zero into a localized test, then prove a global consequence; or integrate many local constraints into one invariant.

### F. Renormalize
Choose a normalization that exposes a stable limiting object, while proving that no RH-equivalent information is inserted by the normalization.

### G. Complete
Embed an incomplete statistic into a larger space where positivity, self-adjointness, compactness, or convexity becomes structurally accessible.

### H. Factor
Seek representations such as A* A, T*JT, Gram matrices, moment matrices, transfer operators, or positive kernels. Factorizations count only if established independently of RH.

### I. Interpolate
Find an analytic or algebraic family joining a regime where a theorem is known to the target regime, and prove that the desired property cannot be lost along the path.

### J. Extract an obstruction category
Classify all possible ways a proposed theorem can fail, then seek a single invariant that vanishes or changes sign on every failure class.

These operations are search heuristics, not proofs.

---

## IV. New-theory construction protocol

For every genuinely new object or principle, produce a `THEORY CARD` containing:

1. NAME (temporary descriptive name; avoid grandiose branding)
2. MOTIVATING OBSTRUCTION
3. FORMAL DEFINITION
4. DOMAIN / CODOMAIN / PARAMETERS
5. WELL-DEFINEDNESS PROOF OBLIGATIONS
6. NATURAL SYMMETRIES AND TRANSFORMATION LAWS
7. SIMPLE EXAMPLES
8. NON-EXAMPLES / FAILURE CASES
9. FIRST EXACT IDENTITY
10. FIRST NONTRIVIAL LEMMA
11. SHARPNESS OR EQUALITY CASE
12. RELATION TO KNOWN STRUCTURES
13. WHY IT IS NOT RH ENCODED AS A DEFINITION
14. RH-RELEVANT MECHANISM
15. INDEPENDENT NON-RH APPLICATION TARGET
16. FASTEST COUNTEREXAMPLE TEST
17. CURRENT STATUS

No theory card may use the word THEOREM for an unproved claim.

---

## V. Promotion criteria for a genuinely new mathematical tool

A proposed invention can move toward `NEW_TOOL` only if all of the following are met:

1. **Definition:** precise, well-defined, noncircular.
2. **Consistency:** compatible with the stated foundational and analytic assumptions.
3. **Structure:** at least one exact structural law is proved.
4. **Nontrivial theorem:** at least one nontrivial result is proved from the new structure.
5. **Independence:** the proof does not use RH or a hidden equivalent.
6. **Adversarial survival:** counterexample, circularity, naturality, and edge-case audits pass.
7. **Abstraction:** the construction is defined on a natural class broader than xi alone, unless there is a compelling intrinsic reason for xi-specificity.
8. **Transfer:** at least one rigorous independent consequence or application exists outside the original RH step.
9. **Novelty:** literature search fails to identify it as a disguised known object/theorem; uncertainty is reported honestly.
10. **Proof reproducibility:** an independent agent can reconstruct the core theorem from the frozen definitions and dependencies.
11. **Formalization readiness:** definitions and central lemmas are stated precisely enough to be encoded in a proof assistant where feasible.

---

## VI. Anti-hallucination / anti-overfitting rules

Reject or heavily penalize an invention if:

- its definition mentions the desired conclusion in disguised form;
- it works only for the first finitely many computed zeros with no theorem controlling the tail;
- a parameter is chosen after seeing the zero configuration and no uniform selection theorem exists;
- the key sign comes from numerical experiments rather than proof;
- a claimed invariant is only approximately invariant without a controlled remainder;
- a new operator is called self-adjoint without a domain/closure proof;
- a measure is called positive without a construction proving positivity;
- a determinant is claimed positive from examples only;
- an infinite sum/product is used without convergence and rearrangement control;
- a symmetry is used inconsistently;
- a new term merely renames a known RH-equivalent criterion;
- the only application is the statement it was designed to prove.

---

## VII. Parallel research doctrine

The lab should run two complementary modes simultaneously:

### EXCLUSION MODE
Find a law all false RH configurations must violate.

### CREATION MODE
Invent new mathematical structures that make such a law, bridge, positivity mechanism, propagation theorem, or rigidity principle provable.

The preferred breakthrough has the form

    NEW STRUCTURE
        => independently proved mathematical law
        => every off-line configuration violates the law
        => RH,

while the NEW STRUCTURE remains meaningful and useful after removing RH from the paper.
