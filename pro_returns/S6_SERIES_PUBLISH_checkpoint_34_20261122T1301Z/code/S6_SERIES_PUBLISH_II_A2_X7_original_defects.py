#!/usr/bin/env python3
"""Post-release exact checks for every extra local bound retained in 02X7.

The initial-weight calculation uses all allowed quadratic monomials. Terms
of total degree at least three have gradient order at least six and cannot
create an order-six two-by-two minor; that bound is proved in the record.
"""
import itertools
import json
import sympy as s


def valuation(poly, t):
    poly = s.Poly(s.expand(poly), t)
    return None if poly.is_zero else min(power[0] for power, coeff in poly.terms() if coeff)


def main():
    x, y, z, t = s.symbols('x y z t')
    delta, tau, r, ell, q = s.symbols('delta tau r ell q', integer=True)
    m, dslack, tslack = s.symbols('m dslack tslack', integer=True)
    m1, m2 = s.symbols('m1 m2', integer=True)
    defect = delta + tau - r
    assert s.expand(defect.subs({tau: ell+q}) - (delta+ell+q-r)) == 0
    plane = s.expand(defect.subs({tau: 2*delta+r+2*delta}))
    assert plane == 5*delta
    unibranch = s.expand(defect.subs({delta:m-1+dslack,tau:2*m+tslack,r:m-1}))
    assert unibranch == 2*m+dslack+tslack
    two_branch = s.expand(defect.subs({delta:m1+m2-1,tau:2*(m1+m2),r:m1+m2-2}))
    assert two_branch == 2*m1+2*m2+1

    quadratic = [x*x, x*y, x*z, y*y, y*z, z*z]
    param = {x:t**3, y:t**4, z:t**5}
    weights = [valuation(term.subs(param),t) for term in quadratic]
    assert weights == [6,7,8,8,9,10]
    assert weights.count(6)==weights.count(7)==1
    allowed = quadratic[2:]
    grad = s.Matrix([[s.diff(term,v).subs(param) for v in (x,y,z)] for term in allowed])
    initial = grad.applyfunc(lambda p:s.expand(p).coeff(t,3))
    assert initial.rank()==1
    minors=[]
    for rows in itertools.combinations(range(grad.rows),2):
        for cols in itertools.combinations(range(3),2):
            det=s.expand(grad.extract(rows,cols).det())
            value=valuation(det,t)
            if value is not None:
                minors.append({'rows':list(rows),'columns':list(cols),'determinant':str(det),'order':value})
    assert min(x['order'] for x in minors)==7

    cubic=[]
    for i in range(4):
        for j in range(4-i):
            k=3-i-j
            cubic.append(x**i*y**j*z**k)
    cubic_gradient_orders=[]
    for term in cubic:
        cubic_gradient_orders.extend(valuation(s.diff(term,v).subs(param),t) for v in (x,y,z) if s.diff(term,v)!=0)
    assert min(cubic_gradient_orders)==6
    # Every n>=3 is represented by residue modulo3, with base3,4,5.
    residue_bases={0:3,1:4,2:5}
    assert {base%3 for base in residue_bases.values()} == {0,1,2}

    print(json.dumps({
        'tag':'02X7',
        'phase':'after target-proof release; retained original items3-8',
        'method':'Symbolic substitution of exact length identities and complete degree-two monomial/gradient enumeration, with a written all-higher-degree bound.',
        'tau_exact_relation':'tau = ell + q',
        'plane_defect':str(plane),
        'unibranch_defect_with_nonnegative_slacks':str(unibranch),
        'two_branch_defect_lower_bound':str(two_branch),
        'quadratic_monomials':[str(v) for v in quadratic],
        'quadratic_initial_weights':weights,
        'allowed_quadratics_after_unique_weights_removed':[str(v) for v in allowed],
        'allowed_gradient_matrix':[[str(v) for v in row] for row in grad.tolist()],
        'order_three_initial_matrix':initial.tolist(),
        'order_three_initial_rank':initial.rank(),
        'all_nonzero_two_by_two_minors':minors,
        'minimum_minor_order':min(v['order'] for v in minors),
        'minimum_degree_three_gradient_order':min(cubic_gradient_orders),
        'all_higher_degree_bound':'Total degree d>=3 has gradient order at least 3(d-1)>=6. Pairing with a gradient entry of order at least3 gives minor terms of order at least9. Higher terms of x(t),y(t),z(t) do not alter the rank-one coefficient at order3.',
        'semigroup_residue_bases':residue_bases,
        'semigroup_reason':'When multiplicity3 and delta2 force the only missing orders to be1,2, every n>=3 has one of bases3,4,5 plus a nonnegative multiple of3.',
        'limitations':'The program checks algebra once the stated analytic length and valuation facts are supplied. It does not replace the written finite-duality or semigroup-filtration argument.',
        'all_assertions_passed':True,
    },indent=2,default=str))


if __name__=='__main__':
    main()
