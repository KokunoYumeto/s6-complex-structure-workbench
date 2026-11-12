"""Exact finite identities accompanying the full analytic proof.

This does not test compactness, analytic gluing, or deformation cohomology;
their proofs are in period_parameter_deformation.tex.
"""
import json
import sympy as S

T,m,D,x,y=S.symbols('T m D x y',real=True,nonzero=True)
r1,r2,beta_re=S.symbols('r1 r2 beta_re',real=True)
delta=S.symbols('delta')
I=S.I
P=S.Matrix([[0,0],[-m/T,1]])
A=S.eye(2)+delta*P/(2*I*D)
B=-delta*P/(2*I*D)
nu=delta*P/(2*I*D+delta)
checks=[]
def check(name, expr):
    if isinstance(expr,S.MatrixBase):
        ok=all(S.cancel(v)==0 for v in expr)
    else:
        ok=S.cancel(expr)==0
    assert ok,name
    checks.append(name)
check('retained idempotent',P*P-P)
check('complex-linear determinant',A.det()-1-delta/(2*I*D))
check('exact inverse',A*(S.eye(2)-delta*P/(2*I*D+delta))-S.eye(2))
check('plus graph annihilates w',A*nu+B)
check('graph derivative',nu.diff(delta).subs(delta,0)-P/(2*I*D))

# Original real coordinate order (Re zeta1, Im zeta1, Re zeta2, Im zeta2).
Pi=S.Matrix([[6*r1,r2,1,0],[6*m,T,0,0],
             [beta_re,r1,0,1],[D+6*m*m/T,m,0,0]])
Pc=Pi.copy(); Pc[2,0]+=x; Pc[3,0]+=y
Q=Pc*Pi.inv()
row=S.Matrix([[0,-m/(T*D),0,1/D]])
want=S.eye(4)+S.Matrix([0,0,x,y])*row
check('original marked real comparison',Q-want)
check('ordered real determinant',Pi.det()-T*D)
check('changed real determinant',Pc.det()-T*(D+y))
check('positive-domain determinant ratio',Q.det()-(D+y)/D)
check('recovery of original u1',row*Pi-S.Matrix([[1,0,0,0]]))

# Explicit critical-ideal computations over characteristic zero.
s,z0,z1,z2=S.symbols('s z0 z1 z2')
for order in (3,4):
    g=S.groebner([S.diff(s**order,s)],s)
    check('finite critical value order '+str(order),g.reduce(s**order)[1])
g=S.groebner([z1*z2,z0*z2,z0*z1],z0,z1,z2)
check('triple-point critical value',g.reduce(z0*z1*z2)[1])
g=S.groebner([z0,z1],z0,z1)
check('double-point critical value',g.reduce(z0*z1)[1])

# A first-order projective vector field vanishing at all three marked points.
c0,c1,c2=S.symbols('c0 c1 c2')
solution=S.solve([c0,c0+c1+c2,c2],(c0,c1,c2))
assert solution=={c0:0,c1:0,c2:0}
checks.append('three marked values kill projective vector field')
print(json.dumps({'status':'PASS','checks':checks,
    'count':len(checks),'KS_convention':'connecting class is minus plus-graph derivative',
    'scope':'exact finite algebra only; analytic proof in accompanying TeX'},indent=2))
