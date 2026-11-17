"""Exact integral homology certificates for parameter v=1 of F.2.16.

This is a second explicit pair, using the method of fourfolds_nonselfdual.py.
The quotient W is not self-dual: its two pencil determinants are 0 and 2.
The monomial basis below was found in the finite cube {-1,0,1}^5 (242
nonzero vectors and eight minus-eigenvectors, first certificate at test57);
its displayed determinant and intertwining identity are checked exactly.
All subsequent exterior and Smith computations are exhaustive finite
linear algebra in degrees0..6. No general parameter search is claimed.
"""
from itertools import combinations, combinations_with_replacement
from sympy import Matrix, eye, zeros, ZZ, binomial, sqrt, gcd
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

A = Matrix([
    [1,0,0,1,-1,1], [0,1,-1,-1,1,0], [0,1,0,-1,0,0],
    [0,2,-1,-1,0,1], [0,2,0,-1,0,0], [0,1,1,-1,0,0]])
B = Matrix([
    [1,0,0,0,0,0], [0,0,-1,0,1,-1], [0,0,-1,0,0,0],
    [0,0,-2,0,1,-2], [0,1,-2,0,1,-3], [0,0,-1,1,0,-1]])
M1, M2 = A.T, B.T
M0 = (M1*M2).inv()
v1 = Matrix([1,3,-2,-1,2,0])
v2 = Matrix([-1,0,0,0,0,0])

def snf(R):
    return tuple(X.to_Matrix() for X in smith_normal_decomp(
        DomainMatrix.from_Matrix(R).convert_to(ZZ)))

def kernel(R):
    D,U,V = snf(R)
    K = V[:,R.rank():]
    assert R*K == zeros(R.rows,K.cols)
    return K

def exterior(M,q):
    inds = list(combinations(range(M.rows),q))
    return Matrix([[M.extract(i,j).det() for j in inds] for i in inds])

def smith_factors(R):
    D = smith_normal_form(R,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]

assert A**5 == eye(6) and B**4 == eye(6)
assert all(A**i != eye(6) for i in range(1,5))
assert all(B**i != eye(6) for i in range(1,4))
assert M1*M2*M0 == eye(6)
N = M0-eye(6)
assert N*N == zeros(6) and N.rank() == 3
assert smith_factors(N) == [1,1,1]
assert M1*v1 == v1 and M2*v2 == v2
ell = Matrix([[1,0,0,0,0,0]])
assert ell*M1 == ell and ell*M2 == ell
assert ell*v1 == Matrix([1]) and ell*v2 == Matrix([-1])
print("M1 =",M1)
print("M2 =",M2)
print("M0 =",M0)
print("twists",list(v1),list(v2),"multiplicities",5,4)
print("cusp Smith factors",smith_factors(N))
print("cohomology common invariant rank",kernel(Matrix.vstack(A-eye(6),B-eye(6))).cols)
print("cohomology global coinvariant Smith factors",
      smith_factors(Matrix.hstack(A-eye(6),B-eye(6))))

# Normal closure of cusp vanishing cycles: these finitely many words suffice.
K = hermite_normal_form(Matrix.hstack(N,M1*N,M2*N))
assert K == eye(6)[:,1:]
assert M1*K == K*(M1[1:,1:]) and M2*K == K*(M2[1:,1:])
print("cusp normal closure lattice basis =",K)
print("residual pi1 abelian relation Smith factors",
      smith_factors(Matrix([[5,0,-1],[0,4,1],[1,1,0]])))

# Exact rational Leray input, including the degree-four cusp kernel.
h0=[]; h1=[]; h2=[]
for q in range(7):
    AA,BB,CC = exterior(A,q),exterior(B,q),exterior(A*B,q)
    n=AA.rows
    aa=n-Matrix.vstack(AA-eye(n),BB-eye(n)).rank()
    bb=n-Matrix.hstack(AA-eye(n),BB-eye(n)).rank()
    local=[n-(T-eye(n)).rank() for T in (AA,BB,CC)]
    pp=aa+bb-(-n+sum(local))
    h0.append(aa);h1.append(pp);h2.append(bb)
    print("degree",q,"global inv/coinv",aa,bb,
          "local invariant ranks",local,"parabolic H1",pp)
assert h0 == [1,1,0,0,0,0,1]
assert h1 == [0,0,0,3,0,0,0]
assert h2 == [1,0,0,0,0,1,1]

# Finite filling groups and covering lattices in degrees two and three.
for M,m,v,C in ((M1,5,v1,A),(M2,4,v2,B)):
    R=zeros(7);R[:6,:6]=M-eye(6);R[:6,6]=-v;R[6,6]=m
    print("finite H1 Smith",m,smith_factors(R))
    D=M[1:,1:]
    for q in range(1,5):
        print("finite mapping-torus vertical coinvariants",m,q,
              smith_factors(exterior(D,q)-eye(int(binomial(5,q)))))
    # q=2: periods on vertical cycles and on the commuting torus (a,lambda).
    lam=Matrix([0]+list(kernel(D-eye(5))[:,0]))
    K2=kernel(exterior(C,2)-eye(15))
    i2=list(combinations(range(6),2))
    pair=Matrix([[v[i]*lam[j]-v[j]*lam[i] for i,j in i2]])*K2
    assert all(int(x)%m == 0 for x in pair)
    print("finite q2 suspension periods divided by m",m,[x/m for x in pair])
    # q=3: determinant of the middle skew pairing gives the covering index.
    i3=list(combinations(range(6),3));J=zeros(20)
    for i,s in enumerate(i3):
        t=tuple(k for k in range(6) if k not in s);j=i3.index(t)
        z=s+t
        J[i,j]=(-1)**sum(z[k]>z[l] for k in range(6) for l in range(k+1,6))
    K3=kernel(exterior(C,3)-eye(20));G=K3.T*J*K3
    assert G.det() == m**4
    print("finite q3 invariant Gram",m,G,"covering index",m**2/sqrt(G.det()))
    i4=list(combinations(range(6),4));J24=zeros(15)
    for i,s in enumerate(i2):
        t=tuple(k for k in range(6) if k not in s);j=i4.index(t)
        z=s+t
        J24[i,j]=(-1)**sum(z[k]>z[l] for k in range(6) for l in range(k+1,6))
    K4=kernel(exterior(C,4)-eye(15));G24=K2.T*J24*K4
    assert abs(G24.det())==m**3
    print("finite q2-q4 Gram",m,G24,"q4 covering index",m**3/abs(G24.det()))

# The only group-cohomology torsion in degree-two/three coefficient systems
# is Z/2, and its restriction to the order-four peripheral circle is nonzero.
for q in (2,3,4):
    AA,BB=exterior(A,q),exterior(B,q);n=AA.rows
    delta=Matrix.vstack(AA-eye(n),BB-eye(n))
    D,U,V=snf(delta)
    tors=[i for i in range(n) if abs(D[i,i])>1]
    print("parabolic coefficient degree",q,"delta Smith factors",smith_factors(delta))
    for i in tors:
        w=V[:,i]/D[i,i]
        local_trivial=[]
        for T in (AA,BB,(AA*BB).inv()):
            d,u,v=snf(T-eye(n));z=u*(T-eye(n))*w
            local_trivial.append(all(
                (z[j]/d[j,j]).q==1 if d[j,j] else z[j]==0
                for j in range(n)))
        assert not all(local_trivial)
        print("torsion local-trivial flags",local_trivial)

# Integral generation of all cusp invariant exterior lattices.
def wedge(x,y):
    z={}
    for s,cs in x.items():
        for t,ct in y.items():
            if set(s)&set(t):continue
            u=s+t
            sign=(-1)**sum(u[i]>u[j] for i in range(len(u)) for j in range(i+1,len(u)))
            key=tuple(sorted(u));z[key]=z.get(key,0)+sign*cs*ct
    return {s:c for s,c in z.items() if c}

odd=[{(i+3,):1} for i in range(3)]
even=[]
for i in range(3):
    for j in range(i,3):
        even.append({(i,j+3):1} if i==j else {(i,j+3):1,(j,i+3):1})
Uc=eye(6)
Uc[3:,:3]=eye(3)  # cohomology: a_i -> a_i+b_i
for q in range(7):
    inds=list(combinations(range(6),q));n=len(inds)
    K=kernel(exterior(Uc,q)-eye(n));columns=[]
    for aa in range(4):
        if aa>q or (q-aa)%2:continue
        bb=(q-aa)//2
        for os in combinations(range(3),aa):
            for es in combinations_with_replacement(range(6),bb):
                w={():1}
                for i in os:w=wedge(w,odd[i])
                for i in es:w=wedge(w,even[i])
                columns.append(Matrix([w.get(s,0) for s in inds]))
    G=Matrix.hstack(*columns)
    coords=K.gauss_jordan_solve(G)[0]
    assert all(x.q==1 for x in coords)
    factors=smith_factors(coords)
    assert factors == [1]*K.cols
    print("cusp degree",q,"rank",K.cols,"monomials",len(columns),"Smith factors",factors)

# The order-four filling is a mapping torus of a monomial matrix.
# This fixed unimodular basis is a certificate, not an unbounded search.
D=M2[1:,1:]
P=Matrix([[-1,1,-1,0,-1],[-1,2,-1,0,-1],[-1,0,0,2,-1],
          [1,-1,0,-1,1],[0,0,2,-1,1]])
monomial=Matrix([[0,0,0,1,0],[1,0,0,0,0],[0,1,0,0,0],
                 [0,0,1,0,0],[0,0,0,0,-1]])
assert abs(P.det())==1 and D*P==P*monomial
print("Order-four vertical monomial conjugacy certificate",P)

# Torsion-cap d2: the boundary inclusion takes the torsion suspension
# class to the same vertical coinvariant, then to global coinvariants.
# The proof of this identification is given in F.2.5.
for q in range(2,6):
    p=q-1
    T=exterior(B[1:,1:],p)
    d,u,v=snf(T-eye(T.rows))
    tors=[i for i in range(T.rows) if abs(d[i,i])>1]
    assert len(tors)==1 and abs(d[tors[0],tors[0]])==2
    w=u.inv()[:,tors[0]]
    inds=list(combinations(range(6),p))
    vertical=list(combinations(range(5),p))
    wf=Matrix([0 if 0 in s else
               w[vertical.index(tuple(i-1 for i in s))] for s in inds])
    AA,BB=exterior(A,p),exterior(B,p)
    dg,ug,vg=snf(Matrix.hstack(AA-eye(AA.rows),BB-eye(BB.rows)))
    gtors=[i for i in range(AA.rows) if abs(dg[i,i])>1]
    assert len(gtors)==1 and abs(dg[gtors[0],gtors[0]])==2
    image=ug*wf
    assert int(image[gtors[0]])%2==1
    print("torsion transgression degree",q,
          "local representative",list(w),
          "global Z/2 residue",int(image[gtors[0]])%2)

print("All exact assertions passed. Integral H2=H3=0 follows from the stated d2 identification.")
print("Bounded-cusp periods follow separately from F.3.11; simultaneous finite holomorphic caps are not asserted here.")
