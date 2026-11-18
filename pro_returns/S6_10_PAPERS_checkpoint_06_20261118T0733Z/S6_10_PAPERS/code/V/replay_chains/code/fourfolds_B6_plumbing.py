"""Exact rational intersection certificate for the UNTWiSTED K13 filling.

The geometric proof in B.6.11 reduces its middle form to minus the
surface pairing on span(F,m,v). No matrix search is involved.
This does not compute a filling for the finite logarithmic sphere.
"""
from sympy import Matrix, symbols, expand
G=Matrix([[0,0,0],[0,-2,-1],[0,-1,-6]])
assert G.rank()==2 and G.nullspace()==[Matrix([1,0,0])]
Q=-G[1:,1:]
assert Q==Matrix([[2,1],[1,6]])
assert Q[0,0]>0 and Q.det()==11>0
print('surface Gram on F,m,v',G)
print('radical',G.nullspace())
print('filling nonsingular rational form',Q)
print('determinant',Q.det(),'signature',2)
a0,ai,b0,bi=symbols('a0 ai b0 bi')
assert expand(-a0*b0-ai*bi+a0*bi+b0*ai+(a0-ai)*(b0-bi))==0
print('same-branch plus conductor cross terms = negative difference pairing')
print('normal line = O(-D0-Dinfinity); pullback c1(W)=pi*F, hence c1(W)^2=0')
print('No finite-log filling or numerical Theta7 value is asserted.')
