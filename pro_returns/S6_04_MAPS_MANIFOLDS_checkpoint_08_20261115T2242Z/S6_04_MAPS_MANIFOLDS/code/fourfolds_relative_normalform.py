"""Exact rational normal form for irreducible (5,4) rank-five pairs.

All statements here are symbolic over Q(r,s,t); no numerical search bound
is used. Exceptional strata are retained via the displayed linear system.
"""
import sympy as S
r,s,t,x = S.symbols('r s t x')
J=S.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
A=S.diag(1,J)
I=S.eye(5)
R=(A+I).inv()
X=S.Matrix([[0,1],[1,0],[0,r],[0,s],[0,t]])
y=S.symbols('y0:10')
Y=S.Matrix(2,5,y)
expressions=list(Y*X)+list(Y*R*X-S.eye(2))+[S.trace(Y*A*X)+1,S.trace(Y*A.inv()*X)-1]
D,b=S.linear_eq_to_matrix(expressions,y)
det=S.factor(D.det())
print('A=',A.tolist())
print('X=',X.tolist())
print('linear coefficient determinant=',det)
print('linear coefficient matrix=',D.tolist())
print('right side=',list(b))
E_inverse=D.inv()
sol=E_inverse*b
sol=sol.applyfunc(S.factor)
YY=S.Matrix(2,5,list(sol))
print('Y=',YY.tolist())
NN=(X*YY).applyfunc(S.factor)
CC=((I+NN)*A).applyfunc(S.factor)
zero=lambda Z:Z.applyfunc(S.factor)==S.zeros(*Z.shape)
assert zero(YY*X)
assert zero(YY*R*X-S.eye(2))
assert zero(NN*NN)
assert S.factor(CC.charpoly(x).as_expr()-(x-1)*(x+1)**2*(x*x+1))==0
assert zero(CC**4-I)
print('N^2=0, C^4=1, characteristic polynomial: exact PASS')
print('det NA|imN=',S.factor((YY*A*X).det()))
print('trace A^2 C^2=',S.factor(S.trace(A*A*CC*CC)))
# Full rank fails for I+RI exactly when every 4x4 minor is zero.
Z=X.row_join(R*X)
minors=[S.factor(Z.extract(rows,range(4)).det()) for rows in __import__('itertools').combinations(range(5),4)]
print('transversality 4x4 minors=',minors)
print('normal form verified symbolically')

# Two polynomial adjugate certificates remain valid on the determinant locus.
DD=S.factor(4*det)
for index in (0,5):
    certificate=(DD*E_inverse[index,:]).applyfunc(S.factor)
    assert (certificate*D-DD*S.eye(10)[index,:]).applyfunc(S.factor)==S.zeros(1,10)
    print('polynomial certificate row',index,'=',list(certificate))
    print('certificate rhs',index,'=',S.factor((certificate*b)[0]))
Q1=r*r-r*s-r*t+s*s+t*t
Q2=r*r-2*r*s-3*r*t+4*s*s-4*s*t+4*t*t
assert S.expand(2*Q1-((r-s)**2+(r-t)**2+s*s+t*t))==0
assert S.factor(DD.subs(r,s+t)-(t-3*s)*(2*t-s)**2)==0
assert S.factor(Q2.subs(r,s+t)-(3*s-t)*(s-2*t))==0
print('positivity and cubic exceptional identities: exact PASS')
for point in ((3,2,1),(4,1,3)):
    E=D.subs(dict(zip((r,s,t),point)))
    print('exception',point,'coefficient rank',E.rank(),'augmented rank',E.row_join(b).rank())
    print('exception solution',S.linsolve((E,b),y))
z=S.symbols('z')
YE=S.Matrix([[4*z+S.Rational(16,5),0,-2*z-1,S.Rational(4,5)-2*z,2*z],
             [2*z-S.Rational(2,5),0,-z,S.Rational(2,5)-z,z]])
XE=X.subs({r:4,s:1,t:3})
CE=(I+XE*YE)*A
assert zero(YE*XE) and zero(YE*R*XE-S.eye(2))
assert zero(CE**4-I)
print('exceptional line C^4=1: exact PASS')
print('exception line d=',S.factor((YE*A*XE).det()))
print('exception line trace A^2 C^2=',S.factor(S.trace(A*A*CE*CE)))

print('ALL SYMBOLIC CHECKS PASSED')
