#!/usr/bin/env python3
"""Independent exact checks for the audited OF maps and target-prism solve."""
from pathlib import Path
from math import gcd
from fractions import Fraction as F
import hashlib,json
import sympy as S
R=Path(__file__).resolve().parents[2]
source=R/'notes/part3_e6_order_three_all_fans_working.md'
expected='47b698d80e2ec7803f4d9f3f03f8dfe9e851db5fa8fa66a00010fb8ef2e2d965'
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected
checks=0
def check(v):
 global checks
 assert v
 checks+=1
def eq(a,b=0):check(S.simplify(a-b)==0)

# The two native quaternion coefficients in q=a+j b multiply by
# (a,b)(c,d)=(ac-conj(b)d,bc+conj(a)d).
zr,zi,ar,ai,br,bi=S.symbols('zr zi ar ai br bi', real=True)
z=zr+S.I*zi;a=ar+S.I*ai;b=br+S.I*bi
def mul(q,r):return (q[0]*r[0]-S.conjugate(q[1])*r[1],q[1]*r[0]+S.conjugate(q[0])*r[1])
q1=mul((1,z),(a,S.conjugate(b)))
q2=mul((1/z,1),(z*a,S.conjugate(z*b)))
for x,y in zip(q1,q2):eq(x,y)

# Exact source-to-reference vertex products and the three signed normal rows.
A,B,C,D,z,a,b,c=S.symbols('A B C D z a b c', nonzero=True)
rows=[(A*C*b*c,a*b/C,1/(A*b)),(B*D*b*c,1/(D*c),a*c/B),(1/a,a*b,a*c)]
for row in rows:eq(S.prod(row),a*b*c)
native=[(A*rows[0][2],C*rows[0][1],rows[0][0]/(A*C)),
        (D*rows[1][1],B*rows[1][2],rows[1][0]/(B*D)),rows[2]]
for row,expected_row in zip(native,[(1/b,a*b,b*c),(1/c,a*c,b*c),(1/a,a*b,a*c)]):
 for x,y in zip(row,expected_row):eq(x,y)

# Physical generator and derivative dictionary, with the retained dual sign.
m,n,k,l=S.symbols('m n k l')
eq((4*(m+n)-4*m)/24,n/6)
check(S.solve([m+n+27,4*m+12],[m,n])=={m:-3,n:-24})
check(-(-3-24)==27)
check(27+2*(-24)==-21)

# Fresh symmetric nine-unknown target solve, followed by symbolic induction.
w0,w1,w2,aa,bb=S.symbols('w0 w1 w2 aa bb', nonzero=True)
v00,v01,v02,v11,v12,v22,d0,d1,d2=S.symbols('v00 v01 v02 v11 v12 v22 d0 d1 d2')
V=S.Matrix([[v00,v01,v02],[v01,v11,v12],[v02,v12,v22]])
equations=list(V*S.Matrix([-w0,w1,0]))+list(V*S.Matrix([-w0,0,w2]))
equations += [w1*d1-w0*d0,w2*d2-w0*d0,v22-aa,d2-(2*aa-bb)]
sol=S.solve(equations,[v00,v01,v02,v11,v12,v22,d0,d1,d2],dict=True)
check(len(sol)==1)
for i in range(3):
 for j in range(3):eq(V[i,j].subs(sol[0]),w2*w2*aa/[w0,w1,w2][i]/[w0,w1,w2][j])
for i,x in enumerate([d0,d1,d2]):eq(sol[0][x],w2*(2*aa-bb)/[w0,w1,w2][i])

p,r=S.symbols('p r', positive=True)
norm=lambda p,r:p*p+p*r+r*r
poly=lambda v:-4+S.Rational(3,2)*(v-1)-S.Rational(27,8)*(v*v-1)
q=norm(p,r);prod=p*r*(p+r);cc=27*prod**2;ee=prod*(6-27*q)
for wi,pp,rr in [(r,p,r+p),(p,p+r,r)]:
 olda=cc/wi**2;oldb=ee/wi;inc=(oldb-olda)/2
 eq(inc,poly(norm(pp,rr))-poly(q))
 nw2=-pp-rr
 eq(nw2**2*olda,27*(pp*rr*(pp+rr))**2)
 eq(nw2*(2*olda-oldb),pp*rr*(pp+rr)*(6-27*norm(pp,rr)))

# Full modulo bound and actual primitive witnesses, without using root output.
def value(s):return F(-4)+F(3,2)*(s-1)-F(27,8)*(s*s-1)
residues=set()
for x in range(112):
 for y in range(112):
  if gcd(gcd(x,y),112)!=1:continue
  s=x*x+x*y+y*y;v=value(s)
  check(v.denominator==1)
  residues.add(int(v)%28)
witnesses={}
for x in range(-40,41):
 for y in range(-40,41):
  if gcd(x,y)!=1:continue
  s=x*x+x*y+y*y;v=value(s)
  witnesses.setdefault(int(v)%28,[x,y,int(v)])
check(residues==set(witnesses))
check(residues=={0,3,4,5,7,10,11,12,14,17,18,19,21,24,25,26})
t=S.symbols('t');eq(poly(t+112)-poly(t),-756*t-42168)
record={'status':'PASS','source_sha256':expected,'checks':checks,'complete_image':sorted(residues),'independent_witnesses':witnesses,'geometry_record':'records/checks_audit_e6_order_three_all_fans.json','scope':'Exact native chart, physical pair, independent target solve, symbolic directed induction and full modular bound; geometric audit recorded separately.'}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':checks,'image':sorted(residues)}))
