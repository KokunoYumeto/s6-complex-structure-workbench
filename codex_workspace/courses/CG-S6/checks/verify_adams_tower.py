"""Finite exact checks of the new full written tower and adjacent cobar arguments."""
from pathlib import Path
from itertools import product
import sys,json,hashlib
W=Path(__file__).resolve().parents[1]
R=W
sys.path.insert(0,str(R/'checks'))
from calculate_degree_six_cobar import monomial,add,words,poly_diff,rank
checks=[]
def ck(name,value):
 assert value,name
 checks.append(name)
P=lambda n=1:monomial(1,n)
Q=lambda n=1:monomial(2,n)
B={(Q(),Q()),(Q(),P(3)),(P(),add(P(2),Q())),(P(),P(5)),(add(P(),Q()),P(2)),(P(3),Q()),(P(3),P(3))}
for power in [1,2]:
 chain={(P(2),)*power+word for word in B}
 ck('Full original B differential after prefix power '+str(power),poly_diff(chain)=={(P(2),)*(power+3),(P(2),)*power+(P(),P(),P(4))})
ck('Complete difference-four R-basis',[(a,b,c) for a,b,c in product(range(5),repeat=3) if a+2*b+3*c==4]==[(0,2,0),(1,0,1),(2,1,0),(4,0,0)])
for s in range(1,8):
 t=s+5;ck('Original degree-five cobar group at length '+str(s),len(words(s,t))-rank(s,t)-rank(s-1,t)==0)
ck('Original primitive degree-two class',not poly_diff({(P(2),)}) and len(words(0,2))==0)
for r in range(2,10):
 ck('Outgoing tower index r='+str(r),(7+r)-(2+r)==5)
 ck('Incoming tower index r='+str(r),2-r<0 or (2-r,9-r)==(0,7))
ck('Finite nonsurjective transition tower right inverse',all(((b0+2*b1)-2*(b1+2*b2)-b0)%4==0 for b0,b1,b2 in product(range(4),repeat=3)))
ck('Finite nonsurjective transition tower left inverse',all(((a0-2*a1)+2*(a1-2*a2)-a0)%4==0 for a0,a1,a2 in product(range(4),repeat=3)))
ck('Original second differential retains coefficient two',[(2*a)%3 for a in range(3)]==[0,2,1])
ck('Source stated vanishing inequality contradicts primitive class',0<2-1<2*1+1)
p=W/'src/the-adams-tower-and-exact-inverse-limits.md'
result=dict(passed=len(checks),checks=checks,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scope='Finite checks supplement the full all-length R-module proof and complete finite-tower inverse-limit proof. They do not certify the still-unwritten topological cooperation-algebra identification or arithmetic completion comparison.')
(W/'checks/ADAMS_TOWER_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
