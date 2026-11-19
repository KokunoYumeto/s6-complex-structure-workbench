"""Exact odd-class bridge for OS45 P2,Q8, weight2 at I8.

The homology bridge is proved.  Its proposed embedded representative and
critical/reference-frame calculation remain research, not a smooth claim.
"""
from pathlib import Path
import json
import sympy as s
from manifolds_general_initial import integer_solution
from manifolds_rankone_families import decomp, wedge
from manifolds_weighted_profiles import group

root = Path(__file__).resolve().parents[1]
r = json.loads((root / 'records/maps_weighted_os45.json').read_text())
M = s.Matrix(r['full']['H2_matrix'])
A = [s.Matrix(x) for x in r['full']['fundamental_group']['conjugation_matrices']]
area = s.zeros(6, 1)
area[1] = 1                         # e1 wedge delta
R = wedge(A[1]) - s.eye(6)
try:
    integer_solution(R, area)
    raise AssertionError('The angular area was unexpectedly zero on the boundary.')
except ValueError:
    pass
area_double = integer_solution(R, 2 * area)
assert (wedge(A[2]) - s.eye(6))[:, 3] == area
keep = list(range(41)) + list(range(50, M.cols))
E = M[:, keep]
target = area.col_join(s.zeros(M.rows - 6, 1))
assert M[:, 15] == target
bound = s.zeros(E.cols, 1)
bound[keep.index(15)] = 1
assert E * bound == target
D, U, V, rank = decomp(E)
normal_images = (U * M[:, 41:43])[rank:, :]
assert normal_images.rows == normal_images.cols == 2
assert normal_images.det() != 0
assert group(E) == {'free': 2, 'torsion': [2]}
assert all(int(v) % 2 == 0 for v in r['critical_bound'])
record = {
    'input': 'OS45/default P2G,Q8G, weights(2,0,0,0,0), ordinary clutch e1',
    'angular_area': list(map(int, area)),
    'boundary_area_order': 2,
    'double_area_monodromy_bound': list(map(int, area_double)),
    'exterior_area_bound_column': 15,
    'exterior_area_bound_description': '(wedge2 A_firstI1-I)(e2 wedge delta)=e1 wedge delta; p=q=0 at this I1.',
    'exterior_H2_presentation': group(E),
    'cusp_normal_free_images': [[int(x) for x in row] for row in normal_images.tolist()],
    'cusp_normal_free_determinant': int(normal_images.det()),
    'odd_class_proof': 'The full cusp H2 boundary kernel is its two free normal tori plus the angular Z2 (D43). Their exterior free images are independent. The angular class is zero in E by the literal column15 and zero in N by its angular solid-torus cap. Therefore the full Mayer-Vietoris kernel is exactly Z2. The map H3(X)=Z8 onto this kernel is surjective, so any bridge mapping to its generator is an odd class.',
    'all_critical_bar_coefficients_even': True,
    'remaining_geometric_step': 'Realize the bridge with controlled reference frame and compute its intersection with the actual local specialization chains from critical curves to regular-fibre preimages. Even bar coefficients alone do not settle that last local intersection.',
}
(root / 'records/root_OS45_bridge.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
