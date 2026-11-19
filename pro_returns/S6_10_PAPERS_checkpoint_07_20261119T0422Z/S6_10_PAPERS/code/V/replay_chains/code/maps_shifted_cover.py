"""Exact cyclic-cover cohomology of the actual regular-fibre complement.

Uses invariant specialization of the unchanged cusp, finite averaging,
and j_* local-system cohomology on the three-punctured disc.  The text
proves these geometric inputs; this is the exact matrix certificate.
"""
from pathlib import Path
from itertools import combinations
from math import comb
import json
import sympy as sp

A1 = sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0 = (A1*A2).inv()


def exterior(A, degree):
    basis = list(combinations(range(A.rows), degree))
    return sp.Matrix([[A.extract(a, b).det() for b in basis] for a in basis])


def companion(polynomial, variable):
    p = sp.Poly(polynomial, variable)
    degree = p.degree()
    C = sp.zeros(degree)
    for i in range(degree-1):
        C[i+1, i] = 1
    for i in range(degree):
        C[i, degree-1] = -p.nth(i)
    return C


def run():
    x = sp.symbols('x')
    cases = []
    cover = [0]*7
    for order in [1, 2, 3, 4, 6, 12]:
        C = companion(sp.cyclotomic_poly(order, x), x)
        extension_degree = C.rows
        assert C**order == sp.eye(extension_degree)
        globals_ = []
        locals_ = []
        base_one = []
        for q in range(5):
            d = comb(4, q)
            size = d*extension_degree
            # The inverse cohomological transport, with the flat-line phase.
            transforms = [sp.kronecker_product(C**power, exterior(A.inv().T, q))
                          for A, power in [(A1,4),(A2,-3),(M0,0)]]
            differences = [T-sp.eye(size) for T in transforms]
            local = [(size-D.rank())//extension_degree for D in differences]
            global_ = (size-sp.Matrix.vstack(*differences).rank())//extension_degree
            assert all((size-D.rank()) % extension_degree == 0 for D in differences)
            globals_.append(global_)
            locals_.append(local)
            h1 = 2*d+global_-sum(local)
            assert h1 >= 0
            base_one.append(h1)
        betti = [(globals_[q] if q <= 4 else 0)
                 +(base_one[q-1] if 1 <= q <= 5 else 0)
                 for q in range(7)]
        expected = {
            1:[1,1,4,6,4,0,0],
            2:[0,0,4,6,4,0,0],
            3:[0,0,3,4,3,0,0],
            4:[0,0,3,4,3,0,0],
            6:[0,1,5,6,5,1,0],
            12:[0,1,4,4,4,1,0],
        }[order]
        assert betti == expected, (order, betti)
        assert sum((-1)**q*b for q,b in enumerate(betti)) == 2
        for q,b in enumerate(betti):
            cover[q] += extension_degree*b
        cases.append({'order':order, 'number_of_characters':extension_degree,
                      'global_invariants':globals_,
                      'local_invariants_by_degree_A1_A2_M0':locals_,
                      'base_degree_one':base_one,
                      'complement_twisted_betti':betti})
    assert cover == [1,7,46,56,46,6,0]
    nontrivial = [cover[q]-cases[0]['complement_twisted_betti'][q] for q in range(7)]
    y_one = [1,0,1,19,45,45,19,1,0,1]
    y_betti = [y_one[q]+2*sum(comb(3,j)*nontrivial[q-j]
                             for j in range(4) if 0 <= q-j < 7)
               for q in range(10)]
    assert y_betti == [1,12,121,407,693,693,407,121,12,1]
    assert y_betti == y_betti[::-1]
    result = {'cases':cases, 'cover_degree':12,
              'E12_rational_betti':cover,
              'Y_rational_betti':y_betti,
              'scope':'Requires the actual invariant-cycle and cover-splice proofs; no integral torsion conclusion.'}
    Path(__file__).with_suffix('.out.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    run()
