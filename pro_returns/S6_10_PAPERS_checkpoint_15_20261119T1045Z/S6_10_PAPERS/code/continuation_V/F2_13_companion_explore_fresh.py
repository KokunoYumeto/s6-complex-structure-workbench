"""Fresh derivation from the companion definitions of F2.13 only."""
from itertools import combinations
from pathlib import Path
import json, math
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def companion(coeff):
    n=len(coeff)-1
    m=S.zeros(n)
    for i in range(n-1):m[i+1,i]=1
    for i in range(n):m[i,n-1]=-coeff[i]
    return m

def wedge(m,k):
    ix=list(combinations(range(m.rows),k))
    return S.Matrix([[m.extract(i,j).det() for j in ix] for i in ix])

def primitive(v):
    d=S.ilcm(*[x.q for x in v]); v=v*d
    g=math.gcd(*[int(x) for x in v])
    return v/g

def snf(m):
    d=smith_normal_form(m,domain=ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]

res={}
for name,g in [('A',[1,0,-1,0,1]),('B',[1,0,1,0,1])]:
    a4=companion([1,1,1,1,1]).inv();b4=companion(g)
    a6=wedge(a4,2);b6=wedge(b4,2)
    ns=(a6-S.eye(6)).col_join(b6-S.eye(6)).nullspace()
    assert len(ns)==1
    om=primitive(ns[0]);i=next(i for i,x in enumerate(om) if abs(x)==1)
    t=S.Matrix.hstack(om,*[S.eye(6)[:,j] for j in range(6) if j!=i])
    aa=t.inv()*a6*t;bb=t.inv()*b6*t
    a=aa[1:,1:];b=bb[1:,1:];n=a*b-S.eye(5)
    assert a**5==S.eye(5) and b**6==S.eye(5) and n*n==S.zeros(5)
    norm=sum((b**j for j in range(6)),S.zeros(5))
    cs=norm.row_join(n).T.nullspace()
    c=None
    for cv in cs:
        cv=primitive(cv).T
        if n.col_join(cv).rank()==3:c=cv;break
    assert c is not None
    av=S.diag(S.ones(1),a);bv=S.diag(S.ones(1),b);bv[0,1:]=c
    nv=av*bv-S.eye(6)
    assert av**5==S.eye(6) and bv**6==S.eye(6) and nv**2==S.zeros(6)
    res[name]={'a4':a4.tolist(),'b4':b4.tolist(),'omega':list(om),'quotient_basis':t.tolist(),'a5':a.tolist(),'b5':b.tolist(),'n5':n.tolist(),'n5_smith':snf(n),'extension_row':list(c),'a6':av.tolist(),'b6':bv.tolist(),'n6_smith':snf(nv),'extension_basis':[list(primitive(x)) for x in cs]}
out=Path(__file__).with_suffix('.output.json');out.write_text(json.dumps(res,indent=2,default=int)+'\n')
print(json.dumps(res,indent=2,default=int))
