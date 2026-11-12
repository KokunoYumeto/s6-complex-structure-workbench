from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def check(label, value):
    assert value, label
    checks.append(label)
def zero(expr):
    return S.simplify(expr)==0

u,y,z,s,d=S.symbols('u y z s d', real=True)
R=S.Function('R')(u); delta=S.Function('delta')(u); h=S.Function('h')(u)
beta=S.Function('beta'); eta=S.Function('eta')
v=y*y/R**2; w=z*z
F=h-y*y+z*z-s*delta*beta(v)*eta(w)
check('Full negative transverse derivative retains the radius factor',zero(S.diff(F,y)+2*y*(1+s*delta/R**2*S.Subs(S.Derivative(beta(S.Symbol('v')),S.Symbol('v')),S.Symbol('v'),v)*eta(w))))
check('Full positive transverse derivative retains the cutoff derivative',zero(S.diff(F,z)-2*z*(1-s*delta*beta(v)*S.Subs(S.Derivative(eta(S.Symbol('w')),S.Symbol('w')),S.Symbol('w'),w))))
expected=S.diff(h,u)-s*S.diff(delta,u)*beta(v)*eta(w)+2*s*delta*S.diff(R,u)/R*v*S.Subs(S.Derivative(beta(S.Symbol('v')),S.Symbol('v')),S.Symbol('v'),v)*eta(w)
check('Full u derivative retains the nonzero variable-radius term',zero(S.diff(F,u)-expected))
axis=S.diff(F,u).subs({y:0,z:0}).subs({beta(0):1,eta(0):1})
check('Axis derivative follows only after transverse coordinates vanish',zero(axis-S.diff(h,u)+s*S.diff(delta,u)))

# Exact block completion before positive square roots are introduced.
A=S.Matrix([[2+u*u,u],[u,3+u*u]])
B=S.Matrix([[u,1],[2,u*u]])
C=S.Matrix([[5+u*u,1],[1,4+u*u]])
x=S.Matrix(S.symbols('x0:2')); zz=S.Matrix(S.symbols('z0:2'))
Q=(-A).row_join(B).col_join(B.T.row_join(C))
schur=C+B.T*A.inv()*B
original=(x.col_join(zz).T*Q*x.col_join(zz))[0]
completed=(-(x-A.inv()*B*zz).T*A*(x-A.inv()*B*zz)+zz.T*schur*zz)[0]
check('Variable matrix completion retains every mixed and Schur term',zero(original-completed))
check('Original negative block stays positive before its sign is applied',S.expand(A.det())==u**4+4*u**2+6)
check('Deleting the Schur contribution changes the original quadratic form',not zero(original-completed+(zz.T*B.T*A.inv()*B*zz)[0]))

# The exact worst case is attained at a corner of this affine parameter box.
for rho in [S.Rational(1,10),S.Rational(1,4),S.Rational(1,2),S.Rational(3,5),S.Rational(3,4),S.Rational(9,10)]:
    K=(1+1/rho)/2
    lower=1-rho*K
    values=[1+ss*rr*bb*ee for ss in [0,1] for rr in [0,rho] for bb in [-K,0] for ee in [0,1]]
    check(f'Negative derivative box rho={rho}: exact positive minimum',min(values)==lower and lower>0)
    values=[1-ss*dd*bb*ee for ss in [0,1] for dd in [0,7] for bb in [0,1] for ee in [-11,0]]
    check(f'Positive derivative box rho={rho}: exact minimum one',min(values)==1)

G=-y*y+z*z-d*(1-y*y)**2
check('Unsafe-cutoff first derivative factors exactly',zero(S.diff(G,y)+2*y*(1-2*d+2*d*y*y)))
check('Unsafe-cutoff full Hessian retained',all(zero(x) for x in S.hessian(G,(y,z))-S.diag(-2+4*d-12*d*y*y,2)))
for dd in [S.Rational(2,3),S.Rational(3,4),1,2,3,5]:
    r=S.sqrt(1-1/(2*S.sympify(dd)))
    for yy in [0,r,-r]:
        check(f'Unsafe d={dd}, y={yy}: exact critical point',zero(S.diff(G,y).subs({d:dd,y:yy})) and zero(S.diff(G,z).subs(z,0)))
    check(f'Unsafe d={dd}: both extra Hessians have negative first entry',zero(S.diff(G,y,2).subs({d:dd,y:r})-(4-8*dd)) and 4-8*dd<0)

# Figure equations and bounds, with no numerical root advertised as a proof.
dd=4*S.exp(-1/(1-u*u))
g=2*4*u/(1-u*u)**2*S.exp(-1/(1-u*u))
check('Figure derivative retains the bump exponential and denominator',zero(S.diff(u+dd,u)-(1-g)))
check('Figure derivative-loss factor has exactly one interior maximum',zero(S.diff(S.log(g),u)-(1-3*u**4)/(u*(1-u*u)**2)))
check('Elementary lower bound on e supports the strict figure ratio',sum(S.Rational(1,S.factorial(j)) for j in range(5))>S.Rational(8,3))
check('Displayed transverse gap is exactly one tenth',1-S.Rational(3,5)*S.Rational(3,2)==S.Rational(1,10))
source=W/'src/morse-cancellation-with-controlled-support.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,limitations='Exact coordinate, derivative, inequality and counterexample checks supplement the written geometric proof. They do not mechanically verify global flow, embedding, compactness or smooth classification arguments. No independent review is claimed.')
(W/'checks/MORSE_CANCELLATION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
