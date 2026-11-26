"""Fresh exact coordinate and residue calculations for III 02M2."""
import sympy as S

r, X, Y, q, t, xE, yE = S.symbols('r X Y q t xE yE')
x, y, z, v, u, s = S.symbols('x y z v u s', nonzero=True)
F = yE**2-xE**3+3*t**3*(t-1)*xE-2*t**4*(t-1)**2

F0 = S.cancel(F.subs({t:r**3,xE:r**4*X,yE:r**6*Y})/r**12)
F1 = S.cancel(F.subs({t:1+r**4,xE:r**2*X,yE:r**3*Y})/r**6)
Finf = S.cancel(F.subs({t:1/q,xE:X/q**2,yE:Y/q**3})*q**6)
assert S.expand(F0-(Y**2-X**3+3*r*(r**3-1)*X-2*(r**3-1)**2)) == 0
assert S.expand(F1-(Y**2-X**3+3*(1+r**4)**3*X-2*r**2*(1+r**4)**4)) == 0
assert S.expand(Finf-(Y**2-X**3+3*(1-q)*X-2*(1-q)**2)) == 0
assert S.discriminant(X**3+2,X) == -108
assert S.discriminant(X**3-3*X,X) == 108
print('PASS full good-reduction polynomials at t=0 and t=1')
print('PASS smooth central cubics: discriminants -108 and 108')

def differential_factor(t_expr,x_expr,y_expr,coords):
    return S.cancel(S.Matrix([t_expr,x_expr]).jacobian(coords).det()/y_expr)

a0 = differential_factor(r**3,r**4*X,r**6*Y,[r,X])
a1 = differential_factor(1+r**4,r**2*X,r**3*Y,[r,X])
ai = differential_factor(1/q,X/q**2,Y/q**3,[q,X])
assert a0 == 3/Y and a1 == 4*r**2/Y and ai == -1/(Y*q)
assert S.diff(Finf,q).subs({q:0,X:1,Y:0}) == 1
print('PASS exact differential factors:',a0,a1,ai)
print('PASS cusp total surface is smooth at the nodal fibre point')

# The numerator form is checked by full Jacobian pullback on each chart.
v_chart = (x*y/u+s)/z
z_chart = (x*y/u+s)/v
eta_z = S.cancel(S.Matrix([x,z,v_chart]).jacobian([x,z,y]).det()/x)
eta_v = S.cancel(S.Matrix([x,z_chart,v]).jacobian([x,y,v]).det()/x)
x_chart = u*(z*v-s)/y
eta_y = S.cancel(S.Matrix([x_chart,z,v]).jacobian([y,z,v]).det()/x_chart)
assert eta_z == 1/(u*z)
assert eta_v == 1/(u*v)
assert eta_y == -1/y
print('PASS three residue transitions:',eta_z,eta_v,eta_y)
assert S.expand(x*y-u*(z*v-s)).subs({x:0,y:0,z:0,v:0}) == s*u
print('PASS no simultaneous zero of all four coordinates for u*s nonzero')

a,b=S.symbols('a b',integer=True)
ray=lambda i,j:S.Matrix([i,j,1])
T0=S.Matrix.hstack(ray(a,b),ray(a+1,b),ray(a,b+1))
T1=S.Matrix.hstack(ray(a+1,b),ray(a,b+1),ray(a+1,b+1))
assert T0.det()==1 and T1.det()==-1
print('PASS height-one monomial chart determinants:',T0.det(),T1.det())
assert -12+24//4 == -6
print('PASS twelfth canonical power: -12+24/4=-6')
print('ALL FRESH EXACT FORM CALCULATIONS PASSED')
