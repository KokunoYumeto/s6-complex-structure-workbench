#!/usr/bin/env python3
"""Exact calculations in the statement-first 02XA derivation.

The analytic proof supplies the line subbundles, torsion-free quotients,
finite lengths and intersection signs.  These checks use Chern characters
and a universal formal intersection polynomial, plus both blowup charts.
They do not read a target proof or an earlier target program.
"""
import json
import sympy as s


def main():
    ell,e,z0,z1,h=s.symbols('ell e z0 z1 h')
    j=e-ell
    j1=-e
    assert s.expand(ell+j+j1)==0
    # In K-theory B=Lbar+J+J1-F0-(J1 tensor O_Z1).  Finite-length sheaves
    # contribute their length in degree four, not its negative.
    characters=sum(1+a*h+a*a*h*h/2 for a in [ell,j,j1])-(z0+z1)*h*h
    coefficient=s.expand(characters).coeff(h,2)
    sum_squares=s.expand(ell*ell+j*j+j1*j1)
    assert s.expand(coefficient-(sum_squares/2-z0-z1))==0
    via_quotients=s.expand(ell*ell-j*j1)
    assert s.expand(via_quotients-sum_squares/2)==0

    # Riemann--Roch and the square-zero polarization calculation.
    m,aa,ka,chi0,t,ae=s.symbols('m aa ka chi0 t ae')
    rr=chi0+(m*m*aa-m*ka)/2
    assert s.Poly(rr,m).LC()==aa/2
    polarized=aa+2*t*ae
    assert s.diff(polarized,t)==2*ae

    # Pair the determinant class with a pulled-back canonical class.
    n,k0r=s.symbols('n k0r')
    pairing=s.expand(-(-n)+k0r)
    assert pairing==n+k0r

    # Integral adjunction cases on the minimal model.
    genus,q=s.symbols('genus q',integer=True,nonnegative=True)
    pa_ge1=1+genus
    minus_square_ge1=1+q
    canonical_positive_genus=s.expand(2*pa_ge1-2+minus_square_ge1)
    assert canonical_positive_genus==2*genus+q+1
    minus_square_rational=2+q
    canonical_rational=s.expand(-2+minus_square_rational)
    assert canonical_rational==q

    # A blowup pulls the canonical class to K+E.  If D'=pullback(D)+cE,
    # torsion of K'+D' makes its intersection with E equal zero.
    c,mu,a=s.symbols('c mu a')
    exceptional_pairing=-(1+c)
    assert s.solve(s.Eq(exceptional_pairing,0),c)==[-1]
    assert s.solve(s.Eq(a-mu,-1),a)==[mu-1]

    # Actual pushforward of a lifted vector column in both blowup charts.
    u,v,alpha,beta=s.symbols('u v alpha beta')
    # alpha and beta denote the original coefficients after substitution.
    charts=[
        (s.Matrix([u,u*v]),s.Matrix([u*alpha,beta-v*alpha]),u),
        (s.Matrix([u*v,v]),s.Matrix([alpha-u*beta,v*beta]),v),
    ]
    chart_output=[]
    for coordinate_map,column,factor in charts:
        jacobian=coordinate_map.jacobian([u,v])
        pushed=s.simplify(jacobian*column)
        assert pushed==factor*s.Matrix([alpha,beta])
        chart_output.append({
            'coordinate_map':[str(x) for x in coordinate_map],
            'holomorphic_lift_before_common_factor_division':[str(x) for x in column],
            'pushforward':[str(x) for x in pushed],
            'exceptional_factor':str(factor),
        })

    print(json.dumps({
        'tag':'02XA',
        'phase':'before target-proof release',
        'chern_roots':['ell','e-ell','-e'],
        'first_chern_class':0,
        'K_theory_identity':'[B]=[Lbar]+[J]+[J1]-[F0]-[J1 tensor O_Z1]',
        'second_chern_character':str(coefficient),
        'sum_of_line_squares':str(sum_squares),
        'quotient_chern_identity_left_side':str(via_quotients),
        'resulting_identity':'(ell^2+(e-ell)^2+e^2)/2=z0+z1',
        'sign_application':'Each line square is <=0 and z0,z1>=0; hence every square and both lengths are zero.',
        'riemann_roch_polynomial':str(rr),
        'riemann_roch_leading_coefficient':str(s.Poly(rr,m).LC()),
        'polarized_square_when_e_square_zero':str(polarized),
        'polarization_linear_coefficient':str(s.diff(polarized,t)),
        'pulled_back_canonical_pairing':str(pairing),
        'adjunction_pa_at_least_one':str(canonical_positive_genus),
        'adjunction_smooth_rational_minimal_curve':str(canonical_rational),
        'blowup_pole_relative_coefficient':-1,
        'blowup_pole_exceptional_multiplicity':'mu-1',
        'foliation_blowup_charts':chart_output,
        'limitations':'This program checks the exact algebraic identities. It does not prove foliation existence, coherent saturation, Riemann--Roch, meromorphic descent, adjunction, the primary classification inputs, or effectiveness of the determinant divisor. Those hypotheses and maps are proved or precisely sourced in the complete derivation.',
        'all_assertions_passed':True,
    },indent=2))


if __name__=='__main__':
    main()
