"""Fresh reconstruction from the isolated permitted packets only.

This computes a proposed cusp extension and must not be read as geometric
identification of that extension.  The proof file records that separate gate.
"""
from itertools import combinations
from math import comb
from pathlib import Path
import json, hashlib, datetime
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

OUT=Path(__file__).parent
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],
            [0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],
            [0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
M={1:A.T,2:B.T};M[0]=(M[1]*M[2]).inv()
v={1:s.Matrix([1,3,-2,-1,2,0]),2:s.Matrix([-1,0,0,0,0,0])}
eps={1:1,2:-1}; mult={1:5,2:4}
S=s.Matrix([[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],
            [-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]])
assert S.inv()*M[0]*S==s.eye(6)+s.Matrix.vstack(s.Matrix.hstack(s.zeros(3),s.eye(3)),s.zeros(3,6))

def n(d,k):return comb(d,k) if 0<=k<=d else 0
def ext(mat,k):
    nr,nc=mat.shape
    if k<0:return s.zeros(0,0)
    rr=list(combinations(range(nr),k));cc=list(combinations(range(nc),k))
    return s.Matrix(len(rr),len(cc),lambda i,j:mat.extract(rr[i],cc[j]).det())
W={(i,k):ext(M[i],k) for i in range(3) for k in range(-1,8)}
T={k:W[0,k]-s.eye(n(6,k)) for k in range(8)}

def smith(mat):
    if min(mat.shape)==0:return s.zeros(*mat.shape),s.eye(mat.rows),s.eye(mat.cols)
    d,u,vv=smith_normal_decomp(DomainMatrix.from_Matrix(mat).convert_to(s.ZZ))
    d,u,vv=[m.to_Matrix() for m in (d,u,vv)]
    assert u*mat*vv==d and abs(int(u.det()))==abs(int(vv.det()))==1
    return d,u,vv

TS={k:smith(T[k]) for k in range(7)}
cusp_ranks=[1,3,9,9,10,3,1,0,0]
kap={}; eta={k:s.zeros(cusp_ranks[k],n(6,k-1)) for k in range(9)}
torsion=[]
for k in range(7):
    d,u,vv=TS[k];rank=sum(d[i,i]!=0 for i in range(min(d.shape)))
    kap[k]=s.zeros(cusp_ranks[k],n(6,k)); kap[k][:n(6,k)-rank,:]=u[rank:,:]
    for j in range(rank):
        if abs(d[j,j])>1:
            torsion.append([k,j,int(d[j,j])])
            assert k==3 and abs(d[j,j])==2
            eta[4][-1,:]=vv.inv()[j,:]
kap[7]=s.zeros(0,0);kap[8]=s.zeros(0,0)

def gd(k):return n(6,k)+2*n(6,k-1)
def bd(k):return n(6,k)+n(6,k-1)
def ed(k):return n(5,k)+n(5,k-1)
def yd(k):return gd(k)+2*ed(k)+2*bd(k-1)
def dg(k):
    z=s.zeros(gd(k-1),gd(k))
    for i in (1,2):z[:n(6,k-1),n(6,k)+(i-1)*n(6,k-1):n(6,k)+i*n(6,k-1)]=W[i,k-1]-s.eye(n(6,k-1))
    return z
def db(i,k):
    z=s.zeros(bd(k-1),bd(k));z[:n(6,k-1),n(6,k):]=W[i,k-1]-s.eye(n(6,k-1))
    return z
P={i:s.Matrix.hstack(eps[i]*v[i],s.eye(6)[:,1:]) for i in (1,2)}
R={i:(P[i].inv()*M[i]*P[i])[1:,1:] for i in (1,2)}
for i in (1,2):
    assert abs(int(P[i].det()))==1 and P[i].inv()*M[i]*P[i]==s.diag(1,R[i])
def de(i,k):
    z=s.zeros(ed(k-1),ed(k));z[:n(5,k-1),n(5,k):]=ext(R[i],k-1)-s.eye(n(5,k-1))
    return z
def je(i,k):
    z=s.zeros(ed(k),bd(k))
    ff=list(combinations(range(6),k)); ss=list(combinations(range(6),k-1)) if k>=1 else []
    kr=list(combinations(range(1,6),k));ks=list(combinations(range(1,6),k-1)) if k>=1 else []
    for j,col in enumerate(ff):
        if 0 not in col:z[kr.index(col),j]=1
        else:
            q=ext(R[i],k-1); norm=sum((q**a for a in range(mult[i])),s.zeros(*q.shape))
            z[n(5,k):,j]=eps[i]*norm[:,ks.index(col[1:])]
    for j,col in enumerate(ss):
        if 0 not in col:z[n(5,k)+ks.index(col),n(6,k)+j]=1
    return z*s.diag(ext(P[i].inv(),k),ext(P[i].inv(),k-1))
def jg(i,k):
    z=s.zeros(gd(k),bd(k));z[:n(6,k),:n(6,k)]=s.eye(n(6,k))
    if i:
        st=n(6,k)+(i-1)*n(6,k-1);z[st:st+n(6,k-1),n(6,k):]=s.eye(n(6,k-1))
    else:
        z[n(6,k):n(6,k)+n(6,k-1),n(6,k):]=-W[2,k-1]*W[0,k-1]
        z[n(6,k)+n(6,k-1):,n(6,k):]=-W[0,k-1]
    return z
Y={}
for k in range(1,9):
    z=s.zeros(yd(k-1),yd(k));aa=gd(k)+2*ed(k);bb=gd(k-1)+2*ed(k-1)
    z[:bb,:aa]=s.diag(dg(k),de(1,k),de(2,k))
    for i in (1,2):
        st=aa+(i-1)*bd(k-1)
        z[:gd(k-1),st:st+bd(k-1)]=jg(i,k-1)
        es=gd(k-1)+(i-1)*ed(k-1)
        z[es:es+ed(k-1),st:st+bd(k-1)]=-je(i,k-1)
        bs=bb+(i-1)*bd(k-2)
        z[bs:bs+bd(k-2),st:st+bd(k-1)]=-db(i,k-1)
    Y[k]=z
Y[0]=s.zeros(0,yd(0));Y[9]=s.zeros(yd(8),0)
for k in range(1,9):assert Y[k-1]*Y[k]==s.zeros(Y[k-1].rows,Y[k].cols)

def j_y(k):
    z=s.zeros(yd(k),bd(k));z[:gd(k),:]=jg(0,k);return z
def j_c(k):return s.Matrix.hstack(kap[k],eta[k])
def global_complex():
    z={0:s.zeros(0,yd(0)+cusp_ranks[0])}
    for k in range(1,9):
        m=s.zeros(yd(k-1)+cusp_ranks[k-1]+bd(k-2),yd(k)+cusp_ranks[k]+bd(k-1))
        m[:yd(k-1),:yd(k)]=Y[k]
        m[:yd(k-1),yd(k)+cusp_ranks[k]:]=j_y(k-1)
        m[yd(k-1):yd(k-1)+cusp_ranks[k-1],yd(k)+cusp_ranks[k]:]=-j_c(k-1)
        m[yd(k-1)+cusp_ranks[k-1]:,yd(k)+cusp_ranks[k]:]=-db(0,k-1)
        z[k]=m
    z[9]=s.zeros(z[8].cols,0)
    for k in range(1,10):assert z[k-1]*z[k]==s.zeros(z[k-1].rows,z[k].cols)
    return z

def homology(d,k,tag):
    dd,u,vv=smith(d[k]);r=sum(dd[i,i]!=0 for i in range(min(dd.shape)))
    vinv=vv.inv(); incoming=vinv*d[k+1]
    assert incoming[:r,:]==s.zeros(r,incoming.cols)
    q,p,w=smith(incoming[r:,:]);a=sum(q[i,i]!=0 for i in range(min(q.shape)))
    tor=[abs(int(q[i,i])) for i in range(a) if abs(q[i,i])>1]
    rank=d[k].cols-r-a
    print(tag,k,rank,tor,flush=True)
    homproj=(p*vinv[r:,:])[a:,:]
    extra={}
    if tag=='Y':
        fibre=j_y(k)[:,:n(6,k)]
        img=homproj*fibre
        print('Y fibre map',k,'rank',img.rank(),'zero',img==s.zeros(*img.shape),flush=True)
        extra['fibre_homology_map']=img.tolist()
        if img==s.zeros(*img.shape):
            coeff=(p*vinv[r:,:]*fibre)[:a,:]
            div=s.diag(*[1/q[j,j] for j in range(a)])
            filler=w[:,:a]*div*coeff
            assert d[k+1]*filler==fibre
            assert all(x.q==1 for x in filler)
            extra['fibre_fillers']=filler.tolist()
    return {'rank':rank,'torsion':tor,'out_rank':r,'in_rank':a,
            'kernel_basis':vv[:,r:].tolist(),'incoming':incoming[r:,:].tolist(),
            'cycle_to_smith':p.tolist(),'incoming_smith':q.tolist(),
            'homology_projection':homproj.tolist(),**extra}

if __name__=='__main__':
    result={'inputs':'Isolated P119 packets; no receiving-proof or prior code exposure',
            'torsion_pivots':torsion,'Y_chain_ranks':[yd(k) for k in range(9)],
            'kap':{k:kap[k].tolist() for k in kap},'candidate_eta':{k:eta[k].tolist() for k in eta}}
    result['Y_homology']={}
    for k in range(9):
        result['Y_homology'][k]=homology(Y,k,'Y')
        (OUT/'fresh_candidate_chain.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
    full=global_complex()
    result['candidate_global_chain_ranks']=[full[k].cols for k in range(9)]
    result['candidate_global_homology']={}
    for k in range(9):
        result['candidate_global_homology'][k]=homology(full,k,'M candidate')
        (OUT/'fresh_candidate_chain.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
    result['candidate_differentials']={k:full[k].tolist() for k in range(1,9)}
    result['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (OUT/'fresh_candidate_chain.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
    print('SAVED',OUT/'fresh_candidate_chain.json',flush=True)
