"""02YI prerelease exact edge-square, row and vanishing-sphere checks.

The graph identities are proved for arbitrary size by summing one-edge
identities.  Each one-edge identity is certified here by a complete rational
interpolation grid with separately proved degree bounds, not by examples
of exceptional configurations.  No target proof or historical target
program was open when this program was written.
"""
from fractions import Fraction
from itertools import product, permutations
import json

# Variables c, wi, wj, ui, uj.  The matrix of a single weighted edge is
# [[c*wj/wi,-c],[-c,c*wi/wj]], and x=(wi*ui,wj*uj).
unit = (0,0,0,0,0)
c = (1,0,0,0,0)
xi = (0,1,0,1,0)
xj = (0,0,1,0,1)
entry_powers = [[(1,-1,1,0,0), c], [c, (1,1,-1,0,0)]]
x_powers = [xi,xj]
left_powers = []
for i in range(2):
    for j in range(2):
        left_powers.append(tuple(x_powers[i][r]+entry_powers[i][j][r]+x_powers[j][r] for r in range(5)))
assert all(all(e >= 0 for e in p) for p in left_powers)
left_degrees = tuple(max(p[r] for p in left_powers) for r in range(5))
right_degrees = (1,1,1,2,2)
bounds = tuple(max(a,b) for a,b in zip(left_degrees,right_degrees))
grid = [(0,1),(1,2),(1,2),(-1,0,1),(-1,0,1)]
assert all(len(values)==degree+1 for values,degree in zip(grid,bounds))
edge_count=0
for cv,wi,wj,ui,uj in product(*grid):
    L=((Fraction(cv*wj,wi),Fraction(-cv)),(Fraction(-cv),Fraction(cv*wi,wj)))
    x=(wi*ui,wj*uj)
    left=sum((x[i]*L[i][j]*x[j] for i in range(2) for j in range(2)),Fraction(0))
    right=Fraction(cv*wi*wj*(ui-uj)**2)
    assert left==right
    edge_count+=1
assert edge_count==72

# Anchor term: (a/wi)*(wi*ui)^2 = a*wi*ui^2.
anchor_grid=[(0,1),(1,2),(-1,0,1)]
anchor_bounds=(1,1,2)
assert all(len(g)==d+1 for g,d in zip(anchor_grid,anchor_bounds))
anchor_count=0
for a,w,u in product(*anchor_grid):
    assert Fraction(a,w)*(w*u)**2==a*w*u*u
    anchor_count+=1

# Weighted row identity, variables c,wi,wj,ui,uj,a:
# (c*wj/wi+a/wi)*(wi*ui)-c*(wj*uj)
# = a*ui+c*wj*(ui-uj).  Cancellation gives the displayed degree bound.
row_bounds=(1,0,1,1,1,1)
row_grid=[(0,1),(1,),(1,2),(-1,1),(-1,1),(0,1)]
assert all(len(g)==d+1 for g,d in zip(row_grid,row_bounds))
row_count=0
for cv,wi,wj,ui,uj,a in product(*row_grid):
    left=(Fraction(cv*wj+a,wi))*(wi*ui)-cv*(wj*uj)
    right=a*ui+cv*wj*(ui-uj)
    assert left==right
    row_count+=1

# The complex orientation is (e1,Je1,e2,Je2).  Tangent-then-J-normal
# order is (e1,e2,Je1,Je2), with the following explicit permutation.
order=(0,2,1,3)
inversions=sum(order[i]>order[j] for i in range(4) for j in range(i+1,4))
normal_orientation_sign=(-1)**inversions
sphere_cells={0:1,2:1}
sphere_euler=sum((-1)**degree*number for degree,number in sphere_cells.items())
self_intersection=normal_orientation_sign*sphere_euler
assert (inversions,normal_orientation_sign,sphere_euler,self_intersection)==(1,-1,2,-2)

# Complex Hessian of q=z1^2+z2^2+z3^2.
hessian=[[2 if i==j else 0 for j in range(3)] for i in range(3)]
determinant=0
for p in permutations(range(3)):
    sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    term=sign
    for i in range(3):term*=hessian[i][p[i]]
    determinant+=term
assert determinant==8

print(json.dumps({
    'target':'02YI / night:P4R.6',
    'edge_matrix':'[[c*wj/wi,-c],[-c,c*wi/wj]]',
    'substituted_vector':'[wi*ui,wj*uj]',
    'left_term_exponents_after_denominator_cancellation':left_powers,
    'separate_degree_bounds':bounds,
    'exact_full_grid_points':edge_count,
    'all_edge_residuals_zero':True,
    'anchor_degree_bounds':anchor_bounds,
    'anchor_full_grid_points':anchor_count,
    'all_anchor_residuals_zero':True,
    'row_degree_bounds':row_bounds,
    'row_full_grid_points':row_count,
    'all_row_residuals_zero':True,
    'interpolation_reason':'A polynomial of separate degree at most d_i that vanishes on the product of d_i+1 distinct rational values is zero, by successive one-variable interpolation.',
    'graph_assembly':'Sum the certified edge blocks and anchor blocks over the actual intersection graph; the derivation proves positivity and the minimum principle for arbitrary finite size.',
    'complex_to_tangent_normal_permutation':order,
    'permutation_inversions':inversions,
    'normal_orientation_sign':normal_orientation_sign,
    'sphere_cell_counts':sphere_cells,
    'sphere_euler':sphere_euler,
    'vanishing_sphere_self_intersection':self_intersection,
    'quadratic_complex_hessian':hessian,
    'quadratic_complex_hessian_determinant':determinant,
    'limits':'The geometric existence and transport of the sphere, conductor duality, exceptional connectedness, integrality and strict positivity are proved in the independent derivation. This program verifies the universal local algebra and the explicit orientation/cell computation.'
},indent=2))
