"""Fresh exact arithmetic and independent-series checks for four Paper I targets.

No attached verification program is imported. Curve arithmetic uses Fractions
and direct finite-field point enumeration. The singular modulus uses directed
mpmath interval arithmetic with explicit infinite-series/product tail bounds.
The theta comparison uses Fourier/pentagonal sums against the Siegel product.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from functools import reduce
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import mpmath as m

ROOT = Path(__file__).parent
m.mp.dps = 90
m.iv.dps = 90


def curve_arithmetic():
    a1, a2, a3, a4, a6 = 0, 0, 1, -38, 90
    b2 = a1*a1 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    delta = -b2*b2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    j = F(c4**3, delta)
    assert (b2,b4,b6,b8,c4,c6,delta,j) == (0,-76,361,-1444,1824,-77976,-6859,-884736)
    finite = {}
    for p in (3,5):
        points = [(x,y) for x in range(p) for y in range(p)
                  if (y*y+y-x*x*x+38*x-90) % p == 0]
        finite[str(p)] = dict(points=points, cardinality=1+len(points), trace=p-len(points))
    assert [finite[str(p)]['cardinality'] for p in (3,5)] == [4,7]
    assert gcd(4,7) == 1 and 7 % 3 != 0 and 4 % 5 != 0
    assert finite['5']['trace'] == -1
    roots = [x for x in range(5) if (x*x-x+5) % 5 == 0]
    assert roots == [0,1]
    # Work on Y^2=x^3-38x+361/4 via the exact map Y=y+1/2.
    def add(p, q):
        if p is None: return q
        if q is None: return p
        x,y = p; u,v = q
        if x == u and y == -v: return None
        slope = (3*x*x-38)/(2*y) if p == q else (v-y)/(u-x)
        xx = slope*slope-x-u
        return (xx, slope*(x-xx)-y)
    p = (F(0),F(19,2))
    assert p[1]**2 == p[0]**3-38*p[0]+F(361,4)
    twice = add(p,p)
    assert (twice[0],twice[1]-F(1,2)) == (F(4),F(-2))
    triple = add(twice,p)
    reduced = []
    for a in range(1,isqrt(19//3)+1):
        for b in range(-a,a+1):
            if (b*b+19) % (4*a): continue
            c=(b*b+19)//(4*a)
            if a > c or ((abs(b)==a or a==c) and b<0): continue
            if gcd(gcd(a,b),c) == 1: reduced.append((a,b,c))
    assert reduced == [(1,1,5)]
    valuation_delta = 0
    dd = abs(delta)
    while dd % 19 == 0:
        dd //= 19
        valuation_delta += 1
    assert valuation_delta == 3 and dd == 1
    local_root = (-1)**((valuation_delta*19)//12)
    quadratic_residue = pow((-2)%19,9,19)
    assert local_root == quadratic_residue == 1
    return dict(invariants=dict(b2=b2,b4=b4,b6=b6,b8=b8,c4=c4,c6=c6,
                                discriminant=delta,j=str(j)),
                finite_fields=finite, split_polynomial_roots_mod_5=roots,
                twice_P=[str(twice[0]),str(twice[1]-F(1,2))],
                triple_P=[str(triple[0]),str(triple[1]-F(1,2))],
                reduced_forms_discriminant_minus19=reduced,
                valuation_discriminant_at19=valuation_delta,
                root_number_at19=local_root, root_number_global=-local_root,
                root_number_input='Rohrlich local root formula; no rank-parity inference')


def cm_interval():
    iv=m.iv
    q=-iv.exp(-iv.pi*iv.sqrt(iv.mpf(19)))
    r=abs(q)
    order=20
    sigma3=lambda n: sum(d**3 for d in range(1,n+1) if n%d==0)
    e4=1+240*sum((iv.mpf(sigma3(n))*q**n for n in range(1,order+1)),iv.mpf(0))
    # sigma_3(n)<=n^4; the ratio of successive n^4*r^n terms is bounded
    # by r*((N+2)/(N+1))^4 for n>=N+1.
    ratio=r*(iv.mpf(order+2)/(order+1))**4
    assert ratio.b < 1
    tail_e4=240*(order+1)**4*r**(order+1)/(1-ratio)
    e4 += iv.mpf([-1,1])*tail_e4
    product=iv.mpf(1)
    for n in range(1,order+1): product *= 1-q**n
    # |sum_{n>N} log(1-q^n)| <= r^(N+1)/((1-r)*(1-r^(N+1))).
    tail_log=r**(order+1)/((1-r)*(1-r**(order+1)))
    delta=q*product**24*iv.exp(iv.mpf([-1,1])*24*tail_log)
    j=e4**3/delta
    assert j.a > iv.mpf('-884736.5') and j.b < iv.mpf('-884735.5')
    assert j.a <= -884736 <= j.b
    return dict(q=str(q), order=order, E4_tail=str(tail_e4),
                log_product_tail=str(tail_log), j_interval=str(j),
                exact_identification='CM integrality + class number one + this width<1 interval imply j=-884736')


def siegel_theta_check():
    mp=m.mp
    cases=[('0.37','1.21','0.2','0.3'),('-0.43','0.91','0.6','0.2'),
           ('0.37','1.21','2.2','-1.7')]
    values=[]
    for re,im,s,t in cases:
        tau=mp.mpc(re,im); a1=mp.mpf(s);a2=mp.mpf(t)
        v=a1*tau+a2;q=mp.exp(2j*mp.pi*tau)
        b2=a1*a1-a1+mp.mpf(1)/6
        # Use exp for q's fractional prefactor to retain the stated branch.
        g=-mp.exp(mp.pi*1j*a2*(a1-1)+mp.pi*1j*tau*b2)*(1-mp.exp(2j*mp.pi*v))
        for n in range(1,161):
            g *= (1-q**n*mp.exp(2j*mp.pi*v))*(1-q**n*mp.exp(-2j*mp.pi*v))
        # Independent theta Fourier sum and Euler pentagonal sum for eta.
        theta=2*sum(((-1)**n*mp.exp(mp.pi*1j*tau*(n+mp.mpf('.5'))**2)
                     *mp.sin((2*n+1)*mp.pi*v) for n in range(100)),mp.mpc(0))
        eta=mp.exp(mp.pi*1j*tau/12)*sum(((-1)**k*q**(k*(3*k-1)//2)
                                                  for k in range(-100,101)),mp.mpc(0))
        rhs=1j*mp.exp(mp.pi*1j*a1*v)*theta/eta
        error=abs(g-rhs)/abs(g)
        norm=mp.exp(-mp.pi*mp.im(v)**2/mp.im(tau))*abs(theta/eta)
        normerror=abs(abs(g)-norm)/norm
        assert error < mp.mpf('1e-75') and normerror < mp.mpf('1e-75')
        values.append(dict(tau=[re,im],a=[s,t],complex_relative_error=mp.nstr(error,12),
                           modulus_relative_error=mp.nstr(normerror,12)))
    # Exact rational-polynomial identities and representative shifts.
    checked=0
    for n in range(2,26):
        for k in range(-2*n,2*n+1):
            b=F(k*k,n*n)-F(k,n)+F(1,6)
            assert F(12*n,2)*b*n == 6*k*k-6*k*n+n*n
            for l in (0,1,n-1):
                assert 6*n*F(l,n)*(F(k,n)-1)*n == 6*l*(k-n)
                checked += 1
    return dict(series_comparisons=values,exact_exponent_phase_cases=checked,
                mathematical_scope='Supplementary checks of product phase/modulus and Fourier prefactors; not a finite-sample proof of modularity')


if __name__ == '__main__':
    result=dict(created_at_utc=datetime.now(timezone.utc).isoformat(),
                program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                python_arithmetic='fractions.Fraction; direct enumeration; no Sage/PARI import',
                mpmath_version=m.__version__, curve=curve_arithmetic(),
                CM=cm_interval(), siegel=siegel_theta_check(),
                ricci_coefficient_in_units_of_pi=str(2*(-(F(-1)+2*F(1,4)))))
    assert result['ricci_coefficient_in_units_of_pi'] == '1'
    out=ROOT/'S6_SERIES_PUBLISH_I_initial_four_compute.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
