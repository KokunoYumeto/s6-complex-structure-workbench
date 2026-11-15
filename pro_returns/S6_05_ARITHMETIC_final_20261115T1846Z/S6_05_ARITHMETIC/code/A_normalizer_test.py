"""Exact diagnostic of potential normalizers; no unproved period relation used."""
import sympy as S

def mul(x,y):
 a,b,c,d=x;e,f,g,h=y
 return S.Matrix([a*e+3*b*f-c*g+3*d*h,a*f+b*e+c*h-d*g,a*g+c*e+3*b*h-3*d*f,a*h+d*e+b*g-c*f])
def bar(x):return S.Matrix([x[0],-x[1],-x[2],-x[3]])
def nr(x):return S.expand(mul(x,bar(x))[0])
one,i,j,k=[S.eye(4)[:,r] for r in range(4)]
V=S.Matrix.hstack((i+3*j)/2,(3*i+3*j)/2,3*k)
U=S.Matrix([[17,0,72],[0,1,0],[4,0,17]])
R=[S.diag(1,-1,1),S.diag(1,1,-1),S.Matrix([[2,-3,0],[1,-2,0],[0,0,1]]),S.Matrix([[10,-9,-36],[3,-2,-12],[2,-2,-7]]),S.Matrix([[17,0,-72],[0,1,0],[4,0,-17]])]
G=S.diag(1,-3,-18)
for name,g in [('elliptic3',(one+i+3*j+k)/2),('j',j),('1+j',one+j)]:
 A=S.Matrix.hstack(*[mul(mul(g,V[:,b]),bar(g))/nr(g) for b in range(3)])
 A=U*S.simplify(V[1:4,:].inv()*A[1:4,:])*U.inv()
 assert A.T*G*A==G
 print(name,'adjoint',A)
 print('source image',tuple(A*S.Matrix([0,0,1])))
 for h in R[1:]:
  C=A*(R[0]*h)*A.inv()
  print('conjugated generator integral?',all(x.q==1 for x in C),'matrix',C)
