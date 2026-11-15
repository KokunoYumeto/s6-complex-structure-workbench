#!/usr/bin/env python3
"""Exact good-modulus ternary Gauss identity; variation-loss countermodel.

The abstract countermodel is not a family of Kloosterman sums.  Its purpose
is to disprove the inference from an untwisted partial-sum bound alone to
the twisted bound needed after a sharp polytope transform.
"""
import json
from math import gcd, isqrt
from pathlib import Path
import sympy as sp
from flint import arb, ctx
from B_A5_salie_audit import jacobi, salie_coeffs

ctx.prec = 192
BASE = Path(__file__).resolve().parents[1]


def conv(a,b):
    q=len(a)
    out=[0]*q
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:
                    out[(i+j)%q]+=x*y
    return out


def gauss(A,B,q):
    out=[0]*q
    for x in range(q):
        out[(A*x*x+B*x)%q]+=1
    return out


def main():
    X=sp.Symbol('X')
    moduli=(5,7,11,13,17,19,23,25,29,31,35,49)
    vectors=((1,0,0),(0,1,0),(0,0,1),(1,2,3),(2,-1,4))
    for q in moduli:
        assert gcd(q,6)==1
        G=gauss(1,0,q)
        G3=conv(conv(G,G),G)
        Phi=sp.Poly(sp.cyclotomic_poly(q,X),X,domain=sp.ZZ)
        for c in vectors:
            lhs=[0]*q
            for a in range(q):
                if gcd(a,q)>1:
                    continue
                v=conv(conv(gauss(a,c[0],q),gauss(-3*a,c[1],q)),gauss(-18*a,c[2],q))
                for k,z in enumerate(v):
                    lhs[(k+2*a)%q]+=z
            H=-18*c[0]**2+6*c[1]**2+c[2]**2
            rhs=conv(G3,salie_coeffs(2,pow(72,-1,q)*H,q))
            delta=[a-jacobi(6,q)*b for a,b in zip(lhs,rhs)]
            P=sp.Poly.from_list(list(reversed(delta)),X,domain=sp.ZZ)
            assert P.rem(Phi).is_zero
    print('PASS: ternary Gauss identity exactly modulo Phi_q for',len(moduli)*len(vectors),'(q,c) pairs')
    print('q =',moduli,'; vectors =',vectors)
    print('S_q(c)=Jacobi(6,q)*G(1;q)^3*T(2,inverse(72)*H(c);q), H=-18c1^2+6c2^2+c3^2')

    rows=[]
    for Q in (16,100,10000):
        D=Q*isqrt(Q)
        assert isqrt(Q)**2==Q
        im=arb(0)
        for q in range(Q+1,2*Q+1):
            im+=(2*arb.pi()*D/(q*(q-1))).sin()
        lower=2*arb(Q).sqrt()
        assert im>lower
        row={'Q':Q,'D':D,'twisted_sum_imaginary_part':str(im),
             'proved_lower_bound':str(lower),
             'untwisted_interval_sum_bound':2,
             'individual_bound':str(2*arb.pi()*D/(Q*(Q+1)))}
        rows.append(row)
        print(json.dumps(row,sort_keys=True))
    print('PASS: abstract untwisted-bound countermodel; no claim that these a_q are Kloosterman coefficients')
    (BASE/'records/B_A5_delta_audit.json').write_text(json.dumps({'gauss_identity_checks':60,'models':rows},indent=2)+'\n')


if __name__=='__main__':
    main()
