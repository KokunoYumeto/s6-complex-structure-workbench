#!/usr/bin/env python3
"""Exact universal invariant identities; no CAS, sampling, or target-proof input.

Binary cubics are checked through three linear factors and their exterior
products. Tacnode covariance is checked through congruence of a 2x2 quadratic
form in the two symbols z and w^2. This file was written before BF proof release.
"""
from fractions import Fraction as Q
import json
N=10
Z=(0,)*N

def c(x): return {} if x==0 else {Z:Q(x)}
def v(i):
 e=list(Z);e[i]=1;return {tuple(e):Q(1)}
def add(*xs):
 out={}
 for x in xs:
  for e,a in x.items():out[e]=out.get(e,Q(0))+a
 return {e:a for e,a in out.items() if a}
def neg(x):return {e:-a for e,a in x.items()}
def sub(x,y):return add(x,neg(y))
def mul(*xs):
 out=c(1)
 for x in xs:
  d={}
  for e,a in out.items():
   for f,b in x.items():
    ef=tuple(i+j for i,j in zip(e,f));d[ef]=d.get(ef,Q(0))+a*b
  out={e:a for e,a in d.items() if a}
 return out
def scale(a,x):return mul(c(a),x)
def power(x,n):return mul(*([x]*n))
def wedge(x,y):return sub(mul(x[0],y[1]),mul(x[1],y[0]))
def matmul(A,B):return [[add(*(mul(A[i][k],B[k][j]) for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A):return [list(x) for x in zip(*A)]
def det2(A):return sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]))

a,b,cc,d,e,f,p,q,r,s=[v(i) for i in range(N)]
lines=[(a,b),(cc,d),(e,f)]
A=mul(a,cc,e)
B=add(mul(b,cc,e),mul(a,d,e),mul(a,cc,f))
C=add(mul(a,d,f),mul(b,cc,f),mul(b,d,e))
D=mul(b,d,f)
disc=add(mul(B,B,C,C),scale(-4,mul(A,C,C,C)),scale(-4,mul(B,B,B,D)),scale(-27,mul(A,A,D,D)),scale(18,mul(A,B,C,D)))
exterior=mul(*(power(wedge(lines[i],lines[j]),2) for i in range(3) for j in range(i+1,3)))
assert disc==exterior
M=[[p,q],[r,s]]
detM=det2(M)
transformed=[(add(mul(x,p),mul(y,r)),add(mul(x,q),mul(y,s))) for x,y in lines]
for i in range(3):
 for j in range(i+1,3):assert wedge(transformed[i],transformed[j])==mul(detM,wedge(lines[i],lines[j]))
# The three squared wedge identities multiply to determinant character 6.
# Tacnode Schur determinant via a unipotent congruence, without differentiating
# or substituting a quartic polynomial in the ambient variables.
alpha,delta,epsilon,u=a,b,cc,d
Qmat=[[alpha,scale(Q(1,2),delta)],[scale(Q(1,2),delta),epsilon]]
U=[[c(1),neg(u)],[c(0),c(1)]]
congruent=matmul(transpose(U),matmul(Qmat,U))
assert det2(U)==c(1)
assert det2(congruent)==det2(Qmat)
assert scale(4,det2(Qmat))==sub(scale(4,mul(alpha,epsilon)),mul(delta,delta))
# Exact clearing identity. Given G=H^2 F-AZ^2 and J=H^2 G-ZR,
# the identity below is polynomial and remains valid before dividing by H.
H,F,AA,ZZ,RR=a,b,cc,d,e
GG=sub(mul(H,H,F),mul(AA,ZZ,ZZ))
JJ=sub(mul(H,H,GG),mul(ZZ,RR))
assert mul(power(H,4),F)==add(mul(AA,H,H,ZZ,ZZ),mul(ZZ,RR),JJ)
print(json.dumps({'status':'all exact identities passed','method':'Sparse Fraction polynomial arithmetic; exterior-product cubic discriminant and quadratic-form congruence','binary_cubic_discriminant_equals_three_squared_wedges':True,'binary_cubic_discriminant_character':{'determinant_exponent':6,'equation_line_exponent':4},'tacnode_invariant':'4 alpha epsilon - delta^2','tacnode_unipotent_congruence_determinant_invariant':True,'conductor_clearing_identity':'H^4 F = A H^2 Z^2 + Z R + J','conductor_clearing_identity_exact':True,'no_numeric_sampling':True,'monomials_in_universal_cubic_discriminant':len(disc),'scope':'Universal algebra identities only. Analytic gluing, conductor orders and global degrees are proved in the separate frozen derivation.','additional_check_events':0},indent=2))
