#!/usr/bin/env python3
"""Exact outer fixed-normal arrows and scalar endpoint winding elimination."""
from pathlib import Path
from datetime import datetime,timezone
import json,sympy as S
ROOT=Path(__file__).resolve().parents[2]
k,a,g,e,u,v,w,ab,eb=S.symbols('k a g e u v w ab eb',nonzero=True)
checks=[]
def check(name,x):
 vals=list(x) if isinstance(x,S.MatrixBase) else [x]
 assert all(S.simplify(t)==0 for t in vals),(name,x)
 checks.append(name)
old=S.Matrix([k*w,a*v,u/(k*a)])
new=S.Matrix([g*w,e*v,u/(g*e)])
arrow=S.diag(g/k,e/a,k*a/(g*e))
check('full second outer base and normal arrow',arrow*old-new)
positive_det=(eb/ab)*(k*a/(g*e))
check('positive-weight determinant',positive_det-(k/g)*(a/ab)*(eb/e))
M,ak,aa,ag,ae,ap,cp,up,vp=S.symbols('M ak aa ag ae ap cp up vp',integer=True)
wind=ak-ag+2*aa-2*ae
check('literal scalar determinant winding',wind.subs({ak:0,aa:0,ag:0,ae:M})+2*M)
fixed_square=(-vp+up)+ak+2*aa-(-ap+cp)
eliminated=fixed_square.subs({up:-ap,vp:ae-cp})
check('arbitrary normal determinant endpoint elimination',eliminated-(ak+2*aa-ae))
check('scalar marked-product obstruction',eliminated.subs({ak:0,aa:0,ae:M})+M)
A,D=S.symbols('A D',nonzero=True)
x,y,z=S.symbols('x y z',nonzero=True)
first=S.Matrix([x/(A*D),A*y,D*z])
rows=[S.Matrix([k*a*y*z,x*y/a,1/(k*y)]),
      S.Matrix([g*e*y*z,1/(e*z),x*z/g]),
      S.Matrix([1/x,x*y,x*z])]
for j,row in enumerate(rows):
 transformed=row.subs({x:first[0],y:first[1],z:first[2]},simultaneous=True)
 check(f'commuting closed scalar vertex seam row{j}',transformed-S.diag(A*D,1/D,1/A)*row)
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=len(checks),identities=checks,
 theorem='Actual marked delta-equivariant product obstruction -M and outer positive-normal determinant winding -2M for nonzero signed scalar winding M.',
 scope='These identities retain the full units and exact endpoint chart maps. They do not assign a corrected global residue to the unassembled outer determinant line.')
(ROOT/'code/part3_fourfold/scalar_outer_clutch_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
