"""02YJ prerelease affine identities and integral leaf cancellation.

Every asserted universal affine identity is recovered from its value at
zero and the coordinate unit vectors.  The proof supplies the affine
degree bound and the topology; this is not sampling of curve graphs.
No YJ target proof or historical YJ program has been opened.
"""
from itertools import permutations
import json

def affine_coefficients(function, variables):
    zero=(0,)*variables
    constant=function(*zero)
    coefficients=[]
    for j in range(variables):
        unit=tuple(int(i==j) for i in range(variables))
        coefficients.append(function(*unit)-constant)
    return [constant]+coefficients

# A graph-of-surfaces model has c component vertices, s auxiliary
# singular-point vertices, E incidence edges, 2G surface one-cells and
# c surface two-cells.  Its connected incidence graph has b=E-c-s+1.
def cell_euler(c,s,E,G):return (c+s)-(E+2*G)+c
def graph_substitution_residual(c,s,b,G):
    return cell_euler(c,s,b+c+s-1,G)-(c+1-2*G-b)
curve_coefficients=affine_coefficients(graph_substitution_residual,4)
assert curve_coefficients==[0]*5

# Connected compact curves with virtually abelian fundamental group
# have either G=0,b<=1 or G=1,b=0; the group proof is in the derivation.
def rational_case(c,b):return (c+1-b)-c-(1-b)
def elliptic_case(c):return (c+1-2)- (c-1)
case_coefficients={'rational':affine_coefficients(rational_case,2),
                   'elliptic':affine_coefficients(elliptic_case,1)}
assert all(not any(v) for v in case_coefficients.values())

# For one point blowup the discrepancy equation is 1+a-mu=0.
blowup_coefficients=affine_coefficients(lambda mu:1+(mu-1)-mu,1)
assert blowup_coefficients==[0,0]

# Adjoin a rational leaf at a point p.  Its CW chain complex has an
# extra vertex v, edge e with boundary v-p, and a sphere two-cell s
# with zero boundary.  The integral change from (p,v) to (p,v-p)
# splits the edge/vertex pair and leaves precisely Z*s in degree 2.
U=((1,1),(0,1));V=((1,-1),(0,1))
def product(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))
assert product(U,V)==product(V,U)==((1,0),(0,1))
old_boundary=((-1,),(1,));new_boundary=product(U,old_boundary)
assert new_boundary==((0,),(1,))
def leibniz(A):
    answer=0
    for sigma in permutations(range(len(A))):
        term=(-1)**sum(sigma[i]>sigma[j] for i in range(len(A))
                      for j in range(i+1,len(A)))
        for i,j in enumerate(sigma):term*=A[i][j]
        answer+=term
    return answer
assert leibniz(U)==leibniz(V)==1

print(json.dumps({
    'target':'02YJ / night:P4R.7',
    'method':'Recover affine polynomial coefficients from zero and unit-vector evaluations; split a universal rational-leaf cellular boundary by an explicit integral basis change.',
    'curve_variable_order':['c','s','b','G'],
    'curve_affine_residual_coefficients':curve_coefficients,
    'curve_identity':'(c+s)-(b+c+s-1+2G)+c = c+1-2G-b',
    'virtually_abelian_case_residual_coefficients':case_coefficients,
    'rational_case_nonnegative_decomposition':'e(C)=c+(1-b), c>=1, b in {0,1}',
    'elliptic_case_nonnegative_decomposition':'e(C)=c-1, c>=1',
    'blowup_discrepancy_coefficients':blowup_coefficients,
    'leaf_basis_change':U,'leaf_basis_inverse':V,
    'old_edge_boundary':old_boundary,'new_edge_boundary':new_boundary,
    'basis_determinants':[leibniz(U),leibniz(V)],
    'leaf_homology_effect':'The edge/new-vertex pair is contractible; the rational leaf contributes one unpaired degree-two class. Its collapse preserves pi1 and kills that H2 class.',
    'limits':'The proof establishes the conductor tree, proper quotient/homeomorphism, cofibration, fundamental group amalgam, virtually abelian classification and the nonnegative smooth-stratum Euler input. The program does not infer these geometric assertions from the cellular arithmetic.'
},indent=2))
