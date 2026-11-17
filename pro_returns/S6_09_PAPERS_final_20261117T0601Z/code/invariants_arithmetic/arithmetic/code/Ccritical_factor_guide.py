"""High-precision coefficient guide, explicitly not an error-certified proof."""
import mpmath as m
from pathlib import Path
m.mp.dps=120
N=120
conv=lambda a,b,n:sum(a[j]*b[n-j] for j in range(n+1))
a=[m.mpf(0)]*(N+1);b=a.copy();c=a.copy();b[0]=1
for n in range(N):
 a[n+1]=(b[n]-conv(a,a,n))/(3*(n+1))
 b[n+1]=m.mpf(4)/3*(c[n]-conv(a,b,n))/(n+1)
 c[n+1]=2*(conv(b,b,n)-conv(a,c,n))/(n+1)
M=N//2-1
B=[b[2*j] for j in range(M+1)];J=[c[2*j+1]/2 for j in range(M+1)]
def mul(a,b):return [conv(a,b,n) for n in range(M+1)]
def power(a,p):
 v=[a[0]**p]+[m.mpf(0)]*M
 for n in range(1,M+1):v[n]=sum(((p+1)*k-n)*a[k]*v[n-k] for k in range(1,n+1))/(n*a[0])
 return v
J2=mul(J,J);B3=mul(mul(B,B),B)
D=mul([B3[n]-(4*J2[n-1] if n else 0) for n in range(M+1)],power(J,m.mpf(-3)/2))
H=[-D[n]/(16*n*n-1) for n in range(M+1)]
Q=power(J,m.mpf('.5'));S=mul(Q,H);TT=mul(Q,[(1+4*n)*H[n] for n in range(M+1)])
r0=2-m.sqrt(3);k=m.pi**2*m.jtheta(3,0,m.exp(-m.pi))**8*m.mpf(3)/4;z0=k*r0*r0;cc=1-1/m.sqrt(3)
C=[B[0]]+[m.mpf(0)]*M;A=[TT[0]-cc*S[0]]+[m.mpf(0)]*M
for n in range(1,M+1):
 C[n]=B[n]-C[n-1]/z0
 A[n]=TT[n]-cc*S[n]-A[n-1]/z0
invC=power(C,-1)
AC=mul(A,invC);SC=mul(S,invC);QC=mul(Q,invC)
print('r0,k,z0',m.nstr(r0,80),m.nstr(k,80),m.nstr(z0,80))
for name,V in [('C',C),('A/C',AC),('S/C',SC),('sqrtJ/C',QC),('H',H)]:
 print(name)
 for n in range(15):print(n,m.nstr(V[n],25))
 print('absnorm at z0',m.nstr(sum(abs(V[n])*z0**n for n in range(M+1)),50))
 print('tail10 at z0',m.nstr(sum(abs(V[n])*z0**n for n in range(10,M+1)),30))
print('radius bounds, A norm, dS norm, conjugate norm, sum')
for r in ['.001','.01','.05','.1','.15','.2','.25',m.nstr(r0,115)]:
 r=m.mpf(r);z=k*r*r
 an=sum(abs(AC[n])*z**n for n in range(M+1))
 sn=sum(abs(SC[n])*z**n for n in range(M+1))
 qn=sum(abs(QC[n])*z**n for n in range(M+1))
 hn=sum(n*abs(H[n])*z**(n-1) for n in range(1,M+1))
 ds=2*r0*r0/((1+r0)*(1+r)*(r0+r))*sn
 # |Im z|/|1+z/z0| <= |z| /sqrt(1-(|z|/z0)^2) if r<r0, but use uniform z0
 hh=4*r/(1-r*r)*qn*hn*min(z0,z/m.sqrt(1-(z/z0)**2)) if r<r0 else 4*r/(1-r*r)*qn*hn*z0
 print(*[m.nstr(x,18) for x in [r,an,ds,hh,an+ds+hh]])
peval=lambda V,z:sum(V[n]*z**n for n in range(len(V)))
print('rho cancellation',m.nstr(peval(TT,-z0)-cc*peval(S,-z0),60))
print('rho radial F',m.nstr(peval(AC,-z0)+m.mpf(1)/6*peval(SC,-z0),60))
print('rho angular F',m.nstr(peval(AC,-z0)+4*r0/(1-r0*r0)*z0*peval(QC,-z0)*peval([n*H[n] for n in range(1,M+1)],-z0),60))
print('Improved orthogonal bound')
for r in ['.001','.01','.05','.1','.15','.2','.25',m.nstr(r0,115)]:
 r=m.mpf(r);z=k*r*r
 an=sum(abs(AC[n])*z**n for n in range(M+1));qn=sum(abs(QC[n])*z**n for n in range(M+1))
 hn=sum(abs(H[n])*z**n for n in range(M+1));hp=sum(n*abs(H[n])*z**(n-1) for n in range(1,M+1))
 ee=2*r0*r0/((1+r0)*(1+r)*(r0+r));qq=2*r/(1-r*r);dd=2*(r0-r)/((1+r0)*(1+r))
 bound=an+qn*m.sqrt(ee**2*hn**2+4*qq*(dd+qq)*z*z*hp*hp)
 print(m.nstr(r,18),m.nstr(bound,25))
print('constant candidates:',m.nstr((sum(abs(AC[n])*z0**n for n in range(M+1))-1/m.sqrt(3))/z0,20),m.nstr((sum(abs(QC[n])*z0**n for n in range(M+1))-1)/z0,20),m.nstr((sum(abs(H[n])*z0**n for n in range(M+1))-1)/z0,20),m.nstr(sum(n*abs(H[n])*z0**(n-1) for n in range(1,M+1)),20))
