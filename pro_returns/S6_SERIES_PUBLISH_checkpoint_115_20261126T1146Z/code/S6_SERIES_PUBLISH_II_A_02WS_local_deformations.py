"""Independent prereading calculations for II 02WS.

Only the statement, earlier proved inputs and the opened GCP v2 primary
source were read before writing this program.  No target proof or target
program was opened.  Second-order truncated polynomial arithmetic gives the
critical values and Hessians of three explicitly constructed deformations.
One-variable interpolation with certified degree bounds makes the checks
identities in the deformation parameter.  The sphere embedding and the
general reduction to these models are proved separately in the derivation.
"""

from fractions import Fraction as Q
from itertools import permutations, product
import hashlib
import json
from pathlib import Path


class Jet:
    def __init__(self, data):
        if not isinstance(data, dict):
            data = {(0, 0, 0): Q(data)}
        self.data = {e: Q(c) for e, c in data.items() if c and sum(e) <= 2}

    @staticmethod
    def coerce(v):
        return v if isinstance(v, Jet) else Jet(v)

    def __add__(self, other):
        other = self.coerce(other)
        out = self.data.copy()
        for e, c in other.data.items():
            out[e] = out.get(e, Q(0)) + c
        return Jet(out)

    __radd__ = __add__

    def __neg__(self):
        return Jet({e: -c for e, c in self.data.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for e, c in self.data.items():
            for f, d in other.data.items():
                g = tuple(e[i] + f[i] for i in range(3))
                if sum(g) <= 2:
                    out[g] = out.get(g, Q(0)) + c*d
        return Jet(out)

    __rmul__ = __mul__

    def coefficient(self, e):
        return self.data.get(tuple(e), Q(0))


def coordinates(center):
    return [Jet({(0, 0, 0): v, tuple(int(i == j) for i in range(3)): Q(1)})
            for j, v in enumerate(center)]


def derivatives(jet):
    gradient = [jet.coefficient([int(i == j) for i in range(3)]) for j in range(3)]
    hessian = []
    for i in range(3):
        row = []
        for j in range(3):
            e = [0, 0, 0]
            e[i] += 1
            e[j] += 1
            row.append(jet.coefficient(e) * (2 if i == j else 1))
        hessian.append(row)
    return jet.coefficient((0, 0, 0)), gradient, hessian


def determinant(matrix):
    total = Q(0)
    for p in permutations(range(3)):
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
        term = Q((-1)**inversions)
        for i in range(3):
            term *= matrix[i][p[i]]
        total += term
    return total


cases = [
    dict(name='two smooth branches with Morse contact',
         polynomial=lambda x, y, z, s: z*(z-x*x-y*y+s),
         center=lambda s: (Q(0), Q(0), -s/2),
         value=lambda s: -s*s/4,
         hessian=lambda s: [[s, 0, 0], [0, s, 0], [0, 0, 2]],
         det=lambda s: 2*s*s, degree=3,
         weights=(1, 1, 2), weighted_degree=4),
    dict(name='three pairwise transverse branches with quadratic triple contact',
         polynomial=lambda x, y, z, s: x*y*(x+y+z*z-s),
         center=lambda s: (s/3, s/3, Q(0)),
         value=lambda s: -s**3/27,
         hessian=lambda s: [[2*s/3, s/3, 0], [s/3, 2*s/3, 0], [0, 0, 2*s*s/9]],
         det=lambda s: 2*s**4/27, degree=4,
         weights=(2, 2, 1), weighted_degree=6),
    dict(name='four smooth branches in general linear position',
         polynomial=lambda x, y, z, s: x*y*z*(x+y+z-s),
         center=lambda s: (s/4, s/4, s/4),
         value=lambda s: -s**4/256,
         hessian=lambda s: [[s*s*Q(2 if i == j else 1, 16) for j in range(3)] for i in range(3)],
         det=lambda s: s**6/1024, degree=4,
         weights=(1, 1, 1), weighted_degree=4),
]
records = []
for case in cases:
    # Center coordinates are linear in s.  Substitution in a total-degree-D
    # polynomial gives degree <=D; first/second derivatives have degrees
    # <=D-1 and <=D-2, and the determinant degree is <=3(D-2).
    bound = max(case['degree'], 3*(case['degree']-2))
    values = []
    for integer in range(1, bound + 2):
        s = Q(integer)
        center = case['center'](s)
        x, y, z = coordinates(center)
        value, gradient, hessian = derivatives(case['polynomial'](x, y, z, s))
        assert gradient == [0, 0, 0]
        assert value == case['value'](s) != 0
        assert hessian == case['hessian'](s)
        det = determinant(hessian)
        assert det == case['det'](s) != 0
        values.append(dict(s=str(s), center=list(map(str, center)),
                           critical_value=str(value), determinant=str(det)))
    print(case['name'] + ':')
    print(f'  {bound+1} exact parameter values; certified degree bound {bound}; zero gradient, stated value/Hessian/determinant.')
    records.append(dict(name=case['name'], degree_bound=bound,
                        weights=case['weights'], weighted_degree=case['weighted_degree'], evaluations=values))

# Whitney normalization in the target coordinate order (x,y,z)=(uv,u,v^2).
# First derivatives are obtained from the same independently written jet
# algebra.  Its minors have separate degree bounds (1,2).
for u0, v0 in product((Q(0), Q(1)), (Q(-1), Q(0), Q(1))):
    u, v, unused = coordinates((u0, v0, Q(0)))
    rows = [derivatives(f)[1][:2] for f in (u*v, u, v*v)]
    minors = [rows[i][0]*rows[j][1]-rows[i][1]*rows[j][0]
              for i, j in ((0, 1), (0, 2), (1, 2))]
    assert minors == [-u0, 2*v0*v0, 2*v0]
print('Whitney differential: 6 grid values at separate bounds (1,2) give minors (-u,2v^2,2v), ideal (u,v), colength 1.')

# Exact monomial weights of the three central models, without expansion by a
# symbolic package.  The listed monomials are obtained by distributivity.
models = [
    ((1, 1, 2), 4, [(0, 0, 2), (2, 0, 1), (0, 2, 1)]),
    ((2, 2, 1), 6, [(2, 1, 0), (1, 2, 0), (1, 1, 2)]),
    ((1, 1, 1), 4, [(2, 1, 1), (1, 2, 1), (1, 1, 2)]),
]
for weights, degree, exponents in models:
    assert all(sum(w*e for w, e in zip(weights, exponent)) == degree for exponent in exponents)
print('All three central models have the positive weights used for the exact analytic unit-removal morphism.')

out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(dict(timing='prereading target 02WS', method='truncated second-order rational polynomial algebra and degree-bounded interpolation', cases=records, whitney_minors=['-u','2v^2','2v'], whitney_ideal='(u,v)'),indent=2)+'\n')
print('All local-deformation certificates passed.')
