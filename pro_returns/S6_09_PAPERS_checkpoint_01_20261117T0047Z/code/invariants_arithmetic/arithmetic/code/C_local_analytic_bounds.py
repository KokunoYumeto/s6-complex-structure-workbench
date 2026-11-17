#!/usr/bin/env python3
"""Evaluate the explicit series majorants in the analytic proof.

No grid, interval cover, or root enumeration is used. The paper gives rational
majorants and geometric-tail arguments sufficient without this program.
"""
from mpmath import mp
mp.dps=70
p=mp.pi
T=mp.mpf(9)/10
AA=[sum(mp.mpf(n)**k*mp.exp(-p*T*n*n)*mp.cosh(p*n/2) for n in range(1,21)) for k in range(3)]
a0,a1,a2=2*AA[0],4*p*AA[1],8*p*p*AA[2]
r=mp.exp(-2*p*T)
E=p*p/3*(1+24*r/(1-r)**3)
print('a0,a1,a2',a0,a1,a2)
print('G_bound',a2/(1-a0)+a1*a1/(1-a0)**2+E)
print('H_bound',-mp.log(1-a0)+mp.mpf(11)*p/120+r/(1-r)**2)
T=mp.mpf(49)/50
th2=[2*p**k*sum((mp.mpf(n)+mp.mpf('.5'))**(2*k)*mp.exp(-p*T*(mp.mpf(n)+mp.mpf('.5'))**2) for n in range(20)) for k in range(3)]
th4=[(1 if k==0 else 0)+2*p**k*sum(mp.mpf(n)**(2*k)*mp.exp(-p*T*n*n) for n in range(1,20)) for k in range(3)]
print('theta2 derivative bounds',*th2)
print('theta4 derivative bounds',*th4)
ep=4*p*p/3*(th2[0]**3*th2[1]+th4[0]**3*th4[1])
epp=p*p/3*(12*th2[0]**2*th2[1]**2+4*th2[0]**3*th2[2]+12*th4[0]**2*th4[1]**2+4*th4[0]**3*th4[2])
r=mp.exp(-2*p*T)
g2p=640*p**5*r*(1+11*r+11*r*r+r**3)/(1-r)**7
Ep=16*p**3*r*(1+r)/(1-r)**5
E6pp=2016*p*p*r*(1+r)*(1+120*r+1191*r**2+2416*r**3+1191*r**4+120*r**5+r**6)/(1-r)**11
print('e2 prime, double prime',ep,epp)
print('g2 prime,E prime,E6 double prime',g2p,Ep,E6pp)
e=mp.mpf(7)/25
astep=mp.mpf(5)/2+3*e*e
amax=mp.mpf(95)/2+astep
Qerr=astep+e*amax/100+30*(mp.mpf(4)/25)**3/(1-mp.mpf(4)/25)*100
print('a2 error, a2 upper, Qerror',astep,amax,Qerr)
print('Rouche leading', (47-astep)/100,'remainder',e+e*amax/10000+30*(mp.mpf(4)/25)**3/(1-mp.mpf(4)/25))
print('delta/h2 bound', (mp.mpf(95)/2+Qerr)/(mp.mpf(99)/10-mp.mpf(3)/5))
print('L remainder coefficient rational',mp.mpf(147)/5+56+mp.mpf(21)/5+mp.mpf(2048)/63+mp.mpf(1100)/49)
print('j boundary lower',mp.mpf(121)/43200)
