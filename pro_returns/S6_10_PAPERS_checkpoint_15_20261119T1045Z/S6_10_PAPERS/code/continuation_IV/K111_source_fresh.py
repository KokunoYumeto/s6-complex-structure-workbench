#!/usr/bin/env python3
"""Fresh exact K111 source/Cartier checks, written before target proof reading.

No producer module, saved coefficient result, or previous program is imported.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
s,t,x,y,k,z,h,m,b,q=S.symbols('s t x y k z h m b q')
r=S.Rational(1,4)-s
F=x**3+r*x**2+t*x+t**2
checks=[]
def zero(name,value):
    value=S.factor(S.cancel(value));assert value==0,(name,value)
    checks.append({'name':name,'result':'PASS'})
def rem_y(value):
    num,den=S.fraction(S.cancel(value))
    return S.rem(S.Poly(num,y),S.Poly(y*y-F,y)).as_expr()
def on_source(px,py):return py*py-(px**3+r*px**2+t*px+t**2)
def plus(px,py,qx,qy,tangent=False):
    slope=(3*px**2+2*r*px+t)/(2*py) if tangent else (qy-py)/(qx-px)
    nx=S.cancel(slope*slope-r-px-qx)
    ny=S.cancel(-py+slope*(px-nx))
    return nx,ny

zero('original section G',on_source(0,t))
p2=plus(S.Integer(0),t,S.Integer(0),t,True)
zero('double x is s',p2[0]-s)
zero('double y is -t-s/2',p2[1]+t+s/2)
zero('2G lies on source',on_source(*p2))
p3=plus(S.Integer(0),t,*p2)
x3=2*t*(2*t+s)/s**2
y3=t*(8*t*t+6*s*t+s*s-s**3)/s**3
zero('chronological 3G x',p3[0]-x3)
zero('chronological 3G y',p3[1]-y3)
zero('3G lies on source',on_source(x3,y3))

# Exact generic inverse-source relation, reduced in the source function field.
minus=plus(x,y,S.Integer(0),-t)
zero('translation by -G preserves source',rem_y(on_source(*minus)))
back=plus(*minus,S.Integer(0),t)
zero('inverse translation x',rem_y(back[0]-x))
zero('inverse translation y',rem_y(back[1]-y))

D=r*r*(1-4*r)+(18*r-4)*t-27*t*t
zero('full cubic discriminant',S.discriminant(F,x)-t*t*D)
zero('central remaining discriminant root',D.subs({s:0,t:S.Rational(1,54)}))
zero('central selected discriminant is I3 order',D.subs(s,0)-(t/2-27*t*t))

# k²=1+12s is an exact double-cover parameter. All checks are rational in k.
sk=(k*k-1)/12;rk=S.Rational(1,4)-sk
xi=(k-1)*(k+2)/18;tc=-(k-1)*(k+2)**2/108
sg=(k+2)/6;c2=k*(k+2)/12
zero('selected node t from xi',tc+xi*(2*rk+3*xi))
zero('selected double root factorization',x**3+rk*x*x+tc*x+tc*tc-(x-xi)**2*(x+rk+2*xi))
zero('selected discriminant root',D.subs({s:sk,t:tc}))
zero('actual G normalization value',sg-(2*rk+3*xi))
zero('normalization coordinate of G',sg*sg-rk-2*xi)
zero('normalization y-coordinate of G',sg*(sg*sg-rk-3*xi)-tc)
zero('ordered c square',c2-rk-3*xi)
zero('exact P_G ratio identity',sg*sg-c2+xi)
zero('xi over s leading coefficient',S.limit(xi/sk,k,1)-1)
zero('selected t over s leading coefficient',S.limit(tc/sk,k,1)+S.Rational(1,2))

Scoord=h*(1+z)/(1-z)
zero('ordered torus coordinate inverse',(Scoord-h)/(Scoord+h)-z)
zero('group inversion gives reciprocal',((-Scoord-h)/(-Scoord+h))-1/z)
X=h*h*((1+z)/(1-z))**2-rk-2*xi
Y=Scoord*(Scoord*Scoord-rk-3*xi)
normal_curve=Y*Y-(X**3+rk*X*X+tc*X+tc*tc)
num,den=S.fraction(S.cancel(normal_curve))
zero('full normalization morphism',S.rem(S.Poly(num,h),S.Poly(h*h-c2,h)).as_expr())
H=lambda w:w**3-m*w*w-c2*w+m*(rk+2*xi)-b
zero('chord values at ordered branches',S.rem(S.Poly(H(h)-H(-h),h),S.Poly(h*h-c2,h)).as_expr())
zero('chord common exact value',S.rem(S.Poly(H(h)+m*xi+b,h),S.Poly(h*h-c2,h)).as_expr())
zero('marked point leading torus ratio',S.limit((-xi/(sg+S.sqrt(c2))**2)/sk,k,1)+1)

kap=S.sqrt(1+12*s)
xiser=xi.subs(k,kap).series(s,0,5).removeO()
tcser=tc.subs(k,kap).series(s,0,5).removeO()
zero('selected xi series',xiser-(s-s*s+6*s**3-45*s**4))
zero('selected height series',tcser-(-s/2-s*s/2+s**3-S.Rational(9,2)*s**4))
c4=16*(r*r-3*t)
q_coefficient=16*tc**2*(18*rk-4-54*tc)/(c4.subs({s:sk,t:tc})**3*sk**2)
zero('complete reciprocal j leading coefficient',S.limit(q_coefficient,k,1)-2)
full_j_ratio=16*(tc+q)**2*(18*rk-4-54*tc-27*q)/(c4.subs({s:sk,t:tc+q})**3*sk**2)
zero('full joint ratio along q=s^2',S.limit(full_j_ratio.subs(q,sk**2),k,1)-2)
zero('full joint ratio along q=2s differs',S.limit(full_j_ratio.subs(q,2*sk),k,1)-18)

# Cartier-divisor pullback is indexed directly from the source translation.
base={0:-1,1:2,2:-1};product={j:0 for j in range(6)}
for shift,power in [(0,1),(3,1),(1,2),(2,2)]:
    for j,n in base.items():product[j+shift]+=power*n
expected={0:-1,1:0,2:1,3:1,4:0,5:-1}
assert product==expected
checks.append({'name':'full chronological Miller Cartier divisor','result':'PASS','coefficients':product})
DM={0:-1,2:1};difference={j:DM.get(j,0)-DM.get(j-3,0) for j in range(6)}
assert product==difference
checks.append({'name':'directed M2 to pullback-by-minus3G module arrow','result':'PASS'})
PN=S.Matrix([[1,-1],[-1,2]])
zero('native matrix determinant',PN.det()-1)
assert PN.inv()==S.Matrix([[2,1],[1,1]])
checks.append({'name':'native matrix literal inverse; no fan identification inferred','result':'PASS'})
zero('displayed physical characteristic arithmetic',(4*S.Integer(71)+4)/24-12)

output={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'count':len(checks),'outcome':'PASS',
        'chronology':'New code and derivation authored before displaying or reading the K111 target proof. Exact source statement only. No producer import.',
        'limits':'Source/normalization, generic group, horizontal Cartier and displayed arithmetic scopes only. No total vertical, cap, Jin cobordism, native fan, held-quaternion, topology or endpoint proof gate.',
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'analysis/continuation_IV/K111_source_fresh.output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'count':len(checks),'outcome':'PASS'},indent=2))
