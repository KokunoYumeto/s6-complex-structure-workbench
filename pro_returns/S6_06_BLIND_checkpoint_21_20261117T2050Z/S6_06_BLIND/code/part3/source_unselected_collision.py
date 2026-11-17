#!/usr/bin/env python3
"""Exact identities for the unselected v=1/8 source collision."""
from pathlib import Path
import json
import sympy as s

root=Path(__file__).resolve().parents[2]
X,Y,T,v,u,x,y,t,z=s.symbols('X Y T v u x y t z')
F=Y**2-X**3-(1-2*v)*X**2-T*X-v**2
checks=[]
def check(label,expr):
    assert s.simplify(expr)==0,(label,s.factor(expr))
    checks.append(label)
vs=s.Rational(1,8); Ts=s.Rational(3,16); Xs=-s.Rational(1,4)
pt={X:Xs,Y:0,T:Ts,v:vs}
for label,expr in [('equation',F),('Fx',s.diff(F,X)),('Fy',s.diff(F,Y)),('Fxx',s.diff(F,X,2))]:
    check('collision '+label,expr.subs(pt))
check('nonzero FT',s.diff(F,T).subs(pt)-s.Rational(1,4))
check('selected factor',F.subs(T,v**2-2*v)-(Y**2-(X-v)**2*(X+1)))
check('selected value', (v**2-2*v).subs(v,vs)+s.Rational(15,64))
check('normal form',F.subs({X:u**2*x,Y:u**3*y,T:u**4*t,v:u**3})/u**6-(y**2-x**3-(u**-2-2*u)*x**2-t*x-1))
a=(1-2*v)*v**(-s.Rational(2,3))
check('normalized coefficient at collision',a.subs(v,vs)-3)
check('coefficient derivative',s.diff(a,v).subs(v,vs)+24)
check('r derivative',s.diff(a/3,v).subs(v,vs)+8)
check('normalized collision value',Ts/(s.Rational(1,2)**4)-3)
check('normalized selected value',-s.Rational(15,64)/(s.Rational(1,2)**4)+s.Rational(15,4))
check('normalized cubic cusp',x**3+3*x**2+3*x+1-(x+1)**3)
check('vertical vector tangency',2*Y*s.diff(F,X)+(3*X**2+2*(1-2*v)*X+T)*s.diff(F,Y))
ss=s.symbols('ss',nonzero=True)
check('cuspidal normalization',F.subs({X:ss**2-s.Rational(1,4),Y:ss**3,T:Ts,v:vs}))
check('normalization of G x',(ss**2-s.Rational(1,4)).subs(ss,s.Rational(1,2)))
check('normalization of G y',(ss**3).subs(ss,s.Rational(1,2))-vs)
for bb in (1,2):
    sb=s.Rational(1,2*bb)
    check(f'additive bG b={bb}',1/sb-2*bb)
    check(f'nonzero vector at bG b={bb}',2*sb**3-s.Rational(1,4*bb**3))
for p in range(1,9):
    for branch,m,k,expected in [('good',4*p,3*p,0),('reduced',4*p-1,3*p-1,1)]:
        check(f'{branch} p={p} x2 exponent',2*m-2*k-2*p)
        check(f'{branch} p={p} x exponent',3*m-4*k-expected)
        check(f'{branch} p={p} constant exponent',6*m-6*k-6*p)
        assert (-2*k-2*p)%m==0 and (-3*k-3*p)%m==0
        checks.extend([f'{branch} p={p} deck x',f'{branch} p={p} deck y'])
for aa,bb in [(1,2),(2,1)]:
    check(f'scalar cancellation a={aa},b={bb}',4-2*aa*bb)
out={'status':'PASS','checks':len(checks),'identities':checks,'collision':{'v':'1/8','X':'-1/4','Y':'0','T':'3/16','F_T':'1/4'},'selected_value':'-15/64','scope':'Algebraic certificate for UI1–4; properness and exact line/root/annular continuation are proved in the note.'}
(root/'code/part3/source_unselected_collision.json').write_text(json.dumps(out,indent=2)+'\n')
msg=f'PASS: {len(checks)} exact source/root/scalar identities for the unselected collision.\n'
(root/'code/part3/source_unselected_collision.out').write_text(msg)
print(msg,end='')
