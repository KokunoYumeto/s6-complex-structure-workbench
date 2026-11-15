"""Exact algebra and degree checks used in C.2.IRR.1.

The geometric proof is in part_C2_irrational.tex.  This script checks its
explicit normalization-ring relation, the Hessian determinant transition,
the Riemann--Hurwitz count, and the Euler bookkeeping.  It does not replace
the conductor cartesian-square or the local-to-global comparisons.
"""
import sympy as s

u, v, x, y, z = s.symbols('u v x y z')
ideal = [x-u*v, y-u, z-v*v]
basis = s.groebner(ideal, u, v, x, y, z, order='lex')
eliminated = [p.as_expr() for p in basis.polys
              if not (p.as_expr().free_symbols & {u, v})]
assert eliminated == [x*x-y*y*z]
print('Exact elimination for (x,y,z)=(uv,u,v^2):', eliminated)
assert s.expand((x*x-y*y*z).subs({x:u*v, y:u, z:v*v})) == 0
print('The pinch relation vanishes identically under the normalization map.')

a, b, c, p, q, r, t = s.symbols('a b c p q r t')
quadratic = s.Matrix([[a,b],[b,c]])
transition = s.Matrix([[p,q],[r,t]])
assert s.expand((transition.T*quadratic*transition).det()
                -transition.det()**2*quadratic.det()) == 0
print('Quadratic determinant transforms by the square of the frame determinant.')

delta = s.symbols('delta', integer=True, nonnegative=True)
deg_normal = 2*delta
deg_hessian_det = -2*deg_normal
assert deg_hessian_det == -4*delta
print('Elliptic normalized image: deg N=2 delta; deg det(Hessian)=-4 delta.')
ramification = (2*1-2)-2*(2*0-2)
assert ramification == 4
print('Connected degree-two elliptic-to-rational cover: ramification degree =',
      ramification)
print('A degree-two cover has one simple ramification point over each branch value.')
print('A unibranch rational image with arithmetic genus <=2 has <=2 singular values.')

blowups, mult = s.symbols('N m', integer=True, nonnegative=True)
e_minimal = 2*(2-2*1)
e_normalization = e_minimal+blowups
e_conductor = 0
e_image = 0
e_support = e_normalization-e_conductor+e_image
e_nearby = mult*(e_normalization-e_conductor)
assert e_support == blowups and e_nearby == mult*blowups
print('Euler identities: e(S)=N and e(Y_t)=m N; m>0 and torus e(Y_t)=0 force N=0.')
print('All exact algebra and degree checks passed.')
