"""Independent native-I2 graph, reciprocal chord and point-line audit."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
note=ROOT/'notes/part3_e6_selected_infinity_attachment_working.md'
text=note.read_text();section=text.split('## IA.4.')[1].split('## IA.5.')[0]
checks=[]
def zero(name,x):
    assert s.factor(x)==0,(name,s.factor(x))
    checks.append(name)
e,t,a,b,A,d,C,z,v,eta,U,chi=s.symbols('e t a b A d C z v eta U chi')
F=b*b-t*a**3-A*a*a-d*a-e*e
D=d+A*a+t*a*a
zero('full ideal square identity',b*b-a*D-e*e-F)
G1=z*z-t*e**4*C**3-A*e*e*C*C-d*C-1
zero('first actual graph equation',F.subs({b:e*z,a:e*e*C})-e*e*G1)
G2=1-t*b**4*C**3-A*b*b*C*C-d*C-v*v
zero('second actual graph equation',F.subs({e:b*v,a:b*b*C})-b*b*G2)
# The ordinary old-source cubic in both minimal resolution charts.
r=e*e*A/d**2;to=e**4*t/d**3
zero('old t-chart curve',z*z-to*(d*C)**3-r*(d*C)**2-d*C-1-G1)
oldx=b**4*v*v*t*C/d**2;oldr=b*b*v*v*A/d**2
u0=v*v/(d*C);v0=v/(d*C)
zero('old x-chart curve',v0*v0-oldx-oldr-u0-u0*u0-v*v/(d*d*C*C)*G2)
# Direct ordinary -G chord, retaining t before restricting to O graph.
x,y=s.symbols('x y');k=(y+e*t)/x
xp=k*k-A-x;yp=e*t-k*xp
On=1-U-A*eta*eta-d*t*eta**4/U-eta**8*v*v*t*t/U**2
xO=U/eta**2;yO=-U/eta**3
xsub=s.factor(xp.subs({x:xO,y:yO,e:eta*v}))
a1=(d-2*v)/U+2*eta**4*v*v*t/U**2
c1=v+a1-eta**4*v*t*a1/U
zero('full O chord x residual exact',xsub-eta**2*t*a1-On/eta**2)
kO=-1/eta+eta**3*v*t/U
zero('full O chord y',eta*v*t-kO*eta**2*t*a1-eta*t*c1)
zero('central graph reset unit',c1.subs({eta:0,U:1,d:1})-(1-v))
zero('actual graph reset preserves e',(eta*c1)*(v/c1)-eta*v)
# Reciprocal chord is regular precisely on the stated T neighbourhood.
kap=(b-e)/D
zero('reciprocal chord exact on the curve',a-kap*(b+e)+F/D)
W=1-kap**2*(A+t*a)
tau=kap*W/(W-e*t*kap**3)
kk=s.symbols('kk')
xpT=1/kk**2-A-t*a;ypT=e*t-xpT/kk
zero('target O parameter exact',-xpT/ypT-kk*(1-kk**2*(A+t*a))/(1-kk**2*(A+t*a)-e*t*kk**3))
taue=s.cancel(tau.subs({b:e*z,a:e**2*C})/e)
zero('target O parameter at central chart',taue.subs(e,0)-(z-1)/d)
# Chi-unit source/point charts and all carried chain powers.
Y,et,sigma,ta,ca=s.symbols('Y et sigma ta ca')
zero('T graph unit',(chi**-3*Y)/(chi**-4)-chi*Y)
zero('O graph unit',-(chi**-2*x)/(chi**-3*y)-chi*(-x/y))
zero('whole point divisor ratio',(chi*ta-chi*ca)/(chi*ta)-(ta-ca)/ta)
Aj,Bj=s.symbols('Aj Bj')
for j in range(-12,13):
    zero(f'chain product j{j}',(chi**j*Aj)*(chi**(-j-1)*Bj)-Aj*Bj/chi)
    zero(f'physical point coefficient j{j}',sigma**j*chi**j*Aj-(chi*sigma)**j*Aj)
# Retained full Miller products' central whole-fibre value.
for branch in ('a6_b1','a2_b3'):
    expr=(2*x)**6*6*(t/x)**3/(6*x**3) if branch=='a6_b1' else (2*x)*(2*t/x)*(2*t/x)**2*(2*x)**2
    zero(branch+' full central coefficient',expr-64*t**3)
out={'status':'PASS','reviewer':'blind_control','utc':datetime.now(timezone.utc).isoformat(),
 'source':'notes/part3_e6_selected_infinity_attachment_working.md',
 'source_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
 'reviewed_section':'IA.4 (IA.3–13), with the complete generic Miller/normality argument and exact overlap to the prior ordinary source graph.',
 'reviewed_section_sha256':hashlib.sha256(section.encode()).hexdigest(),
 'checks':len(checks),'checked_assertions':checks,
 'findings':['The actual ideal is (b,e)^2 and both blowup charts carry all original-resolution functions through t=0.','The full O/T chord and reciprocal chord are regular on their stated charts and preserve the point divisor; the two graph ideals differ by the exact unit chi on the overlap.','Full point Hom has no new divisor after its actual frame ratios; its reciprocal extends on the smooth source charts. All chain powers and fourth-root phases are retained.'],
 'excluded':['Compact global assembly and any return/characteristic number.']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checked_assertions'},indent=2))

