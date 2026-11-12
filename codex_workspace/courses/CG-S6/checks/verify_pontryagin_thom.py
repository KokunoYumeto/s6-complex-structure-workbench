"""Exact finite identities supporting the written geometric comparison."""
from pathlib import Path
import hashlib
import json
import sympy as s

W = Path(__file__).resolve().parents[1]
checks = []


def eq(name, left, right):
    difference = left - right
    entries = list(difference) if isinstance(difference, s.MatrixBase) else [difference]
    assert all(s.simplify(s.trigsimp(x)) == 0 for x in entries), name
    checks.append(name)


x, y, z, u, rho = s.symbols("x y z u rho", real=True)
eps = s.symbols("epsilon", positive=True)
lam = s.exp(rho / (eps**2 - rho))
eq("Full original radial derivative", s.diff(lam, rho), lam * eps**2 / (eps**2 - rho)**2)
eq("Full original radius derivative", s.diff(lam, eps), -2*eps*rho*lam/(eps**2-rho)**2)
eq("Flat exponential retains its constant", -rho/(eps**2-rho), 1-eps**2/(eps**2-rho))

for dimension in (2, 3):
    zz = s.Matrix(s.symbols(f"z0:{dimension}", real=True))
    norm = (zz.T * zz)[0]
    sigma = (2*zz/(1+norm)).col_join(s.Matrix([(norm-1)/(1+norm)]))
    eq(f"Unit target sphere in dimension {dimension}", (sigma.T*sigma)[0], 1)
    eq(f"Exact south stereographic inverse in dimension {dimension}", sigma[:-1, 0]/(1-sigma[-1]), zz)
    eq(f"Exact north stereographic inverse in dimension {dimension}", sigma[:-1, 0]/(1+sigma[-1]), zz/norm)
    derivative = sigma.jacobian(zz)
    expected = (2*s.eye(dimension)/(1+norm)-4*zz*zz.T/(1+norm)**2).col_join(4*zz.T/(1+norm)**2)
    eq(f"Full target differential in dimension {dimension}", derivative, expected)
    eq(f"Original target tangent factor two in dimension {dimension}",
       derivative.subs(dict.fromkeys(zz, 0)), (2*s.eye(dimension)).col_join(s.zeros(1, dimension)))

a, b, d = s.symbols("a b d", positive=True)
c, theta, A1, A2 = s.symbols("c theta A1 A2", real=True)
E = s.Matrix([[b*s.cos(theta), c*s.cos(theta)],
              [b*s.sin(theta), c*s.sin(theta)], [0, d]])
J = s.Matrix([-a*s.sin(theta), a*s.cos(theta), 0])
G = s.Matrix([[b*b, b*c], [b*c, c*c+d*d]])
L = s.Matrix([[s.cos(theta)/b, s.sin(theta)/b, -c/(b*d)], [0, 0, 1/d]])
eq("Original sheared circle normal orthogonality", J.T*E, s.zeros(1, 2))
eq("Complete sheared circle Gram matrix", E.T*E, G)
eq("Full sheared circle Gram determinant", G.det(), b*b*d*d)
eq("Exact inverse-image right inverse on circle", L*E, s.eye(2))
eq("Circle derivative has the actual tangent kernel", L*J, s.zeros(2, 1))
eq("Circle inverse-image Gram matrix", L*L.T, G.inv())
eq("Circle normal-frame recovery", L.T*G, E)
A = s.Matrix([A1, A2])
eq("Original mixed normal squared length", (A.T*G*A)[0], (b*A1+c*A2)**2+d*d*A2*A2)
R = a+b*A1+c*A2
tube = s.Matrix([R*s.cos(theta), R*s.sin(theta), d*A2])
eq("Actual sheared tube derivative determinant", tube.jacobian([theta, A1, A2]).det(), -R*b*d)
eq("Original inverse-image orientation", -R*b*d, -(a+b*A1+c*A2)*b*d)

J = s.Matrix([[2, 0], [0, 3], [1, 1]])
H = J.T*J
Q = H.inv()*J.T
P = s.eye(3)-J*Q
Tau = s.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 2]])
E = P.row_join(s.zeros(3, 1)).col_join((Tau[:, :2]*Q).row_join(Tau[:, 2]))
G = E.T*E
eq("Exercise original tangent Gram matrix", H, s.Matrix([[5, 1], [1, 10]]))
eq("Exercise original tangent Gram inverse", H.inv(), s.Matrix([[10, -1], [-1, 5]])/49)
eq("Exercise full left inverse", 49*Q, s.Matrix([[20, -3, 9], [-2, 15, 4]]))
eq("Exercise full normal projection", 49*P, s.Matrix([[9, 6, -18], [6, 4, -12], [-18, -12, 36]]))
eq("Normal projection idempotence", P*P, P)
eq("Normal projection kills tangent inclusion", P*J, s.zeros(3, 2))
eq("Full original tangent left inverse", Q*J, s.eye(2))
eq("Left inverse kills original normal projection", Q*P, s.zeros(2, 3))
eq("Full original tangent-normal decomposition", J*Q+P, s.eye(3))
eq("Exercise original framing determinant", Tau.det(), 13)
eq("Complete exercise normal frame", 49*E, s.Matrix([[9,6,-18,0],[6,4,-12,0],[-18,-12,36,0],[38,9,22,0],[-6,45,12,49],[20,-3,9,98]]))
eq("Complete exercise Gram matrix", 2401*G, s.Matrix([[2321,306,62,1666],[306,2311,123,1911],[62,123,2473,1470],[1666,1911,1470,12005]]))
eq("Exercise exact Gram determinant", G.det(), s.Rational(169, 49))
Jp = J.col_join(s.zeros(3, 2))
eq("Stable normal frame perpendicular to tangent", Jp.T*E, s.zeros(2, 4))
combined = Jp.row_join(E)
inverse = (H.inv()*Jp.T).col_join(G.inv()*E.T)
eq("Actual full tangent-normal inverse, first composite", inverse*combined, s.eye(6))
eq("Actual full tangent-normal inverse, second composite", combined*inverse, s.eye(6))
S = s.BlockMatrix([[s.zeros(2,2), Q, s.zeros(2,1)],
                   [J, P, s.zeros(3,1)],
                   [s.zeros(1,2), s.zeros(1,3), s.ones(1,1)]]).as_explicit()
Tau_st = s.zeros(3,2).row_join(s.eye(3)).row_join(s.zeros(3,1)).col_join(
    Tau[:,:2].row_join(s.zeros(3,3)).row_join(Tau[:,2]))
eq("Full comparison involution squares to identity", S*S, s.eye(6))
eq("Actual comparison retains both framing matrices", Tau_st*S, combined)
eq("Comparison orientation sign for n=2", S.det(), 1)
Ic = s.Matrix([[0,-1],[1,0]])
t = s.symbols("t", real=True)
th = s.pi*t/2
ph = s.pi*t
C = s.cos(ph)*s.eye(2)+s.sin(ph)*Ic
Ci = s.cos(ph)*s.eye(2)-s.sin(ph)*Ic
eq("Complex-operator interpolation has full inverse", C*Ci, s.eye(2))
eq("Full complex-operator parameter derivative", s.diff(C,t), s.pi*Ic*C)
St = s.BlockMatrix([
    [s.cos(th)*s.eye(2), s.sin(th)*Q, s.zeros(2,1)],
    [-s.sin(th)*J*C, P+s.cos(th)*J*C*Q, s.zeros(3,1)],
    [s.zeros(1,2), s.zeros(1,3), s.ones(1,1)]]).as_explicit()
eq("Original comparison path starts at identity", St.subs(t,0), s.eye(6))
eq("Original comparison path ends at full involution", St.subs(t,1), S)
eq("Comparison midpoint is invertible with exact determinant", St.subs(t,s.Rational(1,2)).det(), 1)

q = s.symbols("q", real=True)
eq("Full Gram-form profile derivative", s.diff(s.exp(q/(1-q)),q), s.exp(q/(1-q))/(1-q)**2)
w = s.Matrix([x,y])
ww = (w.T*w)[0]
qv = w/ww
north = qv.col_join(s.Matrix([u]))/((qv.T*qv)[0]+u*u)
expected = (w/(1+u*u*ww)).col_join(s.Matrix([u*ww/(1+u*u*ww)]))
eq("Suspension north chart retains both mixed terms", north, expected)
eq("Suspension coordinate denominator", 1+u*u*ww, 1+u*u*(x*x+y*y))
Gplus = s.diag(G, 1)
Eplus = s.diag(E, 1)
eq("Stabilized original normal Gram matrix", Eplus.T*Eplus, Gplus)

src = W / "src/framed-manifolds-and-the-pontryagin-thom-map.md"
result = dict(passed=len(checks), checks=checks, source=src.name,
              source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
              scope="Finite exact matrix, stereographic, derivative, framing, orientation and worked-example checks. The written arguments prove compact tube existence, relative regularity, inverse homotopies and the bordism correspondence; these finite checks do not certify those global theorems or the stable class of the six-manifold.")
(W/"checks/PONTRYAGIN_THOM_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(passed=len(checks), source_sha256=result["source_sha256"])))
