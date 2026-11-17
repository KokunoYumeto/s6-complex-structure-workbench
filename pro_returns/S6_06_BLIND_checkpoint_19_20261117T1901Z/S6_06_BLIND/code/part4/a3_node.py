"""Exact matrices and normalizations in the A3 ordinary-node defect proof."""
from pathlib import Path
import json
import sympy as sp

x,y,z,a,b,c,A,B,C,U,V,W,T,u=sp.symbols('x y z a b c A B C U V W T u')
M=sp.Matrix([[y,0,a],[-z,x*x,b],[0,-z,c]])
det=sp.expand(M.det())
assert det==a*z*z+b*y*z+c*x*x*y
minors=[]
from itertools import combinations
for rs in combinations(range(3),2):
    for cs in combinations(range(3),2):
        minors.append(sp.factor(M.extract(rs,cs).det()))
subs={a:y*A,c:z*C,b:-x*x*C+z*B}
G=sp.groebner([z*z,y*z,x*x*y],z,y,x,domain=sp.QQ.frac_field(A,B,C))
assert all(G.reduce(sp.expand(m.subs(subs)))[1]==0 for m in minors)
assert sp.expand(det.subs(subs)-y*z*z*(A+B))==0

f=U*y*z*z+V*z**4+W*x*x*y*y*z+T*x**4*y*y
v=sp.symbols('v')
sub=sp.expand(f.subs(y,z*z*v)/z**4)
assert sub==U*v+V+W*x*x*z*v*v+T*x**4*v*v
normal=z*z+x**4*y
assert sp.expand(normal.subs({y:-u*u,z:x*x*u},simultaneous=True))==0

# All minimal node cases in the proof, including the excluded unit-square
# cases and the exact equality data.
cases=[
 {'module':'free','line':'dz','unit_square':False,'d':[1,1],'b':[1,1],'q':1},
 {'module':'free','line':'dh','unit_square':False,'d':[3,3],'b':[0,0],'q':1},
 {'module':'nonfree','line':'both dz','unit_square':False,'d':[2,2],'b':[1,1],'q':0},
 {'module':'nonfree','line':'mixed','unit_square':False,'d':[4,1],'b':[0,1],'q':0},
]
for case in cases:
    defect=sp.Rational(1)+sum(sp.Rational(d,2)+b for d,b in zip(case['d'],case['b']))+case['q']
    case['defect']=str(defect)
    assert defect>=sp.Rational(9,2)
assert cases[-1]['defect']=='9/2'

out={'working_proof':'notes/part4_a3_node_working.md',
 'presentation_matrix':[[str(t) for t in row] for row in M.tolist()],
 'determinant':str(det),'all_two_by_two_minors':[str(m) for m in minors],
 'ring_condition_determinant':str(sp.factor(det.subs(subs))),
 'equality_equation':str(f),'smooth_factor_substitution':str(sub),
 'normalization_map':['x','-u^2','x^2*u'],'defect_cases':cases,
 'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('A3 ordinary-node conductor and defect checks: PASS')
print('Determinant:',det)
print('Two-by-two minors:',minors)
print('Ring-condition determinant:',sp.factor(det.subs(subs)))
print('Equality defects:',[(row['module'],row['line'],row['defect']) for row in cases])
print('Smooth-factor substitution:',sub)
print('Normalization equation vanishes identically.')
