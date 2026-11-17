"""Exact GF(2) cobar calculations with the full Milnor coproduct."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
W=Path(__file__).resolve().parent
ZERO=(0,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def toggle(out,k):
 if k in out:out.remove(k)
 else:out.add(k)
def degree(m):return sum(a*((1<<(i+1))-1) for i,a in enumerate(m))
def weight(m):return sum((2*i+1)*a.bit_count() for i,a in enumerate(m))
def monomial(i,n=1):
 a=list(ZERO);a[i-1]=n;return tuple(a)
def times(p,q):
 out=set()
 for a,b in p:
  for c,d in q:toggle(out,(add(a,c),add(b,d)))
 return out
@lru_cache(None)
def delta(m):
 out={(ZERO,ZERO)}
 for i,e in enumerate(m,1):
  g=set()
  for k in range(i+1):
   left=ZERO if i==k else monomial(i-k,1<<k)
   right=ZERO if k==0 else monomial(k)
   g.add((left,right))
  for j in range(e):out=times(out,g)
 return frozenset(out)
def differential(word):
 out=set()
 for i,m in enumerate(word):
  for a,b in delta(m):
   if a!=ZERO and b!=ZERO:toggle(out,word[:i]+(a,b)+word[i+1:])
 return out
def poly_diff(words):
 out=set()
 for word in words:
  for term in differential(word):toggle(out,term)
 return out
@lru_cache(None)
def monomials(t):
 out=[]
 def go(i,left,acc):
  if i==4:
   if left==0:out.append(tuple(acc))
   return
  d=(1<<(i+1))-1
  for a in range(left//d+1):go(i+1,left-a*d,acc+[a])
 go(0,t,[]);return tuple(sorted(out))
@lru_cache(None)
def words(s,t):
 if s==0:return ((),) if t==0 else ()
 return tuple((m,)+rest for a in range(1,t-s+2) for m in monomials(a) for rest in words(s-1,t-a))
def solve(s,t,target,max_weight=None):
 cols=[w for w in words(s,t) if max_weight is None or sum(map(weight,w))<=max_weight]
 rows=words(s+1,t);idx={w:i for i,w in enumerate(rows)};basis={}
 for k,w in enumerate(cols):
  v=sum(1<<idx[z] for z in differential(w));c=1<<k
  while v:
   j=v.bit_length()-1
   if j not in basis:basis[j]=(v,c);break
   a,b=basis[j];v^=a;c^=b
 v=sum(1<<idx[w] for w in target);c=0
 while v:
  j=v.bit_length()-1
  if j not in basis:return None
  a,b=basis[j];v^=a;c^=b
 result={w for k,w in enumerate(cols) if c>>k&1}
 assert poly_diff(result)==target
 return result
def display_m(m):return '*'.join('z'+str(i)+(('^'+str(e)) if e!=1 else '') for i,e in enumerate(m,1) if e) or '1'
def display(w):return '['+'|'.join(map(display_m,w))+']'
def rank(s,t):
 rows=words(s+1,t);idx={w:i for i,w in enumerate(rows)};basis={}
 for w in words(s,t):
  v=sum(1<<idx[z] for z in differential(w))
  while v:
   j=v.bit_length()-1
   if j not in basis:basis[j]=v;break
   v^=basis[j]
 return len(basis)
if __name__=='__main__':
 x=monomial(1);y=monomial(1,2);z=monomial(1,4)
 targets={'B':{(y,y,y),(x,x,z)},'V':{(x,z,z)}}
 result={}
 for name,target in targets.items():
  t=sum(map(degree,next(iter(target))))
  chain=solve(2,t,target,max_weight=6)
  assert chain is not None
  result[name]={'internal_degree':t,'chain':[display(w) for w in sorted(chain)],'differential':[display(w) for w in sorted(target)],'terms':[list(w) for w in sorted(chain)],'weights':[(display(w),sum(map(weight,w))) for w in sorted(chain)]}
 checks=[]
 for t in range(1,11):
  for s in range(1,min(4,t)+1):
   for w in words(s,t):assert not poly_diff(differential(w))
  checks.append({'internal_degree':t,'d_squared':True})
 for s in range(1,8):
  t=s+6; dim=len(words(s,t));coh=dim-rank(s,t)-rank(s-1,t)
  checks.append({'s':s,'t':t,'dimension':dim,'cohomology':coh})
 result['finite_checks']=checks
 (W/'DEGREE_SIX_COBAR_CALCULATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,indent=2))
