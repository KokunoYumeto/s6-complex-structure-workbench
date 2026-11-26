#!/usr/bin/env python3
"""Exact rational Rouche certificates for the three primary J-cover labels.

Floating point locates candidate centers only. Every continued sheet is
certified by a rational strict Rouche bound on an entire path segment.
This is new ancillary geometric transport, with no historical code input.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb,ceil,log2
from datetime import datetime,timezone
import json
import sys
import sympy as S
import mpmath as mp

mp.mp.dps=90
HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation5_iii_d2'
ZERO=(F(0),F(0));ONE=(F(1),F(0))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,r):return(a[0]*r,a[1]*r)
def upper(a):return abs(a[0])+abs(a[1])
def lower(a):return max(abs(a[0]),abs(a[1]))
def mc(a):return mp.mpc(mp.mpf(a[0].numerator)/a[0].denominator,mp.mpf(a[1].numerator)/a[1].denominator)
def rational(z):return(F(mp.nstr(z.real,55)),F(mp.nstr(z.imag,55)))
def txt(z):return[str(z[0]),str(z[1])]
def taylor(coeff,c):
    d=len(coeff)-1;powers=[ONE]
    for _ in range(d):powers.append(mul(powers[-1],c))
    out=[]
    for k in range(d+1):
        z=ZERO
        for j in range(k,d+1):z=add(z,scale(powers[j-k],F(coeff[j]*comb(j,k))))
        out.append(z)
    return out
def poly(coeff,z):
    ans=mp.mpc(0)
    for c in reversed(coeff):ans=ans*z+c
    return ans
def newton(N,D,t,z):
    tn=mc(t)
    Nd=[i*N[i] for i in range(1,len(N))]
    Dd=[i*D[i] for i in range(1,len(D))]
    for _ in range(100):
        value=poly(N,z)-tn*poly(D,z)
        deriv=poly(Nd,z)-tn*poly(Dd,z)
        step=value/deriv;z-=step
        if abs(step)<mp.mpf('1e-80'):return z
    raise AssertionError('candidate root Newton iteration did not converge')
def data_at(N,D,t,c):
    nt=taylor(N,c);dt=taylor(D,c)
    return [sub(a,mul(t,b)) for a,b in zip(nt,dt)],dt
def margin(pt,r):
    return lower(pt[1])*r-upper(pt[0])-sum((upper(pt[k])*r**k for k in range(2,len(pt))),F(0))
def certify_small(N,D,t,centers):
    eps=F(1,10**45)
    for i,c in enumerate(centers):
        pt,_=data_at(N,D,t,c)
        assert margin(pt,eps)>0
        for q in centers[:i]:assert lower(sub(c,q))>2*eps
    return eps
def continue_segment(N,D,t0,t1,centers):
    total=sub(t1,t0);pos=F(0);steps=[]
    while pos<1:
        t=add(t0,scale(total,pos));cert=[]
        for i,c in enumerate(centers):
            sep=min(lower(sub(c,q)) for j,q in enumerate(centers) if i!=j)
            k=max(0,ceil(-log2(float(sep)/8)))
            r=F(1,2**k)
            pt,dt=data_at(N,D,t,c)
            while margin(pt,r)<=0:r/=2
            marg=margin(pt,r)
            sensitivity=sum((upper(z)*r**k for k,z in enumerate(dt)),F(0))
            cert.append((r,marg,sensitivity))
        step=1-pos
        assert all(cert[i][0]+cert[j][0]<lower(sub(centers[i],centers[j]))
                   for i in range(len(centers)) for j in range(i))
        while any(upper(scale(total,step))*sens>=marg for r,marg,sens in cert):step/=2
        tnew=add(t,scale(total,step))
        new=[rational(newton(N,D,tnew,mc(c))) for c in centers]
        eps=certify_small(N,D,tnew,new)
        for old,c,(r,marg,sens) in zip(centers,new,cert):
            # The unique new root lies in its old whole-segment disc.
            assert upper(sub(c,old))+eps<r
            assert upper(scale(total,step))*sens<marg
        steps.append({'start':txt(t),'end':txt(tnew),'centers':[txt(c) for c in centers],
                      'radii':[str(z[0]) for z in cert]})
        centers=new;pos+=step
    return centers,steps
def match_cover(p0,p1,q0,q1):
    n=len(p0);answers=[]
    for start in range(n):
        f={0:start};queue=[0];ok=True
        for i in queue:
            for p,q in [(p0,q0),(p1,q1)]:
                j=p[i];k=q[f[i]]
                if j in f:
                    if f[j]!=k:ok=False;break
                else:f[j]=k;queue.append(j)
            if not ok:break
        if ok and len(f)==n and len(set(f.values()))==n:
            answers.append([f[i] for i in range(n)])
    assert len(answers)==1
    f=answers[0];fi=[f.index(i) for i in range(n)]
    assert all(f[p0[i]]==q0[f[i]] and f[p1[i]]==q1[f[i]] for i in range(n))
    return f,fi


def main():
    print('Exact analytic-cover work started',datetime.now(timezone.utc).isoformat(),flush=True)
    x=S.symbols('x')
    models=[
     ('55_II',3*(8*x-1)*(8*x**3+87*x**2+96*x-64),
      (8*x-1)*(64*x**5+1040*x**4+3925*x**3+100*x**2+3200*x-512)),
     ('56_III',75*(5*x-1)*(5*x**3+45*x**2+39*x-25),
      25*(5*x-1)**2*(25*x**4+340*x**3+1086*x**2+100*x+625)),
     ('56_IV',12*x**2*(x**2+8*x+10),4*x**2*(2*x**4+24*x**3+78*x**2+56*x+27)),
     ('45_II',12*x*(x**3-6*x**2+15*x-12),
      4*x*(2*x**5-18*x**4+72*x**3-144*x**2+135*x-27)),
     ('47_II',12*x*(9*x**3+36*x**2+42*x+14),
      12*x*(18*x**5+108*x**4+234*x**3+222*x**2+87*x+8)),
     ('47_III',12*x*(x**3+4*x**2+10*x+6),
      4*x**2*(2*x**4+12*x**3+42*x**2+70*x+63)),
     ('49_IVstar',S.Integer(3),1+x**2)]
    dessins={r['name']:r for r in json.loads((INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KM_dessin_transport_maps.json').read_text())}
    only=sys.argv[1] if len(sys.argv)>1 else None
    saved=INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KM_analytic_cover_maps.json'
    results=json.loads(saved.read_text()) if only and saved.exists() else []
    base=(F(1,2),F(0))
    loops=[[(F(1,2),F(0)),(F(1,2),F(1,2)),(F(-1,2),F(1,2)),
            (F(-1,2),F(-1,2)),(F(1,2),F(-1,2)),(F(1,2),F(0))],
           [(F(1,2),F(0)),(F(1,2),F(-1,2)),(F(3,2),F(-1,2)),
            (F(3,2),F(1,2)),(F(1,2),F(1,2)),(F(1,2),F(0))]]
    for name,g2,g3 in models:
        if only and name!=only:continue
        N0,D0=S.fraction(S.cancel(g2**3/(g2**3-27*g3**2)))
        degree=max(S.degree(N0,x),S.degree(D0,x))
        N=[int(S.expand(N0).coeff(x,i)) for i in range(degree+1)]
        D=[int(S.expand(D0).coeff(x,i)) for i in range(degree+1)]
        approximate=S.Poly(N0-S.Rational(1,2)*D0,x).nroots(n=85,maxsteps=1000)
        centers=[rational(mp.mpc(str(S.re(z)),str(S.im(z)))) for z in approximate]
        eps=certify_small(N,D,base,centers)
        permutations=[];certificates=[]
        for iloop,loop in enumerate(loops):
            current=centers.copy();cc=[]
            for u,v in zip(loop,loop[1:]):
                current,steps=continue_segment(N,D,u,v,current);cc.extend(steps)
            pp=[]
            for c in current:
                choices=[i for i,q in enumerate(centers) if upper(sub(c,q))<eps]
                assert len(choices)==1;pp.append(choices[0])
            assert sorted(pp)==list(range(degree))
            permutations.append(pp);certificates.append(cc)
            print(name,'loop',iloop,'certified segments',len(cc),'permutation',pp,flush=True)
        ds=dessins.get(name)
        if ds:
            f,fi=match_cover(ds['sigma0'],ds['sigma1'],*permutations)
        else:
            # The new ribbon graph will use these literal certified labels.
            f=fi=list(range(degree))
        print(name,'EXACT sheet map passport->actual',f,'inverse',fi,flush=True)
        results=[r for r in results if r['name']!=name]
        results.append({'name':name,'N_coefficients':N,'D_coefficients':D,
                        'basepoint':txt(base),'base_root_centers':[txt(c) for c in centers],
                        'base_enclosure_radius':str(eps),'positive_loops':[[txt(z) for z in loop] for loop in loops],
                        'actual_permutations':permutations,'passport_to_actual':f,
                        'actual_to_passport':fi,'segment_certificates':certificates})
        (HERE/'S6_SERIES_PUBLISH_III_02KM_analytic_cover_maps.json').write_text(json.dumps(results,separators=(',',':'))+'\n')
    print('Exact analytic-cover work completed',datetime.now(timezone.utc).isoformat(),flush=True)

if __name__=='__main__':main()
