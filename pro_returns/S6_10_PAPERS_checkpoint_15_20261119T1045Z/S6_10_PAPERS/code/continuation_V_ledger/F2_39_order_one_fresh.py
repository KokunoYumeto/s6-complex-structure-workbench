import sympy as S
from pathlib import Path
import json
checks=[]
def ck(n,v):
 assert v,n
 checks.append(n)
def comp(f,g):
 A,a=f;B,b=g
 return A*B,A*b+a
def product(items,n=6):
 out=(S.eye(n),S.zeros(n,1))
 for f in items:out=comp(out,f)
 return out
P=S.Matrix([[-1,1],[0,1]]);Q=S.Matrix([[-1,0],[0,1]])
M=S.diag(P,P,P);N=S.diag(Q,Q,Q);I=S.eye(6)
ck('first_finite_matrix',M*M==I);ck('second_finite_matrix',N*N==I)
cusp=(M*N).inv();nil=cusp-I
ck('actual_nontrivial_square_zero_cusp',nil*nil==S.zeros(6) and nil.rank()==3)
for q in range(1,13):ck(f'cusp_power_{q}',cusp**q==I+q*nil and cusp**q!=I)
for pos in range(3):
 for vnum in range(1,5):
  v=S.Matrix([vnum,-vnum,1,2,-1,3]);kap=S.Matrix([2,-1,0,1,3,-2])
  items=[(M,S.Matrix([S.Rational(1,2),0,0,1,0,0])),(N,S.Matrix([0,S.Rational(1,3),0,0,2,0]))]
  items.insert(pos,(I,v));full=product(items);red=product(items[:pos]+items[pos+1:]);B,b=product(items[pos+1:]);delta=B.inv()*v
  name=f'position{pos+1}_v{vnum}'
  ck('linear_cusp_unchanged_'+name,full[0]==red[0])
  ck('actual_affine_clutch_'+name,comp(full,(I,kap))==comp(red,(I,kap+delta)))
  x=S.Matrix(S.symbols('x0:6'));suffix_inverse=lambda y:B.inv()*(y-b)
  ck('actual_suffix_conjugation_'+name,suffix_inverse(B*x+b+v)==x+delta)
  tt=S.symbols('theta');F=lambda x,t:x+t*v
  ck('marked_collar_seam_'+name,F(x,1)==F(x+v,0))
  ck('marked_collar_inverse_'+name,F(x-tt*v,tt)==x)
lam=S.symbols('lambda');C=S.eye(6);C[0,3]=3;C[2,5]=-2
for k,A in enumerate([M,N,cusp]):
 ck(f'charpoly_matrix_identity_{k}',lam*I-C*A*C.inv()==C*(lam*I-A)*C.inv())
 ck(f'charpoly_determinant_identity_{k}',(C*A*C.inv()).charpoly(lam).as_expr()==A.charpoly(lam).as_expr())
out={'result':'PASS','checks':len(checks),'names':checks,'scope':'Exact six-dimensional affine suffix/clutch and collar identities for all3 deletion positions and4 integer vectors; explicit rank3 square-zero cusp powers1..12; characteristic-polynomial identities for3 matrices. No finite test is used to infer the universal geometric/group proof; no full gluing admissibility or specific H1 cone comparison is claimed.'}
p=Path(__file__).with_suffix('.output.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'result':'PASS','checks':len(checks)}))
