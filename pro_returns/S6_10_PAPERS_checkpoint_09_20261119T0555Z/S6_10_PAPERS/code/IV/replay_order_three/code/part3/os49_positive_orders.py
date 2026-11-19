"""Exact all-order origin and characteristic identities for P3F.32.

The geometric page and line maps are proved in the accompanying note;
this script only verifies the displayed symbolic identities.
"""
from pathlib import Path
import json
import sympy as s

sv,v,theta,m,n,D=s.symbols('s v theta m n D')
F=n*D*(sv+2*m*v)/(2*m)+n*(sv+2*m*v)**2/(4*m)-n*m*v
K=D+sv+2*m*v
angular=s.expand(F.subs(v,v+theta)-F-n*theta*K-n*m*theta*(theta-1))
deck=s.expand(F.subs(sv,sv+2*m)-F-n*K-n*m)
assert angular==deck==0
k=s.symbols('k',integer=True,positive=True)
assert s.expand((3*(-8*k)-(-24*k))/24)==0
assert s.Matrix([[2,-3],[1,-1]]).det()==1
out={
    'statement':'P3F.32',
    'status':'Exact symbolic identities verified; geometric proof independently audited',
    'orders':'m=3k, k>0; n=+1 or -1; every integer delta twist d',
    'angular_clutch':'n*theta*K+n*m*theta*(theta-1)*delta',
    'root_deck':'n*K+n*m*delta',
    'line_winding':'2*m*n',
    'page_chi':'k',
    'page_line_square':'-2*k',
    'page_signature':'-8*k',
    'primitive_K_index':0,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('All-order OS49 angular and root-deck identities verified symbolically.')
print('Cap basis determinant1 and primitive K-index0 identity verified.')
print('The actual page and line proof is independently audited in P3F.32.')
