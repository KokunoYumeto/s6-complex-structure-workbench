#!/usr/bin/env python3
"""Fresh quotient/transfer calculation from the safe 02QE affine actions.

Inputs are only the two T matrices, orders, translations and marking from
the safe final-II P309 setup. No target proof, prior check outcome or III
source is read. The companion fresh arithmetic program supplies elementary
matrix/exterior utilities and a final comparison, after deriving the maps.
"""

from argparse import ArgumentParser
from datetime import datetime, timezone
from pathlib import Path
import json

from S6_SERIES_PUBLISH_III_02QE_fresh_integral import (
    apply, calculate as arithmetic_calculation, determinant,
    determinantal_divisors, identity, multiply, transpose,
)


def power(matrix, exponent):
    answer = identity(len(matrix))
    for _ in range(exponent):
        answer = multiply(answer, matrix)
    return answer


def subtract(left, right):
    return [[x - y for x, y in zip(a, b)] for a, b in zip(left, right)]


def zero(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


def one_cover(order, cohomology, translation, quotient, section,
              relation_witness, cohomology_basis_change):
    assert power(cohomology, order) == identity(4)
    action = transpose(power(cohomology, order - 1))
    assert multiply(transpose(action), cohomology) == identity(4)
    assert power(action, order) == identity(4)
    assert determinant(action) == 1
    assert apply(action, translation) == translation
    assert action[0] == [1, 0, 0, 0]
    assert abs(translation[0]) == 1
    assert all((k * translation[0]) % order != 0 for k in range(1, order))
    norm = [[sum(power(action, k)[i][j] for k in range(order))
             for j in range(4)] for i in range(4)]
    assert apply(norm, translation) == [order * x for x in translation]

    # Abelianized relations: (A-I) Lambda and order*t - translation.
    relations = [subtract(action, identity(4))[i] + [-translation[i]]
                 for i in range(4)] + [[0, 0, 0, 0, order]]
    assert multiply(quotient, relations) == zero(2, 5)
    assert multiply(quotient, section) == identity(2)
    assert multiply(relations, relation_witness) == subtract(
        identity(5), multiply(section, quotient))

    h1_pushforward = [row[:4] for row in quotient]
    transfer_on_generators = [norm[i] + [translation[i]] for i in range(4)]
    assert multiply(transfer_on_generators, relations) == zero(4, 5)
    h1_transfer = multiply(transfer_on_generators, section)
    assert multiply(h1_transfer, quotient) == transfer_on_generators
    assert multiply(h1_pushforward, h1_transfer) == [
        [order * x for x in row] for row in identity(2)]
    assert multiply(h1_transfer, h1_pushforward) == norm

    # D_F: H^3(F) -> H_1(F), with <a,D_F(xi)>=int_F a wedge xi.
    volume_pairing = [[0, 0, 0, 1], [0, 0, -1, 0],
                      [0, 1, 0, 0], [-1, 0, 0, 0]]
    inverse_pairing = transpose(volume_pairing)
    assert multiply(volume_pairing, inverse_pairing) == identity(4)
    natural_h3_pullback = multiply(inverse_pairing, h1_transfer)
    assert abs(determinant(cohomology_basis_change)) == 1
    marked_h3_pullback = multiply(natural_h3_pullback, cohomology_basis_change)
    h3_pushforward = transpose(marked_h3_pullback)
    h3_invariants = determinantal_divisors(h3_pushforward)
    assert h3_invariants['rank'] == 2
    image_index = h3_invariants['determinantal_divisors'][2]

    return dict(
        order=order, T=cohomology, A=action, v=translation,
        affine_action='x -> A*x + v/order modulo Z^4',
        orientation_determinant=determinant(action),
        freeness_character='gamma(A*x+v/order)=gamma(x)+v[0]/order; v[0]=+1 or -1',
        norm=norm,
        presentation_generator_order=['hat_gamma', 'hat_u', 'hat_w', 'hat_delta', 't'],
        abelianized_relations_columns=relations,
        abelianization_quotient=quotient, abelianization_section=section,
        relation_lattice_witness=relation_witness,
        abelianization='Z^2, with the explicit quotient/section and relation-lattice identity displayed',
        h1_pushforward=h1_pushforward,
        h1_pushforward_minors=determinantal_divisors(h1_pushforward),
        transfer_on_presentation_generators=transfer_on_generators,
        h1_transfer=h1_transfer,
        natural_h3_pullback=natural_h3_pullback,
        cohomology_basis_change=cohomology_basis_change,
        h3_pullback=marked_h3_pullback,
        h3_pushforward=h3_pushforward,
        h3_pushforward_minors=h3_invariants,
        h3_pushforward_image_index=image_index,
    )


def calculate():
    T1 = [[1, 0, -6, 2], [0, -1, 1, 1], [0, -1, 0, 1], [0, 0, 0, 1]]
    T2 = [[1, 6, 0, -3], [0, 0, -1, 1], [0, 1, 0, 0], [0, 0, 0, 1]]
    v1, v2 = [1, 2, -4, 0], [-1, -3, 3, 0]

    # Bases of Gamma_ab: (t,hat_w) for order 3 and (t,hat_u) for order 4.
    C3 = [[3, 0, 0, 0, 1], [0, 2, 1, 3, 0]]
    K3 = [[0, 0], [0, 0], [0, 1], [0, 0], [1, 0]]
    X3 = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
          [-2, 1, 0, 1, 0], [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0]]
    C4 = [[-4, 0, 0, 0, 1], [0, 1, 1, 2, 0]]
    K4 = [[0, 0], [0, 1], [0, 0], [0, 0], [1, 0]]
    X4 = [[0, 0, 0, 0, 0], [3, 0, 1, 1, 0],
          [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
    # H^3 bases obtained by D_S^{-1}: (-hat_w,t) and (-hat_u,-t).
    W3 = [[0, 1], [-1, 0]]
    W4 = [[0, -1], [-1, 0]]
    three = one_cover(3, T1, v1, C3, K3, X3, W3)
    four = one_cover(4, T2, v2, C4, K4, X4, W4)

    # These comparisons occur only after the quotient and transfer maps above.
    arithmetic = arithmetic_calculation()
    assert three['h3_pullback'] == arithmetic['supplied_pullback_generator_columns_3']
    assert four['h3_pullback'] == arithmetic['supplied_pullback_generator_columns_4']
    alpha3 = three['h3_pushforward'] + [
        [-x for x in row] for row in four['h3_pushforward']]
    assert alpha3 == arithmetic['alpha3']
    assert three['h3_pushforward_image_index'] == 1
    assert four['h3_pushforward_image_index'] == 2
    assert three['h1_pushforward_minors']['determinantal_divisors'][2] == 3
    assert four['h1_pushforward_minors']['determinantal_divisors'][2] == 4
    return dict(
        target='02QE / mapsaudit:finite-degree-three',
        input_scope='Only the safe final-II P309 affine setup; target proof and prior check outcomes remain unopened.',
        safe_packet='agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_02QE_geometric_setup.tex',
        source_edition_sha256='106fcde4a73b9d94f7bd328d05d517bb1c3813ca190bf253258ccf1bce5aa844',
        cover_3=three, cover_4=four,
        geometric_difference_map_alpha3=alpha3,
        geometric_difference_map_minors=determinantal_divisors(alpha3),
        geometric_difference_map_kernel=arithmetic['alpha3_smith_certificate']['integer_kernel_generator'],
        result='The quotient presentations and transfers derive both full integral H^3 pullback lattices; their duals reproduce the supplied alpha3 matrix and the index 1/index 2 conclusions.',
        theorem_dependencies='Written proof: free finite affine quotients; exact normal-form group presentation; explicit abelianization; covering-chain transfer and oriented Poincare duality; Kronecker naturality.',
    )


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] /
                        'agents/continuation4_iii_reductions/S6_SERIES_PUBLISH_III_02QE_fresh_affine.json')
    args = parser.parse_args()
    result = calculate()
    result['completed_utc'] = datetime.now(timezone.utc).isoformat()
    result['program'] = 'code/S6_SERIES_PUBLISH_III_02QE_fresh_affine.py'
    result['attribution'] = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; effort setting not separately exposed; fourth-continuation III reductions'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    for name in ['cover_3', 'cover_4']:
        row = result[name]
        print(name, 'H1 map:', row['h1_pushforward'])
        print(name, 'H3 pullback columns:', row['h3_pullback'])
        print(name, 'H3 pushforward index:', row['h3_pushforward_image_index'])
    print('alpha3 Smith:', result['geometric_difference_map_minors']['smith_nonzero_entries'])
    print('alpha3 kernel:', result['geometric_difference_map_kernel'])
    print(args.output)


if __name__ == '__main__':
    main()
