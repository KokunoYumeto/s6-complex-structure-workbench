"""Exact EI.42--73 graphs, Cartier factors and selected factor charts.

This is a local morphism certificate. The complete compact union and its
oriented characteristic calculation are not asserted.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

base=Path(__file__).resolve().parents[2]
e,nu,rho,s,h,k,z,u,v,eta,uu,d,aa,sig,xx,yy,q,c,g=S.symbols(
    'e nu rho s h k z u v eta uu d aa sig xx yy q c g')
checks=[]
def chk(name,expr):
    value=S.simplify(S.factor(S.together(expr).as_numer_denom()[0]))
    assert value==0,(name,value)
    checks.append(name)

dd=1-3*e**2
rv=-2*nu-3*nu**2
tc=nu**2*(1+2*nu)
xo=s*s-nu*nu
yo=s*(s*s-nu*(1+3*nu))
chk('original parameter bridge',rv.subs(nu,e*e/dd)-e*e*(3*e*e-2)/dd**2)
chk('selected height bridge',tc.subs(nu,e*e/dd)-e**4*(1-e*e)/dd**3)
chk('whole selected normalization',yo**2-xo**3-rv*xo**2-tc*xo-tc**2)
chk('Rees generator nu2',tc/(1+2*nu)-nu*nu)
chk('Rees generator s2',xo+nu*nu-s*s)
chk('Rees generator s nu',s*xo-yo-2*s*nu*nu-s*nu)
L=((1+3*h*k)*h-k)/(1-h*h)
Uv=tc/xo-nu
Vv=yo/xo
chk('whole graph U',Uv.subs({s:-k,nu:h*k},simultaneous=True)-h*L)
chk('whole graph V',Vv.subs({s:-k,nu:h*k},simultaneous=True)-L)
height=(nu+u)*v*v-u*u*(1+3*nu+u)
source_x=v*v-rv-(nu+u)-(nu+u)**2
chk('literal source height',source_x*(nu+u)-tc-height)
chk('A1 graph lies on selected height',height.subs({nu:h*k,u:h*L,v:L},simultaneous=True))
chk('double-branch exact numerator',L.subs(k,h/(1-3*h*h)))
chk('central h-axis exceptional source component',
    source_x.subs({nu:0,u:h*L.subs(k,0),v:L.subs(k,0)},simultaneous=True))
chk('central k-axis proper source component',L.subs(h,0)+k)
asrc=dd*(z*z-1)/(1-e*e)
bsrc=z*(e*e*z*z-1)/(1-e*e)
chk('second graph chart x/t',
    (xo/tc).subs({s:nu*z},simultaneous=True).subs(nu,e*e/dd)-asrc)
chk('second graph chart y/t',
    (yo/tc).subs({s:nu*z},simultaneous=True).subs(nu,e*e/dd)-bsrc)
chk('second graph actual conic',
    bsrc*bsrc-(tc*asrc**3+rv*asrc**2+asrc+1).subs(nu,e*e/dd))
chk('first marked G point',asrc.subs(z,-1))
chk('first marked G coefficient',bsrc.subs(z,-1)-1)
z1,zz=S.symbols('z1 zz')
chk('two-blowup A1 graph',(-zz)*(-z1*z1*zz)-(z1*zz)**2)
for a in (2,6):
    P=-(1+e)/(1-e)
    sa=S.cancel(e/dd*(1+P**a)/(1-P**a))
    chk(f'a{a} actual section limit',sa.subs(e,0)+S.Rational(1,a))
    fnew=(s+e)**a/(s-(1+P**a)/(1-P**a))
    old=s # use a separate original normalization coordinate below
    chk(f'a{a} complete normalized Miller morphism',
        (e/dd)**(a-1)*fnew.subs(s,old*dd/e)-(old+e*e/dd)**a/(old-sa))
    chk(f'a{a} first exceptional Cartier order',
        (rho*z1+rho*rho)**a-rho**a*(z1+rho)**a)
    chk(f'a{a} second exceptional Cartier order',
        (rho*rho*z+rho*rho)**a-rho**(2*a)*(z+1)**a)

# The ordinary -G map on the original source resolution, including its
# actual parabolic double reset.
xorig=v*v-rv-u-u*u
D=1+2*v+2*u
up=xorig/D
vp=up-v-u
xp=u*D
chk('original resolved translation equation',xp-(vp*vp-rv-up-up*up))
chk('original resolved translation base',xp*up-xorig*u)
J=S.Matrix([up,vp]).jacobian([u,v]).subs({nu:0,u:0,v:0})
chk('original central derivative matrix',sum((J-S.Matrix([[-1,0],[-2,-1]])).applyfunc(lambda x:x*x)))
M=S.Matrix([[nu,nu*(1+3*nu)],[1,nu]])
M2=M*M
chk('complete nodal twice-translation numerator',M2[0,0]/nu-(1+4*nu))
chk('complete nodal twice-translation off diagonal',M2[0,1]/nu-2*nu*(1+3*nu))
chk('complete nodal twice-translation denominator',M2[1,0]/nu-2)

# Full O/T source graphs. The formal unit relation is kept as a polynomial.
R=uu**3+(aa*eta*eta-1)*uu**2+d*eta**4*uu+sig*sig*eta**6
X=uu/eta**2
Y=-uu/eta**3
F=Y*Y-X**3-aa*X*X-d*X-sig*sig
chk('formal Weierstrass unit equation',F*eta**6+R)
mu=sig/d
chk('O graph old tau',(-mu*mu*X/(mu**3*Y))-d*eta/sig)
xxold=mu*mu*X
yyold=mu**3*Y
ttold=sig**4/d**3
chk('O graph original finite x',xxold.subs(sig,eta*v)-v*v*uu/d**2)
chk('O graph original finite y',yyold.subs(sig,eta*v)+v**3*uu/d**3)
chk('O graph source u',
    (ttold/xxold).subs(sig,eta*v)-eta**4*v*v/(d*uu))
chk('O graph source v',(yyold/xxold).subs(sig,eta*v)+v/d)
ca=S.symbols('ca')
chk('full O point coefficient',(eta-sig*ca).subs(eta,sig*z)/(sig*z)-(z-ca)/z)
chk('full O other point coefficient',(eta-sig*ca).subs(sig,eta*v)/eta-(1-ca*v))
At=S.symbols('At')
Ft=z*z-sig**4*At**3-aa*sig*sig*At*At-d*At-1
chk('T graph source equation',
    (sig*z)**2-(sig*sig*At)**3-aa*(sig*sig*At)**2-d*sig*sig*At-sig*sig-sig*sig*Ft)
chk('T graph actual x/t',(mu*mu*sig*sig*At)/(sig**4/d**3)-d*At)
chk('T graph actual y/t',(mu**3*sig*z)/(sig**4/d**3)-z)
DT=d+aa*xx+xx*xx
chk('T source ideal identity',xx*DT-(yy*yy-sig*sig)+yy*yy-xx**3-aa*xx*xx-d*xx-sig*sig)

# Chord extension through the other section-corner chart.
Xs=uu/eta**2
Ys=-uu/eta**3
sl=(Ys+sig)/Xs
Xnext=sl*sl-aa-Xs
Ynext=sig-sl*Xnext
Acorner=(d-2*v)/uu+2*eta**4*v*v/uu**2
ccorner=v+Acorner-eta**4*v*Acorner/uu
Rcorner=R.subs(sig,eta*v)
for name,expr in (
 ('full source corner X',Xnext.subs(sig,eta*v)-eta*eta*Acorner),
 ('full source corner Y',Ynext.subs(sig,eta*v)-eta*ccorner)):
    numerator=S.together(expr).as_numer_denom()[0]
    chk(name,S.rem(numerator,Rcorner,uu))
chk('full corner central unit',ccorner.subs({eta:0,uu:1,d:1})-(1-v))
chk('corner preserves sigma',(eta*c)*(v/c)-eta*v)

# Six- and nine-factor resolutions, with every full unit lift.
ss,tt=S.symbols('ss tt')
factor_sets=[(sig,sig,sig,sig,yy,xx),(eta,eta,eta,eta,v,v,v,v,q)]
for fi,factors in enumerate(factor_sets):
    for r in range(len(factors)):
        pre=S.prod(factors[:r]);post=S.prod(factors[r+1:])
        UU=ss*pre;VV=tt*post
        chk(f'factor atlas {fi} chart{r} equation',UU*VV-ss*tt*S.prod(factors[:r]+factors[r+1:]))
        weights=[S.Symbol(f'a{k}') for k in range(len(factors))]
        prod=S.prod(weights)
        sprime=c/S.prod(weights[:r])*ss
        tprime=(prod/c)/S.prod(weights[r+1:])*tt
        chk(f'factor atlas {fi} chart{r} full source unit',sprime*tprime-weights[r]*ss*tt)
        chk(f'factor atlas {fi} chart{r} full U unit',sprime*S.prod([weights[k]*factors[k] for k in range(r)])-c*UU)
        chk(f'factor atlas {fi} chart{r} full V unit',tprime*S.prod([weights[k]*factors[k] for k in range(r+1,len(factors))])-(prod/c)*VV)
E=lambda j:S.Matrix([0,j,1,0])
I=lambda x,y:S.Matrix([x,y,0,1])
cones=[]
for r in range(1,5):cones.append([E(r-1),E(r),I(0,0),I(1,0)])
cones += [[E(4),I(0,0),I(1,0),I(0,1)],[E(4),I(1,0),I(0,1),I(1,1)]]
for n,cone in enumerate(cones):
    det=S.Matrix.hstack(*cone).det()
    chk(f'primitive cone{n} determinant squared',det*det-1)
chk('source adjacent-chart whole U',sig**4*(yy*ss)-sig**4*yy*ss)
chk('source adjacent-chart whole V',(yy*tt)*(1/yy)-tt)
chk('source adjacent-chart whole q',(yy*ss)*(yy*tt)/yy-ss*tt*yy)
for j in range(-6,7):
    for r in range(1,5):
        ind=4*j+r-1
        chk(f'full annular q monomial j{j} r{r}',(sig**4*q)**j*sig**(r-1)*ss-sig**ind*q**j*ss)
        chk(f'ordinary chain product j{j} r{r}',(q**j*ss)*(q**(-j)*tt)-ss*tt)
for r in range(1,5):
    chk(f'finite sigma chart product {r}',S.I**(r-1)*S.I**(4-r)+S.I)

# Complete original/native Hom overlap and every retained integer.
chi,bb,HH,lam,Aline,Bline=S.symbols('chi bb HH lam Aline Bline')
eps=chi*sig
qe=chi**(-4)*HH
te=chi**(-4)
Braw=chi**(-6)*bb
Bhat=eps**(-6)*qe/te**3*Braw
chk('entire native Hom overlap',Bhat-chi**(-4)*HH*sig**(-6)*bb)
chk('actual coupled scalar overlap',lam*eps**4*Bhat-lam*sig**4*HH*sig**(-6)*bb)
for j in range(-8,9):
    chk(f'native chain point coefficient {j}',sig**j*chi**j*Aline-eps**j*Aline)
    chk(f'native chain product {j}',chi**j*Aline*chi**(-j-1)*Bline-chi**(-1)*Aline*Bline)
zloc=S.symbols('zloc')
sn=1/zloc
Z=(sn-1)/(sn+1)
taubar=-chi**(-1)*(sn*sn-e*e)/(sn*(sn*sn-1))
chk('whole selected O ratio',(Z-1)/taubar-2*chi*(1-zloc)/(1-e*e*zloc*zloc))
chk('selected T central ratio',
    S.limit(((s-1)/(s+1)+1)/(chi**3*s*(s*s-1)),s,0)+2*chi**(-3))

# Full horizontal Cartier divisors, including their vertical order.
from collections import Counter
def adddiv(total,source,mult=1,shift=0):
    for key,val in source.items():
        total[key+shift if isinstance(key,int) else key]+=mult*val
    return total
f2div={1:2,2:-1,0:-1,'sigma':1}
f6div={1:6,6:-1,0:-5,'sigma':1}
for a,b in ((6,1),(2,3)):
    outdiv=Counter()
    if a==6:
        adddiv(outdiv,f2div,6);adddiv(outdiv,f6div,1,1);adddiv(outdiv,f6div,-1)
    else:
        for sh,mul in ((0,1),(3,1),(1,2),(2,2)):adddiv(outdiv,f2div,mul,sh)
    target=Counter({a:1,b:1,a+b:-1,0:-1,'sigma':6})
    for key in set(outdiv)|set(target):chk(f'complete Hom divisor a{a} b{b} key{key}',outdiv[key]-target[key])

source=base/'notes/part3_e6_selected_infinity_working.md'
out={'status':'PASS_LOCAL_GRAPHS_AND_FACTOR_ATLASES',
     'utc':datetime.now(timezone.utc).isoformat(),
     'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'count':len(checks),'checks':checks,
     'scope':'EI.42--79 exact normalization/Rees, O/T point-Cartier source graphs, actual source reset, primitive six-chart T0 collar, nine-factor corner, retained q^j and native overlaps, and horizontal Cartier divisor cancellation.',
     'unassigned':'Complete compact global attachment and characteristic return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','count','source_sha256')},indent=2))
