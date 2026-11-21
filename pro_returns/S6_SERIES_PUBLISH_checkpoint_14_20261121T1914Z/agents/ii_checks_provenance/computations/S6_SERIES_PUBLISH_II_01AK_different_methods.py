"""Postrelease independent algorithms for 01AK, compared with its old program.

Normalization: finite free algebra multiplication matrices, not elimination.
Jets: truncated ring evaluation, not symbolic differentiation.
Square membership: direct ideal-square Groebner reduction plus an explicit
saturation certificate, not weighted monomial enumeration.
Conductor: stability of a finite C{x}-lattice under multiplication by t.
"""
import json
from fractions import Fraction
from math import comb
import sympy as s

# Sparse matrices over Z[x], keyed by (row,column,x-exponent).
def madd(A,B):
 C=dict(A)
 for k,v in B.items():C[k]=C.get(k,0)+v
 return {k:v for k,v in C.items() if v}
def mm(A,B):
 C={}
 for (i,j,p),a in A.items():
  for (j2,k,q),b in B.items():
   if j==j2:C[i,k,p+q]=C.get((i,k,p+q),0)+a*b
 return {k:v for k,v in C.items() if v}
def shift(A,p):return {(i,j,q+p):v for (i,j,q),v in A.items()}
Id={(i,i,0):1 for i in range(5)}
Y={(1,0,0):1,(2,1,1):1,(3,2,0):1,(4,3,1):1,(0,4,4):1}
Z={(2,0,0):1,(3,1,0):1,(4,2,0):1,(0,3,4):1,(1,4,3):1}
assert mm(Y,Z)==mm(Z,Y)
assert mm(Y,Y)==shift(Z,1)
assert mm(Y,mm(Z,Z))==shift(Id,4)
assert mm(Z,mm(Z,Z))==shift(Y,3)
def mp(A,n):
 B=Id
 for _ in range(n):B=mm(B,A)
 return B
assert mp(Y,5)==shift(Id,6) and mp(Z,5)==shift(Id,7)
apery=[0,6,7,13,14]
assert [n%5 for n in apery]==list(range(5))
conductor=[]
for r in range(5):
 # Each of the five inequalities is necessary and sufficient for the
 # corresponding basis component to remain in R after multiplication by
 # every C{x}-basis element 1,t,t^2,t^3,t^4 of the normalization.
 k=max(0,max((apery[(r+j)%5]-r-j+4)//5 for j in range(5)))
 conductor.append(r+5*k)
assert conductor==[10,11,12,13,14]

# Sparse Taylor ring Z[t,dx,dy,dz]/(dx,dy,dz)^4, evaluated by multiplication.
zero=(0,0,0,0)
def add(A,B):
 C=dict(A)
 for k,v in B.items():C[k]=C.get(k,0)+v
 return {k:v for k,v in C.items() if v}
def scale(A,n):return {k:n*v for k,v in A.items() if n*v}
def mul(A,B):
 C={}
 for a,c in A.items():
  for b,d in B.items():
   k=tuple(x+y for x,y in zip(a,b))
   if sum(k[1:])<=3:C[k]=C.get(k,0)+c*d
 return {k:v for k,v in C.items() if v}
def power(A,n):
 B={zero:1}
 for _ in range(n):B=mul(B,A)
 return B
XX={(5,0,0,0):1,(0,1,0,0):1}
YY={(6,0,0,0):1,(0,0,1,0):1}
ZZ={(7,0,0,0):1,(0,0,0,1):1}
Fj=add(add(add(scale(power(XX,7),4),scale(mul(mul(power(XX,3),YY),power(ZZ,2)),-15)),
          scale(mul(mul(power(XX,2),power(YY,3)),ZZ),10)),
       add(scale(mul(XX,power(YY,5)),-3),scale(power(ZZ,5),4)))
assert not {k:v for k,v in Fj.items() if sum(k[1:])<=1}
q={k:v for k,v in Fj.items() if sum(k[1:])==2}
assert q=={(25,2,0,0):49,(23,1,0,1):-70,(21,0,0,2):25}
assert {k:v for k,v in Fj.items() if k[1:]==(0,3,0)}=={(17,0,3,0):-20}
gj=[add(power(YY,2),scale(mul(XX,ZZ),-1)),
    add(mul(YY,power(ZZ,2)),scale(power(XX,4),-1)),
    add(power(ZZ,3),scale(mul(power(XX,3),YY),-1))]
linear=[{k:v for k,v in g.items() if sum(k[1:])==1} for g in gj]
expected=[{(7,1,0,0):-1,(6,0,1,0):2,(5,0,0,1):-1},
          {(15,1,0,0):-4,(14,0,1,0):1,(13,0,0,1):2},
          {(16,1,0,0):-3,(15,0,1,0):-1,(14,0,0,1):3}]
assert linear==expected

# Exact differentiation by rational interpolation, followed by a separate
# tensor grid certificate for the global gradient identities. This neither
# calls a symbolic differentiation routine nor expands a symbolic identity.
def valF(x,y,z):return 4*x**7-15*x**3*y*z*z+10*x*x*y**3*z-3*x*y**5+4*z**5
weights=[-sum((Fraction(1,j) for j in range(1,8)),Fraction(0))]
weights += [Fraction((-1)**(j+1)*comb(7,j),j) for j in range(1,8)]
def interpolated_derivative(point,k):
 total=Fraction(0)
 for j,w in enumerate(weights):
  p=list(point);p[k]+=j;total+=w*valF(*p)
 return total
gradient_points=0
for xx in range(8):
 for yy in range(6):
  for zz in range(6):
   aa=yy*yy-xx*zz;bb=yy*zz*zz-xx**4;cc=zz**3-xx**3*yy
   grad=[interpolated_derivative((xx,yy,zz),k) for k in range(3)]
   assert grad==[-28*xx*xx*bb+14*xx*yy*zz*aa-3*yy*aa*aa,
                 -15*xx*aa*aa,20*zz*cc+10*xx*xx*yy*aa]
   assert 5*xx*grad[0]+6*yy*grad[1]+7*zz*grad[2]==35*valF(xx,yy,zz)
   gradient_points+=1

# Recover the conormal rows from the directly evaluated first jets, and
# compute their exterior products with sparse Laurent-polynomial arithmetic.
def p_add(A,B):
 C=dict(A)
 for k,v in B.items():C[k]=C.get(k,0)+v
 return {k:v for k,v in C.items() if v}
def p_mul(A,B):
 C={}
 for p,a in A.items():
  for q,b in B.items():C[p+q]=C.get(p+q,0)+a*b
 return {k:v for k,v in C.items() if v}
def p_scale(A,n,shift=0):return {k+shift:n*v for k,v in A.items() if n*v}
def jet_row(g):
 row=[]
 for i in range(3):
  e=tuple(1 if j==i else 0 for j in range(3))
  row.append({k[0]:v for k,v in g.items() if k[1:]==e})
 return row
ja,jg2,jg3=[jet_row(g) for g in linear]
jb=[p_add(b,p_scale(a,2,8)) for a,b in zip(ja,jg2)]
assert jg3==[p_add(p_scale(a,-3,9),p_scale(b,1,1)) for a,b in zip(ja,jb)]
exterior=[p_add(p_mul(ja[i],jb[j]),p_scale(p_mul(ja[j],jb[i]),-1))
          for i,j in ((0,1),(0,2),(1,2))]
assert exterior==[{21:7},{20:-6},{19:5}]
assert exterior==[p_scale(q,1,15) for q in ({6:7},{5:-6},{4:5})]
assert min(min(q) for q in exterior)==19
ellrow=[p_add(p_scale(a,5,8),p_scale(b,-2)) for a,b in zip(ja,jb)]
ambient_q={}
for i in range(3):
 for j in range(i,3):
  for degree,value in p_scale(p_mul(ellrow[i],ellrow[j]),1 if i==j else 2,-5).items():
   ex=[0,0,0];ex[i]+=1;ex[j]+=1;ambient_q[(degree,*ex)]=value
assert ambient_q==q
assert p_scale(ja[1],1,-6)=={0:2}
assert p_scale(jb[1],1,-6)=={8:5}
normalized_cubic=p_scale({17:-20},1,-18)
assert normalized_cubic=={-1:-20}
quadratic_basis_coefficients=[{11:25},{3:-20},{-5:4}]
q_pole=-min(min(c) for c in quadratic_basis_coefficients)
k_pole=-min(normalized_cubic)
assert (q_pole,k_pole,3*q_pole+2*k_pole)==(5,1,17)

# This algorithm acts on the full polynomial ideal I^2.  It does not form
# the weight-35 coefficient space used by the old computation.
x,y,z=s.symbols('x y z')
a=y*y-x*z;b=y*z*z-x**4;c=z**3-x**3*y
F=4*x**7-15*x**3*y*z*z+10*x*x*y**3*z-3*x*y**5+4*z**5
G=s.groebner([a*a,a*b,a*c,b*b,b*c,c*c],x,y,z,order='grevlex')
remainder=G.reduce(F)[1]
assert remainder!=0 and G.reduce(x*F)[1]==0
certificate=4*b*b-4*z*a*c-3*x*x*y*a*a
assert s.Poly(x*F-certificate,x,y,z).is_zero
print(json.dumps({'all_assertions_passed':True,
 'normalization_method':'five-dimensional free C{x}-algebra with exact Y,Z multiplication matrices; residue classes prove faithful parametrization',
 'normalization_matrix_relations':['Y^2=xZ','YZ^2=x^4','Z^3=x^3Y','Y^5=x^6','Z^5=x^7'],
 'conductor_lattice_thresholds':conductor,
 'jet_method':'evaluate F in a truncated multivariable polynomial ring by sparse integer convolution; no differentiation engine',
 'quadratic_jet':{str(k):v for k,v in q.items()},'radical_cubic_coefficient':'-20*t^17',
 'global_gradient_method':'derivatives recovered from eight rational interpolation values; identities certified on an 8 x 6 x 6 exact grid with the respective polynomial degree bounds',
 'gradient_certificate_points':gradient_points,
 'conormal_exterior_method':'sparse Laurent-polynomial exterior products of rows obtained from first jets',
 'conormal_exterior':exterior,
 'normalized_cubic_from_jet_and_radical_frame':normalized_cubic,
 'quadratic_cubic_combined_poles':[q_pole,k_pole,3*q_pole+2*k_pole],
 'square_method':'grevlex Groebner reduction of all six generators of I^2',
 'F_remainder':str(s.factor(remainder)),'xF_remainder':0,
 'symbolic_membership_certificate':'xF=4b^2-4zac-3x^2ya^2',
 'analytic_bridge':'I^2 is positively weighted homogeneous. An analytic membership identity would give a polynomial weight-35 membership identity, contradicting the nonzero exact Groebner remainder.',
 'timing_scope':'Written and executed after target release and inspection of the old target-specific program; adds no prereading derivation claim.'},indent=2))
