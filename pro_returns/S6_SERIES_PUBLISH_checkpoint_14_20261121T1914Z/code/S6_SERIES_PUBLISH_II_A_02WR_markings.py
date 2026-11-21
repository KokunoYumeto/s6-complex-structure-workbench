# Independent integer-lattice computation from the three supplied complex maps.
from itertools import permutations
I=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
M=[[[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]],[[0,-1,0,0],[1,0,0,0],[0,-1,1,0],[1,0,0,1]],[[1,0,0,0],[0,1,0,0],[0,-1,1,0],[1,0,0,1]]]
N=[M[0],[[0,1,0,0],[-1,0,0,0],[-1,0,1,0],[0,-1,0,1]],[[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]]]
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def det(a):
 out=0
 for p in permutations(range(4)):
  inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));v=(-1)**inv
  for i in range(4):v*=a[i][p[i]]
  out+=v
 return out
for j,(a,b) in enumerate(zip(M,N)):
 assert mm(a,b)==I and mm(b,a)==I and det(a)==1
 print(j,'real determinant',det(a),'two-sided inverse verified',b)
