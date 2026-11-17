"""Finite scalar checks for a global analytic inequality (no parameter grid).

All modular ODE coefficients are exact FLINT rationals.  Real ball arithmetic
only encloses constants and finite scalar sums; all analytic tails are given
explicitly below.  The accompanying proof does not use root searches.
"""
from flint import arb, fmpq, ctx
from pathlib import Path
import json
ctx.prec=512
ROOT=Path(__file__).resolve().parents[1]
M=100;N=2*M+2
zero=fmpq(0)
def conv(a,b,n):return sum((a[j]*b[n-j] for j in range(n+1)),zero)
a=[zero]*(N+1);b=a.copy();c=a.copy();b[0]=fmpq(1)
for n in range(N):
 a[n+1]=(b[n]-conv(a,a,n))/(3*(n+1))
 b[n+1]=fmpq(4,3)*(c[n]-conv(a,b,n))/(n+1)
 c[n+1]=2*(conv(b,b,n)-conv(a,c,n))/(n+1)
B=[b[2*j] for j in range(M+1)];J=[c[2*j+1]/2 for j in range(M+1)]
def mul(a,b):return [conv(a,b,n) for n in range(M+1)]
def power(a,p):
 v=[a[0]**int(p) if p.denominator==1 else fmpq(1)]+[zero]*M
 assert a[0]==1
 for n in range(1,M+1):v[n]=sum((((p+1)*j-n)*a[j]*v[n-j] for j in range(1,n+1)),zero)/(n*a[0])
 return v
J2=mul(J,J);B3=mul(mul(B,B),B)
D=mul([B3[n]-(4*J2[n-1] if n else 0) for n in range(M+1)],power(J,fmpq(-3,2)))
H=[-D[n]/(16*n*n-1) for n in range(M+1)]
Q=power(J,fmpq(1,2));S=mul(Q,H);TT=mul(Q,[(1+4*n)*H[n] for n in range(M+1)])
pi=arb.pi();sq=arb(3).sqrt();r0=2-sq
qi=(-2*pi).exp()
# E4(i) Lambert series: first 49 terms; n^3<=4^n gives a very loose rigorous tail.
A=1+240*sum((n**3*qi**n/(1-qi**n) for n in range(1,50)),arb(0))
Atail=240*(4*qi)**50/((1-4*qi)*(1-qi))
A+=arb(0,Atail.upper())
k=pi*pi*A;z0=k*r0*r0;cc=1-1/sq
print('k=',k.str(90));print('z0=',z0.str(90));print('r0=',r0.str(90))
assert k>14 and k<arb(72)/5
assert z0>arb('1.03156190435581564935682633431773565273882539802035')
assert z0<arb('1.03156190435581564935682633431773565273882539802036')
C=[arb(B[0])]+[arb(0)]*M;AA=[arb(TT[0])-cc*arb(S[0])]+[arb(0)]*M
for n in range(1,M+1):
 C[n]=arb(B[n])-C[n-1]/z0
 AA[n]=arb(TT[n])-cc*arb(S[n])-AA[n-1]/z0
ic=[arb(1)]+[arb(0)]*M
for n in range(1,M+1):ic[n]=-sum((C[j]*ic[n-j] for j in range(1,n+1)),arb(0))
def amul(a,b):return [sum((a[j]*b[n-j] for j in range(n+1)),arb(0)) for n in range(M+1)]
AC=amul(AA,ic);QC=amul([arb(v) for v in Q],ic)
# Coarse outer-circle Lambert bounds at R=12/5 in the z-plane.
r=fmpq(1,13)
e4=1+240*r*(1+4*r+r*r)/(1-r)**5
e6=1+504*r*(1+26*r+66*r*r+26*r**3+r**4)/(1-r)**7
bouter=e4/(fmpq(7,12)**4)
jouter=e6/(fmpq(7,12)**6)/3 # 2 sqrt(12/5)>3, A>1.
print('B outer bound <',float(bouter),'J outer bound <',float(jouter))
assert bouter<400 and jouter<3000
Ro=arb(12)/5;R=arb(3)/2;K=60
ratio=R/Ro
btail=400*ratio**K/(1-ratio)
jtail=3000*ratio**K/(1-ratio)
ctail=400*z0/(Ro-z0)*ratio**K/(1-ratio)
bnorm=sum((abs(arb(B[n]))*R**n for n in range(K)),arb(0))+btail
jnorm=sum((abs(arb(J[n]))*R**n for n in range(K)),arb(0))+jtail
cnorm=sum((abs(C[n])*R**n for n in range(1,K)),arb(0))+ctail
# min Re(1+j1*z+j2*z^2) on |z|=R is 1-j2*R^2-j1^2/(8*j2).
jlower=1-arb(J[2])*R*R-arb(J[1])**2/(8*arb(J[2]))-sum((abs(arb(J[n]))*R**n for n in range(3,K)),arb(0))-jtail
print('on |z|<=3/2: |B|<=',bnorm.str(35),'|J|<=',jnorm.str(35),'|C-1|<=',cnorm.str(35),'Re J>=',jlower.str(35))
assert bnorm<arb(33)/10 and jnorm<arb(5)/2 and cnorm<arb(2)/5 and jlower>arb(1)/5
# D=(B^3-4zJ^2)/J^(3/2) is bounded by 1000 on |z|<=3/2.
dbound=((arb(33)/10)**3+6*(arb(5)/2)**2)/(arb(1)/5)**arb('1.5')
print('D bound',dbound.str(35));assert dbound<1000
# H is bounded by 110 there; H+4zH' is bounded by 910 on |z|<=7/5.
hbound=1+1000*(arb(1)/2-pi/8)
ubound=1+arb(1000)/3*arb(15).log()
print('H bound',hbound.str(35),'U bound',ubound.str(35))
assert hbound<110 and ubound<910
# Therefore |A/C|<10000 and |sqrt(J)/C|<3 on |z|=7/5.
Ri=arb(7)/5
acbound=arb(5).sqrt()/arb(2).sqrt()*(910+cc*110)/((Ri/z0-1)*(arb(3)/5))
qcbound=(arb(5)/2).sqrt()/(arb(3)/5)
print('AC bound',acbound.str(35),'QC bound',qcbound.str(35));assert acbound<10000 and qcbound<3
# Finite coefficient norms through degree 99, plus Cauchy tails from radius 7/5.
s=z0/Ri
actail=10000*s**M/(1-s)
qctail=3*s**M/(1-s)
htail=110*s**M/(1-s)
hptail=110/z0*s**M*(M/(1-s)+s/(1-s)**2)
acnorm=(sum((abs(AC[n])*z0**n for n in range(1,M)),arb(0))+actail)/z0
qcnorm=(sum((abs(QC[n])*z0**n for n in range(1,M)),arb(0))+qctail)/z0
hnorm=(sum((abs(arb(H[n]))*z0**n for n in range(1,M)),arb(0))+htail)/z0
hpnorm=sum((n*abs(arb(H[n]))*z0**(n-1) for n in range(1,M)),arb(0))+hptail
print('finite norm certificates:')
for name,v,limit in [('AC linear norm',acnorm,arb(13)/200),('QC linear norm',qcnorm,arb(7)/50),('H linear norm',hnorm,arb(113)/1000),('H derivative norm',hpnorm,arb(13)/100)]:
 print(name,v.str(60),' < ',limit.str(15));assert v<limit
print('Cauchy tails',*[v.str(20) for v in [actail,qctail,htail,hptail]])
# Explicit cusp estimates, T>=7/5.
r=arb(1)/2000;s=arb(10)/33
E6dev=504*r*(1+26*r+66*r*r+26*r**3+r**4)/(1-r)**7
Dabs=r*(24*r/(1-r)**2).exp()/(1-E6dev)**arb('1.5')
muerr=36*sq*arb(2).sqrt()/pi/1250*(s+s*s/(4*(1-s)))
muder=72*arb(6).sqrt()/1250*(-(1-s).log())
print('cusp Dcircle',Dabs.str(30),'muerror',muerr.str(30),'muderivative',muder.str(30))
assert Dabs<arb(1)/1250 and muerr<arb(1)/125 and muder<arb(13)/250
r=arb(1)/6600
e4dev=240*r*(1+4*r+r*r)/(1-r)**5
e6dev=504*r*(1+26*r+66*r*r+26*r**3+r**4)/(1-r)**7
beta=(5+2*arb(6).sqrt()).log()/(2*pi)
cuspF=arb(6).sqrt()*arb(1038)/963*((arb(365)/1000+arb(1)/125)/(arb(7)/5)+arb(13)/250)
print('cusp E4dev',e4dev.str(30),'E6dev',e6dev.str(30),'beta',beta.str(30),'Fbound',cuspF.str(30))
assert e4dev<arb(37)/1000 and e6dev<arb(77)/1000 and beta<arb(365)/1000 and cuspF<arb(17)/20
out={name:[str(v) for v in V] for name,V in [('B',B),('J',J),('D',D),('H',H)]}
out['constants']={name:v.str(120) for name,v in [('k',k),('z0',z0),('r0',r0)]}
out['norm_bounds']={name:v.str(90) for name,v in [('AC',acnorm),('QC',qcnorm),('H',hnorm),('Hprime',hpnorm)]}
(ROOT/'records/Ccritical_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL ASSERTIONS PASSED')
