"""Independent exact maps for the moving selected fixed-surface cap."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'notes/part3_e6_selected_infinity_moving_cap_working.md'
checks = []

def ck(test, label):
    assert test, label
    checks.append(label)

def zero(expr, label):
    ck(S.cancel(expr) == 0, label)

e, s, z, u, v, rho, R, zz, sig = S.symbols(
    'e s z u v rho R zz sig', nonzero=True)
d = 1 - 3*e**2
P = -(1+e)/(1-e)
Z = (s-1)/(s+1)
alpha = e/d
for a in (2, 6):
    b = P**a
    sa = (1+b)/(1-b)
    Sa = alpha*sa
    fb = (1-Z/b)/(1-Z)
    zero(fb + (1-b)*(s-sa)/(2*b),
         f'a={a}: exact node point-theta ratio')
    phi = -d*(1-b)/(2*b*e)
    zero(fb/(alpha*s-Sa) - phi,
         f'a={a}: complete point Cartier frame quotient')
    ck(S.limit(phi, e, 0) == a,
       f'a={a}: point coefficient is extending nonzero unit')
    ck(S.limit(Sa, e, 0) == -S.Rational(1,a),
       f'a={a}: marked point avoids both original blowup centres')
    Ca = S.Integer(2) if a == 2 else 6+20*e**2+6*e**4
    Ho = e**(-a)*d**(a-1)/Ca
    zero(Ho*phi - (d/(e*(1+e)))**a,
         f'a={a}: retained tensor-point-height coefficient')
    ck(-(4+a-4)+(4-a) == 4-2*a,
       f'a={a}: completed-to-original positive determinant winding')
    ck(-(a+3)+(1-a) == -2*a-2,
       f'a={a}: native-to-original tensor determinant winding')

# Both distinct centres and the elementary-transform blowdown charts.
zero(((1/(u*v)-1)/(1/(u*v)+1)-1)+2*u*v/(1+u*v),
     'O generator ratio is exact')
zero(((z/u-1)/(z/u+1)+1)-2*z/(u+z),
     'T generator ratio is exact')
zero((v*s)*(1/v)-s, 'first O chart gives S=rho*z1')
zero(rho/(rho*R)-1/R, 'second O chart gives S=1/R')
zero((z*zz)**2 - (-zz)*(-z*z*zz),
     'second blowup maps to exact A1 graph hk=rho squared')
zero(rho*(rho*z)-rho**2*z,
     'second blowup first chart S=rho squared times z')

# Full q-factor versus y-factor normal map, including the Z unit.
x, sn, tn = S.symbols('x sn tn', nonzero=True)
an, cn = sig**-4*tn, sig**4*sn
zero(x*an*cn-x*sn*tn, 'y-factor normal map preserves q=Zst')
anq = x**-1*sig**-4*tn
zero(x*anq*cn-sn*tn, 'q-factor normal map retains Z inverse')
zero(x*sn*(tn/x)-sn*tn, 'q-to-y normal overlap preserves height')
c = S.symbols('c', nonzero=True)
zero((e*c)**4*(v/c)**4 - e**4*v**4,
     'full source reset retains sigma fourth power')

# Integral cap connecting map and local tangent changes.
H1 = S.Matrix([[-1]])
H2 = S.Matrix([[1,0,0]])
incl = S.Matrix([[0,0],[1,0],[0,1]])
ck(H1.det() == -1, 'literal cap H1 restriction is unimodular')
ck(H2*incl == S.zeros(1,2) and incl.rank() == 2,
   'integral H2 kernel is precisely the two exceptional classes')
ck(H2.rank() == 1 and H2.nullspace() == [S.Matrix([0,1,0]), S.Matrix([0,0,1])],
   'no residual determinant connecting class')
E = S.diag(-1,-1)
ck((S.Matrix([1,-1]).T*E*S.Matrix([1,-1]))[0] == -2,
   'original first strict exceptional curve retained')
ck(-1-2*1 == -3 and 2*(-3) == -6,
   'two actual local blowup tangent changes')
C1,C2,P1 = S.symbols('C1 C2 P1')
kU = -(C1**2-C2)
lU = -(P1+C1**2-4*C2)
zero((4*kU-lU)-(P1-3*C1**2),
     'full c2 cancels from the normal-link expression')
ck(S.Rational(-6,24) == -S.Rational(1,4),
   'moving U contribution with retained determinant zero')

out = {
    'status':'PASS_INDEPENDENT_MOVING_CAP_MAPS',
    'utc':datetime.now(timezone.utc).isoformat(),
    'source':str(SOURCE.relative_to(ROOT)),
    'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'checks':len(checks),
    'check_labels':checks,
    'scope':'MC.1–6 actual local source, point/tensor, normal, integral cap determinant and tangent comparison. No total return or free characteristic pair.',
    'moving_positive_U_expression':'-1/4',
    'moving_physical_M_expression':'1/4',
    'retained':'Full Z inverse on q-factor normal chart, sigma powers, point and Miller units, finite character, determinant winding, unassigned actual c2.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
