"""Exact cover audit and independently rounded constants for the local proof.
Uses Fraction for the cover and Arb (not mpmath) for analytic constants.
"""
from collections import defaultdict, Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from flint import arb, ctx

ctx.prec=256
P=arb.pi()
BASE=Path(__file__).resolve().parent
SOURCE=BASE.parents[1]/'background/s6_02_return/code/f_interval_parallel_certificate.json'

def a(x):
    q=F(x)
    return arb(q.numerator)/q.denominator

def upper(x):
    return x.upper().str(70,more=True)

def bound_sum_gaussian(k):
    # A_k = sum n^k exp(-0.9*pi*n^2) cosh(0.4*pi*n).
    out=sum((arb(n)**k*(-a('9/10')*P*n*n).exp()*(a('2/5')*P*n).cosh() for n in range(1,11)),arb(0))
    # n=11+j; n^2>=121+23j; (11+j)^k<=11^k*(1+j)^k.
    r=(-a('9/10')*P*23+a('2/5')*P).exp()
    first=(-a('9/10')*P*121+a('2/5')*P*11).exp()*11**k
    moment=[1/(1-r),1/(1-r)**2,(1+r)/(1-r)**3][k]
    return out+arb(0,(first*moment).upper())

def gaussian_tail(alpha,start,power=0):
    # For n=start+j, alpha*n^2 >= alpha*start^2 + alpha*(2start+1)j.
    r=(-alpha*(2*start+1)).exp()
    first=(-alpha*start*start).exp()
    if power==0:
        return first/(1-r)
    if power==2:
        return first*(start*start/(1-r)+2*start*r/(1-r)**2+r*(1+r)/(1-r)**3)
    raise ValueError(power)

def audit_cover():
    b=json.loads(SOURCE.read_text())
    leaves=[]
    for r in b['certified']:
        leaves.append(tuple(map(F,r['box'])))
    for r in b['omitted']:
        q=tuple(map(F,r)); x0,x1,y0,y1=q
        assert x0>=0 and x1<=F(1,10000) and y0>=1-F(1,10000) and y1<=1+F(1,10000)
        leaves.append(q)
    for r in b['outside_modular_domain']:
        q=tuple(map(F,r)); x0,x1,y0,y1=q
        assert x1*x1+y1*y1<1
        leaves.append(q)
    assert not b['pending'] and not b['summary']['undecided_boxes']
    events=defaultdict(list)
    area=F(0)
    for x0,x1,y0,y1 in leaves:
        assert 0<=x0<x1<=F(1,2) and F(17,20)<=y0<y1<=2
        events[x0].append((1,y0,y1))
        events[x1].append((-1,y0,y1))
        area+=(x1-x0)*(y1-y0)
    active=Counter()
    xs=sorted(events)
    for x in xs:
        for sign,y0,y1 in events[x]:
            active[(y0,y1)]+=sign
            assert active[(y0,y1)]>=0
            if active[(y0,y1)]==0:
                del active[(y0,y1)]
        if x==F(1,2):
            assert not active
            continue
        cursor=F(17,20)
        for (y0,y1),mult in sorted(active.items()):
            assert mult==1 and y0==cursor
            cursor=y1
        assert cursor==2
    assert area==F(23,40)
    assert 2*F(1,10000)**2<F(3,20000)**2
    return {'leaves':len(leaves),'certified':len(b['certified']),
            'omitted':len(b['omitted']),'excluded':len(b['outside_modular_domain']),
            'exact_area':str(area),'vertical_sweep_breakpoints':len(xs),
            'interiors_disjoint':True,'closed_rectangles_cover_whole_root':True,
            'omitted_square_inside_local_disc':True}

def local_constants():
    A=[bound_sum_gaussian(k) for k in range(3)]
    a0=2*A[0];a1=4*P*A[1];a2=8*P**2*A[2]
    rr=(-a('9/5')*P).exp()
    G=a2/(1-a0)+a1*a1/(1-a0)**2+P*P/3*(1+24*rr/(1-rr)**3)
    H=-(1-a0).log()+a('11/10')*P/12+rr/(1-rr)**2
    assert G< a('18.373') and H<a('.547') and a0<1
    # Theta constants and their derivative coefficients, using independent sums.
    # Spell the exponent as -pi*(n+1/2)^2, without squaring pi.
    th2=2*sum(((-P*((arb(n)+a('1/2'))**2)).exp() for n in range(16)),arb(0))
    t2d=2*P*sum((((arb(n)+a('1/2'))**2)*(-P*((arb(n)+a('1/2'))**2)).exp() for n in range(16)),arb(0))
    th4=1+2*sum(((-1)**n*(-P*n*n).exp() for n in range(1,17)),arb(0))
    t4d=2*P*sum(((-1)**n*n*n*(-P*n*n).exp() for n in range(1,17)),arb(0))
    # For half-integers starting at 16.5, bound by the integral-free geometric estimate.
    th2+=arb(0,(2*gaussian_tail(P,a('33/2'))).upper())
    t2d+=arb(0,(2*P*gaussian_tail(P,a('33/2'),2)).upper())
    th4+=arb(0,(2*gaussian_tail(P,17)).upper())
    t4d+=arb(0,(2*P*gaussian_tail(P,17,2)).upper())
    d=4*P*P/3*(th2**3*t2d-th4**3*t4d)
    q=(-2*P).exp()
    E4=1+240*sum((n**3*q**n/(1-q**n) for n in range(1,25)),arb(0))
    # (24+k)^3 <= 25^3*k^3, sum k^3 q^(k-1)=(1+4q+q²)/(1-q)^4.
    tail=240*25**3*q**25*(1+4*q+q*q)/(1-q)**5
    E4+=arb(0,tail.upper())
    gquarter=P**4*E4/3
    assert a('10.03')<d<a('10.04')
    assert a('47.26')<gquarter<a('47.30')
    eps=a('3/20000'); rh=a('3/100'); s=a('3/2000'); r2=a('9/400')
    boundary_lower=(a('47.26')-500*r2/(1-r2))*rh**2
    perturb=20*s/((1-s)*(1-r2))
    assert boundary_lower>a('.03217') and perturb<a('.03074') and perturb<boundary_lower
    qerr=500*(r2+s/(1-s))/(1-r2)
    x_over_h=(a('47.30')+qerr)/(a('10.03')-2000*eps/(1-s))
    hsq=(a('10.04')*eps+2000*eps*eps/(1-s))/(a('47.26')-qerr)
    remainder=a('3/5')*(70**2+25*70+25**2)/((1-s)*(1-a('25/20000')))+7*P/(1-eps)
    assert x_over_h<7 and hsq<a('1/20000') and remainder<5000
    b=a('43/100'); qr=(-4*P).exp()
    cusp_strip=1/(P*b).sinh()**2+8*(qr/(1-qr)**3+
                (((-2*P).exp()/(1-(-2*P).exp())**2)+
                 ((-6*P).exp()/(1-(-6*P).exp())**2))/(2*(1-qr)))
    cusp_norm=2*(P*b).cosh()*(-P/3-P*b*b/2).exp()*\
              (2*(2*P*b).cosh()*qr/(1-qr)+qr*qr/(1-qr*qr)).exp()
    assert cusp_strip<a('1/3') and cusp_norm<a('1.082')
    assert (P*b).tanh()>b
    return {'precision_bits':ctx.prec,'A0_upper':upper(A[0]),'A1_upper':upper(A[1]),'A2_upper':upper(A[2]),
            'G_uniform_upper':upper(G),'H_uniform_upper':upper(H),'d':d.str(70,more=True),
            'g2_over_4':gquarter.str(70,more=True),
            'rouche_boundary_lower':boundary_lower.lower().str(70,more=True),
            'rouche_perturbation_upper':upper(perturb),
            'Q_error_upper':upper(qerr),'x_over_h_squared_upper':upper(x_over_h),
            'h_squared_upper':upper(hsq),'remainder_coefficient_upper':upper(remainder),
            'cusp_strip_error_upper':upper(cusp_strip),'cusp_norm_upper':upper(cusp_norm),
            'strict_loss_coefficient_lower':(P/2-a('1/4')).lower().str(70,more=True)}

if __name__=='__main__':
    result={'cover':audit_cover(),'local':local_constants(),'result':'PASS'}
    (BASE/'e4_cover_and_local.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
