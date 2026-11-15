"""Exact local root charts and the multiplicity obstruction.

This verifies the local inputs for analytic torsor descent and the
failure of the simple one-component plumbing to have primitive
rank-one reduction. It does not construct the missing corrected filling.
"""
from sympy import symbols, sqrt, expand, simplify, Matrix, eye, diff, factorial
t,z,X,Y,x,y,r=symbols('t z X Y x y r')
weierstrass=y**2-x**3+3*t**3*(t-1)*x-2*t**4*(t-1)**2
P_y=sqrt(2)*t**2*(t-1)
assert expand(weierstrass.subs({x:0,y:P_y}))==0
root3=expand(weierstrass.subs({t:z**3,x:z**4*X,y:z**6*Y})/z**12)
root4=expand(weierstrass.subs({t:1+z**4,x:z**2*X,y:z**3*Y})/z**6)
assert root3.subs(z,0)==Y**2-X**3-2
assert root4.subs(z,0)==Y**2-X**3+3*X
P3=simplify(P_y.subs(t,z**3)/z**6)
P4=simplify(P_y.subs(t,1+z**4)/z**3)
assert P3.subs(z,0)==-sqrt(2) and P4.subs(z,0)==0
print('order-three good model',root3)
print('central curve Y2=X3+2; P=(0,-sqrt2); fixed affine points (0,+/-sqrt2)')
print('order-four good model',root4)
print('central curve Y2=X3-3X; P=(0,0); unique affine fixed point (0,0)')
# On Y^2=X^3+2, tangent slope at P is zero, so 2P=-P.
slope=0
double_x=slope**2-2*0
double_y=slope*(0-double_x)+sqrt(2)
assert double_x==0 and double_y==sqrt(2)
print('three-torsion checked by doubling P to -P; order-two point has Y=0')
print('local cyclic norm witnesses: H3:2P; H4:formal [4] inverse of 6P; H12:local P/2')

# A rank-one unipotent and its conjugate by an order-three real
# matrix have distinct fixed lines; this is an exact sample of
# the basis-independent argument in B.6.14.
A=Matrix([[0,-1],[1,-1]])
T=Matrix([[1,1],[0,1]])
assert A**3==eye(2) and (A-eye(2)).det()==3
assert Matrix.vstack(T-eye(2),A*T*A.inv()-eye(2)).rank()==2
print('the elliptic local system on the cyclic cover has no common invariant vector')

base=(x*y/r)**12
for j in range(12):
    assert diff(base,y,j).subs(y,0)==0
assert simplify(diff(base,y,12).subs(y,0)/factorial(12))==x**12/r**12
print('at a generic x!=0 branch, f-p=(xy/r)^12 has exact multiplicity12')
print('the other branch has the same multiplicity by symmetry')
print('No primitive rank-one filling or Theta7 value follows from this plumbing.')
