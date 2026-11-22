"""Fresh 02WM calculation, written with the target proof still closed.

Chern characters are added in K-theory.  This does not multiply the total
Chern polynomials used in the earlier WU certificate.
"""
from fractions import Fraction
import itertools
import json


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def display(polynomial):
    return {m: str(c) for m, c in polynomial.items()}


# ch(T_T) = 2-k+(k^2-2e)/2; ch(I_Z L)=1+k+k^2/2-ell.
tangent = {'1': Fraction(2), 'k': Fraction(-1),
           'k2': Fraction(1, 2), 'e': Fraction(-1)}
ideal_line = {'1': Fraction(1), 'k': Fraction(1),
              'k2': Fraction(1, 2), 'ell': Fraction(-1)}
ambient = add(tangent, ideal_line)
assert ambient == {'1': 3, 'k2': 1, 'e': -1, 'ell': -1}

# Elimination in the two equations K^2=e+ell and K^2+e=12 chi.
# The following exact evaluations certify the resulting degree-one identity
# in the independent variables e,ell,chi; the algebraic elimination is also
# written in the derivation.
elimination_grid = []
for e, ell, chi in itertools.product((0, 1), repeat=3):
    k2 = e + ell
    original = k2 + e - 12 * chi
    eliminated = 2 * e + ell - 12 * chi
    assert original == eliminated
    elimination_grid.append([e, ell, chi, original])

rational = []
for ell in range(7):
    e = Fraction(12 - ell, 2)
    if e.denominator == 1 and e >= 3:
        rational.append({'ell': ell, 'e': int(e), 'K2': int(e + ell)})
assert [r['ell'] for r in rational] == [0, 2, 4, 6]

ruled = []
for genus in (0, 1, 2, 3, 7):
    for ell in (0, 1, 2, 4, 6):
        blowups = Fraction(4 * (1 - genus) - ell, 2)
        residual = 2 * (4 * (1 - genus) + blowups) + ell - 12 * (1 - genus)
        assert residual == 0
        ruled.append({'genus': genus, 'ell': ell, 'forced_blowups': str(blowups),
                      'nonnegative_integral': blowups.denominator == 1 and blowups >= 0})

# Coordinate-plane inclusions in the actual cusp charts.  A chosen unit
# minor is evaluated directly by the two-term alternating expression.
charts = []
for omitted in range(3):
    coordinates = [i for i in range(3) if i != omitted]
    jacobian = [[int(row == coordinates[col]) for col in range(2)] for row in range(3)]
    a, b = coordinates
    unit_minor = jacobian[a][0] * jacobian[b][1] - jacobian[a][1] * jacobian[b][0]
    assert unit_minor == 1
    charts.append({'omitted_coordinate': omitted, 'normalization_coordinates': coordinates,
                   'Jacobian': jacobian, 'unit_minor_rows': coordinates, 'unit_minor': unit_minor})

# The reduced hexagon: six marked P1s, each with its two endpoint vertices,
# one connecting 1-cell and one 2-cell.  The endpoint identifications yield
# a cycle graph.  Each 2-cell has zero cellular boundary (edge forth/back).
vertices = list(range(6))
edges = [(i, (i + 1) % 6) for i in vertices]
seen = {0}
while True:
    expanded = seen | {b for a, b in edges if a in seen} | {a for a, b in edges if b in seen}
    if expanded == seen:
        break
    seen = expanded
assert seen == set(vertices)
b0 = 1
b1 = len(edges) - len(vertices) + b0
b2 = 6
e_hexagon = len(vertices) - len(edges) + b2
assert e_hexagon == b0 - b1 + b2 == 6

# The actual blowdown basis of dP6=Bl_3(P2).
intersection_diagonal = [1, -1, -1, -1]
canonical_coordinates = [-3, 1, 1, 1]
k2_del_pezzo = sum(a * a * sign for a, sign in zip(canonical_coordinates, intersection_diagonal))
surface_cells = [1, 0, 4, 0, 1]
e_del_pezzo = sum((-1) ** i * n for i, n in enumerate(surface_cells))
assert k2_del_pezzo == e_del_pezzo == 6


def quadratic_product(a, b, root_square):
    c0, c1 = root_square
    return (a[0] * b[0] + a[1] * b[1] * c0,
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1] * c1)


finite_root_supports = []
for name, relation, rotation, periods, order, degree in (
        ('S1', (-1, 1), (-1, 1), [(-2, 1), (-3, 0)], 3, 9),
        ('S2', (-1, 0), (0, -1), [(-1, 1), (-2, 0)], 4, 8)):
    images = [quadratic_product(rotation, p, relation) for p in periods]
    columns = []
    for real, root in images:
        first = Fraction(root, periods[0][1])
        second = Fraction(real - first * periods[0][0], periods[1][0])
        assert first.denominator == second.denominator == 1
        columns.append([int(first), int(second)])
    a, b = columns
    fixed_determinant = (1 - a[0]) * (1 - b[1]) - b[0] * a[1]
    assert fixed_determinant != 0
    powers = [(1, 0)]
    for _ in range(order):
        powers.append(quadratic_product(powers[-1], rotation, relation))
    assert powers[-1] == (1, 0) and all(p != (1, 0) for p in powers[1:-1])
    finite_root_supports.append({
        'support': name, 'cover_degree': degree, 'moving_period_basis': periods,
        'rotation': rotation, 'rotation_columns_in_that_basis': columns,
        'det_identity_minus_moving_rotation': fixed_determinant,
        'fixed_H1_dimensions_E_and_F': [2, 0], 'b1_quotient': 2,
        'canonical_character_powers': powers, 'canonical_character_order': order,
        'local_base_power': order,
    })

print(json.dumps({
    'scope': 'prerelease 02WM; mathematical formulas proved for all parameters in the derivation',
    'chern_character': {'tangent': display(tangent), 'ideal_line': display(ideal_line),
                        'sum': display(ambient), 'degree_two_equation': 'K2-e-ell=0'},
    'noether_elimination': {'separate_degree_bound': [1, 1, 1], 'nodes_per_variable': [0, 1],
                            'grid': elimination_grid, 'equation': '2e+ell=12chi'},
    'rational_integral_possibilities': rational,
    'ruled_forced_values': ruled,
    'class_VII_nonnegative_equation': {'k_coefficient': 2, 'r_coefficient': 2,
                                      'ell_coefficient': 1, 'right_side': 0},
    'coordinate_plane_charts': charts,
    'conductor_hexagon': {'vertices': vertices, 'edges': edges, 'two_cells': 6,
                          'Betti': [b0, b1, b2], 'Euler': e_hexagon},
    'del_Pezzo_blowdown': {'basis': ['L', 'E1', 'E2', 'E3'],
                          'intersection_diagonal': intersection_diagonal,
                          'canonical_coordinates': canonical_coordinates,
                          'cell_counts': surface_cells, 'K2': k2_del_pezzo, 'Euler': e_del_pezzo},
    'actual_multiple_smooth_supports': finite_root_supports
}, indent=2))
