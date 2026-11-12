"""Exact finite diagnostics for the directional electric spectral calculation."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def eq(name,left,right=0):
    residual=s.simplify(s.expand(left-right))
    assert residual==0,(name,residual)
    checks.append({'name':name,'residual':str(residual)})
x,K,w,t,D,e,mu,R,A,B,z=s.symbols('x K w t D e mu R A B z',real=True)
positive_t=s.symbols('tau',positive=True)
a=(K+w*x)/2;b=(K-w*x)/2;rr=(w*w-K*K)*(1-x*x)/4
eq('first complete ellipsoid polynomial',s.integrate(a*a*b*b,(x,-1,1)),(K**4-s.Rational(2,3)*K*K*w*w+w**4/5)/8)
eq('second complete ellipsoid polynomial',s.integrate((a*a+b*b)*rr,(x,-1,1)),(w*w-K*K)*(5*K*K+w*w)/30)
eq('third complete ellipsoid polynomial',s.integrate(a*b*rr,(x,-1,1)),(w*w-K*K)*(5*K*K-w*w)/60)
eq('fourth complete ellipsoid polynomial',s.integrate(rr**2,(x,-1,1)),(w*w-K*K)**2/15)
# Independent azimuthal integration by exact moments of its cosine variable.
p=(A*A+R*R-(mu*A+z*R)**2)*(B*B+R*R-(mu*B-z*R)**2)
poly=s.Poly(s.expand(p),z)
means={0:1,1:0,2:e/2,3:0,4:3*e*e/8}
avg=sum(coef*means[power[0]] for power,coef in poly.terms())
claimed=e*e*A*A*B*B+(e*(1+mu*mu)*(A*A+B*B)/2-2*mu*mu*e*A*B)*R*R+(mu*mu+3*e*e/8)*R**4
eq('azimuthal average with original preferred axis',(avg-claimed).subs(e,1-mu*mu),0)
P=e*e*a*a*b*b+(e*(2-e)*(a*a+b*b)/2-2*(1-e)*e*a*b)*rr+(1-e+3*e*e/8)*rr**2
eq('full anisotropic ellipsoid integral',s.integrate(s.expand(P),(x,-1,1)),((w*w-K*K)**2+(w*w-K*K)*e*K*K+e*e*K**4)/15)
k1=s.symbols('k1',real=True);kp=K*K-k1*k1
density=(w*w-K*K)**2+(w*w-K*K)*kp+kp**2
eq('ultraviolet polynomial retains anisotropy',density,w**4-(K*K+k1*k1)*w*w+K**4-K*K*k1*k1+k1**4)
eq('three colours and bosonic pair coefficient',s.Rational(3,1)*2/4**2,s.Rational(3,8))
eq('density Fourier prefactor',s.Rational(3,8)/(2*s.pi)**6*s.pi/15,1/(2560*s.pi**5))
eq('Parseval ultraviolet factor',(2*s.pi)**3/(2560*s.pi**5),1/(320*s.pi**2))
# Integrating by parts: differentiating the proposed tail in its lower bound.
lap=s.exp(-t*K)*(kp**2/t+2*K*kp/t**2+(10*K*K-2*k1*k1)/t**3+24*K/t**4+24/t**5)
def mono_tail(n):
    return s.exp(-t*K)*sum(s.factorial(n)/s.factorial(n-r)*K**(n-r)/t**(r+1) for r in range(n+1))
eq('complete Laplace coefficients',lap,mono_tail(4)-(K*K+k1*k1)*mono_tail(2)+(K**4-K*K*k1*k1+k1**4)*mono_tail(0))
for n in (0,2,4):
    eq('monomial tail differentiation '+str(n),s.diff(mono_tail(n),K),-K**n*s.exp(-t*K))
u=s.symbols('u',real=True)
ir=2*s.pi*s.integrate(s.Rational(1,3)-(1+u*u)/5+(1-u*u+u**4)/7,(u,-1,1))/(2560*s.pi**5)
eq('infrared density coefficient',ir,1/(3360*s.pi**4))
eq('large-time norm coefficient',ir*s.factorial(7),3/(2*s.pi**4))
eq('large-time energy coefficient',ir*s.factorial(8),12/s.pi**4)
eq('large-time quotient factor',s.factorial(8)/s.factorial(7),8)
eq('small-time norm coefficient',s.factorial(4)/(320*s.pi**2),3/(40*s.pi**2))
eq('small-time energy coefficient',s.factorial(5)/(320*s.pi**2),3/(8*s.pi**2))
eq('small-time quotient factor',s.factorial(5)/s.factorial(4),5)
eq('directional angular integral',2*s.pi*s.integrate(1-u*u,(u,-1,1)),8*s.pi/3)
eq('directional one-momentum continuity integral',8*s.pi*s.factorial(3)/3,16*s.pi)
eq('full L1 continuity coefficient',s.Rational(3,8)*(16*s.pi)**2/(2*s.pi)**6,3/(2*s.pi**4))
eq('nonnegative derivative symbol decomposition',K**4-K*K*k1*k1+k1**4,kp*kp+k1*k1*kp+k1**4)
report={'exact_checks':len(checks),'all_passed':True,'results':checks,
 'scope':'Finite exact ellipsoid, azimuthal, Fourier, Laplace and moment identities. Full analytical graph and regulator limits are proved in the retained source.',
 'sources':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in ['sources/directional_electric_spectrum.md','check_directional_electric_spectrum.py']}}
(root/'DIRECTIONAL_ELECTRIC_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_checks':len(checks),'all_passed':True}))
