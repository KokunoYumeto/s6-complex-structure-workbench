#!/usr/bin/env python3
"""Independent symbolic checks of opened EF/SEF/EB/III proof formulas.

The program is new. It uses elementary group-law rational functions,
polynomial identities, an integral Gram determinant and symbolic Jacobians.
No producing program is read, imported or called.
"""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as S

P=Path(__file__).resolve().parents[2]
checks=[]
def eq(name,left,right,labels):
    d=S.factor(S.cancel(left-right));assert d==0,(name,d)
    checks.append(dict(name=name,labels=labels,pass_check=True,left=str(S.factor(left)),right=str(S.factor(right))))

r,t,x,y,s,w,h,z,p,beta=S.symbols('r t x y s w h z p beta')
D=27*t*t+(4-18*r)*t+r*r*(4*r-1)
Pr=(324*r**3-405*r**2+144*r-16)/2187
Qr=2*(9*r-2)*(972*r**3-891*r**2+288*r-32)/531441
centroid=(18*r-4)/81
q=S.symbols('q')
eq('EF centered finite critical polynomial',S.expand((t*D/27).subs(t,q+centroid)),q**3+Pr*q+Qr,['P3K.109'])
eq('EF concrete P value',Pr.subs(r,S.Rational(1,2)),-S.Rational(19,8748),['P3K.109'])
eq('EF concrete Q value',Qr.subs(r,S.Rational(1,2)),S.Rational(215,2125764),['P3K.109'])

def add(Pt,Qt,a2,a4):
    X1,Y1=Pt;X2,Y2=Qt
    if Pt==Qt: slope=(3*X1*X1+2*a2*X1+a4)/(2*Y1)
    else:slope=(Y2-Y1)/(X2-X1)
    X3=S.factor(slope*slope-a2-X1-X2)
    Y3=S.factor(slope*(X1-X3)-Y1)
    return X3,Y3
G=(S.Integer(0),t)
G2=add(G,G,r,t);G3=add(G2,G,r,t)
eq('EF doubled source x',G2[0],S.Rational(1,4)-r,['P3K.109','P3K.114'])
eq('EF doubled source y',G2[1],-t-(S.Rational(1,4)-r)/2,['P3K.109','P3K.114'])
eq('EF triple source x',G3[0].subs(r,S.Rational(1,4)-s),4*t*t/s**2+2*t/s,['P3K.109'])
eq('EF triple source y',G3[1].subs(r,S.Rational(1,4)-s),8*t**3/s**3+6*t*t/s**2+t/s-t,['P3K.109'])
eq('III triple source x',G3[0].subs(r,0),8*t+64*t*t,['P3K.114'])
eq('III triple source y',G3[1].subs(r,0),3*t+96*t*t+512*t**3,['P3K.114'])
G6_s1=add(tuple(v.subs(r,-S.Rational(3,4)) for v in G3),tuple(v.subs(r,-S.Rational(3,4)) for v in G3),-S.Rational(3,4),t)
eq('EF s=1 specialized 6G x',G6_s1[0],(4*t*t+2*t-1)*(16*t**4+24*t**3+16*t*t+4*t-1)/(4*t*t*(4*t+3)**2),['P3K.109'])
eq('EF s=1 coincident section formal derivative',S.limit(-G6_s1[0]/G6_s1[1]/t,t,0),-6,['P3K.109'])

A=S.Matrix([[2,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,0,-1],[0,0,-1,2,-1,0],[0,0,0,-1,2,0],[0,0,-1,0,0,2]])
eq('EF E6 determinant',A.det(),3,['P3K.109','P3K.114'])
col=A.inv()[:,0]
want=S.Matrix([S.Rational(4,3),S.Rational(5,3),2,S.Rational(4,3),S.Rational(2,3),1])
for i in range(6):eq('EF E6 correction column '+str(i),col[i],want[i],['P3K.109','P3K.114'])
gram=S.zeros(10);gram[0,0]=gram[9,9]=-1;gram[0,1]=gram[1,0]=gram[9,1]=gram[1,9]=1
gram[2:8,2:8]=-A;gram[8,8]=-2;gram[9,2]=gram[2,9]=gram[9,8]=gram[8,9]=1
eq('EF full integral source Gram determinant',gram.det(),-1,['P3K.109','P3K.114'])
eq('EF source height',2-col[0]-S.Rational(1,2),S.Rational(1,6),['P3K.109','P3K.114'])

# Derive the actual inverse chord and Miller product in a rational source chart.
vv=w+h;xx=s+(w-1)*vv;tt=xx*h/2;yy=xx*(2*w+h-1)/2;rr=S.Rational(1,4)-s
eq('SEF rational source chart',yy*yy-(xx**3+rr*xx*xx+tt*xx+tt*tt),0,['P3K.109','P3K.110','P3K.114'])
minusG=add((xx,yy),(0,-tt),rr,tt)
eq('SEF inverse translation x',minusG[0],vv*h,['P3K.110','P3K.114'])
eq('SEF inverse translation y',minusG[1],tt-(vv-S.Rational(1,2))*vv*h,['P3K.110','P3K.114'])
def f2(X,Y,T,SS):return (Y-T-X/2)/(X-SS)
B21=S.factor(f2(xx,yy,tt,s)*f2(minusG[0],minusG[1],tt,s))
eq('SEF full finite Miller coefficient',B21/tt,2*vv/(s-vv*h),['P3K.110','P3K.114'])
eq('III strict component coefficient',(2*w/s).subs({s:S.Rational(1,4),w:S.Rational(1,2)-1/p}),4*(p-2)/p,['P3K.114'])
Tcentral=(1/(beta-1)**2,-1/(beta-1)**3)
eq('III exceptional component coefficient',-4*(beta-1-(beta**2-1)/2)*f2(*Tcentral,0,S.Rational(1,4)),4*(beta-1)/(beta-3),['P3K.114'])
eq('III strict point-frame coefficient',4*(p-2)/p/((p-2)/p),4,['P3K.114'])
eq('III exceptional point-frame coefficient',4*(beta-1)/(beta-3)*(beta-3)/(beta-1),4,['P3K.114'])

# Obtain the generic M6 valuations directly from the group law and first
# source-chart jets, and specialize s=1 before taking its limits.
x0=s+w*w-w;alpha=2*w/x0;bet=(s-w*w)/x0
mu0=(1-3*s)/(2*(1-s));x60=S.factor(mu0*mu0-(S.Rational(1,4)-s))
f3prime=alpha*(bet-1-alpha/2)/(bet+1-alpha/2)
f23prime=(bet-(1/s-1)-mu0*(alpha-2/s))/(-x60)
eq('EF generic M6 translated f3 coefficient',f3prime,2*w**3/(x0*(w-s)),['P3K.109'])
eq('EF generic M6 translated tangent coefficient',f23prime,2*(1-s)*(w-s)**2/(s**3*x0),['P3K.109'])
f23central=(x0*(w-S.Rational(1,2))-mu0*x0)/(x0-x60)
eq('EF generic M6 original tangent coefficient',f23central,x0*(1-s)/((1-s)*w-s),['P3K.109'])
eq('EF complete generic M6 order-three coefficient',(x0/w)**6*f3prime**2*f23prime/(x0**2*f23central),8*((1-s)*w-s)/s**3,['P3K.109'])

G3one=tuple(v.subs(r,-S.Rational(3,4)) for v in G3)
muone=S.factor((3*G3one[0]**2-S.Rational(3,2)*G3one[0]+t)/(2*G3one[1]))
xx1,yy1,tt1=[S.factor(v.subs(s,1)) for v in (xx,yy,tt)]
tx1,ty1=[S.factor(v.subs(s,1)) for v in minusG]
def f3(X,Y,T,SS):
    U=Y-T-X/2;V=Y+T+X/2
    return SS*X*U/(SS*V-(SS+2*T)*X)
def tang3one(X,Y,T):
    return (Y-G3one[1].subs(t,T)-muone.subs(t,T)*(X-G3one[0].subs(t,T)))/(X-G6_s1[0].subs(t,T))
ratio3=S.cancel(f3(tx1,ty1,tt1,1)/f3(xx1,yy1,tt1,1)/h)
ratio23=S.cancel(tang3one(tx1,ty1,tt1)/tang3one(xx1,yy1,tt1)/h)
x01=w*w-w+1
eq('EF s=1 full f3 translated ratio',S.limit(ratio3,h,0),w**3/((w-1)*x01),['P3K.109'])
eq('EF s=1 full tangent translated ratio',S.limit(ratio23,h,0),-(w-1)**2/x01,['P3K.109'])
eq('EF s=1 order-three coefficient',(x01/w)**6*(w**3/((w-1)*x01))**2*(-(w-1)**2/x01)/(x01/2)**3,-8,['P3K.109'])

G3zero=tuple(v.subs(r,0) for v in G3)
G6zero=add(G3zero,G3zero,0,t)
muzero=S.factor((3*G3zero[0]**2+t)/(2*G3zero[1]))
eq('III tangent central slope',S.limit(muzero,t,0),S.Rational(1,6),['P3K.114'])
eq('III 6G central x',S.limit(G6zero[0],t,0),S.Rational(1,36),['P3K.114'])
eq('III 6G central y',S.limit(G6zero[1],t,0),-S.Rational(1,216),['P3K.114'])
eq('III 6G central additive coordinate',S.limit(-G6zero[0]/G6zero[1],t,0),6,['P3K.114'])
eq('III strict f3 coefficient',f3(p**-2,-p**-3,0,S.Rational(1,4)),p**-2,['P3K.114'])
eq('III strict tangent coefficient',(-p**-3-S.Rational(1,6)*p**-2)/(p**-2-S.Rational(1,36)),6/(p*(p-6)),['P3K.114'])
al=beta*beta-1
eq('III exceptional f3 coefficient',al*(beta-1-al/2)/(beta+1-al/2),(beta-1)**3/(beta-3),['P3K.114'])
eq('III exceptional tangent coefficient',(beta-3-S.Rational(1,6)*(al-8))/(-S.Rational(1,36)),6*(beta-3)**2,['P3K.114'])
eq('III exceptional f6 coefficient',((beta-1)**3/(beta-3))**2*6*(beta-3)**2,6*(beta-1)**6,['P3K.114'])
eq('III full M6 strict coefficient',(2/(p*(p-2)))**6*(6*(p-2)**6)/(6/(p**5*(p-6))),64*(p-6)/p,['P3K.114'])
eq('III full M6 exceptional coefficient',(2*(beta-1)**2)**6*(6/((beta-1)**5*(beta-7)))/(6*(beta-1)**6),64*(beta-1)/(beta-7),['P3K.114'])

# Intrinsic elliptic quotient invariant and the two actual root equations.
jfun=-256*(r*r-3*t)**3/(t*t*D)
eq('EB finite triple-zero denominator',D.subs(t,r*r/3),r*r*(3*r-1)**2/3,['P3K.113'])
eq('EB infinity leading coefficient',S.limit(jfun.subs(t,1/q)/q,q,0),256,['P3K.113'])
eq('III exact degree-one j map',jfun.subs(r,0),6912/(27*t+4),['P3K.114'])
X,Y=S.symbols('X Y')
eq('III exact quartic root equation',(y*y-x**3-t*x-t*t).subs({x:z*z*X,y:z**3*Y,t:z**4})/z**6,Y*Y-X**3-X-z*z,['P3K.114'])
eq('III root doubled-point coordinate',(2*z)/(1+8*z**4),-((S.Rational(1,4))/z**2)/((-z**4-S.Rational(1,8))/z**3),['P3K.114'])
eq('III root full f2 coefficient',f2(z*z*X,z**3*Y,z**4,S.Rational(1,4)),z*z*(z*Y-z*z-X/2)/(z*z*X-S.Rational(1,4)),['P3K.114'])

# Full q-dependent selected inversion, with arbitrary holomorphic units.
c0,c1,c2=S.symbols('c0 c1 c2');qq=c0*c1*c2
AF=S.Function('A');CF=S.Function('C')
AA=AF(qq);CC=CF(qq)
target=S.Matrix([AA*CC*c0,c2/CC,c1/AA])
eq('NE selected vertex preserves original q',S.prod(target),qq,['P3K.110','P3K.114'])
inverse=S.Matrix([target[0]/(AA*CC),AA*target[2],CC*target[1]])
for i in range(3):eq('NE complete selected inverse coordinate '+str(i),inverse[i],[c0,c1,c2][i],['P3K.110','P3K.114'])
eq('NE full-unit selected Jacobian determinant',target.jacobian([c0,c1,c2]).det(),-1,['P3K.110','P3K.114'])

# Arbitrary SL2 basis changes: prove the central cochain multiplication
# as a polynomial identity in matrix entries modulo det(A)=1.
aa,bb,cc,dd,a_line,b_step,cA,cB=S.symbols('aa bb cc dd a_line b_step cA cB')
vx,vy,ux,uy=S.symbols('vx vy ux uy')
MM=S.Matrix([[aa,bb],[cc,dd]]);JJ=S.Matrix([[0,-1],[1,0]])
vv=S.Matrix([vx,vy]);uu=S.Matrix([ux,uy]);NN=S.eye(2)
def mono(Q,V,C):
    Z=S.eye(4);Z[1:3,0]=b_step*V;Z[1:3,1:3]=Q;Z[3,1:3]=a_line*(V.T*JJ*Q);Z[3,0]=C
    return Z
product=mono(MM,vv,cA)*mono(NN,uu,cB)
expected=mono(MM,vv+MM*uu,cA+cB+a_line*b_step*(vv.T*JJ*MM*uu)[0])
for ii in range(4):
 for jj in range(4):
  diff=S.expand(product[ii,jj]-expected[ii,jj]);rem=S.reduced(diff,[aa*dd-bb*cc-1],aa,bb,cc,dd,vx,vy,ux,uy,a_line,b_step,cA,cB)[1]
  eq(f'EF full central-cochain matrix product ({ii},{jj})',rem,0,['P3K.109','P3K.113','P3K.114'])

payload=dict(created_at=datetime.now(timezone.utc).isoformat(),sympy_version=S.__version__,scope='Listed exact algebraic and integral substeps only; source geometric claims are reviewed separately',input='Printed EF/SEF/EB and III formulas; no producer program opened',all_pass=True,total_checks=len(checks),checks=checks)
out=P/'analysis/continuation_IV/endpoint_algebra.output.json';out.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'all_pass':True,'checks':len(checks),'output':str(out)},indent=2))
