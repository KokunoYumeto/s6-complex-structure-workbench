"""Exact component-supported correction search for all 21 MW=Z profiles.

This is a finite integral Picard-lattice calculation.  It does not yet
claim a cap homology algorithm for the newly permitted initial data.
"""
from pathlib import Path
from functools import lru_cache
from math import gcd, lcm
import json
import sympy as s
import manifolds_general_initial as G

ROOT = Path(__file__).resolve().parent


def component_matrix(kind):
    mult, perm, labels = G.component_geometry(kind)
    size = len(mult)
    J = -2 * s.eye(size)
    if kind in ['I1', 'II']:
        J = s.zeros(1)
    elif kind == 'III':
        J = s.Matrix([[-2, 2], [2, -2]])
    else:
        if kind.startswith('I') and kind[1:].isdigit():
            edges = [(i, (i + 1) % size) for i in range(size)]
        elif kind == 'IV':
            edges = [(0, 1), (1, 2), (2, 0)]
        elif kind == 'IV*':
            edges = [(0, 3), (1, 4), (2, 5), (3, 6), (4, 6), (5, 6)]
        elif kind == 'III*':
            chain = [0, 2, 4, 6, 5, 3, 1]
            edges = list(zip(chain, chain[1:])) + [(6, 7)]
        elif kind.startswith('I') and kind.endswith('*'):
            n = int(kind[1:-1])
            edges = [(0, 4), (1, 4), (2, n + 4), (3, n + 4)]
            edges += [(i, i + 1) for i in range(4, n + 4)]
        else:
            raise ValueError(kind)
        for i, j in edges:
            J[i, j] += 1
            J[j, i] += 1
    T = s.zeros(size)
    for j, i in enumerate(perm):
        T[i, j] = 1
    assert J * s.Matrix(mult) == s.zeros(size, 1)
    assert T.T * J * T == J
    assert T * s.Matrix(mult) == s.Matrix(mult)
    assert J.rank() == size - 1
    return J, T, labels, mult


@lru_cache(maxsize=None)
def solve_local(kind, p, q):
    J, T, labels, mult = component_matrix(kind)
    c = s.eye(J.rows)[:, labels[p]] - s.eye(J.rows)[:, labels[0]]
    difference = T ** q - s.eye(J.rows)
    A, rhs = difference * J, -difference * c
    diagonal, left, right, rank = G.decomp(A)
    transformed = left * rhs
    assert left * A * right == diagonal
    obstruction = []
    for j in range(rank):
        if transformed[j] % diagonal[j, j]:
            obstruction.append({'row': j, 'diagonal': int(diagonal[j, j]),
                                'transformed_rhs': int(transformed[j])})
    for j in range(rank, A.rows):
        if transformed[j]:
            obstruction.append({'row': j, 'diagonal': 0,
                                'transformed_rhs': int(transformed[j])})
    try:
        correction = G.integer_solution(A, rhs)
    except ValueError:
        assert obstruction
        return {'kind': kind, 'p': p, 'q': q, 'exists': False,
                'integer_smith_obstruction': obstruction}
    assert not obstruction
    corrected = c + J * correction
    assert difference * corrected == s.zeros(J.rows, 1)
    assert (s.Matrix(mult).T * corrected)[0] == 0
    kernel = G.ikernel(A)
    assert difference * kernel == s.zeros(J.rows, kernel.cols)
    invariant_kernel = G.ikernel(difference)
    assert A * invariant_kernel == s.zeros(J.rows, invariant_kernel.cols)
    assert kernel.cols == invariant_kernel.cols
    return {'kind': kind, 'p': p, 'q': q, 'exists': True,
            'initial_multidegree': list(map(int, c)),
            'vertical_coefficients': list(map(int, correction)),
            'corrected_multidegree': list(map(int, corrected)),
            'all_correction_kernel_columns': [list(map(int, kernel[:, j]))
                                              for j in range(kernel.cols)]}


def main():
    local_rows, global_rows, counterexamples = [], [], []
    kinds = sorted({k for r in G.PROFILES.values() for k in r['kodaira_types']})
    for kind in kinds:
        _, _, labels, _ = component_matrix(kind)
        for p in range(len(labels)):
            for q in range(len(labels)):
                result = solve_local(kind, p, q)
                assert result['exists'] == (p * q % len(labels) == 0)
                local_rows.append(result)
    for key, info in sorted(G.PROFILES.items()):
        height = s.Rational(info['height_matrix'][0][0])
        assert height.p == 1
        denominator = int(height.q)
        component_orders = []
        for component in info['component_maps']:
            assert len(component['moduli']) <= 1
            order = int(component['moduli'][0]) if component['moduli'] else 1
            residue = int(component['rows'][0][0]) if component['rows'] else 0
            assert gcd(residue, order) == 1
            component_orders.append(order)
        assert lcm(*component_orders) == denominator
        valid, extra, discrepancies = 0, [], []
        for a in range(denominator):
            for b in range(denominator):
                possible, narrow = True, True
                for kind, component in zip(info['kodaira_types'], info['component_maps']):
                    assert len(component['moduli']) <= 1
                    order = component['moduli'][0] if component['moduli'] else 1
                    residue = component['rows'][0][0] if component['rows'] else 0
                    p, q = a * residue % order, b * residue % order
                    possible = possible and solve_local(kind, p, q)['exists']
                    narrow = narrow and (p == 0 or q == 0)
                predicted = a * b % denominator == 0
                if possible != predicted:
                    discrepancies.append([a, b, possible, predicted])
                if possible:
                    valid += 1
                    if not narrow:
                        extra.append([a, b])
        row = {'os_entry': key[0], 'profile': key[1], 'height_denominator': denominator,
               'component_group_orders': component_orders,
               'generator_component_maps_are_units': True,
               'component_order_lcm_equals_height_denominator': True,
               'all_residue_pairs_checked': denominator ** 2,
               'number_admitting_component_corrections': valid,
               'new_pairs_beyond_narrowness_OR': extra,
               'discrepancies_with_integral_height_criterion': discrepancies}
        global_rows.append(row)
        counterexamples.extend([dict(row=key, example=x) for x in discrepancies])
        print(key, 'd0', denominator, 'pairs', denominator ** 2,
              'valid', valid, 'extra', len(extra), 'discrepancies', len(discrepancies), flush=True)
    example = solve_local('I4', 2, 2)
    assert example['exists']
    record = {'local_component_pair_cases': local_rows,
              'global_profile_residue_cases': global_rows,
              'integral_height_criterion_discrepancies': counterexamples,
              'example_I4_P2_Q2': example,
              'scope': 'Exact integer equation (sigma-I)(c+JD)=0 only; no new cap or global smooth claim.'}
    (ROOT / 'root_vertical_corrections.json').write_text(json.dumps(record, indent=2) + '\n')
    print('LOCAL CASES', len(local_rows), 'GLOBAL RESIDUE PAIRS',
          sum(r['all_residue_pairs_checked'] for r in global_rows), flush=True)
    print('INTEGRAL HEIGHT CRITERION DISCREPANCIES', len(counterexamples), flush=True)


if __name__ == '__main__':
    main()
