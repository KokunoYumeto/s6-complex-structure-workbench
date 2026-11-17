"""Exact invariant intersection forms for C.2.UN.36.

The matrices act on an oriented homology basis e1,...,e4 of a real
four-torus.  Both oriented rank-two nilpotent forms are retained.
No realization claim is inferred from these linear-algebra checks.
"""
from itertools import combinations
import sympy as s

pairs=list(combinations(range(4),2))
labels=[''.join(str(x+1) for x in p) for p in pairs]

def sign(perm):
    return (-1)**sum(perm[i]>perm[j]
                     for i in range(len(perm))
                     for j in range(i+1,len(perm)))

Q=s.zeros(6)
for a,p in enumerate(pairs):
    for b,q in enumerate(pairs):
        if len(set(p+q))==4:
            Q[a,b]=sign(p+q)
assert Q.det()==-1
assert Q**2==s.eye(6)

def exterior2(U):
    return s.Matrix(6,6,lambda i,j: U.extract(pairs[i],pairs[j]).det())

def inertia(G):
    p=q=z=0
    for val,mult in G.eigenvals().items():
        if val==0: z+=mult
        elif val.is_positive: p+=mult
        elif val.is_negative: q+=mult
        else: raise AssertionError(f'undetermined exact eigenvalue {val}')
    return p,q,z

N1=s.zeros(4); N1[0,1]=1
Nplus=N1.copy(); Nplus[2,3]=1
Nminus=N1.copy(); Nminus[2,3]=-1
rows=[('zero',s.zeros(4),(3,3,0)),
      ('rank-one',N1,(1,1,2)),
      ('rank-two-positive',Nplus,(1,2,1)),
      ('rank-two-negative',Nminus,(2,1,1))]

print('Oriented wedge basis:',labels)
print('Torus intersection form:'); print(Q)
for name,N,expected in rows:
    U=s.eye(4)+N
    assert N**2==s.zeros(4)
    assert U.det()==1
    W=exterior2(U)
    assert W.T*Q*W==Q
    basis=(W-s.eye(6)).nullspace()
    B=s.Matrix.hstack(*basis)
    G=B.T*Q*B
    got=inertia(G)
    assert got==expected
    assert (W-s.eye(6))*B==s.zeros(6,len(basis))
    print(f'\n{name}: rank N={N.rank()}, dim invariants={len(basis)}, '
          f'inertia (+,-,radical)={got}')
    print('Invariant basis columns:'); print(B)
    print('Restricted form:'); print(G)

# The displayed rank-two basis has its last square equal to -2 epsilon.
for eps in [1,-1]:
    B=s.zeros(6,4)
    B[labels.index('12'),0]=1
    B[labels.index('34'),1]=1
    B[labels.index('13'),2]=1
    B[labels.index('14'),3]=1
    B[labels.index('23'),3]=-eps
    G=B.T*Q*B
    assert G==s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,-2*eps]])
print('\nExplicit rank-two basis (12,34,13,14-epsilon*23) verified.')
print('Boundary rank bounds: K3 with n blowups >=16+n; '
      'Enriques or chi=1 elliptic with n blowups >=6+n.')
print('PASS: all exact matrix identities and inertias.')
