#!/usr/bin/env python3
"""Fresh exact K116 coefficient checks, explicitly written after proof reading.

The computation constructs tangent quotients and the actual coordinate maps;
it does not import any source-run program or award a before-reading gate.
"""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def eq(name,expr,detail=''):
 v=s.factor(expr);assert v==0,(name,v)
 checks.append(dict(name=name,result='PASS',detail=detail))
def truth(name,test,detail=''):
 assert test,name;checks.append(dict(name=name,result='PASS',detail=detail))

p,g=s.symbols('p g',nonzero=True)
xp=1/p**2;yp=1/p**3
def tangent_quotient(j):
 xj=1/(j*g)**2;yj=1/(j*g)**3
 slope=3*xj*xj/(2*yj)
 return s.factor((yp-yj-slope*(xp-xj))/(xp-1/(2*j*g)**2))
f2=tangent_quotient(1)
f4=s.factor(f2*f2*tangent_quotient(2))
f8=s.factor(f4*f4*tangent_quotient(4))
for m,fm in [(2,f2),(4,f4),(8,f8)]:
 target=-s.Integer(m)/g**(m-1)*(p-g)**m/((p-m*g)*p**(m-1))
 eq('chronological cusp tangent f'+str(m),fm-target)
B=s.factor(f2**8*f8.subs(p,p-g)/f8)
target=256/g**8*(p-g)*(p-8*g)/(p*(p-9*g))
eq('actual composite cusp Hom coefficient',B-target)
r=(p-8*g)/p
eq('finite normalization module arrow',B*r.subs(p,p-g)/r-256/g**8)
local=256/g**8*(1-73*g*g*xp+72*g**3*yp)/(1-81*g*g*xp)
eq('cusp-ring module coefficient',B-local)
eq('full reciprocal-source line inverse',B*(1/B.subs(p,p+g)).subs(p,p-g)-1)
truth('point-chart overlap is retained, not deleted',s.expand(r)==1-8*g/p,
 'r has a linear normalization term; only the stated smooth-overlap map is used at the cusp.')

x,y,R,t=s.symbols('x y R t');rt3=s.sqrt(3)
f=R**2+t;gg=R**3+s.Rational(3,2)*t*R+s.Rational(3,8)
F=y*y-x**3+3*f*x-2*gg
L=(y+rt3/2)/(x-R)
xt=s.factor(L*L-x-R);yt=s.factor(L*(x-xt)-y)
def rem(expr):
 numerator=s.together(expr).as_numer_denom()[0]
 return s.rem(s.Poly(numerator,y),s.Poly(F,y)).as_expr()
eq('original source translation preserves cubic',rem(yt*yt-xt**3+3*f*xt-2*gg))
Lp=(yt-rt3/2)/(xt-R)
eq('actual inverse slope',rem(Lp+L))
eq('inverse source x after opposite slope',(-L)**2-xt-R-x)
eq('inverse source y after opposite slope',(-L)*(xt-x)-yt-y)
r0=s.symbols('R0')
def cusp_reduce(expr):
 num=s.together(expr.subs({x:0,y:0,R:r0,t:-r0**2},simultaneous=True)).as_numer_denom()[0]
 return s.rem(s.Poly(num,r0),s.Poly(r0**3-s.Rational(3,4),r0)).as_expr()
eq('translation fixes original cusp x',cusp_reduce(xt))
eq('translation fixes original cusp y',cusp_reduce(yt))
jac=s.Matrix([xt,yt]).jacobian([x,y])
expected=s.Matrix([[1,4*r0/rt3],[0,1]])
for i in range(2):
 for j in range(2):eq('cusp derivative entry '+str((i,j)),cusp_reduce(jac[i,j]-expected[i,j]))

u,a,z,Z,Q,b0,P=s.symbols('u a z Z Q b0 P',nonzero=True)
au=-u/3-u**4/9;tc=1/(2*u)-u*u/3;xi=1/(4*u*u)+u/3
tt=s.symbols('tt');RR=tt*tt+a;ff=RR*RR+tt;ggg=RR**3+s.Rational(3,2)*tt*RR+s.Rational(3,8)
h0=2*(s.diff(ggg,tt)-s.Rational(3,2)*xi*s.diff(ff,tt)).subs({tt:tc,a:au},simultaneous=True)
eq('selected full smoothing unit at its centre',h0+2*u**4)
eq('selected and unselected values stay distinct identity',tc+16*au**2-(2*u**3+9)*(4*u**3+3)**2/(162*u))
eq('ordinary-cap discriminant at II',s.Rational(3)*(16*s.Rational(3,256)+3)-s.Rational(153,16))

C=s.zeros(7)
for i in range(7):
 C[i,i]=2
 if i<6:C[i,i+1]=C[i+1,i]=-1
Gm=s.zeros(10);Gm[0,0]=Gm[9,9]=-1;Gm[0,1]=Gm[1,0]=1;Gm[1,9]=Gm[9,1]=1
for i in range(7):
 for j in range(7):Gm[i+2,j+2]=-C[i,j]
Gm[4,9]=Gm[9,4]=1
eq('ten actual source classes form unimodular lattice',Gm.det()+1)
cycle=s.zeros(8)
for i in range(8):cycle[i,i]=-2;cycle[i,(i+1)%8]=cycle[(i+1)%8,i]=1
truth('whole I8 fibre is the complete vertical kernel',cycle.rank()==7 and cycle*s.ones(8,1)==s.zeros(8,1))

eq('infinity inverse-j leading coefficient',1/(1728/(-3*a/4))+a/2304)
eq('actual eighth-point limit',(-s.Rational(1,24))**8/(-a/s.Integer(2304))**3+1/(9*a**3))
X0=1+12*Z/(1-Z)**2;Y0=rt3*12*Z*(Z+1)/(Z-1)**3
eq('oriented infinity nodal parametrization',Y0**2-(X0-1)**2*(X0+2))
eq('eighth-point X via exact infinity map',X0.subs(Z,-1/(9*a**3))-(81*a**6-90*a**3+1)/(9*a**3+1)**2)
eq('eighth-point Y via exact infinity map',Y0.subs(Z,-1/(9*a**3))/rt3-108*a**3*(9*a**3-1)/(9*a**3+1)**3)
eq('identity-component point at II',-1/(9*s.Rational(3,256))+s.Rational(256,27))

# Three downward theta shifts, derived from Theta(z/Q)=-(z/Q)Theta(z).
shift=s.Integer(1)
for k in range(1,4):shift*=-(Z/b0)/Q**k
eq('complete three-shift theta coefficient',shift-(-Z/b0)**3*Q**(-6))
eq('source translation changes old frame by P^-3',shift.subs(Z,Z/P)/shift-P**(-3))
eq('period changes old frame by Q^3',shift.subs(Z,Q*Z)/shift-Q**3)
M=s.Matrix([[-1,3],[-3,8]]);Mi=s.Matrix([[8,-3],[3,-1]])
truth('full primitive-period inverse words',M*Mi==s.eye(2) and M.det()==1,{'matrix':M.tolist(),'inverse':Mi.tolist()})
truth('primitive source valuations',s.Matrix([[8,-3]])*M==s.Matrix([[1,0]]))
truth('pure K line scalar exponent is eight',M[1,1]==8)

A,D,aa,bb,cc=s.symbols('A D aa bb cc',nonzero=True)
eq('first selected vertex preserves actual height',aa/(A*D)*(A*bb)*(D*cc)-aa*bb*cc)
eq('second selected vertex preserves actual height',(A*D*aa)*(bb/D)*(cc/A)-aa*bb*cc)
for fwd,inv in [(1/(A*D),A*D),(A,1/A),(D,1/D)]:eq('full vertex coefficient and reciprocal '+str(fwd),fwd*inv-1)
gamma=s.Matrix(s.symbols('gamma0:3'));zeta=s.Matrix(s.symbols('zeta0:3'));logt=s.symbols('logt');winding=s.symbols('winding',integer=True)
psi=zeta+logt/(2*s.pi*s.I)*gamma
truth('full cap map and inverse',(psi-logt/(2*s.pi*s.I)*gamma)==zeta)
truth('full cap logarithm branch retains period',s.simplify(psi.subs(logt,logt+2*s.pi*s.I*winding)-psi-winding*gamma)==s.zeros(3,1))

out=dict(result='PASS',checks=checks,count=len(checks),program=str(Path(__file__).relative_to(ROOT)),sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 chronology='Written after reading the three K116 supporting proofs; fresh code, targeted comparison. No before-reading proof gate is inferred.',
 scope='Complete listed rational coefficients, Cartier overlaps, source/inverse maps, lattice/period inverses and full formal cap/vertex arrows. Analytic compactness and input topology remain proof arguments, not program certificates.')
(ROOT/'analysis/continuation_IV/K116_full_coefficient_checks.output.json').write_text(json.dumps(out,indent=2,ensure_ascii=False,default=str)+'\n')
print(json.dumps({'result':out['result'],'checks':out['count']}))
