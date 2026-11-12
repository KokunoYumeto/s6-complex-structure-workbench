"""Finite exact tests of the receiving Whitney formulas; no global proof certificate."""
from pathlib import Path
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,ok):
 assert bool(ok),name
 checks.append(name)
def zero(M):return all(S.simplify(x)==0 for x in M)
def qm(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return S.Matrix([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0])
def qc(a):return S.diag(1,-1,-1,-1)*a
a=S.Matrix(S.symbols('a0:4'));b=S.Matrix(S.symbols('b0:4'));c=S.Matrix(S.symbols('c0:4'))
ck('Quaternion associativity with all coefficients',zero(qm(qm(a,b),c)-qm(a,qm(b,c))))
ck('Full quaternion norm identity',S.expand(qm(a,b).dot(qm(a,b))-a.dot(a)*b.dot(b))==0)
ck('Quaternion conjugation reverses order',zero(qc(qm(a,b))-qm(qc(b),qc(a))))
e=[S.eye(4)[:,j] for j in range(4)]
def rho(a,b):return S.Matrix.hstack(*[qm(qm(a,x),qc(b)) for x in e])
ck('Spin-four composition retains both orders',zero(rho(a,b)*rho(c,e[0])-rho(qm(a,c),b)))
der=[S.Matrix.hstack(*[qm(e[j],x) for x in e]) for j in range(1,4)]
der += [S.Matrix.hstack(*[-qm(x,e[j]) for x in e]) for j in range(1,4)]
ck('Six infinitesimal left/right generators independent',S.Matrix.hstack(*[M.reshape(16,1) for M in der]).rank()==6)
for j,M in enumerate(der):ck(f'Infinitesimal generator {j+1} skew',M+M.T==S.zeros(4))
theta=S.symbols('theta',real=True);ct=S.cos(theta);st=S.sin(theta)
half=S.Matrix([S.cos(theta/2),S.sin(theta/2),0,0])
rot=S.Matrix([[ct,-st],[st,ct]])
ck('Opposite right lift gives full (1,i) rotation',zero(rho(half,qc(half))-S.diag(rot,S.eye(2))))
Q=S.diag(S.eye(2),rot)
ck('Equal quaternion lifts give full (j,k) rotation',zero(rho(half,half)-Q))
ck('Full rotation has negative lifted endpoint',half.subs(theta,2*S.pi)==-e[0])
ck('Central negative pair acts trivially',rho(-e[0],-e[0])==S.eye(4))
T=S.Matrix([[2,1,4,-2],[0,3,1,5],[0,0,5,0],[0,0,0,5]])
R=Q*T;corrected=Q*T*Q
answer=S.Matrix([[2,1,4*ct-2*st,-4*st-2*ct],[0,3,ct+5*st,-st+5*ct],[0,0,5*S.cos(2*theta),-5*S.sin(2*theta)],[0,0,5*S.sin(2*theta),5*S.cos(2*theta)]])
gram=S.Matrix([[4,2,8,-4],[2,10,7,13],[8,7,42,-3],[-4,13,-3,54]])
ck('Exercise full corrected frame',zero(corrected-answer))
ck('Correction fixes both specified original columns',zero(corrected[:,:2]-R[:,:2]))
ck('Original full Gram with mixed entries',zero(R.T*R-gram))
ck('Corrected full Gram comparison',zero(corrected.T*corrected-Q.T*gram*Q))
ck('Original and corrected determinants',S.trigsimp(R.det())==150 and S.trigsimp(corrected.det())==150)
for d,p,q in [(5,2,3),(6,2,4),(6,3,3)]:
 ck(f'All relative disk inequalities {(d,p,q)}',1+p-1<d and 2+p-1<d and 2+p<d and 4<d and d-1>2 and 2*d>2)
 slope=S.symbols('slope')
 Ac=S.eye(d)[:,0]+slope*S.eye(d)[:,1]
 Bc=S.eye(d)[:,0]
 tangent=S.Matrix.hstack(Ac,*[S.eye(d)[:,j] for j in range(2,p+1)],Bc,*[S.eye(d)[:,j] for j in range(p+1,d)])
 ck(f'Ordered sheet determinant p={p} q={q}',S.expand(tangent.det()-(-1)**p*slope)==0)
 order=[0]+list(range(2,p+1))+[1]+list(range(p+1,d))
 ck(f'Original corner permutation p={p} q={q}',S.eye(d)[:,order].det()==(-1)**(p-1))
 # A dense, positive original metric and an independent complete corner frame.
 M=S.Matrix(d,d,lambda i,j: 1+(i+1)*(j+2) if i!=j else 4+(i+1)*(j+2))
 G=M.T*M+S.diag(*range(2,d+2))
 F=S.eye(d)
 for i in range(d):
  for j in range(i+1,d):F[i,j]=i+j+1
 V0=F[:,:2];B=F[:,2:]
 Bp=B-V0*(V0.T*G*V0).inv()*V0.T*G*B
 schur=B.T*G*B-B.T*G*V0*(V0.T*G*V0).inv()*V0.T*G*B
 ck(f'Exact metric orthogonality rank {d-2} p={p}',V0.T*G*Bp==S.zeros(2,d-2))
 ck(f'Full Schur Gram rank {d-2} p={p}',Bp.T*G*Bp==schur)
 ck(f'Corner orientation retained rank {d-2} p={p}',S.Matrix.hstack(V0,Bp).det()==F.det())
 ck(f'Schur leading minors positive rank {d-2} p={p}',all(schur[:j,:j].det()>0 for j in range(1,d-1)))
 shear=S.Matrix(2,d-2,lambda i,j:(i+1)*(j+2))
 parameter=S.symbols('s')
 J=S.eye(d);J[:2,2:]=parameter*shear
 ck(f'Complete corner shear inverse rank {d-2} p={p}',J*J.subs(parameter,-parameter)==S.eye(d))
 ck(f'Complete corner shear determinant rank {d-2} p={p}',J.det()==1)
x,y,t,R0,d0,b0=S.symbols('x y t R d0 b0',positive=True)
chi=S.Function('chi')
phi=R0**2-x*x;u=4*phi/d0+2;delta=chi(u)*(phi+d0)
L=(y+2*d0)/d0;H=(phi+d0-y)/d0
eta=chi(L)*chi(H)
cp=lambda arg:S.Subs(S.Derivative(chi(S.Symbol('h')),S.Symbol('h')),S.Symbol('h'),arg).doit()
ck('Full longitudinal cutoff derivative',S.simplify(S.diff(delta,x)+2*x*(chi(u)+4*(phi+d0)/d0*cp(u)))==0)
ck('Full upper-edge cutoff derivative',S.simplify(S.diff(eta,x)+2*x/d0*chi(L)*cp(H))==0)
ck('Both vertical cutoff derivatives',S.simplify(S.diff(eta,y)-(cp(L)*chi(H)-chi(L)*cp(H))/d0)==0)
for rank in [3,4]:
 z=S.symbols('z0:'+str(rank),real=True)
 Z=2-2*sum(a*a for a in z)/b0**2;zeta=chi(Z)
 for nu in range(rank):ck(f'Full normal cutoff derivative rank {rank} column {nu}',S.simplify(S.diff(zeta,z[nu])+4*z[nu]/b0**2*cp(Z))==0)
 v=delta*eta*zeta
 ck(f'Full longitudinal field derivative rank {rank}',S.simplify(S.diff(v,x)-(S.diff(delta,x)*eta+delta*S.diff(eta,x))*zeta)==0)
 Jt=S.symbols('Jt',positive=True);Yx=S.symbols('Yx');Yz=S.symbols('Yz0:'+str(rank))
 J=S.eye(rank+2);J[1,0]=Yx;J[1,1]=Jt
 for j in range(rank):J[1,j+2]=Yz[j]
 ck(f'All mixed flow derivatives determinant rank {rank}',J.det()==Jt)
 inv=S.eye(rank+2);inv[1,0]=-Yx/Jt;inv[1,1]=1/Jt
 for j in range(rank):inv[1,j+2]=-Yz[j]/Jt
 ck(f'All mixed flow derivatives inverse rank {rank}',J*inv==S.eye(rank+2))
f=(1-t)*phi-t*d0;tstar=R0**2/(R0**2+d0)
ck('Exact coalescence equation',S.simplify(f.subs({x:0,t:tstar}))==0)
ck('Nonzero second derivative retains both parameters',S.simplify(S.diff(f,x,2).subs(t,tstar)+2*d0/(R0**2+d0))==0)
ck('Nonzero time derivative retains both parameters',S.diff(f,t).subs(x,0)==-R0**2-d0)
ck('Two prescribed roots',S.simplify(f.subs(x*x,R0**2-t*d0/(1-t)))==0)
ck('No core intersection after time one',S.expand(f.subs(t,1))==-d0)
ck('Exercise exact cancellation time',tstar.subs({R0:3,d0:2})==S.Rational(9,11))
ck('Exercise two intersections',all(S.simplify(f.subs({R0:3,d0:2,t:S.Rational(1,2),x:sign*S.sqrt(7)}))==0 for sign in [-1,1]))
ck('Exercise odd-dimensional sheet sign',S.diff(f,x).subs(t,S.Rational(1,2))*(-1)**3==x)
ck('Full chain rule includes old sheet slope',S.simplify(2*t*x+S.diff(phi,x)-S.diff(f,x))==0)
ck('Exercise second and time derivatives',S.diff(f,x,2).subs({R0:3,d0:2,t:S.Rational(9,11)})==-S.Rational(4,11) and S.diff(f,t).subs({R0:3,d0:2,x:0})==-11)
src=W/'src/whitney-moves-in-the-receiving-dimensions.md'
result=dict(passed=len(checks),checks=checks,source=src.name,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),scope='Finite exact quaternion, full metric, cutoff, sheet-orientation and exercise calculations. Does not certify the global topological proof.')
(W/'checks/RECEIVING_WHITNEY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
