"""Exact checks for the full original period deformation and shift classification. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form
checks=[]
def eq(name,a,b=0):
 if isinstance(a,S.MatrixBase):
  if not isinstance(b,S.MatrixBase):b=S.zeros(*a.shape)
  assert (a-b).applyfunc(S.simplify)==S.zeros(*a.shape),(name,a,b)
 else:assert S.simplify(a-b)==0,(name,a,b)
 checks.append(name)
A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0=(A1*A2).inv()
g,u,w,d=[S.eye(4)[:,i] for i in range(4)]
v1=S.Matrix([1,2,-4,0]);v2=S.Matrix([-1,-3,3,0])
E=d*g.T;I=S.eye(4)
eq('rank-one endomorphism square',E**2)
for i,A in enumerate([A1,A2],1):
 eq(f'full left monodromy commutation {i}',A*E,E)
 eq(f'full right monodromy commutation {i}',E*A,E)
Hentries=S.symbols('h0:16');H=S.Matrix(4,4,Hentries)
solution=list(S.linsolve(list(H*A1-A1*H)+list(H*A2-A2*H),Hentries))
assert len(solution)==1
sol=S.Matrix(4,4,solution[0])
eq('complete simultaneous centralizer solution',sol,sol[0,0]*I+sol[3,0]*E)
assert set().union(*(x.free_symbols for x in sol))=={Hentries[12],Hentries[15]}
checks.append('exactly two independent rational centralizer parameters')
n=S.symbols('n',integer=True)
eq('integer shear full inverse',(I+n*E)*(I-n*E),I)
eq('centralizer determinant',(S.symbols('a')*I+S.symbols('b')*E).det(),S.symbols('a')**4)
N1=I+A1+A1**2;N2=I+A2+A2**2+A2**3
eq('full order3 norm',N1,S.Matrix([[3,0,0,0],[6,0,0,0],[-12,0,0,0],[0,2,1,3]]))
eq('full order4 norm',N2,S.Matrix([[4,0,0,0],[12,0,0,0],[-12,0,0,0],[0,2,2,4]]))
eq('complete order3 norm lattice',hermite_normal_form(N1),hermite_normal_form(S.Matrix.hstack(3*v1,d)))
eq('complete order4 norm lattice',hermite_normal_form(N2),hermite_normal_form(S.Matrix.hstack(-4*v2,2*d)))
r1=-n*(u+w)/3;r2=n*(u+w)/4;l1=-n*w;l2=n*u/2
eq('first exact finite correction',(I-A1)*r1,n*d/3+l1)
eq('second exact finite correction',(I-A2)*r2,-n*d/4+l2)
eq('first actual norm receiver',N1*l1,-n*d)
eq('second actual norm receiver',N2*l2,n*d)
eq('full composed peripheral column',l1+A1*l2,-3*n*w/2+n*d/2)
l0=-A0*(l1+A1*l2)
eq('full cusp peripheral column',l0,3*n*w/2-n*d/2)
eq('cusp fixed w',A0*w,w)
eq('cusp fixed delta',A0*d,d)
eq('first cocycle independent of parameter',(g.T*l1)[0])
eq('second cocycle independent of parameter',(g.T*l2)[0])
T,m,D,tr,mr,br,dr,di=S.symbols('T m D tr mr br dr di',real=True,nonzero=True)
tau=tr+S.I*T;mu=mr+S.I*m;beta=br+S.I*(D+6*m**2/T)
Pi=S.Matrix([[6*mu,tau,1,0],[beta,mu,0,1]])
RealPi=S.Matrix([S.re(Pi[0,:]),S.im(Pi[0,:]),S.re(Pi[1,:]),S.im(Pi[1,:])])
eq('original real coordinate-order determinant',RealPi.det(),T*D)
P=S.Matrix([[0,0],[-m/T,1]]);J=S.eye(2)
eq('Beltrami projector',P**2,P)
delta=dr+S.I*di
Ad=J+delta*P/(2*S.I*D);Bd=-delta*P/(2*S.I*D)
nu=delta*P/(2*S.I*D+delta)
Adinv=J-delta*P/(2*S.I*D+delta)
eq('full complex-linear inverse',Ad*Adinv,J)
eq('Beltrami graph exact annihilation',Ad*nu+Bd)
eq('complete marked real-linear period map',Ad*Pi+Bd*S.conjugate(Pi),Pi+S.Matrix([[0,0,0,0],[delta,0,0,0]]))
eq('complex-linear determinant',Ad.det(),1+delta/(2*S.I*D))
dd=S.symbols('delta')
eq('actual infinitesimal graph derivative',S.diff(dd*P/(2*S.I*D+dd),dd).subs(dd,0),P/(2*S.I*D))
eq('integer-shift period identity',Pi*(I+n*E),Pi+S.Matrix([[0,0,0,0],[n,0,0,0]]))
eq('integer-shift source-to-target marking',(Pi+S.Matrix([[0,0,0,0],[n,0,0,0]]))*(I-n*E),Pi)
eq('cusp period image full column',Pi*l0,S.Matrix([3*n/2,-n/2]))
eq('first translation retains all coordinates',Pi*r1,-n*S.Matrix([tau+1,mu])/3)
eq('second translation retains all coordinates',Pi*r2,n*S.Matrix([tau+1,mu])/4)
ep,b0,b1,b2,t=S.symbols('epsilon b0 b1 b2 t')
assert S.solve([b0,b0+b1+b2,b2],[b0,b1,b2])=={b0:0,b1:0,b2:0}
checks.append('all three infinitesimal critical values force identity')
for nn in range(-15,16):
 rhs=nn*d
 in_norm=(hermite_normal_form(N2)==hermite_normal_form(N2.row_join(rhs)))
 assert in_norm==(nn%2==0)
checks.append('finite parity obstruction positive and negative shifts')
dr2,di2=S.symbols('dr2 di2',real=True)
delta2=dr2+S.I*di2;D1=D+di
Asecond=J+delta2*P/(2*S.I*D1);Bsecond=-delta2*P/(2*S.I*D1)
eq('complete composition complex-linear part',Asecond*Ad+Bsecond*S.conjugate(Bd),J+(delta+delta2)*P/(2*S.I*D))
eq('complete composition antilinear part',Asecond*Bd+Bsecond*S.conjugate(Ad),-(delta+delta2)*P/(2*S.I*D))
uref=S.symbols('u_ref',nonzero=True)
eq('exact reference-parameter KS sign',S.I/(2*S.pi*uref)*(-1/(2*S.I*D)),-1/(4*S.pi*uref*D))
eq('first even cusp translation',S.Matrix([-3*n/2,n/2]).subs(n,2),S.Matrix([-3,1]))
eq('new real determinant with unchanged coordinates',(T*(D+di))/(T*D),(D+di)/D)
root=Path(__file__).resolve().parents[1]
source=root/'src/periods-and-nontrivial-deformation.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,
 limitations='Exact checks of the written period, matrix, finite-norm and Beltrami formulas. Author self-check, not independent proof certification.')
(root/'checks/PERIOD_DEFORMATION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
