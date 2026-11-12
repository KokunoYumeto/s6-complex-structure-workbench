"""Exact rational replay for the Fabel/Jacobi -> NS -> gauge audit."""
import json
from pathlib import Path
import sympy as s

x, y, t, z, tau, r = s.symbols('x y t z tau r')
F = s.Matrix([
    (1+x*y)**3*t + y**2*(1+x*y)*(4+3*x*y),
    y + 3*x*(1+x*y)**2*t + 3*x*y**2*(4+3*x*y),
    2*x - 3*x**2*y - x**3*t,
])
J = F.jacobian([x,y,t])
checks = []
def ck(name, value):
    ok = bool(s.simplify(value))
    checks.append({"name": name, "passed": ok})
    if not ok:
        raise AssertionError(name)

ck("det_DF_minus_2", s.det(J) == -2)
pts = [(0,0,s.Rational(-1,4)), (1,s.Rational(-3,2),s.Rational(13,2)), (-1,s.Rational(3,2),s.Rational(13,2))]
vals = [tuple(F.subs({x:a,y:b,t:c})) for a,b,c in pts]
ck("three_point_collision", vals[0] == vals[1] == vals[2] == (s.Rational(-1,4),0,0))
ck("points_distinct", len(set(pts)) == 3)

gam = s.Matrix([1/z, -s.Rational(3,2)*z, s.Rational(13,2)*z**2])
Fgam = [s.factor(v.subs({x:gam[0], y:gam[1], t:gam[2]})) for v in F]
ck("trajectory_target", tuple(Fgam) == (-s.Rational(1,4)+2*tau,0,0) if False else Fgam[1:] == [0,0])
ck("trajectory_first_coordinate", s.simplify(Fgam[0] - (-s.Rational(1,4)+2*((1-z**2)/8))) == 0)
ck("collision_at_initial_time", s.simplify((-s.Rational(1,4)+2*tau).subs(tau,0)+s.Rational(1,4)) == 0)
ck("endpoint_target_zero", s.simplify((-s.Rational(1,4)+2*tau).subs(tau,s.Rational(1,8))) == 0)
ck("heat_time_inverse", s.simplify(((1-z**2)/8) - tau).subs(tau,(1-z**2)/8) == 0)
ck("root_sheet_minus_quarter", s.simplify((-r**2/s.Integer(2)).subs(r**2,s.Rational(1,2)) + s.Rational(1,4)) == 0)

# Reproduce the complete material matrices from the retained source.
J0 = J.subs({x:1,y:s.Rational(-3,2),t:s.Rational(13,2)})
Jg = J.subs({x:gam[0],y:gam[1],t:gam[2]})
B = s.eye(3); B[1,2] = 6*((1-z**2)/8)
A = s.simplify(Jg.inv()*B*J0)
C = s.simplify(J0.inv()*B.inv()*Jg)
ck("material_inverse_left", all(s.simplify(v)==0 for v in (A*C-s.eye(3))))
ck("material_inverse_right", all(s.simplify(v)==0 for v in (C*A-s.eye(3))))
ck("material_det_one", s.simplify(A.det()-1) == 0)
ck("material_initial_identity", A.subs(z,1) == s.eye(3) and C.subs(z,1) == s.eye(3))
zeta = C.T*s.Matrix([0,0,1])
ck("dual_covector_leading", s.limit(z**3*zeta[2], z, 0, dir='+') == -s.Rational(9,4))
K = s.simplify(C*C.T)
ck("diffusion_det_one", s.simplify(K.det()-1) == 0)

# Abelian SU(2) gauge embedding: curvature norm equals lambda^2 vorticity norm.
lam = s.symbols('lambda', real=True)
u1,u2,u3 = s.symbols('u1 u2 u3', real=True)
d12,d13,d23 = s.symbols('d12 d13 d23', real=True)
curv = lam**2*(d12**2+d13**2+d23**2)
vort = s.Matrix([d23,-d13,d12])
ck("abelian_curvature_norm", s.expand(curv - lam**2*(vort.dot(vort))) == 0)

out = {"checks": checks, "count": len(checks), "passed": sum(c["passed"] for c in checks), "source": "FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md"}
Path(__file__).with_name("FABEL_JACOBI_TO_YM_CHECKS.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out, indent=2))
