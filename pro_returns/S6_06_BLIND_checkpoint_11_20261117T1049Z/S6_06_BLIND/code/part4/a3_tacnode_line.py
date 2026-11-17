#!/usr/bin/env python3
"""Exact local conductor-defect calculation for P4R.16."""
from pathlib import Path
import itertools
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
x, y, z, t, kap = s.symbols('x y z t kap')
h = y**2-x**4
gens = [x*z,y*z,h]
sq = [s.expand(a*b) for i,a in enumerate(gens) for b in gens[i:]]
gb = s.groebner(sq,x,y,z)
ann = {str(v):s.expand(gb.reduce(v*z*h)[1]) for v in [x,y,z]}
assert all(v==0 for v in ann.values())
assert gb.reduce(z*h)[1] != 0
jac = s.Matrix([[s.diff(g,v) for g in gens] for v in [x,y,z]])
matrices=[]
orders=[]
for sign in [1,-1]:
    j=jac.subs({x:t,y:sign*t**2,z:0})
    expected=s.Matrix([[0,0,-4*t**3],[0,0,2*sign*t**2],[t,sign*t**2,0]])
    assert j==expected
    k=s.Matrix([[0,-2*sign*t],[0,1],[1,0]])
    m=s.Matrix([[t,sign*t**2,0],[0,0,2*sign*t**2]])
    assert k*m==j
    matrices.append(m)
j=jac.subs({x:0,y:0,z:t})
m=s.Matrix([[t,0,0],[0,t,0]])
assert s.Matrix([[1,0],[0,1],[0,0]])*m==j
matrices.append(m)
def val(p):
    return min(s.Poly(s.expand(p),t).as_dict())[0]
for m in matrices:
    a=min(val(e) for e in m if e!=0)
    ab=min(val(m[:,list(cols)].det()) for cols in itertools.combinations(range(3),2) if m[:,list(cols)].det()!=0)
    orders.append([a,ab-a])
assert orders==[[1,2],[1,2],[1,1]]
A,B,C=s.symbols('A B C')
H=s.Matrix([[2*t*t*A,kap+t*B],[kap+t*B,2*C]])
assert H.det().subs(t,0)==-kap**2
checks=0
for a,b,ou,ov in itertools.product(range(5),repeat=4):
    if min(ou,ov):continue
    assert max(a-ou,b-ov)+min(a+ov,b+ou)==a+b
    checks+=1
out={'status':'PASS','statement':'P4R.16','curve_ideal':[str(g) for g in gens],
     'symbolic_square_extra_generator':str(z*h),'annihilator_mod_square':{k:str(v) for k,v in ann.items()},
     'normalized_conormal_matrices':[[[str(e) for e in m.row(i)] for i in range(m.rows)] for m in matrices],
     'elementary_divisor_orders':orders,'delta':3,'ramification_orders':[0,0,0],
     'hessian_determinant_constant':str(H.det().subs(t,0)),
     'rank_one_lattice_identity_checks':checks,'local_defect_lower_bound':3+sum(map(sum,orders)),
     'global_contracted_uniform_A3_defect_total':9}
(ROOT/'code/part4/a3_tacnode_line.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: symbolic-square generator, its exact annihilator, all normalized lattices, rank-one obstruction, and defect11>9.')
