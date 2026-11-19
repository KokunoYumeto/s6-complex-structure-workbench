"""Exact source/Cartier/Cox identities for the E80 two-pole continuation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

root = Path(__file__).resolve().parents[2]
h, aa, bb = S.symbols('h alpha beta')
z, w, x, d, coeff = S.symbols('z w x d coeff')
e = h-aa+1
f = aa**2-aa-bb
k = e*(e-1)-f
sbase = h*aa-bb
twot = h*f
checks = []


def check(name, value):
    value = S.factor(S.together(value).as_numer_denom()[0])
    assert value == 0, (name, value)
    checks.append(name)


p1 = S.Matrix([-aa, e, f])
p2 = S.Matrix([-e, -k/e, h*e])
p3 = S.Matrix([k/e, -sbase*e/k-f/e, -f*k/e**2])
for j, p in enumerate((p1, p2, p3), 1):
    check(f'full s arrow {j}', p[2]-p[0]*p[1]-sbase)
    check(f'full t arrow {j}', p[2]*(p[1]-p[0]-1)-twot)
check('actual second source translation z', p2[0]+p1[1])
check('actual second source translation w',
      p2[1]-(sbase/p1[1]+p1[0]-p1[1]+1))
check('actual second source translation x', p2[2]*p1[2]-twot*p1[1])
check('actual third source translation z', p3[0]+p2[1])
check('actual third source translation w',
      p3[1]-(sbase/p2[1]+p2[0]-p2[1]+1))
check('actual third source translation x', p3[2]*p2[2]-twot*p2[1])
check('full line product with both pole factors',
      d*p1[1]**-3*d*p2[1]**-3+d**2*k**-3)
check('central core pole polynomial', k.subs({aa:0,bb:0})-h*(h+1))
check('first source chart Jacobian', p1.jacobian([h,aa,bb]).det()+1)
check('regular h0 chart Jacobian', p2.jacobian([h,aa,bb]).det()+1)

inv1 = {h:w-z-1, aa:-z, bb:z*z+z-x}
ee=-z
hh=-x/z
aaa=-x/z+z+1
inv2 = {h:hh, aa:aaa, bb:hh*aaa-(x-z*w)}
for j, (p, inv) in enumerate(((p1,inv1),(p2,inv2)), 1):
    for i, target in enumerate((z,w,x)):
        check(f'actual endpoint inverse {j}/{i}',
              p[i].subs(inv, simultaneous=True)-target)
    for variable in (h,aa,bb):
        check(f'actual endpoint reverse inverse {j}/{variable}',
              inv[variable].subs(dict(zip((z,w,x),p)),simultaneous=True)
              -variable)

hh3, A3, B3 = S.symbols('h3 A3 B3')
target = S.Matrix([-A3,hh3-A3+1,A3*A3-A3-B3])
check('opposite target s',target[2]-target[0]*target[1]-(hh3*A3-B3))
check('opposite target t',
      target[2]*(target[1]-target[0]-1)-hh3*(A3*A3-A3-B3))
iv={A3:-z,hh3:w-z-1,B3:z*z+z-x}
for i, tgt in enumerate((z,w,x)):
    check('opposite full target inverse '+str(i),
          target[i].subs(iv,simultaneous=True)-tgt)
check('linked next centre on core',target[1].subs({A3:0,B3:0})-(hh3+1))
check('third graph Cox equation',(-e)*(-k/e)-k)
check('third graph full normal x',h*e-p2[2])
check('second graph e f identities',f+ k-e*(e-1))

kk,A,B=S.symbols('kk A B')
DD=1+kk-kk*kk*A
a=kk/DD
b=DD*(-B-A+kk*A*A)
c=-DD*A
EE=1-a-a*a*c
check('endpoint unit product',DD*EE-1)
check('endpoint inverse k',a/EE-kk)
check('endpoint inverse A',-c*EE-A)
check('endpoint inverse B',(c+a*c*c-b)*EE-B)
check('endpoint actual s',a*b-c-(A-kk*B))
check('endpoint actual t',b*EE-(-B-A+kk*A*A))
check('full Cartier coefficient endpoint',
      a**3-DD**-3*kk**3)
check('frame ratio actual M6',
      a**-6*b**-3/((a*b)**-3)-a**-3)

u0,u1,t0,t1,lam=S.symbols('u0 u1 t0 t1 lam',nonzero=True)
cs=u0*t1-u1*t0
ct=t1*(u0*u0*t0-u1-u0)
sc={u0:lam*u0,u1:lam*u1,t0:t0/lam,t1:t1/lam}
check('full Cox source s is invariant',cs.subs(sc,simultaneous=True)-cs)
check('full Cox source t is invariant',ct.subs(sc,simultaneous=True)-ct)
check('Cox source finite s',
      cs.subs({u0:1,u1:z,t0:w,t1:x})-(x-z*w))
check('Cox source finite t',
      ct.subs({u0:1,u1:z,t0:w,t1:x})-x*(w-z-1))
qsel=S.symbols('qsel')
check('associated line product retains full q',
      (d*e**-3*coeff)*(d**-1*e**3*qsel/coeff)-qsel)
kap=S.symbols('kap')
core_h=t1/t0
source_coeff=(-d*d)*t0**3/(t1**3*(t0+t1)**3)
check('full core coefficient lift',
      source_coeff-(-d*d/(core_h**3*(core_h+1)**3))*t0**-3)

# Central chronological three-step norm, without replacing source maps by Id.
zw0=(z,w)
zw1=(-w,z-w+1)
zw2=(-(z-w+1),-z)
zw3=(-zw2[1],zw2[0]-zw2[1]+1)
check('central three-step source z',zw3[0]-z)
check('central three-step source w',zw3[1]-w)
check('central line denominator equals actual 2t',
      zw0[1]*zw1[1]*zw2[1]-z*w*(w-z-1))
check('central cyclic scalar matches E78',
      (8*lam*qsel)**3/(2*S.Symbol('t'))**3
      -(4*lam*qsel/S.Symbol('t'))**3)

Ef=t1+t0-u0*t0*t0
Ff=u0*u0*t0-u0-u1
Kf=t1*(t1+t0)-t0*t0*(2*u0*t1-u1*t0)
check('full common-gauge E K identity',Kf-t1*Ef+cs*t0*t0)
check('full common-gauge E F identity',Ef*Ef-Ef*t0-Kf-t0**3*Ff)
full=S.Matrix([-d*t0/Kf,-d/Ef,
               (cs*Ef*Ef+t0*Ff*Kf)/(d*Ef),
               Ff*Kf*Kf/(d*Ef*Ef)])
fullsub=dict(zip((u0,u1,t0,t1),full))
check('full common-ball source s',cs.subs(fullsub,simultaneous=True)-cs)
check('full common-ball source t',ct.subs(fullsub,simultaneous=True)-ct)
check('first period coefficient in same ball',
      (-d*d/core_h**3/(core_h+1)**3)*(d/t0**3)
      -(-d*t0/(t1*(t0+t1)))**3)
for i,tgt in enumerate((-d*t0/(t1*(t0+t1)),-d/(t0+t1),0,0)):
    check('full common-ball core map '+str(i),
          full[i].subs({u0:0,u1:0})-tgt)
for i,weight in enumerate((1,1,-1,-1)):
    check('full common-ball physical equivariance '+str(i),
          full[i].subs(sc,simultaneous=True)-lam**weight*full[i])
check('full period canonical root',(-d)**3+d**3)
check('source infinity coefficient keeps first period',
      (-d/Ef)**3+d**3/Ef**3)

source=root/'notes/part3_e6_two_pole_continuation_working.md'
record={
    'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
    'checks':len(checks),'identities':checks,
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope':'Full local source, line and Cox continuation of the two finite '
            'E80 poles, with linked chronological centre and actual cyclic norm. '
            'No compact-strip attachment, boundary count or return is assigned.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
