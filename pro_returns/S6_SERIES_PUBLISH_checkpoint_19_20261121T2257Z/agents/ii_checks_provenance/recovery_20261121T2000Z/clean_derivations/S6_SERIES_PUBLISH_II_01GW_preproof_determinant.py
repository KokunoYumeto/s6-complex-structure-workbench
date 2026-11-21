import json
# Exact polynomials in(u,a,b,c,d), represented by coefficient dictionaries.
def add(A,B):
 C=A.copy()
 for e,v in B.items():
  C[e]=C.get(e,0)+v
  if C[e]==0:del C[e]
 return C
def neg(A):return {e:-v for e,v in A.items()}
def mul(A,B):
 C={}
 for e,v in A.items():
  for f,w in B.items():
   h=tuple(x+y for x,y in zip(e,f));C[h]=C.get(h,0)+v*w
 return {e:v for e,v in C.items() if v}
def const(v):return {(0,0,0,0,0):v} if v else {}
def var(k):
 e=[0]*5;e[k]=1;return {tuple(e):1}
u,a,b,c,d=[var(k) for k in range(5)];M=[[a,b],[c,d]]
out=[]
for B in [[[1,0],[0,1]],[[0,1],[-1,0]]]:
 K=[[add(const(B[i][j]),mul(u,M[i][j])) for j in range(2)] for i in range(2)]
 det=add(mul(K[0][0],K[1][1]),neg(mul(K[0][1],K[1][0])))
 detB=B[0][0]*B[1][1]-B[0][1]*B[1][0]
 linear=add(add(mul(const(B[1][1]),a),mul(const(B[0][0]),d)),neg(add(mul(const(B[0][1]),c),mul(const(B[1][0]),b))))
 expected=add(add(const(detB),mul(u,linear)),mul(mul(u,u),add(mul(a,d),neg(mul(b,c)))))
 assert det==expected and detB==1
 out.append({'B':B,'det_B':detB,'det_B_plus_uM':{str(e):v for e,v in sorted(det.items())},'constant_coefficient':det[(0,0,0,0,0)]})
print(json.dumps({'coefficient_certificates':out,'substitution':'u=2*pi*i*q; M=H_prime(q)','analytic_conclusion':'det(B+uM) tends to1 as q tends to0, so the period derivative is invertible on a sufficiently small punctured disc.'},indent=2))
