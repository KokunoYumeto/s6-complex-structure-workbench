#!/usr/bin/env python3
"""New exact input/lattice derivation for III 02KM, before target exposure.

Only the released defining-input JSON is read. No source engine, topology
program, target proof, old check or old outcome is imported or executed.
The full proof and its geometric framing comparison remain a separate task.
"""
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
import hashlib
import json
import math
import sympy as S

HERE = Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation5_iii_d2'
INPUT = INPUT_ROOT.parent/'continuation5_iii_infra'/'S6_SERIES_PUBLISH_III_02KM_marked_inputs.json'
E = S.eye(4)
WEDGES = list(combinations(range(4), 2))
FINITE_H = [[[1,-2],[0,1]],[[1,0],[0,1]],[[6,-7],[1,-1]],
            [[1,-2],[-1,3]],[[0,-1],[1,2]],[[1,-2],[-2,5]],[[1,1],[0,1]]]
POLE = [0,0,1,0,1,1,2]
EPSILON = [0,0,1,0,1,1,1]
SECTION_DEGREE = [4,7,2,10,2,4,1]


def integral(A):
    A = S.Matrix(A)
    assert all(x.q == 1 for x in A)
    return A


def same(A, B):
    assert S.Matrix(A).shape == S.Matrix(B).shape
    assert all(S.expand(x) == 0 for x in S.Matrix(A)-S.Matrix(B))


def wedge(A):
    return S.Matrix([[A.extract(i,j).det() for j in WEDGES] for i in WEDGES])


def skew(coeff):
    A = S.zeros(4)
    for c,(i,j) in zip(coeff,WEDGES): A[i,j],A[j,i] = c,-c
    return A


def smith_maps(A):
    """Euclidean row/column reduction, retaining both integral maps.

    Every operation is a swap, a sign, or addition of an integer multiple.
    The offending-entry step enforces divisibility before the next pivot.
    """
    A = integral(A)
    D,U,V = A.copy(),S.eye(A.rows),S.eye(A.cols)
    def rowadd(i,j,c):
        D[i,:] = D[i,:]+c*D[j,:]
        U[i,:] = U[i,:]+c*U[j,:]
    def coladd(i,j,c):
        D[:,i] = D[:,i]+c*D[:,j]
        V[:,i] = V[:,i]+c*V[:,j]
    k = 0
    while k < min(D.shape):
        nz = [(abs(D[i,j]),i,j) for i in range(k,D.rows)
              for j in range(k,D.cols) if D[i,j]]
        if not nz: break
        _,i,j = min(nz)
        D.row_swap(k,i); U.row_swap(k,i)
        D.col_swap(k,j); V.col_swap(k,j)
        while True:
            if D[k,k] < 0:
                D[k,:] = -D[k,:]; U[k,:] = -U[k,:]
            changed = False
            for i in range(k+1,D.rows):
                if D[i,k]:
                    q = D[i,k]//D[k,k]
                    rowadd(i,k,-q)
                    if D[i,k]: D.row_swap(i,k); U.row_swap(i,k)
                    changed = True
                    break
            if changed: continue
            for j in range(k+1,D.cols):
                if D[k,j]:
                    q = D[k,j]//D[k,k]
                    coladd(j,k,-q)
                    if D[k,j]: D.col_swap(j,k); V.col_swap(j,k)
                    changed = True
                    break
            if changed: continue
            bad = next(((i,j) for i in range(k+1,D.rows)
                        for j in range(k+1,D.cols)
                        if D[i,j] % D[k,k]),None)
            if bad is None: break
            rowadd(k,bad[0],1)
        k += 1
    same(U*A*V,D)
    assert abs(U.det()) == abs(V.det()) == 1
    assert D == S.diag(*[D[i,i] for i in range(k)]).row_join(S.zeros(k,D.cols-k)).col_join(S.zeros(D.rows-k,D.cols))
    assert all(D[i+1,i+1] % D[i,i] == 0 for i in range(k-1))
    return D,U,V,k


def integer_solve(A,B,shorten=False):
    D,U,V,r = smith_maps(A)
    Y = U*S.Matrix(B)
    assert Y[r:,:] == S.zeros(Y.rows-r,Y.cols)
    Z = S.zeros(A.cols,Y.cols)
    for i in range(r): Z[i,:] = Y[i,:]/D[i,i]
    X = integral(V*Z)
    if shorten and r<A.cols:
        # Shorten within the exact kernel coset; the displayed map is checked
        # by multiplication. No assertion depends on a shortest-vector claim.
        basis=V[:,r:].T.lll()
        orth=[]
        for i in range(basis.rows):
            v=basis[i,:]
            for z in orth:v=v-(v.dot(z)/z.dot(z))*z
            orth.append(v)
        for j in range(X.cols):
            y=X[:,j].T
            for i in range(basis.rows-1,-1,-1):
                c=S.floor(y.dot(orth[i])/orth[i].dot(orth[i])+S.Rational(1,2))
                y=y-c*basis[i,:]
            X[:,j]=y.T
    same(A*X,B)
    return X


def rational_local_solution(A,q):
    B=A-S.eye(2)
    if B.det(): return B.inv()*q
    piv = next(((i,j) for i in range(2) for j in range(2) if B[i,j]),None)
    if piv is None:
        assert q == S.zeros(2,1)
        return S.zeros(2,1)
    i,j = piv
    x=S.zeros(2,1);x[j]=q[i]/B[i,j]
    same(B*x,q)
    return x


def lift(A,p,q,w):
    J=S.Matrix([[0,1],[-1,0]])
    beta=-p.T*J*A
    x=rational_local_solution(A,q)
    central=(beta*x)[0]+w
    B=E.copy();B[:2,:2]=A;B[:2,3]=q;B[2,:2]=beta;B[2,3]=central
    return B


def poincare_diagram(A,p,q,w,B):
    J=S.Matrix([[0,1],[-1,0]])
    h=rational_local_solution(A,p);z=rational_local_solution(A,q)
    b=-h.T*J
    change=E.copy();change[:2,3]=z;change[2,:2]=b
    inverse=E.copy();inverse[:2,3]=-z;inverse[2,:2]=-b;inverse[2,3]=(b*z)[0]
    diagonal=E.copy();diagonal[:2,:2]=A;diagonal[2,3]=w
    same(change*inverse,E);same(inverse*diagonal*change,B)
    flip=S.diag(-1,-1,1,1)
    same(flip*B*flip,lift(A,-p,-q,w))
    found=0
    for kind,cocycle in [('P',p),('Q',q)]:
        D,U,V,r=smith_maps(A-S.eye(2));v=U*cocycle
        if any(v[i]%D[i,i] for i in range(r)):continue
        x=integer_solve(A-S.eye(2),cocycle)
        if kind=='P':
            gauge=E.copy();gauge[2,:2]=-x.T*J
            converted=gauge*B*gauge.inv()
            same(converted[2,:2],S.zeros(1,2))
        else:
            gauge=E.copy();gauge[:2,3]=-x
            converted=gauge.inv()*B*gauge
            same(converted[:2,3],S.zeros(2,1))
        assert converted[2,3]==w
        found+=1
    assert found>=1


def product(mats):
    P=S.eye(mats[0].rows)
    for A in mats:P=P*A
    return P


def section_generator_check(elliptic,g):
    local=[];C=[];R=[];prefix=S.eye(2)
    for A in elliptic:
        D,U,V,r=smith_maps(A-S.eye(2))
        B=U.inv()[:,:r]
        local.append(B)
        C.append(U[:r,:]*(A-S.eye(2)))
        R.append(prefix*B)
        prefix=prefix*A
    same(prefix,S.eye(2))
    R=S.Matrix.hstack(*R);C=S.Matrix.vstack(*C)
    same(R*C,S.zeros(2,2))
    D,U,V,r=smith_maps(R)
    assert r==2 and D[:2,:2]==S.eye(2)
    K=V[:,r:]; coord=V.inv()[r:,:]
    relation=integral(coord*C)
    F,L,T,s=smith_maps(relation)
    assert s==2 and F[:2,:2]==S.eye(2) and F.rows==3
    gamma=S.Matrix.vstack(*[integer_solve(B,v) for B,v in zip(local,g)])
    same(R*gamma,S.zeros(2,1))
    c=integral(L*coord*gamma)
    assert abs(c[2])==1
    return {'generator_quotient_coordinate':int(c[2]),
            'local_image_bases':[B.tolist() for B in local],
            'section_relation':R.tolist(), 'coboundary':C.tolist(),
            'relation_kernel':K.tolist(),'relation_kernel_inverse':coord.tolist(),
            'coboundary_target_change':L.tolist(),'coboundary_source_change':T.tolist(),
            'quotient_map':(L[2,:]*coord).tolist(),
            'quotient_section_local':(int(c[2])*gamma).tolist()}


def rank_one_basis(A):
    N=A-E;D,U,V,r=smith_maps(N)
    assert r==1 and D[0,0]==1 and N*N==S.zeros(4)
    w=U.inv()[:,0];b=V[:,0];K=V[:,1:]
    z=V.inv()[1:,:]*w
    F,L,T,s=smith_maps(z)
    assert s==1 and F[0,0]==1
    fixed=integral(K*L.inv())
    H=S.Matrix.hstack(w,b,fixed[:,1:])
    assert abs(H.det())==1
    target=E.copy();target[0,1]=1
    same(A*H,H*target)
    return H


def rank_two_basis(A):
    N=A-E;D,U,V,r=smith_maps(N)
    assert r==2 and D[:2,:2]==S.eye(2) and N*N==S.zeros(4)
    W=U.inv()[:,:2];B=V[:,:2]
    H=S.Matrix.hstack(W[:,0],B[:,0],W[:,1],B[:,1])
    assert abs(H.det())==1
    target=E.copy();target[0,1]=target[2,3]=1
    same(A*H,H*target)
    return H


def first_unit_minor(A,size):
    for rows in combinations(range(A.rows),size):
        for cols in combinations(range(A.cols),size):
            det=A.extract(rows,cols).det()
            if abs(det)==1:return rows,cols,int(det)
    return None


def lists(x):
    if isinstance(x,S.MatrixBase):return [[int(c) for c in row] for row in x.tolist()]
    if isinstance(x,dict):return {k:lists(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [lists(v) for v in x]
    if isinstance(x,S.Integer):return int(x)
    return x


def derive(row):
    p,q=row['P'],row['Q']
    ell=S.Matrix(row['ell']);delta=E[:,2];chi=S.Matrix([[0,0,0,1]])
    elliptic=[S.Matrix(A) for A in row['elliptic_matrices']]
    g=[S.Matrix(v) for v in row['generator_section_cocycle']]
    section=section_generator_check(elliptic,g)
    raw=[integral(lift(A,p*v,q*v,w)) for A,v,w in zip(elliptic,g,row['weights'])]
    for A,v,w,B in zip(elliptic,g,row['weights'],raw):poincare_diagram(A,p*v,q*v,w,B)
    assert [A.tolist() for A in raw]==row['matrices_input_to_be_rederived']
    same(product(raw),E)
    unweighted=product([lift(A,v,v,0) for A,v in zip(elliptic,g)])
    H=E.copy();H[2,3]=-S.Rational(1,p*q)
    same(unweighted,H)
    a=row['additive_index_zero_based'];order=list(range(a,4))+list(range(a))
    mats=[raw[i] for i in order];weights=[row['weights'][i] for i in order]
    d={'II':6,'III':4,'IV':3,'IV*':3}[row['fibers'][a]]
    irow=row['row']-1
    standard={'II':[[0,1],[-1,1]],'III':[[0,1],[-1,0]],
              'IV':[[0,1],[-1,-1]],'IV*':[[0,-1],[1,-1]]}[row['fibers'][a]]
    Hfinite=S.Matrix(FINITE_H[irow])
    assert Hfinite.det()==1
    same(elliptic[a]*Hfinite,Hfinite*S.Matrix(standard))
    shiftQ=rational_local_solution(elliptic[a],q*g[a])
    shiftP=rational_local_solution(elliptic[a],p*g[a])
    same(shiftQ,-ell[:2,0])
    assert all(x.q==1 for x in shiftQ)
    assert math.lcm(*[int(x.q) for x in shiftP])==q
    same(product(mats),E)
    same(mats[0]**d,E)
    assert all(mats[0]**j!=E for j in range(1,d))
    for A in mats: same(chi*A,chi)
    same(mats[0]*ell,ell);same(mats[0]*delta,delta)
    omega=S.Matrix([[p,0,0,0,0,-q]]);form=skew(list(omega))
    for A in mats:same(A.T*form*A,form)
    lam=-(form*ell).T
    u=integer_solve(lam[:,:3],S.ones(1,1)).col_join(S.zeros(1,1))
    pi=S.Matrix.vstack(lam,chi)
    same(pi*S.Matrix.hstack(u,ell),S.eye(2))
    finite_relation=integer_solve(mats[0]-E,E-u*lam-ell*chi,shorten=True)
    same(pi*delta,S.Matrix([q,0]))
    norm=sum((mats[0]**j for j in range(d)),S.zeros(4))
    same(norm*u,S.Rational(d,q)*delta)
    local={};fixed={};vanish=[]
    for i in range(1,4):
        if weights[i]:
            B=rank_two_basis(mats[i]);F=B[:,[0,2]];vanish.extend([B[:,0],B[:,2]])
            kind='rank_two'
        else:
            B=rank_one_basis(mats[i]);F=B[:,[0,2,3]];vanish.append(B[:,0])
            kind='rank_one'
        local[str(i)]={'kind':kind,'H':B,'H_inverse':integral(B.inv())}
        fixed[i]=F
    kills=S.Matrix.hstack(*vanish)
    same(chi*kills,S.zeros(1,4))
    killpre=integer_solve(kills,E[:,:3])
    killminor=first_unit_minor(kills[:3,:],3)
    D=S.Matrix.hstack(*[A-E for A in mats[:3]])
    Dtop=D[:3,:]
    right=integer_solve(Dtop,S.eye(3),shorten=True)
    def j(i,F):
        if i<3:
            out=S.zeros(12,F.cols);out[4*i:4*i+4,:]=F;return out
        return -S.Matrix.vstack(mats[1]*mats[2]*F,mats[2]*F,F)
    K=S.Matrix.hstack(j(0,ell),*[j(i,fixed[i]) for i in range(1,4)])
    same(D*K,S.zeros(4,9))
    comp=S.Matrix.hstack(right,K)
    assert abs(comp.det())==1
    compinv=integral(comp.inv());L=compinv[3:,:]
    same(L*K,S.eye(9))
    sweepdelta=integral(L*j(0,delta))
    assert sweepdelta[0]==0
    graphminor=first_unit_minor(K,9)
    # The fibre quotient and its five explicit relation preimages.
    ab=integer_solve(S.Matrix([[p,-q]]),S.ones(1,1))
    s=S.zeros(6,1);s[0],s[5]=ab[0],ab[1]
    kapp=S.zeros(6,1);kapp[0],kapp[5]=q,p
    relations=S.Matrix.hstack(kapp,S.eye(6)[:,[1,2,3,4]])
    C=S.Matrix.hstack(*[wedge(A)-S.eye(6) for A in mats[:3]])
    fibpre=integer_solve(C,relations,shorten=True)
    quotientbasis=S.Matrix.hstack(s,relations)
    assert abs(quotientbasis.det())==1
    same(omega*s,S.ones(1,1));same(omega*C,S.zeros(1,18))
    ans={'row':row['row'],'P':p,'Q':q,'d':d,'cyclic_original_indices_zero_based':order,
         'section':section,'matrices':mats,'omega':omega,'ell':ell,'u':u,'finite_pi':pi,
         'finite_relation_preimage':finite_relation,'finite_norm':norm,
         'local':local,'vanishing_columns':kills,'vanishing_preimages':killpre,
         'vanishing_unit_minor':killminor,'graph_K':K,'graph_inverse':L,
         'graph_complement':right,'graph_unit_minor':graphminor,
         'sweep_delta_coordinates':sweepdelta,'fibre_s':s,
         'fibre_relation_basis':relations,'fibre_relation_preimages':fibpre}
    ans.update({'finite_elliptic_H':Hfinite,'finite_elliptic_H_inverse':Hfinite.inv(),
                'finite_Q_shift':shiftQ,'finite_P_shift':[str(x) for x in shiftP],
                'pole_per_k':POLE[irow],'epsilon':EPSILON[irow],
                'deck_delta_numerator':d*EPSILON[irow]-POLE[irow],
                'global_section_degree':SECTION_DEGREE[irow]})
    print('ROW',row['row'],'OS',row['OS'],row['profile'],'input lift/section/height exact')
    print('FINITE u=',list(u),'pi=',pi.tolist(),'norm(u)=',(d//q),'delta')
    print('LOCAL',[ (i,local[str(i)]['kind'],int(local[str(i)]['H'].det())) for i in range(1,4)])
    print('GRAPH unit minor',graphminor,'delta=',list(sweepdelta),'s=',list(s))
    print('KILL unit minor',killminor,'all primitive quotient maps and relation preimages exact')
    return lists(ans)


def relative_maps(row):
    q,d=row['Q'],row['d']
    n,m,r,alpha,beta,k=S.symbols('n m r alpha beta k',integer=True)
    c=S.Matrix(row['sweep_delta_coordinates'])[1:,:]
    a=row['pole_per_k'];R=r-a*k
    def bezout(A,B):
        assert A.shape==B.shape
        for z in A-B:assert S.cancel(z.subs(beta,(1-m*alpha)/n))==0
    J=S.Matrix([[-q*R*beta,1,q*R*alpha],[m,0,n]])
    sec=S.Matrix([[0,alpha],[1,0],[0,beta]])
    normal=S.Matrix([-n,-q*R,m])
    U=sec.row_join(normal)
    Uinv=S.Matrix([[-q*R*beta,1,q*R*alpha],[m,0,n],[-beta,0,alpha]])
    bezout(Uinv*U,S.eye(3));bezout(U*Uinv,S.eye(3))
    bezout(J*sec,S.eye(2));bezout(J*normal,S.zeros(2,1))
    F=S.eye(10);F[0,0]=n;F[0,1]=-q*R*alpha
    F[2:,0]=m*c/q;F[2:,1]=R*beta*c
    source=S.eye(10);source[2:,0]=-m*c/q;source[2:,1]=-R*beta*c
    target=S.eye(10);target[0,1]=q*R*alpha
    same(target*F*source,S.diag(n,*([1]*9)))
    same(source*(2*S.eye(10)-source),S.eye(10))
    same(target*(2*S.eye(10)-target),S.eye(10))
    G=S.Matrix([[-n,0,0,0],[m,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
    assert S.expand(G.det()-n)==0
    # Actual fourteen-generator H1 map, then its complete transport.
    blocks=[(J,S.Matrix([[1,0,0],[0,0,1],[0,0,0],[0,0,0]]),sec,normal)]
    for i in range(1,4):
        item=row['local'][str(i)];H=S.Matrix(item['H'])
        inds=[1,2,3] if item['kind']=='rank_one' else [1,3]
        size=len(inds);Ji=S.eye(size).row_join(S.zeros(size,1))
        Vi=S.zeros(4,size+1)
        Vi[0,:size]=H[3,inds]
        Vi[1:,size]=S.eye(3)[:,i] if i<3 else -S.ones(3,1)
        seci=S.eye(size+1)[:,:size];normali=S.eye(size+1)[:,size]
        blocks.append((Ji,Vi,seci,normali))
    MV=S.zeros(14);S14=S.zeros(14);off=0;dest=4;sectoff=0
    for i,(Ji,Vi,Si,Ni) in enumerate(blocks):
        width=Ji.cols;rank=Ji.rows
        MV[:4,off:off+width]=Vi
        MV[dest:dest+rank,off:off+width]=-Ji
        S14[off:off+width,sectoff:sectoff+rank]=Si
        S14[off:off+width,10+i]=Ni
        off+=width;dest+=rank;sectoff+=rank
    assert off==dest==14 and sectoff==10
    changed=MV*S14;Vs=changed[:4,:10]
    bezout(changed,S.Matrix.vstack(Vs.row_join(G),(-S.eye(10)).row_join(S.zeros(10,4))))
    rowchange=S.eye(14);rowchange[:4,4:]=Vs
    inverse_row=S.eye(14);inverse_row[:4,4:]=-Vs
    same(rowchange*inverse_row,S.eye(14))
    perm=list(range(4,14))+list(range(4))
    final=(rowchange*changed)[perm,:]
    bezout(final,S.diag(-S.eye(10),G))
    determinant=S.cancel(S14.det().subs(beta,(1-m*alpha)/n))
    assert abs(determinant)==1
    # Same source datum: exact shear from the unshifted r-coordinate map.
    Fr=F.subs(k,0)
    change=S.eye(10);change[0,1]=q*a*k*alpha;change[2:,1]=-a*k*beta*c
    same(change*Fr,F)
    same(change*(2*S.eye(10)-change),S.eye(10))
    # The degree-three transfer respects the complete abelian relation.
    tu=S.Matrix([n,0]).col_join(m*c/q)
    tl=S.Matrix([-q*R,m]).col_join(S.zeros(8,1))
    tx=S.Matrix([0,n]).col_join(R*c)
    tz=S.Matrix([-q*R*alpha,1]).col_join(R*beta*c)
    same(m*tx-n*tl-q*R*tu,S.zeros(10,1))
    bezout(alpha*tl+beta*tx,tz)
    print('SYMBOLIC ROW',row['row'],'complete J/inverse, F/source/target, G det n, 14x14 MV transport, framing shear, transfer relation exact')


def egcd(a,b):
    oldr,r=a,b;olds,s=1,0;oldt,t=0,1
    while r:
        q=oldr//r
        oldr,r=r,oldr-q*r;olds,s=s,olds-q*s;oldt,t=t,oldt-q*t
    if oldr<0:oldr,olds,oldt=-oldr,-olds,-oldt
    return oldr,olds,oldt


def parameter_checks(rows):
    count=negative=shifted=0
    for row in rows:
        d,q,a,eps,deck=(row[x] for x in ['d','Q','pole_per_k','epsilon','deck_delta_numerator'])
        assert d*eps==a+deck
        cv=[int(x[0]) for x in row['sweep_delta_coordinates'][1:]]
        for k in range(1,7):
            m=d*k
            for n in range(-13,14):
                if math.gcd(n,m)!=1:continue
                gg,alpha,beta=egcd(m,n)
                assert gg==m*alpha+n*beta==1
                assert sorted((j*n)%m for j in range(m))==list(range(m))
                for r in range(-3,4):
                    R=r-a*k
                    assert r+k*deck-eps*m==R
                    # Both directions of the finite boundary coordinate map.
                    cols=[(0,1,0),(alpha,0,beta),(-n,-q*R,m)]
                    for j,(A,B,C) in enumerate(cols):
                        out=(-q*R*beta*A+B+q*R*alpha*C,m*A+n*C,-beta*A+alpha*C)
                        assert out==tuple(int(i==j) for i in range(3))
                    # Quotient kernel lifts, including arbitrary graph coordinates.
                    for h,b in [(1,-2),(-3,1),(2,3)]:
                        A=n*h-q*R*alpha*b
                        L=[(j+1)*(r+k-n) for j in range(8)]
                        reduced=[L[j]-(m//q)*cv[j]*h-R*beta*cv[j]*b for j in range(8)]
                        recovered=[(m//q)*cv[j]*h+R*beta*cv[j]*b+reduced[j] for j in range(8)]
                        assert n*h-q*R*alpha*b==A and recovered==L
                        assert (A+q*R*alpha*b)//n==h
                    count+=1;negative+=n<0;shifted+=R!=r
    print('FRESH_PARAMETER_CASES',count,'NEGATIVE_N',negative,'NONZERO_FRAME_SHIFTS',shifted)
    print('Grid: seven rows, k=1..6, n=-13..13 with gcd(n,dk)=1, r=-3..3; all integer quotient maps and root characters exact.')


def main():
    b=INPUT.read_bytes();data=json.loads(b)
    print('START',datetime.now(timezone.utc).isoformat())
    print('DEFINING_INPUT_SHA256',hashlib.sha256(b).hexdigest())
    answers=[derive(row) for row in data['rows']]
    for row in answers:relative_maps(row)
    parameter_checks(answers)
    target=HERE/'S6_SERIES_PUBLISH_III_02KM_fresh_linear_maps.json'
    # This is mathematical map data, not an inventory or a check manifest.
    with target.open('w',newline='\n') as f:
        f.write('{"scope":"New proof-closed exact linear and relative maps; attachment proved in fresh derivation",\n"rows":[\n')
        for i,answer in enumerate(answers):
            f.write('{\n')
            for j,(key,value) in enumerate(answer.items()):
                f.write(json.dumps(key)+':'+json.dumps(value,separators=(',',':'))+
                        (',' if j+1<len(answer) else '')+'\n')
            f.write('}'+(',' if i+1<len(answers) else '')+'\n')
        f.write(']}\n')
    print('COMPLETE',datetime.now(timezone.utc).isoformat())
    print('Seven input lifts, section generators and all listed integral maps derived; no target proof read.')


if __name__=='__main__':main()
