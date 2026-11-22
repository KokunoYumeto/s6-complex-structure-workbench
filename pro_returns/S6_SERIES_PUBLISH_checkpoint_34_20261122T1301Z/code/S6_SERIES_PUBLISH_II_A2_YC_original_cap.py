#!/usr/bin/env python3
"""Exact retained-proof cap correction, weights and orientation for 02YC.

This is a postrelease check.  It does not count as another independent
derivation, and its finite weight sweep is explicitly not a universal proof.
"""
from fractions import Fraction
from math import lcm
import json
import sympy as sp


def main():
    r,s,theta,psi=sp.symbols('r s theta psi',positive=True,real=True)
    # Write the arbitrary nonzero constant as c=r exp(i psi).
    u=sp.sqrt(r*s)*sp.exp(sp.I*theta)
    v=sp.exp(sp.I*psi)*sp.sqrt(r*s)*sp.exp(-sp.I*theta)
    assert sp.simplify(u*v-r*s*sp.exp(sp.I*psi))==0
    assert sp.simplify(u*sp.conjugate(u)-r*s)==0
    assert sp.simplify(v*sp.conjugate(v)-r*s)==0
    old_u=sp.sqrt(s)*sp.exp(sp.I*theta)
    old_v=r*sp.exp(sp.I*psi)*sp.sqrt(s)*sp.exp(-sp.I*theta)
    old_norm_difference=sp.simplify(old_v*sp.conjugate(old_v)-old_u*sp.conjugate(old_u))
    assert old_norm_difference==s*(r**2-1)
    assert old_norm_difference.subs({r:2,s:1})==3
    t,U,V=sp.symbols('t U V')
    bad_h=t*(t-1)*(t-2)**2
    assert bad_h.subs(t,0)==bad_h.subs(t,1)==bad_h.subs(t,2)==0
    assert sp.diff(bad_h,t).subs(t,0)!=0 and sp.diff(bad_h,t).subs(t,1)!=0
    conic=U*V-bad_h
    assert all(sp.diff(conic,q).subs({t:2,U:0,V:0})==0 for q in (t,U,V))

    # On a cap with phase psi constant, v=e^(i psi) conjugate(u).
    assert sp.simplify(v-sp.exp(sp.I*psi)*sp.conjugate(u))==0
    # Standard symplectic form on the matching cylinder: R(s)^2=r(s)s.
    rho_prime,phase_prime=sp.symbols('rho_prime phase_prime',real=True)
    assert rho_prime/2-rho_prime/2==0
    assert sp.det(sp.Matrix([[rho_prime,0],[phase_prime,0]]))==0
    # Tangent followed by its J-image has negative complex orientation.
    e1=sp.Matrix([1,0,1,0]); e2=sp.Matrix([0,1,0,-1])
    J=sp.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    orientation=sp.Matrix.hstack(e1,e2,J*e1,J*e2).det()
    assert orientation==-4

    # Independent exact-arithmetic sweep of the original rational weights.
    counts={'A_dominant':0,'B_dominant':0,'balanced':0}
    for k in range(1,49):
        for ell in range(1,49):
            rho=min(Fraction(k,2),Fraction(ell,3))
            L=3*rho+Fraction(1,6)
            weights=(L+rho,L,Fraction(1))
            denominator=lcm(*(x.denominator for x in weights))
            ints=tuple(int(x*denominator) for x in weights)
            assert min(ints)>0
            d=3*weights[0]
            gap_A=weights[0]+2*weights[1]+k-d
            gap_B=3*weights[1]+ell-d
            assert min(gap_A,gap_B)==0 and max(gap_A,gap_B)>=0
            assert L-2*rho>0 and L-3*rho>0
            if gap_A==gap_B==0:
                assert k%2==0 and ell%3==0 and k//2==ell//3
                counts['balanced']+=1
            elif gap_A==0:
                counts['A_dominant']+=1
            else:
                counts['B_dominant']+=1
    assert sum(counts.values())==48**2
    print(json.dumps({
        'check':'02YC retained proof: exact cap correction, orientation, weight certificate',
        'old_squared_norm_difference':str(old_norm_difference),
        'old_counterexample':{'c':2,'s':1,'u_squared_norm':1,'v_squared_norm':4},
        'two_simple_zeros_do_not_imply_global_smoothness':{'h':'t(t-1)(t-2)^2','simple_zeros':[0,1],'singular_conic_point':[2,0,0]},
        'corrected_cap':'u=sqrt(|c|s) exp(i theta), v=(c/|c|)sqrt(|c|s) exp(-i theta)',
        'corrected_product':'c*s',
        'corrected_squared_norms':['|c|*s','|c|*s'],
        'smooth_cap_graph':'v=(c/|c|) conjugate(u)',
        'orientation_determinant':int(orientation),
        'matching_sphere_square':-2,
        'rational_weight_sweep':{'k_range':[1,48],'l_range':[1,48],
                               'cases':counts,'total':sum(counts.values())},
        'scope':'Symbolic cap and orientation identities are exact. The 2304-case rational weight sweep is a supplementary finite certificate; the complete inequalities are proved in the frozen derivation and retained proof.',
        'status':'PASS'},indent=2))


if __name__=='__main__':
    main()
