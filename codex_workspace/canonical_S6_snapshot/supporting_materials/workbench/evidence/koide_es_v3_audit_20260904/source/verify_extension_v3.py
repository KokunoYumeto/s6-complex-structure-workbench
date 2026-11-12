#!/usr/bin/env python3
"""Exact identities and bounded checks for the Koide--Erdos--Straus extension.

The proofs in the paper are algebraic.  This script is a reproducibility
receipt, not a substitute for those proofs.  All exhaustive loops use exact
integer arithmetic; floating arithmetic occurs only in the character-sum
roundoff check.
"""
from __future__ import annotations

import cmath
import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Iterable

import sympy as sp
from sympy.ntheory.modular import crt


def sieve_primes(limit: int) -> list[int]:
    b = bytearray(b"\x01") * (limit + 1)
    if limit >= 0: b[0] = 0
    if limit >= 1: b[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if b[p]:
            b[p*p:limit+1:p] = b"\x00" * (((limit-p*p)//p)+1)
    return [i for i in range(2, limit + 1) if b[i]]


PRIMES_2M = sieve_primes(2_000_000)
PRIME_SET_200K = set(p for p in PRIMES_2M if p <= 200_000)


def is_prime(n: int) -> bool:
    if n < 2: return False
    if n <= 200_000: return n in PRIME_SET_200K
    return bool(sp.isprime(n))


@lru_cache(maxsize=None)
def factorint_small(n: int) -> tuple[tuple[int, int], ...]:
    x = n
    fac: list[tuple[int, int]] = []
    for p in PRIMES_2M:
        if p*p > x: break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p; e += 1
            fac.append((p,e))
        if p > 2000 and x == n:  # harmless speed guard for prime-ish small inputs
            pass
    if x > 1: fac.append((x,1))
    return tuple(fac)


@lru_cache(maxsize=None)
def divisors(n: int) -> tuple[int, ...]:
    out = [1]
    for p,e in factorint_small(n):
        old = list(out)
        pe = 1
        for _ in range(e):
            pe *= p
            out += [d*pe for d in old]
    return tuple(sorted(out))


def xgcd(a: int, b: int) -> tuple[int,int,int]:
    old_r,r=a,b; old_s,s=1,0; old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_r,old_s,old_t


def centered_bezout(r: int, t: int) -> tuple[int,int]:
    g,A,B=xgcd(r,t)
    assert g==1
    x,y=-B,A  # r*y-t*x=1
    # unique centered representative x mod r, tie broken toward smaller |y|
    k0=round(-x/r)
    candidates=[]
    for k in range(k0-2,k0+3):
        xx=x+k*r; yy=y+k*t
        candidates.append((abs(xx),abs(yy),k,xx,yy))
    _,_,_,x,y=min(candidates)
    assert r*y-t*x==1 and 2*abs(x)<=r
    return x,y


def factor_ray(u: int, a: int) -> tuple[int,int,int]:
    g=math.gcd(u,a)
    r=u//g; t=a//g; s=g//r
    assert g==r*s
    assert u==r*r*s and a==r*s*t and a*a//u==s*t*t
    assert math.gcd(r,t)==1
    return r,s,t


def channel_states(n: int, R: int):
    assert n%4==1 and R%4==3 and 0<R<n and math.gcd(n,R)==1
    a=(n+R)//4; N=n*a
    for delta in divisors(n*n):
        for u in divisors(a*a):
            if (4*u+delta)%R: continue
            v=a*a//u
            d=(n*n//delta)*u
            e=delta*v
            assert d*e==N*N
            assert (N+d)%R==0 and (N+e)%R==0
            yield delta,u,v,(N+d)//R,(N+e)//R,d,e


def shell_states(n: int,R: int):
    a=(n+R)//4; N=n*a
    for d in divisors(N*N):
        if (N+d)%R: continue
        e=N*N//d
        if (N+e)%R: continue
        yield (N+d)//R,(N+e)//R,d,e


def terminal_data(R: int,delta: int,u: int):
    j=(R-3)//4; T=(4*u+delta)//R
    sig=1 if delta%4==1 else -1
    ell0=(T+sig)//4; ell1=u-j*T; ell2=sig
    assert 4*ell0==T+sig
    assert 12*ell0-4*ell1-3*ell2==delta
    # U_j [[R,-u],[4,-T]]
    left=((R-4*j,-u+j*T),(4,-T))
    right=((3,-ell1),(4,ell2-4*ell0))
    assert left==right
    assert 3*(-T)-(-ell1)*4==-delta
    assert math.gcd(3,4,ell1,T)==1
    assert (ell1%3!=0)==(delta%3!=0)
    return (j,T,ell0,ell1,ell2)


def opening_data(r: int,t: int,delta: int,k: int=0):
    x,y=centered_bezout(r,t)
    x+=k*r; y+=k*t
    A11=delta*r*r-x*x
    A12=delta*r*t-x*y
    A22=delta*t*t-y*y
    assert A11*A22-A12*A12==-delta
    if k==0: assert A11>0
    return x,y,A11,A12,A22


def matmul2(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def det2(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]


def inv_unimod(A):
    d=det2(A); assert abs(d)==1
    return ((A[1][1]//d,-A[0][1]//d),(-A[1][0]//d,A[0][0]//d))


def transpose(A): return ((A[0][0],A[1][0]),(A[0][1],A[1][1]))


def neg(A): return tuple(tuple(-x for x in row) for row in A)


def verify_opening_terminal_morphism(n: int,R: int,delta: int,u: int,a: int):
    r,s,t=factor_ray(u,a)
    j,T,ell0,ell1,ell2=terminal_data(R,delta,u)
    x,y,A11,A12,A22=opening_data(r,t,delta)
    A=((A11,A12),(A12,A22))
    B=((r,x),(t,y)); Binv=inv_unimod(B)
    J=((0,1),(1,0))
    LA=neg(matmul2(J,Binv))
    RA=matmul2(transpose(Binv),J)
    D=((1,0),(0,-delta))
    assert matmul2(matmul2(LA,A),RA)==D
    Rmat=((3,-ell1),(4,-T))
    P0=((-1,1),(-4,3)); Q0=((1,T-ell1),(0,1))
    assert matmul2(matmul2(P0,Rmat),Q0)==D
    composite=matmul2(matmul2(matmul2(matmul2(inv_unimod(P0),LA),A),RA),inv_unimod(Q0))
    assert composite==Rmat
    return {'ray':[r,t],'content':s,'bezout':[x,y],'opening':[list(A[0]),list(A[1])],
            'terminal':[list(Rmat[0]),list(Rmat[1])]}


def primitive_root_table(p: int):
    g=int(sp.primitive_root(p)); tab={}; x=1
    for j in range(p-1): tab[x]=j; x=x*g%p
    return g,tab


def fourier_count(n: int,R: int,delta: int):
    assert is_prime(R) and math.gcd(n,R)==1
    a=(n+R)//4
    fac=factorint_small(a)
    _,logs=primitive_root_table(R)
    target=(-delta*pow(n,-1,R))%R
    total=0j
    for j in range(R-1):
        def chi(z): return cmath.exp(2j*math.pi*j*logs[z%R]/(R-1))
        D=1+0j
        for q,e in fac:
            z=chi(q)
            D*=sum(z**beta for beta in range(-e,e+1))
        total+=chi(target).conjugate()*D
    return total/(R-1)


def choose_R_for_saturation(r: int,t: int,M: int,c: int):
    A=4*r*t; g=math.gcd(A,M); residue=(-c)%g
    floor=max(M,r,t,20)
    for R in PRIMES_2M:
        if R<=floor: continue
        if R%g==residue and R%4==3 and math.gcd(R,r*t*M)==1:
            return R
    raise RuntimeError('R search exhausted')


def saturation_progression(r: int,t: int,M: int,c: int):
    A=4*r*t; g=math.gcd(A,M); Mp=M//g
    R=choose_R_for_saturation(r,t,M,c)
    sR=(-pow(4*r*r,-1,R))%R
    sM=0 if Mp==1 else (pow(A//g,-1,Mp)*((c+R)//g))%Mp
    s0=int(crt([R,Mp],[sR,sM],check=True)[0])
    L=R*Mp; p0=A*s0-R; Q=A*L
    assert Q%M==0 and p0%M==c%M
    assert (4*r*r*s0+1)%R==0
    assert math.gcd(p0,Q)==1
    return R,s0,L,p0,Q


def first_progression_prime(p0: int,Q: int,R: int,max_steps=5000):
    k=max(0,(R+1-p0+Q-1)//Q)
    for j in range(k,k+max_steps):
        p=p0+Q*j
        if is_prime(p): return p,j
    return None


def verify_es(p: int,R: int,r: int,s: int,t: int,channel: str):
    a=r*s*t; assert p+R==4*a
    if channel=='E':
        assert (4*r*r*s+1)%R==0
        kap=(p*r+t)//R; assert p*r+t==R*kap
        xyz=(a,p*r*s*kap,s*t*kap)
    else:
        assert (r+t)%R==0
        kap=(r+t)//R
        xyz=(a,p*r*s*kap,p*s*t*kap)
    x,y,z=xyz
    assert 4*x*y*z==p*(x*y+x*z+y*z)
    return xyz


def symbolic_receipt():
    n,d=sp.symbols('n d', nonzero=True)
    A=(n*n/d+d)/2; B=(n*n/d-d)/2
    rho=sp.Matrix([[A,0,B],[0,n,0],[B,0,A]])
    J=sp.diag(1,-1,-1)
    assert sp.simplify(rho.T*J*rho-n*n*J)==sp.zeros(3)
    assert sp.factor(rho.det())==n**3
    return {'rho':[[str(rho[i,j]) for j in range(3)] for i in range(3)],
            'conformal_factor':'n^2','determinant':'n^3'}



def chi4_odd(n: int) -> int:
    assert n % 2 == 1
    return 1 if n % 4 == 1 else -1


def verify_diagonal_ray_counts(bound: int = 5000):
    cases = 0
    total_certificates = 0
    max_count = 0
    max_examples = []
    exceptional = []
    for p in PRIMES_2M:
        if p >= bound:
            break
        if p % 4 != 1:
            continue
        m = (p + 1) // 2
        ds = divisors(m)
        residuals = [R for R in ds if R % 4 == 3]
        character_count = (len(ds) - sum(chi4_odd(d) for d in ds)) // 2
        assert character_count == len(residuals)

        fac = factorint_small(m)
        tau = math.prod(e + 1 for _, e in fac)
        char_product = 1
        has_three_mod_four = False
        for q, e in fac:
            if q % 4 == 1:
                char_product *= e + 1
            else:
                assert q % 4 == 3
                has_three_mod_four = True
                char_product *= 1 if e % 2 == 0 else 0
        assert (tau - char_product) // 2 == len(residuals)
        assert (len(residuals) == 0) == (not has_three_mod_four)
        if p % 8 == 5:
            assert residuals
        if p % 24 == 13:
            assert residuals
        if not residuals:
            assert p % 24 == 1
            exceptional.append(p)

        triples = []
        matrices = []
        for R in residuals:
            assert (p + 1) % R == 0
            ss = (p + R) // 4
            k = (p + 1) // R
            assert k % 4 == 2
            xyz = (ss, ss * k, p * ss * k)
            x, y, z = xyz
            assert x <= y <= z
            assert 4 * x * y * z == p * (x*y + x*z + y*z)
            ell0 = (k + 2) // 4
            ell1 = (3*k + 2) // 4
            Rmat = ((3, -ell1), (4, -(k+1)))
            assert det2(Rmat) == -1
            triples.append(xyz)
            matrices.append(Rmat)
        assert len(set(triples)) == len(residuals)
        assert len(set(matrices)) == len(residuals)
        cases += 1
        total_certificates += len(residuals)
        if len(residuals) > max_count:
            max_count = len(residuals)
            max_examples = [(p, m, list(residuals))]
        elif len(residuals) == max_count and len(max_examples) < 5:
            max_examples.append((p, m, list(residuals)))

    return {
        'prime_bound': bound,
        'prime_cases': cases,
        'total_diagonal_certificates': total_certificates,
        'max_diagonal_count': max_count,
        'max_count_examples': [
            {'p': p, 'm': m, 'R_values': Rs} for p, m, Rs in max_examples
        ],
        'exceptional_primes_sample': exceptional[:30],
        'exceptional_prime_count': len(exceptional),
    }


def rational_nonintersection_receipt():
    # The proof reduces rationality of two nonzero Lorentz coordinates to one
    # of these three irrational square-class ratios.
    ratios = [sp.sqrt(sp.Rational(3, 2)), 1/sp.sqrt(2), sp.sqrt(3)]
    assert all(x.is_rational is False for x in ratios)
    # The one-coordinate cases reduce to U^2=2/3 or V^2=2.
    assert sp.sqrt(sp.Rational(2, 3)).is_rational is False
    assert sp.sqrt(2).is_rational is False
    return {
        'two_coordinate_obstructions': [str(x) for x in ratios],
        'one_coordinate_obstructions': ['U^2 = 2/3', 'V^2 = 2'],
        'conclusion': 'the exact orthogonal-homothetic defect map has no Q-rational image point',
    }

def main():
    out={'symbolic_lorentz':symbolic_receipt()}

    # Exhaustive fixed-shell bijection and terminal/opening tests.
    shell_cases=oriented=0; morphisms=0; sample=None
    for n in range(5,162,4):
        for R in range(3,n,4):
            if math.gcd(n,R)!=1: continue
            sh=sorted(shell_states(n,R)); ch=list(channel_states(n,R))
            assert sh==sorted((y,z,d,e) for _,_,_,y,z,d,e in ch)
            C={(delta,u,v) for delta,u,v,*_ in ch}
            for idx,(delta,u,v,y,z,d,e) in enumerate(ch):
                assert (n*n//delta,v,u) in C
                assert (n*n//delta,v,u)!=(delta,u,v)
                terminal_data(R,delta,u)
                if idx<2 or (n,R,delta)==(45,7,9):
                    rec=verify_opening_terminal_morphism(n,R,delta,u,(n+R)//4); morphisms+=1
                    if sample is None and not is_prime(n) and delta not in (1,n,n*n):
                        sample={'n':n,'R':R,'delta':delta,'u':u,'v':v,'y':y,'z':z,**rec}
            shell_cases+=1; oriented+=len(ch)
    out.update(shell_bound=161,shell_cases_checked=shell_cases,oriented_states_checked=oriented,
               explicit_GL2_morphisms_checked=morphisms,sample_composite_channel=sample)

    # Prime specialization.
    prime_shells=prime_states=0
    for p in [q for q in PRIMES_2M if q<1000 and q%4==1]:
        for R in range(3,p,4):
            ch=list(channel_states(p,R)); a=(p+R)//4
            E={u for u in divisors(a*a) if (4*u+1)%R==0}
            M={u for u in divisors(a*a) if (4*u+p)%R==0}
            assert {u for delta,u,v,*_ in ch if delta==1}==E
            assert {u for delta,u,v,*_ in ch if delta==p}==M
            assert {(v,u) for delta,u,v,*_ in ch if delta==1}=={
                (u,v) for delta,u,v,*_ in ch if delta==p*p}
            assert len(ch)==2*len(E)+len(M)
            prime_shells+=1; prime_states+=len(ch)
    out.update(prime_bound=1000,prime_shells_checked=prime_shells,
               prime_oriented_states_checked=prime_states)

    # Universal diagonal channel identity in all bounded coprime odd shells.
    diagonal_shells = diagonal_states = 0
    for n in range(5, 162, 4):
        for R in range(3, n, 4):
            if math.gcd(n, R) != 1:
                continue
            a = (n + R) // 4
            states = list(channel_states(n, R))
            actual = {delta for delta, u, v, *_ in states if u == a and v == a}
            expected = {delta for delta in divisors(n*n) if (n + delta) % R == 0}
            assert actual == expected
            for delta in expected:
                k = (n + delta) // R
                assert (a*n*k) % delta == 0
                x, y, z = a, a*k, a*n*k//delta
                assert 4*x*y*z == n*(x*y + x*z + y*z)
                delta2 = n*n//delta
                k2 = (n + delta2)//R
                assert k2*delta == n*k
                assert (a*k2, a*n*k2//delta2) == (z, y)
                diagonal_states += 1
            diagonal_shells += 1
    out.update(general_diagonal_shells_checked=diagonal_shells,
               general_diagonal_states_checked=diagonal_states)

    # Character orthogonality checks.
    ferr=0.0; fcases=0
    for n,R in [(13,3),(17,7),(29,7),(37,11),(45,7),(65,11),(77,19),(101,23),(145,31)]:
        if R>=n or math.gcd(n,R)!=1: continue
        a=(n+R)//4
        for delta in divisors(n*n):
            brute=sum((4*u+delta)%R==0 for u in divisors(a*a))
            calc=fourier_count(n,R,delta)
            ferr=max(ferr,abs(calc.real-brute),abs(calc.imag))
            assert abs(calc.real-brute)<1e-7 and abs(calc.imag)<1e-7
            fcases+=1
    out.update(fourier_channel_counts_checked=fcases,max_fourier_roundoff=ferr)

    # Structural saturation for all hard classes, actual prime examples for one ray.
    hard=[c for c in range(840) if c%12==1 and math.gcd(c,840)==1]
    assert len(hard)==48
    rays=[(1,1),(1,2),(2,3),(5,7)]
    sat=[]; prime_examples=[]
    for r,t in rays:
        for c in hard:
            R,s0,L,p0,Q=saturation_progression(r,t,840,c)
            assert p0%840==c and math.gcd(p0,Q)==1
            sat.append((r,t,c,R,Q))
            if (r,t)==(1,1):
                found=first_progression_prime(p0,Q,R,1000)
                assert found is not None
                p,k=found; s=s0+k*L
                xyz=verify_es(p,R,r,s,t,'E')
                prime_examples.append({'class_mod_840':c,'R':R,'s':s,'p':p,'Q':Q,'xyz':list(xyz)})
    out.update(hard_classes_mod_840=hard,rays_structurally_checked=rays,
               ray_class_progressions_checked=len(sat),actual_prime_examples_checked=len(prime_examples),
               prime_examples=prime_examples[:12])

    # Fixed q=11 diagonal-ray subprogression in every 1 mod 12 class.
    q11_examples=[]
    for c in hard:
        p_res=int(crt([840,11],[c,10],check=True)[0])
        assert math.gcd(p_res,9240)==1
        found=first_progression_prime(p_res,9240,11,2000)
        assert found is not None
        p,jj=found
        ss=(p+11)//4; kk=(p+1)//11
        assert (p+11)%4==0 and (p+1)%11==0
        x,y,z=ss,ss*kk,p*ss*kk
        assert 4*x*y*z==p*(x*y+x*z+y*z)
        assert p%840==c
        q11_examples.append({'class_mod_840':c,'p':p,'s':ss,'k':kk,'xyz':[x,y,z]})
    # Finite union relative-density factors for several residual primes.
    Qset=[11,19,23,31,43]
    num=den=1
    from fractions import Fraction
    complement=Fraction(1,1)
    for q0 in Qset: complement*=Fraction(q0-2,q0-1)
    out.update(q11_fixed_progressions_checked=len(q11_examples),
               q11_examples=q11_examples[:12],
               finite_density_residuals=Qset,
               finite_solved_relative_density=str(1-complement))

    # Opening torsor and defect-one map exact algebra.
    opens=[]
    for r,t in [(1,1),(1,2),(2,3),(3,5),(5,7),(8,13)]:
        for delta in [1,3,5,9,25]:
            x,y,A11,A12,A22=opening_data(r,t,delta)
            for k in range(-5,6):
                xx,yy,B11,B12,B22=opening_data(r,t,delta,k)
                assert B11*B22-B12*B12==-delta
                # exact quadratic torsor formula
                assert B11==A11-2*k*r*x-k*k*r*r
                assert B12==A12-k*(r*y+t*x)-k*k*r*t
                assert B22==A22-2*k*t*y-k*k*t*t
            # raw and native discriminants
            assert A11*A22-A12*A12==-delta
            assert 2*A11>0
            opens.append({'ray':[r,t],'delta':delta,'w':[x,y],
                          'A':[[A11,A12],[A12,A22]],
                          'raw_period_triple':[str(A11),f'{A12}/sqrt(6)',str(A22)],
                          'det':-delta})
    out.update(bezout_opening_torsors_checked=len(opens),opening_examples=opens[:10])

    out['diagonal_ray_exact_count'] = verify_diagonal_ray_counts(5000)
    out['rational_nonintersection'] = rational_nonintersection_receipt()

    path=Path(__file__).with_name('verification_results.json')
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__': main()
