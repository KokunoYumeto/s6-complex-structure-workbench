"""Exact local-algebra checks for the rational delta-two space cusp.

This is a calculation, not a claim that the complete symbolic-square module
has been classified. All arithmetic is over Q and output is retained.
"""
from pathlib import Path
import sympy as s

x,y,z,t=s.symbols('x y z t')
variables=(x,y,z)
generators=(y*y-x*z,y*z-x**3,z*z-x*x*y)
products=[generators[i]*generators[j] for i in range(3) for j in range(i,3)]
special=x**5+x*y**3+z**3-3*x*x*y*z
basis=s.groebner(products,x,y,z,order='grevlex')
param={x:t**3,y:t**4,z:t**5}
lines=[]
lines.append('Ideal generators: '+str(generators))
lines.append('Special polynomial: '+str(special))
lines.append('Value and gradient on parametrization: '+str([
    s.expand(special.subs(param)),
    *[s.expand(s.diff(special,v).subs(param)) for v in variables]]))
for multiplier in (s.Integer(1),x,y,z):
    remainder=s.expand(basis.reduce(s.expand(multiplier*special))[1])
    lines.append(f'I^2 remainder of ({multiplier})*F: {remainder}')
    if multiplier!=1:
        assert remainder==0
    else:
        assert remainder!=0
hessian=s.hessian(special,variables).subs(param).applyfunc(s.expand)
lines.append('Hessian along parametrization: '+str(hessian))
lines.append('Exact Hessian rank over Q(t): '+str(hessian.rank()))
lines.append('Upper-left 2x2 determinant: '+str(s.factor(hessian[:2,:2].det())))
assert hessian.rank()==2
assert s.factor(hessian[:2,:2].det())==75*t**16
gradient_orders=[]
for generator in generators:
    row=[]
    for variable in variables:
        polynomial=s.Poly(s.diff(generator,variable).subs(param),t)
        row.append(min(m[0] for m,c in polynomial.terms() if c))
    gradient_orders.append(row)
lines.append('Orders of gradients: '+str(gradient_orders))
minimum=[min(row[j] for row in gradient_orders) for j in range(3)]
lower_bounds=s.Matrix(3,3,lambda i,j:minimum[i]+minimum[j])
special_orders=s.Matrix(3,3,lambda i,j:min(m[0] for m,c in s.Poly(hessian[i,j],t).terms() if c))
lines.append('Entrywise lower orders for Hessian of I^2 along C: '+str(lower_bounds))
lines.append('Entrywise orders for Hessian of F: '+str(special_orders))
assert lower_bounds-special_orders==s.ones(3,3)
lines.append('All exact assertions passed. Symbolic-square generation is not asserted by this program.')
output='\n'.join(lines)+'\n'
print(output,end='')
Path(__file__).with_suffix('.out').write_text(output)
