#!/usr/bin/env python3
"""Exact lattice steps for the proved relative equivariant-star algorithm."""
from pathlib import Path
from datetime import datetime,timezone
from math import gcd
from functools import reduce
from itertools import combinations
import json
import sympy as s

root=Path(__file__).resolve().parents[2]
checks=[];records=[]
def ck(name,value):
    assert bool(value),name
    checks.append({'name':name,'pass':True})
def ray(P,n,i):return s.Matrix([*(P*n),1-i,i])
def primitive_point(B):
    inv=B.inv()
    j=next(j for j in range(4) if any(x.q!=1 for x in inv[:,j]))
    alpha=inv[:,j].applyfunc(lambda x:x-s.floor(x));p=B*alpha
    g=reduce(gcd,(abs(int(x)) for x in p));return p/g,alpha/g,j
def regular_columns(C):
    d=C.cols
    return reduce(gcd,(abs(int(C.extract(rows,range(d)).det())) for rows in combinations(range(4),d)))==1

I=s.eye(2);e1=s.Matrix([1,0]);e2=s.Matrix([0,1]);o=s.zeros(2,1)
for a,b,N in ((2,1,3),(1,2,4)):
    W=s.Matrix([[1,b],[-a,-2]]);E=s.Matrix([[0,0],[0,N]]);H=I+W+E
    protectedI=s.Matrix.hstack(ray(I,o,0),ray(I,e1,0),ray(I,e1-e2,0))
    protectedW=s.Matrix.hstack(ray(W,o,0),ray(W,e1,0))
    protectedE=s.Matrix([[0,0],[0,1],[1,1],[0,0]])
    for label,B in [('I',protectedI),('W',protectedW),('E_chain',protectedE)]:ck(f'{a},{b},{N} protected {label} is regular in saturated lattice',regular_columns(B))
    for label,P0,u,v in [('I',I,e1,-e2),('W',W,e1,e2-b*e1),('E',E,e1,-e2)]:
        for ti,w in enumerate((u,v)):
            ns=(o,w,u+v);lo=[ray(P0,z,0) for z in ns];hi=[ray(H,z,1) for z in ns]
            cones=[s.Matrix.hstack(lo[0],lo[1],lo[2],hi[2]),s.Matrix.hstack(lo[0],lo[1],hi[1],hi[2]),s.Matrix.hstack(lo[0],hi[0],hi[1],hi[2])]
            for ci,B in enumerate(cones):
                D=abs(int(B.det()))
                if D<=1:continue
                name=f'{a},{b},{N} {label}/{ti}/{ci}'
                p,alpha,j=primitive_point(B);support=[i for i in range(4) if alpha[i]>0]
                ck(name+' point integral primitive',all(x.q==1 for x in p) and reduce(gcd,(abs(int(x)) for x in p))==1)
                ck(name+' half-open coefficients',all(0<=x<1 for x in alpha) and any(x>0 for x in alpha))
                ck(name+' exact ray expansion',B*alpha==p)
                F=B[:,support]
                ck(name+' minimal support face is singular',not regular_columns(F))
                drops=[]
                for i in support:
                    C=B.copy();C[:,i]=p;Di=abs(int(C.det()))
                    ck(name+f' determinant drop column {i}',Di==alpha[i]*D and 0<Di<D);drops.append(Di)
                m=s.Matrix([2,-1]);T=s.eye(4);T[:2,2]=P0*m;T[:2,3]=H*m
                ck(name+' period action unimodular',T.det()==1)
                ck(name+' transported star has same coefficients',(T*B)*alpha==T*p)
                records.append({'a':a,'b':b,'N':N,'sector':label,'triangle':ti,'tetrahedron':ci,'D':D,'primitive_point':[str(x) for x in p],'alpha':[str(x) for x in alpha],'selected_standard_column':j,'minimal_face_columns':support,'new_determinants':drops})

result={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'identities':checks,'lattice_steps':records,'proof':'notes/part3_source_zero_equivariant_resolution_audit.md','scope':'Exact local lattice-step certificate accompanying the general relative period-equivariant termination proof. No analytic quotient or return conclusion.'}
(root/'code/part3/source_zero_equivariant_resolution.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(checks)} exact relative lattice-resolution checks on {len(records)} singular actual cones.')
