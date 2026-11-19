"""Exact E90--93 theta factors, Cartier graph, and period arrows.

Analytic convergence, divisor completeness, and geometric scope are proved
in the companion note. This certificate checks the displayed algebra and
does not assign a compact attachment or a return.
"""
from pathlib import Path
import json
import sympy as S

P,R,p,Q,Z,u,c,f,U6,a,theta,TP,TP6,tau = S.symbols(
    'P R p Q Z u c f U6 a theta TP TP6 tau', nonzero=True)
checks=[]
def ck(name,expr):
    v=S.factor(expr)
    assert v==0,(name,v)
    checks.append(name)

q=P**2*R
ck('two exact backward theta factors',
   P**6*(1-q/P**6)*(1-q**2/P**6)-(R-P**4)*(R-P)*(R+P))
for n in range(1,12):
    ck('forward product exponent '+str(n),q**n*P**6-P**(2*n+6)*R**n)
for n in range(3,12):
    ck('remaining backward exponent '+str(n),q**n/P**6-P**(2*n-6)*R**n)
ck('exceptional full divisor',
   ((R-P)*(R+P)*(R-P**4)).subs(R,p*P)
   -P**3*(p-1)*(p+1)*(p-P**3))
fp_lead=-TP/(P*theta*a*tau)
fp6_lead=-TP6/(P**6*theta*a*tau)
f6_lead=-tau**-5
ck('origin fixes full scalar and sign',
   fp_lead**6/(f6_lead*fp6_lead)-TP**6/(a**5*theta**5*TP6))
qq=P**3*p
b1=P**3/p;b2=p**-2
ck('first point period shift',P**6*U6*Z**-3*(-Z/P**6)+U6*Z**-2)
ck('second point period shift',
   P**6*U6*Z**-3*Z**2*qq**-3*b2**-2-P**-3*p*U6*Z**-1)

x,y,A=S.symbols('x y A',nonzero=True)
rays=[(1,0),(1,1),(1,2),(1,3),(0,1)]
for i,(r,s) in enumerate(zip(rays,rays[1:])):
    ck('regular graph determinant '+str(i),S.Matrix.hstack(S.Matrix(r),S.Matrix(s)).det()-1)
for j in range(3):
    pp=x*y;rr=x**j*y**(j+1)
    ck('graph point lift '+str(j),pp**3/rr-x**(3-j)*y**(2-j))
    ck('graph first inverse '+str(j),pp**(j+1)/rr-x)
    ck('graph second inverse '+str(j),rr/pp**j-y)
ck('last graph point lift',x**3/(x**3*A)-A**-1)
bb,unit=S.symbols('bb unit',nonzero=True)
ck('typed local Cartier generator',
   (Z-1)/(Z-bb)*(Z-bb)/(bb*(Z-1))*unit-unit/bb)

# N=4 p=0 corner, using the full corrected coefficient YC.
v=p-1;b=v**-4*c**-1;d0=v**24*c**6
a0=p*v**12*c**3
ck('actual K X multiplier',P**9*p/(P**9*b**9*a0)-d0)
ck('actual K Y multiplier',b**9*P**9*a0-P**9*p/d0)
ck('p0 character determinant',S.Matrix([[-3,-1],[4,1]]).det()-1)
ck('p0 period determinant',S.Matrix([[0,1],[-1,-6]]).det()-1)
XX,YY=S.symbols('XX YY',nonzero=True)
for i in (-2,0,3):
    ck('H1 source chain '+str(i),P*b**-1*XX/P**(i+1)-b**-1*XX/P**i)
for j in (-1,0,2):
    T=P**9*p
    ck('K line chain '+str(j),T*d0**-1*YY/T**(j+1)-d0**-1*YY/T**j)
vc,z0,w0=S.symbols('vc z0 w0',nonzero=True)
ck('generic p0 actual normal product',z0*vc*P**6*w0/vc-P**6*z0*w0)
ck('generic p0 actual height',P**6*(P**3*p)-P**9*p)

# Generic p=infinity actual point frame; all u-powers are kept.
pp=u*R;qq=u**2*R**3;cp=R**-3
ck('infinity point representative',pp**6/qq**3-cp)
ck('infinity full theta shift coefficient',
   pp**6*U6*Z**-3*(-Z**3/(qq**6*cp**3))+U6*u**-6*R**-3)
Kz=R;Kv=R**5*f**2;Lz=u;Lv=R**-9*f**-3
ck('infinity h source',Kz**3*Lz**2-u**2*R**3)
ck('infinity h line',Kv**3*Lv**2-R**-3)
ck('infinity B source',Kz**-1*Lz**-1-u**-1*R**-1)
ck('infinity B line',Kv**-1*Lv**-1-R**4*f)
ck('infinity dual h',Kv**-3*Lv**-2-R**3)
ck('infinity dual B',Kv*Lv-R**-4*f**-1)
ck('infinity period determinant',S.Matrix([[1,-1],[2,-3]]).det()+1)
ck('infinity raw character determinant',S.Matrix([[1,0],[5,-1]]).det()+1)

out={'status':'PASS','count':len(checks),'checks':checks,
     'scope':'Full point-theta and Cartier factors; actual generic exceptional-end period maps. No full corner gluing, compact boundary ledger, characteristic pair, or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
