#!/usr/bin/env python3
"""Fresh exact OS45 computations from K116/K117/K119 statements only.
No printed supporting proof argument has been opened at this stage.
"""
from pathlib import Path
import sympy as s,json,math
from fractions import Fraction as Q
OUT=Path(__file__).resolve().parents[1]/'output';checks=[]
def check(name,truth):
 assert truth,name
 checks.append(name)
u,t,a,x,y,z,S,v,u0=s.symbols('u t a x y z S v u0')
R=t*t+a;f=R**2+t;g=R**3+s.Rational(3,2)*t*R+s.Rational(3,8)
D=s.expand(64*(f**3-g**2));aa=-u/3-u**4/9;tc=1/(2*u)-u*u/3;xi=1/(4*u*u)+u/3
check('literal section G',s.expand((R**3-3*f*R+2*g)-s.Rational(3,4))==0)
check('quartic discriminant',s.expand(D+48*a*(t*t+a)**2+8*t**3+72*a*t+9)==0)
check('selected f=xi2',s.cancel(f.subs({a:aa,t:tc})-xi**2)==0)
check('selected g=xi3',s.cancel(g.subs({a:aa,t:tc})-xi**3)==0)
check('nodal normalization',s.expand((S*(S*S-3*xi))**2-(S*S-2*xi)**3+3*xi**2*(S*S-2*xi)-2*xi**3)==0)
check('node branches c2=3xi',s.cancel((4*u**3+3)/(4*u*u)-3*xi)==0)
SG=-s.sqrt(3)/(2*u);c=v/(2*u)
check('literal section torus coordinate',s.cancel((SG-c)/(SG+c)-(s.sqrt(3)+v)/(s.sqrt(3)-v))==0)
Z=(S-c)/(S+c)
check('normalization inverse S',s.cancel(c*(1+Z)/(1-Z)-S)==0)
Dsel=s.factor(s.diff(D,t).subs({a:aa,t:tc}));kap=s.factor(Dsel/(64*1728*xi**6))
check('selected discriminant derivative',Dsel==2*(4*u**3+3)**3/(27*u*u))
check('original-height Tate leading unit',kap==2*u**10/(4*u**3+3)**3)
check('whole quartic collision discriminant',s.factor(s.discriminant(D,t)-331776*(256*a**3-3)**3)==0)
residual=s.cancel(D.subs(a,aa)/(t-tc));un=16*u**6+120*u**3+243
check('unselected cubic collision discriminant',s.factor(s.discriminant(residual,t))==-1024*u**4*un**3/6561)
check('type II resultant',s.cancel(s.resultant(f,g,t)-(256*a**3-3)/4096)==0)
check('source type II factorization',s.factor((256*aa**3-3)+(4*u**3+3)**2*un/729)==0)
check('source a derivative',s.diff(aa,u)==-(4*u**3+3)/9)
check('type II t=minus16a2 f',s.rem(s.together(f.subs(t,-16*a*a)).as_numer_denom()[0],256*a**3-3,a)==0)
check('type II t=minus16a2 g',s.rem(s.together(g.subs(t,-16*a*a)).as_numer_denom()[0],256*a**3-3,a)==0)
check('type II f derivative',s.rem(s.diff(f,t).subs(t,-16*a*a)+2,256*a**3-3,a)==0)
check('type II g derivative',s.rem(s.diff(g,t).subs(t,-16*a*a)+3*a,256*a**3-3,a)==0)
check('selected-unselected separation formula',s.cancel(tc+16*aa*aa-(2*u**3+9)*(4*u**3+3)**2/(162*u))==0)
check('unselected II polynomial squarefree degree6',s.degree(un,u)==6 and s.gcd(un,s.diff(un,u))==1)
cap=2187-16*u**3*(u**3+3)**3
check('cap factorization',s.expand(cap+(2*u**3-3)*(8*u**9+84*u**6+342*u**3+729))==0)
check('cap pullback',s.expand((16*aa**3+3)*729-cap)==0)
check('cap polynomial squarefree degree12',s.degree(cap,u)==12 and s.gcd(cap,s.diff(cap,u))==1)
for left,right,name in [(un,u,'unselectedII/u0'),(un,u**3+3,'unselectedII/a0'),(un,4*u**3+3,'unselectedII/selectedII'),(un,cap,'unselectedII/cap'),(cap,u,'cap/u0'),(cap,u**3+3,'cap/a0'),(cap,4*u**3+3,'cap/selectedII')]:check('disjoint '+name,s.gcd(left,right)==1)
check('selected cap tc zero numerator',s.cancel(tc+(2*u**3-3)/(6*u))==0)
check('eight finite a0 source points',s.degree(u*(u**3+3),u)==4 and s.gcd(u*(u**3+3),4*u**3+3)==1)
check('48 puncture count',8+1+3+12+24==48)
# Fourfold positive winding at selected type II: exact local units.
a0=-u0/3-u0**4/9
numer=s.cancel((aa-a0)+(u-u0)**2*(u*u+2*u*u0+3*u0*u0)/9)
check('a difference after u0 cubic',s.rem(s.together(numer).as_numer_denom()[0],4*u0**3+3,u0)==0)
check('v square exact local factor',s.expand(4*(u-u0)*(u*u+u*u0+u0*u0)-4*u**3+4*u0**3)==0)
unit=-(u*u+2*u*u0+3*u0*u0)/(144*(u*u+u*u0+u0*u0)**2)
check('four-turn nonzero leading unit',s.simplify(unit.subs(u,u0)+1/(216*u0*u0))==0)
check('kappa winding numerator nonzero at selected II',s.gcd(2*u**10,4*u**3+3)==1)
# Ordinary-cap local smoothing and Tate coefficient.
check('cap discriminant at t0',D.subs(t,0)==-3*(16*a**3+3))
check('node motion derivative',s.simplify(-s.diff(D,a).subs(t,0)/s.diff(D,t).subs(t,0)+2*a)==0)
check('cap reference nodal cubic',s.rem(s.expand((x+a)**2*(x-2*a)-(x**3-3*f.subs(t,0)*x+2*g.subs(t,0))),16*a**3+3,a)==0)
capkap=s.diff(D,t).subs(t,0)/(64*1728*f.subs(t,0)**3)
check('cap kappa exact value',s.rem(s.together(capkap-1/(288*a*a)).as_numer_denom()[0],16*a**3+3,a)==0)
check('cap node h value',s.simplify(2*s.diff(g,t).subs(t,0)-3*(-a)*s.diff(f,t).subs(t,0)-6*a)==0)
rr=s.sqrt(3)
for sig in [1,-1]:
 pg=(sig/rr-1)/(sig/rr+1)
 check('cap PG branch '+str(sig),s.simplify(pg-(-2+sig*rr))==0)
# Exact symbolic prism solve for all nonzero weights.
w0,w1,w2,I0,I1,I2,J0,J1,J2,C,E=s.symbols('w0 w1 w2 I0 I1 I2 J0 J1 J2 C E',nonzero=True)
ws=[w0,w1,w2];Is=[I0,I1,I2];Js=[J0,J1,J2]
V=s.Matrix(3,3,lambda i,j:(Is[i]/ws[i]if i==j else 0)+C/(ws[i]*ws[j]));delta=s.Matrix([(Js[i]+E)/ws[i]for i in range(3)])
for i in [1,2]:
 ei=s.eye(3)[:,i];e0=s.eye(3)[:,0]
 check('symbolic full symmetric prism '+str(i),all(s.cancel(v)==0 for v in V*(ws[i]*ei-w0*e0)-(Is[i]*ei-I0*e0)))
 check('symbolic full tangent prism '+str(i),s.cancel(ws[i]*delta[i]-w0*delta[0]-Js[i]+J0)==0)
# Bounded integral fan algorithm: exact Fraction, both signed seed ranges.
def mm(A,B):return [[sum(A[i][k]*B[k][j]for k in range(2))for j in range(2)]for i in range(2)]
Q0=[[1,-1],[0,1]];Q1=[[1,0],[-1,1]];Q0i=[[1,1],[0,1]];Q1i=[[1,0],[1,1]]
def data(P):
 p,b=P[0];q,ss=P[1];check_det=p*ss-b*q;assert check_det==1
 Ri=[[ss,-b],[-q,p]];B=[[-6*Ri[i][0]*P[0][j]for j in range(2)]for i in range(2)]
 xx,yy=Ri[0][1],Ri[1][1];w=[xx,yy,-xx-yy];d=[-xx-2*yy,-2*xx-yy,xx-yy];ell=[B[1][1]-B[1][0],B[0][0]-B[0][1],B[1][1]]
 ii=[-3*w[i]+d[i]*(ell[i]+3)for i in range(3)];jj=[-3*w[i]-d[i]*(ell[i]+3)for i in range(3)]
 return w,ii,jj
runs=steps=0
for p in range(1,16):
 for r in range(1,16):
  if math.gcd(p,r)!=1:continue
  for shift in range(-3,4):
   q0=0 if p==1 else pow(r,-1,p);q=q0+p*shift;ss=(1-r*q)//p;P=[[p,-r],[q,ss]];cur=P;word=[]
   while cur[0][1]!=0:
    pp,rr=cur[0][0],-cur[0][1];edge=0 if rr>=pp else 1
    nxt=mm(cur,Q0i if edge==0 else Q1i);assert nxt[0][0]-nxt[0][1]<pp+rr
    word.append(edge);cur=nxt
   assert cur[0][0]==1 and cur[1][1]==1
   j=cur[1][0];h=18*j*(j-1)
   VV=[[Q(h),Q(6-12*j),Q(12*j-6)],[Q(6-12*j),Q(0),Q(0)],[Q(12*j-6),Q(0),Q(0)]]
   dd=[Q(-12-h),Q(12*j-12),Q(-12*j)];sscore=Q(-1-3*j*(j-1))
   for edge in reversed(word):
    va,db=VV[edge][edge],dd[edge];sscore+=(db-va)/2;cur=mm(cur,Q0 if edge==0 else Q1);ww,ii,jj=data(cur)
    assert all(ww)
    cc=ww[2]**2*va-ww[2]*ii[2];ee=ww[2]*(2*va-db)-jj[2]
    VV=[[Q(ii[i],ww[i])*(i==k)+Q(cc,ww[i]*ww[k])for k in range(3)]for i in range(3)]
    dd=[Q(jj[i]+ee,ww[i])for i in range(3)]
    assert VV[2][2]==va and dd[2]==2*va-db
    assert all(v.denominator==1 for row in VV for v in row)and all(v.denominator==1 for v in dd)and sscore.denominator==1
    for i in [1,2]:
     assert all(ww[i]*VV[k][i]-ww[0]*VV[k][0]==(ii[i]if k==i else 0)-(ii[0]if k==0 else 0)for k in range(3))
     assert ww[i]*dd[i]-ww[0]*dd[0]==jj[i]-jj[0]
    steps+=1
   assert cur==P;runs+=1
check('bounded signed-seed positive fan exact integral recurrence',runs>0 and steps>0)
payload={'checker':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same model family','phase':'statement-only prereading; no K116/K117/K119 printed proof argument opened','check_count':len(checks),'checks':checks,'bounded_fan_cases':runs,'bounded_fan_steps':steps,'exact_formulas':{'D64':str(D),'selected_Dprime':str(Dsel),'kappa_at_selected_node':str(kap),'residual_cubic_discriminant':str(s.factor(s.discriminant(residual,t))),'selected_typeII_local_unit':str(unit)},'scope_limit':'source algebra, branch maps, collision counts/disjointness, original-height leading winding, local node chart algebra, exact prism formula and bounded fan recurrence. Full Cartier/cap gluing, topology, all-fan physical sign and original endpoint comparison remain for proof review.'}
(OUT/'prereading_exact.json').write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps(payload,indent=2))
