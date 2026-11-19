"""Five unrestricted one-log/original-additive calculations, D2.21 draft.

Geometric inputs are the marked models of D2.20 and the actual finite-good
log cap. The all-parameter conclusion uses the displayed residual matrix,
not the validation bounds. No full homology theorem is registered yet.
"""
from pathlib import Path
from math import gcd
import sys,json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from manifolds_rankone_families import decomp,ikernel,wedge,biv,bezout
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'records/explorer/api/engine'))
import os_monodromy as om
CASES=[(49,'III',6,'IV*',3,2),(49,'III',6,'III',4,7),
       (50,'IV',12,'IV',3,6),(43,'II',2,'II',6,8),(46,'II',4,'II',6,8)]
chi=s.Matrix([[0,0,0,1]]);delta=s.eye(4)[:,2]
def run(entry,profile,d,finite,order,components):
    info=om.os_info(entry,profile=profile,verbose=False)
    types=list(info['kodaira_types']);weights=[int(x=='I1') for x in types]
    assert sum(weights)==1
    pair=om.check_pair(entry,(1,),(d,),profile=profile,verbose=False)
    assert pair['valid'] and pair['pairing']==1 and pair['Q_globally_narrow']
    old=[s.Matrix(x) for x in om.monodromy_tuple(entry,(1,),(d,),tuple(weights),profile=profile,verbose=False)]
    fin=types.index(finite);cyclic=list(range(fin,3))+list(range(fin))
    A=[old[i] for i in cyclic];kinds=[types[i] for i in cyclic]
    ww=[weights[i] for i in cyclic];cusp=ww.index(1);original=3-cusp
    assert A[0]**order==s.eye(4) and A[0]*A[1]*A[2]==s.eye(4)
    fixed=[ikernel(x-s.eye(4)) for x in A]
    be,g=bezout(list(chi*fixed[0]));assert g==1
    ell=fixed[0]*be; assert (chi*ell)[0]==1
    def j(i,x):
        if i<2:
            z=s.zeros(8,x.cols);z[4*i:4*i+4,:]=x;return z
        return -(A[1]*x).col_join(x)
    D=s.Matrix.hstack(A[0]-s.eye(4),A[1]-s.eye(4))
    DD,_,_,rd=decomp(D);assert rd==3 and all(abs(DD[i,i])==1 for i in range(3))
    B=s.Matrix.hstack(*[j(i,fixed[i]) for i in (1,2)])
    K=B.row_join(j(0,ell));DK,UK,VK,rk=decomp(K)
    assert B.cols==4 and rk==5 and D*K==s.zeros(4,5)
    assert all(abs(DK[i,i])==1 for i in range(5))
    L=VK*s.diag(*[1/DK[i,i] for i in range(5)])*UK[:5,:]
    assert L*K==s.eye(5) and (L*j(0,delta))[4]==0
    E=s.Matrix.hstack(*[wedge(x)-s.eye(6) for x in A]);DE,_,_,re=decomp(E)
    assert re==5 and all(abs(DE[i,i])==1 for i in range(5))
    omega=s.Matrix([[1,0,0,0,0,-d]]);assert omega*E==s.zeros(1,18)
    mat=A[original];z=(mat[:2,:2]-s.eye(2)).inv()*mat[:2,3]
    assert all(x.q==1 for x in z)
    w=s.Matrix([[1,0,z[1],0,-z[0],0]])
    kernel=ikernel(w);h=gcd(*map(int,list(omega*kernel)))
    assert h>0
    eta=ikernel((A[0][:3,:3]-s.eye(3)).T).T
    assert eta.shape==(1,3)
    if eta[2]<0:eta=-eta
    beta,g=bezout(list(eta));assert g==1
    beta=beta.col_join(s.zeros(1,1));q=int(eta[2])
    N=sum([A[0]**i for i in range(order)],s.zeros(4))
    assert N*beta==(order//q)*delta and N*ell==order*ell
    c=int(-(omega*biv(beta,ell))[0]);c2=int(-(omega*biv(ell,delta))[0])
    assert abs(c)==d//q and c2==-d
    count=0
    for k in range(1,13):
      m=order*k
      for n in [-11,-7,-3,-1,1,3,7,11]:
       if gcd(n,m)!=1:continue
       for r in [-5,0,2]:
        aa,bb,gg=map(int,s.gcdex(m,n));assert gg==1
        v=n*ell+r*delta;Nm=k*N
        col1=s.Matrix([-(omega*biv(beta,v))[0]]).col_join(L*j(0,Nm*beta))
        col2=s.Matrix([-aa*(omega*biv(ell,v))[0]]).col_join(L*j(0,aa*Nm*ell+bb*v))
        normal=s.zeros(6,5);normal[1:5,:4]=s.eye(4);normal[0,4]=h
        full=normal.row_join(col1).row_join(col2)
        residual=full.extract([0,5],[4,5,6])
        assert residual==s.Matrix([[h,c*n,-d*r*aa],[0,0,1]])
        assert gcd(h,c*n)==1
        SN=smith_normal_form(full,domain=s.ZZ)
        assert [abs(int(SN[i,i])) for i in range(6)]==[1]*6
        count+=1
    print(entry,profile,'finite',finite,'original',kinds[original],
          'h,c,q',h,c,q,'b',components-1,'full6x7Smith',count,flush=True)
    return dict(entry=entry,profile=profile,P=1,Q=d,types=kinds,weights=ww,
      A=[x.tolist() for x in A],finite_order=order,original_index=original,cusp_index=cusp,
      original_components=components,b=components-1,ell=ell.tolist(),beta=beta.tolist(),
      original_projection=z.tolist(),original_area=w.tolist(),original_fibre_kernel=kernel.tolist(),
      h=h,c=c,q=q,normal_coefficients=[c,c2],K=K.tolist(),left_inverse=L.tolist(),
      omega=omega.tolist(),norm=N.tolist(),smith_checks=count)
if __name__=='__main__':
    records=[run(*case) for case in CASES]
    (ROOT/'records/manifolds_mixed_additive.json').write_text(json.dumps(records,indent=2,default=int)+'\n')
