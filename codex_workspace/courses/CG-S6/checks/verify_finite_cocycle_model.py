"""Exact supplementary checks on the full finite cocycle model and all face maps."""
from pathlib import Path
from itertools import combinations
from math import comb
import json,hashlib,numpy as np
W=Path(__file__).resolve().parents[1]
checks=[];ranks=[]
def check(name,value):
 if not value: raise AssertionError(name)
 checks.append(name)
def faces(q,n):return list(combinations(range(q+1),n+1)) if n>=0 else []
def delta(q,n):
 b=faces(q,n); ix={v:i for i,v in enumerate(b)}; tar=faces(q,n+1)
 a=np.zeros((len(tar),len(b)),dtype=np.int64)
 for r,t in enumerate(tar):
  for i in range(n+2):a[r,ix[t[:i]+t[i+1:]]]+=(-1)**i
 return a
def pull(q,r,n,theta):
 b=faces(q,n);ix={v:i for i,v in enumerate(b)};tar=faces(r,n);a=np.zeros((len(tar),len(b)),dtype=np.int64)
 for i,t in enumerate(tar):
  v=tuple(theta[j] for j in t)
  if len(set(v))==len(v):a[i,ix[v]]=1
 return a
def extra(q,n):
 b=faces(q,n);ix={v:i for i,v in enumerate(b)};tar=faces(q+1,n);a=np.zeros((len(tar),len(b)),dtype=np.int64)
 for i,t in enumerate(tar):
  if t[0]>0:a[i,ix[tuple(v-1 for v in t)]]=1
 return a
def face(q,n,i):return pull(q,q-1,n,[j for j in range(q+1) if j!=i])
def degeneracy(q,n,i):return pull(q,q+1,n,[j if j<=i else j-1 for j in range(q+2)])
def cone_dual(q,n):
 # U^n -> U^(n-1), evaluation on the full cone chain with apex zero.
 b=faces(q,n);ix={v:i for i,v in enumerate(b)};tar=faces(q,n-1);a=np.zeros((len(tar),len(b)),dtype=np.int64)
 for i,t in enumerate(tar):
  if t[0]>0:a[i,ix[(0,)+t]]=1
 return a
def rank(a,p):
 a=a.copy()%p;r=0
 for j in range(a.shape[1]):
  pivot=next((k for k in range(r,a.shape[0]) if a[k,j]),None)
  if pivot is None:continue
  a[[r,pivot]]=a[[pivot,r]];a[r]=(a[r]*pow(int(a[r,j]),-1,p))%p
  for k in range(a.shape[0]):
   if k!=r and a[k,j]:a[k]=(a[k]-a[k,j]*a[r])%p
  r+=1
  if r==a.shape[0]:break
 return r
for q in range(8):
 for n in range(5):
  d=delta(q,n); dn=delta(q,n+1);dim=len(faces(q,n))
  check(f'Full integer coboundary square q={q}, n={n}',not np.any(dn@d))
  s_next=cone_dual(q,n+1)
  rhs=np.eye(dim,dtype=np.int64)
  lhs=s_next@d
  if n>0:lhs+=delta(q,n-1)@cone_dual(q,n)
  else:
   rhs[:,0]-=1
  check(f'Full cone identity including augmentation q={q}, n={n}',np.array_equal(lhs,rhs))
  for p in [2,3,5]:
   r=rank(d,p);ker=dim-r;want=1 if n==0 else (comb(q,n) if q>=n else 0)
   check(f'Cocycle dimension p={p}, q={q}, n={n}',ker==want)
   check(f'Exact image onto next cocycles p={p}, q={q}, n={n}',r==len(faces(q,n+1))-rank(dn,p))
   ranks.append(dict(p=p,q=q,n=n,dimension=dim,rank=r,kernel_dimension=ker))
for q in range(5):
 for n in range(4):
  e=extra(q,n);dim=len(faces(q,n))
  check(f'Extra degeneracy first face q={q}, n={n}',np.array_equal(face(q+1,n,0)@e,np.eye(dim,dtype=np.int64)))
  if q>=1:
   for i in range(1,q+2):
    check(f'Extra degeneracy face i={i}, q={q}, n={n}',np.array_equal(face(q+1,n,i)@e,extra(q-1,n)@face(q,n,i-1)))
  for i in range(1,q+2):
   check(f'Extra degeneracy repeat i={i}, q={q}, n={n}',np.array_equal(degeneracy(q+1,n,i)@e,extra(q+1,n)@degeneracy(q,n,i-1)))
  check(f'Two extra degeneracies q={q}, n={n}',np.array_equal(degeneracy(q+1,n,0)@e,extra(q+1,n)@e))
  for i in range(q+1):
   pb=degeneracy(q,n,i)
   pn=degeneracy(q,n+1,i)
   check(f'Full delta repeat compatibility q={q}, n={n}, i={i}',np.array_equal(delta(q+1,n)@pb,pn@delta(q,n)))
  if q>=1:
   for i in range(q+1):
    check(f'Full delta face compatibility q={q}, n={n}, i={i}',np.array_equal(delta(q-1,n)@face(q,n,i),face(q,n+1,i)@delta(q,n)))
for n in range(1,10):
 for q in range(n,2*n):
  # Enumerate every incoming fibre and outgoing base position in the first quadrant.
  incoming=[(r,q-r+1) for r in range(2,q+2) if (q-r+1==0 or (r>=n+1 and q-r+1>=n))]
  outgoing=[(q+1-r,r-1) for r in range(2,q+2) if (q+1-r==0 or (q+1-r>=n+1 and r-1>=n))]
  check(f'Only full transgression source n={n}, q={q}',incoming==[(q+1,0)])
  check(f'Only full transgression target n={n}, q={q}',outgoing==[(0,q)])
for p in [2,3,5]:
 # Original degree-zero element a lifts through (0,a), with edge coboundary a-0.
 for a in range(p):
  z=np.array([a],dtype=np.int64);lift=extra(0,0)@z
  check(f'Original endpoint sign p={p}, a={a}',list(lift)==[0,a] and list(delta(1,0)@lift)==[a])
for m in range(4):
 for n in range(4):
  for c in range(5):
   check(f'First original shift sign m={m}, n={n}, degree={c}',(n*c+m+n-(m+n*(c-1)))%2==0)
   check(f'Second original shift sign m={m}, n={n}, degree={c}',(n*c+m+n+c-(c-m+n+n*c))%2==0)
src=W/'src/the-adams-tower-and-exact-inverse-limits.md'
out=dict(passed=len(checks),checks=checks,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),ranks=ranks,scope='Finite exact checks of the original cochain identities, all maps in the selected degree ranges and the transgression support. The realization, bundle, all-degree finiteness and convergence proofs are the written arguments in Sections 8–11; finite tests are supplementary.')
(W/'checks/FINITE_COCYCLE_MODEL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps(dict(passed=len(checks),rank_records=len(ranks),source_sha256=out['source_sha256'])))
