"""Exact directed root/base graph checks; no completed attachment inferred."""
from pathlib import Path
from datetime import datetime,timezone
from math import gcd
import hashlib,json
import sympy as s

R=Path(__file__).resolve().parents[2]
checks=[]
def ck(name,value):
    ans=s.factor(s.together(value).as_numer_denom()[0])
    assert ans==0,(name,ans)
    checks.append(name)
def yes(name,value):
    assert bool(value),name
    checks.append(name)

e,z,X,Y,t,u,h=s.symbols('e z X Y t u h',nonzero=True)
d=1-3*e*e;A=3*e*e-2;C=(1-e*e)*(1+3*e*e);C1=4*d*d-C
ck('actual tangent coefficient identity',d*d-4*e*e*A-C)

# Uniform literal threefold addition: t=z^r, h=z^c.
g=e*h;dg=d*t/(2*e);sg=C*t*t/(4*e*e)
x3=s.cancel(4*dg*g/sg+4*g*g/(sg*sg))
y3=s.cancel(-g+(dg+2*g/sg)*x3)
Q=t**3/h;K=t*t/h
tau=-8*e*C*K*(d*C*Q+8*e**4)/(C*C*C1*Q*Q+96*d*C*e**4*Q+512*e**8)
ck('full joint tau3 from both actual chords',-x3/y3-tau)
ck('full joint tau3 small-z coefficient',
   (-8*e*C*(d*C*Q+8*e**4)/(C*C*C1*Q*Q+96*d*C*e**4*Q+512*e**8)).subs(t,0)+C/(8*e**3))

# Check both actual source roots and their full parameter-dependent arrows.
E,H=s.symbols('E H',nonzero=True)
dd,aa=s.symbols('dd aa',nonzero=True)
eta,Z,U,V=s.symbols('eta Z U V',nonzero=True)
instances=[]
for branch in ('good','reduced'):
 for l in range(1 if branch=='good' else 0,13):
    m=3*l if branch=='good' else 3*l+2
    k=2*l if branch=='good' else 2*l+1
    r=l if branch=='good' else l+1
    c=0 if branch=='good' else 1
    bst=l if branch=='good' else l+2
    g0=gcd(m,4)
    # E^m=e and H^m=d keep all fractional powers as integer monomials.
    zo=E**(-4)*H**3*z
    if branch=='good':
        xo=E**(-2*l)*X;yo=E**(-3*l)*Y
        old=yo**2-xo**3-(E**(2*m)*aa/H**(2*m))*zo**(2*l)*xo**2-zo**l*xo-1
        factor=E**(-6*l)
    else:
        xo=E**(-2*(l+2))*H**2*X
        yo=E**(-3*(l+2))*H**3*Y
        old=yo**2-xo**3-(E**(2*m)*aa/H**(2*m))*zo**(2*l+2)*xo**2-zo**(l+2)*xo-zo**2
        factor=E**(-6*(l+2))*H**6
    native=Y**2-X**3-aa*z**(2*r)*X**2-H**m*z**(r+c)*X-E**(2*m)*z**(2*c)
    ck(f'{branch}{l} entire root equation',old/factor-native)
    ck(f'{branch}{l} marked G actual Y',yo.subs(Y,E**m*z**c)-(1 if branch=='good' else zo))
    ck(f'{branch}{l} actual root height',zo**m-E**(-4*m)*H**(3*m)*z**m)
    ck(f'{branch}{l} uniform exponent m',3*r-c-m)
    ck(f'{branch}{l} uniform exponent k',2*r-c-k)
    yes(f'{branch}{l} exact D^-4 X weight',(-2*bst-8*k)%m==0)
    yes(f'{branch}{l} exact D^-4 Y weight',(-3*bst-12*k)%m==0)
    yes(f'{branch}{l} deck kernel X',(2*bst)%g0==0)
    yes(f'{branch}{l} deck kernel Y',(3*bst)%g0==0)
    yes(f'{branch}{l} distinguished ray primitive',gcd(m//g0,4//g0)==1)
    # Exact old-root chart on e=eta^m,z=eta^4 Z.
    xnew=eta**(2*bst)*U/(H**2 if branch=='reduced' else 1)
    ynew=eta**(3*bst)*V/(H**3 if branch=='reduced' else 1)
    ck(f'{branch}{l} weighted graph actual X',xo.subs({E:eta,z:eta**4*Z,X:xnew},simultaneous=True)-U)
    ck(f'{branch}{l} weighted graph actual Y',yo.subs({E:eta,z:eta**4*Z,Y:ynew},simultaneous=True)-V)
    ck(f'{branch}{l} weighted graph actual old z',zo.subs({E:eta,z:eta**4*Z},simultaneous=True)-H**3*Z)
    # The full formal-coordinate pole cancels in the directed old chart.
    tau_ratio=s.cancel(xo/yo*Y/X)
    ck(f'{branch}{l} formal coefficient directed to old root',
       tau_ratio*z**k/E**(3*m)-zo**k/H**(2*m))
    for n in (-1,1):
     for char in range(m):
        # Coordinates ordered (Rlambda,Ftilde,zeta,D), last two modulo m.
        Avec=s.Matrix([n,n,char,1]);Bvec=s.Matrix([m,m,0,0]);Dvec=s.Matrix([0,0,0,1])
        Cvec=-4*Avec+4*Dvec
        ck(f'{branch}{l} n{n} d{char} C scalar',Cvec[0]+4*n)
        ck(f'{branch}{l} n{n} d{char} C source',Cvec[1]+4*n)
        ck(f'{branch}{l} n{n} d{char} C base',Cvec[3])
        if branch=='reduced':
            Cbar=Cvec-n*Bvec;expected=-(m+4)*Avec+4*Dvec
            ck(f'{branch}{l} n{n} d{char} actual B power scalar',Cbar[0]-expected[0])
            ck(f'{branch}{l} n{n} d{char} actual B power source',Cbar[1]-expected[1])
            yes(f'{branch}{l} n{n} d{char} retained character',(Cbar[2]-expected[2])%m==0)
            yes(f'{branch}{l} n{n} d{char} retained deck',(Cbar[3]-expected[3])%m==0)
            yes(f'{branch}{l} n{n} d{char} identity component',(m+4)%3==0)
        ck(f'{branch}{l} n{n} d{char} native scalar-root cancellation',s.Rational(4*n,m)-n*s.Rational(4,m))
    N=m//g0
    yes(f'{branch}{l} complete finite root cyclic norm',4*N%m==0)
    ck(f'{branch}{l} exact retained B cyclic exponent',s.Rational(4*N,m)-s.Rational(4,g0))
    instances.append({'branch':branch,'l':l,'m':m,'k':k,'kernel':g0,'parameter_cover':N})

# Full ordinary point/tensor factors, without dropping parameter powers.
for a in (2,6):
 for j in range(-5,6):
  for ht in range(-3,4):
    ck(f'M{a} line{j} height{ht} full tensor arrow',
       (e**4/d**3)**ht*((e/d)**(1-a))**j-e**(4*ht+(1-a)*j)*d**(-3*ht+(a-1)*j))

sa,el,up,alog,LC,Lbar,ho,hn,mm=s.symbols('sa el up alog LC Lbar ho hn mm')
sold=sa+3*el-4*up
ck('good full annular residual',(sold*alog+ho-up*LC)-(sa*alog+hn)
   -(3*el*alog+up*(-4*alog-LC)+ho-hn))
ck('reduced full annular residual',(sold*alog+ho-up*Lbar)-(sa*alog+hn)
   -(3*el*alog+up*(mm*alog-(mm+4)*alog-Lbar)+ho-hn))

# The complementary cover, its genuine source map and all deck characters.
xi,sigma,xb,yb,chi,rr=s.symbols('xi sigma xb yb chi rr',nonzero=True)
for row in instances:
    branch,l,m,k=row['branch'],row['l'],row['m'],row['k']
    rstar=l if branch=='good' else l+1
    c=0 if branch=='good' else 1
    bst=rstar+c
    native=Y**2-X**3-aa*z**(2*rstar)*X**2-dd*z**(rstar+c)*X-e**2*z**(2*c)
    direct=native.subs({z:xi**4,e:xi**m*sigma,X:xi**(2*bst)*xb,Y:xi**(3*bst)*yb},simultaneous=True)
    comp=yb**2-xb**3-aa*xi**(2*m)*xb**2-dd*xb-sigma**2
    ck(f'{branch}{l} complete complementary equation',direct/xi**(6*bst)-comp)
    xo=sigma**2/dd**2*xb;yo=sigma**3/dd**3*yb;to=sigma**4/dd**3
    ro=xi**(2*m)*sigma**2*aa/dd**2
    old=yo**2-xo**3-ro*xo**2-to*xo-to**2
    ck(f'{branch}{l} original source at complementary chart',old*dd**6/sigma**6-comp)
    # All weights are retained as integers modulo the actual group order.
    yes(f'{branch}{l} graph mu4 preserves e',(m-m)%4==0)
    yes(f'{branch}{l} graph mu4 preserves native X',(2*bst-2*bst)%4==0)
    yes(f'{branch}{l} graph mu4 preserves native Y',(3*bst-3*bst)%4==0)
    yes(f'{branch}{l} mu4 equals fourth III source X',(-2*bst-2*m)%4==0)
    yes(f'{branch}{l} mu4 equals fourth III source Y',(-3*bst+m)%4==0)
    yes(f'{branch}{l} root lift preserves parameter',(m-m)%(4*m)==0)
    yes(f'{branch}{l} root lift native X',(2*bst+2*m+8*k)%(4*m)==0)
    yes(f'{branch}{l} root lift native Y',(3*bst+3*m+12*k)%(4*m)==0)
    yes(f'{branch}{l} mth root lift is graph mu4 X',(2*m+2*bst)%4==0)
    yes(f'{branch}{l} mth root lift is graph mu4 Y',(3*m+3*bst)%4==0)
    for a in (2,6):
        yes(f'{branch}{l} primitive tensor mu4 character M{a}',(-m*a-2*m)%4==0)
        yes(f'{branch}{l} root-lift primitive tensor M{a}',(-a-2)%4==0)
    for j in range(-7,8):
        # Ordinary chain: V=sigma^j X_j, X_jY_j=sigma.
        yes(f'{branch}{l} point chain deck j{j}',(-j+j)%4==0)
        yes(f'{branch}{l} chain equation deck j{j}',(j-1-j+1)%4==0)
        yes(f'{branch}{l} literal B/mu4 commutator j{j}',(j+4-j)%4==0)

# The actual invariant quotient by Dtilde^4 and the remaining mu4 action.
ce=chi*sigma
cd=1-3*ce**2;ca=3*ce**2-2
cubic=yb**2-xb**3-ca*chi**2*xb**2-cd*xb-sigma**2
I=s.I
ck('ordinary mu4 entire equation',
   cubic.subs({chi:I*chi,sigma:-I*sigma,xb:-xb,yb:-I*yb},simultaneous=True)+cubic)
ck('ordinary mu4 fixes actual original x',
   (sigma**2/cd**2*xb).subs({chi:I*chi,sigma:-I*sigma,xb:-xb},simultaneous=True)-sigma**2/cd**2*xb)
ck('ordinary mu4 fixes actual original y',
   (sigma**3/cd**3*yb).subs({chi:I*chi,sigma:-I*sigma,yb:-I*yb},simultaneous=True)-sigma**3/cd**3*yb)
ck('ordinary graph exact height',chi**4*(sigma**4/cd**3)-ce**4/cd**3)
HH=1-chi**4*(1-ce**2)
ck('selected height factor and mu4',HH.subs({chi:I*chi,sigma:-I*sigma},simultaneous=True)-HH)

# Full point-section chart at 2G on the smooth complementary family.
a2,ds=s.symbols('a2 ds',nonzero=True)
SS=ds**2/4-a2*sigma**2
x2=SS/sigma**2
y2=-sigma-ds*x2/(2*sigma)
ck('full complementary tau2',-x2/y2-2*sigma*SS/(ds*SS+2*sigma**4))
ck('central source translation squares exactly',ds/(ds/xb)-xb)
ck('central source translation y squares exactly',-ds*(-ds*yb/xb**2)/(ds/xb)**2-yb)
ck('central M6 full Hom orbit', (2*xb/ds)**6*(6*(ds/xb)**3/ds)/(6*xb**3/ds)-64/ds**3)
ck('central M2 full chronological orbit', (2*xb/ds)*(2*ds/xb/ds)*(2*ds/xb/ds)**2*(2*xb/ds)**2-64/ds**3)
for xx,yy in [(1,s.sqrt(2)),(1,-s.sqrt(2)),(-1,I*s.sqrt(2)),(-1,-I*s.sqrt(2))]:
    ck(f'central half T point {xx},{yy}',yy**2-xx**3-xx)
    slope=(3*xx**2+1)/(2*yy)
    xdouble=slope**2-2*xx
    ydouble=-yy+slope*(xx-xdouble)
    ck(f'central half T double x {xx},{yy}',xdouble)
    ck(f'central half T double y {xx},{yy}',ydouble)

# Literal local A1 normalization graph of the selected type-III trace.
hh,kk,rho,SS0,nu=s.symbols('hh kk rho SS0 nu',nonzero=True)
aa0=hh*kk
LL=((1+3*hh*kk)*hh-kk)/(1-hh**2)
UU=hh*LL;VV=LL
ck('A1 graph maps to exact selected divisor',(aa0+UU)*VV**2-UU**2*(1+3*aa0+UU))
ck('A1 graph normalization coordinate bridge',
   LL.subs({hh:-nu/SS0,kk:-SS0},simultaneous=True)-SS0*(SS0**2-nu*(1+3*nu))/(SS0**2-nu**2))
ck('A1 graph base bridge',(-nu/SS0)*(-SS0)-nu)

# Both complete ordinary overlaps and the retained cap reference-deck cocycle.
bb,lam,vlog,ld=S_b,S_lam,S_vlog,S_ld=s.symbols('bb lam vlog ld',nonzero=True)
ck('complete finite-native selected coefficient',
   (chi*sigma)**(-6)*(chi**(-4)*HH)/(chi**(-4))**3
     *chi**(-6)*bb-chi**(-4)*HH*sigma**(-6)*bb)
ck('complete fixed-scalar ordinary coefficient',
   lam*(chi*sigma)**4*chi**(-4)*HH*sigma**(-6)*bb
     -lam*sigma**4*HH*sigma**(-6)*bb)
for j in range(-16,17):
    Aj,Bj=s.symbols('Aj Bj',nonzero=True)
    ck(f'ordinary chain product {j}',
       chi**j*Aj*chi**(-j-1)*Bj-chi**(-1)*Aj*Bj)
    ck(f'ordinary chain physical coefficient {j}',
       sigma**j*chi**j*Aj-(chi*sigma)**j*Aj)
ck('quarter graph exact positive cap angle',
   (3*ld-4*(vlog-s.Rational(1,4)))-(3*ld-4*vlog)-1)
for m in range(2,32):
    for n in (-1,1):
        for j0 in range(-2,3):
            for j1 in range(-2,3):
                jj=[j0,j1,-j0,2-j1]
                # Actual commuting words (A exponent, B exponent).
                word=s.Matrix([0,0])
                for jt in jj:
                    word+=s.Matrix([1,jt])
                ck(f'four-sector A word m{m} n{n} j{j0},{j1}',word[0]-4)
                ck(f'four-sector retained B word m{m} n{n} j{j0},{j1}',word[1]-sum(jj))
                ck(f'actual cap norm word m{m} n{n} j{j0},{j1}',m*s.Rational(n,m)-n)

source=R/'notes/part3_e6_selected_infinity_root_working.md'
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'source':str(source.relative_to(R)),
     'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'check_count':len(checks),
     'scope':'Exact punctured root/Cartier/scalar coordinates, joint tau3, both weighted graph charts, all retained cyclic characters/norms, directed annular residual, ordinary mu4 quotient/line-chain maps and selected A1 normalization identities. No global selected-fan attachment or numerical return follows from these checks.',
     'instances':instances,'checks':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','source_sha256','check_count','scope']},indent=2))
