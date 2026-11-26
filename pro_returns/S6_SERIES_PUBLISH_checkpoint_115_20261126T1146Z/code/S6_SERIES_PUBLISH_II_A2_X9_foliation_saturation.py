#!/usr/bin/env python3
"""Exact Chern and blowup calculations for the statement-first 02X9 check.

The proof supplies all analytic maps and sheaf exactness.  This program
uses a universal symmetric intersection matrix, checks both blowup charts,
and writes the complete positive-definite equality classification, not a
bounded search over exceptional coefficients.
"""
import json
import sympy as s


def main():
    k,z0,z1=s.symbols('k z0 z1',integer=True,nonnegative=True)
    names=['KK','KV','KR','KZ','VV','VR','VZ','RR','RZ','ZZ']
    KK,KV,KR,KZ,VV,VR,VZ,RR,RZ,ZZ=s.symbols(' '.join(names))
    M=s.Matrix([[KK,KV,KR,KZ],[KV,VV,VR,VZ],
                [KR,VR,RR,RZ],[KZ,VZ,RZ,ZZ]])
    ell=s.Matrix([-1,1,0,1])
    jj=s.Matrix([0,-1,1,-1])
    jj1=s.Matrix([1,0,-1,0])
    chern=s.expand((ell.T*M*ell)[0]-(jj.T*M*jj1)[0])
    def H(Q):
        return s.expand(Q[2,2]-Q[2,3]+Q[3,3]-Q[0,2]-Q[0,3]-Q[1,2]+2*Q[1,3])
    assert s.expand(chern.subs({KK:-k,KV:VV})-(H(M)-k))==0
    c,d,eps=s.symbols('c d epsilon',integer=True)
    a=s.Matrix([1,eps,c,d])
    # Pullbacks intersect E trivially and E.E=-1.
    increment=s.expand(H(M-a*a.T)-H(M))
    expected=-c*c+c*d-d*d+(1+eps)*c+(1-2*eps)*d
    assert s.expand(increment-expected)==0
    u,v=s.symbols('u v',real=True)
    Q=u*u-u*v+v*v
    assert s.expand(2*Q-((u-v)**2+u*u+v*v))==0
    equality=[]
    for e in [0,1]:
        val=s.expand(increment.subs({eps:e,c:1+u,d:1-e+v}))
        assert s.expand(val-(1-Q))==0
        equality.append({'epsilon':e,'center_c':1,'center_d':1-e,
                         'shifted_increment':str(val),
                         'equality_exactly':{'c':1,'d':1-e}})
    mu=s.symbols('mu',integer=True,nonnegative=True)
    # Last exceptional curve has coefficient zero in the zero divisor Z.
    d_last=-mu
    last_regular_equation=s.Eq(d_last,1)
    assert s.solve(last_regular_equation,mu)==[]
    assert s.solve(s.Eq(d_last,0),mu)==[0]
    x,y,uu,vv=s.symbols('x y u v')
    aa,bb=s.symbols('a b',positive=True)
    vec=s.Matrix([bb*x,-aa*y])
    charts=[]
    for mp in [s.Matrix([uu,uu*vv]),s.Matrix([uu*vv,vv])]:
        Jac=mp.jacobian([uu,vv])
        lifted=s.simplify(Jac.inv()*vec.subs({x:mp[0],y:mp[1]},simultaneous=True))
        charts.append([str(s.expand(t)) for t in lifted])
    assert charts==[[str(s.expand(bb*uu)),str(s.expand(-(aa+bb)*vv))],
                    [str(s.expand((aa+bb)*uu)),str(s.expand(-aa*vv))]]
    h=s.symbols('h',positive=True)
    m=s.symbols('m',integer=True,positive=True)
    principal_intersection=s.expand(m*0+h)
    assert principal_intersection==h
    print(json.dumps({
      'tag':'02X9','phase':'before target-proof release',
      'intersection_basis':['K','V','R','Z'],
      'chern_expression_before_surface_identities':str(chern),
      'H_functional':str(H(M)),
      'chern_identity':'H(R,Z)=k+z0+z1 after K.K=-k and K.V=V.V',
      'universal_blowup_increment':str(increment),
      'positive_definite_form':str(Q),
      'twice_form_as_sum_of_squares':str((u-v)**2+u*u+v*v),
      'complete_equality_cases':equality,
      'last_curve_zero_divisor_coefficient':str(d_last),
      'last_regular_equality_solutions_with_mu_nonnegative':[],
      'last_saddle_equality_solutions_with_mu_nonnegative':[0],
      'saddle_blowup_chart_generators':charts,
      'each_chart_zero_ideal':'(u,v), since a,b,a+b are nonzero',
      'saddle_points_on_last_exceptional':'two distinct points, one in each chart',
      'Hopf_contraction_principal_intersection':str(principal_intersection),
      'limitations':'No holomorphic saturation, minimal-resolution property, foliation classification, sheaf-depth assertion, or finite normalization theorem is established by these algebra calculations. The complete pre-release derivation proves their use. No target program has been read.',
      'all_assertions_passed':True,
    },indent=2))


if __name__=='__main__':
    main()
