"""Postrelease alternative discriminant and exact cusp-basis transport.

This file was written after reading the isolated old E14 routine.  It adds
no independent event.  The critical-root norm calculation replaces the
old symbolic discriminant call and the prereading universal cubic formula.
"""
from fractions import Fraction as F
import json


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: v*c for k, v in a.items() if v*c}


def multiply(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            p = (i+k, j+l)
            out[p] = out.get(p, F(0)) + x*y
    return {k: v for k, v in out.items() if v}


# Exponents are (T,epsilon).  No discriminant, resultant or root solver.
t = {(1, 0): F(1)}
e = {(0, 1): F(1)}
one = {(0, 0): F(1)}
t2 = multiply(t, t)
t3 = multiply(t2, t)
t4 = multiply(t3, t)
d = add(scale(t3, 4), scale(multiply(add(t, e), add(t, e)), 27))
dp = add(scale(t2, 12), scale(add(t, e), 54))
critical_value = scale(add(t4, scale(t3, 3)), F(4, 3))
quotient = scale(add(add(t, e), scale(t2, F(-2, 9))), F(1, 2))
assert add(d, scale(critical_value, -1)) == multiply(dp, quotient)

# D'=12(T-r1)(T-r2), r1+r2=-9/2 and r1*r2=(9/2)epsilon.
# The exact remainder above gives D(r)=(4/3)r^3(r+3).
root_product = scale(e, F(9, 2))
shifted_root_product = add(root_product, scale(one, F(-9, 2)))
critical_norm = scale(
    multiply(multiply(multiply(root_product, root_product), root_product),
             shifted_root_product), F(16, 9))
assert critical_norm == {(0, 4): F(729), (0, 3): F(-729)}
# Res(D,D')=12^3 D(r1)D(r2), disc(D)=-Res(D,D')/4.
discriminant = scale(critical_norm, F(-12**3, 4))
assert discriminant == {(0, 3): F(314928), (0, 4): F(-314928)}
assert {i: v for (i, j), v in d.items() if j == 0} == {3: F(4), 2: F(27)}

# Gaussian rationals encode the actual invertible changes between the
# two displayed complex-linear jet-map models, with a common target frame.
def gadd(a, b):
    return (a[0]+b[0], a[1]+b[1])


def gmul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def mm(a, b):
    return [[gadd(gmul(a[i][0], b[0][j]), gmul(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


z, u, i = (F(0), F(0)), (F(1), F(0)), (F(0), F(1))
own = [[u, z], [z, (F(0), F(2))]]
printed = [[u, (F(0), F(-1))], [z, i]]
change = [[u, (F(0), F(-1))], [z, (F(1, 2), F(0))]]
inverse = [[u, (F(0), F(2))], [z, (F(2), F(0))]]
assert mm(own, change) == printed
assert mm(change, inverse) == mm(inverse, change) == [[u, z], [z, u]]

print(json.dumps({
    "timing": "postrelease, after the exact old E14 slice was read and run",
    "critical_value_identity_verified": True,
    "critical_norm": {f"T^{a} eps^{b}": str(v) for (a, b), v in critical_norm.items()},
    "discriminant": {f"T^{a} eps^{b}": str(v) for (a, b), v in discriminant.items()},
    "central_collision": "T^2(4T+27)",
    "jet_model_change": "[[1,-i],[0,1/2]]",
    "jet_model_inverse": "[[1,2i],[0,2]]",
    "both_inverse_compositions_checked": True,
    "scope": "Finite exact identities only. The separate comparison specifies the source and target frame maps; this matrix test alone does not identify geometric frames.",
    "new_independent_events": 0
}, indent=2))
