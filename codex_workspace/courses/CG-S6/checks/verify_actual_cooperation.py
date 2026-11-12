"""Exact examples for the full cofree differential, contraction and reversal."""
from pathlib import Path
from functools import lru_cache
import hashlib,json
from calculate_degree_six_cobar import ZERO,monomial,monomials,words,delta,degree,differential,poly_diff,toggle
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,test):
 assert test,name
 checks.append(name)
def linear(function,terms):
 out=set()
 for term in terms:
  for x in function(term):toggle(out,x)
 return out
@lru_cache(None)
def jd(term):
 g,w=term;out=set()
 for a,b in delta(g):
  if b!=ZERO:toggle(out,(a,(b,)+w))
 for z in differential(w):toggle(out,(g,z))
 return frozenset(out)
def h(term):
 g,w=term
 if g!=ZERO:return frozenset()
 if not w:return frozenset({('augmentation',)})
 return frozenset({(w[0],w[1:])})
def dh(term):
 out=set()
 for z in h(term):
  terms={(ZERO,())} if z==('augmentation',) else jd(z)
  for v in terms:toggle(out,v)
 return out
def hd(term):return linear(h,jd(term))
def plus(a,b):return set(a)^set(b)
def coproduct_twice(m,left):
 out=set()
 for a,b in delta(m):
  for c,d in delta(a if left else b):toggle(out,(c,d,b) if left else (a,c,d))
 return out
def opposite_diff(w):
 out=set()
 for i,m in enumerate(w):
  for a,b in delta(m):
   if a!=ZERO and b!=ZERO:toggle(out,w[:i]+(b,a)+w[i+1:])
 return out
def jb(s,t):
 return tuple((g,w) for a in range(t+1) for g in monomials(a) for w in words(s,t-a))
for t in range(11):
 ck(f'Full coalgebra coassociativity, degree {t}',all(coproduct_twice(m,True)==coproduct_twice(m,False) for m in monomials(t)))
 ck(f'Both original counits, degree {t}',all({b for a,b in delta(m) if a==ZERO}=={m} and {a for a,b in delta(m) if b==ZERO}=={m} for m in monomials(t)))
 for s in range(min(4,t)+1):
  basis=jb(s,t)
  ck(f'Entire cofree differential squares to zero, length {s}, degree {t}',all(not linear(jd,jd(v)) for v in basis))
  ck(f'Augmented full contraction identity, length {s}, degree {t}',all(plus(dh(v),hd(v))=={v} for v in basis))
  ck(f'Primitive restriction equals cobar differential, length {s}, degree {t}',all(jd((ZERO,w))==frozenset((ZERO,z) for z in differential(w)) for w in words(s,t)))
  ck(f'Opposite-coalgebra reversal, length {s}, degree {t}',all({tuple(reversed(z)) for z in differential(w)}==opposite_diff(tuple(reversed(w))) for w in words(s,t)))
x=monomial(1);x2=monomial(1,2);y=monomial(2)
ck('Retain both degree-one endpoints',delta(x)=={(ZERO,x),(x,ZERO)})
ck('Degree-two full coproduct is primitive',delta(x2)=={(ZERO,x2),(x2,ZERO)})
ck('Original noncocommutative degree-three term',delta(y)=={(ZERO,y),(x2,x),(y,ZERO)} and {(b,a) for a,b in delta(y)}!=delta(y))
ck('Exercise full differential',jd((ZERO,(y,)))=={(ZERO,(x2,x))})
ck('Exercise first composite',hd((ZERO,(y,)))=={(x2,(x,))})
ck('Exercise second composite',dh((ZERO,(y,)))=={(ZERO,(y,)),(x2,(x,))})
# Independently enumerate all degree compositions, not the coalgebra monomial routine.
@lru_cache(None)
def compositions(length,total):
 if length==0:return ((),) if total==0 else ()
 return tuple((a,)+rest for a in range(1,total-length+2) for rest in compositions(length-1,total-a))
for n in [5,6]:
 for s in range(1,13):
  for shift,label in [(-1,'incoming'),(0,'middle'),(1,'outgoing')]:
   length=s+shift;total=s+n;rows=compositions(length,total);bound=n+1-shift
   ck(f'Exact original support bound, stem {n}, length {s}, {label}',all(sum(d-1 for d in row)==n-shift and all(1<=d<=bound for d in row) for row in rows))
   if length>0:ck(f'Support bound attained, stem {n}, length {s}, {label}',any(bound in row for row in rows))
src=W/'src/the-actual-mod-two-adams-resolution-and-cooperation-maps.md'
out=dict(passed=len(checks),checks=checks,source=src.name,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
 scope='Full algebraic cofree-resolution examples through internal degree ten and length four, including both counits, all endpoints, the contraction and coproduct reversal. Independent degree-composition enumeration tests the receiving support bound through length twelve. These checks do not identify the actual cooperation algebra or certify a topological classification. The all-degree construction and both resolution homotopies are the written proof.')
(W/'checks/ACTUAL_COOPERATION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=out['source_sha256'])))
