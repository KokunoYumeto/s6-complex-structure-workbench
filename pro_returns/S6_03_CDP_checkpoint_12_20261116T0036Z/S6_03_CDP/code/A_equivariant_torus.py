"""Integral lattice checks for the equivariant Seifert construction UN35.

The H1-vanishing proof uses actual norm tori and restriction/corestriction.
These matrices certify the claimed cyclic lattice models and the exact
linear lift of elliptic automorphisms to (C*)^2.
"""
import sympy as s

I=s.eye(2)
models={
    1:I,
    2:-I,
    3:s.Matrix([[0,-1],[1,-1]]),
    4:s.Matrix([[0,-1],[1,0]]),
    6:s.Matrix([[0,-1],[1,1]]),
}
for n,M in models.items():
    assert M.det()==1
    assert M**n==I
    assert all(M**k!=I for k in range(1,n))
    if n>1:
        assert sum((M**k for k in range(n)),s.zeros(2))==s.zeros(2)
    print(f'order {n}: M={list(M)}; det=1; exact order verified')

# The augmentation quotient Z[C3]/Z(1+g+g^2) has basis [1],[g].
assert models[3]*s.Matrix([1,0])==s.Matrix([0,1])
assert models[3]*s.Matrix([0,1])==s.Matrix([-1,-1])
print('order 3: exact cyclic norm-one character lattice verified')

# Ind_{C2}^{C4}(sign), basis e,g e: g^2 e=-e.
assert models[4]**2==-I
print('order 4: exact induced quadratic norm-one lattice verified')

P=s.Matrix([[1,-1],[0,1]])
assert P.det()==1
assert P.inv()*models[6]**2*P==models[3]
assert models[6]**3==-I
print('order 6: degree-two restriction is order-3 norm lattice; '
      'degree-three restriction is two sign lattices')
assert 3-2==1
print('restriction/corestriction indices 2 and 3 have gcd 1')

# For a CM period tau, the row (1,tau) defines the elliptic quotient.
tau=s.Symbol('tau')
for n,poly in [(3,tau**2+tau+1),(4,tau**2+1),(6,tau**2-tau+1)]:
    M=models[n]
    row=s.Matrix([[1,tau]])
    diff=row*M-tau*row
    assert all(s.rem(x,poly,tau)==0 for x in diff)
    kernel=s.Matrix([-tau,1])
    inv_tau={3:-1-tau,4:-tau,6:1-tau}[n]
    diff=M*kernel-inv_tau*kernel
    assert all(s.rem(x,poly,tau)==0 for x in diff)
    print(f'order {n}: quotient character tau and additive-kernel '
          'character tau^(-1) verified')
print('PASS: all integral and polynomial identities')
