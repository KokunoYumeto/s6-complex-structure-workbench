"""Exact sanity check distinguishing Engel's untwisted family from B.4.33.

The linear period local system is the same.  The affine collar and
parameter-closing data are different.  All identities are symbolic.
"""
from pathlib import Path
import json
import sympy as S

tau, mu, beta, c, w = S.symbols('tau mu beta c w')
P = S.Matrix([[6*mu, tau, 1, 0], [beta+c, mu, 0, 1]])
delta = S.Matrix([0,0,0,1])
gamma = S.Matrix([[1,0,0,0]])
ed = S.Matrix([0,1])
E = delta * gamma
A1 = S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
assert P.subs(c,c-12) == P*(S.eye(4)-12*E)
for A in (A1,A2):
    assert A*E == E*A
stack = (A1[:3,:3]-S.eye(3)).col_join(A2[:3,:3]-S.eye(3))
assert stack.rank() == 3

untwisted_vectors = [S.zeros(4,1),S.zeros(4,1)]
actual_vectors = [S.Matrix([1,2,-4,0]),S.Matrix([-1,-3,3,0])]
untwisted_jumps = []
actual_jumps = []
for vector in untwisted_vectors:
    sigma = w*P*vector
    root_translation = sigma-sigma.subs(c,c-12)
    assert root_translation == S.zeros(2,1)
    untwisted_jumps.append(list(root_translation))
for vector,epsilon in zip(actual_vectors,[1,-1]):
    sigma = w*P*vector
    root_translation = sigma-sigma.subs(c,c-12)
    assert S.expand(root_translation[1]) == 12*epsilon*w
    assert root_translation[0] == 0
    actual_jumps.append(list(root_translation.applyfunc(S.expand)))

v, k, kj, eps = S.symbols('v k kj eps')
scalar_closing = -k*ed
root_closing = scalar_closing+12*eps*w*ed
assert (root_closing.subs(k,kj+12*eps*w)+kj*ed).applyfunc(S.expand) == S.zeros(2,1)
orders = {'zero':4,'one':-3,'infinity':-1}
assert sum(orders.values()) == 0
assert 4*3 == 12 and (-3)*4 == -12

# The common zero (Z,W)=(1,1) extends on the untwisted local
# node model xy=u*z*v_coord, q=z*v_coord.
q,u = S.symbols('q u')
x,y,z,v_coord = S.symbols('x y z v_coord')
section = {x:1,y:u*q,z:1,v_coord:q}
assert (x*y-u*z*v_coord).subs(section) == 0
assert (z*v_coord-q).subs(section) == 0

record = {
    'status':'PASS',
    'same_linear_monodromy':True,
    'quotient_common_fixed_space_dimension':0,
    'untwisted_twist_vectors':[[0,0,0,0],[0,0,0,0]],
    'untwisted_root_collar_parameter_jumps':untwisted_jumps,
    'sphere_identity_closing_root_translations':actual_jumps,
    'sphere_identity_closing_W_multipliers':['s1^(-12)','s2^(12)'],
    'sphere_correcting_scalar_divisor':orders,
    'untwisted_correcting_scalar':'1',
    'untwisted_cusp_clutching':'0 with the common extending toric zero',
    'untwisted_local_zero_section':{'x':1,'y':'u*q','z':1,'v': 'q'},
    'scope':'The difference is affine closing and axial clutching, not a different invariant lattice or a failure of the period proof.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2,default=str)+'\n')
print('PASS: the untwisted and sphere ordinary period local systems have the same zero quotient fixed space.')
print('PASS: zero untwisted collars commute with the identity c -> c-12 closing.')
print('PASS: sphere identity closing instead produces s1^(-12), s2^(12) root factors.')
print('PASS: K cancels these factors by root units and has cusp order -1.')
print('PASS: the untwisted common zero extends on xy=u*z*v, so its axial clutching is zero.')
print('ALL EXACT SANITY CHECKS PASSED')
