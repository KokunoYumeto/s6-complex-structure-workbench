"""Exact EI.31--41 source, point/tensor and finite graph-deck identities.

The analytic Cartier extension and the old-cap domain are proved in the
working note. No compact period quotient or return is certified here.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

base = Path(__file__).resolve().parents[2]
X,Y,sig,d,aa,xi,tau,ta=S.symbols('X Y sig d aa xi tau ta')
i=S.I
checks=[]

def check(name,expr):
    value=S.simplify(S.factor(S.together(expr).as_numer_denom()[0]))
    assert value == 0, (name,value)
    checks.append(name)

F=Y**2-X**3-aa*X**2-d*X-sig**2
Sp=d**2/4-aa*sig**2
mu=sig/d
xo,yo,to,ro=mu**2*X,mu**3*Y,sig**4/d**3,sig**2*aa/d**2
check('literal original source map',
      (yo**2-xo**3-ro*xo**2-to*xo-to**2)/mu**6-F)
x2=Sp/sig**2
y2=-sig-d*x2/(2*sig)
tau2=2*sig*Sp/(d*Sp+2*sig**4)
check('second section lies on whole joint source',
      F.subs({X:x2,Y:y2}, simultaneous=True))
check('literal formal coordinate of second section',tau2+x2/y2)
check('second formal leading coefficient',(tau2/sig).subs(sig,0)-2/d)
f2=(Y-sig-d*X/(2*sig))/(X-x2)
f2h=(sig*Y-sig**2-d*X/2)/(sig**2*X-Sp)
check('full second Miller vertical divisor',f2-sig*f2h)
check('second Miller central function',f2h.subs(sig,0)-2*X/d)
f3=Sp*X*(sig*Y-sig**2-d*X/2)/(Sp*(sig*Y+sig**2-d*X/2)-2*sig**4*X)
check('third Miller central function',f3.subs(sig,0)-X)
X3=2*d/Sp+4*sig**4/Sp**2
Y3=d**2/Sp-1+6*d*sig**4/Sp**2+8*sig**8/Sp**3
L3=(3*sig**4*X3**2+2*aa*sig**2*X3+d)/(2*Y3)
X6=L3**2-aa*sig**2-2*sig**4*X3
f23h=(sig*Y-sig**2*Y3-L3*X+sig**2*L3*X3)/(sig**2*X-X6)
f6h=f3**2*f23h
for name,value,expected in (
    ('X3',X3,8/d),('Y3',Y3,3),('L3',L3,d/6),
    ('X6',X6,d**2/36),('sixth tangent',f23h,6*X/d),
    ('sixth Miller',f6h,6*X**3/d)):
    check('central '+name,value.subs(sig,0)-expected)
for name,expr,wt in (('f2',f2,1),('f3',f3,2),
                     ('f2 primitive',f2h,2),('f6 primitive',f6h,6)):
    for power in range(4):
        z=i**power
        after=expr.subs({X:z**2*X,Y:z**3*Y,sig:z**3*sig,aa:z**2*aa,d:z**4*d},simultaneous=True)
        check(f'complete {name} fourth-root weight {power}',after-z**wt*expr)

slope=(Y+sig)/X
Xp=slope**2-aa-X
Yp=sig-slope*Xp
n=S.together(F.subs({X:Xp,Y:Yp},simultaneous=True)).as_numer_denom()[0]
check('whole source minus-G chord',S.rem(n,F,Y))
check('central two-torsion source x',
      S.rem(S.together(Xp.subs(sig,0)-d/X).as_numer_denom()[0],F.subs(sig,0),Y))
check('central two-torsion source y',
      S.rem(S.together(Yp.subs(sig,0)+d*Y/X**2).as_numer_denom()[0],F.subs(sig,0),Y))
check('M6 complete central chronological norm',
      (2*X/d)**6*(6*(d/X)**3/d)/(6*X**3/d)-64/d**3)
check('M2 complete central chronological norm',
      (2*X/d)*(2/X)*(2/X)**2*(2*X/d)**2-64/d**3)

rows=[]
for a in (2,6):
    for ell in range(0 if a==6 else 1,7):
        m=3*ell+2 if a==6 else 3*ell
        bst=ell+2 if a==6 else ell
        e=xi**m*sig
        dd=1-3*e**2
        AA=3*e**2-2
        ac=AA*xi**(2*m)
        C=(1-e**2)*(1+3*e**2)
        H=1-xi**(4*m)*(1-e**2)
        check(f'row{a},{ell} actual second-section unit',dd**2-4*ac*sig**2-C)
        check(f'row{a},{ell} original selected height',
              sig**4/dd**3-e**4*(1-e**2)/dd**3-sig**4*H/dd**3)
        check(f'row{a},{ell} graph source X exponent',i**(-2*bst)-i**(2*m))
        check(f'row{a},{ell} graph source Y exponent',i**(-3*bst)-i**(3*m))
        check(f'row{a},{ell} full xi power comparison',m+bst-4*(ell+(1 if a==6 else 0)))
        check(f'row{a},{ell} graph original x',(i**(-m))**2*i**(2*m)-1)
        check(f'row{a},{ell} graph original y',(i**(-m))**3*i**(3*m)-1)
        check(f'row{a},{ell} graph original t',(i**(-m))**4-1)
        check(f'row{a},{ell} graph epsilon',i**m*i**(-m)-1)
        check(f'row{a},{ell} point Cartier ratio',
              (i**(-m)*tau-i**(-m)*ta)/(i**(-m)*tau)-(tau-ta)/tau)
        check(f'row{a},{ell} primitive tensor character',i**(-m*a)-(-1)**m)
        check(f'row{a},{ell} original tensor invariant',(i**(-m))**(-a)*i**(-m*a)-1)
        check(f'row{a},{ell} full Miller invariant',(i**(-m))**a*i**(m*a)-1)
        check(f'row{a},{ell} local determinant',i*i**(-m)*i**(-m)-i**(1-2*m))
        # The lifted native deck has Weierstrass multiplier i and sigma -i.
        check(f'row{a},{ell} native primitive tensor',i**(-a)+1)
        check(f'row{a},{ell} native original tensor',(-i)**(-a)*i**(-a)-1)
        check(f'row{a},{ell} native point ratio',
              ((-i)*tau-(-i)*ta)/((-i)*tau)-(tau-ta)/tau)
        check(f'row{a},{ell} native mth source x',(-1)**m-i**(2*m))
        check(f'row{a},{ell} native mth source y',(-i)**m-i**(3*m))
        check(f'row{a},{ell} native mth sigma',(-i)**m-i**(-m))
        rows.append({'a':a,'l':ell,'m':m,'b_star':bst,'tensor_character':str(i**(-m*a))})

# The two original-source Cartier coefficient frames are literally related.
W=S.Symbol('W')
for a in (2,6):
    check(f'a{a} original whole tensor arrow',
          (mu**(a-1)*sig)**(-1)*W-sig**(-a)*d**(a-1)*W)
    check(f'a{a} native tensor power action',(-i)**(-a)*i**(-a)-1)

q=S.Symbol('q')
check('smooth central joint discriminant',
      16*((-2*q)**2-4)-64*(q*q-1))
source=base/'notes/part3_e6_selected_infinity_working.md'
out={'status':'PASS_LOCAL_JOINT_SOURCE_LINE','utc':datetime.now(timezone.utc).isoformat(),
     'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'count':len(checks),'rows':rows,'checks':checks,
     'scope':'EI.31--41 exact complementary ordinary source, full Miller and vertical Cartier maps, actual graph/native finite-deck characters and normal determinants.',
     'unassigned':'Compact period quotient, selected-collision attachment, characteristic pair and source return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','count','source_sha256')},indent=2))
