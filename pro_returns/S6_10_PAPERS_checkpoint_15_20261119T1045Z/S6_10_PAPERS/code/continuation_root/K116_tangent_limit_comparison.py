"""Fresh post-comparison check of the printed additional tangent-doubling route."""
from pathlib import Path
import sympy as s
import json, datetime
a,z=s.symbols('a z',nonzero=True)
R=1+a*z*z;F=R*R+z**3
points={1:(R,z**3/2)} # second coordinate is Y/sqrt(3)
steps=[]
for m in [1,2,4]:
    X,E=points[m]
    slope=s.cancel((X**2-F)/(2*E))
    XX=s.cancel(3*slope**2-2*X)
    EE=s.cancel(-E+slope*(X-XX))
    points[2*m]=(XX,EE)
    steps.append({'multiple':2*m,'X':str(XX),'Y_over_sqrt3':str(EE)})
x8=s.cancel(points[8][0]).subs(z,0)
y8=s.cancel(points[8][1]).subs(z,0)
wantx=(81*a**6-90*a**3+1)/(9*a**3+1)**2
wanty=108*a**3*(9*a**3-1)/(9*a**3+1)**3
assert s.cancel(x8-wantx)==0,(x8,wantx)
assert s.cancel(y8-wanty)==0,(y8,wanty)
out={'status':'passed','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':'three new exact rational tangent doublings in (X,Y/sqrt3), followed by cancellation and specialization',
 'scope':'O45P.25 additional tangent-doubling equality; program written after the printed assertion was read, without reading its former producing code. No additional prereading proof claim.',
 'X8_at_zero':str(s.factor(x8)),'Y8_over_sqrt3_at_zero':str(s.factor(y8)),'steps':steps}
target=Path(__file__).with_suffix('.output.json');target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='steps'},indent=2))
