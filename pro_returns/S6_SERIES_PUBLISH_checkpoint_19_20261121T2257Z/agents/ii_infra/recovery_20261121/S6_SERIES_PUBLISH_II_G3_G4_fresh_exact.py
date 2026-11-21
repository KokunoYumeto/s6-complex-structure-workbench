#!/usr/bin/env python3
"""Fresh prerelease exact arithmetic from the G3/G4 statement-only packets.
Standard-library rational polynomial Euclid, matrix elimination and integer
minor witnesses; no old target checking program is imported or opened.
"""
from fractions import Fraction as F
from itertools import permutations,combinations
from functools import reduce
from math import gcd
from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).resolve().parent

def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a

def padd(a,b):return trim([ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def pscale(a,c):return trim([c*x for x in a])
def pmul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def pdiv(a,b):
 a=trim(list(map(F,a)));b=trim(list(map(F,b)));q=[F(0)]*max(1,len(a)-len(b)+1)
 while any(a) and len(a)>=len(b):
  n=len(a)-len(b);c=a[-1]/b[-1];q[n]+=c;a=padd(a,pscale([F(0)]*n+b,-c))
 return trim(q),trim(a)
def xgcd(a,b):
 r0,r1=list(map(F,a)),list(map(F,b));s0,s1=[F(1)],[F(0)];t0,t1=[F(0)],[F(1)]
 while any(r1):
  q,r=pdiv(r0,r1);r0,r1=r1,r;s0,s1=s1,padd(s0,pscale(pmul(q,s1),-1));t0,t1=t1,padd(t0,pscale(pmul(q,t1),-1))
 c=r0[-1];return pscale(r0,1/c),pscale(s0,1/c),pscale(t0,1/c)
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a):return list(map(list,zip(*a)))
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def det(a):
 n=len(a);v=0
 for p in permutations(range(n)):
  inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));z=(-1)**inv
  for i in range(n):z*=a[i][p[i]]
  v+=z
 return v
def inv(a):
 n=len(a);m=[list(map(F,r))+list(map(F,e)) for r,e in zip(a,eye(n))]
 for j in range(n):
  k=next(i for i in range(j,n) if m[i][j]);m[j],m[k]=m[k],m[j];q=m[j][j];m[j]=[x/q for x in m[j]]
  for i in range(n):
   if i!=j:
    q=m[i][j];m[i]=[x-q*y for x,y in zip(m[i],m[j])]
 out=[r[n:] for r in m];assert mul(a,out)==eye(n);return out

def serial(x):
 if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
 if isinstance(x,list):return [serial(y) for y in x]
 if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
 return x
Q=[4,12,12,31];Qprime=[12,24,93];g,u,v=xgcd(Q,Qprime)
assert g==[1] and padd(pmul(u,Q),pmul(v,Qprime))==[1]
# P(t)=Q(t^4); Q(0)=4 and the leading coefficient at infinity is31.
P=[0]*13
for i,c in enumerate(Q):P[4*i]=c
Pprime=[(i+1)*P[i+1] for i in range(12)]
gp,up,vp=xgcd(P,Pprime);assert gp==[1]
B={
 '*':[[1,0,-6,-2],[0,-1,-1,1],[0,1,0,-1],[0,0,0,1]],
 '2':[[1,0,6,3],[0,1,2,1],[0,0,1,0],[0,0,0,1]],
 '+':[[1,0,0,0],[0,2,1,0],[0,-1,0,0],[0,0,0,1]],
 '-':[[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]]}
prod=reduce(mul,B.values(),eye(4));assert prod==eye(4)
A={k:transpose(inv(b)) for k,b in B.items()};Ds={k:sub(a,eye(4)) for k,a in A.items()}
for k in B:assert mul(transpose(B[k]),A[k])==eye(4) and det(B[k])==1
M=[sum((Ds[k][i] for k in B),[]) for i in range(4)];assert all(x==0 for x in M[0])
col=lambda k,j:[Ds[k][i][j] for i in range(4)]
w={'e2':[x-y for x,y in zip(col('-',1),col('+',1))], 'e3':[-x for x in col('-',1)],'e4':col('-',0)}
assert list(w.values())==[[0,1,0,0],[0,0,1,0],[0,0,0,1]]
mins=[]
for k in range(1,5):
 z=0
 for rows in combinations(range(4),k):
  for cols in combinations(range(16),k):z=gcd(z,abs(int(det([[M[i][j] for j in cols] for i in rows]))))
 mins.append(z)
assert mins==[1,1,1,0]
coh_stack=sum((sub(b,eye(4)) for b in B.values()),[])
# Exact symbolic constraints: B_- v=v gives d=c=0;
# B_+ v=v then gives b=0; every B_i fixes a e1.
assert sub(B['-'],eye(4))==[[0,0,0,-1],[0,0,1,0],[0,0,0,0],[0,0,0,0]]
assert all(mul(b,[[1],[0],[0],[0]])==[[1],[0],[0],[0]] for b in B.values())
G3=[[ -1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]];assert sub(G3,eye(4))==[[-2,0,0,0],[0,-2,0,0],[0,0,0,0],[0,0,0,0]]
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Fresh Python standard library Fraction polynomial Bezout identities, Gauss-Jordan inverse, explicit integer image generators and determinantal divisors. No SymPy, Smith library, old code or target argument used.','G3':{'discriminant_without_nonzero_scalar':P,'cubic_Q':Q,'Q_Qprime_gcd':g,'Q_bezout_u':u,'Q_bezout_v':v,'P_Pprime_gcd':gp,'P_bezout_u':up,'P_bezout_v':vp,'nonzero_constant':Q[0],'infinity_discriminant_factor':31,'monodromy':G3,'difference':sub(G3,eye(4)),'coinvariants':'Z^2 direct sum (Z/2)^2'},'G4':{'cohomology_matrices':B,'ordered_product':prod,'homology_dual_inverse_transposes':A,'difference_matrix':M,'explicit_image_basis_witnesses':w,'witness_formulas':{'e2':'(A_- -I)column2 -(A_+ -I)column2','e3':'-(A_- -I)column2','e4':'(A_- -I)column1'},'determinantal_divisors':mins,'Smith_diagonal':[1,1,1,0],'common_fixed_cohomology':'Z e1; B_- forces c=d=0 and B_+ then b=0','coinvariant_isomorphism':'[v1,v2,v3,v4] maps to v1 in Z; inverse n maps to [n e1]','t_prime':1,'r':4-1+1,'tested_unacted_count':4-1+4},'target_proofs_opened':False,'events_added':0}
f=D/'S6_SERIES_PUBLISH_II_G3_G4_fresh_exact_output.json';f.write_text(json.dumps(serial(out),indent=2)+'\n');print(json.dumps({'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'gcd':serial(g),'Q_bezout_u':serial(u),'Q_bezout_v':serial(v),'all_checks_passed':True,'coinvariant_witnesses':serial(w)}))
