"""Postrelease verification of the explicit Pluecker chart derived before release.

The coefficient ring is Z[p12,p13,p14,p23,p24,p34,z1,z2].
Only sparse integer-polynomial addition and multiplication are used.
"""
from pathlib import Path
import json,datetime
names=['p12','p13','p14','p23','p24','p34','z1','z2']
zero=(0,)*len(names)
def var(i):
 e=list(zero);e[i]=1;return {tuple(e):1}
def add(*polys):
 out={}
 for p in polys:
  for e,c in p.items():out[e]=out.get(e,0)+c
 return {e:c for e,c in out.items()if c}
def neg(p):return {e:-c for e,c in p.items()}
def mul(p,q):
 out={}
 for a,c in p.items():
  for b,d in q.items():
   e=tuple(x+y for x,y in zip(a,b));out[e]=out.get(e,0)+c*d
 return {e:c for e,c in out.items()if c}
def show(p):
 return [{'coefficient':c,'powers':dict((n,v)for n,v in zip(names,e)if v)}for e,c in sorted(p.items())]
p12,p13,p14,p23,p24,p34,z1,z2=[var(i)for i in range(8)]
R=add(mul(p12,p34),neg(mul(p13,p24)),mul(p14,p23))
A=[p12,{},neg(p23),neg(p24)]
B=[{},p12,p13,p14]
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
coeffs=[p12,p13,p14,p23,p24,p34]
differences=[]
for (i,j),c in zip(pairs,coeffs):
 diff=add(mul(A[i],B[j]),neg(mul(A[j],B[i])),neg(mul(p12,c)))
 expected=neg(R)if (i,j)==(2,3)else {}
 assert diff==expected;differences.append(show(diff))
# P=p12*(z1*w1+z2*w2); coefficients of P wedge v.
P=[mul(p12,z1),mul(p12,z2),add(neg(mul(z1,p23)),mul(z2,p13)),add(neg(mul(z1,p24)),mul(z2,p14))]
triple_coeffs=[
 add(mul(P[0],p23),neg(mul(P[1],p13)),mul(P[2],p12)),
 add(mul(P[0],p24),neg(mul(P[1],p14)),mul(P[3],p12)),
 add(mul(P[0],p34),neg(mul(P[2],p14)),mul(P[3],p13)),
 add(mul(P[1],p34),neg(mul(P[2],p24)),mul(P[3],p23))]
assert triple_coeffs==[{}, {},mul(z1,R),mul(z2,R)]
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'timing':'Postrelease exact verification of formulas already present in the prerelease frozen GD derivation; no additional independent-check event.',
 'ring':'Z[p12,p13,p14,p23,p24,p34,z1,z2]',
 'plucker_relation':show(R),'scaled_wedge_differences':differences,
 'scaled_kernel_wedge_coefficients':list(map(show,triple_coeffs)),
 'interpretation':'On p12 nonzero and R=0, A/p12 and B/p12 give v=p12*w1 wedge w2. The first two kernel equations solve the remaining two coordinates uniquely; the last two vanish by R. The exact kernel therefore has dimension two and the displayed holomorphic basis.',
 'all_assertions_passed':True,'events_added':0}
f=Path(__file__).with_name('S6_SERIES_PUBLISH_II_01GD_plucker_exact_output.json')
assert not f.exists();f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
