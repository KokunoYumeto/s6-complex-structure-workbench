"""Supplementary exact checks for the original bar and actual degree-eight comparison."""
from pathlib import Path
from itertools import product,combinations_with_replacement
from math import comb
from functools import lru_cache
import json,hashlib
from calculate_degree_six_cobar import monomials,delta,ZERO,monomial,differential
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,value):
 assert value,name
 checks.append(name)
def tog(s,x):
 if x in s:s.remove(x)
 else:s.add(x)
def xor(*sets):
 out=set()
 for s in sets:
  for x in s:tog(out,x)
 return out
for length in range(1,7):
 internal=[];faces=[]
 for ns in product(range(4),repeat=length):
  eps=sum((length-i-1)*n for i,n in enumerate(ns))
  for j,n in enumerate(ns):
   if n:internal.append((eps-(length-j-1)+1+sum(x+1 for x in ns[:j])-(eps+length+sum(ns[:j])))%2==0)
  for j in range(length-1):
   merged=ns[:j]+(ns[j]+ns[j+1],)+ns[j+2:]
   ep2=sum((length-i-2)*n for i,n in enumerate(merged))
   faces.append(eps-ep2==sum(ns[:j+1]) and ep2+sum(x+1 for x in ns[:j+1])==eps+j+1)
 ck(f'full original internal prism signs length {length}',all(internal))
 ck(f'full original multiplication prism signs length {length}',all(faces))

# An independent finite bar complex for E(x,y), retaining the mixed letter xy.
# Original internal degrees are |x|=1 and |y|=3.
deg={1:1,2:3,3:4}
def bdiff(word):
 out=set()
 for j in range(len(word)-1):
  if not word[j]&word[j+1]:tog(out,word[:j]+(word[j]|word[j+1],)+word[j+2:])
 return out
@lru_cache(None)
def shuffle(a,b):
 if not a:return frozenset([b])
 if not b:return frozenset([a])
 return frozenset(xor({(a[0],)+w for w in shuffle(a[1:],b)},{(b[0],)+w for w in shuffle(a,b[1:])}))
def dp(poly):return xor(*(bdiff(w) for w in poly))
def times(p,q):return xor(*(shuffle(a,b) for a in p for b in q))
@lru_cache(None)
def words(n):
 if n==0:return ((),)
 if n<0:return ()
 return tuple((a,)+w for a in [1,2,3] for w in words(n-deg[a]-1))
def rank(cols):
 basis={}
 for v in cols:
  while v:
   i=v.bit_length()-1
   if i not in basis:basis[i]=v;break
   v^=basis[i]
 return len(basis)
def vec(poly,index):return sum(1<<index[w] for w in poly)
for n in range(13):
 domain=words(n);lower={w:i for i,w in enumerate(words(n-1))};index={w:i for i,w in enumerate(domain)}
 out=[vec(bdiff(w),lower) for w in domain];incoming=[vec(bdiff(w),index) for w in words(n+1)]
 reps=[set(shuffle((1,)*a,(2,)*b)) for a in range(n//2+1) for b in range(n//4+1) if 2*a+4*b==n]
 ck(f'complete finite bar differential square total degree {n}',all(not dp(bdiff(w)) for w in words(n+1)))
 ck(f'exterior bar homology dimension total degree {n}',len(domain)-rank(out)-rank(incoming)==len(reps))
 ck(f'all retained divided-power representatives cycles degree {n}',all(not dp(v) for v in reps))
 ck(f'divided-power representatives independent modulo full boundaries degree {n}',rank(incoming+[vec(v,index) for v in reps])==rank(incoming)+len(reps))
sample=[w for n in range(8) for w in words(n)]
for n in range(1,8):ck(f'all positive shuffle squares total degree {n}',all(not shuffle(w,w) for w in words(n)))
for a in sample:
 for b in sample:
  ck(f'full bar shuffle Leibniz identity {a} {b}',dp(shuffle(a,b))==xor(times(bdiff(a),{b}),times({a},bdiff(b))))
for a,b,c,d in product(range(4),repeat=4):
 if 2*(a+c)+4*(b+d)>12:continue
 lhs=times(shuffle((1,)*a,(2,)*b),shuffle((1,)*c,(2,)*d))
 rhs=set(shuffle((1,)*(a+c),(2,)*(b+d))) if comb(a+c,a)*comb(b+d,b)%2 else set()
 ck(f'full two-generator divided-power product {a},{b};{c},{d}',lhs==rhs)

# Complete original tuple indexing, all lower-stage exterior products retained.
dimension_rows=[];previous=None
for q in range(1,13):
 bound=q+8;tuples=[j for j in combinations_with_replacement(range(bound.bit_length()),q) if sum(2**v for v in j)<=bound]
 if previous is not None:
  formed=[]
  for j in previous:
   olddegree=sum(2**v for v in j)
   for a in range(bound.bit_length()):
    if 2**a*(olddegree+1)<=bound:formed.append((a,)+tuple(a+v for v in j))
  ck(f'complete bar-to-tuple bijection stage {q}',sorted(formed)==tuples and len(formed)==len(set(formed)))
  ck(f'original suspension inserts zero stage {q}',all((0,)+j in tuples for j in previous))
 dimensions=[0]*(bound+1);dimensions[0]=1
 for j in tuples:
  d=sum(2**v for v in j)
  for n in range(bound,d-1,-1):dimensions[n]+=dimensions[n-d]
 if q>=8:ck(f'full stable cooperation dimensions stage {q}',dimensions[q:q+9]==[1,1,1,2,2,2,3,4,4])
 ck(f'no decomposable in detecting degree stage {q}',2*q>bound or dimensions[2*q]==sum(sum(2**v for v in j)==2*q for j in tuples))
 dimension_rows.append(dict(stage=q,generator_tuples=tuples,homology_dimensions=dimensions));previous=tuples

primitive_rows=[]
for n in range(1,9):
 basis=monomials(n);tensor=sorted({(a,b) for m in basis for a,b in delta(m) if a!=ZERO and b!=ZERO})
 cols=[sum(1<<i for i,t in enumerate(tensor) if t in delta(m)) for m in basis]
 kernels=[]
 for mask in range(1<<len(basis)):
  v=0
  for i,c in enumerate(cols):
   if mask>>i&1:v^=c
  if v==0:kernels.append(mask)
 expected=[0,1<<basis.index(monomial(1,n))] if n in [1,2,4,8] else [0]
 ck(f'full primitive kernel in original degree {n}',kernels==expected)
 primitive_rows.append(dict(degree=n,basis=basis,ordered_tensor_rows=tensor,full_reduced_columns=cols,kernel_masks=kernels))
x=monomial(1);y=monomial(2);z=monomial(3);xz=tuple(a+b for a,b in zip(x,z))
terms={(monomial(1,1)[:1]+(2,0,0),x),(monomial(1,5),y),(x,z),(z,x),(monomial(2,2),monomial(1,2)),(monomial(1,4),(1,1,0,0))}
ck('all six original actual boundary terms in Exercise 9.2',differential((xz,))==terms)
ck('Exercise 9.1 all exterior classes through degree six',dimension_rows[1]['homology_dimensions'][:7]==[1,0,1,1,1,2,2])
for n in range(1,33):ck(f'original stable product desuspension sign exponent {n}',sum(2*(j-1) for j in range(1,n+1))==n*(n-1) and n*(n-1)%2==0)
src=W/'src/the-actual-mod-two-cooperation-comparison-through-degree-eight.md'
report=dict(passed=len(checks),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),checks=checks,tuple_and_homology_rows=dimension_rows,primitive_rows=primitive_rows,scope='Finite supplementary checks of original prism signs, complete small exterior bar complexes and their actual representatives, shuffle identities, full tuple indexing and stage dimensions, all reduced coproducts through degree eight and both worked exercises. The topological comparison, all-stage suspension and stable nonvanishing are proved in the written text; these finite checks do not certify those geometric proofs.')
(W/'checks/ACTUAL_DEGREE_EIGHT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=report['source_sha256'])))
