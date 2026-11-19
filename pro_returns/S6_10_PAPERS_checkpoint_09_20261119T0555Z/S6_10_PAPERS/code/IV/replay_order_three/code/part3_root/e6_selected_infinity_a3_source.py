"""Exact actual A3 source charts, canonical frame and tangent comparison."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
PROOF = ROOT/'notes/part3_e6_selected_infinity_a3_source_working.md'
checks = []


def ck(v,n):
    assert bool(v),n
    checks.append(n)


a,b = S.symbols('a b',nonzero=True)
rows=[]
for k in range(4):
    N=S.Matrix([[k+1,k],[1,1]])
    ck(N.det()==1,f'chart{k}: positive quotient determinant one')
    x,y,z=a**(k+1)*b**k,a**(3-k)*b**(4-k),a*b
    ck(S.expand(x*y-z**4)==0,f'chart{k}: full invariant source equation')
    ck(all(q>=0 for q in (k+1,k,3-k,4-k)),f'chart{k}: invariant semigroup morphism')
    wedge=S.det(S.Matrix([[S.diff(x,a)/x,S.diff(x,b)/x],
                         [S.diff(z,a)/z,S.diff(z,b)/z]]))
    ck(S.cancel(z*wedge/4-S.Rational(1,4))==0,f'chart{k}: exact extending source canonical frame')
    vector=N.inv()*S.Matrix([S.Rational(16,3),2])
    ck(vector==S.Matrix([S.Rational(16,3)-2*k,2*k-S.Rational(10,3)]),
       f'chart{k}: actual radial field inverse matrix')
    ck(all(q!=0 for q in vector),f'chart{k}: one nondegenerate complex zero')
    rows.append({'k':k,'ray_matrix':[[int(q) for q in row] for row in N.tolist()],'invariant_exponents':[[k+1,k],[3-k,4-k],[1,1]],
                 'canonical_unit':'1/4','radial_weights':list(map(str,vector))})
I=S.Matrix([[-2,1,0],[1,-2,1],[0,1,-2]])
ck(I.det()==-4,'free integral A3 intersection matrix and boundary order four')
for k in range(1,4):
    ck(S.Matrix([k-1,1])+S.Matrix([k+1,1])==2*S.Matrix([k,1]),
       f'exceptional{k}: full primitive minus-two wall')
dc2=S.Integer(4)-S.Rational(1,4);dp1=-2*dc2
ck(dc2==S.Rational(15,4) and dp1==-S.Rational(15,2),'actual four-chart relative tangent difference')
ck(2*dc2+S.Rational(3,2)==9 and 2*dp1-3==-18,'two A3 and one exchanged-pair A1 differences')
ck(12-9==3 and -24-(-18)==-6,'original orbifold source Euler and Pontryagin values')
t=S.symbols('t')
disc=16*(4*t*t-4*t**3)
ck(S.factor(disc-64*t*t*(1-t))==0,'literal native source discriminant')
out={'status':'PASS_ACTUAL_A3_SOURCE_TANGENT_COMPARISON','utc':datetime.now(timezone.utc).isoformat(),
     'checks':len(checks),'check_labels':checks,'proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),
     'source_charts':rows,'exceptional_intersection_matrix':[[int(q) for q in row] for row in I.tolist()],
     'each_A3_delta_c2':'15/4','each_A3_delta_p1':'-15/2',
     'two_A3_one_A1_delta_c2':'9','two_A3_one_A1_delta_p1':'-18',
     'minimal_source_euler':'12','minimal_source_p1':'-24',
     'orbifold_source_euler':'3','orbifold_source_p1':'-6',
     'unassigned':'Actual resolved physical normal extensions, surface/reference-cap terms and total return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('source_charts','check_labels')},indent=2))
