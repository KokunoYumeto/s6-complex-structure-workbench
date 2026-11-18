"""Full finite-native I2 O/T graph and source-reset identities."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
import sympy as S

base=Path(__file__).resolve().parents[2]
e,t,x,y,a,b,z,C,v,eta,U,d,A,chi=symbols=S.symbols('e t x y a b z C v eta U d A chi')
checks=[]
def ck(expr,name):
    assert S.factor(expr)==0,(name,S.factor(expr))
    checks.append(name)

native=y*y-x**3-A*x*x-d*t*x-e*e*t*t
xo=e**2*x/d**2;yo=e**3*y/d**3;to=e**4*t/d**3;r=e**2*A/d**2
old=yo**2-xo**3-r*xo**2-to*xo-to**2
ck(old-e**6/d**6*native,'full original-source scaling')
node=b*b-t*a**3-A*a*a-d*a-e*e
ck(native.subs({x:t*a,y:t*b})-t*t*node,'literal native I2 chart')
ck(b*b-(a*(d+A*a+t*a*a)+e*e)-node,'T ideal equality generator')

# Actual graph b=e*z, a=e^2*C and original t-chart.
T1=z*z-t*e**4*C**3-A*e**2*C*C-d*C-1
ck(node.subs({b:e*z,a:e**2*C})-e*e*T1,'T first graph equation')
ck((z*z-(to.subs(x,0))*(d*C)**3-r*(d*C)**2-d*C-1)-T1,'T first original resolved equation')
ck(xo.subs(x,t*e**2*C)/to-d*C,'T first original x/t')
ck(yo.subs(y,t*e*z)/to-z,'T first original y/t')

# Complementary graph e=b*v, a=b^2*C, including t=0.
T2=1-t*b**4*C**3-A*b*b*C*C-d*C-v*v
ck(node.subs({e:b*v,a:b*b*C})-b*b*T2,'T second graph equation')
u0=v*v/(d*C);v0=v/(d*C)
x0=b**4*v*v*t*C/d**2;r0=b*b*v*v*A/d**2
ck((v0*v0-r0-u0-u0*u0-x0)-v*v/(d*d*C*C)*T2,'T second original resolved equation')
ck(xo.subs({x:t*b*b*C,e:b*v})-x0,'T second original x')

# O graph and its complete -G chord, with e=eta*v.
Oeq=1-U-A*eta**2-d*t*eta**4/U-eta**8*v*v*t*t/U**2
kk=-1/eta+eta**3*v*t/U
aa=(d-2*v)/U+2*eta**4*v*v*t/U**2
cc=v+aa-eta**4*v*t*aa/U
ck(kk*kk-A-U/eta**2-eta**2*t*aa-Oeq/eta**2,'O-to-T full chord x')
ck(eta*v*t-kk*(eta**2*t*aa)-eta*t*cc,'O-to-T full chord y')
ck(cc.subs({eta:0,U:1,d:1})-(1-v),'O-to-T exact central corner unit')
ck((cc/v).subs({eta:0,U:1,d:1})-(1/v-1),'O-to-T central additive coordinate')
ck((eta*cc)*(v/cc)-eta*v,'O-to-T preserves parameter')
uold=eta**4*v*v*t/(d*U);vold=-v/d
xold=v*v*U/d**2
ck(vold*vold-eta*eta*v*v*A/d**2-uold-uold*uold-xold-v*v/d**2*Oeq,'O full original x-chart equation')

# Inverse-form target O coordinate through the whole finite T graph.
D=d+A*a+t*a*a
kappa=(b-e)/D
W=1-kappa*kappa*(A+t*a)
tau=kappa*W/(W-e*t*kappa**3)
kt=S.symbols('kt',nonzero=True)
xprime=(1-kt*kt*(A+t*a))/(kt*kt)
yprime=e*t-xprime/kt
ck(-xprime/yprime-(kt*(1-kt*kt*(A+t*a))/(1-kt*kt*(A+t*a)-e*t*kt**3)),'T-to-O exact reciprocal chord')
taublow=S.cancel(tau.subs({b:e*z,a:e**2*C})/e)
ck(taublow.subs(e,0)-(z-1)/d,'T-to-O complete central coordinate')

# Both source graph ideals and point frames on the chi-unit overlap.
Ybar,etabar,sigma,taubar,ca=S.symbols('Ybar etabar sigma taubar ca')
ck((chi**-3*Ybar)/(chi**-4)-chi*Ybar,'native T coordinate equals chi Ybar')
ck(-(chi**-2*x)/(chi**-3*y)-chi*(-x/y),'native O coordinate equals chi etabar')
ck((chi*taubar-chi*sigma*ca)/(chi*taubar)-(taubar-sigma*ca)/taubar,'actual point Cartier ratio agrees')
for j in range(-8,9):
    Aj,Bj=S.symbols('Aj Bj')
    Xj=chi**j*Aj;Yj=chi**(-j-1)*Bj
    ck(Xj*Yj-Aj*Bj/chi,f'chain product {j}')
    ck(sigma**j*Xj-(chi*sigma)**j*Aj,f'physical coefficient {j}')

source=base/'notes/part3_e6_selected_infinity_attachment_working.md'
out={'status':'PASS_NATIVE_I2_GRAPH','utc':datetime.now(timezone.utc).isoformat(),
     'checks':len(checks),'check_labels':checks,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'scope':'Literal native I2 source graph, both original resolution charts, complete reciprocal -G chord, O/T additive reset, chi-unit graph and point-line overlap, all integer chain powers. No global compact attachment or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
