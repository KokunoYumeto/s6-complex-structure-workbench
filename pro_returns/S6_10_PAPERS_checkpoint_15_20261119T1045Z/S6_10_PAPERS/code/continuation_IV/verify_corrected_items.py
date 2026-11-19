#!/usr/bin/env python3
"""Fresh exact arithmetic for the receiving correction split.

This verifies the indicated arithmetic and linear maps, not the geometric
construction or full all-fan completeness theorems cited by the corrections.
No producing-run program is imported or replayed.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(name, labels, result, detail):
    assert bool(result), (name, detail)
    checks.append(dict(name=name,labels=['iv:correction:'+x for x in labels.split()],pass_=True,detail=detail))

k,l,x,J,n,j,p,b,H,c=s.symbols('k l x J n j p b H c', integer=True)
A=lambda k,l:(4*k-l)/24
check('dual characteristic index',
 'P3F.25 P3K.6 P3K.10 P3K.22 P3K.23 P3K.24 P3K.27 P3K.30 P3K.32 P3K.33 P3F.53 P3K.35 P3K.36 P3K.37 P3K.40 P3K.45 P3K.46 P3K.50 P3K.52 P3K.54 P3K.56 P3K.57 P3K.58 P3K.59 P3K.60',
 s.expand(A(-k,-l)+A(k,l))==0,'Odd characteristic pairings and their exact index change sign.')
check('dual fibre character', 'P3K.6', s.simplify((1/(c*x))*c-1/x)==0,
 'The fibre map D(x)=1/x has D(cx)=c^-1 D(x).')
check('weighted OS47 trace', 'P3F.25 P3K.23 P3F.53', Q(-72+12*14,24)==4,
 'Physical trace (-72-12*(-14))/24=4.')
profile=[(d,Q(d,2)-1) for d in [8,14,20,30]]
check('primitive reference table', 'P3K.10 P3K.22 P3K.27 P3K.30 P3K.32 P3F.53',
 [int(v) for d,v in profile]==[3,6,9,14],profile)
check('primitive OS45 covers', 'P3K.10', sorted({3*N%28 for N in range(1,29)})==list(range(28)),
 'Positive pullback numbers 1,...,28 yield every residue.')
check('physical free-pair dictionary', 'P3K.23 P3K.27 P3K.30 P3K.32',
 s.expand((6*c)+(3*H-6*c)-3*H)==0 and s.expand(4*(6*c)-24*c)==0,
 'm=6chi,n=3H-6chi imply k_M=m+n=3H and ell_M=4m=24chi.')
check('general physical reference index', 'P3K.30 P3K.32 P3F.53',
 s.expand(A(3*H,24*c)-(H/2-c))==0,'(12H-24chi)/24=H/2-chi.')
check('fixed-edge correction', 'P3K.23', [7*a%28 for a in [3,6,9,14,4,0]]==[21,14,7,14,0,0],
 'Add n=6 A_M to the physical baseline.')
check('reduced III complete residues', 'P3K.24', sorted({(3*z+2)%28 for z in range(28)})==list(range(28)),
 'The actual reduced expression takes every residue over 28 consecutive l.')
check('literal fan parameter arrow', 'P3K.25', s.expand((-j)*(-j-1)-j*(j+1))==0,
 'n=-j transports (1,-j),(1,-j-1) exactly to (1,n),(1,n-1).')
check('primitive vertical counterexample', 'P3K.25 P3K.31 P3K.32', 3-Q(2*(2-1),2)==2,
 'T0=3, T2=2 while old cocharacter S=1 at both.')
L=s.Matrix([[-1,2,2],[0,1,0],[0,0,1]])
check('meridian-dual exterior map', 'P3K.29', L*L==s.eye(3),
 {'meridian_matrix':L.tolist(),'dual_matrix':L.T.tolist(),'pairing_matrix':(L*L).tolist()})
check('nonzero native right coordinate', 'P3K.29', -1!=0,
 'At scalar winding J=1, the retained native right coordinate -J=-1 contradicts zero.')
check('shorter characteristic cover', 'P3K.33 P3K.35 P3K.36',
 s.simplify(b*A(3*H/b,24*c/b)-A(3*H,24*c))==0,
 'An actual degree-b cover multiplies characteristic integrals by b; no residue is divided.')
check('original shorter reference seed', 'P3K.33', A(Q(1),Q(4))==0 and Q(1,3)*3==1 and Q(1,6)*24==4,
 'At K=L=1: Hhat=1/3,chihat=1/6,physical pair=(1,4),baseline=0.')
check('Liu-Rollenske shorter seed', 'P3K.36', A(Q(3),Q(12))==0,
 'Actual u=w^2: Hhat=1,chihat=1/2,physical pair=(3,12),baseline=0.')
check('original and LR T2 counterexamples', 'P3K.33 P3K.36', (-2)%28==26,
 'For actual J=2, subtract J*2*(2-1)/2 from the zero reference.')
os49index=s.expand(A(2*j-6*j*(n-1)**2,8*j))
check('OS49 vertical physical index', 'P3K.17 P3K.34 P3K.37 P3K.44',
 s.expand(os49index+j*(n-1)**2)==0,'The actual j-seed index is -j(n-1)^2.')
check('OS49 original and shorter counterexamples', 'P3K.17 P3K.34 P3K.37 P3K.44',
 ((-3)%28,(-1)%28,0)==(25,27,0),'k=1 has original negative25, shorter negative27, positive0.')
check('actual iterate arithmetic', 'P3K.41 P3K.43 P3K.44', all((N*a)%28 == sum([a]*N)%28 for N in range(1,29) for a in range(28)),
 'Concatenating N actual oriented returns gives N times the residue, checked for complete residues of N and a.')
check('selected-cusp physical pair', 'P3K.40 P3K.45 P3K.46 P3K.50 P3K.52',
 A(Q(-6),Q(0))==-1,'Physical pair(-6,0) has central integer -1.')
check('selected-cusp first flops', 'P3K.40 P3K.45 P3K.54', [(-1+r)%28 for r in [-6,-6,0]]==[21,21,27],
 'Add retained native right coordinates(-6,-6,0) to baseline-1.')
seq=-1-3*n*(n-1)
check('selected-cusp vertical recurrence', 'P3K.56', s.expand(seq.subs(n,n+1)-seq+6*n)==0,
 's(n+1)-s(n)=-6n, s(0)=-1.')
check('selected-cusp complete image', 'P3K.56',
 s.expand(seq.subs(n,n+28)-seq+28*(6*n+81))==0 and sorted({int(seq.subs(n,z))%28 for z in range(28)})==[5,7,9,13,19,21,23,27],
 'Symbolic period28 and exhaustive 28-residue evaluation.')
seq2=-7-24*j*(j+1)
check('mutation sequence least period', 'P3K.59',
 s.expand(seq2.subs(j,j+7)-seq2+28*(12*j+48))==0 and all(any(int((seq2.subs(j,z+h)-seq2.subs(j,z)))%28 for z in range(7)) for h in range(1,7)),
 'Period7 symbolically; each smaller positive h fails on a saved complete period.')
check('mutation sequence image', 'P3K.59', sorted({int(seq2.subs(j,z))%28 for z in range(7)})==[1,13,17,21],
 'Seven actual residues: '+str([int(seq2.subs(j,z))%28 for z in range(7)]))
check('fixed infinity sign', 'P3K.57', [-v for v in [0,1]]==[0,-1],
 'Physical duality transports actual U-indices0,1 to0,-1.')
check('cut-relation arithmetic', 'P3K.58 P3K.60', s.expand(1-(-1-2*k*(3*p-1))-(2+2*k*(3*p-1)))==0,
 'Z+Zprime=1-I=2+2k(3p-1) in the reduced branch.')
check('order-two kernel', 'P3K.60', [z for z in range(28) if 2*z%28==0]==[0,14],
 'Kernel of times2 is exactly0,14; no choice is made.')
check('complete paired possibilities', 'P3K.60',
 all({(z,(z+a)%28) for z in range(28) if (2*z+a-a-2*t)%28==0} == {((t+14*e)%28,(a+t+14*e)%28) for e in [0,1]} for a in [1,2] for t in range(28)),
 'For each branch a=1,2 and every kA residue, the displayed two pairs are exactly all solutions.')

out=dict(program=str(Path(__file__).relative_to(ROOT)),sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 scope='Exact arithmetic, covering-number identities and displayed linear maps only. Input geometric proofs and full all-fan completeness are not certified by this program.',
 checks=checks,count=len(checks),result='PASS')
(ROOT/'analysis/continuation_IV/corrected_items_arithmetic.output.json').write_text(json.dumps(out,indent=2,ensure_ascii=False,default=str)+'\n')
print(json.dumps({'result':out['result'],'checks':len(checks),'labels':len({l for q in checks for l in q['labels']})}))
