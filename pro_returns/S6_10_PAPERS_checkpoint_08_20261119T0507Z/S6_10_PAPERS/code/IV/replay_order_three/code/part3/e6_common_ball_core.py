"""Literal first-period/core coefficient and its sharp norm bound."""
from pathlib import Path
import json
import sympy as S

d,t0,t1,zeta,c=S.symbols('d t0 t1 zeta c', nonzero=True)
h=t1/t0
checks=[]
def ck(name, expr):
    value=S.factor(expr)
    assert value == 0, (name,value)
    checks.append(name)

outside=-d**2/(h**3*(h+1)**3)
full=outside*d*t0**(-3)
ck('first actual period retained', full+d**3*t0**3/(t1**3*(t0+t1)**3))
u=S.Matrix([-d*t0/(t1*(t0+t1)),-d/(t0+t1)])
ck('literal common-ball lift coefficient',u[0]**3-full)
ck('literal common-ball projective base',u[1]-h*u[0])
for i in range(2):
    ck('physical scalar equivariance '+str(i),
       u[i].subs({t0:t0/c,t1:t1/c},simultaneous=True)-c*u[i])
    ck('auxiliary deck equivariance '+str(i),
       u[i].subs({t0:t0/zeta,t1:t1/zeta},simultaneous=True)-zeta*u[i])
M=S.Matrix([[0,S.Rational(1,2)],[S.Rational(1,2),1]])
lam=(1+S.sqrt(2))/2
ck('largest norm eigenvalue', (M-lam*S.eye(2)).det())
v=S.Matrix([1,1+S.sqrt(2)])
for i in range(2):
    ck('aligned equality vector '+str(i),(M*v-lam*v)[i])
ck('sharp reciprocal bound',1/lam-2/(1+S.sqrt(2)))

out={'status':'PASS','count':len(checks),'checks':checks,
     'scope':'The first actual period in one charged ball; no global face count or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
