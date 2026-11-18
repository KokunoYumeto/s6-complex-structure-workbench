"""Exact integral normal-torus calculation for four all-semistable profiles.

Constant graph and exterior certificates are independent of the smooth-fibre
logarithmic multiplicity and affine translation. The Smith formulas are
proved for all integers in the accompanying theorem; the full augmented
Smith samples below independently corroborate those formulas.
"""
from pathlib import Path
import sys,json
import sympy as s
from math import gcd
from itertools import combinations
from sympy.matrices.normalforms import smith_normal_form

from manifolds_rankone_families import decomp,ikernel,wedge,biv
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(Path(__file__).resolve().parent/'explorer'))
import os_monodromy as om

CASES=[(45,8),(47,14),(55,20),(56,30)]

def run(entry,P):
    info=om.os_info(entry,verbose=False)
    pair=om.check_pair(entry,(P,),(1,),verbose=False)
    assert pair['valid'] and pair['pairing']==1
    weights=(0,0,0,0,1)
    A=[s.eye(4)]+[s.Matrix(x) for x in om.monodromy_tuple(
        entry,(P,),(1,),weights,verbose=False)]
    product=s.eye(4)
    for x in A:product=product*x
    assert product==s.eye(4)
    N=len(A);D=s.Matrix.hstack(*[x-s.eye(4) for x in A[:-1]])
    S,U,V,rank=decomp(D)
    assert rank==3
    assert [abs(S[i,i]) for i in range(rank)]==[1,1,1]
    W=V[:,rank:];Winv=V.inv()[rank:,:]
    assert Winv*W==s.eye(17)
    def j(i,x):
        if i<N-1:
            y=s.zeros(4*(N-1),x.cols);y[4*i:4*i+4,:]=x;return y
        out=[]
        for a in range(N-1):
            prod=s.eye(4)
            for z in A[a+1:N-1]:prod=prod*z
            out.append(-prod*x)
        return s.Matrix.vstack(*out)
    fixed=[ikernel(x-s.eye(4)) for x in A]
    B=s.Matrix.hstack(*[j(i,fixed[i]) for i in range(1,N)])
    assert B.shape==(20,14) and D*B==s.zeros(4,14)
    SB,UB,VB,rb=decomp(Winv*B)
    assert rb==14 and all(abs(SB[i,i])==1 for i in range(14))
    proj=UB[14:,:]*Winv
    J=proj*j(0,s.eye(4))
    assert J.rank()==3 and J[:,2]==s.zeros(3,1)
    selected=J[:,[0,1,3]]
    assert abs(selected.det())==1
    # Canonical leftover sweeps e1,e2,gamma.
    proj=selected.inv()*proj
    J=proj*j(0,s.eye(4))
    assert J==s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])
    K=B.row_join(j(0,s.eye(4)[:,[0,1,3]]))
    SK,UK,VK,rk=decomp(K)
    assert rk==17 and all(abs(SK[i,i])==1 for i in range(17))
    L=VK*s.diag(*[1/SK[i,i] for i in range(17)])*UK[:17,:]
    assert L*K==s.eye(17)
    assert (L*j(0,s.eye(4))) [14:,:]==J
    E=s.Matrix.hstack(*[wedge(x)-s.eye(6) for x in A])
    SE,UE,VE,re=decomp(E)
    assert re==5 and all(abs(SE[i,i])==1 for i in range(5))
    omega=s.Matrix([[P,0,0,0,0,-1]])
    assert omega*E==s.zeros(1,E.cols)
    m,n,a,b,c=s.symbols('m n a b c',integer=True)
    v=s.Matrix([a,b,c,n])
    cols=[]
    for x in s.eye(4).columnspace():
        cols.append(s.Matrix([-(omega*biv(x,v))[0]]).col_join(m*J*x))
    cols.append(s.zeros(1,1).col_join(J*v))
    C=s.Matrix.hstack(*cols)
    assert C==s.Matrix([[-P*b,P*a,n,-c,0],[m,0,0,0,a],
                       [0,m,0,0,b],[0,0,0,m,n]])
    minors=[s.factor(C[:,ii].det()) for ii in combinations(range(5),4)]
    count=zero_count=0
    for mm in range(1,13):
      for nn in (-7,-2,-1,0,1,2,7):
       for aa,bb,cc in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,3,5),
                        (3,6,2),(-2,4,3),(2,4,1),(1,1,4)]:
        if gcd(mm,aa,bb,cc,nn)!=1:continue
        vv=s.Matrix([aa,bb,cc,nn])
        normal=s.zeros(18,14);normal[1:15,:]=s.eye(14)
        actual=[]
        for xx in s.eye(4).columnspace():
            actual.append(s.Matrix([-(omega*biv(xx,vv))[0]]).col_join(
                L*j(0,mm*xx)))
        actual.append(s.zeros(1,1).col_join(L*j(0,vv)))
        full=normal.row_join(s.Matrix.hstack(*actual))
        DD=smith_normal_form(full,domain=s.ZZ)
        nonzero=[abs(int(DD[i,i])) for i in range(18) if DD[i,i]]
        tt=gcd(mm,nn,aa,bb)*gcd(mm,nn,P,cc)
        assert mm%tt==0 and (nn==0 or abs(nn)%tt==0)
        assert gcd(gcd(mm,nn,aa,bb),gcd(mm,nn,P,cc))==1
        expected=[1]*14+[1,tt,mm]+([mm*abs(nn)//tt] if nn else [])
        assert nonzero==expected,(entry,mm,nn,aa,bb,cc,nonzero,expected)
        count+=1;zero_count+=nn==0
    print(entry,info['kodaira_types'],'rank and primitivity passed',
          'C=',C.tolist(),'minors=',minors,'full Smith cases',count,
          'n=0 cases',zero_count,flush=True)
    return dict(entry=entry,P=P,types=info['kodaira_types'],
                P_components=pair['P_components'],Q_components=pair['Q_components'],
                A=[x.tolist() for x in A],graph_kernel=W.tolist(),
                unchanged_normals=B.tolist(),projection=proj.tolist(),J=J.tolist(),
                primitive_fixed_sweeps=K.tolist(),left_inverse=L.tolist(),
                omega=omega.tolist(),C=str(C),maximal_minors=list(map(str,minors)),
                full_smith_cases=count,zero_cases=zero_count)

if __name__=='__main__':
    result=[run(*c) for c in CASES]
    (Path(__file__).resolve().parent/'manifolds_semistable.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
