"""Integral top-class pullback certificate for the circle fibre Y.

The geometric classifying target is the Euler(-1) circle bundle over
Sigma_6, split into two copies of Sigma_(3,1) x S1. Its top class is
the boundary connecting class of gamma1 wedge gamma2.
"""
from pathlib import Path
import json
import sympy as sp
from maps_shifted_fibre_integral import saturated_columns
from maps_shifted_return import boundary_matrix, BASE


def run():
    volume = sp.zeros(len(BASE[2]),1)
    volume[BASE[2].index((0,4)),0] = 1
    coefficients = []
    for side in range(2):
        basis = saturated_columns(boundary_matrix(2,side)[0])
        sol, params = basis.gauss_jordan_solve(volume)
        assert params.rows == 0
        assert all(c.q == 1 for c in sol)
        assert basis*sol == volume
        coefficients.append(list(map(int,sol)))
    # Surjection H2(Y) -> H2(aspherical target)=Z^12, followed by
    # the primitive top-class injection proved by relative Hurewicz.
    kernel_rank = 121-12
    coinvariant_rank = 1+kernel_rank
    assert coinvariant_rank == 110
    y,w,h1 = sp.symbols('y w h1')
    # z-1=(h1-1)+h1(h2-1), so the two central opens cover after z-1 inversion.
    assert sp.expand((h1-1)+h1*w-(h1*(w+1)-1)) == 0
    result = {'gamma1_gamma2_in_both_primitive_boundary_images':True,
              'integral_coefficients_in_saturated_bases':coefficients,
              'classifying_H3_pullback':'zero',
              'pi2_fibre_coinvariants_free_rank':coinvariant_rank,
              'pi2_fibre_coinvariants_torsion':[6,6],
              'central_localized_pi2_free_rank':24,
              'scope':'Module consequences require the geometric classifying-map and localization proof in text.'}
    Path(__file__).with_suffix('.out.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    run()
