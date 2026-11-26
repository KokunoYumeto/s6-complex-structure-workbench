#!/usr/bin/env python3
"""Exact algebra in the statement-first 02X7 conductor argument.

This checks the matrices and identities supplied to it. The analytic depth,
duality, curve-classification and valuation arguments are in the derivation;
they are not certified by sampling. No manuscript proof is read by this code.
"""
import json
import sympy as s


def main():
    t, a, b = s.symbols('t a b')
    # Branch maps (t,0), (0,t), (t,t); columns are x^2, xy, y^2.
    quadratic = s.Matrix([[1, 0, 0], [0, 0, 1], [1, 1, 1]])
    assert quadratic.det() == -1
    assert quadratic * quadratic.inv() == s.eye(3)
    first = s.Matrix([[1, 0], [0, 1], [1, 1]])
    annihilator = s.Matrix([[-1, -1, 1]])
    assert annihilator * first == s.zeros(1, 2)
    # A conductor first jet must survive all three branch-idempotent tests.
    restrictions = []
    for i in range(3):
        idem = s.zeros(3)
        idem[i, i] = 1
        restrictions.append(annihilator * idem * first)
    restriction_matrix = s.Matrix.vstack(*restrictions)
    assert restriction_matrix.rank() == 2
    assert restriction_matrix.nullspace() == []

    delta, ramification, ell, q = s.symbols('delta R ell q', integer=True)
    deg_B = 0
    deg_omega_E = -2
    deg_V = deg_B - (deg_omega_E - ramification)
    deg_F = deg_V - ell
    chi_F = deg_F + 2  # rank(F) = 2 on P^1
    chi_M = chi_F - q
    chi_C = 1 - delta
    chi_double = s.expand(chi_C + chi_M)
    assert chi_double == 5 - delta + ramification - ell - q
    plane_contribution = s.expand(delta + 2*delta + 2*delta)
    assert plane_contribution == 5*delta

    # These nonnegative slack parameters express whole infinite cases.
    k, u, v, w, z = s.symbols('k u v w z', integer=True, nonnegative=True)
    cases = {
        'ordinary_node_and_no_other_singularity': s.Integer(5),
        'ordinary_node_and_at_least_one_other_singularity': 5 + (2 + k),
        'planar_two_branch_delta_at_least_two': 5*(2+k) + u,
        # delta >= 2; m1 >= 2; m2 >= 1; q and extra contributions >= 0.
        'nonplanar_two_branch': (2+k) + ((2+u)+1) + ((1+v)+1) + w + z,
    }
    chi_cases = {name: s.expand(5-value) for name, value in cases.items()}
    assert chi_cases['ordinary_node_and_no_other_singularity'] == 0
    assert s.expand(chi_cases['ordinary_node_and_at_least_one_other_singularity'] + 2) == -k
    assert s.expand(chi_cases['planar_two_branch_delta_at_least_two'] + 5) == -5*k-u
    assert s.expand(chi_cases['nonplanar_two_branch'] + 2) == -k-u-v-w-z

    c, graph_b = s.symbols('c graph_b', integer=True)
    e_curve = c + 1 - graph_b
    assert e_curve.subs({c:1, graph_b:1}) == 1

    print(json.dumps({
        'tag': '02X7',
        'method': 'Exact symbolic matrix inverses, nullspaces, determinant and polynomial identities; exhaustive cases are parameterized by nonnegative integer slacks.',
        'quadratic_branch_coefficient_matrix': quadratic.tolist(),
        'quadratic_determinant': str(quadratic.det()),
        'quadratic_inverse': quadratic.inv().tolist(),
        'first_jet_branch_coefficient_matrix': first.tolist(),
        'first_jet_annihilator': annihilator.tolist(),
        'idempotent_restriction_matrix': restriction_matrix.tolist(),
        'idempotent_restriction_rank': restriction_matrix.rank(),
        'idempotent_restriction_nullspace': [],
        'degrees_and_euler': {name: str(value) for name, value in {
            'deg_B': deg_B, 'deg_omega_P1': deg_omega_E, 'deg_V': deg_V,
            'deg_F': deg_F, 'chi_F': chi_F, 'chi_M': chi_M,
            'chi_C': chi_C, 'chi_symbolic_double': chi_double,
            'planar_local_contribution': plane_contribution,
            'rational_curve_graph_euler': e_curve}.items()},
        'exhaustive_case_contributions': {name: str(value) for name,value in cases.items()},
        'exhaustive_case_euler_values': {name: str(value) for name,value in chi_cases.items()},
        'conclusion': 'The supplied valuation/duality cases force chi = 0 or chi <= -2, excluding -1.',
        'limitations': 'Analytic conductor purity, topology, finite canonical duality, and the local valuation bounds require the written proof. This program claims no numerical classification or standalone theorem certificate.',
        'all_assertions_passed': True,
    }, indent=2, default=str))


if __name__ == '__main__':
    main()
