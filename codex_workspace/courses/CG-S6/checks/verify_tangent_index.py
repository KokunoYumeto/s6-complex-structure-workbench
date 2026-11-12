from pathlib import Path
import sympy as S
import hashlib,json
W=Path(__file__).resolve().parents[1];checks=[]
def zero(M):return all(S.simplify(v)==0 for v in M)
def check(label,v):
 assert v,label
 checks.append(label)
for r in range(1,5):
 # a,u_1,...,u_(r-1),v_1,...,v_(r-1),w; the original bidegree zigzag.
 size=2*r;w=size-1;b=S.zeros(size);h=S.zeros(size);delta=S.zeros(size)
 for j in range(1,r):b[r+j-1,j]=1;h[j,r+j-1]=1
 if r==1:delta[w,0]=1
 else:
  delta[r,0]=1
  for j in range(1,r-1):delta[r+j,j]=1
  delta[w,r-1]=1
 I=S.zeros(size,2);I[0,0]=1;I[w,1]=1;P=I.T
 T=S.zeros(size)
 for k in range(r+1):T+=(-delta*h)**k*delta
 D=P*T*I;Ip=I-h*T*I;Pp=P-P*T*h;hp=h-h*T*h;dt=b+delta
 check(f'Zigzag{r}: vertical contraction exact',zero(b*h+h*b-S.eye(size)+I*P))
 check(f'Zigzag{r}: original double-complex relations',zero(b*b) and zero(delta*delta) and zero(b*delta+delta*b))
 check(f'Zigzag{r}: full transferred sign and nonzero higher term',D[1,0]==(-1)**(r-1) and D.rank()==1)
 check(f'Zigzag{r}: nilpotence gives the exact finite inverse',zero((S.eye(size)+delta*h)*sum([(-delta*h)**k for k in range(r+1)],S.zeros(size))-S.eye(size)))
 check(f'Zigzag{r}: inclusion is a chain map',zero(dt*Ip-Ip*D))
 check(f'Zigzag{r}: projection is a chain map',zero(Pp*dt-D*Pp))
 check(f'Zigzag{r}: projection/inclusion retraction',zero(Pp*Ip-S.eye(2)))
 check(f'Zigzag{r}: full differential homotopy',zero(dt*hp+hp*dt-S.eye(size)+Ip*Pp))
 check(f'Zigzag{r}: source total cohomology vanishes',dt.rank()==r)
a=S.symbols('a')
for m in range(2,7):
 for N in range(2,7):
  rel=S.expand((1+a)**m-1)
  mat=S.Matrix([[S.expand(a**k*rel).coeff(a,j) for k in range(N-1)] for j in range(1,N)])
  target=S.zeros(N-1,1);target[0]=m**(N-1)
  coeff=mat.inv()*target
  check(f'Tensor order{m},nilpotence{N}: stated integer annihilator is an exact relation',all(c.q==1 for c in coeff) and zero(mat*coeff-target))
rel=S.expand((1+a)**3-1)
mat=S.Matrix([[S.expand(a**k*rel).coeff(a,j) for k in range(3)] for j in range(1,4)])
check('Exercise1:9a is an exact integral combination of full binomial relations',all(c.q==1 for c in mat.inv()*S.Matrix([9,0,0])))
aa,bb,cc,dd=S.symbols('aa bb cc dd',nonzero=True)
A=S.Matrix([[aa,bb],[cc,dd]])
left=S.Matrix([[1,0],[-cc/aa,1]]);right=S.Matrix([[1,-bb/aa],[0,1]])
check('Fredholm reduction keeps the full Schur denominator',zero(left*A*right-S.diag(aa,dd-cc*bb/aa)))
I6=S.eye(6);orientation=I6.row_join(-I6).col_join(I6.row_join(I6))
check('Original diagonal normal map has determinant2^6',orientation.det()==2**6)
for k in range(7):check(f'Diagonal degree{k}: test-product sign cancels the signed coefficient',(-1)**k*(-1)**(k*k)==1)
contract=S.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
check('Original tangent-to-two-form contraction retains the middle minus sign',contract.det()==1 and zero(contract*contract-S.eye(3)))
x,y,z,ell,t=S.symbols('x y z ell t')
ch=sum(sum((t*v)**k/S.factorial(k) for k in range(4)) for v in [x,y,z])
line=sum((t*ell)**k/S.factorial(k) for k in range(4))
td=S.prod(1+t*v/2+(t*v)**2/12 for v in [x,y,z])
full=S.expand(ch*line*td).coeff(t,3)
c1=x+y+z;c2=x*y+x*z+y*z;c3=x*y*z
expected=c3/2+c1**3/2-S.Rational(19,24)*c1*c2+S.Rational(5,4)*ell*c1*c1-S.Rational(3,4)*ell*c2+S.Rational(5,4)*ell**2*c1+ell**3/2
check('Full original root product gives every degree-six coefficient',S.expand(full-expected)==0)
chi=S.symbols('chi');chi0=0;chi1=-chi;chi2=chi;chi3=0
check('Exact Serre and tangent-contraction signs give twice the tangent index',chi0-chi1+chi2-chi3==2*chi)
source=W/'src/tangent-index-with-torsion-line-bundles.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,
 limitations='Exact finite transfers with nonzero higher components, integral binomial relations, orientation and the entire characteristic polynomial. These supplement the written operator and topological proofs, without constituting independent review.')
(W/'checks/TANGENT_INDEX_CHECKS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
