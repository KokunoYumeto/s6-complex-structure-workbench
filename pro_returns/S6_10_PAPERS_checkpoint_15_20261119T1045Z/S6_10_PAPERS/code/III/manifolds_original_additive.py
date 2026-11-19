"""All free regular logs with the actual original non-narrow-P additive fills.

The geometry is proved in Theorem D.2.20. This records exact monodromies,
primitive graph splittings, original principal-torus-bundle fibre kernels,
and both degree-one and degree-two integral Mayer--Vietoris matrices.
"""
from pathlib import Path
import sys,json
from math import gcd
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from manifolds_rankone_families import decomp,ikernel,wedge,biv,bezout
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'explorer'))
import os_monodromy as om
CASES=[(43,'default',2),(43,'II',2),(46,'default',4),(46,'II',4),
       (49,'III',6),(50,'IV',12)]
COMPONENTS={'II':1,'III':2,'IV':3,'IV*':7,'III*':8,'I1*':6,'I3*':8}
chi=s.Matrix([[0,0,0,1]])

def run(entry,profile,d):
    info=om.os_info(entry,profile=profile,verbose=False)
    types=list(info['kodaira_types']);zero=types.index('I1')
    weights=[0]*len(types);weights[zero]=1
    pair=om.check_pair(entry,(1,),(d,),profile=profile,verbose=False)
    assert pair['valid'] and pair['pairing']==1 and pair['Q_globally_narrow']
    A=[s.eye(4)]+[s.Matrix(x) for x in om.monodromy_tuple(entry,(1,),(d,),tuple(weights),profile=profile,verbose=False)]
    N=len(A);product=s.eye(4)
    for x in A:product=product*x
    assert product==s.eye(4)
    D=s.Matrix.hstack(*[x-s.eye(4) for x in A[:-1]])
    DD,UD,VD,rd=decomp(D)
    assert rd==3 and [abs(DD[i,i]) for i in range(rd)]==[1,1,1]
    def j(i,x):
        if i<N-1:
            y=s.zeros(4*(N-1),x.cols);y[4*i:4*i+4,:]=x;return y
        out=[]
        for k in range(N-1):
            p=s.eye(4)
            for mat in A[k+1:N-1]:p=p*mat
            out.append(-p*x)
        return s.Matrix.vstack(*out)
    fixed=[ikernel(x-s.eye(4)) for x in A]
    B=s.Matrix.hstack(*[j(i,fixed[i]) for i in range(1,N)])
    nb=B.cols
    K=B.row_join(j(0,s.eye(4)[:,[0,1,3]]))
    DK,UK,VK,rk=decomp(K)
    assert rk==4*(N-1)-3==nb+3 and D*K==s.zeros(4,rk)
    assert all(abs(DK[i,i])==1 for i in range(rk))
    L=VK*s.diag(*[1/DK[i,i] for i in range(rk)])*UK[:rk,:]
    assert L*K==s.eye(rk)
    J=(L*j(0,s.eye(4)))[nb:,:]
    assert J==s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])
    E=s.Matrix.hstack(*[wedge(x)-s.eye(6) for x in A])
    DE,UE,VE,re=decomp(E)
    assert re==5 and all(abs(DE[i,i])==1 for i in range(re))
    omega=s.Matrix([[1,0,0,0,0,-d]])
    assert omega*E==s.zeros(1,E.cols)
    local=[];fibre_relations=[];defect=0
    for k,kind in enumerate(types,1):
        mat=A[k]
        dq,uq,vq,rq=decomp(mat-s.eye(4))
        assert all(abs(dq[i,i])==1 for i in range(rq))
        quotient=uq[rq:,:];lift=uq.inv()[:,rq:]
        assert quotient*lift==s.eye(4-rq)
        nonnarrow=any(pair['P_components'][k-1])
        if kind in COMPONENTS and nonnarrow:
            r=(mat[:2,:2]-s.eye(2)).inv()*mat[:2,3]
            assert all(x.q==1 for x in r)
            w=s.Matrix([[1,0,r[1],0,-r[0],0]])
            assert w*(wedge(mat)-s.eye(6))==s.zeros(1,6)
            W=ikernel(w);values=list(omega*W)
            coeff,g=bezout(values)
            z=W*coeff
            assert g>0 and w*z==s.zeros(1,1) and int((omega*z)[0])==g
            fibre_relations.append(g)
            rr=COMPONENTS[kind];defect+=rr-2
            local_map=chi
            local.append(dict(index=k,type=kind,nonnarrow=True,components=rr,
                 elliptic_projection_shift=r.tolist(),area_covector=w.tolist(),
                 fibre_kernel=W.tolist(),global_values=values,primitive_relation=z.tolist(),
                 relation_coefficient=g,free_defect=rr-2,quotient=quotient,lift=lift,local_map=local_map))
        else:
            assert kind=='II' or kind=='I1'
            local_map=quotient
            local.append(dict(index=k,type=kind,nonnarrow=False,free_defect=0,
                               quotient=quotient,lift=lift,local_map=local_map))
    assert gcd(*fibre_relations)==1
    source_rank=5+sum(x['lift'].cols+1 for x in local)
    target_rank=N+4+sum(x['local_map'].rows for x in local)
    assert defect+source_rank-target_rank==7
    # The open family's H1 is Z gamma plus N-1 base meridians.
    def H1_matrix(mm,aa,bb,cc,nn):
        relation=s.Matrix([-aa,-bb,-cc,-nn,mm])
        dr,ur,vr,rr=decomp(relation)
        assert rr==1 and abs(dr[0,0])==1
        smooth_q=ur[1:,:]
        F=s.zeros(target_rank,source_rank)
        F[0,3]=1;F[1,4]=1
        F[N:N+4,:5]=-smooth_q
        col=5;row=N+4
        for x in local:
            i=x['index'];lift=x['lift'];nr=lift.cols;lm=x['local_map']
            F[0,col:col+nr]=chi*lift
            if i<N-1:F[1+i,col+nr]=1
            else:
                for jj in range(N-1):F[1+jj,col+nr]=-1
            F[row:row+lm.rows,col:col+nr]=-lm*lift
            col+=nr+1;row+=lm.rows
        assert col==source_rank and row==target_rank
        return F
    m,n,a,b,c=s.symbols('m n a b c',integer=True)
    v=s.Matrix([a,b,c,n]);normal=s.zeros(nb+4,nb+len(fibre_relations))
    normal[1:nb+1,:nb]=s.eye(nb)
    for kk,g in enumerate(fibre_relations):normal[0,nb+kk]=g
    normals=[]
    for x in s.eye(4).columnspace():
        normals.append(s.Matrix([-(omega*biv(x,v))[0]]).col_join(L*j(0,m*x)))
    normals.append(s.zeros(1,1).col_join(L*j(0,v)))
    regular=s.Matrix.hstack(*normals)
    reduced=regular[nb+1:,:]
    assert reduced==s.Matrix([[m,0,0,0,a],[0,m,0,0,b],[0,0,0,m,n]])
    count=zero_count=0
    for mm in range(1,13):
      for nn in [-7,-2,-1,0,1,2,7]:
       for aa,bb,cc in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,3,5),
                        (3,6,2),(-2,4,3),(2,4,1),(1,1,4)]:
        if gcd(mm,aa,bb,cc,nn)!=1:continue
        full=normal.row_join(regular.subs({m:mm,n:nn,a:aa,b:bb,c:cc}))
        SN=smith_normal_form(full,domain=s.ZZ)
        actual=[abs(int(SN[i,i])) for i in range(full.rows)]
        gg=gcd(mm,aa,bb,nn)
        assert actual==[1]*(nb+1)+[gg,mm,mm]
        F=H1_matrix(mm,aa,bb,cc,nn)
        SF=smith_normal_form(F,domain=s.ZZ)
        actual1=[abs(int(SF[i,i])) for i in range(min(F.shape)) if SF[i,i]]
        assert actual1==([1]*(target_rank-1)+([abs(nn)] if nn else []))
        # Exact base degree of all degree-two bridge classes, at representative
        # free inputs in each rank regime. Remaining inputs share the same
        # displayed gamma equation -n*k=0.
        if mm<=3:
            KF=ikernel(F)
            image=list(KF[4,:])
            assert gcd(*[abs(int(x)) for x in image])==(mm if nn==0 else 0)
        count+=1;zero_count+=nn==0
    print(entry,profile,'original',types,'fibre relations',fibre_relations,
          'free defect',defect,'H1 ranks',source_rank,target_rank,
          'full H2 and H1 Smith cases',count,'n=0',zero_count,flush=True)
    record=dict(entry=entry,profile=profile,P=1,Q=d,types=types,weights=weights,
      A=[x.tolist() for x in A],K=K.tolist(),left_inverse=L.tolist(),omega=omega.tolist(),
      fibre_relations=fibre_relations,free_defect=defect,H1_source_rank=source_rank,
      H1_target_rank=target_rank,normal=normal.tolist(),regular_symbolic=str(regular),
      residual=str(reduced),full_smith_cases=count,zero_cases=zero_count)
    for x in local:
        for key in ['quotient','lift','local_map']:
            x[key]=x[key].tolist()
    record['local']=local
    return record

if __name__=='__main__':
    record=[run(*x) for x in CASES]
    (ROOT/'manifolds_original_additive.json').write_text(json.dumps(record,indent=2,default=int)+'\n')
