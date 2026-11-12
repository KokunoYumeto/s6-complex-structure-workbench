"""Exact identities and independent quadratures for the full local spectrum.

These checks diagnose constants and finite coordinate maps. They are not a
numerical construction of the interacting continuum Yang--Mills spectrum.
"""
from pathlib import Path
from itertools import product
import json, math
import numpy as np
import sympy as s
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok,details=None):
    checks.append(dict(name=name,passed=bool(ok),details=details))
    if not ok: raise AssertionError(name)

# All signs in the 8 by 8 standing-wave / travelling-wave transform.
betas=list(product([0,1],repeat=3)); signs=list(product([-1,1],repeat=3))
U=s.Matrix([[s.I/s.sqrt(8)*s.I**sum(r*b for r,b in zip(rho,beta))
             for rho in signs] for beta in betas])
check('Exact parity transform U*U=I',s.simplify(U.conjugate().T*U)==s.eye(8))
check('Exact parity transform UU*=I',s.simplify(U*U.conjugate().T)==s.eye(8))
Kmat=s.Matrix(8,8,lambda i,j:s.Rational((i+1)*(j+2),13)+s.I*(i-j))
Tmat=(U*Kmat*U.T).applyfunc(s.expand)
norm=lambda M: s.expand(sum(s.expand(s.conjugate(v)*v) for v in M))
check('Two bilinear mode indices retain the Hilbert--Schmidt norm',
      s.simplify(norm(Kmat)-norm(Tmat))==0)

# Polarization bracket before angular integration: no sign or scalar dropped.
c=s.symbols('c', real=True)
ss=s.sqrt(1-c*c)
p=s.Matrix([0,0,1]);q=s.Matrix([ss,0,c])
ep=[s.Matrix([1,0,0]),s.Matrix([0,1,0])]
eq=[s.Matrix([c,0,-ss]),s.Matrix([0,1,0])]
pol=s.Matrix(2,2,lambda i,j:s.simplify(p.cross(ep[i]).dot(q.cross(eq[j]))+ep[i].dot(eq[j])))
check('Exact two-polarization bracket',pol==(1+c)*s.eye(2))
check('All polarization contractions',s.simplify(sum(x*x for x in pol)-2*(1+c)**2)==0)
check('Opposite momenta cancel electric and magnetic terms',pol.subs(c,-1)==s.zeros(2))
check('Parallel momenta retain both terms',pol.subs(c,1)==2*s.eye(2))

K,w,u=s.symbols('K w u',positive=True)
r=(w+u)/2;v=(w-u)/2
cos=(K*K-r*r-v*v)/(2*r*v)
check('Exact ellipsoid energy-angle identity',s.simplify(2*r*v*(1+cos)-(K*K-u*u))==0)
integ=s.simplify(s.pi/(4*K)*s.integrate((K*K-u*u)**2,(u,-K,K)))
check('Complete ellipsoid radial integral',integ==4*s.pi*K**4/15)
coef=s.Rational(3,4)/(2*s.pi)**6
check('Three-colour boson and Fourier density constant',s.simplify(coef*integ/K**4)==1/(320*s.pi**5))
check('Low-energy density constant for nonzero integral',s.simplify(4*s.pi/(320*s.pi**5*7))==1/(560*s.pi**4))
check('Raw norm large-time constant',s.factorial(7)/560==9)
check('Raw excitation large-time constant',s.factorial(8)/560==72)
check('Point-profile norm integral',s.simplify(4*s.pi*s.factorial(6)/(320*s.pi**5))==9/s.pi**4)
alpha,beta=s.symbols('alpha beta',real=True)
check('Velocity-to-curvature raw scaling exponent',s.expand((6-2*beta).subs(beta,2*alpha+2))==2-4*alpha)

# Original finite arrays and exact midpoint product coordinates, many parities.
maxerr=0.
for L in [2,3,5]:
    N=2*L+1; ns=np.arange(-L,L+1,dtype=float); ne=np.arange(-L,L,dtype=float)
    vv=np.array([np.sqrt((2-(j==0))/N)*np.cos(np.pi*j*(ns+L+.5)/N) for j in range(N)])
    ww=np.array([-np.sqrt(2/N)*np.sin(np.pi*j*(ne+L+1)/N) for j in range(1,N)])
    sj=2*np.sin(np.pi*np.arange(1,N)/(2*N))
    err=max(np.max(np.abs(vv@vv.T-np.eye(N))),np.max(np.abs(ww@ww.T-np.eye(N-1))),
            np.max(np.abs(np.diff(vv[1:],axis=1)-sj[:,None]*ww)))
    check(f'Original open vertex/edge orthogonality and derivative L={L}',err<3e-14,float(err))
    for jj in product(range(1,min(N,5)),repeat=3):
        avec=.13;ell=avec*N;k=np.pi*np.array(jj)/ell
        sv=2*np.sin(np.pi*np.array(jj)/(2*N));eps=np.cross(sv,[0,0,1]);eps/=np.linalg.norm(eps)
        x=np.array([.17,-.21,.09]);bb=tuple(j%2 for j in jj);phase=(-1)**sum(j//2 for j in jj)
        lhs=np.array([np.sqrt(8)*eps[i]*(-np.sin(k[i]*x[i]+np.pi*jj[i]/2))*
                      math.prod(np.cos(k[d]*x[d]+np.pi*jj[d]/2) for d in range(3) if d!=i)
                      for i in range(3)])
        rhs=sum(phase*1j/np.sqrt(8)*np.exp(1j*np.pi*np.dot(rho,bb)/2)*
                (np.array(rho)*eps)*np.exp(1j*np.dot(np.array(rho)*k,x)) for rho in signs)
        maxerr=max(maxerr,float(np.max(np.abs(lhs-rhs))))
check('All original parity signs in component-plane-wave map',maxerr<2e-14,maxerr)

# Complete original open-box transverse basis, including zero coordinates.
L=2;N=2*L+1;a=.13
vertices=list(product(range(-L,L+1),repeat=3))
vid={n:i for i,n in enumerate(vertices)}
edges=[(n,i) for n in vertices for i in range(3) if n[i]<L]
eid={e:i for i,e in enumerate(edges)}
def shifted(n,i):
    out=list(n);out[i]+=1;return tuple(out)
faces=[(n,i,k) for n in vertices for i in range(3) for k in range(i+1,3) if n[i]<L and n[k]<L]
d0=np.zeros((len(edges),len(vertices)));d1=np.zeros((len(faces),len(edges)))
for e,(n,i) in enumerate(edges):d0[e,vid[n]]=-1;d0[e,vid[shifted(n,i)]]=1
for f,(n,i,k) in enumerate(faces):
    for e,sgn in [((n,i),1),((shifted(n,i),k),1),((shifted(n,k),i),-1),((n,k),-1)]:d1[f,eid[e]]=sgn
cols=[];frequencies=[]
for jj in product(range(N),repeat=3):
    active=[i for i in range(3) if jj[i]>0]
    if len(active)<2:continue
    sv=2*np.sin(np.pi*np.array(jj)/(2*N))
    _,_,vt=np.linalg.svd(sv[active].reshape(1,-1),full_matrices=True)
    for base in vt[1:]:
        eps=np.zeros(3);eps[active]=base
        vec=[]
        for n,i in edges:
            if i not in active:vec.append(0.);continue
            val=-math.sqrt(2/N)*math.sin(math.pi*jj[i]*(n[i]+L+1)/N)*eps[i]
            for d in range(3):
                if d!=i:val*=math.sqrt((2-(jj[d]==0))/N)*math.cos(math.pi*jj[d]*(n[d]+L+.5)/N)
            vec.append(val)
        cols.append(vec);frequencies.append(float(np.linalg.norm(sv)))
VV=np.array(cols).T;sig=np.array(frequencies);curl=d1@VV
check('Complete product-basis dimension equals original gauge-reduced dimension',
      VV.shape[1]==len(edges)-len(vertices)+1==4*L*L*(4*L+3))
check('All original face boundaries close',np.max(np.abs(d1@d0))==0)
check('Every original transverse mode is orthogonal to gradients',np.max(np.abs(d0.T@VV))<2e-14)
check('All transverse modes have the original counting metric',np.max(np.abs(VV.T@VV-np.eye(len(sig))))<2e-14)
check('Every original curl eigenvalue and boundary sign',np.max(np.abs(d1.T@curl-VV*sig**2))<3e-14)
ww=sig/a
constant_pair=(curl.T@curl)/(a*a*np.sqrt(ww[:,None]*ww[None,:]))-np.sqrt(ww[:,None]*ww[None,:])*(VV.T@VV)
check('Constant local energy has zero pair coefficient in every mode',np.max(np.abs(constant_pair))<2e-13)

# Independently integrate the original polar angle reduced only by delta energy.
for kval,omega in [(0.3,.8),(1.2,1.3),(2.1,5.),(3.,3.01)]:
    def angular_delta_integrand(rr):
        ss=omega-rr
        cc=(kval*kval-rr*rr-ss*ss)/(2*rr*ss)
        return 2*np.pi/kval*rr*rr*ss*ss*(1+cc)**2
    actual=quad(angular_delta_integrand,(omega-kval)/2,(omega+kval)/2,epsabs=1e-11,epsrel=1e-11)[0]
    expected=4*np.pi*kval**4/15
    check(f'Independent polar-delta integral K={kval}, omega={omega}',
          abs(actual-expected)<1e-10*max(1,abs(expected)),dict(actual=actual,expected=expected))

# A Gaussian test profile has hhat=exp(-b |k|^2/2), with integral one.
# It tests two different numerical integrations of the stated spectral law.
# It is used solely as a quadrature diagnostic, not as compact source data.
for time,bwidth in [(.7,.4),(2.,1.1),(10.,.3)]:
    inner=lambda om: quad(lambda kk:kk**6*np.exp(-bwidth*kk*kk),0,om,epsabs=2e-11)[0]/(80*np.pi**4)
    via_density=quad(lambda om:np.exp(-time*om)*inner(om),0,np.inf,epsabs=1e-11,epsrel=1e-9)[0]
    via_momentum=quad(lambda kk:kk**6*np.exp(-time*kk-bwidth*kk*kk),0,np.inf,
                      epsabs=1e-11,epsrel=1e-10)[0]/(80*np.pi**4*time)
    check(f'Independent spectral versus Fourier Laplace integration t={time}',
          abs(via_density-via_momentum)<2e-9*max(abs(via_momentum),1e-8),
          dict(spectral=via_density,fourier=via_momentum))

# Large-time asymptotics after exact change v=tK avoids underflow.
rows=[]
for time in [8,16,32,64]:
    I=quad(lambda vv:vv**6*np.exp(-vv-(vv/time)**2),0,np.inf,epsabs=1e-8)[0]
    I1=quad(lambda vv:vv**7*np.exp(-vv-(vv/time)**2),0,np.inf,epsabs=1e-8)[0]
    rows.append(dict(time=time,norm_constant_ratio=I/720,energy_quotient_times_time=1+I1/I))
check('Large-time raw coefficient approaches 9/pi^4',abs(rows[-1]['norm_constant_ratio']-1)<.02,rows)
check('Large-time unaltered energy quotient approaches 8/t',abs(rows[-1]['energy_quotient_times_time']-8)<.04)

out=dict(passed=all(x['passed'] for x in checks),groups=len(checks),checks=checks,
         scope='Exact algebra, finite original arrays, independent numerical quadratures; not an interacting continuum certification.')
(ROOT/'FULL_LOCAL_SPECTRUM_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=out['passed'],groups=out['groups'],parity_max_error=maxerr)))
