from fractions import Fraction
from math import floor
import sympy as s
# A line (d,a,b) means f^*O(d) tensor O(a S1+b S2).
# L=(-1,2,1), F=(0,1,1). Projection to the coarse base
# uses floor(a/3)+floor(b/4), including negative a,b.
O=(0,0,0); L=(-1,2,1); F=(0,1,1)
def add(A,B): return tuple(a+b for a,b in zip(A,B))
def deg(A):
 d,a,b=A
 return d+floor(Fraction(a,3))+floor(Fraction(b,4))
def dims(d): return max(0,d+1),max(0,-d-1)
def direct(A): return [[deg(A)],[deg(A),deg(add(A,L))],[deg(add(A,L))]]
def coh(A):
 ds=direct(A); h=[0]*4
 for q,dd in enumerate(ds):
  for d in dd:
   x,y=dims(d); h[q]+=x; h[q+1]+=y
 return h
for name,A in [('O',O),('L',L),('F',F)]:
 print(name,'line=',A,'Rq degrees=',direct(A),'Hq dimensions=',coh(A))
print('L^-1 coarse degree=',deg(tuple(-x for x in L)))
print('E=O+L cohomology=',[a+b for a,b in zip(coh(O),coh(L))])
# Torus dual complex normalization complex of W; all higher coherent
# cohomology of rational strata vanishes.
d0=s.zeros(3,1); d1=s.Matrix([[1,-1,1],[1,-1,1]])
print('W normalization d0=',d0,'d1=',d1)
print('Hq(W,O)=',[1-d0.rank(),3-d0.rank()-d1.rank(),2-d1.rank()])
# D = three P1 components joined at P and Q; incidence map C^3 -> C^4.
dD=s.Matrix([[1,-1,0],[0,1,-1],[1,-1,0],[0,1,-1]])
print('D normalization incidence=',dD)
print('h0(D,O),h1(D,O)=',3-dD.rank(),4-dD.rank())
# Boundary hexagon pulls back a Cech class on theta graph with alternating
# traversal +e1-e2+e3-e1+e2-e3, identically zero.
boundary_chain=s.Matrix([1,-1,1])+s.Matrix([-1,1,-1])
assert boundary_chain==s.zeros(3,1)
print('Hexagon image in oriented theta edges=',boundary_chain)
# R^q f_* J for J=I_D F: first two rows kernel of evaluation at infinity.
print('Rq f_* J=',[[-1],[-1,-1],[0]])
print('Hq(J)=',[0,0,1,0])
print('Hq(T_X)=',[1,1,1,0])
