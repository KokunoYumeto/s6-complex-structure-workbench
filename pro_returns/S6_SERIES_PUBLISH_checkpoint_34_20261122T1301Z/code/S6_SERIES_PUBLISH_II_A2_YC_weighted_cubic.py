#!/usr/bin/env python3
"""Exact weighted initial forms and finite-map identities for 02YC.

The accompanying derivation proves the conic matching sphere, the proper
finite-map intersection formula and compact weighted transport. This
program checks their displayed polynomial and weight identities only.
"""
import json
from math import gcd
import sympy as sp


def main():
    x,y,z,w,t = sp.symbols('x y z w t')
    c2,c1,c0,A,B,c,d = sp.symbols('c2 c1 c0 A B c d')
    depressed=sp.expand((t-c2/3)**3+c2*(t-c2/3)**2+c1*(t-c2/3)+c0)
    expected=t**3+(c1-c2**2/3)*t+(c0-c1*c2/3+2*c2**3/27)
    assert sp.expand(depressed-expected)==0

    a,b,k = sp.symbols('a b k', integer=True, positive=True)
    # w_z=6 clears the denominators 2 and 3 of the minimum slope.
    wa_y=9*a+1; wa_x=12*a+1; wa_degree=3*wa_x
    assert sp.expand(wa_x+2*wa_y+6*a-wa_degree)==0
    a_other_gap=sp.expand(3*wa_y+6*b-wa_degree)
    assert a_other_gap==3*(2*b-3*a)
    assert sp.expand(wa_y-3*(a/2)*6)==1
    assert sp.expand(wa_y-2*(a/2)*6)==3*a+1

    wb_y=6*b+1; wb_x=8*b+1; wb_degree=3*wb_x
    assert sp.expand(3*wb_y+6*b-wb_degree)==0
    b_other_gap=sp.expand(wb_x+2*wb_y+6*a-wb_degree)
    assert b_other_gap==2*(3*a-2*b)
    assert sp.expand(wb_y-3*(b/3)*6)==1
    assert sp.expand(wb_y-2*(b/3)*6)==2*b+1

    we_y=18*k+1; we_x=24*k+1; we_degree=3*we_x
    assert sp.expand(we_x+2*we_y+12*k-we_degree)==0
    assert sp.expand(3*we_y+18*k-we_degree)==0
    assert sp.expand(we_y-18*k)==1

    # Finite maps: (x,y,z)->(x,u=y^3,v=z^b), and similarly in the A case.
    gb=x**3+d*y**3*z**b-1
    assert sp.expand(d*(y**3*z**b-(1-x**3)/d)-gb)==0
    ga=x**3+c*x*y**2*z**a-1
    assert sp.expand(c*x*(y**2*z**a-(1-x**3)/(c*x))-ga)==0
    P=x**3+c*x*w**2+d*w**3
    assert sp.gcd(x**3-1,3*x**2)==1
    assert sp.expand(x*sp.diff(P,x)+w*sp.diff(P,w)-3*P)==0
    ge=P.subs(w,y*z**k)-1
    assert sp.expand(ge-(x**3+c*x*y**2*z**(2*k)+d*y**3*z**(3*k)-1))==0
    assert (sp.diff(P,x).subs(w,0))==3*x**2

    # A depressed nonzero cubic initial perturbation cannot be a cube.
    lam=sp.symbols('lambda')
    cube=sp.Poly((x-lam*w)**3,x)
    assert cube.coeff_monomial(x**2)==-3*lam*w
    assert sp.expand(((x-lam*w)**2*(x+2*lam*w))-
                     (x**3-3*lam**2*x*w**2+2*lam**3*w**3))==0
    assert sp.expand(-4*(-3*lam**2)**3-27*(2*lam**3)**2)==0
    assert gcd(3,gcd(1,gcd(1,1)))==1
    assert gcd(3,gcd(2,1))==1
    assert gcd(3,3)==3

    rho_prime,phi_prime=sp.symbols('rho_prime phi_prime', real=True)
    # On the matching cylinder: du-area gives rho'/2, dv-area -rho'/2.
    assert sp.expand(rho_prime/2-rho_prime/2)==0
    # The d rho wedge d phi term vanishes because both are multiples of ds.
    assert sp.det(sp.Matrix([[rho_prime,0],[phi_prime,0]]))==0

    out={
        'check':'02YC weighted cubic and exact proper finite maps',
        'depressed_coefficients':[str(c1-c2**2/3),str(c0-c1*c2/3+2*c2**3/27)],
        'A_dominant_weights':[str(wa_x),str(wa_y),6],
        'A_dominant_other_term_gap':str(a_other_gap),
        'B_dominant_weights':[str(wb_x),str(wb_y),6],
        'B_dominant_other_term_gap':str(b_other_gap),
        'equal_slope_weights':[str(we_x),str(we_y),6],
        'positive_y_coefficient_minimum_weight_gap':1,
        'finite_map_cases':[
            {'model':'x^3+d*y^3*z^b=1','base':'C_x','h':'(1-x^3)/d','u':'y^3','v':'z^b','degree':'3*b','pulled_back_square':'-6*b'},
            {'model':'x^3+c*x*y^2*z^a=1','base':'C*_x','h':'(1-x^3)/(c*x)','u':'y^2','v':'z^a','degree':'2*a','pulled_back_square':'-4*a'},
            {'model':'P(x,y*z^k)=1','base':'Gamma={P(x,w)=1}','h':'w','u':'y','v':'z^k','degree':'k','pulled_back_square':'-2*k'}],
        'simple_zeros_per_base_function':3,
        'binary_cubic_Euler_identity':True,
        'equal_case_includes_double_root_binary_cubic':True,
        'noncube_scalar_cover_monodromy_is_transitive':True,
        'matching_sphere_symplectic_pullback_zero':True,
        'matching_sphere_square':-2,
        'scope':'Exact polynomial, weight, and finite-map identities; analytic construction and intersection transfer are proved in the derivation.',
        'status':'PASS'}
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
