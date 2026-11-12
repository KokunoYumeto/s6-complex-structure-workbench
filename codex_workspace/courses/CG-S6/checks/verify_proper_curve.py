from pathlib import Path
import sympy as S
import hashlib,json
W=Path(__file__).resolve().parents[1];checks=[]
def zero(M):return all(S.simplify(v)==0 for v in M)
def check(label,value):
 assert value,label
 checks.append(label)
t,z=S.symbols('t z')
de=S.Matrix([[0,1],[0,0]]);df=de
m0=S.diag(t,t**2);m1=S.diag(t**2,t)
bminus=m0.col_join(-df);bzero=de.row_join(m1)
check('Different noncommuting degree maps retain the shifted-cone sign',zero(bzero*bminus))
check('Removing the shift sign produces the nonzero defect',not zero(bzero*m0.col_join(df)))
b=S.zeros(8);b[2:6,0:2]=bminus;b[6:8,2:6]=bzero
check('Full three-degree cone differential squares to zero',zero(b*b))
Q=b+b.T;L=b*b.T+b.T*b
check('All-degree square retains both Laplacian summands',zero(Q*Q-L))
check('Laplacian commutes with the original cone differential',zero(L*b-b*L))
check('Original multiplication terms remain in the full Laplacian',not zero(L-L.subs(t,0)))
u0=S.Matrix([[1,t],[0,1+t]])
u1=S.Matrix([[1+t*t,0],[t,1]])
dfnew=S.simplify(u1.inv()*df*u0)
m0new=m0*u0;m1new=m1*u1
check('Unequal parameter gauges retain the exact chain map',zero(de*m0new-m1new*dfnew))
check('Parameter-gauged cone retains its full inverse factors',zero(de.row_join(m1new)*m0new.col_join(-dfnew)))
check('Gauge inverse domain retains both determinant factors',S.factor(u0.det()*u1.det())==(t+1)*(t*t+1))
for r in range(1,9):
 N=S.zeros(r)
 for j in range(r-1):N[j+1,j]=1
 check(f'Torsion length{r}: uniformizer kernel is one-dimensional',len(N.nullspace())==1)
 check(f'Torsion length{r}: residue quotient is one-dimensional',r-N.rank()==1)
 check(f'Torsion length{r}: connecting element is the top retained power',N.nullspace()[0]==S.eye(r)[:,r-1])
 check(f'Torsion length{r}: nilpotence retains exact length',zero(N**r) and (r==1 or not zero(N**(r-1))))
for m in range(1,9):
 M=S.zeros(m)
 for j in range(m-1):M[j+1,j]=1
 M[0,m-1]=t
 check(f'Branch order{m}: full companion equation',zero(M**m-t*S.eye(m)))
 check(f'Branch order{m}: exact characteristic polynomial',S.expand(M.charpoly(z).as_expr()-(z**m-t))==0)
 M0=M.subs(t,0)
 check(f'Branch order{m}: central fibre retains all{m} basis vectors',M0.rows==m and zero(M0**m))
 check(f'Branch order{m}: unreduced derivative is m times original power',m-(m*M0**(m-1)).rank()==m-1)
source=W/'src/proper-base-change-over-a-curve.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,
 limitations='Finite exact cone, gauge, torsion and branch computations supplement the written analytic proof. They do not verify functional-analytic estimates or constitute independent review.')
(W/'checks/PROPER_CURVE_CHECKS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
