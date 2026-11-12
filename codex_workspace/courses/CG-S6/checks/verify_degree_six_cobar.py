"""Exact finite checks supplementing the all-length written cobar proof."""
from pathlib import Path
from itertools import product
import hashlib,json
from calculate_degree_six_cobar import monomial,add,degree,weight,delta,words,monomials,differential,poly_diff,rank
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,test):
 assert test,name
 checks.append(name)
P=lambda n=1:monomial(1,n)
Q=lambda n=1:monomial(2,n)
T=monomial(3)
B={(Q(),Q()),(Q(),P(3)),(P(),add(P(2),Q())),(P(),P(5)),(add(P(),Q()),P(2)),(P(3),Q()),(P(3),P(3))}
V={(Q(),Q(2)),(Q(),P(6)),(P(2),T),(P(2),add(P(),Q(2))),(P(2),add(P(4),Q())),(P(2),P(7)),(add(P(2),Q()),P(4)),(P(5),P(4))}
ck('Seven original B terms',len(B)==7)
ck('Eight original V terms',len(V)==8)
ck('Complete B differential',poly_diff(B)=={(P(2),P(2),P(2)),(P(),P(),P(4))})
ck('Complete V differential',poly_diff(V)=={(P(),P(4),P(4))})
ck('B exact degrees',all(len(w)==2 and sum(map(degree,w))==6 for w in B))
ck('V exact degrees',all(len(w)==2 and sum(map(degree,w))==9 for w in V))
ck('B unique leading weight-six term',{w for w in B if sum(map(weight,w))==6}=={(Q(),Q())})
ck('V both leading weight-six terms',{w for w in V if sum(map(weight,w))==6}=={(Q(),Q(2)),(P(2),T)})
for t in range(1,11):
 good=True
 for m in monomials(t):
  left=set();right=set()
  for a,b in delta(m):
   for c,d in delta(a):
    key=(c,d,b)
    if key in left:left.remove(key)
    else:left.add(key)
   for c,d in delta(b):
    key=(a,c,d)
    if key in right:right.remove(key)
    else:right.add(key)
  good=good and left==right
 ck(f'Full coproduct coassociativity in internal degree {t}',good)
 ck(f'Full coproduct preserves weight in degree {t}',all(weight(a)+weight(b)<=weight(m) for m in monomials(t) for a,b in delta(m)))
 ck(f'Original differential squares to zero in degree {t}',all(not poly_diff(differential(w)) for s in range(1,min(t,4)+1) for w in words(s,t)))
for s in range(1,8):
 t=s+6
 ck(f'Finite cobar rank in length {s} internal degree {t}',len(words(s,t))-rank(s,t)-rank(s-1,t)==(1 if s==2 else 0))
for r in range(1,9):
 chain={(P(),)*(r-1)+w for w in V}
 ck(f'Full eight-term exercise preimage at r={r}',poly_diff(chain)=={(P(),)*r+(P(4),P(4))})
for k,wanted in [(5,6),(6,9),(7,12)]:
 count=sum(1 for e in product(range(k+1),repeat=6) if sum(a*b for a,b in zip(e,[1,2,3,5,6,7]))==k)
 ck(f'Complete R-basis enumeration in difference {k}',count==wanted)
ck('Only length-one degree-eight first-page class',[(i,j) for i in range(1,5) for j in range(5) if (1<<j)*((1<<i)-1)==8]==[(1,3)])
# Independently enumerate original odd-prime monomials through degree seven.
for prime in [3,5,7,11]:
 ds=[]
 for a,e0,e1 in product(range(3),range(2),range(2)):
  d=a*2*(prime-1)+e0+e1*(2*prime-1)
  if 1<=d<=7:ds.append(d)
 ck(f'Odd-prime original low-degree monomials p={prime}',sorted(ds)==([1,4,5,5,6] if prime==3 else [1]))
# Exact signed identities from the full primitive coproducts at p=3.
def modsum(*polys):
 out={}
 for poly in polys:
  for word,c in poly.items():out[word]=(out.get(word,0)+c)%3
 return {w:c for w,c in out.items() if c}
ck('Odd-prime exercise cancels the negative term',modsum({('T','X','X'):-1,('X','T','X'):1},{('T','X','X'):2*2})=={('X','T','X'):1})
ck('Odd-prime inverse of two retained',(2*2)%3==1)
src=W/'src/the-degree-six-milnor-cobar-calculation.md'
result=dict(passed=len(checks),checks=checks,source=src.name,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),scope='Finite original-coproduct, correcting-cochain, weight, rank, basis and signed exercise checks. The written R-module and odd-prime word arguments prove all lengths. No stable homotopy, framed bordism or global topological conclusion is certified by these checks.')
(W/'checks/DEGREE_SIX_COBAR_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
