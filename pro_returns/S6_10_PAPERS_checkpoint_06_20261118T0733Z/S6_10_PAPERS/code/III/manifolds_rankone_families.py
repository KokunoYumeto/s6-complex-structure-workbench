"""Unbounded one-log calculations for seven further marked MW=Z inputs.

Uses the public MIT monodromy code only to derive the geometric open
monodromies, with its local-narrowness hypotheses checked. Local fillings
are independently specified in the proof: one rank-two cusp and two
primitive rank-one models. No local-model database or API is used.
All integral kernels and left inverses use unimodular Smith decomposition.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
import sys,json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(Path(__file__).resolve().parent/'explorer'))
import os_monodromy as om

CASES=[
 ('45_II',45,'II',8,1,[0,0,1,0],1,6),
 ('47_II',47,'II',14,1,[0,0,1,0],3,6),
 ('47_III',47,'III',7,2,[0,1,0,0],3,4),
 ('55_II',55,'II',20,1,[0,0,0,1],2,6),
 ('56_IV',56,'IV',10,3,[0,0,0,1],2,3),
 ('56_III',56,'III',15,2,[0,0,0,1],2,4),
 ('49_default',49,'default',2,3,[0,0,1,0],1,3),
]
PAIRS=list(combinations(range(4),2))
delta=s.eye(4)[:,2]
chi=s.Matrix([[0,0,0,1]])

def decomp(A):
    D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(s.ZZ))
    D,U,V=(x.to_Matrix() for x in (D,U,V))
    assert U*A*V==D and abs(U.det())==abs(V.det())==1
    rank=sum(D[i,i]!=0 for i in range(min(D.shape)))
    return D,U,V,rank

def ikernel(A):
    D,U,V,r=decomp(A)
    return V[:,r:]

def bezout(values):
    coefficients=[];g=0
    for value in values:
        aa,bb,gg=map(int,s.gcdex(g,int(value)))
        coefficients=[aa*x for x in coefficients]+[bb]
        g=gg
    assert sum(int(a)*b for a,b in zip(values,coefficients))==g
    return s.Matrix(coefficients),g

def wedge(A):
    return s.Matrix([[A.extract(i,j).det() for j in PAIRS] for i in PAIRS])

def biv(x,y):
    return s.Matrix([x[i]*y[j]-x[j]*y[i] for i,j in PAIRS])

def run_case(case):
    name,entry,profile,P,Q,weights,finite,d=case
    info=om.os_info(entry,profile=profile,verbose=False)
    pair=om.check_pair(entry,(P,),(Q,),profile=profile,verbose=False)
    assert pair['valid'] and pair['pairing']==1
    original=[s.Matrix(A) for A in om.monodromy_tuple(
        entry,(P,),(Q,),tuple(weights),profile=profile,verbose=False)]
    order=list(range(finite,4))+list(range(finite))
    A=[original[i] for i in order]
    kinds=[info['kodaira_types'][i] for i in order]
    ww=[weights[i] for i in order]
    cusp=ww.index(1)
    assert len(A)==4 and A[0]**d==s.eye(4)
    assert A[0]*A[1]*A[2]*A[3]==s.eye(4)
    assert all(chi*B==chi and B*delta==delta for B in A)
    for i in (1,2,3):
        DD,_,_,r=decomp(A[i]-s.eye(4))
        expected=2 if i==cusp else 1
        assert r==expected
        assert all(abs(DD[j,j])==1 for j in range(r))
        assert (A[i]-s.eye(4))**2==s.zeros(4)
    SV,_,_,rv=decomp(s.Matrix.hstack(*[A[i]-s.eye(4) for i in (1,2,3)]))
    assert rv==3 and all(abs(SV[i,i])==1 for i in range(3))
    finite_fixed=ikernel(A[0]-s.eye(4))
    coordinates,g=bezout(list(chi*finite_fixed));assert g==1
    ell=finite_fixed*coordinates
    assert int((chi*ell)[0])==1
    fixed=[ikernel(A[i]-s.eye(4)) for i in range(4)]
    Dgraph=s.Matrix.hstack(*[A[i]-s.eye(4) for i in range(3)])
    def j(i,x):
        if i<3:
            out=s.zeros(12,x.cols);out[4*i:4*i+4,:]=x;return out
        return -(A[1]*A[2]*x).col_join(A[2]*x).col_join(x)
    K=s.Matrix.hstack(*[j(i,fixed[i]) for i in (1,2,3)],j(0,ell))
    SK,UK,VK,rk=decomp(K)
    assert rk==9 and Dgraph.rank()==3 and Dgraph*K==s.zeros(4,9)
    assert all(abs(SK[i,i])==1 for i in range(9))
    # Diagonal signs can be negative; retain them in the inverse.
    L=VK*s.diag(*[1/SK[i,i] for i in range(9)])*UK[:9,:]
    assert L*K==s.eye(9)
    delta_coordinates=L*j(0,delta)
    assert delta_coordinates[8]==0
    ext=s.Matrix.hstack(*[wedge(B)-s.eye(6) for B in A])
    SE,_,_,re=decomp(ext)
    assert re==5 and all(abs(SE[i,i])==1 for i in range(5))
    omega=ikernel(ext.T).T
    assert omega.shape==(1,6)
    if next(v for v in omega if v)!=abs(next(v for v in omega if v)):
        omega=-omega
    vertical=A[0][:3,:3]
    eta=ikernel((vertical-s.eye(3)).T).T
    assert eta.shape==(1,3)
    if eta[2]<0:eta=-eta
    bp,gg=bezout(list(eta));assert gg==1
    beta=bp.col_join(s.zeros(1,1))
    q=int(eta[2]);assert q>0 and d%q==0
    N=sum((A[0]**i for i in range(d)),s.zeros(4))
    assert N*beta==(d//q)*delta and N*ell==d*ell
    first=int(-(omega*biv(beta,ell))[0])
    second=int(-(omega*biv(ell,delta))[0])
    assert abs(first)==1
    assert (omega*biv(beta,delta))[0]==0
    checks=0
    for kval in range(1,9):
        m=d*kval
        for n in (-7,-3,-1,1,3,7):
            if gcd(n,m)!=1:continue
            r=5
            alpha,b,gcdmn=map(int,s.gcdex(m,n));assert gcdmn==1
            v=n*ell+r*delta;Nm=kval*N
            col1=s.Matrix([-int((omega*biv(beta,v))[0])]).col_join(L*j(0,Nm*beta))
            col2=s.Matrix([-alpha*int((omega*biv(ell,v))[0])]).col_join(
                L*j(0,alpha*Nm*ell+b*v))
            normals=s.zeros(10,8);normals[1:9,:]=s.eye(8)
            full=normals.row_join(col1).row_join(col2)
            reduced=s.Matrix([[first*n,second*r*alpha],[0,1]])
            assert full.extract((0,9),(8,9))==reduced
            DD=smith_normal_form(full,domain=s.ZZ)
            assert [abs(int(DD[i,i])) for i in range(10)]==[1]*9+[abs(n)]
            checks+=1
    print(name,'order',d,'types',kinds,'cusp',cusp,'ell',list(ell),
          'omega',list(omega),'q',q,'normal coefficients',(first,second),
          'full Smith checks',checks,flush=True)
    return dict(name=name,os_entry=entry,profile=profile,P=P,Q=Q,
                original_types=info['kodaira_types'],
                component_moduli=[x['moduli'] for x in info['component_maps']],
                P_components=pair['P_components'],Q_components=pair['Q_components'],
                original_weights=weights,cyclic_reorder=order,types=kinds,
                cusp_index=cusp,finite_order=d,A=[a.tolist() for a in A],
                ell=ell.tolist(),delta=delta.tolist(),fixed=[f.tolist() for f in fixed],
                K=K.tolist(),K_left_inverse=L.tolist(),delta_coordinates=delta_coordinates.tolist(),
                omega=omega.tolist(),eta=eta.tolist(),beta=beta.tolist(),q=q,
                finite_norm=N.tolist(),normal_coefficients=[first,second],checks=checks)

if __name__=='__main__':
    results=[run_case(c) for c in CASES]
    (Path(__file__).resolve().parent/'manifolds_rankone_families.json').write_text(
        json.dumps(results,indent=2,default=int)+'\n')
    print('All seven unrestricted normal matrices have unit n coefficient.',flush=True)
