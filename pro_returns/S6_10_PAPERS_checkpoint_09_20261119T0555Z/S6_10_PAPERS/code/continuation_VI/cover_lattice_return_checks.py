#!/usr/bin/env python3
"""Independent exact continuation calculations; no inherited programs imported."""
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd,lcm
from functools import reduce
from pathlib import Path
import json

def I(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def tr(A):return list(map(list,zip(*A)))
def mp(A,n):
 B=I(len(A))
 for _ in range(n):B=mm(B,A)
 return B

def det(A):
 A=[list(map(Q,r)) for r in A];v=Q(1)
 for i in range(len(A)):
  j=next((j for j in range(i,len(A)) if A[j][i]),None)
  if j is None:return Q(0)
  if j!=i:A[i],A[j]=A[j],A[i];v=-v
  a=A[i][i];v*=a
  for j in range(i+1,len(A)):
   b=A[j][i]/a
   for k in range(i,len(A)):A[j][k]-=b*A[i][k]
 return v

def rref(A):
 A=[list(map(Q,r)) for r in A];p=[];r=0
 for c in range(len(A[0])):
  j=next((j for j in range(r,len(A)) if A[j][c]),None)
  if j is None:continue
  A[r],A[j]=A[j],A[r];a=A[r][c];A[r]=[x/a for x in A[r]]
  for j in range(len(A)):
   if j!=r:
    a=A[j][c];A[j]=[x-a*y for x,y in zip(A[j],A[r])]
  p.append(c);r+=1
  if r==len(A):break
 return A,p

def kernel(A):
 R,p=rref(A);free=[j for j in range(len(A[0])) if j not in p];out=[]
 for j in free:
  v=[Q(0)]*len(A[0]);v[j]=1
  for row,i in enumerate(p):v[i]=-R[row][j]
  out.append(v)
 return out

def inertia(A):
 # Rational congruence diagonalization. A zero diagonal with a nonzero
 # offdiagonal gives a hyperbolic 2x2 pivot; no floating eigenvalues.
 A=[list(map(Q,r)) for r in A];pos=neg=zero=0
 while A:
  n=len(A);p=next((i for i in range(n) if A[i][i]),None)
  if p is not None:
   order=[p]+[i for i in range(n) if i!=p];A=[[A[i][j] for j in order] for i in order];a=A[0][0]
   pos+=a>0;neg+=a<0
   A=[[A[i][j]-A[i][0]*A[0][j]/a for j in range(1,n)] for i in range(1,n)]
  else:
   pair=next(((i,j) for i in range(n) for j in range(i+1,n) if A[i][j]),None)
   if pair is None:zero+=n;break
   i,j=pair;order=[i,j]+[k for k in range(n) if k not in pair];A=[[A[i][j] for j in order] for i in order];a=A[0][1]
   pos+=1;neg+=1
   A=[[A[i][j]-(A[i][0]*A[1][j]+A[i][1]*A[0][j])/a for j in range(2,n)] for i in range(2,n)]
 return [pos,neg,zero]

def conv(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def companion(p):
 n=len(p)-1;A=[[0]*n for _ in range(n)]
 for j in range(n-1):A[j+1][j]=1
 for i in range(n):A[i][-1]=-p[i]
 return A

phi={1:[-1,1],2:[1,1],3:[1,1,1],4:[1,0,1],5:[1,1,1,1,1],6:[1,-1,1],8:[1,0,0,0,1],10:[1,-1,1,-1,1],12:[1,0,-1,0,1]}
patterns=[]
for counts in product(range(5),range(5),range(3),range(3),range(3),range(2),range(2),range(2),range(2)):
 keys=[1,2,3,4,6,5,8,10,12]
 if counts[0]%2 or counts[1]%2:continue
 if sum(c*(len(phi[k])-1) for c,k in zip(counts,keys))!=4:continue
 factors=[k for c,k in zip(counts,keys) for _ in range(c)];patterns.append(sorted(factors))
assert len(patterns)==19
monodromy=[]
for factors in sorted(patterns):
 p=[1]
 for n in factors:p=conv(p,phi[n])
 A=companion(p);M=lcm(*factors);vals=[]
 for k in range(1,M+1):
  P=mp(A,k);vals.append(int(det([[Q(i==j)-P[i][j] for j in range(4)] for i in range(4)])))
 j=Q(sum(vals),M);assert j in [0,4,6,8]
 coeff={}
 for n in range(1,M+1):
  if M%n==0:coeff[n]=Q(vals[n-1]-sum(d*c for d,c in coeff.items() if n%d==0),n)
 assert sum(coeff.values())==j
 monodromy.append({'factors':factors,'semisimple_order':M,'lefschetz_period':vals,'average':int(j),'zero_index':int(j/2),'acampo_coefficients':{str(k):int(v) if v.denominator==1 else str(v) for k,v in coeff.items()}})

pairs=list(combinations(range(4),2));B=[]
for a in pairs:
 row=[]
 for b in pairs:
  s=a+b;row.append(0 if len(set(s))<4 else (-1)**sum(s[i]>s[j] for i in range(4) for j in range(i+1,4)))
 B.append(row)
invariants=[]
for tag,entries,expected in [('identity',[],[3,3,0]),('rank_one',[(0,1,1)],[1,1,2]),('rank_two_positive',[(0,1,1),(2,3,1)],[1,2,1]),('rank_two_negative',[(0,1,1),(2,3,-1)],[2,1,1])]:
 A=I(4)
 for i,j,a in entries:A[i][j]=a
 G=[[A[i][k]*A[j][l]-A[i][l]*A[j][k] for k,l in pairs] for i,j in pairs]
 K=kernel([[x-Q(i==j) for j,x in enumerate(row)] for i,row in enumerate(G)])
 Gram=mm(mm(K,B),tr(K));sig=inertia(Gram);assert sig==expected
 invariants.append({'type':tag,'kernel_basis':K,'gram':Gram,'inertia':sig})

# Reconstruct branch-index counts from exact lattice fixed-point determinants.
local={(2,1):('I0*',6),(3,1):('IV',4),(3,2):('IV*',8),(4,1):('III',3),(4,3):('III*',9),(6,1):('II',2),(6,5):('II*',10)}
elliptic=[];configs=set()
for n in [2,3,4,6]:
 A=[[-1,0],[0,-1]] if n==2 else companion(phi[n]);exact={};branches=[]
 for e in sorted([e for e in range(2,n+1) if n%e==0],reverse=True):
  P=mp(A,n//e);fixed=abs(int(det([[Q(i==j)-P[i][j] for j in range(2)] for i in range(2)])))
  exact[e]=fixed-sum(c for d,c in exact.items() if d%e==0)
  assert exact[e]%(n//e)==0
  branches += [e]*(exact[e]//(n//e))
 for a in range(1,n):
  types=[];euler=0
  for e in branches:
   r=a%e
   if not r:continue
   c=gcd(r,e);typ,val=local[(e//c,r//c)];types.append(typ);euler+=val
  assert euler in [12,24];configs.add(tuple(sorted(types)))
  elliptic.append({'base_order':n,'branch_indices':sorted(branches),'fibre_character':a,'types':sorted(types),'euler':euler,'chi':euler//12})
for d in [2,3,4,6]:configs.add(tuple(sorted([local[(d,1)][0],local[(d,d-1)][0]])))
assert len(configs)==11

# Meridians: compare Smith invariants by gcds of minors, independently of any
# row-reduction/Smith implementation in the inherited code.
def smith_invariants(rows):
 n=len(rows);m=len(rows[0]);prev=1;diags=[]
 for k in range(1,min(n,m)+1):
  g=0
  for rr in combinations(range(n),k):
   for cc in combinations(range(m),k):
    z=det([[rows[i][j] for j in cc] for i in rr]);assert z.denominator==1;g=gcd(g,abs(int(z)))
    if g==1:break
   if g==1:break
  if g==0:break
  assert g%prev==0;diags.append(g//prev);prev=g
 return {'free_rank':n-len(diags),'torsion':[v for v in diags if v>1]}
groups=[]
for d in [1,2,3]:
 for seed in range(5):
  T=I(4);T[0][1]=seed%3-1;T[2][3]=(seed+1)%3-1
  vs=[[seed+1,1,-seed,2],[1,-seed-1,2,seed]];ns=[2,3];v0=[-x+y for x,y in zip(*vs)]
  Td=mp(T,d);cols=[[Td[i][j]-Q(i==j) for i in range(4)] for j in range(4)]
  cover=[c+[Q(0)] for c in cols]
  for v,n in zip(vs,ns):
   for j in range(d):
    Tv=[r[0] for r in mm(mp(T,j),[[Q(x)] for x in v])]
    cols.append([x-n*y for x,y in zip(Tv,v0)]);cover.append(Tv+[Q(n)])
  a=smith_invariants(tr(cols));b=smith_invariants(tr(cover));assert a==b
  groups.append({'d':d,'seed':seed,'invariants':a})

# Exact truncated polynomials in (s,z), newly implemented dictionary arithmetic.
def add(A,B):
 C=A.copy()
 for k,v in B.items():C[k]=C.get(k,0)+v
 return {k:v for k,v in C.items() if v}
def scale(A,c):return {k:v*c for k,v in A.items() if v*c}
def pmul(A,B,limit):
 C={}
 for (s,z),v in A.items():
  for (t,w),u in B.items():
   if s+t<=limit:C[s+t,z+w]=C.get((s+t,z+w),0)+v*u
 return {k:v for k,v in C.items() if v}
def ppow(A,n,limit):
 C={(0,0):1}
 for _ in range(n):C=pmul(C,A,limit)
 return C
def dz(A):return {(s,z-1):v*z for (s,z),v in A.items() if z}
def shift(A,d):return {(s+d,z):v for (s,z),v in A.items()}
def compose(A,P,limit):
 C={}
 for (s,z),v in A.items():C=add(C,scale(shift(ppow(P,z,limit-s),s),v))
 return {k:v for k,v in C.items() if k[0]<=limit}
def coefficient(A,s):return {z:v for (t,z),v in A.items() if t==s}
return_tests=[]
z={(0,1):1}
for d in range(1,9):
 limit=2*d+1;a={(0,0):2,(0,1):-1,(0,2):3};b={(0,0):5,(0,1):2};c={(0,2):-7};psi={(0,0):1,(0,1):4,(0,2):-2};psi1={(0,0):3,(0,1):-2}
 A=add(add(shift(a,d),shift(b,d+1)),shift(c,d+2));P=add(add(z,shift(psi,d)),shift(psi1,d+1))
 first=add(compose(A,P,limit),scale(pmul(A,dz(P),limit),-1))
 expected=add(pmul(dz(a),psi,limit),scale(pmul(a,dz(psi),limit),-1))
 assert all(t>=2*d for t,w in first)
 assert coefficient(first,2*d)==coefficient(expected,0)
 H={(0,0):1,(0,1):2,(0,3):-1};h=add(H,shift(b,1));delta=add({(0,1):3,(0,2):2},shift(c,1))
 second=add(add(compose(h,P,limit),scale(h,-1)),scale(pmul(A,dz(delta),limit),-1))
 expected2=add(pmul(dz(H),psi,limit),scale(pmul(a,dz({k:v for k,v in delta.items() if k[0]==0}),limit),-1))
 assert all(t>=d for t,w in second)
 assert coefficient(second,d)==coefficient(expected2,0)
 return_tests.append({'normal_order':d,'first_order':'2d','second_order':'d','identities':'a_prime*psi-a*psi_prime; H_prime*psi-a*delta0_prime'})

out={'authorship':'New independent program, 19 November 2026; stdlib rational arithmetic and explicit polynomials only.',
 'monodromy_averages':monodromy,'invariant_lattice_forms':invariants,'elliptic_quotient_characters':elliptic,'distinct_positive_configurations':len(configs),
 'meridian_smith_comparisons':groups,'return_germ_coefficients':return_tests,
 'limits':'Finite exact computations verify all listed tables and displayed sample comparisons; general geometric and formal identities have written proofs.',
 'status':'all assertions passed'}
def clean(x):
 if isinstance(x,Q):return int(x) if x.denominator==1 else str(x)
 if isinstance(x,list):return [clean(y) for y in x]
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
 return x
out=clean(out);Path(__file__).with_name('cover_lattice_return_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'monodromy_rows':len(monodromy),'invariant_forms':[r['inertia'] for r in invariants],'elliptic_configurations':len(configs),'meridian_presentations':len(groups),'return_orders':[r['normal_order'] for r in return_tests],'status':out['status']},indent=2))
