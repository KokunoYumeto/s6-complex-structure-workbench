"""Exact Haar Jacobian and foot coordinates for the A-B-A count domains."""
import sympy as s
u,r,v=s.symbols('u r v',real=True)
A=lambda x:s.diag(s.exp(x/2),s.exp(-x/2))
B=lambda x:s.Matrix([[s.cosh(x/2),s.sinh(x/2)],[s.sinh(x/2),s.cosh(x/2)]])
g=A(u)*B(r)*A(v)
a,b,c,d=g[0,0],g[0,1],g[1,0],g[1,1]
assert s.simplify(g.det())==1
assert s.simplify(a*b/(c*d))==s.exp(2*u)
assert s.simplify(a*c/(b*d))==s.exp(2*v)
assert s.simplify(a*d+b*c)==s.cosh(r)
columns=[]
for x in (u,r,v):
 M=s.simplify(g.inv()*g.diff(x))
 columns.append(s.Matrix([2*M[0,0],M[0,1]+M[1,0],M[0,1]-M[1,0]]))
J=s.simplify(s.Matrix.hstack(*columns).det())
ratio=s.simplify((J/s.sinh(r)).rewrite(s.exp))
assert ratio == -1
print('matrix',g)
print('distance invariant ad+bc=cosh(r) PASS')
print('source foot exp(2u)=ab/cd; target shift exp(2v)=ac/bd PASS')
print('Haar Jacobian in fixed Lie algebra basis',J)
print('Haar density is constant times sinh(r) du dr dv PASS')
