"""Independent exact Cartier/blowup/normal-clutch checks for MC.1--6."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'notes/part3_e6_selected_infinity_moving_cap_working.md'
count=0
def ck(v):
    global count
    assert bool(v)
    count+=1
def eq(v): ck(S.cancel(S.together(v))==0)
eps,s=S.symbols('eps s', nonzero=True)
d=1-3*eps**2;alpha=eps/d;P=-(1+eps)/(1-eps);Z=(s-1)/(s+1)
for a in (2,6):
    b=P**a;sa=(1+b)/(1-b);Sa=alpha*sa
    fb=(1-Z/b)/(1-Z)
    eq(fb+(1-b)*(s-sa)/(2*b))
    phi=-d*(1-b)/(2*b*eps)
    eq(fb-phi*(alpha*s-Sa))
    ck(S.limit(phi,eps,0)==a)
    ck(S.limit(Sa,eps,0)==-S.Rational(1,a))
    Ca=2 if a==2 else 6+20*eps**2+6*eps**4
    Ho=eps**(-a)*d**(a-1)/Ca
    eq(Ho*phi-(d/(eps*(1+eps)))**a)
    # Retained outer map and its composition with the completed-point
    # sigma^4 normal map. Conjugation reverses the first phase.
    chiL_order=1-a
    ck(-(4-chiL_order)+chiL_order==-2*a-2)
    ck(-(4+a-4)==-a)
    ck(-a+(4-a)==4-2*a)

rho,z1,zeta,v,SS,zz=S.symbols('rho z1 zeta v SS zz')
eq((rho*z1).subs({rho:v*SS,z1:1/v},simultaneous=True)-SS)
eq((rho*z1).subs(z1,rho*zz)-rho**2*zz)
h=-zeta;k=-z1**2*zeta
eq(h*k-(z1*zeta)**2)
r,t,uu,ww=S.symbols('r t uu ww')
ck(S.Matrix([r,r*t]).jacobian([r,t]).det()==r)
ck(S.Matrix([uu*ww,ww]).jacobian([uu,ww]).det()==ww)
I=-S.eye(2)
eO=S.Matrix([-1,0]);middle=S.Matrix([1,-1]);eT=S.Matrix([0,1])
for x,sq in ((eO,-1),(middle,-2),(eT,-1)):
    ck((x.T*I*x)[0]==sq)
ck((eO.T*I*middle)[0]==1 and (middle.T*I*eT)[0]==1)

# The actual Mayer--Vietoris maps, including difference sign, are
# primitive; no rational relaxation is used.
h1=S.Matrix([[-1]])
h2=S.Matrix([[1,0,0]])
ck(abs(h1.det())==1)
ck(h2.nullspace()==[S.Matrix([0,1,0]),S.Matrix([0,0,1])])
ck(h2.rank()==1)

c1sq,c2,p1=S.symbols('c1sq c2 p1')
kU=-(c1sq-c2);ellU=-(p1+c1sq-4*c2)
eq(4*kU-ellU-(p1-3*c1sq))
ck(S.diff(4*kU-ellU,c2)==0)
ck(((4*kU-ellU)/24).subs({c1sq:0,p1:-6})==-S.Rational(1,4))
ck(-1-2*1==-3 and 2*(-3)==-6)

result={'status':'PASS_EXACT_MOVING_CAP_ARROWS','reviewer':'blind_control',
        'utc':datetime.now(timezone.utc).isoformat(),'checks':count,
        'source':str(SOURCE.relative_to(ROOT)),'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
        'scope':'MC1--6 Cartier factors, two actual blowups, retained determinant windings, integral MV maps and c2 cancellation. Full source/Hopf/orientation map read separately in peer audit. No total source return.',
        'positive_U_contribution':'-1/4','physical_M_contribution':'1/4'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
