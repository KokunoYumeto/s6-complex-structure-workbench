"""Two independent evaluations of genus-two periods, not of the rank-six lift.

Method A: tanh-sinh integration after resolving the endpoint square roots.
Method B: binomial power series with exact cosine moments.
The branch cycles are the lifts of the oriented edges of a Euclidean MST of
the five finite roots.  Each edge has an empty diameter disk, so the series
converges and the root branches used by both methods are specified explicitly.
No numerical result in this file is used as a proof of the global lift.
"""
import mpmath as mp
from itertools import combinations
from pathlib import Path
import json
mp.mp.dps=90

def fmt(z):
    return [mp.nstr(mp.re(z),80),mp.nstr(mp.im(z),80)]

def roots_for(lam):
    roots=mp.polyroots([1,0,0,0,lam**3,lam**4],maxsteps=2000,error=False,
                       extraprec=100)
    return sorted(roots,key=lambda x:(float(mp.re(x)),float(mp.im(x))))

def tree(roots):
    parent=list(range(5))
    def get(i):
        while parent[i]!=i:i=parent[i]
        return i
    es=[]
    for _,i,j in sorted((abs(roots[i]-roots[j]),i,j) for i,j in combinations(range(5),2)):
        if get(i)!=get(j):
            parent[get(i)]=get(j);es.append((i,j))
    return es

def period_pair(roots,i,j):
    mid=(roots[i]+roots[j])/2; h=(roots[i]-roots[j])/2
    others=[k for k in range(5) if k not in [i,j]]
    radii=[h/(mid-roots[k]) for k in others]
    r=max(map(abs,radii)); assert r<1
    R0=mp.fprod(mp.sqrt(mid-roots[k]) for k in others)
    def invR(theta):
        t=mp.cos(theta)
        return 1/(R0*mp.fprod(mp.sqrt(1+rho*t) for rho in radii))
    integral=[2j*mp.quad(lambda th:(mid+h*mp.cos(th))**k*invR(th),
                        [0,mp.pi/4,mp.pi/2,3*mp.pi/4,mp.pi],method='tanh-sinh')
              for k in [0,1]]
    # Each |binom(-1/2,n)| <= 1.  Threefold convolution is bounded by
    # binom(n+2,2)*r**n.  The tail is summed symbolically below.
    N=max(80,int(mp.ceil(mp.log(mp.mpf('1e-78'))/mp.log(r)))+50)
    fs=[]
    for rho in radii:
        a=[mp.mpc(1)]
        for n in range(1,N+1):a.append(a[-1]*(-rho)*(2*n-1)/(2*n))
        fs.append(a)
    coeff=fs[0]
    for b in fs[1:]:
        coeff=[mp.fsum(coeff[k]*b[n-k] for k in range(n+1)) for n in range(N+1)]
    moments=[mp.mpf(0)]*(N+2);moments[0]=mp.mpf(1)
    for n in range(2,N+2,2):moments[n]=moments[n-2]*(n-1)/n
    s0=mp.fsum(coeff[n]*moments[n] for n in range(N+1))
    s1=mp.fsum(coeff[n]*moments[n+1] for n in range(N+1))
    series=[2j*mp.pi*s0/R0,2j*mp.pi*(mid*s0+h*s1)/R0]
    tail=(r**(N+1)/2)*((N+3)*(N+2)/(1-r)+(2*N+5)*r/(1-r)**2
                       +r*(1+r)/(1-r)**3)
    tail0=2*mp.pi*tail/abs(R0)
    tail1=tail0*(abs(mid)+abs(h))
    err=max(abs(a-b) for a,b in zip(integral,series))
    assert err<mp.mpf('1e-65')
    return {'edge':[i,j],'ratio':mp.nstr(r,30),'N':N,
            'quadrature':[fmt(z) for z in integral],
            'series':[fmt(z) for z in series],
            'agreement_error':mp.nstr(err,12),
            'formal_series_tail_bounds':[mp.nstr(tail0,12),mp.nstr(tail1,12)]}

out={'precision_digits':mp.mp.dps,'scope':__doc__,'points':[]}
for lv in [1,2]:
    lam=mp.mpf(lv);roots=roots_for(lam);edges=tree(roots)
    point={'lambda':lv,'roots':[fmt(r) for r in roots],
           'root_residual':mp.nstr(max(abs(r**5+lam**3*r+lam**4) for r in roots),12),
           'edges':edges,'periods':[]}
    print('lambda',lv,'edges',edges,'root residual',point['root_residual'],flush=True)
    for i,j in edges:
        p=period_pair(roots,i,j);point['periods'].append(p)
        print(json.dumps(p,indent=2),flush=True)
    out['points'].append(point)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
