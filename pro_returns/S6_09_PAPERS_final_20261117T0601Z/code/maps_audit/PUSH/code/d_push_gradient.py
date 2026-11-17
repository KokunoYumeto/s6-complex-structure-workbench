"""Check the exact theta-heat derivative identity numerically by a separate
symmetric difference of the product expression. This is an implementation
cross-check, not a proof or a global critical-point certificate.
"""
import mpmath as m
m.mp.dps=80
pi=m.pi
seed=m.mpf('.5')-1j*m.log(5+2*m.sqrt(6))/(2*pi)
def wp(z,t):
 q=m.exp(2j*pi*t)
 f=pi*pi/m.sin(pi*z)**2-pi*pi/3
 d=-2*pi**3*m.cos(pi*z)/m.sin(pi*z)**3
 for n in range(1,70):
  k=q**n/(1-q**n)
  f+=8*pi*pi*n*k*(1-m.cos(2*pi*n*z))
  d+=16*pi**3*n*n*k*m.sin(2*pi*n*z)
 return f,d
def mu(t):
 return m.findroot(lambda z:wp(z,t)[0],(seed,seed+m.mpf('.01')),tol=m.mpf('1e-68'))
def normD(t):
 z=mu(t);q=m.exp(2j*pi*t);u=m.exp(2j*pi*z)
 prod=2*m.sin(pi*z)*m.exp(pi*1j*t/6)
 for n in range(1,80):prod*=(1-q**n*u)*(1-q**n/u)
 return 6/pi*(m.log(abs(prod))-m.log(2*m.sqrt(3)))-6*m.im(z)**2/m.im(t)
def formula(t):
 z=mu(t);q=m.exp(2j*pi*t)
 L=pi*m.jtheta(1,pi*z,m.exp(pi*1j*t),1)/m.jtheta(1,pi*z,m.exp(pi*1j*t))
 Z=L+2*pi*1j*m.im(z)/m.im(t)
 E4=1+240*sum(n**3*q**n/(1-q**n) for n in range(1,80))
 g2=4*pi**4*E4/3
 P=wp(z,t)[1]
 return 1j*Z*(3*Z*P-2*g2)/(4*pi*pi*P)
for tr,ti in [('0.2','1.2'),('0.45','0.95'),('0.3','2')]:
 t=m.mpc(tr,ti);eps=m.mpf('1e-12')
 f=formula(t)
 df=((normD(t+eps)-normD(t-eps))/(2*eps)-1j*(normD(t+1j*eps)-normD(t-1j*eps))/(2*eps))/2
 print('tau',m.nstr(t,10),'formula',m.nstr(f,35))
 print('symmetric difference',m.nstr(df,35),'difference',m.nstr(abs(f-df),8))
print('80-digit arithmetic; no rigorous truncation or difference error certificate claimed.')
