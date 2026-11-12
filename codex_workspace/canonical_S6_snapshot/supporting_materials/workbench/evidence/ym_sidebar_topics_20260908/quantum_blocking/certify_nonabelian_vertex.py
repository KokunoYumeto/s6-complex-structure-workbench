"""Integer-only outward interval certificate for one full cubic vertex.

Every endpoint is an integer divided by SCALE. This certificate evaluates
the complete finite radical spectral sum, not sampled floating point data.
"""
from pathlib import Path
from itertools import product
from math import isqrt
import json

ROOT=Path(__file__).resolve().parent
SCALE=10**40
def ceildiv(a,b):return -((-a)//b)
class I:
    def __init__(self,lo,hi=None):self.lo=int(lo);self.hi=int(lo if hi is None else hi);assert self.lo<=self.hi
    @classmethod
    def rat(cls,p,q=1):
        assert q>0
        return cls(p*SCALE//q,ceildiv(p*SCALE,q))
    def __add__(self,o):
        if isinstance(o,int):o=I.rat(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-o
    def __rsub__(self,o):return -self+o
    def __mul__(self,o):
        if isinstance(o,int):o=I.rat(o)
        vals=[a*b for a in [self.lo,self.hi] for b in [o.lo,o.hi]]
        return I(min(vals)//SCALE,ceildiv(max(vals),SCALE))
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,int):o=I.rat(o)
        assert o.lo>0 or o.hi<0
        if o.hi<0:return (-self)/(-o)
        low=min(a*SCALE//b for a in [self.lo,self.hi] for b in [o.lo,o.hi])
        high=max(ceildiv(a*SCALE,b) for a in [self.lo,self.hi] for b in [o.lo,o.hi])
        return I(low,high)
    def sqrt(self):
        assert self.lo>=0
        low=isqrt(self.lo*SCALE);high=isqrt(self.hi*SCALE)
        if high*high<self.hi*SCALE:high+=1
        assert low*low<=self.lo*SCALE and high*high>=self.hi*SCALE
        return I(low,high)
    def data(self):return dict(lower_numerator=str(self.lo),upper_numerator=str(self.hi),denominator=str(SCALE))

zero=I.rat(0);one=I.rat(1)
sqrt5=I.rat(5).sqrt()
sin1=(sqrt5-one)/4;cos1=((5+sqrt5)/8).sqrt()
co=[one];si=[zero]
for m in range(1,20):
    co.append(co[-1]*cos1-si[-1]*sin1)
    si.append(si[-1]*cos1+co[-2]*sin1)
sq25=I.rat(2,5).sqrt();sq15=I.rat(1,5).sqrt()

L=2;N=5
vertices=list(product(range(-L,L+1),repeat=3))
def shift(n,d):
    v=list(n);v[d]+=1;return tuple(v)
edges=[(n,d) for n in vertices for d in range(3) if n[d]<L]
eid={e:i for i,e in enumerate(edges)}
paths={(-L,-L,-L):[]};tree=set()
for n in sorted(vertices,key=lambda v:sum(v)):
    if n==(-L,-L,-L):continue
    d=next(d for d in range(3) if n[d]>-L)
    par=list(n);par[d]-=1;par=tuple(par)
    e=eid[(par,d)];tree.add(e);paths[n]=paths[par]+[e]
chords=[e for e in range(len(edges)) if e not in tree]
specified=[((-1,1,-2),1),((-1,2,-2),2),((-1,1,-1),1)]
selected=[eid[e] for e in specified]
assert [chords.index(e) for e in selected]==[43,52,45]
B=[]
for e in selected:
    n,d=edges[e];row={e:-1}
    for p in paths[n]+paths[shift(n,d)]:row[p]=row.get(p,0)-1
    B.append(row)

def phi(jj,e):
    n,d=edges[e]
    if jj[d]==0:return zero
    out=-sq25*si[(jj[d]*(2*n[d]+6))%20]
    for k in range(3):
        if k!=d:out=out*(sq15 if jj[k]==0 else sq25)*co[(jj[k]*(2*n[k]+5))%20]
    return out

KK=[[zero for _ in range(3)] for _ in range(3)]
QQ=[[zero for _ in range(3)] for _ in range(3)]
terms=0
for jj in product(range(N),repeat=3):
    if sum(j>0 for j in jj)<2:continue
    ss=[2*si[j] for j in jj]
    lam=sum((x*x for x in ss),zero);sigma=lam.sqrt()
    PP=[[(one if d==k else zero)-ss[d]*ss[k]/lam for k in range(3)] for d in range(3)]
    target_phi=[phi(jj,e) for e in selected]
    Bphi=[]
    for row in B:
        rr=[zero,zero,zero]
        for e,b in row.items():rr[edges[e][1]]=rr[edges[e][1]]+b*phi(jj,e)
        Bphi.append(rr)
    for i in range(3):
        di=edges[selected[i]][1]
        for k in range(3):
            dk=edges[selected[k]][1]
            KK[i][k]=KK[i][k]+sigma*target_phi[i]*target_phi[k]*PP[di][dk]
            QQ[i][k]=QQ[i][k]+sigma*target_phi[k]*sum((Bphi[i][d]*PP[d][dk] for d in range(3)),zero)
    terms+=1

def coefficient(K,Q):
    # Q_b dot(e_b cross K_b), with the original ordered colour assignment.
    return (Q[0][2]*K[0][1]-Q[0][1]*K[0][2]
           +Q[1][0]*K[1][2]-Q[1][2]*K[1][0]
           +Q[2][1]*K[2][0]-Q[2][0]*K[2][1])/8
kin=coefficient(KK,QQ);mag=I.rat(-1,8);full=kin+mag
assert full.lo>I.rat(-243,1000).hi and full.hi<I.rat(-242,1000).lo

# A short human-readable rational matrix enclosure; retain the full certificate.
def coarse_matrix(M):
    numerators=[];out=[]
    for row in M:
        ns=[];rr=[]
        for x in row:
            n=x.lo*10**6//SCALE
            assert x.hi<(n+1)*SCALE//10**6
            ns.append(n);rr.append(I.rat(n,10**6)+I(0,SCALE//10**6))
        numerators.append(ns);out.append(rr)
    return numerators,out
Kn,Kco=coarse_matrix(KK);Qn,Qco=coarse_matrix(QQ)
broad=coefficient(Kco,Qco)+mag
assert broad.lo>I.rat(-243,1000).hi and broad.hi<I.rat(-242,1000).lo
receipt=dict(proved=True,method='Outward integer arithmetic with fixed denominator10^40; every square root enclosed by integer-square inequalities.',
             original_box_L=2,original_chord_indices=[43,52,45],original_edges=specified,
             frequency_blocks=terms,dimension=176,K=[[x.data() for x in row] for row in KK],
             Q=[[x.data() for x in row] for row in QQ],kinetic=kin.data(),magnetic=mag.data(),full=full.data(),
             short_K_lower_numerators=Kn,short_Q_lower_numerators=Qn,short_entry_denominator=10**6,
             short_entry_upper_increment=1,short_full_enclosure=broad.data(),
             strict_conclusion='-243/1000 < a*cubic_coefficient < -242/1000',
             scope='A finite rigorous cubic-vertex certificate for the original operator; not a continuum gap certificate.')
(ROOT/'NONABELIAN_VERTEX_CERTIFICATE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['proved','frequency_blocks','strict_conclusion','short_K_lower_numerators','short_Q_lower_numerators']},indent=2))
