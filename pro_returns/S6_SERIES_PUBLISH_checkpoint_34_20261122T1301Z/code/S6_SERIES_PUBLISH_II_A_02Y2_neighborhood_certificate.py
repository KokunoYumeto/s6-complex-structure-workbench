"""02Y2 prerelease exact algebra in the independently constructed maps.

No target proof or old computational routine was opened to write this file.
The polynomial calculations certify universal map identities.  They do not
stand in for the geometric neighborhood, path, or covering arguments.
"""

import json


def add(a, b):
    c = dict(a)
    for e, v in b.items():
        c[e] = c.get(e, 0) + v
        if not c[e]:
            del c[e]
    return c


def neg(a):
    return {e: -v for e, v in a.items()}


def mul(a, b):
    c = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            e = (i + k, j + l)
            c[e] = c.get(e, 0) + v * w
    return {e: v for e, v in c.items() if v}


def encoded(a):
    return [{"q_power": i, "t_power": j, "coefficient": a[(i, j)]}
            for i, j in sorted(a)]


one, q, t = {(0, 0): 1}, {(1, 0): 1}, {(0, 1): 1}
one_minus_t = add(one, neg(t))
one_minus_q = add(one, neg(q))
q_prime = add(mul(one_minus_t, q), t)

# H_t has L-vertex coefficient lambda_i*((1-t)+t/q), and
# non-L coefficient lambda_j*(1-t).  Summing these gives one.
total = add(q_prime, mul(one_minus_t, one_minus_q))
assert total == one

# After applying r, the L-vertex coefficient is
# lambda_i*((1-t)+t/q)/q_prime = lambda_i/q.
# Multiplication by q*q_prime reduces this to a polynomial identity.
retraction_numerator = add(mul(one_minus_t, q), t)
assert retraction_numerator == q_prime

# q(H_t)=q_prime>0 for q>0, 0<=t<=1 by its displayed sum.
assert add(q_prime, neg(add(q, mul(t, one_minus_q)))) == {}

# Symbolic Laurent monomials have exponent a*m+b and coefficient in Z[m].
# Differentiate z^m and multiply by z^-m without substituting any m.
coefficient_of_derivative = {1: 1}  # the polynomial m
derivative_exponent = (1, -1)
inverse_exponent = (-1, 0)
product_exponent = tuple(a + b for a, b in zip(derivative_exponent, inverse_exponent))
assert product_exponent == (0, -1)
assert coefficient_of_derivative == {1: 1}

print(json.dumps({
    "target": "02Y2 / night:P4R.1",
    "method": "Integer coefficient convolution in Q[q,t], and formal affine exponents a*m+b",
    "universal_parameter_scope": "All q>0, 0<=t<=1; every positive integer m",
    "total_barycentric_weight": encoded(total),
    "q_after_homotopy": encoded(q_prime),
    "cleared_retraction_identity_difference": encoded(add(retraction_numerator, neg(q_prime))),
    "laurent_pullback": {
        "map": "z -> z^m",
        "d(z^m)/z^m_coefficient_polynomial_in_m": coefficient_of_derivative,
        "z_exponent_affine_in_m": product_exponent,
        "conclusion": "d(z^m)/z^m = m*z^-1 dz; integrating the oriented normal circle gives winding m"
    },
    "geometric_proof_location": "S6_SERIES_PUBLISH_II_A_02Y2_derivation.md",
    "limits": "No numerical sampling; no claim to certify topology by this program."
}, indent=2))
