"""Post-reading algebra for the mathematical example moved into P4.47.

This verifies the two transverse nodes for the displayed quadratic model.
The proof treats analytic higher terms by the explicit local Jacobian map.
"""
import json
import sympy as s

a,b,c,t,eps,U = s.symbols('a b c t epsilon U', nonzero=True)
y,z = s.symbols('y z')
G = a*t*y+b*t*z+c*y*z
h = t*y*z
F = (G-eps)**2+U*h**2
J = s.Matrix([[s.diff(G,y),s.diff(G,z)], [s.diff(h,y),s.diff(h,z)]])
points = [{y:0,z:eps/(b*t)}, {y:eps/(a*t),z:0}]
rows = []
for i,p in enumerate(points):
    assert s.cancel((G-eps).subs(p)) == 0
    assert s.cancel(h.subs(p)) == 0
    assert all(s.cancel(s.diff(F,v).subs(p)) == 0 for v in [y,z])
    jac = s.factor(J.det().subs(p))
    assert jac == [-t*eps,t*eps][i]
    det = s.factor(s.hessian(F,[y,z]).det().subs(p))
    assert det == 4*U*t**2*eps**2
    rows.append(dict(point={str(k):str(v) for k,v in p.items()},
                     jacobian= str(jac), hessian_determinant=str(det)))
print(json.dumps({'scope':'Exact quadratic-model branch and Hessian identities; post-reading presentation verification only.',
                  'coordinate_map':['G-epsilon','h*sqrt(U)'],
                  'node_coordinates':['u+i*v','u-i*v'],
                  'node_equation':'(u+i*v)*(u-i*v) = u^2+v^2',
                  'points':rows,'all_assertions_passed':True},indent=2))
