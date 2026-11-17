from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

root=Path(__file__).resolve().parents[2]
A,v,z,t,x=s.symbols('A v z t x')
T0=v**2-2*v
checks=[]

# Good fourth root. The source deck is (-X,-iY,iz).
B=s.I
D=B*(A**2-T0)/(2*v)
C=A*D/B-v
X=A*z**2+B;Y=C*z**3+D*z
equation=Y**2-(X**3+(1-2*v)*z**2*X**2+(1+T0*z**4)*X+v**2*z**6)
constraint=s.factor((A**2-T0)**2-4*v**2*(2*A+1-2*v))
assert s.expand(constraint-(A-v)**2*((A+v)**2+4*v))==0
assert s.rem(s.together(equation).as_numer_denom()[0],constraint,A)==0
X1=v*z**2+s.I;Y1=s.I*z
assert s.expand(Y1**2-(X1**3+(1-2*v)*z**2*X1**2+(1+T0*z**4)*X1+v**2*z**6))==0
X2=v*z**2-s.I;Y2=-s.I*z
slope=s.cancel((Y2-Y1)/(X2-X1))
sum_x=s.expand(slope**2-(1-2*v)*z**2-X1-X2)
sum_y=s.expand(-Y1+slope*(X1-sum_x))
assert sum_x==0 and sum_y==v*z**3
checks.extend(['good shifted-root exact section','good addition S+D*S=G','good cyclic norm is 2G'])

# Reduced third root. The parabola through the three D-orbit points
# meets -G; the displayed equations are precisely the coefficient identities.
F1=A**3-v*t*(t**2-3*A)-T0*t**2
F2=t**4-6*A*t**2-3*A**2-4*t**2+8*v*t**2-8*v*t
parabola=x**2/(t*z)+(t**2-3*A)*z*x/(2*t)-v*z**3
curve=x**3+(1-2*v)*z**2*x**2+(z+T0*z**4)*x+v**2*z**6
quartic=x*((x-A*z**2)**3-t**2*z**3)/(t**2*z**2)
diff=s.Poly(s.together(parabola**2-curve-quartic).as_numer_denom()[0],x)
G=s.groebner([F1,F2],A,t,v,z,order='grevlex')
for coeff in diff.all_coeffs():
    assert G.reduce(coeff)[1]==0
checks.append('reduced norm parabola coefficient identity modulo exact equations')
resultant=s.factor(s.resultant(F1,F2,t))
rho,E=s.symbols('rho E')
Xred=v*z**2+E**2*z
Yred=rho*E**2*z**2+E*z
red_eq=s.expand(Yred**2-(Xred**3+(1-2*v)*z**2*Xred**2+(z+T0*z**4)*Xred+v**2*z**6))
red_ideal=s.groebner([rho**2-1-v,E**3-1-rho],E,rho,v,z,order='grevlex')
assert red_ideal.reduce(red_eq)[1]==0
assert red_ideal.reduce(s.expand(F1.subs({A:v,t:E**3})))[1]==0
assert red_ideal.reduce(s.expand(F2.subs({A:v,t:E**3})))[1]==0
checks.append('reduced exact holomorphic section with rho^2=1+v and E^3=1+rho; cyclic norm G')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
     'checks':checks,
     'good_shifted_constraint':str(constraint),
     'good_exact_section':{'X':str(X1),'Y':str(Y1),'norm':'2G'},
     'reduced_constraints':[str(F1),str(F2)],
     'reduced_resultant':str(resultant),
     'reduced_exact_section':{'X':str(Xred),'Y':str(Yred),
         'branches':['rho^2=1+v, rho(0)=1','E^3=1+rho, E(0)^3=2'],
         'norm':'G'},
     'scope':'Exact source norm sections only. No global completed quotient, protected-cusp descent, line norm or return is inferred.'}
(root/'code/part3_fourfold/global_cap_norm_sections.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
