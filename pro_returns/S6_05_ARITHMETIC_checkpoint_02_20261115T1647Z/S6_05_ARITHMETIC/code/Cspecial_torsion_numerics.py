#!/usr/bin/env python3
"""Independent analytic evaluation of the norm at every exact-order n root,
2<=n<=8, and comparison with division-polynomial formulas.
"""
import sys,json,itertools
from pathlib import Path
import sympy as s
import mpmath as mp
from Cspecial_division import t,psi,exactorder,D
mp.mp.dps=110

def cm(z):
    z=s.N(z,mp.mp.dps+10)
    return mp.mpc(str(s.re(z)),str(s.im(z)))

def eta(tau):
    q=mp.exp(2j*mp.pi*tau)
    return mp.exp(mp.pi*1j*tau/12)*mp.fprod(1-q**r for r in range(1,161))

def norm(v,tau):
    return mp.exp(-mp.pi*v.imag**2/tau.imag)*abs(mp.jtheta(1,mp.pi*v,mp.exp(mp.pi*1j*tau))/eta(tau))

def reduce(v,tau):
    for k in range(50):
        n=mp.nint(tau.real)
        tau-=n
        if abs(tau)<1-mp.mpf('1e-105'):
            v,tau=v/tau,-1/tau
        else:break
    else:raise ArithmeticError('reduction failed')
    a=mp.floor(v.imag/tau.imag)
    v-=a*tau
    v-=mp.floor(v.real)
    return v,tau

def periods_at_zero(tt):
    aa=-mp.mpf(3)/4*tt**3*(tt-1)
    bb=mp.mpf(1)/4*tt**4*(tt-1)**2
    scale=mp.sqrt(abs(aa))
    ee=mp.polyroots([1,0,aa/scale**2,bb/scale**3],maxsteps=1000,error=False)
    ee=[z*scale for z in ee]
    for e1,e2,e3 in itertools.permutations(ee):
        mm=(e2-e3)/(e1-e3)
        K=mp.ellipk(mm)
        tau=1j*mp.ellipk(1-mm)/K
        if tau.imag>0:
            v=mp.ellipf(mp.asin(mp.sqrt((e1-e3)/(-e3))),mm)/(2*K)
            return reduce(v,tau)
    raise ArithmeticError('no positive period basis')

def show(z,n=70): return mp.nstr(z,n)

def main():
    rows=[]
    print('working decimal digits:',mp.mp.dps)
    for n in range(2,9):
        f=exactorder(n)
        roots=s.nroots(f,n=115,maxsteps=1000) if f.degree()>0 else []
        print('\nexact order',n,'smooth roots',len(roots))
        for idx,root in enumerate(roots):
            tt=cm(root)
            v,tau=periods_at_zero(tt)
            nn=norm(v,tau)
            m=n-1
            pp=mp.mpc(str(s.re(s.N(psi(m).subs(t,root),120))),str(s.im(s.N(psi(m).subs(t,root),120))))
            delta=27*tt**8*(tt-1)**3
            rhs=abs(delta)/abs(pp)**(mp.mpf(12)/(m*m-1))
            err=abs(nn**12-rhs)
            aa=n*v.imag/tau.imag
            bb=n*v.real-aa*tau.real
            torsionerr=max(abs(aa-mp.nint(aa)),abs(bb-mp.nint(bb)))
            print('t =',show(tt))
            print('tau =',show(tau))
            print('v =',show(v))
            print('n*v lattice coordinates =',int(mp.nint(aa)),int(mp.nint(bb)))
            print('torsion error =',show(torsionerr,8))
            print('N =',show(nn))
            print('N^12 analytic =',show(nn**12))
            print('N^12 algebraic =',show(rhs))
            print('absolute discrepancy =',show(err,8))
            assert err<mp.mpf('1e-90')
            assert torsionerr<mp.mpf('1e-90')
            rows.append(dict(n=n,t=show(tt,105),tau=show(tau,105),v=show(v,105),N=show(nn,105),N12=show(nn**12,105),error=show(err,8),torsion_error=show(torsionerr,8)))
    print('\nSPECIAL POINTS')
    for name,tau,v,target in [('rho',mp.mpc(mp.mpf('0.5'),mp.sqrt(3)/2),(2-mp.mpc(mp.mpf('0.5'),mp.sqrt(3)/2))/3,mp.root(3,4)),('i',mp.j,(1-mp.j)/2,mp.sqrt(2))]:
        R=mp.jtheta(1,mp.pi*v,mp.exp(mp.pi*1j*tau))/eta(tau)
        beta=6j/mp.pi*mp.log(R/(2*mp.sqrt(3)))
        N=norm(v,tau)
        DD=6/mp.pi*mp.log(N/(2*mp.sqrt(3)))
        print(name,'R=',show(R))
        print(name,'arg R=',show(mp.arg(R)))
        print(name,'N=',show(N))
        print(name,'beta=',show(beta))
        print(name,'D=',show(DD))
        print(name,'error=',show(abs(N-target),8))
        assert abs(N-target)<mp.mpf('1e-100')
    Path(__file__).resolve().parent.parent.joinpath('records/Cspecial_torsion_numerics.json').write_text(json.dumps(rows,indent=2)+'\n')
    print('\nALL ASSERTIONS PASSED')

if __name__=="__main__":
    main()
