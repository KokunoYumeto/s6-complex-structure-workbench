"""Exact cusp exterior-lattice certificate, extracted from the supplied v1 audit.
This checks only the integral-generation assertion of maps E.1.3.
No finite-filling or global-homology credit is inferred.
"""
from itertools import combinations, combinations_with_replacement
from sympy import Matrix, eye, zeros, ZZ, binomial, sqrt, gcd
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

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

