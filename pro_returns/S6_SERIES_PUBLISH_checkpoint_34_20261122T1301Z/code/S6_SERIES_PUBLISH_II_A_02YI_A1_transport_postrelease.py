"""Postrelease exact coordinate and oriented-cycle transport to WN's n=1 fibre.
The prerelease YI derivation and program are unchanged.
"""
from fractions import Fraction as F
from itertools import product, permutations
import json

def z(a,b=0):return (F(a),F(b))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def total(values):
 out=z(0)
 for value in values:out=add(out,value)
 return out

def phi(v):
 a,b,c=v
 return (a,add(b,mul(z(0,1),c)),add(neg(b),mul(z(0,1),c)))
def inverse(v):
 x,y,w=v
 return (x,mul(z(F(1,2)),sub(y,w)),mul(z(0,F(-1,2)),add(y,w)))
count=0
for values in product((-1,0,1),repeat=3):
 v=tuple(z(a) for a in values);x,y,w=phi(v)
 assert sub(mul(x,x),mul(w,y))==total(mul(a,a) for a in v)
 assert inverse(phi(v))==v
 assert phi(inverse(v))==v
 count+=1
assert count==27
# The polynomial identity has separate degree <=2 in each complex variable;
# both linear inverse identities have degree <=1.  The full 3^3 grid proves
# all identities over Q(i) by separate-variable interpolation.
M=((z(1),z(0),z(0)),(z(0),z(1),z(0,1)),(z(0),z(-1),z(0,1)))
det=z(0)
for p in permutations(range(3)):
 term=z((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)))
 for i in range(3):term=mul(term,M[i][p[i]])
 det=add(det,term)
assert det==z(0,2)

def determinant_real(A):
 result=F(0)
 for p in permutations(range(len(A))):
  term=F((-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p))))
  for i,j in enumerate(p):term*=A[i][j]
  result+=term
 return result
# Ambient complex chart (y,z), real coordinate order (Re y,Im y,Re z,Im z).
# At the north pole the outward sphere basis is (d/dz2,d/dz3).
# Its graph is z=-conjugate(y); the affine E_+ curve is y=0.
north=((1,0,0,0),(0,1,0,0),(-1,0,1,0),(0,1,0,1))
# At the south pole outward orientation reverses the first sphere vector.
south=tuple(tuple(-a if j==0 else a for j,a in enumerate(row)) for row in north)
np=determinant_real(north);sp=determinant_real(south)
assert (np,sp)==(1,-1)
print(json.dumps({'timing':'postrelease supplement; no extra independent credit','map_normalized_coordinates':'x=z1, y=z2+i*z3, z=-z2+i*z3','inverse':'z1=x, z2=(y-z)/2, z3=(y+z)/(2*i)','general_epsilon':'First divide all z_j by one chosen sqrt(epsilon); the equation q=epsilon then becomes x^2-z*y=1.','coefficient_field':'Q(i), represented by exact rational pairs','separate_degree_bounds':[2,2,2],'full_grid_points':count,'all_coordinate_and_inverse_residuals_zero':True,'complex_linear_determinant':[str(det[0]),str(det[1])],'real_orientation_preserved':'The real determinant of an invertible complex linear map is |det_C|^2>0.','north_intersection_with_affine_E_plus':int(np),'south_intersection_with_affine_E_minus':int(sp),'cycle_map_proved_in_comparison':'The outward real sphere maps to E_- minus E_+, the negative of the prior program vector (0,0,1,-1). Both have square -2.','limits':'The old compactification identifies its exceptional basis and primitive kernel; the coordinate identities and local intersection signs here supply their exact transport to the prerelease normal-bundle computation.'},indent=2))
