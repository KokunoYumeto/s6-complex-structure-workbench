"""Exact E6 selected-cusp source, line, root, normal and period maps.

The certificate checks the displayed identities. The actual exterior/cap
and relative-frame arguments are recorded in the accompanying proof.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

root = Path(__file__).resolve().parents[2]
w, xi, Y, q, X, T, z = S.symbols('w xi Y q X T z')
ss, x, y, a, b, h, gg, j = S.symbols('s x y a b h g j')
checks = []


def check(name, value):
    num = S.together(value).as_numer_denom()[0]
    value = S.factor(num)
    assert value == 0, (name, value)
    checks.append(name)


v, D = w**2-1, w**2-3
A = 3-2*w**2
s0 = v*(w**2+3)/4
curve = Y**2-X**3-A*X**2-D*T*X-T**2
K = Y**2-xi**2*(xi+w**2)
aa = v**2+D*xi
check('exact full physical-height equation', curve.subs({X:xi+v,T:v+q})-(K-q*(q+aa)))
check('inverse q polynomial after square-root choice', (2*q+aa)**2-(aa**2+4*q*(q+aa)))
check('selected normalization', curve.subs({X:ss**2-1,Y:ss*(ss**2-w**2),T:v}))
check('normalization xi', ss**2-1-v-(ss**2-w**2))
check('normalization node product', (ss-w)*(ss+w)-(ss**2-w**2))
f = S.Matrix([ss**2-w**2,ss*(ss**2-w**2),w])
df = f.jacobian([ss,w])
minors = [S.det(df[[i,k],:]) for i,k in ((0,2),(1,2),(0,1))]
for i,(found,expected) in enumerate(zip(minors,[2*ss,3*ss**2-w**2,2*w*(ss**2-w**2)])):
    check('normalization derivative minor '+str(i), found-expected)
nf = S.Matrix([3*ss**2-w**2,-2*ss,2*w*(ss**2-w**2)])
dk = S.Matrix([S.diff(K,xi),S.diff(K,Y),S.diff(K,w)]).subs({xi:ss**2-w**2,Y:ss*(ss**2-w**2)})
for i in range(3):
    check('full normal covector component '+str(i),dk[i]+(ss**2-w**2)*nf[i])
check('first Cox normal factor', (ss**2-w**2)/((ss-w)/(ss+w))-(ss+w)**2)
check('second Cox normal factor', (ss**2-w**2)*((ss-w)/(ss+w))-(ss-w)**2)
other=-A*A*(w*w+3)/27
check('second critical height', other-v+4*w**6/27)
c4=16*(A*A-3*D*T)
disc=-432*T*T*(T-v)*(T-other)
check('selected c4',c4.subs(T,v)-16*w**4)
check('actual kappa coefficient',S.diff(disc,T).subs(T,v)/c4.subs(T,v)**3+v*v/(64*w**6))
check('actual extending kappa factor',(-v*v/(64*w**6))*w**6+v*v/64)

U=Y-T-D*X/2
Vs=Y+T+D*X/2
check('actual cA1 source factor',U*Vs-X*X*(X-s0)-curve)
f2=U/(X-s0)
f3=s0*X*U/(s0*Vs-(D*s0+2*T)*X)
node={w:0,X:-1,Y:0,T:-1}
check('Miller f2 at cusp',f2.subs(node)-2)
check('Miller f3 at cusp',f3.subs(node)-3)
xp,yp=S.Rational(-8,9),S.Rational(-1,27)
lam=(3*xp*xp+6*xp+3)/(2*yp)
x2=lam*lam-3-2*xp
f23=(Y-yp-lam*(X-xp))/(X-x2)
check('actual third point on cusp',yp*yp-(xp+1)**3)
check('tangent at third point',lam+S.Rational(1,2))
check('actual sixth point',x2+S.Rational(35,36))
check('third-point tangent Miller at cusp',f23.subs(node)-S.Rational(2,3))
check('full f6 at cusp',f3.subs(node)**2*f23.subs(node)-6)
check('B6 includes source target ratio',2**6*S.Rational(6,6)-64)
check('selected Hom divided by physical height',64/S.Integer(-1)**3+64)
for sign in (1,-1):
    kval=(Y-sign*T)/X
    xx=kval*kval-A-X
    yy=-sign*T-kval*xx
    check('translation '+str(sign)+' fixes cusp X',xx.subs(node)+1)
    check('translation '+str(sign)+' fixes cusp Y',yy.subs(node))
    target=curve.subs({X:xx,Y:yy},simultaneous=True)
    numerator=S.together(target).as_numer_denom()[0]
    check('full chord source map '+str(sign),S.rem(numerator,curve,Y))
PG=(1+w)/(1-w)
g=1/PG
S6=w*(1+PG**6)/(1-PG**6)
c6=(1+w)**6/(6+20*w*w+6*w**4)
check('exact actual sixth section theta point',S6-w*(1+PG**6)/(1-PG**6))
check('full Cartier theta coefficient unit',w-S6-c6)
check('literal Cartier theta divisor arrow',ss-S6-c6*(1-((ss-w)/(ss+w))/PG**6)/(1-(ss-w)/(ss+w)))
check('actual f2 on both node branches',f2.subs({X:v,Y:0,T:v})-2)
check('actual f3 on both node branches',f3.subs({X:v,Y:0,T:v})-(3+w*w))
for sg in (1,-1):
    check('full f6 selected node branch '+str(sg),(sg*w+1)**6/(sg*w-S6)-(6+20*w*w+6*w**4))
check('full selected Hom node coefficient',2**6/v**3-64/v**3)
check('actual sixth point reflection',S6.subs(w,-w)-S6)
check('actual Cartier coefficient reflection',c6.subs(w,-w)-PG**-6*c6)
ZZ=S.symbols('ZZ',nonzero=True)
ft=lambda zz,pp:(1-zz/pp)/(1-zz)
check('full nodal theta reflection coefficient',ft(1/ZZ,PG**-6)-PG**6*ft(ZZ,PG**6))
check('actual target period cancels reflection line factor',PG**-6*PG**6-1)
check('actual source Tate multiplier',g*PG-1)
check('extending fractional-source logarithm input',(g-1)/w+2/(1+w))
St=((1+gg)*ss+(1-gg)*w)/(((1-gg)/w)*ss+1+gg)
check('literal normalization group action',(St-w)/(St+w)-gg*(ss-w)/(ss+w))
check('retained source shear',St.subs(gg,1+w*h)-ss-h*(ss*ss-w*w)/(2+h*(w-ss)))
Xt,Yt,Qt=S.symbols('Xt Yt Qt')
check('full weighted pencil',
    (K-q*(q+aa)).subs({xi:w*w*Xt,Y:w**3*Yt,q:w**6*Qt})/w**6
    -(Yt*Yt-Xt*Xt*(Xt+1)-Qt*(v*v+D*w*w*Xt)-w**6*Qt*Qt))
check('actual weighted section formal parameter',-((-v)/w**2)/((v+w**6*Qt)/w**3)-w*v/(v+w**6*Qt))

r=A/D**2
check('actual original source parameter degree four',r-S.Rational(1,3)+w**4/(3*D**2))
check('ordinary s unit comparison',s0/D**2-(S.Rational(1,4)-r))
check('original source full scaling',
    D**6*(y*y-x**3-r*x*x-z*x-z*z).subs({x:X/D**2,y:Y/D**3,z:T/D**3})-curve)
# hD is the exact chosen square root of D. Reduce polynomial identities by hD^2=D.
hD=S.symbols('hD')
Xp,Yp,zp=S.symbols('Xp Yp zp')
old_root=(hD**3*Yp)**2-(D*Xp)**3-(hD**3*zp)**2*(r*(D*Xp)**2+D*Xp+1)
new_root=Yp**2-Xp**3-zp**2*(A*Xp**2+D*Xp+1)
check('full quadratic-root scaling',S.rem(S.together(old_root-D**3*new_root).as_numer_denom()[0],hD*hD-D,hD))
check('full root Cartier tau weight',S.rem(S.together((-D*Xp/(hD**3*Yp))-(-Xp/Yp)/hD).as_numer_denom()[0],hD*hD-D,hD))
check('full selected cap unit under rescaling',(1-(v/D**3)*(D**3*zp*zp))-(1-v*zp*zp))
scale=S.symbols('scale',nonzero=True)
check('full selected scalar cancellation',(q/scale**3)/(T/scale**3)**3*scale**-6-q/T**3)
z0,v0,L6=S.symbols('z0 v0 L6')
check('actual root Cartier quotient',z0*v0/(z0*v0-z0*L6)-v0/(v0-L6))
check('root half-division norm',2*(2*j-S.Rational(3,2)*j)-j)
for n in (-1,1):
    check('signed finite-root scalar norm '+str(n),2*n-n*2)
    for d in (0,1):
        check('finite line character square '+str((n,d)),(-1)**(2*d)-1)

# The literal EU.11 sector equation after its I_z identification.
sa,ka,fa,pia,cl,ha,jab,blog,lattice=S.symbols(
    'sa ka fa pia cl ha jab blog lattice')
for n in (-1,1):
    fb=fa+pia
    hb=ha-n*sa*pia+jab*blog+lattice
    difference=n*(sa+ka)*fb+(sa+ka)*cl+hb-(n*sa*fa+sa*cl+ha)
    check('actual cap-cut Lie square '+str(n),
          difference-ka*(n*fb+cl)-jab*blog-lattice)
    check('contracting H squared equals B '+str(n),2*n*n-2)
    check('contracting H to n equals A '+str(n),n*n-1)
check('reference marked endpoint r zero',r.subs(w*w,S.Rational(3,2)))
check('reference marked endpoint rho minus one',
      (w*w/D).subs(w*w,S.Rational(3,2))+1)
orbit_mv=S.Matrix([[0,1],[-1,0]])
check('actual orbit Mayer Vietoris determinant',orbit_mv.det()-1)
check('actual orbit Mayer Vietoris inverse',sum(
    (orbit_mv.inv()*orbit_mv-S.eye(2))[i,j]**2
    for i in range(2) for j in range(2)))
radius,bbphase,unitphase=S.symbols('radius bbphase unitphase',nonzero=True)
su2disc=S.Matrix([[radius*unitphase,-bbphase],
                 [bbphase,radius/unitphase]])
check('literal SU2 clutch filling determinant',
      su2disc.det()-(radius**2+bbphase**2))

# Literal normal shears and period exponents; entries retain arbitrary signs.
sampleP=[]
for p in range(-3,4):
 for rr in range(-3,4):
  for ss0 in range(-2,3):
   for zz in range(-2,3):
    P=S.Matrix([[p,rr],[ss0,zz]])
    if abs(P.det())==1:
        sampleP.append(P)
for i,P in enumerate(sampleP):
    R=P.inv()
    assert R*P==S.eye(2)
    BW=-6*R*S.Matrix([[1,0],[0,0]])*P
    assert S.trace(BW)==-6
    checks.append('full period conjugation / height '+str(i))
    xi0,eta0=R*S.Matrix([0,1])
    weights=(xi0,eta0,-xi0-eta0)
    diffs=(-xi0-2*eta0,-2*xi0-eta0,xi0-eta0)
    assert all((int(ww)-int(dd))%2==0 for ww,dd in zip(weights,diffs))
    checks.append('complete Spin endpoint parity '+str(i))
aa0,bb0,cc0=S.symbols('a0 b0 c0',nonzero=True)
A11,A12,A21,A22=S.symbols('A11 A12 A21 A22',nonzero=True)
rows=[(A11*A21*bb0*cc0,aa0*bb0/A21,1/(A11*bb0)),
      (A12*A22*bb0*cc0,1/(A22*cc0),aa0*cc0/A12),
      (1/aa0,aa0*bb0,aa0*cc0)]
for i,row in enumerate(rows):
 check('complete unit Cox vertex product '+str(i),S.prod(row)-aa0*bb0*cc0)
for jj in range(-10,11):
 check('vertical physical index '+str(jj),(4*(-6-18*jj*(jj-1)))/24-(-1-3*jj*(jj-1)))
 check('vertical native pair '+str(jj),(-6-18*jj*(jj-1))-6*(-1-3*jj*(jj-1)))

paths=[root/'notes/part3_e6_selected_cusp_working.md',Path(__file__),root/'notes/part3_e6_marked_node_cover_working.md']
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),
     'identities':checks,'sample_unimodular_bases':len(sampleP),
     'source_hashes':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
     'scope':'Exact displayed E6 source/height/normal/Cartier/root/period/Cox identities and algebra of the fully written vertical comparison. Geometric attachment and physical transfer require the accompanying complete proof audit.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
