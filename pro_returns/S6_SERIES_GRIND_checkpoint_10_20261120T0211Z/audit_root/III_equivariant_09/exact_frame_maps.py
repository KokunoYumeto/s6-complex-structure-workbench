"""Root's new post-reading exact check of the two concrete frame maps.

No other producer or saved calculation is read. This checks symbolic maps,
weights and the local four-preimage degree certificate; the Borel integral
and actual-collar arguments remain written mathematical proofs.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

P=Path(__file__).parent
a,b,ab,bb,s,e,x,t=S.symbols('a b abar bbar s epsilon x t')
checks=[]
def check(name,truth):
    assert truth,name
    checks.append(name)
def zero(expr):
    return S.expand(S.together(expr).as_numer_denom()[0])==0
def matrix_equal(name,left,right):
    for i in range(left.rows):
        for j in range(left.cols):check(f'{name}[{i},{j}]',zero(left[i,j]-right[i,j]))

roots=[2*x,-x+t,-x-t]
check('equivariant first Chern root sum',S.expand(sum(roots))==0)
c2=sum(roots[i]*roots[j] for i in range(3) for j in range(i+1,3))
check('equivariant c2 before x-square relation',S.expand(c2+3*x*x+t*t)==0)
check('equivariant p1 before x-square relation',S.expand(sum(r*r for r in roots)-6*x*x-2*t*t)==0)
check('representation roots have same lambda',S.expand((0**2+t*t+(-t)**2)/2-t*t)==0)
fundc2=-x*x
adjc2=(2*x)*(-2*x)
check('adjoint complexification c2 factor4',S.expand(adjc2-4*fundc2)==0)
check('adjoint real lambda stable factor2',S.expand(-adjc2/2+2*fundc2)==0)

A=-a*bb+e*bb**2; B=b*ab+e*ab**2
Ac=-ab*b+e*b**2; Bc=bb*a+e*a**2
M2=S.Matrix([[B,Ac],[-A,Bc]])
M1=S.Matrix([[ab,-b],[bb,a]])
M1adj=S.Matrix([[a,b],[-bb,ab]])
unit=a*ab+b*bb
matrix_equal('A1 adjugate inverse',M1*M1adj,unit*S.eye(2))
check('A1 exact unit determinant',S.expand(M1.det()-unit)==0)
norm=S.expand(A*Ac+B*Bc)
check('A2 unnormalized determinant',S.expand(M2.det()-norm)==0)
matrix_equal('A2 Hermitian norm',S.Matrix([[Bc,-Ac],[A,B]])*M2,norm*S.eye(2))

action={a:a/s,b:b*s,ab:ab*s,bb:bb/s}
D1=S.diag(s,1/s);D2=S.diag(s**2,1/s**2)
matrix_equal('A1 exact action',M1.subs(action,simultaneous=True),D1*M1)
matrix_equal('A2 exact action',M2.subs(action,simultaneous=True),D2*M2)
check('A2 norm invariant',zero(norm.subs(action,simultaneous=True)-norm))
C=M2*M1adj
matrix_equal('weight2 to weight1 adapter',C.subs(action,simultaneous=True),D2*C*D1.inv())
check('adapter determinant',S.expand(C.det()-norm*unit)==0)

# The Hopf coordinate used in both relative maps is (abar,b).
v=S.Matrix([ab,b]);matrix_equal('literal scalar Hopf coordinate',v.subs(action,simultaneous=True),s*v)
# In the non-axis common-zero case the two equations imply a=-epsilon^2*a.
check('common-zero linear elimination',S.expand((a-e*b)+(e*(b+e*a))-(1+e**2)*a)==0)
check('first axis A2 has nonzero epsilon coefficient',S.expand(B.subs({b:0,bb:0})-e*ab**2)==0)
check('second axis A2 has nonzero epsilon coefficient',S.expand(A.subs({a:0,ab:0})-e*bb**2)==0)

# Four exact preimages of the regular diagonal target for (z1^2,-z2^2).
z1,z2=S.symbols('z1 z2');Q=S.Matrix([z1*z1,-z2*z2]);J=Q.jacobian([z1,z2])
preimages=[]
for i in [-1,1]:
 for j in [-1,1]:
  u=S.Rational(1,2)**S.Rational(1,2)*i
  v0=S.I*S.Rational(1,2)**S.Rational(1,2)*j
  vals={z1:u,z2:v0};q=Q.subs(vals)
  check(f'quadratic preimage {i},{j}',q==S.Matrix([S.Rational(1,2),S.Rational(1,2)]))
  check(f'unit sphere preimage {i},{j}',S.simplify(u*S.conjugate(u)+v0*S.conjugate(v0))==1)
  det=S.simplify(J.det().subs(vals))
  check(f'positive real local degree {i},{j}',S.simplify(det*S.conjugate(det))==4)
  preimages.append([str(u),str(v0)])

report={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','assertions':len(checks),'checks':checks,
 'preimages_of_normalized_diagonal':preimages,
 'degree_scope':'The four nonzero complex-Jacobian preimages and homogeneous radial normalization give degree4 for the quadratic pair. Simultaneous conjugation has real determinant+1. A1 has degree1, so the displayed group product has degree3.',
 'scope':'Exact current universal frame/action/characteristic identities, after root read both frozen proofs. No historical producer/output imported; no global collar, localization or integral spectral-sequence proof is replaced by code.',
 'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'exact_frame_maps.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'assertions':len(checks),'program_sha256':report['program_sha256']}))
