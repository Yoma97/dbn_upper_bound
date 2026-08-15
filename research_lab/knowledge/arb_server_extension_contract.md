# Arb_Riemann_Lab Server Extension Contract

This contract defines the next rigorous endpoints required by `orchestrator_v3.py`.
It is an interface specification only; it does not claim the currently connected server already implements them.

## Common response envelope

Every endpoint should return:

```json
{
  "status": "CERTIFIED | INCONCLUSIVE | ERROR",
  "convention_id": "rh-lab-v1",
  "precision_bits": 256,
  "enclosure": "machine-readable Arb/Acb interval",
  "certificate": {
    "sign": "POSITIVE | NEGATIVE | CONTAINS_ZERO | UNKNOWN",
    "nonvanishing": true,
    "notes": ""
  }
}
```

No endpoint may convert an inconclusive ball to a floating-point guess for certification.

## Required endpoints

### `riemann_xi`
Inputs: complex `s`, `precision_bits`.
Output: rigorous Acb enclosure of `xi(s)` under the Convention Lock.

### `riemann_xi_derivative`
Inputs: complex `s`, integer `order >= 0`, `precision_bits`.
Output: rigorous enclosure of `xi^(order)(s)`.

### `H_t`
Inputs: real/complex `z`, real `t`, `precision_bits`.
Output: rigorous enclosure of canonical `H_t(z)` with
`H_0(z)=xi(1/2+i z/2)/8` and `partial_t H_t=-partial_z^2 H_t`.

### `H_t_derivative`
Inputs: `z`, `t`, integer `order >= 0`, `precision_bits`.
Output: rigorous enclosure of `partial_z^order H_t(z)`.

### `laguerre_expression`
Inputs: supported function descriptor, real `x`, integer `n >= 0`, parameters, precision.
Output: rigorous enclosure of the coefficient `L_n(x)` in
`F(x+iy)F(x-iy)=sum_n L_n(x)y^(2n)`.

### `interval_integral`
Inputs: supported integrand descriptor, interval/box domain, precision, optional tail theorem identifier.
Output: rigorous enclosure of the integral and explicit tail/truncation certificate.

### `interval_sign_on_box`
Inputs: supported expression/function descriptor, real or complex box, precision, adaptive subdivision budget.
Output: certified POSITIVE/NEGATIVE/NONZERO or INCONCLUSIVE, plus the final covering.

### `matrix_inertia`
Inputs: rigorous real-symmetric/Hermitian interval matrix.
Output: certified counts `(n_positive, n_negative, n_zero)` when separable; otherwise INCONCLUSIVE.

### `smallest_singular_value`
Inputs: rigorous interval matrix/operator discretization certificate.
Output: enclosure for the smallest singular value, with nonzero certificate when lower bound > 0.

### `interval_newton`
Inputs: supported finite-dimensional system, starting box, precision.
Output: certified unique-zero / no-zero / inconclusive result using interval Newton or Krawczyk.

## Security and proof rules

- Reject NaN/Inf and malformed precision/domain inputs.
- Apply hard resource ceilings per request.
- Return conventions and function versions in every result.
- Preserve Arb/Acb balls; do not stringify only a midpoint.
- Never label a finite computation as an RH proof.
- For unbounded claims, require the caller to provide an analytic reduction/tail theorem identifier.
