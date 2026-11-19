"""Independent exact upper-collar inverse-period and fan-edge certificate."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json

root=Path(__file__).resolve().parents[2]
W,T,q2,L,uP,uQ,uX,E,c=s.symbols('W T q2 L uP uQ uX E c', nonzero=True)
q1=W*T; Q=q1*q2*uQ; P=uP/q2; cX=q2*uX; uG=uQ*uP
checks=[]
def check(name,left,right):
    assert s.factor(left-right)==0,name
    checks.append(name)

# Actual upper chart and its full inverse, with E evaluated on W,T,q2.
t=uP*L/E**2; w=T*L/E**2
s0=E**2*W/L; s1=E**2*q2/(uP*L)
check('upper inverse W',s0*t/uP,W)
check('upper inverse T',uP*w/t,T)
check('upper inverse q2',s1*t,q2)
check('upper inverse L',E**2*t/uP,L)
check('upper source q1',s0*w,q1)

# Dense original source torus before extending the displayed final chart.
Z0=q2*uQ*T
V0=L*uP**2*W/q2**2
check('full upper TL source',Z0,uG*s1*w)
check('full upper TL line',V0,E**2*s0/s1**2)
check('full upper h-inverse/J line',V0/(P**2*W),L)

# B=(P^-1 Z,c*q1*cX^-2 V), for the reduced branch c=2lambda.
Zpre=P*Z0
Vpre=cX**2*V0/(c*q1)
Wpre=Q/Zpre
Lpre=s.factor(Zpre*Vpre)
F=uG*uP**2*uX**2/c
check('actual inverse B source',Zpre,uG*T)
check('actual inverse B complementary source',Wpre,q2*W/uP)
check('actual inverse B coefficient',Vpre,L*uP**2*uX**2/(c*T))
check('full diagonal coefficient is an extending unit times L',Lpre,F*L)
check('forward B recovers source',Zpre/P,Z0)
check('forward B recovers line',c*q1*Vpre/cX**2,V0)
check('ordinary source node product',Zpre*(q1/Zpre),q1)
check('collision unit value',F.subs({uQ:s.Rational(1,256),uP:16,uX:s.Rational(-1,4)}),1/c)

# All theta product factors are holomorphic, with nonnegative q2 exponents.
S=P*W
for r in range(1,7):
    check('theta numerator Q^r*S r='+str(r),Q**r*S,
          W**(r+1)*T**r*q2**(r-1)*uQ**r*uP)
    check('theta numerator Q^r/S r='+str(r),Q**r/S,
          W**(r-1)*T**r*q2**(r+1)*uQ**r/uP)
check('theta denominator complementary coordinate',Q/W,q2*T*uQ)

# Exact edge and monomial characters, including the retained height.
rays=[s.Matrix([0,0,1]),s.Matrix([1,-1,1])]
characters=[s.Matrix([[1,0,0]]),s.Matrix([[-1,0,1]]),s.Matrix([[1,1,0]])]
values=s.Matrix([[int((ch*ray)[0]) for ray in rays] for ch in characters])
assert values==s.Matrix([[0,1],[1,0],[0,0]])
checks.append('edge {0,e1-e2} carries (Z,q1/Z,ZV) with ZV invertible')
check('chart character matrix is unimodular',s.Matrix.vstack(*characters).det(),-1)
e1=s.Matrix([1,0]);e2=s.Matrix([0,1]);J=s.Matrix([[-1,0],[1,1]])
def vertices(vs):return {tuple(x) for x in vs}
assert vertices([J*x for x in [s.zeros(2,1),e1,e2]])==vertices([x-e1 for x in [e1,e2,e1+e2]])
checks.append('J carries first negative-square triangle with full translate')
assert vertices([J*x for x in [e1,e2,e1+e2]])==vertices([x-e1+e2 for x in [s.zeros(2,1),e1,e2]])
checks.append('J carries second negative-square triangle with full translate')

# The charged and upper descriptions agree literally on their full overlap.
a,b,tau,z=s.symbols('a b tau z',nonzero=True)
charged={W:a*tau/uP,T:uP*z/tau,q2:b*tau,L:E**2*z*tau/uP}
check('charged overlap source',Zpre.subs(charged,simultaneous=True),uG*uP*z/tau)
check('charged overlap line',Lpre.subs(charged,simultaneous=True),uG*uP*uX**2*E**2*z*tau/c)

out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':len(checks),
 'identities':checks,'final_source_chart':'original marked TL source S=W,T0=T',
 'final_toric_edge':[[0,0,1],[1,-1,1]],
 'final_line_arrow':'Lpre=(uG*uP^2*uX^2/c_lambda)*L',
 'scope':'Literal full inverse period, Cartier/theta factors, upper inverse and correctly translated ordinary fan edge. The global mixed-face and finite-strip attachment remains a separate audit.'}
(root/'code/part3_root/source_zero_upper_period.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
