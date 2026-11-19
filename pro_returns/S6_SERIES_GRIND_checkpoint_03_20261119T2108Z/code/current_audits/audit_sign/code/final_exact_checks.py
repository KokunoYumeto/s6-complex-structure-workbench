"""Fresh exact checks written from the formulas, without importing attached S6 code.
These certify the stated algebraic identities, not their geometric hypotheses.
"""
from pathlib import Path
from itertools import product
from math import gcd,lcm
import json
import sympy as s
D=Path(__file__).resolve().parents[1]
out={}
# UN50 and UN63: the literal ordered exponent maps.
r,k,n,l=s.symbols('r k n l',integer=True)
A=s.Matrix([[-l,r],[k,-n]]);B=s.Matrix([[n,r],[k,l]])
assert A*B==(r*k-n*l)*s.eye(2)
assert A.det()==n*l-r*k
out['UN50_UN63_ordered_exponent_map']={'matrix':str(A),'determinant':str(A.det()),'inverse_product':str(A*B),'under_rk_minus_nl_equals_one':'determinant -1 and inverse product I2'}
# UN35: all finite elliptic integral lattice actions, including the actual order6 restrictions.
M={1:s.eye(2),2:-s.eye(2),3:s.Matrix([[0,-1],[1,-1]]),4:s.Matrix([[0,-1],[1,0]]),6:s.Matrix([[0,-1],[1,1]])}
for d,T in M.items():
 assert T**d==s.eye(2)
 assert all(T**j!=s.eye(2) for j in range(1,d))
P=s.Matrix([[1,-1],[0,1]])
assert P.inv()*M[6]**2*P==M[3] and M[6]**3==-s.eye(2)
out['UN35_finite_lattice_actions']={str(d):{'matrix':str(T),'exact_order':d,'determinant':int(T.det())} for d,T in M.items()}
out['UN35_order6_restriction_conjugacy']=True
# UN25 and UN79: exact Weierstrass discriminants and squarefreeness.
T=s.symbols('T')
polys={25:(T**4-3,T**6+T+2),79:(T**4+1,T**6)}
out['Weierstrass_discriminants']={}
for row,(a,b) in polys.items():
 disc=s.expand(4*a**3+27*b**2);g=s.gcd(disc,s.diff(disc,T));assert g==1
 out['Weierstrass_discriminants'][str(row)]={'polynomial':str(disc),'gcd_with_derivative':str(g),'degree':s.degree(disc,T),'leading_coefficient':int(s.Poly(disc,T).LC())}
assert s.diff(4*polys[25][0]**3+27*polys[25][1]**2,T).subs(T,0)==108
# UN8: every displayed small-resolution chart and the Picard intersection matrix.
u,v,a,b,rr,ss,hh,j,alpha,beta=s.symbols('u v a b r s h j alpha beta')
f=u*v-a*b*(alpha*a+beta*b)
charts=[{a:u*rr,v:rr*b*(alpha*u*rr+beta*b)}, {b:ss*hh,u:a*ss,v:hh*(alpha*a+beta*ss*hh)}, {a:(j*v-beta*b)/alpha,u:(j*v-beta*b)*b*j/alpha}]
for c in charts:assert s.simplify(f.subs(c,simultaneous=True))==0
G=s.Matrix([[0,1,1,1],[1,0,1,1],[1,1,0,3],[1,1,3,0]])
assert G.det()==-3
out['UN8_small_resolution_charts']={'all_three_chart_equations_zero':True,'intersection_determinant':int(G.det()),'intersection_rank':G.rank()}
# UN24: quotient fixed-point counts and full root-configurations.
fix={d:int(s.simplify((2-2*s.cos(2*s.pi/d))**2)) for d in [2,3,4,6]}
assert fix=={2:16,3:9,4:4,6:1}
configs={2:{1:fix[2]},3:{2:fix[3]},4:{3:fix[4],1:(fix[2]-fix[4])//2},6:{5:fix[6],2:(fix[3]-fix[6])//2,1:(fix[2]-fix[6])//3}}
out['UN24_K3_quotient_configurations']={'fixed_points':fix,'A_rank_multiplicities':configs}
# UN73/76: determinant identity for the entire punctured period family.
x,w,y,aa,s11,s12,s22=s.symbols('x w y a S11 S12 S22',real=True)
J=s.Matrix([[0,1],[-1,0]]);S=s.Matrix([[s11,s12],[s12,s22]]);Ap=S+aa*J;I=s.eye(2)
block=(I+x*J).row_join(w*J*(Ap-y*I)).col_join((w*J).row_join((I-x*J)*Ap+y*(I+x*J)))
r2=x*x+w*w
expected=(1+r2)**2*S.det()+(1-r2)*(1+r2)*y*s.trace(S)+y*y*(1-r2)**2+((1+r2)*aa+2*x*y)**2
assert s.expand(block.det()-expected)==0
out['UN73_UN76_period_determinant_identity']={'symbolic_difference':0,'variables':'arbitrary real x,w,y,a,S11,S12,S22','positivity_reason':'S positive definite and (1-r^2)y >= 0; first term strictly positive and every remaining term nonnegative'}
# UN52/56/59/63/78: exact compressed exponent and lattice-volume arithmetic,
# exhaustive finite corroboration in addition to the all-integer proof.
cases=0
for m in product(range(1,13),repeat=3):
 N=lcm(*m);g=gcd(gcd(m[0],m[1]),m[2]);nu=s.Rational(N*N*g,m[0]*m[1]*m[2]);assert nu.is_Integer and nu>0
 for a,b in [(m[0],m[1]),(m[1],m[2])]:
  gg=gcd(a,b);A0=a//gg;B0=b//gg;h=N//lcm(a,b)
  assert a*B0==b*A0==gg*A0*B0
  assert h*gg*A0*B0==N
  assert gcd(N//a,N//b)==h
  assert lcm(N//a,N//b)==N//gg
 cases+=1
out['weighted_root_finite_checks']={'multiplicity_triples':cases,'range':'1..12 in each coordinate','all_compressed_neck_and_inertia_formulas_match':True,'all_simplex_volumes_positive_integral':True}
# UN79 balancing curve: exact branch data and two independent Euler counts.
z=s.symbols('z');pp=z*z+1;qq=3*z*z+z+5;factors=[pp,qq,qq-pp,qq-2*pp]
discs=[int(s.discriminant(f,z)) for f in factors]
assert discs==[-4,-59,-31,-11]
for i in range(4):
 for j in range(i):assert s.gcd(factors[i],factors[j])==1
out['UN79_balance']={'four_branch_discriminants':discs,'all_pairwise_gcds':1,'branch_count':8,'genus':3,'blowup_Euler':0+2+2-4,'stratum_Euler':sum([0,4,4,6,6,-8])-24+12}
# UN52 triangle involution and UN59 examples: actual map compatibility.
z0,w0,t0=s.symbols('z w t',nonzero=True)
edges=[(1/w0,t0/(z0*w0)),(w0,t0*w0/z0),(1/w0,t0*w0/z0)]
signs=[(1,1),(1,-1),(-1,1)]
for i,e in enumerate(edges):
 left=[s.simplify(c.subs({z0:signs[i][0]*z0,w0:signs[i][1]*w0,t0:-t0},simultaneous=True)) for c in e]
 right=[signs[(i+1)%3][j]*e[j] for j in range(2)]
 assert all(s.simplify(a-b)==0 for a,b in zip(left,right))
examples={}
for N in [2,3,4,6]:
 L=2*N;first=[];orders=[]
 for j in range(L):
  first.append(s.Rational((j+1)%L,N)-s.Rational(j,N)-s.Rational(1,N))
  orders.append(sum(s.Rational((j+2*a)%L,N) for a in range(N)))
 assert all(v==0 for v in first[:-1]) and first[-1]==-2
 assert all(v==(N-1 if j%2==0 else N) for j,v in enumerate(orders))
 examples[str(N)]={'edge_residuals':list(map(str,first)),'N_fold_translation':list(map(str,orders))}
out['UN52_triangle_equivariance']=True
out['UN59_finite_action_examples']=examples
out['scope']='Exact polynomial, lattice, determinant and finite-range arithmetic only. Geometric existence, analytic convergence and topology are assessed in the separate full proof-comparison events.'
(D/'final_exact_checks.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps(out,indent=2,default=int))
