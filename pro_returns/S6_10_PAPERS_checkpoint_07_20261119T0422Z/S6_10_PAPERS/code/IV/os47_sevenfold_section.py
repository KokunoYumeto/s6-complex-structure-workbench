"""Independent exact group-law check of the section used in P3F.21."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
import sympy as s
started=datetime.now(timezone.utc).isoformat()
t=s.symbols('t')
f=1+8*t+40*t**2+48*t**3
g=1+12*t+84*t**2+280*t**3+504*t**4
G=(1+4*t,12*t**2) # y=sqrt(3)*Y
cancel=s.cancel
def add(P,Q):
    x,y=P;u,v=Q
    slope=cancel((x*x-f)/(2*y) if P==Q else (v-y)/(u-x))
    xn=cancel(3*slope*slope-x-u)
    yn=cancel(-y+slope*(x-xn))
    assert cancel(3*yn*yn-xn**3+3*f*xn-2*g)==0
    return xn,yn
assert s.expand(3*G[1]**2-G[0]**3+3*f*G[0]-2*g)==0
P2=add(G,G);P4=add(P2,P2);P6=add(P4,P2);P7=add(P6,G)
claimed=-(140*t**3-609*t**2-420*t+92)/(t+10)**2
assert cancel(P7[0]-claimed)==0
num,den=s.fraction(P7[0])
assert num.subs(t,-10)!=0 and s.factor(den)==(t+10)**2
assert s.factor(g*g-f*f*f)==-1728*t**7*(64*t*t+13*t+2)
out=Path(__file__).resolve().parents[2]/'analysis/IV/os47_sevenfold_section_check.json'
result={'started_utc':started,'completed_utc':datetime.now(timezone.utc).isoformat(),
        'verdict':'passed exact rational-function identities',
        'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'x_7G':str(s.factor(P7[0])),'Y_7G':str(s.factor(P7[1])),
        'independent_binary_addition_chain':[1,2,4,6,7],
        'pole_at_minus10':{'x_order':2,'numerator_value':str(num.subs(t,-10))},
        'discriminant_polynomial':str(s.factor(g*g-f*f*f)),
        'scope':'The rational group law and ordinary pole. Resolution component indices, topology and orientation are separate proof checks.'}
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
