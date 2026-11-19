#!/usr/bin/env python3
"""After-reading comparison of the printed P1.12 cone with the frozen model.

This is additional comparison work, not the before-reading certificate.
The old producer programs and stored Smith bases are not used here.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

ROOT=Path(__file__).resolve().parents[2]
fresh=ROOT/'code/continuation_V_ledger/P1_12_complement_fresh.py'
ns={'__file__':str(fresh)}
exec(compile(fresh.read_text().split('\nHY={};HB={}')[0],str(fresh),'exec'),ns)
S=ns['S'];size=ns['size'];exterior=ns['exterior'];ints=ns['ints']
M=ns['M'];vv=ns['vv'];C=ns['C'];D=ns['D'];m=ns['m'];U0=ns['U0']
fresh_dY=ns['dY'];fresh_dB=ns['dB'];fresh_J=ns['J'];Ydim=ns['Ydim'];Bdim=ns['Bdim']
checks=[];cert={}
def check(name,value):
    checks.append({'name':name,'pass':bool(value)})
    if not value:raise AssertionError(name)
def span(n,k,which):
    ids=list(ns['combinations'](range(n),k)) if 0<=k<=n else []
    return [j for j,I in enumerate(ids) if ((0 in I)==which)]

old_d={};old_f={};old_H={};psi={}
for i in range(2):
    eps=int(vv[i][0]);P=(eps*vv[i]).row_join(S.zeros(1,5).col_join(S.eye(5)))
    R=M[i][1:,1:];A=C[i].inv()
    check(f'cap{i+1}:old_P_unimodular',P.det()==1)
    check(f'cap{i+1}:old_adapted_action',P.inv()*M[i]*P==S.diag(S.ones(1,1),R))
    for k in range(9):
        n=size(6,k);p=size(6,k-1);nv=size(5,k);nh=size(5,k-1)
        dd=S.zeros(p,n)
        if nh:dd[:nh,nv:]=exterior(R,k-1)-S.eye(nh)
        old_d[i,k]=dd
        L=exterior(P.inv(),k)
        ff=S.zeros(n,n)
        if n:
            ff[:nv,:]=L[span(6,k,False),:]
            if nh:
                norm=sum((exterior(R,k-1)**j for j in range(m[i])),S.zeros(nh,nh))
                ff[nv:,:]=eps*norm*L[span(6,k,True),:]
        old_f[i,k]=ff
        hh=S.zeros(n,p)
        if nh:hh[nv:,:]=exterior(P.inv(),k-1)[span(6,k-1,False),:]
        old_H[i,k]=hh
        pp=S.zeros(n,n)
        if nv:pp[:nv,:nv]=(-1)**k*exterior(A,k)
        if nh:pp[nv:,nv:]=(-1)**k*exterior(D[i],k-1)*exterior(A,k-1)
        psi[i,k]=pp
        check(f'cap{i+1}:psi_integral_unimodular_degree{k}',all(v.q==1 for v in pp) and abs(pp.det())==1)
        if k<=7:
            check(f'cap{i+1}:cover_transport_degree{k}',pp*ff==ns['cover_f'][i,k]*((-1)**k*S.eye(n)))
            check(f'cap{i+1}:homotopy_transport_degree{k}',pp*hh==ns['homotopy_H'][i,k]*((-1)**(k-1)*S.eye(p)))
        if k>=1:
            check(f'cap{i+1}:old_cover_cycles_degree{k}',dd*ff==S.zeros(p,n))
            check(f'cap{i+1}:old_prism_degree{k}',dd*hh==old_f[i,k-1]*(exterior(M[i],k-1)-S.eye(p)))
            check(f'cap{i+1}:psi_chain_map_degree{k}',ns['core_d'].get((i,k),S.zeros(p,n))*pp==psi[i,k-1]*dd)

def dims(k):
    n=size(6,k);p=size(6,k-1);q=size(6,k-2)
    return [n,p,p,n,n,p,q,p,q]
def slots(k):
    a=0;out=[]
    for n in dims(k):out.append(slice(a,a+n));a+=n
    return out
def bigdim(k):return sum(dims(k))
big_d={};projection={};inclusion={};homotopy={};small_d={};old_J={};comparison={};small_psi={}
for k in range(10):
    n=size(6,k);p=size(6,k-1);q=size(6,k-2)
    f,x1,x2,e1,e2,a1,b1,a2,b2=slots(k)
    ff,xx1,xx2,ee1,ee2,aa1,bb1,aa2,bb2=slots(k-1)
    bd=S.zeros(bigdim(k-1),bigdim(k))
    if k>=1:
        W1=exterior(M[0],k-1);W2=exterior(M[1],k-1)
        bd[ff,x1]=W1-S.eye(p);bd[ff,x2]=W2-S.eye(p)
        bd[ff,a1]=S.eye(p);bd[ff,a2]=S.eye(p)
        bd[xx1,b1]=S.eye(q);bd[xx2,b2]=S.eye(q)
        for i,(ee,e,aa,b) in enumerate([(ee1,e1,a1,b1),(ee2,e2,a2,b2)]):
            bd[ee,e]=old_d.get((i,k),S.zeros(p,n))
            bd[ee,aa]=-old_f.get((i,k-1),S.zeros(p,p))
            bd[ee,b]=-old_H.get((i,k-1),S.zeros(p,q))
        if q:
            bd[aa1,b1]=-(exterior(M[0],k-2)-S.eye(q))
            bd[aa2,b2]=-(exterior(M[1],k-2)-S.eye(q))
    big_d[k]=bd
    pr=S.zeros(Ydim(k),bigdim(k));inc=S.zeros(bigdim(k),Ydim(k))
    if k<=8:
        pr[:n,e1]=S.eye(n);pr[:n,f]=old_f[0,k];pr[:n,x1]=old_H[0,k]
        pr[n:2*n,e2]=S.eye(n);pr[n:2*n,x2]=old_H[1,k]
        pr[2*n:,a2]=S.eye(p)
        if p:pr[2*n:,x2]=exterior(M[1],k-1)-S.eye(p)
        inc[e1,:n]=S.eye(n);inc[e2,n:2*n]=S.eye(n)
        inc[a1,2*n:]=-S.eye(p);inc[a2,2*n:]=S.eye(p)
    projection[k]=pr;inclusion[k]=inc
    kh=S.zeros(bigdim(k+1),bigdim(k));nf,nx1,nx2,ne1,ne2,na1,nb1,na2,nb2=slots(k+1)
    kh[na1,f]=S.eye(n);kh[nb1,x1]=S.eye(p);kh[nb2,x2]=S.eye(p)
    homotopy[k]=kh
    sd=S.zeros(Ydim(k-1),Ydim(k))
    if k>=1:
        for i in range(2):
            sd[i*p:(i+1)*p,i*n:(i+1)*n]=old_d.get((i,k),S.zeros(p,n))
            sd[i*p:(i+1)*p,2*n:]=(1 if i==0 else -1)*old_f.get((i,k-1),S.zeros(p,p))
    small_d[k]=sd
    jb=S.zeros(bigdim(k),Bdim(k));jb[f,:n]=S.eye(n)
    if p:
        uu=exterior(U0,k-1);ww2=exterior(M[1],k-1)
        jb[x1,n:]=-ww2*uu;jb[x2,n:]=-uu
    old_J[k]=jb
    sp=S.diag(psi.get((0,k),S.zeros(n,n)),psi.get((1,k),S.zeros(n,n)),(-1)**(k-1)*S.eye(p))
    small_psi[k]=sp;comparison[k]=sp*pr

for k in range(9):
    check(f'cone:projection_inclusion_degree{k}',projection[k]*inclusion[k]==S.eye(Ydim(k)))
    check(f'cone:deformation_retraction_degree{k}',big_d[k+1]*homotopy[k]+(homotopy[k-1]*big_d[k] if k else S.zeros(bigdim(k),bigdim(k)))==S.eye(bigdim(k))-inclusion[k]*projection[k])
    check(f'cone:homotopy_square_zero_degree{k}',homotopy[k+1]*homotopy[k]==S.zeros(bigdim(k+2),bigdim(k)))
    if k>=1:
        check(f'cone:d_squared_degree{k}',big_d[k-1]*big_d[k]==S.zeros(bigdim(k-2),bigdim(k)))
        check(f'cone:projection_chain_map_degree{k}',small_d[k]*projection[k]==projection[k-1]*big_d[k])
        check(f'cone:inclusion_chain_map_degree{k}',big_d[k]*inclusion[k]==inclusion[k-1]*small_d[k])
        check(f'cone:physical_transport_degree{k}',fresh_dY[k]*comparison[k]==comparison[k-1]*big_d[k])
    gamma=S.diag((-1)**k*S.eye(size(6,k)),(-1)**(k-1)*S.eye(size(6,k-1)))
    check(f'cone:actual_boundary_transport_degree{k}',comparison[k]*old_J[k]==fresh_J[k]*gamma)
    cert[str(k)]={'old_differential':ints(big_d[k]),'projection_to_old_small':ints(projection[k]),'inclusion_from_old_small':ints(inclusion[k]),'contracting_homotopy':ints(homotopy[k]),'small_orientation_transport':ints(small_psi[k]),'comparison_to_frozen_physical_model':ints(comparison[k]),'old_boundary_inclusion':ints(old_J[k]),'boundary_fibre_antipode':ints(gamma)}
check('cone:printed_chain_ranks',[bigdim(k) for k in range(9)]==[3,22,71,132,155,118,57,16,2])
K1=S.Matrix([[-1,-1,0,-1,0],[0,1,0,1,1],[0,1,0,0,0],[0,-1,-1,0,-1],[0,0,1,0,0]])
K2=S.Matrix([[-1,0,-1,0,-1],[-1,1,0,1,-1],[0,1,-1,1,-1],[0,-1,0,-1,1],[1,-1,1,0,1]])
for i,K in enumerate([K1,K2]):
    dd=K.inv()*M[i][1:,1:]*K
    check(f'printed_conjugator{i+1}:unimodular',abs(K.det())==1)
    check(f'printed_conjugator{i+1}:signed_permutation',all(sum(abs(dd[a,b]) for a in range(5))==1 for b in range(5)) and all(sum(abs(dd[a,b]) for b in range(5))==1 for a in range(5)))
    check(f'printed_conjugator{i+1}:exact_action',dd==D[i])
    cert[f'printed_conjugator{i+1}']={'matrix':ints(K),'action':ints(dd),'determinant':int(K.det())}
out={'completed_at':datetime.now(timezone.utc).isoformat(),'scope':'After-reading exact integral chain/basis comparison; no additional prereading claim. Old producer code and Smith exports not read by this program.','fresh_script_sha256':hashlib.sha256(fresh.read_bytes()).hexdigest(),'pass':all(x['pass'] for x in checks),'check_count':len(checks),'checks':checks,'certificates':cert}
p=ROOT/'analysis/continuation_V_ledger/P1_12_old_cone_comparison.output.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'pass':out['pass'],'check_count':len(checks),'output':str(p)},indent=2))
