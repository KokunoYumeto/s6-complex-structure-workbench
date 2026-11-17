#!/usr/bin/env python3
"""Exact lattice identities for the retained ordinary-origin shear."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
root=Path(__file__).resolve().parents[2]
N,c,r,h,n,k,m=s.symbols('N c r h n k m',integer=True)
rr,ss=s.symbols('r s',real=True)
j1,j2,t,L=s.symbols('j1 j2 t L')
checks=[]
def ck(name,z):
    if isinstance(z,s.MatrixBase):ok=all(s.simplify(x)==0 for x in z)
    else:ok=s.simplify(z)==0
    assert ok,name
    checks.append({'name':name,'pass':True})
for a,b in ((1,2),(2,1)):
    I=s.eye(2);W=s.Matrix([[1,b],[-a,-2]]);E=s.Matrix([[0,0],[0,N]]);H=I+W+E
    for tag,P0 in [('I',I),('W',W),('E',E)]:
        T=s.eye(4);T[:2,2]=P0*s.Matrix([j1,j2]);T[:2,3]=H*s.Matrix([j1,j2])
        S=s.eye(4);S[1,3]=-c
        if tag=='E':S[1,2]=-c
        ck(f'{a},{b} {tag} actual shear determinant',S.det()-1)
        ck(f'{a},{b} {tag} exact period commutation',S*T-T*S)
    nu=s.Matrix([b*c/(2*N),-c/N])
    ck(f'{a},{b} E rational period bottom',E*nu-s.Matrix([0,-c]))
    ck(f'{a},{b} E rational period top',H*nu-s.Matrix([0,-c]))
    ck(f'{a},{b} E 2m power is integral',(2*m*nu-s.Matrix([b*n,-2*n])).subs({c:k*n,N:k*m}))
    ck(f'{a},{b} W bounded transverse period',(s.Matrix([[a,1]])*H*s.Matrix([j1,j2]))[0]-(a*j1+(N+1)*j2))
    hh=(L-a*t)/(N-1)
    ck(f'{a},{b} W longitudinal bound identity',rr*t+ss*(2*t-b*hh)-((rr+2*N*ss/(N-1))*t-b*ss*L/(N-1)))
    jj1=(L-b*j2)/2
    ck(f'{a},{b} E longitudinal bound identity',-a*ss*jj1+(N*rr+(N-1)*ss)*j2-(N*(rr+ss)*j2-a*ss*L/2))
    ck(f'{a},{b} W kernel has nonzero H first coordinate',(H*s.Matrix([-b*h,h]))[0]+b*h)
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'identities':checks,
     'proof':'notes/part3_source_zero_origin_shear.md',
     'scope':'Finite common protected refinement and obstruction to a finite-orbit fan invariant under the scalar shear alone. No actual combined A0 continuation or analytic nonexistence theorem is asserted.'}
(root/'code/part3/source_zero_origin_shear.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS: {len(checks)} exact ordinary-origin shear identities.')
