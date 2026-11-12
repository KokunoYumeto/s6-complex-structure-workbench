"""Exact retained affine phases, norm equations and bundle power identities."""
from pathlib import Path
from itertools import combinations
import sympy as S
import hashlib,json
W=Path(__file__).resolve().parents[1];checks=[]
def check(name,v):assert v,name;checks.append(name)
def zero(v):return all(S.expand(x)==0 for x in v) if isinstance(v,S.MatrixBase) else S.expand(v)==0
a,b=S.symbols('a b',integer=True);xs=S.symbols('x0:4',real=True);ls=S.symbols('l0:4',integer=True);ms=S.symbols('mu0:4',integer=True)
x=S.Matrix(xs);lam=S.Matrix(ls);mu=S.Matrix(ms)
A=[S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]),S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])]
vs=[S.Matrix([1,2,-4,0]),S.Matrix([-1,-3,3,0])]
expectedD=[S.Matrix([[-48*b,0,-6*b,0],[0,0,-b,0],[-6*b,-b,-b,0],[0,0,0,0]]),S.Matrix([[18*b,0,6*b,0],[0,0,-b,0],[6*b,-b,0,0],[0,0,0,0]])]
expectedN=[S.Matrix([[3,0,0,0],[6,0,0,0],[-12,0,0,0],[0,2,1,3]]),S.Matrix([[4,0,0,0],[12,0,0,0],[-12,0,0,0],[0,2,2,4]])]
constants=[58*b/S.Integer(3),81*b/S.Integer(8)];betas=[8*b/S.Integer(9),27*b/S.Integer(32)]
for j,m in enumerate([3,4]):
 vals=[2*a,a,3*a+6*b,b,0,0] if j==0 else [a,a,2*a+6*b,b,0,0]
 C=S.zeros(4)
 for val,(i,k) in zip(vals,combinations(range(4),2)):C[i,k]=val
 E=C-C.T;D=A[j].T*C*A[j]-C;v=vs[j]
 Q=lambda y:sum(D[i,i]*y[i]*(y[i]-1)/2 for i in range(4))+sum(D[i,k]*y[i]*y[k] for i,k in combinations(range(4),2))
 r=A[j].T*C*v/m;R=lambda y:Q(y)+(r.T*y)[0]
 N=sum((A[j]**s for s in range(m)),S.zeros(4))
 ell=S.Matrix([[-22*b,0,0,a+2*b]]) if j==0 else S.Matrix([[9*b,0,0,-(a+3*b)/2]])
 beta=betas[j];phase=lambda y:R(y)+(ell*y)[0]+beta
 check(f'Case{j+1}: original exact order',A[j]**m==S.eye(4) and all(A[j]**s!=S.eye(4) for s in range(1,m)))
 check(f'Case{j+1}: affine power retains v',A[j]*v==v and sum((A[j]**s*v/m for s in range(m)),S.zeros(4,1))==v)
 check(f'Case{j+1}: full alternating Chern form invariant',zero(A[j].T*E*A[j]-E))
 check(f'Case{j+1}: complete polarization matrix',D==expectedD[j] and D==D.T)
 check(f'Case{j+1}: translation cocycle defect is the original integer bilinear term',zero((lam.T*C*(x+mu))[0]+(mu.T*C*x)[0]-((lam+mu).T*C*x)[0]-(lam.T*C*mu)[0]))
 check(f'Case{j+1}: polarization with all diagonal falling factors',zero(Q(x+lam)-Q(x)-(lam.T*D*x)[0]-Q(lam)))
 check(f'Case{j+1}: affine linear factor',r==([S.Matrix([-8*b,0,-4*b/S.Integer(3),0]),S.Matrix([0,0,-3*b/S.Integer(4),0])][j]))
 check(f'Case{j+1}: exact generator/lattice comparison modulo the stated integer',zero((lam.T*C*x)[0]+phase(x+lam)-phase(x)-((A[j]*lam).T*C*(A[j]*x+v/m))[0]-Q(lam)-(ell*lam)[0]))
 check(f'Case{j+1}: norm matrix with original columns',N==expectedN[j])
 defect=S.expand(sum(R(A[j]**s*x+S.Rational(s,m)*v) for s in range(m))-(v.T*C*x)[0])
 kappa=S.Matrix([[66*b,-2*a-4*b,-a-2*b,-3*a-6*b]]) if j==0 else S.Matrix([[-36*b,a+3*b,a+3*b,2*a+6*b]])
 check(f'Case{j+1}: full uncorrected power defect including constant',zero(defect-(kappa*x)[0]-constants[j]))
 check(f'Case{j+1}: integer norm equation for displayed row',zero(kappa+ell*N))
 free1,free2=S.symbols('free1 free2',integer=True)
 full=S.Matrix([[-22*b-2*free1+4*free2,free1,free2,a+2*b]]) if j==0 else S.Matrix([[9*b-3*free1+3*free2,free1,free2,-(a+3*b)/2]])
 check(f'Case{j+1}: full two-parameter row solution',zero(kappa+full*N))
 check(f'Case{j+1}: norm has exactly the two free row parameters',N.rank()==2)
 check(f'Case{j+1}: all affine linear-correction constants',zero(sum((ell*(A[j]**s*x+S.Rational(s,m)*v))[0] for s in range(m))-(ell*N*x)[0]-S.Rational(m-1,2)*(ell*v)[0]))
 check(f'Case{j+1}: retained finite-power constant is zero',zero(constants[j]+S.Rational(m-1,2)*(ell*v)[0]+m*beta))
 check(f'Case{j+1}: original complete lifted power equals the translation exactly',zero(sum(phase(A[j]**s*x+S.Rational(s,m)*v) for s in range(m))-(v.T*C*x)[0]))
 check(f'Case{j+1}: omitting constant retains nonzero scalar defect',S.simplify((constants[j]+S.Rational(m-1,2)*(ell*v)[0]).subs(b,1))==[-S.Rational(8,3),-S.Rational(27,8)][j])
 check(f'Case{j+1}: omitted scalar is not one',not [-S.Rational(8,3),-S.Rational(27,8)][j].is_integer)
 aa,bb=S.symbols('aa bb',integer=True)
 if j==1:
  check('Case2: parametrized parity lattice gives an integer lift',S.expand(ell[3].subs({a:2*aa+bb,b:bb},simultaneous=True))==-aa-2*bb)
  check('Case2: missing h class forces half-integral coordinate',ell[3].subs({a:1,b:0},simultaneous=True)==-S.Rational(1,2))
  check('Case2: twice h gives the stated entire exponent',zero(phase(x).subs({a:2,b:0},simultaneous=True)+x[3]))
  expected=9*x[0]*(x[0]-1)+6*x[0]*x[2]-x[1]*x[2]-S.Rational(3,4)*x[2]+9*x[0]-2*x[3]+S.Rational(27,32)
  check('Case2: h plus q retains every phase contribution',zero(phase(x).subs({a:1,b:1},simultaneous=True)-expected))
B=S.Matrix([[0,2],[2,12]]);P=S.Matrix([[2,1],[0,1]])
check('Actual downstairs intersection form',P.T*B*P/4==S.Matrix([[0,1],[1,4]]))
check('Actual integral image index',P.det()==2)
source=W/'src/integral-line-bundle-descent-for-the-affine-fillings.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,limitations='Exact symbolic identities in the original coordinates; arbitrary-bundle necessity, classification and quotient smoothness are proved in the written chapter, not certified by the finite checks. No independent review.')
(W/'checks/AFFINE_LINE_DESCENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(passed=len(checks),source_sha256=out['source_sha256'])))
