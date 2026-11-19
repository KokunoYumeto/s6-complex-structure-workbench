#!/usr/bin/env python3
"""Fresh exact checks of K109/110/113/114 endpoint algebra.

Written in this continuation without importing a supplied calculator.  This
certificate checks the displayed algebra and integral lattice operations;
the compactness, analytic extension and cover-lifting arguments are audited
separately in IV_endpoint_proof_audit.md.
"""
from pathlib import Path
import hashlib, json, time
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
EVENTS = []
START = time.time()
def check(name, value, details=None):
    good = bool(value)
    EVENTS.append({"name": name, "passed": good, "details": details})
    if not good:
        raise AssertionError(name)
def zero(name, expression):
    out = S.factor(S.cancel(expression))
    check(name, out == 0, str(out))

t, r, x, y, s, w, h, z = S.symbols('t r x y s w h z')
F = x**3+r*x**2+t*x+t**2
D = 27*t**2+(4-18*r)*t+r**2*(4*r-1)
zero('Weierstrass discriminant', 16*S.discriminant(F,x)+16*t**2*D)
p=t-r**2/3
qc=t**2-r*t/3+2*r**3/27
j=-256*(r**2-3*t)**3/(t**2*D)
zero('short-cubic j',1728*4*p**3/(4*p**3+27*qc**2)-j)
zero('node discriminant',S.discriminant(D,t)-16*(1-3*r)**3)
zero('denominator at triple zero',D.subs(t,r**2/3)-r**2*(3*r-1)**2/3)
zero('infinity simple-zero coefficient',S.limit(j.subs(t,1/z)/z,z,0)-256)
zero('zero double-pole coefficient',S.limit(t**2*j,t,0)+256*r**4/(4*r-1))
zero('r=0 exact j',j.subs(r,0)-6912/(27*t+4))
sig=(18*r-4)/27
prod=r**2*(4*r-1)/27
Pr=(324*r**3-405*r**2+144*r-16)/2187
Qr=2*(9*r-2)*(972*r**3-891*r**2+288*r-32)/531441
zero('critical centroid P',prod-sig**2/3-Pr)
zero('critical centroid Q',prod*sig/3-2*sig**3/27-Qr)
om=S.symbols('omega')
rr=(1-om**2)/3
tc=(om-1)**2*(2*om+1)/27
zero('marked root substitution',D.subs({r:rr,t:tc}))
zero('marked inverse',((54*t-18*r+4)/(4*(1-3*r))).subs({r:rr,t:tc})-om)
zero('marked excluded product', (r*(4*r-1)*(3*r-1)).subs(r,rr)+om**2*(om**2-1)*(4*om**2-1)/9)
zero('r0 marked selected node',tc.subs(om,-1)+S.Rational(4,27))

# Group law is derived directly from chord intersection with the input cubic.
rs=S.Rational(1,4)-s
def plus(P,Q, tangent=False):
    xp,yp=P; xq,yq=Q
    slope=(3*xp**2+2*rs*xp+t)/(2*yp) if tangent else (yq-yp)/(xq-xp)
    xx=S.factor(slope**2-rs-xp-xq)
    yy=S.factor(-yp+slope*(xp-xx))
    return xx,yy
G=(S.Integer(0),t)
G2=plus(G,G,True)
G3=plus(G,G2)
zero('2G x',G2[0]-s)
zero('2G y',G2[1]+t+s/2)
zero('3G x',G3[0]-4*t**2/s**2-2*t/s)
zero('3G y',G3[1]-8*t**3/s**3-6*t**2/s**2-t/s+t)
for name,(xx,yy) in [('2G',G2),('3G',G3)]:
    zero(name+' lies on source', yy**2-(xx**3+rs*xx**2+t*xx+t**2))
zero('original additive 3G coordinate',S.limit(-(G3[0]/t**2)/(G3[1]/t**3),t,S.oo)+s/2)
zero('good-root formal logarithm leading coefficient',S.limit(-(z**2*G3[0].subs(t,z**-3))/(z**3*G3[1].subs(t,z**-3))/z**2,z,0)+s/2)

u=w-1; v=w+h
xx=s+u*v; tt=xx*h/2; yy=xx*(u+v)/2
zero('whole source chart', yy**2-(xx**3+rs*xx**2+tt*xx+tt**2))
xp=v*h; yp=tt-(v-S.Rational(1,2))*xp
zero('inverse-translation source equation',yp**2-(xp**3+rs*xp**2+tt*xp+tt**2))
def f2(X,Y,T): return (Y-T-X/2)/(X-s)
zero('M2 full finite coefficient',f2(xx,yy,tt)*f2(xp,yp,tt)/tt-2*v/(s-v*h))

# The M6 exceptional specialization is done before taking the central limit.
G31=tuple(q.subs(s,1) for q in G3)
G61=tuple(q.subs(s,1) for q in plus(G3,G3,True))
sl3=S.factor((3*G3[0]**2+2*rs*G3[0]+t)/(2*G3[1]))
zero('s1 tangent at 3G',sl3.subs(s,1)-(24*t**3+24*t**2+3*t-1)/(2*t*(4*t+3)))
zero('s1 x6G',G61[0]-(4*t**2+2*t-1)*(16*t**4+24*t**3+16*t**2+4*t-1)/(4*t**2*(4*t+3)**2))
def f3(X,Y,T):
    U=Y-T-X/2; V=Y+T+X/2
    return s*X*U/(s*V-(s+2*T)*X)
def g23(X,Y,T):
    X3,Y3=G31
    X6,_=G61
    return (Y-Y3.subs(t,T)-sl3.subs(s,1).subs(t,T)*(X-X3.subs(t,T)))/(X-X6.subs(t,T))
x1=xx.subs(s,1); t1=tt.subs(s,1); y1=yy.subs(s,1)
xp1=xp; yp1=yp.subs(s,1)
ratio3=S.cancel((f3(xp,yp,tt)/f3(xx,yy,tt)).subs(s,1)/h)
ratio23=S.cancel(g23(xp1,yp1,t1)/g23(x1,y1,t1)/h)
lim3=S.factor(S.limit(ratio3,h,0))
lim23=S.factor(S.limit(ratio23,h,0))
x0=w*w-w+1
zero('s1 complete f3 ratio',lim3-w**3/((w-1)*x0))
zero('s1 complete tangent ratio',lim23+(w-1)**2/x0)
zero('s1 complete B6 central coefficient',(x0/w)**6*lim3**2*lim23/(x0/2)**3+8)
zero('s1 section coincidence speed',S.limit(-G61[0]/G61[1]/t,t,0)+6)

# Full E6+A1 section lattice, reconstructed from the stated component arrows.
C=S.zeros(6)
for i in range(6): C[i,i]=2
for i,k in [(0,1),(1,2),(2,3),(3,4),(2,5)]: C[i,k]=C[k,i]=-1
check('E6 determinant',C.det()==3)
e0=S.eye(6)[:,0]
check('E6 full correction column',C.inv()*e0==S.Matrix([S.Rational(4,3),S.Rational(5,3),2,S.Rational(4,3),S.Rational(2,3),1]))
gram=S.zeros(10)
gram[0,0]=gram[9,9]=-1
gram[0,1]=gram[1,0]=gram[1,9]=gram[9,1]=1
gram[2:8,2:8]=-C
gram[8,8]=-2
gram[9,2]=gram[2,9]=gram[9,8]=gram[8,9]=1
check('full ten-class unimodularity',gram.det()==-1)
zero('primitive source height',2-(e0.T*C.inv()*e0)[0]-S.Rational(1,2)-S.Rational(1,6))

# Symbolic SL2 identities retain both extension constants and the central cochain.
pa,qa,ra,pb,qb,rb=S.symbols('pa qa ra pb qb rb',nonzero=True)
AA=S.Matrix([[pa,qa],[ra,(1+qa*ra)/pa]])
BB=S.Matrix([[pb,qb],[rb,(1+qb*rb)/pb]])
va=S.Matrix(S.symbols('v1 v2')); vb=S.Matrix(S.symbols('w1 w2'))
ca,cb,aa,bb,ee,cc=S.symbols('ca cb aa bb ee cc')
JJ=S.Matrix([[0,-1],[1,0]])
def mon(A,V,c):
    out=S.eye(4); out[1:3,0]=bb*V;out[1:3,1:3]=A
    out[3,0]=c;out[3,1:3]=aa*V.T*JJ*A
    return out
MA,MB=mon(AA,va,ca),mon(BB,vb,cb)
MP=mon(AA*BB,va+AA*vb,ca+cb+aa*bb*(va.T*JJ*AA*vb)[0])
for row in range(4):
 for col in range(4): zero(f'full cochain product {row},{col}',(MA*MB-MP)[row,col])
N=S.zeros(4);N[3,0]=1
CENT=ee*S.eye(4)+cc*N
for row in range(4):
 for col in range(4): zero(f'centralizer including arbitrary c {row},{col}',(CENT*MA-MA*CENT)[row,col])
check('rank-one remaining shear',N.rank()==1)
zero('centralizer determinant',CENT.det()-ee**4)
ww=S.Matrix(S.symbols('wz1 wz2'))
dual=ww.T*JJ*(AA-S.eye(2))-(ww-AA*ww).T*JJ*AA
for col in range(2): zero('full dual-invariant equation '+str(col),dual[0,col])

# Both local inversion charts, actual whole unit coefficients, and their inverses.
Aunit,Cunit=S.symbols('Aunit Cunit',nonzero=True)
aco,bco,cco=S.symbols('a b c')
one=S.Matrix([Aunit*Cunit*aco,cco/Cunit,bco/Aunit])
back=S.Matrix([one[0]/(Aunit*Cunit),Aunit*one[2],Cunit*one[1]])
check('selected inversion full affine inverse',back==S.Matrix([aco,bco,cco]))
zero('selected first-chart base product',S.prod(one)-aco*bco*cco)
zero('selected first-chart source character',one[0]*one[1]-Aunit*aco*cco)
zero('selected first-chart line character',one[0]*one[2]-Cunit*aco*bco)

# Universal exponent identities plus finite checks in every stated residue class.
for ell in range(1,31):
 m=3*ell
 for n in (-1,1):
  check(f'M2 annular exponent l={ell},n={n}',n*ell-3*n*ell+2*n*ell==0)
  check(f'M2 triple scalar exponent l={ell},n={n}',-3*ell*n==-m*n)
  check(f'M2 complete root phase l={ell},n={n}',(-ell*n*(0+1+2))%3==0)
  for Jwind in range(-4*m,4*m+1):
   check(f'M2 primitive divisibility {ell},{n},{Jwind}',(3*n*Jwind)%m==0 if Jwind%ell==0 else (3*n*Jwind)%m!=0)
for ell in range(31):
 m=3*ell+2
 for n in (-1,1):
  for nu in range(-25,26):
   check(f'full negative annular norm {m},{n},{nu}',n+m*nu!=0)

result={
 'actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited from root (not separately exposed)',
 'scope':'Fresh exact algebra certificate, not a replacement for analytic and geometric proof review',
 'source_labels':['night:P3K.109','night:P3K.110','night:P3K.113','night:P3K.114'],
 'checks':len(EVENTS),'passed':all(e['passed'] for e in EVENTS),
 'elapsed_seconds':time.time()-START,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'events':EVENTS,
}
out=ROOT/'independent_IV_endpoint_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='events'},indent=2))
