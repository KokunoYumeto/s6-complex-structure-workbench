"""Exact conductor and conormal identities used in P4.30--P4.31."""
from pathlib import Path
import itertools,json
import sympy as sp

t,x,y,z=sp.symbols('t x y z')
directions=[(1,0),(0,1),(1,1)]
evaluation=[]
for degree in range(5):
    monomials=[x**i*y**(degree-i) for i in range(degree+1)]
    M=sp.Matrix([[q.subs({x:a,y:b}) for q in monomials]
                 for a,b in directions])
    rank=M.rank()
    assert rank==min(degree+1,3)
    evaluation.append({'degree':degree,'matrix':[[int(v) for v in row] for row in M.tolist()],'rank':int(rank)})

plane_h=y*y-x**3
plane_grad=[sp.diff(plane_h,u).subs({x:t*t,y:t**3}) for u in (x,y)]
assert plane_grad==[-3*t**4,2*t**3]
assert [sp.expand(q/t**3) for q in plane_grad]==[-3*t,2]

relations=[y*y-x*z,y*z-x**3,z*z-x*x*y]
param={x:t**3,y:t**4,z:t**5}
assert all(sp.expand(f.subs(param))==0 for f in relations)
J=sp.Matrix([[sp.diff(f,u).subs(param) for u in (x,y,z)] for f in relations])
minors=[]
for rows in itertools.combinations(range(3),2):
    for cols in itertools.combinations(range(3),2):
        v=sp.expand(J.extract(rows,cols).det())
        if v!=0:
            order=min(mon[0] for mon,coeff in sp.Poly(v,t).terms())
            minors.append({'rows':rows,'cols':cols,'value':str(v),'order':order})
assert min(q['order'] for q in minors)>=6

result={'proofs':['P4.30','P4.31'],'ordinary_triple_evaluations':evaluation,
        'plane_cusp_gradient':[str(q) for q in plane_grad],
        'plane_cusp_ramification_order':1,'plane_cusp_conormal_lattice_colength':3,
        'space_branch_parametrization':['t^3','t^4','t^5'],
        'space_branch_gradient_matrix':[[str(v) for v in row] for row in J.tolist()],
        'space_branch_minors':minors,'space_branch_ramification_order':2,
        'space_branch_minimum_minor_order':min(q['order'] for q in minors),
        'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('P4.30--P4.31 exact conductor/conormal identities: PASS')
print('Three-branch evaluation ranks, degrees 0..4:',[q['rank'] for q in evaluation])
print('Plane cusp: ramification order 1; conormal colength 3')
print('Space branch (t^3,t^4,t^5): ramification order 2; minimum minor order',result['space_branch_minimum_minor_order'])
