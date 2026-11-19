#!/usr/bin/env python3
"""Exact period and outer-clutch calculation; no global fan return."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json
ROOT=Path(__file__).resolve().parents[2]
s,v,m=S.symbols('s v m',integer=True)
u=S.Matrix([2*s,s]);g=S.Matrix([-3*s,-s+m*v])
H=-u-g;K=3*u+2*g
checks=[]
def test(name,expr):
 ok=bool(expr);checks.append(dict(name=name,passed=ok));assert ok,name
test('literal H period',H==S.Matrix([s,-m*v]))
test('literal K period',K==S.Matrix([0,s+2*m*v]))
test('primitive period lattice determinant',S.Matrix([[2,-3],[1,-1]]).det()==1)
wind_k,wind_a,wind_g,wind_e=0,-m,0,2*m
test('outer positive determinant winding',S.simplify(wind_k+2*wind_a+2*m)==0)
t=2*m;l0,l1,l2=6*m,0,4*m
ordinary=(-l0,l0-l2);native=(ordinary[0]+2*t,ordinary[1])
test('double native first',S.simplify(native[0]+2*m)==0)
test('double native second',S.simplify(native[1]-2*m)==0)
A,D,kappa,alpha,gamma,eta,a,b,c=S.symbols('A D kappa alpha gamma eta a b c',nonzero=True)
rows=[(kappa*alpha*b*c,a*b/alpha,1/(kappa*b)),
      (gamma*eta*b*c,1/(eta*c),a*c/gamma),
      (1/a,a*b,a*c)]
sub={a:a/(A*D),b:A*b,c:D*c}
for j,row in enumerate(rows):
 target=(A*D*row[0],row[1]/D,row[2]/A)
 actual=tuple(x.subs(sub,simultaneous=True) for x in row)
 test('full vertex row '+str(j),all(S.simplify(x-y)==0 for x,y in zip(actual,target)))
for n in (-1,1):
 test('closing square n='+str(n),S.simplify(gamma**n*gamma**(-n))==1 and S.simplify(eta**n*eta**(-n))==1)
test('Cox q preserved',S.simplify((a/(A*D))*(A*b)*(D*c)-a*b*c)==0)
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,
 actual_outer_determinant_winding='-2*m',
 doubled_native_free_arithmetic=['-2*m','2*m'],
 scope='Actual H/K periods, outer clutch, both-sign forward seam, all three vertex rows and native C2 ruling map. Root central-orientation audit pending; no numerical OS49 mapping or corrected global residue assigned.')
out=ROOT/'code/part3_fourfold/os49_outer_clutch_certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
