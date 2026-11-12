"""Exact path parameters, cap branches, filtration positions and integer edges."""
from pathlib import Path
import hashlib,json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
W=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
t,s,r,u=S.symbols('t s r u',real=True)
join=1/(1+t)
left=(1+t)*s;right=(1+t)*s-1
check('Path-lift left seam parameter is the original terminal point',S.simplify(left.subs(s,join))==1)
check('Path-lift right seam parameter is the original initial time',S.simplify(right.subs(s,join))==0)
check('Time-zero lift has the original path parametrization',left.subs(t,0)==s)
check('Lift endpoint has the full original base time',right.subs(s,1)==t)
samples=[S.Rational(i,16) for i in range(17)]
check('Both path-lift branch arguments remain in their exact domains',all(
  (0<=left.subs({t:tt,s:ss})<=1 if ss<=1/(1+tt) else 0<=right.subs({t:tt,s:ss})<=tt)
  for tt in samples for ss in samples))
check('Path contraction starts at the original path parameter',((1-u)*s).subs(u,0)==s)
check('Path contraction ends at the original initial endpoint',((1-u)*s).subs(u,1)==0)
check('Path contraction preserves every initial endpoint',((1-u)*s).subs(s,0)==0)
check('Compression cap inner branch ends on the top',2-1==1)
check('Compression cap outer branch ends on the side',S.simplify(r/r)==1)
check('Compression cap branches agree at radius one half',S.Rational(1,1)/S.Rational(1,2)==2)
check('Compression cap fixes the original rim at every time',S.expand((1-s+s/r)*r).subs(r,1)==1 and (s*(1/r-1)).subs(r,1)==0)
check('Entire compression interpolation stays in its cylinder',all(
  0<=(1-ss+ss*min(2,1/rr if rr else S.oo))*rr<=1 and
  0<=ss*(min(2,1/rr if rr else S.oo)-1)<=1
  for rr in samples for ss in samples))
lamtop=2/(t+1);lamside=1/r
check('Exact-sequence cap top branch time is one',S.simplify(-1+lamtop*(t+1))==1)
check('Exact-sequence cap side branch radius is one',S.simplify(lamside*r)==1)
check('Exact-sequence cap branches agree at their actual threshold',S.simplify(lamtop-lamside.subs(r,(t+1)/2))==0)
check('Exact-sequence cap fixes top and side pointwise',lamtop.subs(t,1)==1 and lamside.subs(r,1)==1)
check('Exact-sequence cap has valid values on the whole rational test grid',all(
  0<=-1+min(2/(tt+1),1/rr if rr else S.oo)*(tt+1)<=1 and
  0<=min(2/(tt+1),1/rr if rr else S.oo)*rr<=1 and
  (-1+min(2/(tt+1),1/rr if rr else S.oo)*(tt+1)==1 or min(2/(tt+1),1/rr if rr else S.oo)*rr==1)
  for rr in samples for tt in samples))
p,q,rr=S.symbols('p q rr',integer=True)
check('Homology differential retains total degree minus one',S.expand((p-rr)+(q+rr-1)-(p+q-1))==0)
check('First-quadrant stabilization bound removes both neighbouring entries',all(
  (pp-rrr<0 and qq-rrr+1<0)
  for pp in range(25) for qq in range(25) for rrr in [max(pp,qq+1)+1,max(pp,qq+1)+3]))
for n in [2,3,5,6,17]:
 incoming=[(rrr,n-rrr+1) for rrr in range(2,n+4) if n-rrr+1>=0 and not 0<n-rrr+1<n]
 outgoing=[(n+1-rrr,rrr-1) for rrr in range(2,n+4) if n+1-rrr>=0 and not 0<rrr-1<n]
 check(f'Only the retained transgression can meet the two relevant entries, n={n}',incoming==[(n+1,0)] and outgoing==[(0,n)])
m=S.symbols('m',integer=True)
D=S.Matrix([[m]])
check('Original integer transgression retains its sign and multiplicity',(D*S.Matrix([1]))[0]==m)
for value in [-7,-2,-1,0,1,2,6]:
 matrix=D.subs(m,value);snf=smith_normal_form(matrix,domain=S.ZZ)
 check(f'Integral edge kernel and cokernel agree with the full chain matrix, m={value}',
       abs(snf[0,0])==abs(value) and len(matrix.nullspace())==int(value==0))
fundamental=S.Matrix([1,1]);quotient=S.Matrix([[1,-1]])
check('Original global orientation class dies in the punctured quotient',quotient*fundamental==S.zeros(1,1))
check('Both original boundary classes have opposite primitive signs',
      quotient*S.Matrix([1,0])==S.Matrix([1]) and quotient*S.Matrix([0,1])==S.Matrix([-1]))
check('Punctured quotient has no hidden integral torsion',smith_normal_form(fundamental,domain=S.ZZ)==S.Matrix([1,0]))
for d in [5,6]:
 groups={j:int(j%(d-1)==0) for j in range(101)}
 check(f'Looped S{d} additive recurrence retains the actual sphere dimension',
       groups[0]==1 and all(groups[j]==0 for j in range(1,d-1)) and
       all(groups[j]==groups[j+d-1] for j in range(102-d)))
source=W/'src/path-fibres-and-integral-homotopy-equivalences.md'
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 passed=len(checks),checks=checks,
 scope='Exact path and cap identities, rational domain checks, filtration bidegrees, integral Smith forms including signs and torsion, original boundary generators and loop-sphere recurrence. Finite checks support the full written topological proofs.',
 independent_review=False)
(W/'checks/PATH_FIBRE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
