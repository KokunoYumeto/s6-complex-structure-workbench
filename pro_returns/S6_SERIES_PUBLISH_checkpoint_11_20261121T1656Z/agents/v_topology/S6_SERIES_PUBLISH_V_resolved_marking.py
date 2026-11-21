#!/usr/bin/env python3
"""Small post-proof-read arithmetic checks supporting notation clarification."""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

I4 = s.eye(4)
A1 = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
v1, v2 = s.Matrix([1,2,-4,0]), s.Matrix([-1,-3,3,0])
C1, C2 = s.Matrix([[-1,-1],[1,0]]), s.Matrix([[0,1],[-1,0]])
DX1 = s.Matrix([[0,1,0],[-1,-1,0],[1,0,1]])
DX2 = s.Matrix([[0,-1,0],[1,0,0],[0,1,1]])
for j, A, v, D, m in ((1,A1,v1,DX1,3),(2,A2,v2,DX2,4)):
    U = s.Matrix.hstack(v/v[0], I4[:,1:])
    assert U.det() == 1
    assert U.inv()*A*U == s.diag(1,D)
    assert A*v == v and A**m == I4
    print(f'j={j}: det(U_j)=1; U_j^(-1) A_j U_j=diag(1,D_Xj); A_j v_j=v_j; A_j^{m}=I')
    print('U_j =', U.tolist())
    print('D_Xj =', D.tolist())
assert C1**3 == s.eye(2) and C2**4 == s.eye(2)
C0 = (C1*C2).inv()
assert C0 == s.Matrix([[1,1],[0,1]])
print('A_0 =', (A1*A2).inv().tolist())
print('C_0 =', C0.tolist())
SN = smith_normal_form((C1-s.eye(2)).row_join(C2-s.eye(2)),domain=s.ZZ)
assert [abs(SN[i,i]) for i in range(2)] == [1,1]
print('elliptic coinvariant Smith factors = [1,1]')

t = s.symbols('t')
a,b = -3*t**3*(t-1),2*t**4*(t-1)**2
delta_core = s.factor(4*a**3+27*b**2)
assert delta_core == -108*t**8*(t-1)**3
assert s.cancel(1728*4*a**3/delta_core) == 1728*t
print('Weierstrass discriminant core 4a^3+27b^2 =',delta_core)
print('j =',s.cancel(1728*4*a**3/delta_core))

z,cE = s.symbols('s c_E')
c11,c12,c21,c22 = s.symbols('c11 c12 c21 c22')
CC = s.Matrix([[c11,c12],[c21,c22]])
B0 = s.Matrix([[0,1],[-1,0]])
P = s.Matrix([[1,-1,0],[0,1,-1]])
Q = B0.inv()*P
S = s.Matrix([[1,1],[0,1],[0,0]])
k,r = s.Matrix([1,1,1]),s.Matrix([[0,0,1]])
AA,BB = P.col_join(r),Q.col_join(r)
Z2,Z3 = z*B0+CC,z*s.eye(3)+S*CC*Q+k*cE*r
assert AA.det() == BB.det() == 1
assert s.simplify(AA*Z3*BB.inv()-s.diag(Z2,z+cE)) == s.zeros(3)
assert s.simplify(P*Z3-Z2*Q) == s.zeros(2,3)
assert s.simplify(Z3*S*B0-S*Z2) == s.zeros(3,2)
print('cusp product: det(A)=det(B)=1; A Z3 B^-1=diag(Z2,s+c_E)')
print('projection marking: P Z3=Z2 Q; section angular/deck maps: S, S B0')
print('section marking: Z3 S B0=S Z2')
print('All listed post-proof-read arithmetic checks passed; no full rerun of E1.4/E1.5 cohomology is claimed.')
