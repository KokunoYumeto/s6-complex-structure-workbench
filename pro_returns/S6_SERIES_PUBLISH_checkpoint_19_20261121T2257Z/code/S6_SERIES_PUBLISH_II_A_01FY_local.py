import sympy as s
# Independent coordinate-Jacobian tests, expressed as pulled-back top forms.
r,xp,yp=s.symbols('r xp yp', nonzero=True)
coord=s.Matrix([r**3,r**4*xp]); jac=coord.jacobian([r,xp]).det()
print('cubic canonical coefficient:',s.factor(jac/(r**6*yp)))
assert s.simplify(jac/(r**6*yp)-3/yp)==0
A=s.Matrix([[0,1],[-1,2]])
print('primitive rank-one character determinant:',A.det()); assert A.det()==1
X,Y,Z=s.symbols('X Y Z',nonzero=True)
rankone=s.Matrix([[Y,X,0],[1/X,0,0],[0,0,1/Z]]).det()
ranktwo=s.Matrix([[Y*Z,X*Z,X*Y],[0,1/Y,0],[0,0,1/Z]]).det()
print('rank-one dq wedge dlogX wedge dlogZ:',rankone)
print('rank-two dq wedge dlogY wedge dlogZ:',ranktwo)
assert s.simplify(rankone+1/Z)==0 and ranktwo==1
b,m=s.symbols('b m',integer=True)
print('Serre dimension difference:',s.expand((-b-m-1)-(-m)))
assert s.solve(s.Eq(-b-m-1,-m),b)==[-1]
h0=lambda d:max(d+1,0);h1=lambda d:max(-d-1,0)
h=[1,h0(0)+h0(-1),h1(0)+h1(-1)+h0(-1),h1(-1)]
print('total structure-sheaf dimensions:',h);assert h==[1,1,0,0]
