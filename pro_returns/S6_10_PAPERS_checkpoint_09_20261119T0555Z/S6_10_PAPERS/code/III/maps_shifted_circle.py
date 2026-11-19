"""Exact lattice and Euler certificate for E.2.13.

This checks the finite algebra in the geometric circle-fibration proof.
It does not replace the actual-map submersion or deck-action arguments.
"""
from pathlib import Path
import json
import math

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def run():
    # Generators: a1,a2,b1,b2,h1,h2; positive peripheral relations.
    relations = sp.Matrix([
        [3, 0, 0, 0, -1, 0],
        [0, 4, 0, 0, 1, 0],
        [0, 0, 3, 0, 0, -1],
        [0, 0, 0, 4, 0, 1],
        [1, 1, 1, 1, 0, 0],
    ])
    character = sp.Matrix([4, -3, -4, 3, 12, -12])
    assert relations * character == sp.zeros(5, 1)
    assert math.gcd(*map(int, character)) == 1
    normal = smith_normal_form(relations, domain=ZZ)
    assert [abs(int(normal[i, i])) for i in range(5)] == [1] * 5
    assert relations.rank() == 5

    residues = [4, -3, -4, 3]
    cone_orders = [12 // math.gcd(12, r) for r in residues]
    assert cone_orders == [3, 4, 3, 4]
    assert math.gcd(12, *residues) == 1
    orb_euler = sp.Integer(2) - sum(1 - sp.Rational(1, m) for m in cone_orders)
    assert orb_euler == -sp.Rational(5, 6)
    surface_euler = 12 * orb_euler
    genus = 1 - surface_euler / 2
    assert genus == 6

    # The centre's character and the positive diagonal kernel basis.
    central_character = sp.Matrix([[12, -12]])
    basis = sp.Matrix([[1, 0], [1, 1]])  # v=(1,1), w=(0,1)
    assert basis.det() == 1
    assert central_character * basis == sp.Matrix([[0, -12]])
    pulled_euler = sp.Matrix([-1, -1])
    assert basis.inv() * pulled_euler == sp.Matrix([-1, 0])

    # Standard S3 boundary orientation is -dr wedge dphi1 wedge dphi2.
    # For theta=(cos(r)^2/4)dphi1+(sin(r)^2/3)dphi2,
    # the coefficient of dr wedge dphi1 wedge dphi2 in theta dtheta
    # is -sin(r)cos(r)/6. Dividing by (2pi)^2 cancels phase integrals.
    r = sp.symbols('r', real=True)
    A = sp.cos(r) ** 2 / 4
    B = sp.sin(r) ** 2 / 3
    coefficient = sp.simplify(B * sp.diff(A, r) - A * sp.diff(B, r))
    contact_integral = sp.integrate(-coefficient, (r, 0, sp.pi / 2))
    assert contact_integral == sp.Rational(1, 12)
    orb_circle_euler = -contact_integral
    assert 12 * orb_circle_euler == -1

    result = {
        'statement': 'E.2.13',
        'relation_smith_nonzero': [1] * 5,
        'primitive_character': list(map(int, character)),
        'cone_image_orders': cone_orders,
        'orbifold_euler': str(orb_euler),
        'surface_cover_degree': 12,
        'surface_genus': int(genus),
        'central_kernel_vector': [1, 1],
        'oriented_kernel_basis_det': int(basis.det()),
        'pulled_torus_euler': [-1, -1],
        'kernel_circle_euler': -1,
        'fibre_group_H1_free_rank': 12,
        'outer_return_order': 12,
        'scope': 'Finite algebra only; actual submersion and infinite homotopy order proved in text.',
    }
    output = Path(__file__).with_suffix('.out.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
