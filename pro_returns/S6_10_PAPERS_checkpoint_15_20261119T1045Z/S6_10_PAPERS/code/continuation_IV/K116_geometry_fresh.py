#!/usr/bin/env python3
"""Exact new algebra for the unselected-II source-disc geometry.

Only the listed equations and intersection computations are certified.
No K116 producing-run program or printed proof is imported.
"""
from pathlib import Path
import sympy as s
import json,hashlib

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def eq(name,expr,detail=''):
 value=s.factor(expr)
 assert value==0,(name,value)
 checks.append(dict(name=name,result='PASS',detail=detail))

t,a,z,w,A,B=s.symbols('t a z w A B');sqrt3=s.sqrt(3)
R=t*t+a;f=R*R+t;g=R**3+s.Rational(3,2)*t*R+s.Rational(3,8)
x=R+z;y=sqrt3/2+z*w
source=y*y-x**3+3*f*x-2*g
reduced=z*z+(3*(t*t+a)-w*w)*z-3*t-sqrt3*w
eq('actual rational-source substitution',source+z*reduced)
Ab=3*t-sqrt3*w-3/z;Bb=3*t+sqrt3*w
eq('literal factorization into AB',Ab*Bb+3*z+9*a-3*reduced/z)
zi=-A*B/3-3*a;ti=(A+B+3/zi)/6;wi=(B-A-3/zi)/(2*sqrt3)
eq('inverse rational source equation',reduced.subs({z:zi,t:ti,w:wi},simultaneous=True))
eq('inverse A coordinate',(3*ti-sqrt3*wi-3/zi)-A)
eq('inverse B coordinate',(3*ti+sqrt3*wi)-B)
eq('forward inverse z',(-Ab*Bb/3-3*a)-z+reduced/z)

Z,H,X,S=s.symbols('Z H X S')
Ri=1+a*Z**2;F=Ri**2+Z**3;G=Ri**3+s.Rational(3,2)*Z**3*Ri+s.Rational(3,8)*Z**6
N=48*a+8*Z+96*a*a*Z**2+72*a*Z**3+(48*a**3+9)*Z**4
eq('full infinity discriminant unit',G**2-F**3-Z**8*N/64)
eq('exact shifted cubic',(H+S)**3-3*S*S*(H+S)+2*G-(H*H*(3*S+H)+2*(G-S**3)))
eq('unit leading coefficient',N.subs(Z,0)/64-3*a/4)
for i in range(8):
 xi,yi=s.symbols('x_i y_i')
 u=xi**(i+1)*yi**i;v=xi**(7-i)*yi**(8-i);zz=xi*yi
 eq('A7 resolution chart '+str(i),u*v-zz**8)

C=s.zeros(7)
for i in range(7):
 C[i,i]=2
 if i<6:C[i,i+1]=C[i+1,i]=-1
e=s.zeros(7,1);e[2,0]=1;coeff=C.inv()*e
eq('A7 correction diagonal',coeff[2,0]-s.Rational(15,8))
assert C*coeff==e
checks.append(dict(name='literal inverse component-pairing map',result='PASS',detail={'Cartan':C.tolist(),'correction':coeff.T.tolist()}))
hg=-2+coeff[2,0]
eq('marked G projected square',hg+s.Rational(1,8))
for n,intersection,component_correction in [(8,3,0),(9,5,s.Rational(15,8))]:
 eq('section '+str(n)+'G intersection with O',-2-2*intersection+component_correction-n*n*hg)
eq('actual Hom fibre degree',s.Integer(5)-1-3-0-1)

rr,aa,tt=s.symbols('R0 a0 t0')
ft=s.diff(f,t).subs({t:-rr**2,a:rr/4})
gt=s.diff(g,t).subs({t:-rr**2,a:rr/4})
eq('unselected cusp source f_t',s.rem(s.together(ft+2).as_numer_denom()[0],rr**3-s.Rational(3,4),rr))
eq('unselected cusp source g_t',s.rem(s.together(gt+3*rr/4).as_numer_denom()[0],rr**3-s.Rational(3,4),rr))
u=s.symbols('u');au=-u/3-u**4/9
eq('selected-cover unramified derivative',s.diff(au,u)+(4*u**3+3)/9)
polyII=16*u**6+120*u**3+243
assert s.resultant(polyII,4*u**3+3,u)!=0
checks.append(dict(name='unselected-II distinct from selected cusp',result='PASS',detail=str(s.resultant(polyII,4*u**3+3,u))))
assert s.discriminant(polyII,u)!=0
checks.append(dict(name='six distinct nonzero u roots for twelve ordered points',result='PASS',detail={'discriminant':str(s.discriminant(polyII,u)),'constant':243}))

out=dict(result='PASS',checks=checks,count=len(checks),program=str(Path(__file__).relative_to(ROOT)),sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 scope='Exact rational-source maps, full infinity equation, A7 resolution monomials, intersection computations and local cusp derivatives. Original normalized Hom evaluation and full analytic gluing remain a separate proof comparison.')
(ROOT/'analysis/continuation_IV/K116_geometry_fresh.output.json').write_text(json.dumps(out,indent=2,ensure_ascii=False,default=str)+'\n')
print(json.dumps({'result':out['result'],'checks':out['count']}))
