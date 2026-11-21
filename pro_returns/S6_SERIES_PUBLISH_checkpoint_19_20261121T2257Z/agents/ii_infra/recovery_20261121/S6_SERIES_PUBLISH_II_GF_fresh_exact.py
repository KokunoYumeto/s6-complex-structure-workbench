#!/usr/bin/env python3
"""Prerelease exact GF marking and integral-image calculations; stdlib only."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,combinations
from math import gcd
import json,hashlib,datetime
D=Path(__file__).resolve().parent
# Gaussian rational numbers are pairs, never floating-point complex numbers.
def z(a=0,b=0):return(F(a),F(b))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return(x[0],-x[1])
def det2(a):return add(mul(a[0][0],a[1][1]),neg(mul(a[0][1],a[1][0])))
def matmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return list(map(list,zip(*a)))
def real_matrix(m):
 # z_global=M z_local; real order is (Re C,Im C,Re B,Im B).
 a=[]
 for row in m:
  a.append(sum(([q[0],-q[1]] for q in row),[]));a.append(sum(([q[1],q[0]] for q in row),[]))
 return a
def det(a):
 out=F(0);n=len(a)
 for p in permutations(range(n)):
  v=F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
  for i in range(n):v*=a[i][p[i]]
  out+=v
 return out
def iota(v):return [(F(v[0],2),F(v[1],2)),(F(v[2],2),F(v[3],2))]
M=[[[z(0),z(1)],[z(1),z(0)]],[[z(0,1),z(0)],[z(0,1),z(1)]],[[z(1),z(0)],[z(0,1),z(1)]]]
K=[real_matrix(m) for m in M];dets=[det2(m) for m in M];assert dets==[z(-1),z(0,1),z(1)] and all(det(k)==1 for k in K)
w=[[0,0,1,0],[0,1,0,1],[1,0,0,1]];u=[[0,0,0,1],[-1,0,-1,0],[0,1,-1,0]]
for n,k in enumerate(K):assert [r[0] for r in k]==w[n] and [r[1] for r in k]==u[n]
transport=[]
for n,(m,k) in enumerate(zip(M,K)):
 for j in range(4):
  alpha=[int(j==v) for v in range(4)];pulled=[sum(k[v][l]*alpha[v] for v in range(4)) for l in range(4)];left=iota(pulled);a=iota(alpha);right=[add(mul(conj(m[0][l]),a[0]),mul(conj(m[1][l]),a[1])) for l in range(2)];assert left==right
 transport.append('iota(K_%s^T alpha)=conjugate(M_%s)^T iota(alpha), verified on all four integral basis covectors'%(n+1,n+1))
v=[1,1,0,-1];assert all(sum(x*y for x,y in zip(row,v))==0 for row in w)
minor_gcd=0
for cols in combinations(range(4),3):minor_gcd=gcd(minor_gcd,abs(int(det([[row[j] for j in cols] for row in w]))))
assert minor_gcd==1
# Solve c=0,b+d=0,a+d=0 over Z: (a,b,c,d)=n(1,1,0,-1).
for n in range(-7,8):assert [n,n,0,-n]==[n*x for x in v]
# Every local torsion rational image is a subset of the rational global image.
# This identity is a symbolic linear-map consequence; samples are not used to
# establish the all-rational assertion.
def serial(x):
 if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
 if isinstance(x,(list,tuple)):return [serial(a) for a in x]
 if isinstance(x,dict):return{k:serial(v) for k,v in x.items()}
 return x
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'construction_packet_sha256':'4112dd78ef95ec40705ddf294ac2dec2935bb3dae934fffb827488e98cdc8fc7','method':'Explicit Gaussian-rational coordinate pullback and integer kernel equations; no target proof or prior target program opened.','complex_marking_matrices':M,'complex_determinants':dets,'real_integral_markings':K,'real_determinants':[det(k) for k in K],'w_vectors':w,'u_vectors':u,'coherent_integral_transport':transport,'annihilator_equations':['c=0','b+d=0','a+d=0'],'primitive_integer_kernel_generator':v,'gcd_of_all_maximal_minors':minor_gcd,'kernel_iota':iota(v),'events_added':0}
f=D/'S6_SERIES_PUBLISH_II_GF_fresh_exact_output.json';f.write_text(json.dumps(serial(out),indent=2)+'\n');print(json.dumps({'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'all_checks_passed':True,'kernel':v,'transport_checks':12}))
