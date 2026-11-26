#!/usr/bin/env python3
"""Fresh exact checks for KI; no target or earlier program/output is read."""
import json
import sympy as s

J = s.diag(1,-1,-1,-1)
I4 = s.eye(4)
H,EA,EB,EC = [I4[:,j] for j in range(4)]
boundary = [H-EA-EC,EA,H-EA-EB,EB,H-EB-EC,EC]
r = H-EB
rprime = H-EA
ints = lambda c:[(c.T*J*b)[0] for b in boundary]
assert ints(r) == [1,0,0,1,0,0]
assert ints(rprime) == [0,1,0,0,1,0]
assert (EC.T*J*EC)[0] == -1
assert ((H-EA-EB).T*J*(H-EA-EB))[0] == -1

n0 = s.Matrix([0,0,1])
ne1 = s.Matrix([1,0,1])
ne2 = s.Matrix([0,1,1])
delta = s.Matrix([0,1,0])
chart = s.Matrix.hstack(n0,ne1,ne2)
assert chart.det() == 1
assert chart.inv()*delta == s.Matrix([-1,0,1])
assert delta == ne2-n0
B0 = s.Matrix([[0,1],[-1,0]])
assert B0*s.Matrix([-1,0]) == s.Matrix([0,1])
assert B0*s.Matrix([0,1]) == s.Matrix([1,0])

def add(a,b,scale=1):
    out=dict(a)
    for key,val in b.items():out[key]=out.get(key,0)+scale*val
    return {key:val for key,val in out.items() if val}

def shift(a,v):
    return {(key[0]+v[0],key[1]+v[1]):val for key,val in a.items()}

Ddelta={(0,1):1,(0,0):-1}
rotated=add(shift(Ddelta,(0,1)),Ddelta,-1)
diagonal=add(shift(Ddelta,(1,0)),Ddelta,-1)
assert rotated == {(0,2):1,(0,1):-2,(0,0):1}
assert diagonal == {(1,1):1,(1,0):-1,(0,1):-1,(0,0):1}

# Actual fibre evaluation of 2q in ordered (gamma,u,w,delta) coordinates.
Q=s.zeros(4)
Q[1,2]=2;Q[2,1]=-2
Q[0,3]=12;Q[3,0]=-12
g,u,w,dd=[I4[:,j] for j in range(4)]
pair=lambda a,b:(a.T*Q*b)[0]
assert [pair(u,w),pair(u,dd),pair(g,dd)] == [2,0,12]
down=s.Matrix([[10,-2,12,0]])
assert down*r == s.Matrix([[-2]])
assert down*rprime == s.Matrix([[12]])
assert down*EC == s.Matrix([[0]])
assert down*(H-EA-EB-EC) == s.Matrix([[0]])

m=s.symbols('m',integer=True)
d=2*m+1
b=m
values=s.Matrix([10*b,-2*b,12*b,0])
residues=s.Matrix([-5,1,-6,0])
assert s.expand(-2*b-1) == -d
assert (values-residues).applyfunc(s.expand) == d*s.Matrix([5,-1,6,0])
cohomology=J*residues
assert cohomology == s.Matrix([-5,-1,6,0])
square=(cohomology.T*J*cohomology)[0]
assert square == -12
assert (cohomology.T*J*r)[0] == 1
assert (cohomology.T*J*EA)[0] == 1

cyclic_coefficients={-1:1,0:-2,1:1}
assert sum(cyclic_coefficients.values()) == 0
assert s.expand((-12)*d) == -24*m-12
z,zn=s.symbols('z zn')
assert s.expand(-(zn-z)**2-(-z*z-zn*zn+2*z*zn)) == 0

def vector(v):return [str(x) for x in v]
def relative(v):return {str(k):val for k,val in sorted(v.items())}

print(json.dumps({
 'scope':'Fresh pre-KI-proof exact calculation; no old code, proof or output read.',
 'delta_weights':[-1,0,1],
 'rotated_period_bar_lambda':[-1,0],
 'ruling_intersections':{'H_minus_EB':[int(x) for x in ints(r)],
                         'H_minus_EA':[int(x) for x in ints(rprime)]},
 'diagonal_self_intersections':[-1,-1],
 'rotated_relative_vector':relative(rotated),
 'diagonal_relative_vector':relative(diagonal),
 'fibre_2q_values':[2,0,12],
 'downstairs_H_EA_EB_EC':[10,-2,12,0],
 'normalizing_Bezout':'-2*((d-1)/2)=1-d',
 'normalized_evaluations':vector(residues),
 'discarded_exact_d_multiples':[5,-1,6,0],
 'normalized_cohomology_coefficients':vector(cohomology),
 'normalized_square':str(square),
 'ruling_and_fixed_curve_evaluations':[1,1],
 'cyclic_product_row_sum':0,
 'scope_of_proof':'All geometric maps, UCT lifts, coefficient basis and cubic naturality are established in the written derivation; no d sampling.'
},indent=2))
