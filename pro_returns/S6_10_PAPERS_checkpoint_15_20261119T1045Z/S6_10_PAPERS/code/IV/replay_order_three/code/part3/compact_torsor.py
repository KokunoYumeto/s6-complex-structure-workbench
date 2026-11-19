"""Integral compact-page torsor obstruction and exact angular clutch.
Only construction matrices and the origin formula of this run are used.
"""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
A=sp.Matrix([[0,1],[-1,-1]])
B=sp.Matrix([[0,-1],[1,0]])
G=A*B*A.inv()*B.inv()
print('cyclic monodromy shifts: A -> 4, B -> -3 in Z/12')
print('commutator shift: 4-3-4+3 = 0')
print('G=[A,B]=',G)
print('G-I=',G-sp.eye(2))
print('det(G-I)=',sp.det(G-sp.eye(2)))
print('SNF(G-I)=',smith_normal_form(G-sp.eye(2),domain=ZZ))
s,v,theta,mu,C=sp.symbols('s v theta mu C')
def F(ss,vv):
 return sp.Matrix([mu*(ss+12*vv)/2,C*(ss+12*vv)/12-(ss+12*vv)**2/24+6*vv])
gamma=sp.Matrix([6*mu,C-s-12*v]); delta=sp.Matrix([0,1])
angular=sp.simplify(F(s,v+theta)-F(s,v)-theta*gamma-6*theta*(1-theta)*delta)
print('angular identity residual=',angular)
print('gauge endpoints=',[6*t*(1-t) for t in [0,1]])
print('Q-deck angular residual=',sp.simplify((F(s+12,v+theta)-F(s+12,v))-(F(s,v+theta)-F(s,v))))
assert angular==sp.zeros(2,1)
assert sp.det(G-sp.eye(2))==-1
