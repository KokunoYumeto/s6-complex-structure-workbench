#!/usr/bin/env python3
"""Exact algebra behind the binary-product sphere and its boundary transport.

This is a universal polynomial calculation over Z, not a parameter sweep.
The geometric existence and compactness arguments are in the derivation/review.
No external packages or local file dependencies are used.
"""
from itertools import permutations
import json


N = 10
ZERO_EXPONENT = (0,) * N


def constant(n):
    return {} if n == 0 else {ZERO_EXPONENT: n}


def variable(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): 1}


def add(*polynomials):
    out = {}
    for p in polynomials:
        for e, c in p.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def scale(p, n):
    return {e: n * c for e, c in p.items() if n * c}


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, b in q.items():
            ef = tuple(ej + fj for ej, fj in zip(e, f))
            out[ef] = out.get(ef, 0) + c * b
    return {e: c for e, c in out.items() if c}


def product(xs):
    out = constant(1)
    for x in xs:
        out = mul(out, x)
    return out


def permutation_sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p))
                      for j in range(i + 1, len(p)))


def determinant(a):
    n = len(a)
    return add(*(scale(product(a[i][p[i]] for i in range(n)),
                       permutation_sign(p))
                 for p in permutations(range(n))))


def transpose(a):
    return list(map(list, zip(*a)))


def matrix_product(a, b):
    return [[add(*(mul(x, y) for x, y in zip(row, col)))
             for col in transpose(b)] for row in a]


def equal(a, b):
    assert a == b, (a, b)


z, o = constant(0), constant(1)
a, b, c, d, e, f, g, h, i, j = [variable(k) for k in range(N)]

# Endpoint disks z=bar(y) and z=(a+ib)bar(y), oriented by y.
# Columns are their four real tangent vectors in (Re y,Im y,Re z,Im z).
endpoint_matrix = [
    [o, z, o, z],
    [z, o, z, o],
    [o, z, a, b],
    [z, scale(o, -1), b, scale(a, -1)],
]
endpoint_det = determinant(endpoint_matrix)
negative_squared_distance = scale(add(mul(sub(a, o), sub(a, o)),
                                     mul(b, b)), -1)
equal(endpoint_det, negative_squared_distance)

# For distinct unit phases this determinant is strictly negative.
# Both endpoint tangent orientations reverse together at the other endpoint.
reversed_endpoint_matrix = [row[:] for row in endpoint_matrix]
for row in reversed_endpoint_matrix:
    row[0] = scale(row[0], -1)
    row[2] = scale(row[2], -1)
equal(determinant(reversed_endpoint_matrix), endpoint_det)

# Independently, J:TL -> NL reverses the normal orientation in a surface.
# (e1,e2,Je1,Je2) versus (e1,Je1,e2,Je2).
normal_orientation_sign = permutation_sign([0, 2, 1, 3])
assert normal_orientation_sign == -1
sphere_square = normal_orientation_sign * 2
assert sphere_square == -2

# Pullback of the Kahler form on the cylinder: let a=r*r', b=phi'.
# In basis (ds,dtheta), y contributes a ds^dtheta and z contributes
# a ds^(b ds-dtheta), giving zero as an exact exterior identity.
ds, dtheta = [o, z], [z, o]
z_angle = [b, scale(o, -1)]
wedge = lambda u, v: sub(mul(u[0], v[1]), mul(u[1], v[0]))
equal(add(mul(a, wedge(ds, dtheta)), mul(a, wedge(ds, z_angle))), z)

# d and i here are independent formal symbols, so the weight identity holds
# for every integer d and every exponent 0 <= i <= d.
degree, index, multiplicity = a, b, c
weighted_exponent = add(scale(sub(degree, index), 2), index, index)
equal(weighted_exponent, scale(degree, 2))
equal(mul(weighted_exponent, multiplicity),
      scale(mul(degree, multiplicity), 2))

# Exact change of generators of (x-bi*w, x-bj*w) to (x,w), with
# invertible denominator bj-bi. Both inverse identities are checked.
bi, bj, x, w = a, b, c, d
gi, gj = sub(x, mul(bi, w)), sub(x, mul(bj, w))
delta = sub(bj, bi)
equal(sub(gi, gj), mul(delta, w))
equal(sub(mul(bj, gi), mul(bi, gj)), mul(delta, x))
equal(sub(mul(delta, x), mul(bi, mul(delta, w))), mul(delta, gi))
equal(sub(mul(delta, x), mul(bj, mul(delta, w))), mul(delta, gj))

# A complex linear normal differential with coefficients a+ib,c+id
# is a real 2x4 matrix. Its two singular values both equal the complex
# gradient norm: A A^t=(a^2+b^2+c^2+d^2)I_2.
normal = [[a, scale(b, -1), c, scale(d, -1)], [b, a, d, c]]
norm_squared = add(*(mul(q, q) for q in [a, b, c, d]))
equal(matrix_product(normal, transpose(normal)),
      [[norm_squared, z], [z, norm_squared]])

# For an arbitrary surjective real boundary derivative B:R^5 -> R^2,
# the right inverse is B^t (B B^t)^(-1). Verify it symbolically after
# clearing its positive Gram determinant. The corresponding interior
# right-inverse formula follows by the same matrix identity in dimension six.
boundary = [[a, b, c, d, e], [f, g, h, i, j]]
gram = matrix_product(boundary, transpose(boundary))
gram_adjugate = [[gram[1][1], scale(gram[0][1], -1)],
                [scale(gram[1][0], -1), gram[0][0]]]
gram_det = determinant(gram)
right_inverse_numerator = matrix_product(transpose(boundary), gram_adjugate)
equal(matrix_product(boundary, right_inverse_numerator),
      [[gram_det, z], [z, gram_det]])

result = {
    "method": "universal sparse polynomial arithmetic over Z, determinant expansion, exterior products",
    "finite_parameter_sweep": False,
    "endpoint_intersection_determinant": "-((a-1)^2+b^2)",
    "endpoint_intersection_sign_for_distinct_phases": -1,
    "simultaneous_endpoint_orientation_reversal_preserves_sign": True,
    "J_normal_orientation_sign": normal_orientation_sign,
    "sphere_square_by_Euler_number": sphere_square,
    "cylinder_Kahler_pullback": "0",
    "weighted_exponents": ["2(d-i)+i+i=2d", "m[2(d-i)+i+i]=2dm"],
    "generator_change_and_inverse": "verified after clearing the unit bj-bi",
    "complex_normal_Gram_matrix": "(a^2+b^2+c^2+d^2)I_2",
    "boundary_right_inverse": "B[B^t adj(BB^t)]=det(BB^t)I_2 for universal real 2x5 B",
    "all_assertions_passed": True,
}
print(json.dumps(result, indent=2, sort_keys=True))
