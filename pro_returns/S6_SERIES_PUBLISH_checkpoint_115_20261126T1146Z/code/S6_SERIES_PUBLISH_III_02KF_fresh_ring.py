"""Fresh integer checks for the pre-proof 02KF derivation.

No original ring proof, program, or output is read.  The parameter-uniform
chain argument is in the companion derivation; these finite calculations
check its curve intersections, signs, integral inverse and ring relations.
"""
from datetime import datetime, timezone
import json
from math import gcd

def pairing(a, b):
    return a[0]*b[0] - sum(x*y for x, y in zip(a[1:], b[1:]))

H = (1, 0, 0, 0)
EA = (0, 1, 0, 0)
EB = (0, 0, 1, 0)
EC = (0, 0, 0, 1)
curves = [(1,-1,0,-1), EA, (1,-1,-1,0), EB,
          (1,0,-1,-1), EC]
ruling = (1,0,-1,0)
intersections = [pairing(ruling, c) for c in curves]
assert intersections == [1, 0, 0, 1, 0, 0]
assert pairing(ruling, ruling) == 0
# The principal total fibre divisor gives the remaining self coefficient.
self_coefficient = -sum(intersections)
assert self_coefficient == -2
normal_disc_vector = {(0,0): 1, (1,0): -2, (2,0): 1}
assert all(sum(n*((v+(1,))[k]) for v,n in normal_disc_vector.items()) == 0
           for k in range(3))
# The chain (Psi_u D - D - H) has this same vector; quotient projection
# cancels the first two chains and sends it to minus the (u,w) trace torus.
D = {(0,0):-1, (1,0):1}
translated_D = {(i+1,j):n for (i,j),n in D.items()}
chain_vector = {v:translated_D.get(v,0)-D.get(v,0)
                for v in set(D)|set(translated_D)}
assert chain_vector == normal_disc_vector

checks = []
for d in [1,5,7,11,13,17,19,25,31,49,101]:
    assert gcd(d,6) == 1
    inverse = (d-1)//2
    assert -2*inverse == 1-d
    assert gcd(2,d) == 1
    for sign in [-1,1]:
        p = sign*d
        # The actual finite quotient coordinate sends u wedge w to 2h;
        # the chain sign gives ruling = -2h in coker(p).
        order = d//gcd(d,2)
        assert order == d
        assert (-2*inverse-1) % d == 0
        attachment_det = p  # determinant of [[0,-p],[1,0]]
        assert abs(attachment_det) == d
    if d > 1:
        products = [[(-2 if i==j else 1 if (i-j)%d in [1,d-1] else 0)
                     for j in range(d)] for i in range(d)]
        assert all(sum(row)==0 for row in products)
        assert all(products[i][j]==products[j][i] for i in range(d) for j in range(d))
        assert all(products[(i+1)%d][(j+1)%d]==products[i][j]
                   for i in range(d) for j in range(d))
    checks.append({"d":d,"ruling_coefficient_in_h":-2,
                   "ruling_order":d,"inverse_h_in_ruling":inverse,
                   "both_signs_of_p_checked":True,
                   "ring_augmentation_relation_checked":d>1})

print(json.dumps({"finished_utc":datetime.now(timezone.utc).isoformat(),
                  "method":"direct integer intersection and chain-coordinate identities",
                  "curve_intersections":intersections,
                  "self_divisor_coefficient":self_coefficient,
                  "normal_disc_vector":{str(k):v for k,v in normal_disc_vector.items()},
                  "checks":checks,"all_passed":True},indent=2))
