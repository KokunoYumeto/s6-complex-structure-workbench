"""Bounded 2-neighbor search for primitive-cusp (5,12) lattices.

At each vertex we exhaust every A-stable F2 subspace: A has the
semisimple decomposition F2^2 plus the irreducible degree-four Phi5
module. There are ten such subspaces. We retain B-stable ones with
square-zero N acyclic, which exactly preserves cusp primitivity for
the corresponding one-step overlattice. The breadth-first depth
bound is four; this is not a complete classification of lattices.
"""
from sympy import Matrix, eye, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from itertools import combinations

A=Matrix([[1,0,0,0,0,0],[0,1,0,1,0,0],[0,1,0,0,0,0],
          [0,-1,0,0,1,1],[0,1,-1,0,-1,0],[0,0,1,0,0,0]])
B=Matrix([[1,0,0,0,1,0],[0,0,1,0,0,0],[0,0,0,0,0,1],
          [0,1,-2,0,0,0],[0,0,1,0,-1,-1],[0,0,0,1,1,2]])
def factors(T):
    D=smith_normal_form(T,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
def reduced_rows(T):
    a=[[int(x)%2 for x in T.row(i)] for i in range(T.rows)]
    piv=[];r=0
    for c in range(T.cols):
        j=next((j for j in range(r,len(a)) if a[j][c]),None)
        if j is None:continue
        a[r],a[j]=a[j],a[r]
        for k in range(len(a)):
            if k!=r and a[k][c]:a[k]=[x^y for x,y in zip(a[k],a[r])]
        piv.append(c);r+=1
        if r==len(a):break
    return Matrix(a),piv
def basis(T):
    R,p=reduced_rows(T.T)
    return R[:len(p),:].T
def rank(T):return len(reduced_rows(T)[1])
def kernel(T):
    R,p=reduced_rows(T);free=[i for i in range(T.cols) if i not in p];out=[]
    for i in free:
        v=zeros(T.cols,1);v[i]=1
        for j,c in enumerate(p):v[c]=R[j,i]
        out.append(v)
    return Matrix.hstack(*out) if out else zeros(T.cols,0)
def exterior(T,q):
    ix=list(combinations(range(T.rows),q))
    return Matrix([[T.extract(i,j).det() for j in ix] for i in ix])
def signature(C,D):
    out=[]
    for q in range(1,4):
        X,Y=exterior(C,q),exterior(D,q);n=X.rows
        out.append(tuple(factors(Matrix.hstack(X-eye(n),Y-eye(n)))))
    return tuple(out)

queue=[(A,B,eye(6),0)];seen=set();count=0
while queue:
    C,D,Q,depth=queue.pop(0)
    key=tuple(Q)
    if key in seen:continue
    seen.add(key);count+=1
    assert factors(C*D-eye(6))==[1,1,1]
    print('vertex',count,'depth',depth,'basis',Q,'coinvariant signature',signature(C,D))
    if depth==4:continue
    F=kernel(C-eye(6));E=basis(C-eye(6))
    assert F.cols==2 and E.cols==4
    us=[zeros(6,0),F[:,0:1],F[:,1:2],basis(F[:,0:1]+F[:,1:2]),F]
    children=0
    for U in us:
        for X in [zeros(6,0),E]:
            S=basis(Matrix.hstack(U,X));d=S.cols
            if d in (0,6) or d%2:continue
            if rank(Matrix.hstack(S,D*S))!=d:continue
            if rank((C*D-eye(6))*S)!=d//2:continue
            H=hermite_normal_form(Matrix.hstack(2*eye(6),S))/2
            C1=H.inv()*C*H;D1=H.inv()*D*H
            assert all(x.q==1 for x in C1) and all(x.q==1 for x in D1)
            assert factors(C1*D1-eye(6))==[1,1,1]
            Q1=Q*H
            # Normalize a common scalar so homothetic lattices have one key.
            vals=[x for x in Q1 if x]
            from sympy import ilcm,igcd
            den=1
            for x in vals:den=ilcm(den,int(x.q))
            ints=[int(x*den) for x in Q1];g=0
            for x in ints:g=igcd(g,x)
            Q1=hermite_normal_form(Matrix(6,6,ints)/g)
            C1=Q1.inv()*A*Q1;D1=Q1.inv()*B*Q1
            queue.append((C1,D1,Q1,depth+1));children+=1
    print('primitive-cusp nonhomothetic neighbors generated',children)
print('total distinct normalized lattices through depth four',count)
