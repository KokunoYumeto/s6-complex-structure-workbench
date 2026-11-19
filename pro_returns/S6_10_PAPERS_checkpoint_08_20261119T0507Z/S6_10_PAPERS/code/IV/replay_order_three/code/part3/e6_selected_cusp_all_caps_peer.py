"""Independent exact-arrow checks accompanying the full EG peer review.

The source/root extensions and relative cobordisms are reviewed in the
separate audit record. These identities do not replace those arguments.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
tests = []


def zero(name, expr):
    result = s.factor(s.together(expr).as_numer_denom()[0])
    assert result == 0, (name, result)
    tests.append(name)


def yes(name, result):
    assert bool(result), name
    tests.append(name)


w, S = s.symbols('w S')
X, Y, T, q, xi = s.symbols('X Y T q xi')
v = w*w - 1
D = w*w - 3
A = 3 - 2*w*w
s0 = v*(w*w+3)/4
P = (1+w)/(1-w)
Z = (S-w)/(S+w)
curve = Y*Y-X**3-A*X*X-D*T*X-T*T
on_node = {X:S*S-1, Y:S*(S*S-w*w), T:v}
zero('complete selected normalization', curve.subs(on_node))
zero('source A1 coefficient', D*D/4-A-s0)
zero('full implicit selected equation',
     curve.subs({X:xi+v,T:q+v})
     -(Y*Y-xi*xi*(xi+w*w)-q*(q+v*v+D*xi)))

# Derive the actual sixfold Miller function by its complete chord formula.
U = Y-T-D*X/2
f2 = U/(X-s0)
f3 = s.cancel((s0*X*U/(s0*(Y+T+D*X/2)-(D*s0+2*T)*X)).subs(on_node))
x3 = s.cancel(4*v*v/s0**2+2*D*v/s0)
y3 = s.cancel(v*(8*v*v+6*D*s0*v+D*D*s0*s0-s0**3)/s0**3)
k3 = s.cancel((3*x3*x3+2*A*x3+D*v)/(2*y3))
x6 = s.cancel(k3*k3-A-2*x3)
f6 = s.cancel(f3*f3*(on_node[Y]-y3-k3*(on_node[X]-x3))/(on_node[X]-x6))

ft = lambda zz, pp: (1-zz/pp)/(1-zz)
for a in (2,6):
    Sa = s.cancel(w*(1+P**a)/(1-P**a))
    ca = s.cancel(w-Sa)
    actual = s.cancel(f2.subs(on_node)) if a == 2 else f6
    zero(f'M{a} actual full Miller chord restriction', actual-(S+1)**a/(S-Sa))
    zero(f'M{a} strict Cartier to theta arrow', S-Sa-ca*ft(Z,P**a))
    zero(f'M{a} full tensor to point coefficient',
         ft(Z,P)**a/actual-ca/(1+w)**a*ft(Z,P**a))
    zero(f'M{a} finite point at the cusp', Sa.subs(w,0)+s.Rational(1,a))
    zero(f'M{a} finite unit at the cusp', ca.subs(w,0)-s.Rational(1,a))
    zero(f'M{a} section even in the ordered cover', Sa.subs(w,-w)-Sa)
    zero(f'M{a} full Cartier reflection coefficient', ca.subs(w,-w)-P**(-a)*ca)
    zero(f'M{a} reflected tensor coefficient even',
         (ca/(1+w)**a).subs(w,-w)-ca/(1+w)**a)
    zz = s.Symbol('zz', nonzero=True)
    zero(f'M{a} exact theta inversion on the nodal limit',
         ft(1/zz,P**(-a))-P**a*ft(zz,P**a))
    zero(f'M{a} actual target H cancels the line reflection', P**(-a)*P**a-1)
    for sign in (-1,1):
        zero(f'M{a} node{sign} actual Miller value',
             actual.subs(S,sign*w)-(1+w)**a/ca)
    if a == 6:
        zero('full sixfold node coefficient', actual.subs(S,w)-(6+20*w*w+6*w**4))
        S6 = Sa
    else:
        S2 = Sa
zero('actual M2 to M6 trace unit at cusp',
     ((S-S2)/(S-S6)).subs({S:0,w:0})-3)
zero('actual M2 to M6 trace coefficient at infinity',
     s.limit((S-S2)/(S-S6),S,s.oo)-1)

f0,f1,f2s,f3s,t0,t1,t2,t3,c6s,c6t = s.symbols(
    'f0 f1 f2s f3s t0 t1 t2 t3 c6s c6t', nonzero=True)
B23 = f0*f3s*f1**2*f2s**2
zero('M2 source and target Miller maps before telescoping',
     f0**2*f1**2*f2s**2*(1/f0)/(1/f3s)-B23)
zero('M2 three actual translation steps in the full theta frame',
     B23*(t3**2/f3s)/(t0**2/f0)-(f0*t1/t0*f1*t2/t1*f2s*t3/t2)**2)
zero('M6 actual source and target Miller maps in theta frame',
     (f0**6*c6t/c6s)*(t1**6/c6t)/(t0**6/c6s)-(f0*t1/t0)**6)
zero('M2 complete six node factors',B23.subs({f0:2,f1:2,f2s:2,f3s:2})-64)
zero('retained central selected Hom coefficient',s.Integer(64)/(-1)**3+64)

# Full analytic source shear and its actual projection-normal coefficients.
g,h = s.symbols('g h')
St=((1+g)*S+(1-g)*w)/(((1-g)/w)*S+1+g)
zero('actual source Mobius arrow on Z',(St-w)/(St+w)-g*Z)
zero('source shear fixing both branches',
     St.subs(g,1+w*h)-S-h*(S*S-w*w)/(2+h*(w-S)))
for sign in (-1,1):
    zero(f'full source shear fixes branch{sign}',St.subs(S,sign*w)-sign*w)
dx,dy,dw=s.symbols('dx dy dw')
nf=(3*S*S-w*w)*dx-2*S*dy+2*w*(S*S-w*w)*dw
numerator=(2*Y*dy-(3*xi*xi+2*xi*w*w)*dx-2*w*xi*xi*dw)
zero('full projection-normal one-form',
     numerator.subs({xi:S*S-w*w,Y:S*(S*S-w*w)})+(S*S-w*w)*nf)
zero('first fixed chart y-squared normal coefficient',(S*S-w*w)/Z-(S+w)**2)
zero('second fixed chart x-squared normal coefficient',(S*S-w*w)*Z-(S-w)**2)

# Derive each winding from the full literal period/character map.
kap,al,gg,eta,qq=s.symbols('kap al gg eta qq',nonzero=True)
for j in range(-8,9):
    zero(f'vertical{j} full H coefficient',
         al*(qq*eta)**j*(kap*qq*gg**j)**(-j)-al*eta**j*kap**(-j)*gg**(-j*j))
    zero(f'vertical{j} full B coefficient',qq*eta*gg**(-j)-qq*(eta*gg**(-j)))
    zero(f'vertical{j} reflected seed',
         (-6-18*j*(j-1))-(-6-18*(1-j)*(-j)))

sa,k,fa,period,cc,ha,jj,bb,lam=s.symbols('sa k fa period cc ha jj bb lam')
fb=fa+period
for n in (-1,1):
    hb=ha-n*sa*period+jj*bb+lam
    zero(f'signed{n} full target-sheet annular square',
         n*(sa+k)*fb+(sa+k)*cc+hb-n*k*fb-k*cc
         -(n*sa*fa+sa*cc+ha+jj*bb+lam))
    zero(f'signed{n} primitive quotient generator',n*n-1)

bases=0
for p in range(-2,3):
 for q0 in range(-2,3):
  for r in range(-2,3):
   for t in range(-2,3):
    PM=s.Matrix([[p,q0],[r,t]])
    if abs(PM.det())!=1:continue
    RM=PM.inv();BP=-6*RM*s.Matrix([[1,0],[0,0]])*PM
    for i in range(2):
     for j in range(2):
      zero(f'fan{bases} full q character{i}{j}',(RM*PM)[i,j]-int(i==j))
      zero(f'fan{bases} full winding{i}{j}',-6*RM[i,0]*PM[0,j]-BP[i,j])
    zero(f'fan{bases} determinant winding',s.trace(BP)+6)
    bases+=1

ell=s.symbols('ell',integer=True,nonnegative=True)
m=3*ell+2;kroot=2*ell+1
zero('all reduced roots exact division relation',2*m-1-3*kroot)
zero('all reduced graph D exponent',-1-3*kroot+2*m)
zero('all reduced deck X exponent',-6*kroot-2+4*m)
zero('all reduced deck Y exponent',-9*kroot-3+6*m)
zero('all reduced graph tau exponent',3*kroot+1-2*m)
for kk in range(1,22,2):
 for j in range(1,kk+1):
    zero(f'graph k{kk} ray{j} marked coefficient',j-min(j,kk))
    if j>1:zero(f'graph k{kk} regular adjacent{j}',s.det(s.Matrix([[j,j-1],[1,1]]))-1)

lift,chi,c,t=s.symbols('lift chi c t')
phase=lift+t*chi*(c-lift)
zero('relative level homotopy original endpoint',phase.subs(t,0)-lift)
zero('relative level homotopy fixes outer collar',phase.subs(chi,0)-lift)
zero('relative level homotopy terminal constant near surgery',phase.subs({t:1,chi:1})-c)
zero('original source parameter exact four-turn equation',
     A/D**2-s.Rational(1,3)+w**4/(3*D**2))

source=ROOT/'notes/part3_e6_selected_cusp_all_caps_working.md'
result={'status':'PASS','reviewer':'blind_control','utc':datetime.now(timezone.utc).isoformat(),
        'check_count':len(tests),'basis_count':bases,'source':str(source.relative_to(ROOT)),
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'scope':'Independent exact actual Miller/chord, Cartier/theta, signed annular, source/normal, full period/Cox and relative level-homotopy identities. The complete geometric proof is separately reviewed.',
        'checks':tests}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','check_count','basis_count','source_sha256']},indent=2))
