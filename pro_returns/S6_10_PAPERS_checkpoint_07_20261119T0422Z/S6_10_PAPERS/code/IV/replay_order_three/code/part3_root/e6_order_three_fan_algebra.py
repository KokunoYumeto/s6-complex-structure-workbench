"""Exact zero-winding order-three fan algebra.

This certificate checks the executed arithmetic for the explicitly stated
native products and geometric arrows in the accompanying working proof.
The geometry of those products is a separate proof obligation until audited.
"""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
checks = 0
def check(b):
    global checks
    assert b
    checks += 1

I = ((1, 0), (0, 1))
R = ((-1, -1), (1, 0))
Q = (((1, -1), (0, 1)), ((1, 0), (-1, 1)))
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def mul(A, B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def inv(A):
    d = det(A)
    assert d in (-1, 1)
    return ((A[1][1]//d, -A[0][1]//d), (-A[1][0]//d, A[0][0]//d))
def neg(A): return tuple(tuple(-v for v in r) for r in A)
def weights(A):
    B = inv(A)
    x, y = B[0][1], B[1][1]
    return (x, y, -x-y)
def norm(A):
    x, y, _ = weights(A)
    return x*x+x*y+y*y
def canonical(A):
    if det(A) == -1:
        A = ((A[0][1], A[0][0]), (A[1][1], A[1][0]))
    choices=[]
    for _ in range(3):
        for B in (A, neg(A)):
            if (B[0] == (1, 0) and B[1][1] == 1) or (B[0][0] > 0 and B[0][1] < 0):
                choices.append(B)
        A=mul(A,R)
    check(len(choices)==1)
    return choices[0]
def factor(C):
    A=C; reverse=[]
    while A[0][1] != 0:
        p,r=A[0][0],-A[0][1]
        old=p+r
        i=0 if r>=p else 1
        A=mul(A,inv(Q[i]));reverse.append(i)
        check(A[0][0]-A[0][1] < old)
    check(A[0]==(1,0) and A[1][1]==1)
    W=tuple(reversed(reverse));B=A
    for i in W:B=mul(B,Q[i])
    check(B==C)
    return A,W
def formula(S):
    return -4+F(3,2)*(S-1)-F(27,8)*(S*S-1)
def evaluate(A):
    C=canonical(A)
    check(norm(C)==norm(A))
    P,word=factor(C)
    V=[[F(27),F(0),F(0)],[F(0),F(0),F(0)],[F(0),F(0),F(0)]]
    delta=[F(-21),F(0),F(0)]
    value=F(-4); increments=[]
    for i in word:
        a,b=V[i][i],delta[i]
        n=(b-a)/2
        check(n.denominator==1)
        P=mul(P,Q[i]);w=weights(P)
        check(all(w))
        c=w[2]*w[2]*a;e=w[2]*(2*a-b)
        W=[[c/F(w[j]*w[k]) for k in range(3)] for j in range(3)]
        d=[e/F(w[j]) for j in range(3)]
        check(W[2][2]==a and d[2]==2*a-b)
        check(all(v.denominator==1 for row in W for v in row) and all(v.denominator==1 for v in d))
        for j in (1,2):
            check(all(w[j]*W[k][j]-w[0]*W[k][0]==0 for k in range(3)))
            check(w[j]*d[j]-w[0]*d[0]==0)
        value+=n;increments.append(int(n));V,delta=W,d
        S=norm(P);p,r=P[0][0],-P[0][1];prod=p*r*(p+r)
        check(c==27*prod**2)
        check(e==prod*(6-27*S))
        check(value==formula(S))
    check(P==C and value==formula(norm(A)))
    check(value.denominator==1)
    return {"canonical":C,"word":word,"increments":increments,"integer":int(value),"residue":int(value)%28,
            "V":[[int(v) for v in row] for row in V],"delta":[int(v) for v in delta],"S":norm(A)}

matrices=0;fans={}
for a in range(-12,13):
 for b in range(-12,13):
  for c in range(-12,13):
   for d in range(-12,13):
    A=((a,b),(c,d))
    if abs(det(A))!=1:continue
    out=evaluate(A);matrices+=1;fans[str(out['canonical'])]=out

# Algebraic closure under the exact identical-fan coordinate arrows.
for x in range(-40,41):
 for y in range(-40,41):
    if gcd(x,y)!=1:continue
    S=x*x+x*y+y*y
    check(S%2==1 and formula(S).denominator==1)
    check(S==y*y+y*(-x-y)+(-x-y)**2)
    check(S==(-x)**2+(-x)*(-y)+(-y)**2)
    check(formula(S+112)-formula(S) == -756*S-42168)
    check(int(formula(S+112)-formula(S))%28==0)

def egcd(a,b):
    oldr,r=a,b; olds,s=1,0; oldt,t=0,1
    while r:
        q=oldr//r
        oldr,r=r,oldr-q*r;olds,s=s,olds-q*s;oldt,t=t,oldt-q*t
    if oldr<0:return -oldr,-olds,-oldt
    return oldr,olds,oldt

# Mod112 gives an upper bound for every primitive (x,y). Each entry
# is then realized by an explicit integral unimodular matrix.
upper=set()
for x in range(112):
 for y in range(112):
    if gcd(gcd(x,y),112)!=1:continue
    upper.add(int(formula(x*x+x*y+y*y))%28)
witnesses={}
for radius in range(1,57):
 for x in range(-radius,radius+1):
  for y in range(-radius,radius+1):
    if max(abs(x),abs(y))!=radius or gcd(x,y)!=1:continue
    _,u,v=egcd(x,y);A=((y,-x),(u,v))
    check(det(A)==1 and weights(A)[:2]==(x,y))
    out=evaluate(A)
    witnesses.setdefault(out['residue'],{"P":A,"physical_coordinates":[x,y],"S":out['S'],"integer":out['integer']})
 if set(witnesses)==upper:break
check(set(witnesses)==upper)

result={"status":"PASS_EXACT_FAN_ALGEBRA_GEOMETRY_SEPARATE",
        "checks":checks,"matrices_checked":matrices,"distinct_fans":len(fans),
        "entry_bound":12,"seed":{"V":[[27,0,0],[0,0,0],[0,0,0]],"delta":[-21,0,0],"index":-4},
        "formula":"-4+3(S-1)/2-27(S^2-1)/8; S=x^2+xy+y^2, (x,y)=P^-1 e2",
        "image_mod28":sorted(upper),"witnesses":{str(k):v for k,v in sorted(witnesses.items())},
        "representative_examples":[evaluate(I),evaluate(Q[0]),evaluate(((2,-1),(-1,1)))],
        "scope":"Exact arithmetic of the specified seed, directed flop update, integral prism reconstruction and identical-fan arrows. The full geometric product proof is retained separately."}
(HERE/'e6_order_three_fan_algebra.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('witnesses','representative_examples')}))
