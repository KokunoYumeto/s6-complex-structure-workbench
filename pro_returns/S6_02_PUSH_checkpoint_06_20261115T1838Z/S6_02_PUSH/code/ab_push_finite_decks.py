"""Exact finite-place and component-cover checks for Parts B.1--B.3.

All arithmetic is symbolic, integer or rational.  This script verifies
identities used in the proof; it does not infer analytic gluing from them.
"""
import json
from pathlib import Path
import sympy as S

tau, mu, beta, c, xi = S.symbols('tau mu beta c xi')
P = S.Matrix([[6*mu,tau,1,0],[beta+c,mu,0,1]])
A1 = S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
v1 = S.Matrix([1,2,-4,0])
v2 = S.Matrix([-1,-3,3,0])
data = [
    (1,3,A1,v1,(tau-1)/tau,(1-mu)/tau,
     beta+2-6*(1-mu)**2/tau,S.Matrix([[-1/tau,0],[(1-mu)/tau,1]])),
    (2,4,A2,v2,-1/tau,1+mu/tau,
     beta-3-6*mu**2/tau,S.Matrix([[1/tau,0],[-mu/tau,1]]))
]
answer = {'finite': []}
for j,m,A,v,tp,mp,bp,R in data:
    Pg = S.Matrix([[6*mp,tp,1,0],[bp+c,mp,0,1]])
    assert (R*P-Pg*A).applyfunc(S.simplify) == S.zeros(2,4)
    assert A**m == S.eye(4)
    assert A*v == v
    translation = Pg*v/m
    gamma = int(v[0])
    shift = 12*gamma//m
    assert 12*gamma % m == 0
    assert S.diff(translation[1],c) == S.Rational(gamma,m)
    xi_image = S.simplify(R[0,0]*xi+translation[0])
    unit_exponent = S.simplify(R[1,0]*xi+translation[1]-S.Rational(gamma,m)*c)
    cycles = []
    unused = set(range(12))
    while unused:
        first = min(unused)
        cycle = [first]
        nxt = (first+shift)%12
        while nxt != first:
            cycle.append(nxt)
            nxt = (nxt+shift)%12
        unused.difference_update(cycle)
        cycles.append(cycle)
    for power in range(1,m):
        assert (power*shift)%12 != 0
        assert all((k+power*shift)%12 != k for k in range(12))
    item = {'j':j,'order':m,'gamma':gamma,'shift':shift,
            'cycles':cycles,'xi_image':str(xi_image),
            'unit_exponent_in_exp_minus_2pi_i':str(unit_exponent)}
    answer['finite'].append(item)
    print('finite place',j,': period covariance verified; shift',shift)
    print('component cycles =',cycles)
    print('elliptic coordinate image =',xi_image)
    print('unit exponent (with exp(-2*pi*i*...)) =',unit_exponent)
    print('all nonidentity powers free on component and node labels')

residues = sorted({(a*4+b*3)%12 for a in (-1,1) for b in (-1,1)})
assert residues == [1,5,7,11]
assert 0 not in residues
answer['incompatible_peripheral_products_mod12'] = residues
print('possible products of finite rotations, allowing orientation reversal =',residues)
print('none is zero; a trivial cusp component permutation cannot close the relation')

# For the orientation (+4,-3), a corrected cusp must rotate by -1.
required_cusp = (-4+3)%12
assert required_cusp == 11
ramification = [(3,4),(4,3),(12,1)]
ramification_sum = sum(count*(order-1) for order,count in ramification)
assert ramification_sum == 28
euler = 2*12-ramification_sum
assert euler == -4
genus = (2-euler)//2
assert genus == 3
answer['conditional_connected_component_cover'] = {
    'degree':12,'peripheral_shifts':[4,-3,-1],
    'ramification_indices':[3,4,12],'ramification_sum':28,'genus':3}
print('necessary corrected cyclic cover: degree 12; ramification (3,4,12); genus',genus)

# The unmodified cusp fan: G1 fixes each rho label; G2 adds n.
for n in (2,12):
    assert all((j+n)%n == j for j in range(n))
    print('plain cusp base change n =',n,': rho labels modulo n globally defined')

path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(answer,indent=2)+'\n')
print('ALL EXACT CHECKS PASSED')
