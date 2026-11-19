"""Integral boundary saturation and fibre homology for the actual Y.

Relies on torsion-free H*(E12), proved by the primitive j_* complex in
maps_shifted_cover_integral.py. Poincare--Lefschetz then makes every
boundary restriction image primitive, fixing it as the saturation of
the rational image already computed in maps_shifted_return.py.
"""
from pathlib import Path
from functools import reduce
from math import gcd
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ
from maps_shifted_return import boundary_matrix, BASE, contraction


def smith(matrix):
    D,U,V = smith_normal_decomp(DomainMatrix.from_Matrix(matrix).convert_to(ZZ))
    D,U,V = D.to_Matrix(),U.to_Matrix(),V.to_Matrix()
    assert D == U*matrix*V
    assert abs(U.det(method='domain-ge')) == 1
    assert abs(V.det(method='domain-ge')) == 1
    entries = [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    return entries,U,V


def saturated_columns(matrix):
    if matrix.cols == 0:
        return sp.zeros(matrix.rows,0)
    entries,U,V = smith(matrix)
    inv = U.inv()
    assert all(a.q == 1 for a in inv)
    saturated = inv[:, :len(entries)]
    assert matrix.row_join(saturated).rank() == len(entries)
    return saturated


def run():
    results = []
    saturated = {}
    for q in range(9):
        A,_ = boundary_matrix(q,0)
        B,_ = boundary_matrix(q,1)
        AA,BB = saturated_columns(A),saturated_columns(B)
        saturated[q] = (AA,BB)
        D = AA.row_join(BB)
        entries,U,V = smith(D)
        row = {'boundary_degree':q, 'rank':len(entries),
               'units':entries.count(1),
               'cokernel_torsion':[e for e in entries if e>1]}
        results.append(row)
        print(row,flush=True)
    betti = [1,12,121,407,693,693,407,121,12,1]
    cohomology = [{'degree':q, 'free_rank':betti[q],
                   'torsion':results[q-1]['cokernel_torsion'] if q else []}
                  for q in range(10)]
    # Integral Poincare duality in dimension nine reverses torsion q <-> 10-q.
    for q in range(1,10):
        assert cohomology[q]['torsion'] == cohomology[10-q]['torsion']
    assert [r['torsion'] for r in cohomology] == [[],[],[],[6,6],[],[],[],[6,6],[],[]]
    variation = []
    for q in range(1,9):
        A,B = saturated[q]
        ds,U,V = smith(A.row_join(-B))
        kernel = V[:,len(ds):]
        common = A*kernel[:A.cols,:]
        P,Q = saturated[q-1]
        es,L,R = smith(P.row_join(Q))
        target = L*contraction(q)*common
        free = target[len(es):,:]
        torsion_rows = [i for i,e in enumerate(es) if e>1]
        torsion_values = [[int(target[i,j]) % es[i] for j in range(target.cols)]
                         for i in torsion_rows]
        row = {'degree':q,
               'free_image_rank':free.rank(),
               'free_image_divisibility':abs(reduce(gcd,map(int,free),0)),
               'torsion_target_orders':[es[i] for i in torsion_rows],
               'torsion_image_matrix':torsion_values}
        variation.append(row)
        print('variation',row,flush=True)
    assert [r['free_image_divisibility'] for r in variation] == [0,0,0,72,72,0,0,0]
    assert all(all(a == 0 for row in r['torsion_image_matrix'] for a in row)
               for r in variation)
    output = {'scope':'Depends on the integral j_* cap identification and primitive-image argument.',
              'boundary_smith':results, 'Y_integral_cohomology':cohomology,
              'integral_torus_twist_variation':variation}
    Path(__file__).with_suffix('.out.json').write_text(json.dumps(output,indent=2)+'\n')


if __name__ == '__main__':
    run()
