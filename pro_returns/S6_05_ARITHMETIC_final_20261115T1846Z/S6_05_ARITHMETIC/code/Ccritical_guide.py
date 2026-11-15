"""Exploratory computations only: zeros of the two critical factors.

These samples and root searches are not a proof by enumeration.  Their role
is to suggest explicit analytic inequalities to prove subsequently.
"""
import cmath
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import root

pi=math.pi
beta=math.log(5+2*math.sqrt(6))/(2*pi)

def data(tau):
    if tau.imag < .3 or abs(tau.real)>3: raise ArithmeticError('outside guide domain')
    q=cmath.exp(2j*pi*tau)
    N=max(18,int(40/tau.imag))
    coeff=[q**n/(1-q**n) for n in range(1,N+1)]
    E2=1-24*sum((n+1)*v for n,v in enumerate(coeff))
    E4=1+240*sum((n+1)**3*v for n,v in enumerate(coeff))
    E6=1-504*sum((n+1)**5*v for n,v in enumerate(coeff))
    def wp(z):
        w=pi*z; ss=cmath.sin(w);cs=cmath.cos(w)
        f=pi*pi/ss**2-pi*pi*E2/3
        p=-2*pi**3*cs/ss**3
        for n,v in enumerate(coeff,1):
            f-=8*pi*pi*n*v*cmath.cos(2*pi*n*z)
            p+=16*pi**3*n*n*v*cmath.sin(2*pi*n*z)
        return f,p
    z=.5-1j*beta
    for k in range(65):
        f,p=wp(z)
        if abs(f)<2e-13:break
        step=f/p
        if abs(step)>.15:step*=.15/abs(step)
        z-=step
    if abs(wp(z)[0])>2e-9:raise ArithmeticError('wp residual')
    W=pi/cmath.tan(pi*z)+2j*pi*z.imag/tau.imag
    for n,v in enumerate(coeff,1):W+=4*pi*v*cmath.sin(2*pi*n*z)
    g2=4*pi**4*E4/3
    p=wp(z)[1]
    B=3*W*p-2*g2
    t=E4**3/(E4**3-E6**2)
    Ltau=1j*W*B/(24*pi*p)
    tprime=-2j*pi*t*E6/E4
    Lt=Ltau/tprime
    return dict(tau=tau,z=z,W=W,B=B,t=t,Lt=Lt,Ltau=Ltau,g2=g2,p=p)

def target(x,which):
    try:
        d=data(complex(*x));v=d[which]
        if which=='B':v/=pi**4
        return [v.real,v.imag]
    except (ArithmeticError,OverflowError,ValueError,ZeroDivisionError):return [1e3+x[0],1e3+x[1]]

def serial(d):return {k:[v.real,v.imag] for k,v in d.items()}

def main():
    rows=[]
    for x in [0,.05,.1,.2,.3,.4,.5]:
        bottom=math.sqrt(1-x*x)
        for extra in [.0001,.01,.05,.15,.4,1,2,4]:
            tau=complex(x,bottom+extra)
            d=data(tau);rows.append(serial(d))
            print('tau',tau,'t',d['t'],'W',d['W'],'B',d['B'],'Lt*(t-1)',d['Lt']*(d['t']-1))
    roots=[]
    for which in ['W','B']:
        for x in np.linspace(0,.5,6):
            for y in [math.sqrt(1-x*x)+.01,1.1,1.4,2.0,3.0]:
                sol=root(lambda v:target(v,which),[x,y],tol=2e-10)
                if np.linalg.norm(sol.fun)<1e-6:
                    tau=complex(*sol.x)
                    if all(abs(tau-z[1])>1e-5 or z[0]!=which for z in roots):
                        roots.append((which,tau,float(np.linalg.norm(sol.fun))))
                        print('ROOT',which,tau,'residual',np.linalg.norm(sol.fun))
    print('ALL_ROOTS',roots)
    p=Path(__file__).resolve().parents[1]/'records/Ccritical_guide.json'
    p.write_text(json.dumps(dict(samples=rows,roots=[(w,[z.real,z.imag],e) for w,z,e in roots]),indent=2)+'\n')

if __name__=='__main__':main()
