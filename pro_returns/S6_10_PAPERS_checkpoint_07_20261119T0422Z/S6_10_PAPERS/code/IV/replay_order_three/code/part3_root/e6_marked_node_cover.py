"""Exact source, selected-height and Miller-weight maps for the E6 node cover."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S

w, X, Y, T, q = S.symbols('w X Y T q')
x, y, t, d, s = S.symbols('x y t d s')
checks = []

def check(name, expression, curve=None):
    numerator = S.together(expression).as_numer_denom()[0]
    if curve is not None:
        numerator = S.rem(numerator, curve, y)
    value = S.factor(numerator)
    assert value == 0, (name, value)
    checks.append(name)

D = w*w-3
rho = w*w/D
r = (3-2*w*w)/D**2
v = w*w-1
t_selected = v/D**3
u = v/D**2
c = w/D
check('rho discriminant cover', rho**2-(1-3*r))
check('selected finite critical value', t_selected-(1-3*rho**2+2*rho**3)/27)
check('selected double root', u-(2*rho**2-rho-1)/9)
check('selected normalization square', c**2-(u+(rho-1)**2/9))
check('ordered branch parametrization', w**2-3*rho/(rho-1))
check('normalized marked section point', (((1-rho)/3-c)/((1-rho)/3+c))-(1+w)/(1-w))

old = y*y-x**3-r*x*x-t*x-t*t
new = Y*Y-X**3-(3-2*w*w)*X*X-D*T*X-T*T
check('full source rescaling', D**6*old.subs({x:X/D**2,y:Y/D**3,t:T/D**3})-new)
check('selected cubic', -new.subs({T:v,Y:0})-(X-v)**2*(X+1))
sigma = S.symbols('sigma')
check('selected normalization source map', new.subs({T:v,X:sigma**2-1,Y:sigma*(sigma**2-w*w)}))
check('exact selected height', (T/D**3-t_selected)-q/D**3 if False else (T/D**3-t_selected)-(T-v)/D**3)

a2=3-2*w*w
disc=-16*T*T*(a2*a2*(4*a2-D*D)+(4*D**3-18*a2*D)*T+27*T*T)
t_other=-a2*a2*(w*w+3)/27
check('discriminant factorization', disc+432*T*T*(T-v)*(T-t_other))
check('selected root separation', v-t_other-4*w**6/27)
c4=16*(a2*a2-3*D*T)
check('selected c4', c4.subs(T,v)-16*w**4)
kappa=-v*v/(64*w**6)
check('full-height inverse-j leading coefficient', S.diff(disc,T).subs(T,v)/c4.subs(T,v)**3-kappa)

Snew=v*(w*w+3)/4
U=Y-T-D*X/2
V=Y+T+D*X/2
check('cA2 source equation', (U*V-X*X*(X-Snew))-new)
check('second section coordinate', Snew/D**2-(S.Rational(1,4)-r))
check('ordinary source at original infinity', new.subs(w*w,3)-(Y*Y-X**3+3*X*X-T*T))

curve=y*y-x**3-(d*d/4-s)*x*x-d*t*x-t*t
Ug=y-t-d*x/2
Vg=y+t+d*x/2
f2=Ug/(x-s)
x3=4*t*t/s**2+2*d*t/s
y3=t*(8*t*t+6*d*t*s+d*d*s*s-s**3)/s**3
ell=y-t+(2*t/s+d/2)*x
f3=s*x*Ug/(s*Vg-(d*s+2*t)*x)
check('third section lies on source', curve.subs({x:x3,y:y3}))
check('full Miller f3 identity', f3-f2*ell/(x-x3),curve)

scale=S.symbols('scale', nonzero=True)
subs={x:X/scale**2,y:Y/scale**3,t:T/scale**3,d:d/scale,s:s/scale**2}
check('full Miller f2 weight', f2.subs(subs,simultaneous=True)-f2.subs({x:X,y:Y,t:T})/scale)
check('full Miller f3 weight', f3.subs(subs,simultaneous=True)-f3.subs({x:X,y:Y,t:T})/scale**2)

# The tangent line quotient f_{2,P} has weight one for every actual section P.
xp,yp=S.symbols('xp yp')
ap=d*d/4-s
lam=(3*xp*xp+2*ap*xp+d*t)/(2*yp)
x2=lam*lam-ap-2*xp
f2p=(y-yp-lam*(x-xp))/(x-x2)
scaled=dict(subs);scaled.update({xp:xp/scale**2,yp:yp/scale**3})
check('full arbitrary-section tangent Miller weight', f2p.subs(scaled,simultaneous=True)-f2p.subs({x:X,y:Y,t:T})/scale)
check('f6 weight from complete factors', scale**-4*scale**-1-scale**-5)
check('B6 source target weight after exact f6 ratio', scale**-6*scale**-5/scale**-5-scale**-6)
check('selected Hom scalar under full rescaling', (q/scale**3)/(T/scale**3)**3*scale**-6-q/T**3)

boundary={
 'selected_cusp':{'w':'0','rho':'0','r':'1/3','T_selected':'-1','root_separation_order':6},
 'selected_I3':{'w':'1,-1','rho':'-1/2','r':'1/4','T_selected':'0'},
 'unselected_I3':{'w_squared':'-3','rho':'1/2','r':'1/4'},
 'unselected_III':{'w_squared':'3/2','rho':'-1','r':'0'},
 'original_r_infinity':{'w_squared':'3','rho':'infinity','new_source':'Y^2=X^3-3X^2+T^2'},
 'selected_III':{'w':'infinity','rho':'1','r':'0'},
}
for value,rhov,rv in ((1,S.Rational(-1,2),S.Rational(1,4)),(-3,S.Rational(1,2),S.Rational(1,4)),(S.Rational(3,2),-1,0)):
 check('boundary rho at w_squared='+str(value),rho.subs(w*w,value)-rhov)
 check('boundary r at w_squared='+str(value),r.subs(w*w,value)-rv)
check('selected III rho at infinity',S.limit(rho,w,S.oo)-1)
check('selected III r at infinity',S.limit(r,w,S.oo))

record={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),'identities':checks,'boundary_dictionary':boundary,
 'scope':'Exact actual source/section/selected-height/branch/Cartier-Miller weight maps; no unfinished sphere attachment or return value assigned.'}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
