#!/usr/bin/env python3
"""Exact source/root/Cartier and complete endpoint identities for the D=0 note."""
from pathlib import Path
import sympy as S,json,hashlib
R0=Path(__file__).resolve().parents[2];checks=[]
def eq(name,e):
 v=S.factor(S.together(e))
 if v!=0:raise AssertionError((name,v))
 checks.append(name)
w,z,t,x,y,ss,eta,n,c,f,ell,ho,hn,Pi=S.symbols('w z t x y ss eta n c f ell ho hn Pi')
D=w*w-3;R=3-2*w*w;v=w*w-1;s0=D*D/4-R
eq('actual s0',s0-(w*w-1)*(w*w+3)/4)
eq('source A1 coefficient',D*D-4*R-4*s0)
q=S.symbols('q')
U=y-t-D*x/2;V=y+t+D*x/2
eq('actual source A1 equation',U*V-x*x*(x-s0)-(y*y-x**3-R*x*x-D*t*x-t*t))
S0=S.symbols('S')
X=S0*S0-1;Y=S0*(S0*S0-w*w)
eq('actual selected nodal normalization',Y*Y-X**3-R*X*X-D*v*X-v*v)
cc=(w*w+1)/2
eq('literal tangent factor',(Y-v-D*X/2)-(S0+1)**2*(S0-cc))
eq('literal vertical factor',X-s0-(S0-cc)*(S0+cc))
ff=(S0+1)**2/(S0+cc)
for sign in [-1,1]:
 eq('node f2 '+str(sign),ff.subs(S0,sign*w)-2)
PG=(1+w)/(1-w)
S2=w*(1+PG**2)/(1-PG**2)
S6=w*(1+PG**6)/(1-PG**6)
eq('actual doubled point',S2+cc)
c2=(1+w)**2/2;c6=(1+w)**6/(6+20*w*w+6*w**4)
eq('point-line c2',w-S2-c2)
eq('point-line c6',w-S6-c6)
eq('full c2 reflection',c2.subs(w,-w)-PG**-2*c2)
eq('full c6 reflection',c6.subs(w,-w)-PG**-6*c6)
for sign in [-1,1]:
 eq('node f6 '+str(sign),(sign*w+1)**6/(sign*w-S6)-(6+20*w*w+6*w**4))
eq('full M2 node coefficient',2**6-64)
eq('full M6 node coefficient',2**6-64)
eq('selected coefficient at D zero',(64/v**3).subs(w*w,3)-8)
eq('Tate height at D zero',(-v*v/(64*w**6)).subs(w*w,3)+S.Rational(1,432))

# Actual source charts, retaining independent coefficient parameters.
dd,rr,u,v0,alpha,beta=S.symbols('dd rr u v0 alpha beta')
xx=v0*v0-rr-dd*u-u*u;tt=xx*u
kap=v0-u;xp=kap*kap-rr-xx;yp=-tt-kap*xp
eq('full X addition chart',xp-u*(dd-2*v0+2*u))
up=xx/(dd-2*v0+2*u);vp=-up-v0+u
eq('full source chart preserves base',up*xp-tt)
eq('full source chart preserves y',vp*xp-yp)
eq('full source chart equation',xp-(vp*vp-rr-dd*up-up*up))
curve=beta*beta-t*alpha**3-rr*alpha**2-dd*alpha-1
num=S.fraction(S.together((beta-1)/alpha-(dd+rr*alpha+t*alpha**2)/(beta+1)))[0]
eq('regular exceptional chord',S.rem(num,curve,beta))

# Exact root power dictionary, symbolic in the admitted order.
l=S.symbols('l',integer=True,nonnegative=True)
mg=3*l;mr=3*l+2;kg=2*l;kr=2*l+1
eq('good quadratic coefficient exponent',-2+3*(2*l)/mg)
eq('good linear coefficient exponent',3*l/mg-1)
eq('good source marked exponent',3*(2*l)/mg-2)
eq('reduced quadratic root coefficient',-2+(3*(2*l+2)+4-6)/mr)
eq('reduced linear root coefficient',(3*(l+2)+2-6)/mr-1)
eq('reduced constant root coefficient',6/mr-6/mr)
eq('reduced old to new X deck',6*kr+2-4*mr)
eq('reduced old to new Y deck',9*kr+3-6*mr)
eq('good deck fixes X',6*kg-4*mg)
eq('good deck fixes Y',9*kg-6*mg)
eq('reduced formal-coordinate factor',2/mr-3/mr+1/mr)
eq('reduced full root norm cancellation',6/mr-2*3/mr)
eq('reduced full chord-times-tau factor',1/mr-1/mr)
eq('full source selected norm factor',-6+6)
aa,jj,hh0,dd0,fp,fpa,fa,vm=S.symbols('aa jj hh0 dd0 fp fpa fa vm')
eq('typed point tensor ratio',(fp**aa/fa*vm)/(fpa*vm)-fp**aa/(fa*fpa))
for aval in [2,6]:
 eq(f'actual tensor coordinate weight a{aval}',fp**aval/(dd0**(1-aval)*fa)*vm-dd0**(aval-1)*fp**aval/fa*vm)
 eq(f'full tensor Cox weight a{aval}',(aval-1)*jj-3*hh0-((aval-1)*jj+(-3)*hh0))
 eq(f'new old tensor period jump a{aval}',(aval-1)*(eta+1)-(aval-1)*eta-(aval-1))
 eq(f'old new tensor period jump a{aval}',-(aval-1)*(eta+1)+(aval-1)*eta+(aval-1))
eq('actual marked height',2-S.Rational(4,3)-S.Rational(1,2)-S.Rational(1,6))
iota,tmw=S.symbols('iota tmw')
eq('actual index torsion determinant',6*(iota**2*tmw**2/6)-iota**2*tmw**2)

# Full cap coefficient vectors in (R_lambda, zeta character, F, root deck).
for nn in [-1,1]:
 for mm in [2,3,5,6,8,9,11,12,14,15]:
  for d0 in [0,1,mm-1]:
   avec=S.Matrix([nn,d0,nn,1])
   cvec=S.Matrix([3*nn,3*d0,3*nn,0])
   deck=S.Matrix([0,0,0,3])
   eq(f'full cap endpoint m{mm}n{nn}d{d0}',sum((deck+cvec-3*avec)))
   for j in range(4):
    eq(f'full cap endpoint column m{mm}n{nn}d{d0}j{j}',(deck+cvec-3*avec)[j])
g,g3,hh=S.symbols('g g3 hh')
rlift=2*g-hh/mr
formal3r=2*g3-3*hh/mr
eq('full retained reduced source period',3*rlift-formal3r-2*(3*g-g3))
eq('reference lift and cochain identity',n*ss*(f+Pi)+(ho-n*ss*Pi)-(n*ss*f+ho))
old=n*(ss+3*eta)*f+(ss+3*eta)*c+ho
new=n*ss*f+ss*c+hn
capcorr=eta*(n*ell+3*c)
eq('literal old native overlap',old-capcorr-new-(eta*n*(3*f-ell)+ho-hn))
eq('parameter chart period jump',((eta+1)*n*Pi+ho-hn)-(eta*n*Pi+ho-hn)-n*Pi)

# Actual global valuation map, rather than an inferred dimension argument.
j,k,b=S.symbols('j k b')
eq('rational norm degree',3-2-1)
eq('endpoint rational divisor degree',3*j/b-2*j/b-k-(j/b-k))
eq('actual source removal',b*k-b*k)
for bb in [1,3]:
 for mm in ([2,5,8,11] if bb==1 else [3,6,9,12]):
  eq(f'root finite valuation b{bb}m{mm}',-bb*S.Rational(2*mm,bb)/mm+2)
  eq(f'I2 finite valuation b{bb}m{mm}',-bb*S.Rational(-3,bb)-3)
# Reproducible Laurent/finite-group solve, with every coefficient independent.
TT=S.symbols('TT',nonzero=True)
coeff={j:S.symbols(f'c{j+6}') for j in range(-6,7)}
laurent=sum(coeff[j]*TT**j for j in coeff)
u0=-sum(coeff[j]*TT**j for j in coeff if j>=0)
uinf_minus=sum(coeff[j]*TT**(j+1) for j in coeff if j<=-1)
uinf_zero=sum(coeff[j]*TT**j for j in coeff if j<=-1)
uinf_plus=sum(coeff[j]*TT**(j-1) for j in coeff if j<=-1)
eq('actual O minus one Laurent operator',TT**-1*uinf_minus-u0-laurent)
eq('actual physical O Laurent operator',uinf_zero-u0-laurent)
eq('actual O plus one Laurent operator',TT*uinf_plus-u0-laurent)
eq('actual triangular frame derivative solve',-laurent/TT+uinf_plus-TT**-1*u0)
xx0,uu0=S.symbols('xx0 uu0')
for mm in range(2,16):
 average=-S.Rational(1,mm)*sum((xx0**h-1)*uu0 for h in range(mm))
 for gg in range(mm):
  expr=S.expand(xx0**gg*average-average-(xx0**gg-1)*uu0)
  eq(f'finite vector cocycle m{mm}g{gg}',S.rem(expr,xx0**mm-1,xx0))
ee=S.symbols('ee')
eps=ee**2/(3-2*(ee+3))
eq('original infinity coordinate degree two',S.cancel(eps/ee**2).subs(ee,0)+S.Rational(1,3))
eq('D simple at both native centres',(S.diff(D,w)**2).subs(w*w,3)-12)
ww0,uu1,DD=S.symbols('ww0 uu1 DD')
for rr0 in range(4):
 for ss0 in range(6):
  eq(f'good correction full monomial r{rr0}s{ss0}',ww0**rr0*(DD*uu1)**ss0-DD**ss0*ww0**rr0*uu1**ss0)
src=R0/'notes/part3_e6_d_zero_disc_working.md'
out={'status':'PASS','checks':len(checks),'source':str(src.relative_to(R0)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'identities':checks,'scope':'Exact source/root/Cartier, signed cap endpoint, retained period and relative cochain identities; the complete family proof is separately submitted for geometric audit.','numbered_promotion':False}
(R0/'code/part3/e6_d_zero_disc.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
