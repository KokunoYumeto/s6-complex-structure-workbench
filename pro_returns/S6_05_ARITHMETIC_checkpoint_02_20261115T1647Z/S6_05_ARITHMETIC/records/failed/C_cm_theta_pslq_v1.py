#!/usr/bin/env python3
"""Independent 250-digit theta norms and 200-digit PSLQ at all 11 rational CM moduli.

Numerical checks do not establish transcendence or algebraicity. Known rational
relations among the two real period components are removed before PSLQ.
"""
from pathlib import Path
import json
import mpmath as m

root=Path(__file__).resolve().parents[1]
m.mp.dps=270
ds=[2,3,4,7,7,11,19,27,43,67,163]
bad=[[2,3,7],[2,3,11],[2,7],[2,3,7,19],[2,7],[3,7,11],[19],[3,11,23],[3,7,43],[7,31,67],[7,11,19,127,163]]
finite=[[(2,'1/2'),(3,'1/2')],[(2,'2/3'),(3,'1/4')],[(2,'3/4')],[(2,'1')],[(2,'1')],[(3,'1/2')],[],[(3,'5/12')],[],[],[]]
data=[]
for line in (root/'code/C_cm_250.out').read_text().splitlines():
    if '|' in line:
        j,h,w1,w2=line.split('|')
        data.append((int(j),m.mpf(h),m.mpf(w1),m.mpf(w2)))
assert len(data)==11
rows=[]
print('Theta and height precision: 270 decimal digits. PSLQ: 200 decimal digits.')
print('PSLQ maxcoeff=10^8, maxsteps=10000, tolerance=10^-185.')
for k,(j,ht,w1,w2) in enumerate(data):
    T=m.sqrt(ds[k]) if k<4 else m.sqrt(ds[k])/2
    re=m.mpf(0) if k<4 else m.mpf(1)/2
    tau=re+1j*T
    q=(-1 if k>=4 else 1)*m.exp(-2*m.pi*T)
    # 350 terms give far more than 250 digits at the smallest T and |Im z|<.4.
    c=[(n,q**n/(1-q**n)) for n in range(1,351)]
    def wp_y(y):
        return m.pi**2*(1/m.cosh(m.pi*y)**2-m.mpf(1)/3
                  +8*sum(n*qn*(1-(-1)**n*m.cosh(2*m.pi*n*y)) for n,qn in c))
    y=m.findroot(wp_y,(m.mpf('.34'),m.mpf('.39')),tol=m.mpf('1e-265'))
    mu=m.mpf(1)/2-1j*y
    etaabs=m.exp(-m.pi*T/12)*m.fprod(abs(1-q**n) for n in range(1,351))
    norm=m.exp(-m.pi*y*y/T)*abs(m.jtheta(1,m.pi*mu,m.exp(m.pi*1j*tau)))/etaabs
    logN=m.log(norm)
    E4=1+240*sum(n**3*q**n/(1-q**n) for n in range(1,351))
    Delta=q*m.fprod((1-q**n)**24 for n in range(1,351))
    jerr=abs(E4**3/Delta-j)
    ss=sum(m.mpf(v)*m.log(p) for p,v in finite[k])
    herr=abs(logN-(ss-ht))
    print('\nINDEX',k+1,'j',j,'CM_tau',m.nstr(tau,255),flush=True)
    print('mu',m.nstr(mu,255))
    print('N',m.nstr(norm,255))
    print('logN',m.nstr(logN,255))
    print('height_O',m.nstr(ht,255))
    print('D',m.nstr(6/m.pi*(logN-m.log(2*m.sqrt(3))),255))
    print('j absolute error',m.nstr(jerr,8),'global identity error',m.nstr(herr,8))
    assert jerr<m.mpf('1e-245') and herr<m.mpf('1e-245')
    ps=sorted(set(bad[k]+[2,3]))
    labels=['logN']+['log('+str(p)+')' for p in ps]+['pi','real omega1']
    vals=[logN]+[m.log(p) for p in ps]+[m.pi,w1]
    if ds[k]!=4:
        labels+=['abs imaginary omega2']
        vals+=[w2]
    else:
        print('Removed exact period relation: real omega1 = 2 abs imaginary omega2.')
    with m.workdps(200):
        relation=m.pslq(m.matrix(vals),tol=m.mpf('1e-185'),maxcoeff=10**8,maxsteps=10000)
    print('PSLQ labels',labels)
    print('PSLQ relation',relation,flush=True)
    rows.append(dict(index=k+1,j=j,tau=m.nstr(tau,255),mu=m.nstr(mu,255),N=m.nstr(norm,255),logN=m.nstr(logN,255),height_O=m.nstr(ht,255),D=m.nstr(6/m.pi*(logN-m.log(2*m.sqrt(3))),255),height_error=m.nstr(herr,8),labels=labels,relation=relation))
    (root/'records/C_cm_theta_pslq.json').write_text(json.dumps(rows,indent=2)+'\n')
print('\nALL 11 INDEPENDENT IDENTITIES AGREE TO AT LEAST 245 DECIMAL PLACES.')
