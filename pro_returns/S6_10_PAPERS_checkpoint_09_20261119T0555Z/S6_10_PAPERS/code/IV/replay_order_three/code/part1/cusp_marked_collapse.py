"""Mark the graded collapse by H_1=(a1,a2,a3,b1,b2,b3), N b_i=a_i.
Tests whether the proposed orbit model's canonical collapse is invariant under
that specified monodromy. Failure is retained as a geometric diagnostic.
"""
from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('cusp_collapse.py').read_text().replace("Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,default=int))",''))

def sign_perm(x):return (-1)**sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x)))
def base_cycle(J):
 sdim=len(J);p=3-sdim;K=tuple(i for i in range(3) if i not in J)
 # PD b_J corresponds to dx_K with orientation sign (J,K).
 eps=sign_perm(tuple(J)+K)
 coeff=[]
 for c in cells[p]:
  v=eps
  for j,k in enumerate(K):v*=c[j+1][k]-c[j][k]
  coeff.append(v)
 return s.Matrix(coeff)

Mstd=s.eye(6)
for j in range(3):Mstd[j,j+3]=1
maps={}
for degree in range(7):
 blocks=[]
 for q in range(4):
  sdim=degree-q;p=3-sdim
  if not 0<=p<=3:continue
  nt=len(cells[p])*s.binomial(3-p,q)
  ta=D[p,q] if p<3 else s.zeros(0,nt);tb=D[p-1,q] if p else s.zeros(nt,0)
  tz,tpi=presentation(ta,tb)
  H=s.zeros(tz.cols,s.binomial(6,degree))
  P=s.diag(*[wedge(Q[p,i],q) for i in range(len(cells[p]))])
  for col,ij in enumerate(combinations(range(6),degree)):
   I=tuple(i for i in ij if i<3);J=tuple(i-3 for i in ij if i>=3)
   if len(I)!=q:continue
   v=s.zeros(s.binomial(3,q),1);v[list(combinations(range(3),q)).index(I)]=1
   z=(-1)**(q*sdim)*s.kronecker_product(base_cycle(J),v)
   H[:,col]=tpi*P*z
  blocks.append(H)
 C=s.Matrix.vstack(*blocks);maps[degree]=C
 Dm=wedge(Mstd,degree)-s.eye(s.binomial(6,degree))
 print('degree',degree,'map',C,'rank',C.rank(),'M_invariance',C*Dm==s.zeros(C.rows,Dm.cols))
 print('invariance_error',C*Dm)
 print('image_smith',snf(C)[0])
Path(__file__).with_suffix('.json').write_text(json.dumps({str(k):m.tolist() for k,m in maps.items()},indent=2,default=int))
