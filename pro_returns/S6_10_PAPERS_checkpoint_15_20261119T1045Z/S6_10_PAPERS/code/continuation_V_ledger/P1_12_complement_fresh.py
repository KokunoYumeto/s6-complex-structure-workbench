#!/usr/bin/env python3
"""Fresh integral chain construction from the clean P1.12 input packet.

No earlier P1.12 proof, checker, chain matrix or stored basis is read.
All Smith decompositions retain and verify both unimodular transforms.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
import json,re,math
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT=Path(__file__).resolve().parents[2]
AN=ROOT/'analysis/continuation_V_ledger'
packet=(ROOT/'analysis/continuation_root/P1_12_complement_clean_assertions_packet.md').read_text()
data=json.loads(re.search(r'```json\s*(.*?)```',packet,re.S).group(1))
checks=[];certificates={}
def check(name,ok,extra=None):
    checks.append({'name':name,'pass':bool(ok),'evidence':extra})
    if not ok:raise AssertionError(name)
def ints(A):return [[int(v) for v in row] for row in A.tolist()]
def size(n,k):return math.comb(n,k) if 0<=k<=n else 0
def exterior(A,k):
    n=A.rows
    if not 0<=k<=n:return S.zeros(0,0)
    ids=list(combinations(range(n),k))
    if k==0:return S.ones(1,1)
    return S.Matrix([[A.extract(i,j).det() for j in ids] for i in ids])
def snf(A,name):
    m,n=A.shape
    if m==0 or n==0:return S.zeros(m,n),S.eye(m),S.eye(n)
    dd,uu,vv=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(S.ZZ))
    D,U,V=dd.to_Matrix(),uu.to_Matrix(),vv.to_Matrix()
    check(name+':smith_equation',U*A*V==D)
    check(name+':left_unimodular',abs(U.det())==1)
    check(name+':right_unimodular',abs(V.det())==1)
    certificates[name]={'input':ints(A),'diagonal':ints(D),'left':ints(U),'right':ints(V)}
    return D,U,V
def kernel(A,name):
    D,U,V=snf(A,name);rank=sum(D[i,i]!=0 for i in range(min(D.shape)))
    Z=V[:,rank:]
    check(name+':kernel',A*Z==S.zeros(A.rows,Z.cols))
    return Z

M=[S.Matrix(data['M1']),S.Matrix(data['M2'])]
m=[data['m1'],data['m2']]
vv=[S.Matrix(data['v1']),S.Matrix(data['v2'])]
U0=(M[0]*M[1]).inv()
check('cusp_inverse_integral',all(x.q==1 for x in U0))
Smark=S.Matrix(data['cusp_marking_S'])
check('cusp_marking',Smark.inv()*U0*Smark==S.eye(6)+S.Matrix.vstack(S.zeros(3,3).row_join(S.eye(3)),S.zeros(3,6)))
C=[];D=[];Q=[]
for i in range(2):
    lower=M[i][1:,1:];w=S.eye(5)[:,0]
    if i==0:
        c=S.Matrix.hstack(*[lower**j*w for j in range(5)])
    else:
        W=S.Matrix.hstack(*[lower**j*w for j in range(4)])
        Z=kernel(lower+S.eye(5),'negative_eigenspace')
        cof=S.Matrix(1,5,[(-1)**(j+4)*W.extract([a for a in range(5) if a!=j],range(4)).det() for j in range(5)])
        coeff=cof*Z
        a,b,g=S.gcdex(coeff[0],coeff[1]);check('negative_vector_bezout',abs(g)==1)
        z=Z*S.Matrix([a/g,b/g]);c=W.row_join(z)
    d=c.inv()*lower*c
    q=vv[i].row_join(S.zeros(1,5).col_join(c))
    check(f'cap{i+1}:basis_unimodular',abs(q.det())==1)
    check(f'cap{i+1}:adapted_action',q.inv()*M[i]*q==S.diag(S.ones(1,1),d))
    check(f'cap{i+1}:order',d**m[i]==S.eye(5))
    check(f'cap{i+1}:signed_permutation',all(sum(abs(d[a,b]) for a in range(5))==1 for b in range(5)) and all(sum(abs(d[a,b]) for b in range(5))==1 for a in range(5)))
    C.append(c);D.append(d);Q.append(q)
certificates['adapted_cap_bases']={str(i+1):{'C':ints(C[i]),'D':ints(D[i]),'Q':ints(Q[i])} for i in range(2)}

# Core-chain order: vertical k-cells, then positive quotient-circle
# prisms.  The quotient (u,y)~(u+1/m,Dy) glues the top of such a
# prism by D^-1, so its boundary is D^-1-I.  The actual homotopy
# q(x)->q(Mx)=q(x-v/m) is the negative prism, namely -D times
# the positive prism.  Keeping this orientation also makes the
# finite-cover horizontal coefficient the positive norm N.
core_d={};cover_f={};homotopy_H={}
for i in range(2):
    for k in range(8):
        nv=size(5,k);nh=size(5,k-1)
        d=S.zeros(size(6,k-1),size(6,k))
        if nh:d[:nh,nv:]=exterior(D[i].inv(),k-1)-S.eye(nh)
        core_d[i,k]=d
        if 0<=k<=6:
            ids=list(combinations(range(6),k));vert=[a for a,I in enumerate(ids) if 0 not in I];horiz=[a for a,I in enumerate(ids) if 0 in I]
            L=exterior(Q[i].inv(),k)
            norm=sum((exterior(D[i],k-1)**j for j in range(m[i])),S.zeros(nh,nh)) if nh else S.zeros(0,0)
            f=L[vert,:].col_join(norm*L[horiz,:])
        else:f=S.zeros(0,0)
        cover_f[i,k]=f
        H=S.zeros(size(6,k),size(6,k-1))
        if nh:
            ids0=list(combinations(range(6),k-1));vertical=[a for a,I in enumerate(ids0) if 0 not in I]
            H[nv:,:]=-exterior(D[i],k-1)*exterior(Q[i].inv(),k-1)[vertical,:]
        homotopy_H[i,k]=H
        check(f'cap{i+1}:cover_cycle_degree{k}',d*f==S.zeros(d.rows,f.cols))
        if k>=1:
            check(f'cap{i+1}:prism_homotopy_degree{k}',d*H==cover_f[i,k-1]*(exterior(M[i],k-1)-S.eye(size(6,k-1))))

Ydim=lambda k:2*size(6,k)+size(6,k-1)
Bdim=lambda k:size(6,k)+size(6,k-1)
dY={};dB={};J={}
for k in range(9):
    n=size(6,k);p=size(6,k-1);prev=size(6,k-1)
    dy=S.zeros(Ydim(k-1),Ydim(k));db=S.zeros(Bdim(k-1),Bdim(k))
    if k>=1:
        for i in range(2):
            dy[i*prev:(i+1)*prev,i*n:(i+1)*n]=core_d.get((i,k),S.zeros(prev,n))
            dy[i*prev:(i+1)*prev,2*n:]=(1 if i==0 else -1)*cover_f.get((i,k-1),S.zeros(prev,p))
        if p:db[:p,n:]=exterior(U0,k-1)-S.eye(p)
    dY[k]=dy;dB[k]=db
    j=S.zeros(Ydim(k),Bdim(k))
    if n:j[:n,:n]=cover_f[0,k]
    if p:
        u=exterior(U0,k-1);b=exterior(M[1],k-1)
        j[:n,n:]=-homotopy_H.get((0,k),S.zeros(n,p))*b*u
        j[n:2*n,n:]=-homotopy_H.get((1,k),S.zeros(n,p))*u
        j[2*n:,n:]=-(b-S.eye(p))*u
    J[k]=j
    if k>=1:
        check(f'Y:d_squared_degree{k}',dY[k-1]*dy==S.zeros(dY[k-1].rows,dy.cols))
        check(f'B:d_squared_degree{k}',dB[k-1]*db==S.zeros(dB[k-1].rows,db.cols))
        check(f'boundary_chain_map_degree{k}',dy*j==J[k-1]*db)

def homology(d,nextd,name):
    n=d.cols
    D,U,V=snf(d,name+':d')
    rank=sum(D[i,i]!=0 for i in range(min(D.shape)))
    cycle=V[:,rank:];coordinates=V.inv()*nextd
    check(name+':image_in_kernel',coordinates[:rank,:]==S.zeros(rank,nextd.cols))
    rel=coordinates[rank:,:]
    Dr,Ur,Vr=snf(rel,name+':relations')
    rr=sum(Dr[i,i]!=0 for i in range(min(Dr.shape)))
    keep=[i for i in range(rr) if abs(Dr[i,i])>1]+list(range(rr,cycle.cols))
    tors=[abs(int(Dr[i,i])) for i in keep if i<rr]
    reps=(cycle*Ur.inv())[:,keep]
    proj=(Ur*V.inv()[rank:,:])[keep,:]
    check(name+':representative_cycles',d*reps==S.zeros(d.rows,reps.cols))
    check(name+':representative_projection',proj*reps==S.eye(len(keep)))
    result={'rank':cycle.cols-rr,'torsion':tors,'representatives':reps,'projection':proj,
            'relation_diagonal':tors,'relation_matrix':S.diag(*tors).col_join(S.zeros(cycle.cols-rr,len(tors))) if tors else S.zeros(cycle.cols-rr,0)}
    certificates[name+':homology']={'rank':result['rank'],'torsion':tors,'representatives':ints(reps),'projection':ints(proj)}
    return result

HY={};HB={}
for k in range(8):
    print('homology degree',k,flush=True)
    HY[k]=homology(dY[k],dY[k+1],f'Y{k}')
    HB[k]=homology(dB[k],dB[k+1],f'B{k}')
expectedY=[1,1,3,9,12,9,3,0]
check('Y_all_ranks',[HY[k]['rank'] for k in range(8)]==expectedY,{'actual':[HY[k]['rank'] for k in range(8)]})
check('Y_all_homology_free',all(not HY[k]['torsion'] for k in range(8)))
for k,rank,tors in [(1,4,[]),(2,12,[]),(3,18,[2])]:
    check(f'B{k}:expected_homology',HB[k]['rank']==rank and HB[k]['torsion']==tors)

def solve_integer(A,b,name):
    D,U,V=snf(A,name);rhs=U*b;rank=sum(D[i,i]!=0 for i in range(min(D.shape)))
    z=S.zeros(A.cols,b.cols)
    for i in range(rank):
        for j in range(b.cols):
            check(name+f':divisible_{i}_{j}',rhs[i,j]%D[i,i]==0)
            z[i,j]=rhs[i,j]/D[i,i]
    check(name+':remaining_zero',rhs[rank:,:]==S.zeros(A.rows-rank,b.cols))
    x=V*z;check(name+':solution',A*x==b);return x

low_maps={}
for k in [1,2,3]:
    hB=HB[k];hY=HY[k];nt=len(hB['torsion']);JH=hY['projection']*J[k]*hB['representatives']
    ds,us,vs=snf(JH,f'jY{k}:surjectivity')
    check(f'jY{k}:onto',sum(ds[i,i]!=0 for i in range(min(ds.shape)))==hY['rank'] and all(abs(ds[i,i])==1 for i in range(hY['rank'])))
    check(f'jY{k}:torsion_zero',JH[:,:nt]==S.zeros(hY['rank'],nt))
    low_maps[k]={'jY':ints(JH)}
    if k>=2:
        free_kernel=kernel(JH[:,nt:],f'jY{k}:free_kernel')
        K=S.eye(hB['rank']+nt)[:,:nt].row_join(S.zeros(nt,free_kernel.cols).col_join(free_kernel))
        fibre_to_B=hB['projection'][:,:size(6,k)]
        fibre_to_Y=hY['projection']*J[k][:,:size(6,k)]
        Z=kernel(fibre_to_Y,f'jY{k}:vertical_kernel')
        image=fibre_to_B*Z
        rel=hB['relation_matrix']
        lifts=solve_integer(image.row_join(rel),K,f'jY{k}:vertical_lifts')
        actual=Z*lifts[:Z.cols,:]
        check(f'jY{k}:vertical_class',fibre_to_B*actual+rel*lifts[Z.cols:,:]==K)
        Udiff=exterior(U0,k)-S.eye(size(6,k));Dk,Uk,Vk=snf(Udiff,f'collapse{k}:saturated_image')
        rr=sum(Dk[i,i]!=0 for i in range(min(Dk.shape)));collapse=Uk[rr:,:]
        ck=collapse*actual
        check(f'collapse{k}:torsion_killed',ck[:,:nt]==S.zeros(ck.rows,nt))
        check(f'collapse{k}:free_isomorphism',ck[:,nt:].rows==ck[:,nt:].cols and abs(ck[:,nt:].det())==1,
              {'free_determinant':int(ck[:,nt:].det()) if ck[:,nt:].rows==ck[:,nt:].cols else None})
        low_maps[k].update({'kernel_HB_coordinates':ints(K),'vertical_lifts':ints(actual),
                            'collapse_quotient':ints(collapse),'collapse_on_kernel':ints(ck)})
    else:
        dd,uu,vv0=snf(U0-S.eye(6),'collapse1:saturated_image');rank=sum(dd[i,i]!=0 for i in range(6));q=uu[rank:,:]
        collapse_chain=q.row_join(S.zeros(q.rows,1))
        combined=JH.col_join(collapse_chain*hB['representatives'])
        check('degree1:combined_cusp_map_unimodular',combined.rows==combined.cols and abs(combined.det())==1,
              {'determinant':int(combined.det())})
        low_maps[k]['combined_cusp_map']=ints(combined)

certificates['chains']={'dY':{str(k):ints(v) for k,v in dY.items()},'dB':{str(k):ints(v) for k,v in dB.items()},'boundary_inclusion':{str(k):ints(v) for k,v in J.items()}}
certificates['low_degree_maps']=low_maps
out={'created_utc':datetime.now(timezone.utc).isoformat(),'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation',
     'old_target_proof_and_code_opened':False,'pass':all(c['pass'] for c in checks),'check_count':len(checks),
     'Y_homology':{str(k):{'rank':HY[k]['rank'],'torsion':HY[k]['torsion']} for k in HY},
     'B_homology':{str(k):{'rank':HB[k]['rank'],'torsion':HB[k]['torsion']} for k in HB},
     'checks':checks,'certificates':certificates}
p=AN/'P1_12_complement_fresh.output.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'pass':out['pass'],'check_count':out['check_count'],'output':str(p),'Y':out['Y_homology'],'B_low':{str(k):out['B_homology'][str(k)] for k in [1,2,3]}}),flush=True)
