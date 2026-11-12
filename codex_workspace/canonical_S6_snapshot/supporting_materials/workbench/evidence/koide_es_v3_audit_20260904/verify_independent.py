"""Independent exact regression checks; no imported verifier routines.

Run from any directory. Results are written beside this file. The unbounded
arguments, domains, and inverse maps are in koide_es_v3_audit.tex.
"""
from fractions import Fraction as F
from math import gcd, isqrt, lcm
from pathlib import Path
import json
import sympy as s


def divisors(n):
    low = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return sorted(set(low + [n // d for d in low]))


def delta(q):
    x, y, z = q
    return 4 * (x*y+x*z+y*z) - x*x-y*y-z*z


def beta(a, b):
    D = -1-a*a-b*b+4*a+4*b+4*a*b
    K = 1-2*a-2*b
    assert D != 0 and K != 0
    ell = F(2*K, D)
    return (1+ell, ell*a, ell*b)


def main():
    out = {}
    shells = states = 0
    for n in range(5, 162, 4):
        for R in range(3, n, 4):
            if gcd(n, R) != 1:
                continue
            a = (n+R)//4
            N = n*a
            # Enumerate positive reciprocal solutions from a rigorously
            # bounded smaller denominator, independently of divisor channels.
            # If y<=z, N/R<y<=2N/R; z=Ny/(Ry-N).
            direct = set()
            for y in range(N//R+1, 2*N//R+1):
                if (N*y) % (R*y-N) == 0:
                    z = N*y//(R*y-N)
                    direct.update(((y,z),(z,y)))
            constructed = set()
            for dlt in divisors(n*n):
                for u in divisors(a*a):
                    if (4*u+dlt) % R:
                        continue
                    v = a*a//u
                    d, e = n*n//dlt*u, dlt*v
                    assert (N+d)%R == (N+e)%R == 0
                    y, z = (N+d)//R, (N+e)//R
                    assert F(4,n) == F(1,a)+F(1,y)+F(1,z)
                    kap = gcd(R*y-N,n*n)
                    assert (n*n//kap,(R*y-N)//kap,(R*z-N)//dlt)==(dlt,u,v)
                    assert y != z
                    T=(4*u+dlt)//R
                    sig=1 if dlt%4==1 else -1
                    assert (T+sig)%4==0
                    l0,l1,l2=(T+sig)//4,(3*T-dlt)//4,sig
                    assert 12*l0-4*l1-3*l2==dlt
                    assert (l1%3==0)==(dlt%3==0)
                    constructed.add((y,z))
                    states += 1
            assert direct == constructed
            shells += 1
    out['independent_reciprocal_shells']=shells
    out['independent_oriented_states']=states

    prime_cases = certificates = 0
    for p in range(5, 5000, 4):
        if any(p%d==0 for d in range(2,isqrt(p)+1)):
            continue
        m=(p+1)//2
        ds=divisors(m)
        Rs=[R for R in ds if R%4==3]
        chi=lambda d: 1 if d%4==1 else -1
        assert len(Rs)==(len(ds)-sum(map(chi,ds)))//2
        for R in Rs:
            x=(p+R)//4
            k=(p+1)//R
            assert F(4,p)==F(1,x)+F(1,x*k)+F(1,p*x*k)
        prime_cases+=1
        certificates+=len(Rs)
    out['diagonal_prime_cases']=prime_cases
    out['diagonal_certificates']=certificates

    a,b,dlt=s.symbols('a b dlt', nonzero=True)
    D=-1-a*a-b*b+4*a+4*b+4*a*b
    K=1-2*a-2*b
    ell=2*K/D
    q=(1+ell,ell*a,ell*b)
    assert s.cancel(delta(q)+1)==0
    ai=s.cancel(q[1]/(q[0]-1))
    bi=s.cancel(q[2]/(q[0]-1))
    assert ai==a and bi==b
    assert s.cancel(a*((b*b-dlt)/a)-b*b+dlt)==0
    out['birational_symbolic_identity_and_inverse']=True
    tested=0
    for av in range(1,21):
        for bv in range(-20,21):
            qv=beta(av,bv)
            assert delta(qv)==-1
            assert qv[1]/(qv[0]-1)==av
            assert qv[2]/(qv[0]-1)==bv
            Dv=-1-av*av-bv*bv+4*av+4*bv+4*av*bv
            Kv=1-2*av-2*bv
            denominator=abs(Dv)//gcd(abs(Dv),abs(2*Kv))
            assert lcm(*(v.denominator for v in qv))==denominator
            tested+=1
    out['rational_map_denominator_cases']=tested
    out['example_A_1_1_0']=[str(v) for v in beta(1,1)]
    assert beta(1,1)==(F(1,3),F(-2,3),F(-2,3))
    # Opening positivity is valid for positive integer channel order, not
    # for every positive real delta as the broad definition could suggest.
    assert F(1,8)*2**2-1**2==F(-1,2)
    out['positive_real_delta_counterexample']={'r':2,'t':1,'delta':'1/8','all_companions_x':'odd','max_A11':'-1/2'}
    assert F(4,73)==F(1,20)+F(1,220)+F(1,4015)
    assert not any(R%4==3 for R in divisors(37))
    out['p73_misses_diagonal_but_has_other_ray']=[20,220,4015]

    # Exact retained conformal scale and orientation.
    n,d=s.symbols('n d', nonzero=True)
    A=(n*n/d+d)/2; B=(n*n/d-d)/2
    rho=s.Matrix([[A,0,B],[0,n,0],[B,0,A]])
    JL=s.diag(1,-1,-1)
    assert all(s.cancel(x)==0 for x in rho.T*JL*rho-n*n*JL)
    assert s.cancel(rho.det()-n**3)==0
    out['lorentz_scale_and_orientation']=True
    out['passed']=True
    target=Path(__file__).with_name('independent_results.json')
    target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
