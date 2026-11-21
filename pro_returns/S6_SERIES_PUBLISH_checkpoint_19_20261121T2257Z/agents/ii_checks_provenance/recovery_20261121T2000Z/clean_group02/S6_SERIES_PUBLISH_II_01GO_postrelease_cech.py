"""Exact two-chart Cech matrices for the embedded-point example.

Written after E17 target release. The symbolic interval argument is
universal; actual finite matrices are also computed for explicit k.
No new prerelease derivation or extra independent event is claimed.
"""
import sympy as s
import json

# Different local-algebra method from the old Groebner truncations:
# rho(z)=0 and rho(epsilon)=E21 define a two-dimensional representation.
# rho(f)=f(0,0) I + (d f/d epsilon)(0,0) E21 is multiplicative by
# the product rule. It kills z*epsilon, epsilon^2 and z^N for every
# N>=1, but it does not kill epsilon. No truncation range is used.
Z=s.zeros(2);E=s.Matrix([[0,0],[1,0]])
assert Z*E==E*Z==s.zeros(2) and E**2==s.zeros(2)
assert E*s.Matrix([1,0])==s.Matrix([0,1])
a,b,c,d=s.symbols('a b c d')
assert (a*s.eye(2)+b*E)*(c*s.eye(2)+d*E)==a*c*s.eye(2)+(a*d+b*c)*E

def cech(k):
    B=abs(k)+4
    # O(-k) transition: a section on the infinity chart has coefficient
    # z^(-k)*f_infinity(1/z) on the finite chart.
    cols=[('finite',j,j) for j in range(B+1)]
    cols += [('infinity',j,-k-j) for j in range(B+1)]
    exponents=list(range(min(0,-k-B),max(B,-k)+1))
    M=s.zeros(len(exponents),len(cols))
    for c,(chart,j,n) in enumerate(cols):
        M[exponents.index(n),c]=1 if chart=='finite' else -1
    rank=M.rank()
    h0=len(cols)-rank+1  # the actual C_p square-zero summand
    h1=len(exponents)-rank
    missing=[n for n in exponents if not(n>=0 or n<=-k)]
    overlap=[n for n in exponents if 0<=n<=-k]
    assert h0==len(overlap)+1 and h1==len(missing)
    assert h0==max(1-k,0)+1 and h1==max(k-1,0)
    return {'k':k,'matrix_shape':list(M.shape),'rank':rank,
            'H0_O_basis_exponents':overlap,'H1_basis_exponents':missing,
            'h0_including_embedded_point':h0,'h1':h1}

# Universal dimensions, from the explicit disjoint/overlapping interval
# pivot choice (one column for each exponent in the union).
k=s.symbols('k',integer=True,positive=True)
B=k+4
columns=2*(B+1);rows=B-(-k-B)+1
assert s.expand(rows-columns)==k-1  # k>=1, the two image intervals disjoint
h=s.symbols('h',integer=True,nonnegative=True) # k=-h <=0
B=h+4
columns=2*(B+1);union_rows=B-(-4)+1
assert s.expand(columns-union_rows)==h+1 # overlap exponents 0,...,h
samples=[cech(i) for i in range(-8,9)]
print(json.dumps({'timing':'after 01GO target proof release',
 'old_routine_timing':'Cech program was written after target release; the uniform two-dimensional local-algebra representation was added after reading the isolated E17 old Groebner routine',
 'local_algebra_representation':{'z':'zero 2x2 matrix','epsilon':'E21','all_orders_map':'rho(f)=f(0,0)I + partial_epsilon f(0,0)E21',
  'nonmembership_witness':'rho(epsilon)e1=e2 is nonzero; all defining relations and z^N for every N>=1 map to zero'},
 'method':'construct the actual Laurent Cech boundary from both chart bases; choose pivots by the image-exponent union; add the square-zero skyscraper as a zero-differential summand',
 'universal_argument':{
  'excluded_tail_contraction':'each exponent beyond the retained interval is the image of a unique finite- or infinity-chart basis term, so deleting those paired terms preserves cohomology',
  'k_ge_1':'image intervals disjoint, kernel 0, missing exponents -k<n<0 have cardinality k-1',
  'k_le_0':'image intervals cover the target, overlap 0<=n<=-k has cardinality 1-k',
  'embedded_summand':'one degree-zero basis vector epsilon with zero differential, for every k'},
 'matrix_samples':samples,'sample_scope':'exact checks of the universal pivot formulas, not an inference from a finite range',
 'formula_h0':'max(1-k,0)+1','formula_h1':'max(k-1,0)',
 'new_independent_event_count':0,'all_assertions_passed':True},indent=2))
