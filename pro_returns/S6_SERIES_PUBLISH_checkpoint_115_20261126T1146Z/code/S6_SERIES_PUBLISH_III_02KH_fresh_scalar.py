#!/usr/bin/env python3
"""Fresh symbolic covering-torus and scalar maps for 02KH.

Inputs are the marked lattice and q=uw+6 gamma delta. No manuscript,
earlier proof, earlier program or prior outcome is read. The geometric
transfer and Poincare-duality maps are proved in the companion derivation.
"""
from datetime import datetime, timezone
from itertools import combinations
import json
import sympy as S

start = datetime.now(timezone.utc).isoformat()
n = S.symbols('n', integer=True, nonnegative=True)
d = 2*n + 1
basis = S.eye(4)
gamma, u, w, delta = [basis[:,i] for i in range(4)]
pairs = list(combinations(range(4), 2))

def wedge(a,b):
    return S.Matrix([a[i]*b[j]-a[j]*b[i] for i,j in pairs])

q = S.Matrix([[0,0,6,1,0,0]])
torus = S.Matrix.hstack(u,w)
assert (q*wedge(u,w))[0] == 1
assert (2*q*wedge(u,w))[0] == 2
assert torus.extract([1,2],[0,1]).det() == 1
cover_lattice = S.diag(d,1,1,1)
assert cover_lattice.det() == d
assert cover_lattice*torus == torus
inverse_two = n+1
assert S.expand(2*inverse_two-d) == 1
l0,l1,l2 = S.symbols('l0 l1 l2', integer=True)
p = 12*l0-4*l1-3*l2
cx,cy = 4*l0-l1-l2, l1+l2-3*l0
assert S.expand(3*cx-l1-p) == 0
assert S.expand(4*cy-l2+p) == 0
assert S.expand(cx+cy-l0) == 0

report = {
 'started_utc':start,
 'finished_utc':datetime.now(timezone.utc).isoformat(),
 'scope':'Fresh symbolic torus pairing and covering-lattice verification before 02KH proof exposure. The derivation supplies every topological map.',
 'all_odd_degrees':str(d),
 'ordered_wedge_pairs':pairs,
 'q_coefficients':list(q),
 'q_on_u_w':1,
 'twice_q_on_u_w':2,
 'torus_primitive_minor':1,
 'cover_lattice':[[str(z) for z in row] for row in cover_lattice.tolist()],
 'cover_index':str(S.factor(cover_lattice.det())),
 'restricted_torus_cover_identity':True,
 'inverse_of_two_mod_d':str(inverse_two),
 'exact_bezout_identity':'2*(n+1) - (2*n+1) = 1',
 'cyclic_quotient_coefficients':[str(cx),str(cy)],
 'cyclic_relation_errors':[str(p),str(-p),'0'],
 'fixed_torus_norm':'d*y',
 'torsion_input':'d*y=0 from the exact admitted KD torsion exponent',
 'endpoint_d_one':'n=0; the same scalar identities hold and the homology groups used in the target vanish',
 'sampling':'No finite sampling is used; all displayed identities are symbolic.'
}
print(json.dumps(report, indent=2, default=str))
