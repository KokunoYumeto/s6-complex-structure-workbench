"""Independent signed word checks for the retained odd-prime bar calculation."""
from pathlib import Path
from itertools import product
from functools import lru_cache
from math import comb,factorial
import json,hashlib
W=Path(__file__).resolve().parents[1]
checks=[];ranks=[]
def ck(name,value):
 assert value,name
 checks.append(name)
def add(out,word,c,p=None):
 out[word]=out.get(word,0)+c
 if p:out[word]%=p
 if not out[word]:del out[word]
@lru_cache(None)
def sh(a,b):
 if not a:return {b:1}
 if not b:return {a:1}
 out={}
 for w,c in sh(a[1:],b).items():add(out,(a[0],)+w,c)
 for w,c in sh(a,b[1:]).items():add(out,(b[0],)+w,(-1)**len(a)*c)
 return out
def bd(w,p):
 out={}
 for j in range(len(w)-1):
  if w[j]+w[j+1]<p:add(out,w[:j]+(w[j]+w[j+1],)+w[j+2:],(-1)**(j+1),p)
 return out
def dpoly(poly,p):
 out={}
 for w,c in poly.items():
  for v,z in bd(w,p).items():add(out,v,c*z,p)
 return out
def rank(cols,p):
 basis={}
 for col in cols:
  v=dict(col)
  while v:
   i=max(v)
   if i not in basis:
    u=pow(v[i],-1,p);basis[i]={j:c*u%p for j,c in v.items()};break
   c=v[i]
   for j,z in basis[i].items():add(v,j,-c*z,p)
 return len(basis)
for p,limit in [(3,6),(5,4),(7,3)]:
 for n in range(limit+1):
  words=list(product(range(1,p),repeat=n));below={w:i for i,w in enumerate(product(range(1,p),repeat=max(0,n-1)))};index={w:i for i,w in enumerate(words)}
  incoming=[bd(w,p) for w in product(range(1,p),repeat=n+1)]
  out=[{below[z]:c for z,c in bd(w,p).items()} for w in words]
  inc=[{index[z]:c for z,c in poly.items()} for poly in incoming]
  u=(p-1,1)*(n//2);rep=((1,)+u) if n%2 else u
  ro=rank(out,p);ri=rank(inc,p)
  ck(f'full signed differential squared p={p} length={n+1}',all(not dpoly(v,p) for v in incoming))
  ck(f'full bar homology dimension p={p} length={n}',len(words)-ro-ri==1)
  ck(f'original representative independent p={p} length={n}',not bd(rep,p) and rank(inc+[{index[rep]:1}],p)==ri+1)
  ranks.append(dict(prime=p,length=n,dimension=len(words),outgoing_rank=ro,incoming_rank=ri,original_representative=rep))
 for m,n in product(range(5),repeat=2):
  um=(p-1,1)*m;un=(p-1,1)*n;vm=(1,)+um;vn=(1,)+un
  ck(f'full integer divided-power shuffle p={p} m={m} n={n}',sh(um,un)=={um+un:comb(m+n,m)})
  ck(f'full integer odd-even shuffle p={p} m={m} n={n}',sh(vm,un)=={(1,)+um+un:comb(m+n,m)})
  ck(f'full integer even-odd shuffle p={p} m={m} n={n}',sh(um,vn)=={(1,)+um+un:comb(m+n,m)})
  ck(f'full integer odd-odd shuffle p={p} m={m} n={n}',not sh(vm,vn))
 for i in range(2,p):ck(f'original one-letter decomposable boundary p={p} exponent={i}',bd((i-1,1),p)=={(i,):p-1})
 for d in [0,2,4,6]:
  for n in range(6):
   ck(f'original even resolution bidegrees p={p} d={d} n={n}',sum((p-1,1)*n)*d==n*p*d)
   ck(f'original odd resolution bidegrees p={p} d={d} n={n}',sum((1,)+(p-1,1)*n)*d==(n*p+1)*d)
# Original graded generator recursion, including every truncated-algebra power.
generators_by_stage=[]
for p in [3,5,7,11,13]:
 gs=[('T',0)];target=[1,1,0,0,1,2,1,0] if p==3 else [1,1,0,0,0,0,0,0]
 for q in range(1,13):
  new=[]
  for kind,d in gs:
   new.append(('T' if kind=='E' else 'E',d+1))
   start=d+1 if kind=='E' else p*d+2
   j=1 if kind=='E' else 0
   while p**j*start-q<=7:
    new.append(('T',p**j*start));j+=1
  gs=new
  ck(f'all original generator parities p={p} stage={q}',all((d%2==1)==(kind=='E') for kind,d in gs))
  ck(f'all original generator excesses p={p} stage={q}',all(0<=d-q<=7 for _,d in gs))
  dims=[0]*(q+8);dims[0]=1
  for kind,d in gs:
   old=dims[:];dims=[0]*len(old)
   for power in range(2 if kind=='E' else p):
    for n,c in enumerate(old):
     if n+power*d<len(old):dims[n+power*d]+=c
  ex=[sum(d-q==r for _,d in gs) for r in range(8)]
  if q>=4:ck(f'exact eventual cooperation generator count p={p} stage={q}',ex==target)
  if q>=8:ck(f'actual low-degree homology equals generator count p={p} stage={q}',dims[q:q+8]==target)
  generators_by_stage.append(dict(prime=p,stage=q,generators=gs,excess_counts=ex,homology_at_excess_0_through_7=dims[q:q+8]))
for p in [3,5,7]:
 for n in range(121):
  remaining=n;j=0;den=1
  while remaining:
   digit=remaining%p;remaining//=p;den*=factorial(p**j)**digit;j+=1
  cn=factorial(n)//den
  ck(f'full original divided-power coefficient and inverse p={p} N={n}',factorial(n)%den==0 and cn%p!=0 and cn*pow(cn%p,-1,p)%p==1)

# Exact sign conjugacy from the alternating resolution to the original cobar.
for length in range(1,7):
 valid=True
 for degrees in product(range(1,5),repeat=length):
  eps=length+sum((length-j-1)*d for j,d in enumerate(degrees))
  for j,d in enumerate(degrees):
   for b in range(1,d):
    split=degrees[:j]+(b,d-b)+degrees[j+1:]
    epnew=length+1+sum((length-i)*v for i,v in enumerate(split))
    left=j+1+epnew;right=eps+sum(v-1 for v in degrees[:j])+b
    valid &= (left-right)%2==0
 ck(f'full original cobar sign conjugacy length={length}',valid)

# Complete signed preimages of original degree-six words at p=3.
dd={'t':{},'x':{},'tx':{('t','x'):2,('x','t'):1},'x2':{('x','x'):2}}
excess={'t':0,'x':3,'tx':4,'x2':7}
def cd(poly):
 out={}
 for word,c in poly.items():
  pref=0
  for j,letter in enumerate(word):
   for rep,z in dd[letter].items():add(out,word[:j]+rep+word[j+1:],c*(-1)**pref*z,3)
   pref+=excess[letter]
 return out
for a,b,c in product(range(5),repeat=3):
 original=('t',)*a+('x',)+('t',)*b+('x',)+('t',)*c;current=original;pre={}
 while ('x','t') in tuple(zip(current,current[1:])):
  j=next(i for i in range(len(current)-1) if current[i:i+2]==('x','t'))
  pref=current[:j];suf=current[j+2:];add(pre,pref+('tx',)+suf,(-1)**sum(excess[z] for z in pref),3)
  current=pref+('t','x')+suf
 add(pre,('t',)*(a+b+c)+('x2',),2,3)
 ck(f'full actual signed cobar preimage a={a} b={b} c={c}',cd(pre)=={original:1})
# The two worked exercises retain their full integer coefficients and all terms.
ck('exercise 7.1 original coefficients and bidegrees',comb(6,3)*comb(7,1)==140 and comb(6,3)*comb(9,3)==1680 and 1680%3==0 and 1680%9!=0 and (2*7,6*7,8*7)==(14,42,56) and (2*9,6*9,8*9)==(18,54,72))
ck('exercise 7.1 original inverse and nonzero representative',140%3==2 and (2*140)%3==1 and not bd((2,1)*9,3))
ck('exercise 7.2 complete original four-term preimage',cd({('tx','x','t'):1,('t','x','tx'):-1,('t','tx','x'):1,('t','t','x2'):2})=={('x','t','x','t'):1})
src=W/'src/the-original-odd-prime-cooperations-and-degree-six-adams-calculation.md'
r=dict(passed=len(checks),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),checks=checks,full_bar_ranks=ranks,generators_by_stage=generators_by_stage,scope='Finite supplementary checks, including all retained letters at the stated primes and lengths, full stable-range generator recursion and algebra powers, original divided-power coefficients, suspension/cobar signs and exact all-term sample preimages. The geometric comparisons, all-index arguments and convergence are proved in the local text; these finite checks do not certify those proofs.',publication=False)
(W/'checks/ODD_PRIME_BAR_CHECKS.json').write_text(json.dumps(r,indent=2)+'\n','utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=r['source_sha256'])))
