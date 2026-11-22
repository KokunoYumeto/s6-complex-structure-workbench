# Exact E14-only body plus original SymPy import and symbol declarations.
import sympy as s
t=s.symbols('t')
mu,e1,e2,bb,x,y,r=s.symbols('mu e1 e2 b x y r')

eps=s.symbols('eps')
disc=4*t**3+27*(t+eps)**2
print('E14 elliptic collision discriminant:',s.factor(s.discriminant(disc,t)))
assert s.factor(disc.subs(eps,0))==t**2*(4*t+27)
print('E14 exact cusp jet slope:',s.series(-s.I/(1+x),x,0,2))
jet_matrix=s.Matrix([[1,-s.I],[0,s.I]])
assert jet_matrix.det()==s.I
print('E14 exact jet restriction determinant:',jet_matrix.det())
