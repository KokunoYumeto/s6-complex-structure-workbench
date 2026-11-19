"""Fresh exact linear algebra from supplied matrix data, independent of old code."""
from pathlib import Path
import json
from math import gcd
from functools import reduce
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parents[4]
src=ROOT/'materials/S6_08_PAPERS_2_returns_code/returns/S6_04_MAPS_MANIFOLDS/records/fourfolds_marked_survivor_input.json'
if not src.exists():
    ROOT=ROOT.parent
    src=ROOT/'materials/S6_08_PAPERS_2_returns_code/returns/S6_04_MAPS_MANIFOLDS/records/fourfolds_marked_survivor_input.json'
data=json.loads(src.read_text())
Ms=[s.Matrix(m) for m in data['matrices']];n=6;I=s.eye(n)
def smith(A):
    D=smith_normal_form(A,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
def cokernel(A):
    ds=smith(A);return {'free_rank':A.rows-len(ds),'torsion':[d for d in ds if d>1],'smith_nonzero':ds}
N=(Ms[0]*Ms[1]).inv()-I
assert N*N==s.zeros(n)
assert N.rank()==3 and smith(N)==[1,1,1]
rec=[]
for M,v,order in zip(Ms,data['numerators'],data['orders']):
    assert M**order==I and all(M**d!=I for d in range(1,order))
    assert (M*s.Matrix(v)-s.Matrix(v))==s.zeros(n,1)
    cols=(M-I).col_join(s.zeros(1,n)).row_join(s.Matrix(v+[-order]))
    rec.append({'order':order,'charpoly':str(s.factor(M.charpoly().as_expr())),
      'first_coordinate_power_translations':[str(s.Rational(v[0]*j,order)%1) for j in range(1,order)],
      'finite_filling_H1':cokernel(cols)})

# Solve ZM=MZ in 36 variables, collecting all exact equations.
zs=s.symbols('z0:36');Z=s.Matrix(6,6,zs)
equations=[entry for M in Ms for entry in Z*M-M*Z]
coeff,_=s.linear_eq_to_matrix(equations,zs)
centralizer=[s.Matrix(6,6,v) for v in coeff.nullspace()]
out={'input_file':str(src),'homology':{
    'invariants_rank':len((Ms[0]-I).col_join(Ms[1]-I).nullspace()),
    'coinvariants':cokernel((Ms[0]-I).row_join(Ms[1]-I))},
    'cohomology':{'invariants_rank':len((Ms[0].T-I).col_join(Ms[1].T-I).nullspace()),
    'coinvariants':cokernel((Ms[0].T-I).row_join(Ms[1].T-I))},
    'cusp_smith':smith(N),'finite':rec,
    'rational_centralizer_dimension':len(centralizer),
    'rational_centralizer_basis':[[list(z.row(i)) for i in range(6)] for z in centralizer]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str))
print(json.dumps(out,indent=2,default=str))
