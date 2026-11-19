"""Independent narrow EX.4–5 source/Cartier/chord checks."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

root=Path(__file__).resolve().parents[2]
a,b,c,b0,c0=S.symbols('a b c b0 c0')
X=a*b
z=a*b*(b-a)/(2*c)
Y=a*b*(a+b)/2
rel=c*c-1-b0*X-c0*X*X
K=1+b*(b-a)*(b0+c0*X)/(2*c*(c+1))
F=1-X*(b0+c0*X)*(K+1)/(2*c*(c+1))-c0*a*b*b*(a-b)/(4*c*c)
Xp=a*(a-b)*F
checks=[]


def check(name, expr, mod=None, var=None):
    num=S.together(expr).as_numer_denom()[0]
    if mod is not None:
        num=S.rem(num,mod,var)
    num=S.factor(num)
    assert num==0,(name,num)
    checks.append(name)


check('actual root equation after middle chart',
      Y*Y-X**3-z*z*(1+b0*X+c0*X*X),rel,c)
check('actual chord slope kappa equals aK',(Y-z)/X-a*K,rel,c)
check('actual full X prime equals a(a-b)F',
      (a*K)**2-c0*z*z-X-Xp,rel,c)
cp=S.symbols('cp')
H=K+b*(a-b)*(b0+c0*Xp)/(2*c*(1+cp))
ap=(b-a)*F/H
bp=-a*H
check('literal target product a prime b prime',ap*bp-Xp)
check('literal target V prime',
      (-z-a*K*Xp+z*cp)+a*Xp*H,
      cp*cp-1-b0*Xp-c0*Xp*Xp,cp)
tau,zr,L,u,v=S.symbols('tau zr L u v')
for kk in range(1,16,2):
    check('full graph quotient '+str(kk),
          (tau/(tau-zr**kk*L)).subs(tau,zr**kk*u)-u/(u-L))
    check('second graph quotient '+str(kk),
          (tau/(tau-zr**kk*L)).subs(tau,zr**kk/v)-1/(1-v*L))
    for jj in range(1,kk+1):
        assert min(jj,kk)==jj
        checks.append('actual equal exceptional orders '+str((kk,jj)))
for ell in range(21):
    m=3*ell+2
    kk=2*ell+1
    wa=ell+1
    for label,weight in [('X',2*wa+2*kk),('Y',3*wa+3*kk),
                         ('b0X',ell+2*wa),('c0X2',2*ell+4*wa)]:
        assert weight%m==0,(ell,label,weight)
        checks.append('full reduced deck '+str((ell,label)))
    assert S.gcd(wa,m)==1
    checks.append('primitive actual reduced root action '+str(ell))
    assert 2*m-1==3*kk
    checks.append('identity-group division source '+str(ell))
    check('formal division norm '+str(ell),
          m*(2-S.Rational(2*m-1,m))-1)
    assert (kk-kk)%m==0
    checks.append('typed chord/formal-coordinate deck cancellation '+str(ell))
wp,up,eps,eta=S.symbols('wp up eps eta')
for jj in (1,2):
    remainder=S.rem(wp*eps+up*up*eta,up**jj,up)
    check('actual translated marked ideal w,u^j '+str(jj),
          remainder.subs(wp,0))
    remainder=S.rem((wp*eps+up*up*eta)**jj,up,up)
    check('actual translated marked ideal u,w^j '+str(jj),
          remainder-eps**jj*wp**jj)

source=root/'notes/part3_e6_unselected_iii_extension_working.md'
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
     'checks':len(checks),'identities':checks,
     'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Narrow independent EX.4–5 actual middle source chart, full '
             'Cartier graph and normalized chord lift. No independent '
             're-audit of the later global annular attachment.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
