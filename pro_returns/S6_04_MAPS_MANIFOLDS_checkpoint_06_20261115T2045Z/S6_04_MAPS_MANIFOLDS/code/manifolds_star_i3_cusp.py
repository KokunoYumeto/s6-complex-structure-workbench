"""Exact integral normal-torus calculation for OS50 II with the actual index-three cusp.

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
sys.path.insert(0,str(ROOT/'records/explorer/api/engine'))
import os_monodromy as om

CASES=[(50,12,'II')]

def run(entry,P,profile):
    info=om.os_info(entry,profile=profile,verbose=False)
    pair=om.check_pair(entry,(P,),(1,),profile=profile,verbose=False)
    assert pair['valid'] and pair['pairing']==1
    weights=(0,1,0)
    A=[s.eye(4)]+[s.Matrix(x) for x in om.monodromy_tuple(
        entry,(P,),(1,),weights,profile=profile,verbose=False)]
    star=A[3]
    assert (star**2-s.eye(4)).rank()==1
    for matrix,rank_expected in [(star-s.eye(4),2),(wedge(star)-s.eye(6),4)]:
        ds,_,_,rs=decomp(matrix)
        assert rs==rank_expected and all(abs(ds[i,i])==1 for i in range(rs))
    ell=s.Matrix([-1,3,0,4])
    assert star*ell==ell
    local_delta=s.Matrix([[-9,-3,1,0]])
    assert local_delta*star==local_delta and local_delta*ell==s.zeros(1,1)
    local_fix=ikernel(star-s.eye(4))
    check=s.Matrix.hstack(s.eye(4)[:,2],ell)
    assert abs((local_fix.T*local_fix).inv().multiply(local_fix.T*check).det())==1
    good=A[1]
    for matrix,rank_expected in [(good-s.eye(4),2),(wedge(good)-s.eye(6),4)]:
        ds,_,_,rs=decomp(matrix)
        assert rs==rank_expected and all(abs(ds[i,i])==1 for i in range(rs))
    ell_good=s.Matrix([-1,1,0,1])
    assert good*ell_good==ell_good
    fg=ikernel(good-s.eye(4));cg=s.Matrix.hstack(s.eye(4)[:,2],ell_good)
    assert abs(((fg.T*fg).inv()*fg.T*cg).det())==1
    product=s.eye(4)
    for x in A:product=product*x
    assert product==s.eye(4)
    N=len(A);D=s.Matrix.hstack(*[x-s.eye(4) for x in A[:-1]])
    S,U,V,rank=decomp(D)
    assert rank==3
    assert [abs(S[i,i]) for i in range(rank)]==[1,1,3]
    cusp=A[2]
    dc,uc,vc,rc=decomp(cusp-s.eye(4))
    assert [abs(dc[i,i]) for i in range(rc)]==[1,3]
    ec,_,_,rec=decomp(wedge(cusp)-s.eye(6))
    assert rec==2 and all(abs(ec[i,i])==1 for i in range(rec))
    tor_vector=uc.inv()[:,1]
    assert int((U*tor_vector)[2])%3!=0
    actual=s.Matrix.hstack(good-s.eye(4),star-s.eye(4),ikernel(cusp-s.eye(4)))
    da,_,_,ra=decomp(actual)
    assert ra==3 and all(abs(da[i,i])==1 for i in range(ra))
    Gamma=s.Matrix([[3,2],[0,1]]);F=s.Matrix([[1,1],[0,-1]])
    assert F*Gamma==s.Matrix([[3,3],[0,-1]])
    degrees=[]
    for aa in range(3):
        points=[(aa+1,0),(aa-1,1),(aa,0),(aa,1)]
        deg=[sum(sign*int((x+y)%3==cc) for sign,(x,y) in zip([1,1,-1,-1],points)) for cc in range(3)]
        assert deg==[0,0,0];degrees.append(deg)
    print('Boundary torsion',tor_vector.T,'maps to',int((U*tor_vector)[2]),'mod3; full vanishing primitive; all fixed degrees0',flush=True)
    W=V[:,rank:];Winv=V.inv()[rank:,:]
    assert Winv*W==s.eye(9)
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
    assert B.shape==(12,6) and D*B==s.zeros(4,6)
    SB,UB,VB,rb=decomp(Winv*B)
    assert rb==6 and all(abs(SB[i,i])==1 for i in range(6))
    proj=UB[6:,:]*Winv
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
    assert rk==9 and all(abs(SK[i,i])==1 for i in range(9))
    L=VK*s.diag(*[1/SK[i,i] for i in range(9)])*UK[:9,:]
    assert L*K==s.eye(9)
    assert (L*j(0,s.eye(4))) [6:,:]==J
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
        normal=s.zeros(10,6);normal[1:7,:]=s.eye(6)
        actual=[]
        for xx in s.eye(4).columnspace():
            actual.append(s.Matrix([-(omega*biv(xx,vv))[0]]).col_join(
                L*j(0,mm*xx)))
        actual.append(s.zeros(1,1).col_join(L*j(0,vv)))
        full=normal.row_join(s.Matrix.hstack(*actual))
        DD=smith_normal_form(full,domain=s.ZZ)
        nonzero=[abs(int(DD[i,i])) for i in range(10) if DD[i,i]]
        tt=gcd(mm,nn,aa,bb)*gcd(mm,nn,P,cc)
        assert mm%tt==0 and (nn==0 or abs(nn)%tt==0)
        assert gcd(gcd(mm,nn,aa,bb),gcd(mm,nn,P,cc))==1
        expected=[1]*6+[1,tt,mm]+([mm*abs(nn)//tt] if nn else [])
        assert nonzero==expected,(entry,mm,nn,aa,bb,cc,nonzero,expected)
        count+=1;zero_count+=nn==0
    print(entry,info['kodaira_types'],'rank and primitivity passed',
          'C=',C.tolist(),'minors=',minors,'full Smith cases',count,
          'n=0 cases',zero_count,flush=True)
    return dict(boundary_torsion=tor_vector.tolist(),torsion_value=int((U*tor_vector)[2]),Gamma=Gamma.tolist(),fan_symmetry=F.tolist(),fixed_degrees=degrees,entry=entry,P=P,profile=profile,types=info['kodaira_types'],
                P_components=pair['P_components'],Q_components=pair['Q_components'],
                A=[x.tolist() for x in A],graph_kernel=W.tolist(),
                unchanged_normals=B.tolist(),projection=proj.tolist(),J=J.tolist(),
                primitive_fixed_sweeps=K.tolist(),left_inverse=L.tolist(),
                omega=omega.tolist(),C=str(C),maximal_minors=list(map(str,minors)),
                full_smith_cases=count,zero_cases=zero_count)

if __name__=='__main__':
    result=[run(*c) for c in CASES]
    (ROOT/'records/manifolds_star_i3_cusp.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
