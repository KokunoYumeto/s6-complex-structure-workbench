"""Integral local/global lattices for the corrected fourfold E.1.

This records exact algebra for an ongoing Leray calculation; no total
integral homology conclusion is inferred without the geometric maps.
"""
from itertools import combinations
from sympy import Matrix, eye, zeros, diag, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

def snf(R):
    return tuple(X.to_Matrix() for X in smith_normal_decomp(
        DomainMatrix.from_Matrix(R).convert_to(ZZ)))

def kernel(R):
    D,U,V=snf(R)
    K=V[:,R.rank():]
    assert R*K==zeros(R.rows,K.cols)
    return K

def ext(M,q):
    ids=list(combinations(range(M.rows),q))
    return Matrix([[M.extract(i,j).det() for j in ids] for i in ids])

def factors(R):
    D,U,V=snf(R)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]

A1=Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
C1=Matrix([[-1,-1],[1,0]])
C2=Matrix([[0,1],[-1,0]])
M1=diag(A1,C1);M2=diag(A2,C2);M0=(M1*M2).inv()
v1=Matrix([1,2,-4,0,0,0]);v2=Matrix([-1,-3,3,0,0,0])
# Cohomology may use transposes instead of inverse transposes for
# individual kernels/images. Simultaneous invariants/coinvariants are
# unchanged; peripheral restriction expressions below use the actual
# inverse-transpose representation for the ordered product.
T1=M1.inv().T;T2=M2.inv().T;T0=M0.inv().T
assert T1*T2*T0==eye(6)
for q in range(7):
    AA,BB,CC=ext(T1,q),ext(T2,q),ext(T0,q)
    n=AA.rows
    cob=Matrix.vstack(AA-eye(n),BB-eye(n))
    rel=Matrix.hstack(AA-eye(n),BB-eye(n))
    print('q',q,'global inv',n-cob.rank(),'coinv free',n-rel.rank(),
          'coinv torsion',[x for x in factors(rel) if x>1],
          'cob torsion',[x for x in factors(cob) if x>1])
    dd,uu,vv=snf(cob)
    for i in range(min(dd.shape)):
        if abs(dd[i,i])<=1:continue
        w=vv[:,i]/dd[i,i]
        flags=[]
        for TT in (AA,BB,CC):
            d,u,v=snf(TT-eye(n));z=u*(TT-eye(n))*w
            flags.append(all((z[j]/d[j,j]).q==1 if d[j,j] else z[j]==0
                             for j in range(n)))
        print('  cob torsion locally trivial',flags)
        if q==2:
            order=abs(int(dd[i,i]));orders=[]
            for TT in (AA,BB,CC):
                d,u,v=snf(TT-eye(n));z=u*(TT-eye(n))*w
                orders.append(next(a for a in range(1,order+1) if all(
                    (a*z[j]/d[j,j]).q==1 if d[j,j] else a*z[j]==0
                    for j in range(n))))
            assert orders==[3,2,1]
            print('  q2 torsion restriction orders',orders)

for M,T,v,m in ((M1,T1,v1,3),(M2,T2,v2,4)):
    P=eye(6);P[:,0]=v/v[0]
    assert P.det()==1
    MM=P.inv()*M*P
    assert MM[0,0]==1 and MM[0,1:]==zeros(1,5) and MM[1:,0]==zeros(5,1)
    D=MM[1:,1:]
    print('finite order',m,'adapted basis',P,'vertical D',D)
    for q in range(1,7):
        W=ext(D.inv().T,q-1);local=W-eye(W.rows)
        dl,ul,vl=snf(local)
        print(' finite Hq torsion',q,[x for x in factors(local) if x>1])
        # A torsion suspension representative in the adapted vertical
        # covectors embeds back via P^{-t}, then into global coinvariants.
        ids=list(combinations(range(6),q-1))
        vid=list(combinations(range(5),q-1))
        change=ext(P.inv().T,q-1)
        AA,BB=ext(T1,q-1),ext(T2,q-1)
        dg,ug,vg=snf(Matrix.hstack(AA-eye(AA.rows),BB-eye(BB.rows)))
        for i in range(min(dl.shape)):
            if abs(dl[i,i])<=1:continue
            w=ul.inv()[:,i]
            emb=Matrix([0 if 0 in s else w[vid.index(tuple(j-1 for j in s))]
                        for s in ids])
            z=ug*change*emb
            tors=[(abs(int(dg[j,j])),int(z[j])%abs(int(dg[j,j])))
                  for j in range(min(dg.shape)) if abs(dg[j,j])>1]
            free=[z[j] for j in range(AA.rows) if not dg[j,j]]
            assert all(x==0 for x in free)
            print('  torsion d2 representative',list(w),'global torsion residues',tors)

# The degree-three covering cokernels are computed without choosing a
# splitting of either Wang sequence: their horizontal inclusion is the
# isomorphism ker(D on wedge^2)/Norm -> covering cokernel.  All global
# invariant three-forms are horizontal in both adapted splittings.
K3=kernel(Matrix.vstack(ext(T1,3)-eye(20),ext(T2,3)-eye(20)))
print('global invariant three-form basis',K3)
idx3=list(combinations(range(6),3));idx2=list(combinations(range(5),2))
norms=[];ims=[]
for M,v,m in ((M1,v1,3),(M2,v2,4)):
    P=eye(6);P[:,0]=v/v[0]
    D=(P.inv()*M*P)[1:,1:].inv().T
    TT=ext(D,2);N=sum((TT**i for i in range(m)),zeros(10))
    J=kernel(TT-eye(10))
    norm=J.gauss_jordan_solve(N)[0]
    Kp=ext(P.T,3)*K3
    assert all(Kp[i,j]==0 for i,s in enumerate(idx3) if 0 not in s
               for j in range(K3.cols))
    beta=Matrix([[Kp[idx3.index((0,)+tuple(i+1 for i in s)),j]
                  for j in range(K3.cols)] for s in idx2])
    im=J.gauss_jordan_solve(beta)[0]
    assert all(x.q==1 for x in norm) and all(x.q==1 for x in im)
    norms.append(norm);ims.append(im)
    print('finite q3 cokernel order',m,'norm matrix',norm,
          'global image',im,'Smith factors',factors(norm))
    TT1=D;N1=sum((TT1**i for i in range(m)),zeros(5))
    J1=kernel(TT1-eye(5))
    norm1=J1.gauss_jordan_solve(N1)[0]
    assert factors(norm1)==([1] if m==3 else [2])
    print('finite q2 covering cokernel Smith factors',m,factors(norm1))
R=Matrix.hstack(diag(*norms),Matrix.vstack(*ims))
assert factors(R)==[1]*8
print('combined finite q3 cokernels modulo global invariants',factors(R))

# Primitive target summands for the natural transgressions.
X1=A1.inv().T;X2=A2.inv().T
Y1=C1.inv().T;Y2=C2.inv().T
from sympy import kronecker_product
for label,Z1,Z2,rank in (
    ('X q1',X1,X2,1),
    ('X q2',ext(X1,2),ext(X2,2),1),
    ('E q1',Y1,Y2,0),
    ('mixed Xq1 Eq1',kronecker_product(X1,Y1),
     kronecker_product(X2,Y2),0)):
    rel=Matrix.hstack(Z1-eye(Z1.rows),Z2-eye(Z2.rows))
    assert Z1.rows-rel.rank()==rank and all(x==1 for x in factors(rel))
    print('primitive target',label,'free rank',rank,'Smith factors',factors(rel))

print('All exact assertions passed. Integral homology proof uses these lattices,')
print('the natural transgressions from X, the elliptic section, UCT and duality.')
