# Post-release supplement. Pure integer arithmetic; no symbolic algebra library.
# A polynomial of degree <=d in each variable is determined by its values on a
# product of d+1 distinct integer points. Degree bounds follow from the displayed
# affine matrix entries and the four-factor determinant expansion.
from itertools import product
Z=(0,0); O=(1,0); I=(0,1)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sm(v):
 r=Z
 for x in v:r=add(r,x)
 return r
def mm(a,b):return [[sm(mul(x,y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
def zm(a):return all(v==Z for row in a for v in row)
J=[[Z,O,Z,Z],[neg(O),Z,Z,Z],[Z,Z,Z,O],[Z,Z,neg(O),Z]]
S=[[Z,O],[O,Z]]
for t in range(3):
 T=(t,0);iT=mul(I,T)
 P=[[O,I,T,iT],[neg(T),iT,O,neg(I)]]
 B=[[neg(iT),neg(T),I,O],[neg(I),O,neg(iT),T]]
 assert zm(mm(mm(P,J),tr(P)))
 assert mm(mm(S,P),J)==B
 assert zm(mm(B,tr(P)))
print('Gaussian-integer evaluations at t=0,1,2: PJP^t=0, B=SPJ, BP^t=0.')
print('Degree bounds: 2,1,2. Three distinct evaluation points certify all polynomial entries.')
def bareiss(a):
 a=[r[:] for r in a];sgn=1;prev=1;n=len(a)
 for k in range(n-1):
  if a[k][k]==0:
   r=next((r for r in range(k+1,n) if a[r][k]),None)
   if r is None:return 0
   a[k],a[r]=a[r],a[k];sgn=-sgn
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=a[i][j]*pivot-a[i][k]*a[k][j]
    assert num%prev==0
    a[i][j]=num//prev
  for i in range(k+1,n):a[i][k]=0
  prev=pivot
 return sgn*a[-1][-1]
for x,y in product(range(5),repeat=2):
 M=[[1,0,x,-y],[0,1,y,x],[-x,-y,1,0],[-y,x,0,-1]]
 assert bareiss(M)==-(1+x*x+y*y)**2
print('Bareiss integer determinants on 5x5 grid: det M=-(1+x^2+y^2)^2.')
print('Each side has degree at most4 in each variable; grid interpolation certifies identity.')
# Squared-norm identity as M^t M, by integer evaluations and quadratic bounds.
for x,y in product(range(3),repeat=2):
 M=[[1,0,x,-y],[0,1,y,x],[-x,-y,1,0],[-y,x,0,-1]]
 G=[[sum(M[k][i]*M[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
 assert G==[[(1+x*x+y*y)*int(i==j) for j in range(4)] for i in range(4)]
print('3x3 grid with degree<=2 in each variable certifies M^t M=(1+x^2+y^2)I4.')
Minf=[[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,1,0,0]]
assert bareiss(Minf)==-1
print('Infinity real-frame determinant:',bareiss(Minf))
