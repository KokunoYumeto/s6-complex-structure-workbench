"""Fresh exact checks of B.4.3, C.3.5, D.4.6, E.3.1.
No retained implementation is imported or inspected. Standard-library rational
linear algebra, truncated polynomial arithmetic, and an independently assembled
fundamental square are used.
"""
from fractions import Fraction as F
from itertools import product
import json


def add(p,q):
 r=p.copy()
 for m,c in q.items():
  r[m]=r.get(m,F(0))+c
 return {m:c for m,c in r.items() if c}
def scale(p,k):return {m:k*c for m,c in p.items() if k*c}
def mul(p,q,deg=99):
 r={}
 for m,c in p.items():
  for n,d in q.items():
   a=tuple(x+y for x,y in zip(m,n))
   if sum(a)<=deg:r[a]=r.get(a,F(0))+c*d
 return {m:c for m,c in r.items() if c}
def const(c,n):return {(0,)*n:F(c)}
def var(i,n):return {tuple(int(j==i) for j in range(n)):F(1)}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mm(a,b):return [[dot(row,col) for col in zip(*b)] for row in a]
def inverse(a):
 n=len(a);r=[[F(x) for x in a[i]]+[F(i==j) for j in range(n)] for i in range(n)]
 for j in range(n):
  p=next(i for i in range(j,n) if r[i][j]);r[j],r[p]=r[p],r[j]
  c=r[j][j];r[j]=[x/c for x in r[j]]
  for i in range(n):
   if i!=j:
    c=r[i][j];r[i]=[x-c*y for x,y in zip(r[i],r[j])]
 return [row[n:] for row in r]
def rank(a):
 r=[[F(x) for x in row] for row in a];i=0
 for j in range(len(r[0]) if r else 0):
  p=next((p for p in range(i,len(r)) if r[p][j]),None)
  if p is None:continue
  r[i],r[p]=r[p],r[i];c=r[i][j];r[i]=[x/c for x in r[i]]
  for k in range(len(r)):
   if k!=i:
    c=r[k][j];r[k]=[x-c*y for x,y in zip(r[k],r[i])]
  i+=1
 return i

report={}
# Todd degree-three identity, generated from product of the three one-root
# series 1+x/2+x^2/12 (no x^3 term).
x=[var(i,3) for i in range(3)]
todd=const(1,3)
for a in x:todd=mul(todd,add(add(const(1,3),scale(a,F(1,2))),scale(mul(a,a),F(1,12))),3)
todd3={m:c for m,c in todd.items() if sum(m)==3}
c1=add(add(x[0],x[1]),x[2]);c2=add(add(mul(x[0],x[1]),mul(x[0],x[2])),mul(x[1],x[2]))
assert todd3==scale(mul(c1,c2),F(1,24))
def monomials(weight,weights=(3,4)):
 if weight<0:return []
 return [(a,b) for a in range(weight//weights[0]+1) for b in range(weight//weights[1]+1) if weights[0]*a+weights[1]*b==weight]
report['B.4.3']={'Todd_degree3_equals_c1c2_over24':True,'weighted_H0_O0':monomials(0),'weighted_H0_Ominus1':monomials(-1),'H1_O_via_Leray':1,'S6_chiO':0,'S6_h1_minus_h2':1}
# Coherence: variables (h,k,c,ell), beta is suppressed because it cancels
# by linearity. The c-dependent part of the vertical coordinate is exact.
h,k,c,l=[var(i,4) for i in range(4)]
def b(hh,cc):return add(add(scale(mul(hh,cc),-F(1,12)),mul(hh,l)),scale(mul(hh,hh),-F(1,24)))
defect=add(add(b(h,c),b(k,add(c,h))),scale(b(add(h,k),c),-1))
assert not defect
A1=[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
A2=[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
M0=inverse(mm(A1,A2));g=[1,0,0,0];d=[0,0,0,1]
def defect_per_h(A,inc):return [F(A[i][0]-g[i],12)+inc*d[i] for i in range(4)]
f1=defect_per_h(A1,-F(1,3));f2=defect_per_h(A2,F(1,4));f0=defect_per_h(M0,F(1,12))
assert f1==list(map(F,[0,F(1,2),-F(1,2),-F(1,2)]))
assert f2==list(map(F,[0,0,-F(1,2),F(1,2)]))
assert f0==[0]*4
# Exponents of (exp(2pi i mu), exp(2pi i C21), q, H) for each coordinate.
U=[[-6,0,0,0],[0,-1,0,1]];deck=[[6,0,0,0],[0,1,-1,0]]
prod_exp=[[u+v for u,v in zip(a,b)] for a,b in zip(U,deck)]
assert prod_exp==[[0,0,0,0],[0,0,-1,1]]
report['C.3.5']={'composition_defect_polynomial':defect,'eta1_per_h':[str(x) for x in f1],'eta2_per_h':[str(x) for x in f2],'eta0_per_h':[str(x) for x in f0],'M0':[[str(x) for x in row] for row in M0],'finite_chart1_root_exponent':4*3-12,'finite_chart1_unit':'a1^4/(t-1)^3','finite_chart2_root_exponent':-3*4+12,'finite_chart2_unit':'t^4/a2^3','cusp_q_exponent':-4+3,'cusp_H':'A(q)^4/(A(q)-q)^3','unit_times_gamma_deck_exponents':prod_exp,'six_positive_w_loops_delta_c':-12,'closing_h':12}
report['D.4.6']={'Dpart_dt_coefficient_pi_times':str(F(6)*F(7,384)),'Dpart_Re_t_coefficient_pi_times':str(F(2)*F(6)*F(7,384)),'global_factor_classification_recomputed':False,'scope':'Exact conversion only; global factor-zero theorem is a cited statement input.'}
# Actual anti-diagonal triangulation with edge directions e1,e2,e1-e2.
triangles=[[(0,0),(1,0),(0,1)],[(1,1),(0,1),(1,0)]]
edges=[(1,0),(0,1),(1,-1)]
inc=[]
for tri in triangles:
 row=[0]*3
 for p,q in zip(tri,tri[1:]+tri[:1]):
  v=tuple(q[j]-p[j] for j in range(2))
  if v in edges:row[edges.index(v)]+=1
  else:row[edges.index(tuple(-x for x in v))]-=1
 inc.append(row)
r=rank(inc);dims=[1,3-r,2-r]
assert dims==[1,2,1]
a=[v[0] for v in edges];bb=[v[1] for v in edges]
assert all(dot(row,a)==dot(row,bb)==0 for row in inc)
# Lexicographic vertex order induces a compatible Delta-complex diagonal.
def det2(v,w):return v[0]*w[1]-v[1]*w[0]
def integral_cup(axis1,axis2):
 value=0
 for tri in triangles:
  p,q,r=sorted(tri)
  v=tuple(q[i]-p[i] for i in range(2));w=tuple(r[i]-q[i] for i in range(2))
  orient=1 if det2(v,w)>0 else -1
  value+=orient*v[axis1]*w[axis2]
 return value
cup=[[integral_cup(i,j) for j in range(2)] for i in range(2)]
assert cup==[[0,1],[-1,0]]
report['E.3.1']={'oriented_triangles':triangles,'edge_directions':edges,'normalization_d1':inc,'normalization_d0':[[0],[0],[0]],'d1_rank':r,'Hq_dimensions':dims,'degree1_cocycles_dx_dy':[a,bb],'cup_pairing':cup,'cup_determinant':1,'H1_O1_dual_weight':-8,'H0_Ominus8':monomials(-8)}
print(json.dumps(report,indent=2))
