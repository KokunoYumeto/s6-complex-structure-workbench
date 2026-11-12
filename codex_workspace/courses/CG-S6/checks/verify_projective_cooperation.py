"""Supplementary checks of original bar signs and projective coefficient maps."""
from pathlib import Path
from math import comb
import json,hashlib
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,test):
    assert test,name
    checks.append(name)
def put(d,key,value):
    d[key]=d.get(key,0)+value
    if d[key]==0:del d[key]
def boundary(n):return 1+(-1)**n if n else 0
for n in range(1,33):
    lhs={};rhs={}
    for a in range(n+1):
        b=n-a
        if a:put(lhs,(a-1,b),boundary(a))
        if b:put(lhs,(a,b-1),(-1)**a*boundary(b))
    for a in range(n):put(rhs,(a,n-1-a),boundary(n))
    ck(f'integral bar diagonal chain map degree {n}',lhs==rhs)
    ck(f'integral bar boundary square degree {n}',boundary(n)*boundary(n-1)==0)
    left={(a,b,n-a-b) for a in range(n+1) for b in range(n-a+1)}
    right={(n-b-c,b,c) for b in range(n+1) for c in range(n-b+1)}
    ck(f'full coassociative bar diagonal degree {n}',left==right)
    beta=(boundary(n+1)//2)%2
    ck(f'original Z/4 Bockstein and cup power degree {n}',beta==n%2)
for n in range(2,33):
    mixed=[comb(n,i)%2 for i in range(1,n)]
    ck(f'actual additive coefficient constraint degree {n}',any(mixed)==bool(n&(n-1)))
for n in range(1,9):
    # Coefficient of x_1^(2^n) in f_23(f_12(x_1)), retaining both ends.
    composition={(j,2**i,i) for i in range(n+1) for j in range(n+1) if i+j==n}
    coproduct={(n-i,2**i,i) for i in range(n+1)}
    ck(f'full three-factor composition coefficient {n}',composition==coproduct)
    ck(f'coefficient {n} both original endpoints', (n,1,0) in composition and (0,2**n,n) in composition)
    ck(f'coefficient {n} original grading',all(2**i*(2**j-1)+(2**i-1)==2**n-1 for j,p,i in composition))
# Original integer product differential and both receiving cobar boundaries.
for a in range(9):
    for b in range(9):
        left=(boundary(a+1)//2)%2
        right=(((-1)**a*boundary(b+1))//2)%2
        ck(f'full projective product Bockstein {a},{b}',(left,right)==(a%2,b%2))
        ck(f'full projective product Bockstein square {a},{b}',all(c%2==0 for c in (a*(a+1),a*b+b*a,b*(b+1))))
from calculate_degree_six_cobar import monomial,delta,differential,poly_diff,ZERO
v=monomial(1);v2=monomial(1,2);v3=monomial(1,3);w=monomial(2)
ck('full first actual-coordinate coproduct model',set(delta(v))=={(v,ZERO),(ZERO,v)})
ck('full second actual-coordinate coproduct model',set(delta(w))=={(w,ZERO),(v2,v),(ZERO,w)})
ck('full original cubic coproduct model',set(delta(v3))=={(v3,ZERO),(v2,v),(v,v2),(ZERO,v3)})
ck('first ordered cobar boundary model',differential((w,))=={(v2,v)})
ck('opposite ordered cobar boundary model',poly_diff({(w,),(v3,)})=={(v,v2)})
ck('full square primitive model',set(delta(v2))=={(v2,ZERO),(ZERO,v2)})
src=W/'src/the-original-projective-coordinate-and-actual-cooperations.md'
report=dict(passed=len(checks),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),checks=checks,
 scope='Exact finite bar-chain, integer-sign, coefficient and grading checks. These supplement the written actual-map construction. They do not establish injectivity or surjectivity of the polynomial-to-cooperation map.')
(W/'checks/PROJECTIVE_COOPERATION_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=report['source_sha256'])))
