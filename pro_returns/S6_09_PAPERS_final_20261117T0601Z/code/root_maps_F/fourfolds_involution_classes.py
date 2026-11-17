"""Complete56-class ordered(2,2) primitive-cusp catalogue and normalizer.

No matrix-height cutoff is used.  The finite part is similarity of
matrices of size at most3 overF2; the integral reductions are exact Smith
operations. Every returned conjugator is checked against all three
marked matrices. The theorem explains the complete integral reduction.
"""
from pathlib import Path
from itertools import product
import json
import sympy as S
from fourfolds_survivor_test import kernel,snf,factors
from fourfolds_vankampen import affine_certificate,two_point_structure

def bits(code,n):
    return tuple(tuple((code>>(i*n+j))&1 for j in range(n)) for i in range(n))
def code(M):
    n=len(M)
    return sum((int(M[i][j])&1)<<(i*n+j) for i in range(n) for j in range(n))
def mm(A,B):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%2
                       for j in range(n)) for i in range(n))
def inverse(A):
    n=len(A);R=[list(A[i])+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if R[i][j]),None)
        if pivot is None:return None
        R[j],R[pivot]=R[pivot],R[j]
        for i in range(n):
            if i!=j and R[i][j]:R[i]=[a^b for a,b in zip(R[i],R[j])]
    return tuple(tuple(row[n:]) for row in R)
def finite_classes(n):
    if n==0:return {0:(0,())},[0],{0:[0]}
    group=[]
    for c in range(1<<(n*n)):
        A=bits(c,n);Ai=inverse(A)
        if Ai is not None:group.append((A,Ai))
    unseen=set(range(1<<(n*n)));lookup={};orbits={}
    while unseen:
        rep=min(unseen);B=bits(rep,n);orbit={}
        for G,Gi in group:
            c=code(mm(mm(G,B),Gi));orbit.setdefault(c,Gi)
        # Gi sends each resulting conjugate back to the representative.
        for c,G in orbit.items():lookup[c]=(rep,G)
        unseen.difference_update(orbit);orbits[rep]=sorted(orbit)
    return lookup,sorted(orbits),orbits

FINITE={n:finite_classes(n) for n in range(4)}
assert [len(FINITE[n][1]) for n in range(4)]==[1,2,6,14]
I=S.eye(3);N=S.zeros(6)
N[:3,3:]=I

def standard_A(p,q,r):
    A=S.zeros(3)
    for i in range(p):A[i,i]=1
    for i in range(p,p+q):A[i,i]=-1
    if r:A[p+q,p+q+1]=A[p+q+1,p+q]=1
    return A
def flatten(M):return S.Matrix(list(M))
def norm_matrix(A):
    return S.Matrix.hstack(*[flatten(A*E+E*A) for E in
       (S.Matrix(3,3,lambda i,j:int(3*i+j==a)) for a in range(9))])
def primitive_completion(v):
    D,U,V=snf(v)
    assert abs(D[0,0])==1
    P=U.inv();P[:,0]=v
    assert abs(P.det())==1
    return P
def normalize_A(A):
    plus=kernel(A-I);minus=kernel(A+I);P=plus.row_join(minus)
    if abs(P.det())==1:return P,plus.cols,minus.cols,0
    assert abs(P.det())==2
    Pi=P.inv()
    j=next(j for j in range(3) if any(x.q>1 for x in Pi[:,j]))
    a=(2*Pi[:plus.cols,j]).applyfunc(lambda x:int(x)%2)
    b=(2*Pi[plus.cols:,j]).applyfunc(lambda x:int(x)%2)
    PP=plus*primitive_completion(a);PM=minus*primitive_completion(b)
    w=(PP[:,0]+PM[:,0])/2
    C=S.Matrix.hstack(PP[:,1:],PM[:,1:],w,A*w)
    assert all(x.q==1 for x in C) and abs(C.det())==1
    return C,plus.cols-1,minus.cols-1,1
def canonical_pair(M1,M2,M0):
    NN=M0-S.eye(6);DD,U,V=snf(NN)
    assert NN*NN==S.zeros(6) and factors(NN)==[1,1,1]
    beta=V[:,:3];alpha=NN*beta;R=alpha.row_join(beta)
    assert abs(R.det())==1 and R.inv()*NN*R==N
    T=R.inv()*M1*R;A=T[:3,:3]
    assert T[3:,:3]==S.zeros(3) and T[3:,3:]==-A
    C,p,q,r=normalize_A(A);W=S.diag(C,C).inv()*R.inv()
    T=W*M1*W.inv();A=standard_A(p,q,r);B=T[:3,3:]
    assert T[:3,:3]==A and A*B==B*A
    G=S.eye(3);labels=[];Bcan=S.zeros(3)
    for start,n in ((0,p),(p,q)):
        sub=B[start:start+n,start:start+n]
        c=code(sub.tolist());rep,gg=FINITE[n][0][c];labels.append(rep)
        if n:
            lift=S.Matrix(gg);assert abs(lift.det())==1
            G[start:start+n,start:start+n]=lift
            Bcan[start:start+n,start:start+n]=S.Matrix(bits(rep,n))
    W=S.diag(G,G)*W;BB=(W*M1*W.inv())[:3,3:]
    Z=norm_matrix(A);DD,UU,VV=snf(Z);rhs=UU*flatten(BB-Bcan)
    y=S.zeros(9,1)
    for i in range(9):
        if DD[i,i]:
            assert rhs[i]%DD[i,i]==0;y[i]=rhs[i]/DD[i,i]
        else:assert rhs[i]==0
    D=S.Matrix(3,3,list(VV*y));F=S.eye(6);F[:3,3:]=D
    P=F*W
    M=S.BlockMatrix([[A,Bcan],[S.zeros(3),-A]]).as_explicit()
    target=(M,M*(S.eye(6)-N),S.eye(6)+N)
    assert abs(P.det())==1 and all(x.q==1 for x in P)
    assert all(P*X==Y*P for X,Y in zip((M1,M2,M0),target))
    return (p,q,r,*labels),target,P

def jsonable(x):
    if isinstance(x,S.MatrixBase):return [[int(z) for z in row] for row in x.tolist()]
    if isinstance(x,dict):return {str(k):jsonable(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [jsonable(v) for v in x]
    if isinstance(x,S.Integer):return int(x)
    if isinstance(x,S.Rational):return str(x)
    return x

if __name__=='__main__':
    root=Path(__file__).resolve().parents[1];rows=[];tate=[]
    Q=S.eye(6)
    for i,j,a in ((0,3,2),(1,5,-3),(5,2,1),(3,1,-2)):
        E=S.eye(6);E[i,j]=a;Q=E*Q
    for r in (0,1):
      for p in range(4-2*r):
        q=3-2*r-p;A=standard_A(p,q,r)
        comm=S.Matrix.hstack(*[flatten(A*E-E*A) for E in
             (S.Matrix(3,3,lambda i,j:int(3*i+j==a)) for a in range(9))])
        K=kernel(comm);Z=K.gauss_jordan_solve(norm_matrix(A))[0]
        assert all(x.q==1 for x in Z)
        ff=factors(Z);assert len(ff)==K.cols and ff.count(2)==p*p+q*q and all(x in (1,2) for x in ff)
        tate.append({'p':p,'q':q,'r':r,'Smith':ff})
        for bp,bq in product(FINITE[p][1],FINITE[q][1]):
            B=S.zeros(3)
            if p:B[:p,:p]=S.Matrix(bits(bp,p))
            if q:B[p:p+q,p:p+q]=S.Matrix(bits(bq,q))
            M1=S.BlockMatrix([[A,B],[S.zeros(3),-A]]).as_explicit()
            M2=M1*(S.eye(6)-N);M0=S.eye(6)+N
            assert M1*M2*M0==S.eye(6) and M1**2==M2**2==S.eye(6)
            key=(p,q,r,bp,bq)
            got,_,_=canonical_pair(M1,M2,M0);assert got==key
            got,_,_=canonical_pair(*(Q*M*Q.inv() for M in (M1,M2,M0)));assert got==key
            vs=[kernel(M-S.eye(6))[:,0] for M in (M1,M2)]
            certs=[affine_certificate(M,v,4) for M,v in zip((M1,M2),vs)]
            assert all(c['free'] for c in certs)
            group=two_point_structure([M1,M2],vs,[4,4])
            rows.append({'key':key,'matrices':[M1,M2,M0],'numerators':vs,
                         'actual_orders':[4,4],'group':group})
        print('INTEGRAL TYPE',p,q,r,'Tate quotient',ff,'classes',len(FINITE[p][1])*len(FINITE[q][1]),flush=True)
    assert len(rows)==56 and len({tuple(r['key']) for r in rows})==56
    payload={'classes':rows,'tate':tate,'finite_field_orbits':{n:FINITE[n][2] for n in FINITE},
             'normalizations_checked':112,'free_affine_actions_checked':112}
    (root/'records/fourfolds_involution_classes.json').write_text(json.dumps(jsonable(payload),indent=2)+'\n')
    print('ALL56 CLASSES;112 EXACT CONJUGATORS;112 FREE ORDER4 LIFTS; COMPLETE GROUPS AND H1: PASS')
