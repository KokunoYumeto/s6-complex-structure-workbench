"""Integral j_* cohomology certificate for the cyclic twelve-cover of E.

The regular representation unfolds both finite affine caps; each unchanged
cusp has the primitive invariant specialization matrix of B.5.16.
"""
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ

from maps_shifted_cover import A1, A2, M0, exterior


def image_coordinates(D):
    B = hermite_normal_form(D)
    if B.cols == 0:
        return sp.zeros(0, D.cols)
    pivots = list(B.T.rref()[1])
    square = B.extract(pivots, list(range(B.cols)))
    X = square.inv()*D.extract(pivots, list(range(D.cols)))
    assert B*X == D
    assert all(a.q == 1 for a in X)
    return X


def run():
    permutation = sp.zeros(12)
    for i in range(12):
        permutation[(i+1)%12, i] = 1
    result = []
    for q in range(5):
        transforms = [sp.kronecker_product(permutation**power, exterior(A.inv().T, q))
                      for A, power in [(A1,4),(A2,-3),(M0,0)]]
        dimension = transforms[0].rows
        differences = [T-sp.eye(dimension) for T in transforms]
        coordinates = [image_coordinates(D) for D in differences]
        differential = sp.Matrix.vstack(*coordinates)
        smith = smith_normal_form(differential, domain=ZZ)
        entries = [abs(int(smith[i,i])) for i in range(min(smith.shape)) if smith[i,i]]
        row = {'vertical_degree':q,
               'H0_free_rank':dimension-len(entries),
               'H1_free_rank':differential.rows-len(entries),
               'H1_torsion':[v for v in entries if v > 1],
               'cochain_shape':list(differential.shape)}
        result.append(row)
        print(row, flush=True)
    assert [r['H0_free_rank'] for r in result] == [1]*5
    assert [r['H1_free_rank'] for r in result] == [6,45,55,45,6]
    assert all(not r['H1_torsion'] for r in result)
    output = {'scope':'Integral local-system calculation; the actual boundary restriction lattice is not computed.',
              'j_star_groups':result}
    Path(__file__).with_suffix('.out.json').write_text(json.dumps(output,indent=2)+'\n')


if __name__ == '__main__':
    run()
