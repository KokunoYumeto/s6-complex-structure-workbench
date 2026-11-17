#!/usr/bin/env python3
import mpmath as mp
mp.mp.dps=90
from Cspecial_torsion_numerics import eta,norm
mp.mp.dps=90

def E(k,tau):
    q=mp.exp(2*mp.pi*1j*tau)
    c={2:-24,4:240,6:-504}[k]
    return 1+c*sum(n**(k-1)*q**n/(1-q**n) for n in range(1,150))
def g2(tau):return 4*mp.pi**4/3*E(4,tau)
def g3(tau):return 8*mp.pi**6/27*E(6,tau)
def ellL(v,tau):
    q=mp.exp(mp.pi*1j*tau)
    return mp.pi*mp.jtheta(1,mp.pi*v,q,1)/mp.jtheta(1,mp.pi*v,q)
def wp(v,tau):
    q=mp.exp(mp.pi*1j*tau)
    zz=mp.pi*v
    a=mp.jtheta(1,zz,q);b=mp.pi*mp.jtheta(1,zz,q,1);c=mp.pi**2*mp.jtheta(1,zz,q,2)
    return (b/a)**2-c/a-mp.pi**2*E(2,tau)/3
rho=(1+mp.sqrt(3)*1j)/2
mu=(2-rho)/3
p=mp.diff(lambda v:wp(v,rho),mu)
print('P0=',mp.nstr(p,65))
print('P0^2 + g3=',mp.nstr(p*p+g3(rho),8))
print('rho mu prime claimed=',-mp.mpf(1)/3)
print('rho mu second claimed=',mp.nstr(3*p/(8*mp.pi**2),65))
for e in ['0.001','0.0001','0.00001']:
 d=mp.mpf(e)
 for direction in [1,1j,mp.exp(1j*mp.pi/6)]:
  delta=d*direction
  tau=rho+delta
  v=mp.findroot(lambda v:wp(v,tau),mu-delta/3)
  coeff=(v-mu+delta/3)/delta**2
  LC=(mp.log(norm(v,tau))-mp.log(norm(mu,rho)))/d**3
  pred=mp.re(7j*p*p*direction**3/(192*mp.pi**3))
  tt=g2(tau)**3/(g2(tau)**3-27*g3(tau)**2)
  print(e,mp.nstr(direction,8),'mu second/2',mp.nstr(coeff,25),'L cubic',mp.nstr(LC,25),'pred',mp.nstr(pred,25),'t',mp.nstr(tt,15))

G=g2(1j)
A=-3*mp.pi*1j/2;B=-9*mp.pi**2*1j/8
for hh in [mp.mpf('0.001'),mp.mpf('0.0001'),mp.mpc('0.0001','0.0002')]:
 tau=mp.findroot(lambda tau:wp((1-tau)/2+hh,tau),1j+A*hh*hh)
 L=mp.log(norm((1-tau)/2+hh,tau))
 quartic=3*mp.pi**2/8*abs(hh)**4-3*mp.pi**2/4*abs(hh)**2*mp.re(hh*hh)-5*G/192*mp.re(hh**4)
 print('i h',hh,'tau-B quotient',mp.nstr((tau-1j-A*hh*hh)/hh**4,30),'expected',mp.nstr(B,30))
 print('L quartic ratio',mp.nstr((L-mp.log(2)/2+mp.pi/2*abs(hh)**2)/quartic,30))
