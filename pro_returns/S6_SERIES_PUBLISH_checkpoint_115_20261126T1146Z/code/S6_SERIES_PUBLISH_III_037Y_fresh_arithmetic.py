#!/usr/bin/env python3
"""Fresh exact sublattice and global-scope arithmetic for III 037Y."""
import sympy as s

n=s.symbols('n',integer=True,positive=True)
I=s.eye(4)
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0=s.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
S=s.diag(1,1,n,n)
g,u,w,d=[I[:,j] for j in range(4)]
assert A2*u==w
assert A1*u==-w+d
assert S.inv()*A2*S*u==s.Matrix([0,0,1/n,0])
assert S.inv()*A1*S*u==s.Matrix([0,0,-1/n,1/n])
assert S.det()==n*n
print('PASS: A2*u=w and A1*u=-w+delta have cover-basis short coefficients 1/N and (-1/N,1/N); index is N^2')

K=M0-I
assert K*K==s.zeros(4)
MN=I+n*K
assert (MN*S-S*M0).applyfunc(s.simplify)==s.zeros(4)
assert S.subs(n,1)==I
assert A1.det()==A2.det()==1
print('PASS: changed cusp clutch M0^N*S_N=S_N*M0; N=1 is the full original lattice and identity marking')

entries=s.symbols('b0:16',integer=True)
B=s.Matrix(4,4,entries)
congruence=I+n*B
expected=(s.eye(2)+n*B[:2,:2]).row_join(n*n*B[:2,2:])
expected=expected.col_join(B[2:,:2].row_join(s.eye(2)+n*B[2:,2:]))
assert (S.inv()*congruence*S-expected).applyfunc(s.expand)==s.zeros(4)
assert all(expr.is_polynomial(n,*entries) for expr in expected)
print('PASS: every actual GL4(Z) monodromy matrix congruent to I mod N preserves the cover lattice, with explicit integral cover-basis matrix')

assert s.factor(n*n-1)==(n-1)*(n+1)
assert s.factor(n**3-n*n)==n*n*(n-1)
for N in range(1,9):
    in_cover=(S.inv()*A2*S*u).subs(n,N)
    integral=all(v.q==1 for v in in_cover)
    assert integral==(N==1)
print('PASS: original-base witness fails for every sampled N=2,...,8 and holds at N=1; general exclusion is the exact coefficient 1/N')
print('ALL FRESH 037Y ARITHMETIC PASSED; target paragraph remains closed.')
