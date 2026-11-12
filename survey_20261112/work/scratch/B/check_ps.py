# Sanity checks for period_shift_classification.tex (PS3)-(PS21) and hodge counts. Exact arithmetic with sympy.
import sympy as sp
T1 = sp.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2 = sp.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1 = sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
print("A1 == (T1^-1)^t:", A1 == (T1.inv()).T, " A2 == (T2^-1)^t:", A2 == (T2.inv()).T)
print("A1^3=I", A1**3 == sp.eye(4), "A2^4=I", A2**4 == sp.eye(4))
v1 = sp.Matrix([1,2,-4,0]); v2 = sp.Matrix([-1,-3,3,0])
print("A1 v1=v1", A1*v1 == v1, "A2 v2 = v2", A2*v2 == v2)
E = sp.zeros(4,4); E[3,0] = 1
print("A_j E = E A_j = E:", A1*E==E, E*A1==E, A2*E==E, E*A2==E)
N1 = sp.eye(4)+A1+A1**2; N2 = sp.eye(4)+A2+A2**2+A2**3
print("N1 =", N1.tolist()); print("N2 =", N2.tolist())
# centralizer
X = sp.Matrix(4,4, sp.symbols('x0:16'))
eqs = list((X*A1-A1*X)) + list((X*A2-A2*X))
sol = sp.solve(eqs, list(X), dict=True)[0]
Xs = X.subs(sol); print("centralizer:", Xs.tolist())
# PS14
n = sp.symbols('n')
uh = sp.Matrix([0,1,0,0]); wh = sp.Matrix([0,0,1,0]); dh = sp.Matrix([0,0,0,1])
r1 = -n/sp.Integer(3)*(uh+wh); l1 = -n*wh
r2 = n/sp.Integer(4)*(uh+wh); l2 = n/sp.Integer(2)*uh
print("PS14 j=1:", sp.simplify((sp.eye(4)-A1)*r1 - (n*1/sp.Integer(3)*dh + l1)).T.tolist())
print("PS14 j=2:", sp.simplify((sp.eye(4)-A2)*r2 - (n*(-1)/sp.Integer(4)*dh + l2)).T.tolist())
# quotient Lambda^{A_j}/N_j Lambda via Smith normal form
from sympy.matrices.normalforms import smith_normal_form
for name,A,N in (("j=1",A1,N1),("j=2",A2,N2)):
    K = (A-sp.eye(4)).nullspace()
    # integral basis of fixed lattice: saturate
    Kb = sp.Matrix.hstack(*[k*sp.ilcm(*[sp.fraction(x)[1] for x in k]) for k in K])
    print(name, "fixed basis cols:", Kb.T.tolist())
    # express N columns in fixed basis (assume Kb primitive basis)
    coords = sp.Matrix.hstack(*[ (Kb.T*Kb).inv()*Kb.T*N[:,i] for i in range(4)])
    print(name, "N cols in fixed basis:", coords.tolist(), " SNF:", smith_normal_form(coords, domain=sp.ZZ).tolist())
    cd = (Kb.T*Kb).inv()*Kb.T*dh
    print(name, "delta-hat coords:", cd.T.tolist())
# cocycle PS21
A0 = (A1*A2).inv()
l1n = l1; l2n = l2
print("l1 + A1 l2 =", sp.simplify(l1n + A1*l2n).T.tolist(), " A_g0 =", A0.tolist())
print("l0 =", sp.simplify(-A0*(l1n+A1*l2n)).T.tolist())
# contractions with q
Q = sp.Matrix([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
print("i_v1 q =", (v1.T*Q).tolist(), " i_v2 q =", (v2.T*Q).tolist())
# invariants of wedge^2: check q invariant: T^t Q T ? (Q as form on Lambda: A^t Q A = Q)
print("q invariant under A1,A2:", A1.T*Q*A1 == Q, A2.T*Q*A2 == Q)
