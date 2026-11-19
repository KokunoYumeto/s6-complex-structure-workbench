"""Exact boundary certificates for E.2.10--E.2.11.

This supplements the geometric proof. It does not infer a full ZG-module
from its ordinary coinvariants or claim a smooth classification.
"""
from pathlib import Path
from itertools import product
from math import gcd
from functools import reduce
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
import manifolds_shifted_mv as mv

ROOT = Path(__file__).resolve().parent


def skew(i, j):
    a = s.zeros(4)
    a[i, j] = 1
    a[j, i] = -1
    return a


radical = skew(0, 1).col_join(skew(0, 2)).nullspace()
assert radical == [s.Matrix([0, 0, 0, 1])]
source, target = mv.basis(2)
v = source.index(('f', 1, (0,), (0,)))
t1 = source.index(('m', 1, (0,), ()))
t2 = source.index(('m', 0, (), (0,)))
mixed_row = target.index((0, 1, (), (0,)))
second_g_sweep = target.index((1, 0, (), (0,)))
cases = []
for eps1, eta1, eps2, eta2 in product((1, -1), repeat=4):
    D = mv.matrix(2, eps1, eta1, (eps2, eta2))
    kernel = D.nullspace()
    assert all(k[i] == 0 for k in kernel for i in (v, t1, t2))
    witness = D.row(mixed_row) - D.row(second_g_sweep)
    expected = s.zeros(1, D.cols)
    expected[v] = 12*eps1
    assert witness == expected
    divisibility = reduce(gcd, (abs(int(x)) for x in D[:, v]), 0)
    assert divisibility == 12
    cases.append(dict(signs=[eps1, eta1, eps2, eta2],
                      kernel_rank=len(kernel),
                      retained_three_coordinates_zero=True,
                      twelve_v_image_witness=[mixed_row, second_g_sweep],
                      coefficient_gcd=divisibility))

# A primitive Ext vector can be changed to (1,0,...,0) by an
# automorphism over Z/12. This is its resulting integer presentation.
R = s.zeros(7, 8)
for i in range(7):
    R[i, i+1] = 12
R[0, 0] = -1
S = smith_normal_form(R, domain=s.ZZ)
factors = [abs(int(S[i, i])) for i in range(7)]
assert factors == [1, 12, 12, 12, 12, 12, 12]
out = dict(
    common_radical=radical[0].T.tolist()[0],
    all_cases=cases,
    pullback_H3_N_generator_order=12,
    extension_smith_factors=factors,
    pi2_coinvariants='Z^2 direct_sum (Z/12)^6',
    scope='Coinvariants and nonprojectivity; not the complete ZG-module.'
)
encoded = json.dumps(out, indent=2, default=int)+'\n'
(ROOT/'maps_shifted_pi2.out.json').write_text(encoded)
print(encoded, end='')
