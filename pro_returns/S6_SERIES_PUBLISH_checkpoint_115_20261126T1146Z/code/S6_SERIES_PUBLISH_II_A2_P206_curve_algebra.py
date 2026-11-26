#!/usr/bin/env python3
"""Post-reading exact calculations for P206 and the positive-Euler P4.40.

These are computations of finite-dimensional cotangent spaces and actual
polynomial restriction maps. They do not certify the analytic ring theorem,
proper conductor pushout, monodromy comparison or global counterexample.
The original P4.40 proof was read before this program was written.
"""
import itertools
import json
import sympy as s


def columns(vectors, r):
    return s.Matrix.hstack(*vectors) if vectors else s.zeros(r, 0)


def coordinate_product(a, b):
    return s.Matrix([a[i]*b[i] for i in range(len(a))])


rows=[]
for r, nonzero in [(1,1),(2,1),(3,1),(2,2),(3,2),(3,3)]:
    coeff=s.Matrix([[1]*nonzero+[0]*(r-nonzero)])
    h=coeff.nullspace()
    e=[s.eye(r)[:,i] for i in range(r)]
    mu2=columns([coordinate_product(a,b)
                 for a,b in itertools.combinations_with_replacement(h,2)],r)
    mu3=columns([coordinate_product(a,b) for a in h for b in e],r)
    # A contains all degree >=2 branch terms. In m_A/m_A^2, degree
    # one has H, degree two is C^r/(H.H), and degree three is
    # C^r/(H.C^r). All degree >=4 terms are products of two
    # terms of degree >=2, so there is no omitted later quotient.
    cotangent=len(h)+(r-mu2.rank())+(r-mu3.rank())
    expected=(r+1 if nonzero==1 else r if nonzero==2 else 2)
    assert cotangent==expected
    rows.append({'branches':r,'nonzero_hyperplane_coefficients':nonzero,
                 'first_jet_basis':[list(v) for v in h],
                 'product_rank_degree_2':mu2.rank(),
                 'product_rank_degree_3':mu3.rank(),
                 'embedding_dimension':cotangent,
                 'embeds_in_dimension_three':cotangent<=3})

t,x,y=s.symbols('t x y')
# The restriction maps, rather than merely the names of singularities.
cusp=[t**2,t**3]
assert s.expand(cusp[1]**2-cusp[0]**3)==0
tacnode=[(t,t**2),(t,-t**2)]
for a,b in tacnode:
    assert s.expand((y*y-x**4).subs({x:a,y:b}, simultaneous=True))==0
# For the remainder G+yH, restriction is (G+t^2H,G-t^2H).
G,H=s.symbols('G H')
restriction=s.Matrix([[1,t*t],[1,-t*t]])
inverse=s.Matrix([[s.Rational(1,2),s.Rational(1,2)],
                  [1/(2*t*t),-1/(2*t*t)]])
assert s.simplify(inverse*restriction)==s.eye(2)
assert s.expand((G+t*t*H)+(G-t*t*H))==2*G

triple=[(t,0),(0,t),(t,t)]
second=[x*x-x*y,y*y-x*y,x*y]
matrix=s.Matrix([[s.expand(poly.subs({x:a,y:b}, simultaneous=True)).coeff(t,2)
                  for poly in second] for a,b in triple])
assert matrix==s.eye(3)
for a,b in triple:
    assert s.expand((x*y*(x-y)).subs({x:a,y:b}, simultaneous=True))==0
first=s.Matrix([[a.coeff(t) if hasattr(a,'coeff') else 0,
                 b.coeff(t) if hasattr(b,'coeff') else 0] for a,b in triple])
assert s.Matrix([[1,1,-1]])*first==s.zeros(1,2)
assert first.rank()==2

# The local length is the independent r-1 constant identifications
# plus one first-derivative relation, giving delta=r for all six rows.
for row in rows:
    row['delta']=(row['branches']-1)+1
    row['excess']=row['delta']-(row['branches']-1)
    assert row['excess']==1

# In the positive-Euler application, n+1-b<=2 and b<=1 imply n<=2.
# The retained meridian argument excludes b=0; the acyclic-conductor
# theorem excludes (n,b)=(1,1). Those are analytic inputs, not proved here.
possibilities=[(n,b) for n in range(1,3) for b in range(2)
               if n+1-b<=2 and b!=0 and (n,b)!=(1,1)]
assert possibilities==[(2,1)]
n,b=possibilities[0]
delta_sum=n+1
branch_identification_sum=n-1+b
excess_sum=delta_sum-branch_identification_sum
assert (delta_sum,branch_identification_sum,excess_sum)==(3,2,1)

out={
 'timing':'post-reading P4.40 original proof; no independent derivation claim',
 'cotangent_spaces':rows,
 'cusp_map':['x=t^2','y=t^3'],
 'tacnode_map':[[str(a),str(b)] for a,b in tacnode],
 'tacnode_restriction_inverse':[[str(z) for z in inverse.row(i)] for i in range(2)],
 'tacnode_inverse_scope':'(f1-f2)/(2*t^2) is convergent because constants and first derivatives agree',
 'triple_map':[[str(a),str(b)] for a,b in triple],
 'triple_independent_second_jet_polynomials':[str(p) for p in second],
 'triple_second_jet_restriction_matrix':matrix.tolist(),
 'global_Euler_arithmetic':{'remaining_n_b':possibilities,
     'delta_sum':delta_sum,'branch_identification_sum':branch_identification_sum,
     'excess_sum':excess_sum,'maximum_local_branches':branch_identification_sum+1},
 'not_certified_by_program':[
   'Convergent analytic generation and lifting to ambient coordinate changes',
   'The exact conductor pushout and its fundamental-group comparison',
   'The meridian theorem and global nonnegative fibrewise Euler bound',
   'The compact counterexample or either complete corrected theorem'],
 'events_added':0}
print(json.dumps(out,indent=2,default=str))
