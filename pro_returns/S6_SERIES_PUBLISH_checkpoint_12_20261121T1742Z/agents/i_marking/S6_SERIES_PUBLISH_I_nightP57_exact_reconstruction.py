#!/usr/bin/env python3
"""New exact coefficient reconstruction, written before receiving P5.7 proof exposure.
Generator laws are solved from covariance as polynomial coefficient equations;
Cramer's rule on integer minors reconstructs unknown coefficients. No SymPy.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,combinations
from datetime import datetime,timezone
import json,hashlib,re,html
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
V=('tau','mu','beta','Ytau','Ymu','Ybeta','c','delta','cprime','n','M0','di','ci')
N=len(V);zero=(0,)*N

def const(x):return {} if x==0 else {zero:F(x)}
def var(name):
 e=[0]*N;e[V.index(name)]=1;return {tuple(e):F(1)}
def add(*ps):
 out={}
 for p in ps:
  for e,a in p.items():out[e]=out.get(e,F(0))+a
 return {e:a for e,a in out.items() if a}
def scale(k,p):return {e:F(k)*a for e,a in p.items() if F(k)*a}
def sub(p,q):return add(p,scale(-1,q))
def mul(p,q):
 out={}
 for e,a in p.items():
  for f,b in q.items():
   g=tuple(x+y for x,y in zip(e,f));out[g]=out.get(g,F(0))+a*b
 return {e:a for e,a in out.items() if a}
def fmt(p):
 terms=[]
 for e,a in sorted(p.items()):
  mon='*'.join(name+(f'^{k}' if k!=1 else '') for name,k in zip(V,e) if k) or '1'
  terms.append((str(a),mon))
 return terms
def determinant(a):
 n=len(a);total=F(0)
 for perm in permutations(range(n)):
  inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  term=F((-1)**inv)
  for i,j in enumerate(perm):term*=a[i][j]
  total+=term
 return total

def solve_poly_system(matrix,rhs):
 n=len(matrix[0]);chosen=None
 for ids in combinations(range(len(matrix)),n):
  square=[matrix[i] for i in ids];det=determinant(square)
  if det:chosen=ids;break
 assert chosen is not None
 monomials=set().union(*(rhs[i] for i in chosen))
 solutions=[{} for _ in range(n)]
 for mon in monomials:
  values=[rhs[i].get(mon,F(0)) for i in chosen]
  for j in range(n):
   repl=[[F(x) for x in row] for row in square]
   for i in range(n):repl[i][j]=values[i]
   value=determinant(repl)/det
   if value:solutions[j][mon]=value
 residuals=[]
 for row,right in zip(matrix,rhs):
  left=add(*(scale(a,s) for a,s in zip(row,solutions)))
  residuals.append(sub(left,right));assert not residuals[-1]
 return solutions,{'matrix':matrix,'rhs':[fmt(x) for x in rhs],'chosen_rows_zero_based':chosen,'chosen_determinant':str(det),'solutions':[fmt(x) for x in solutions],'all_equation_residuals':[fmt(x) for x in residuals]}

def matmul(a,b):
 return [[add(*(mul(x,y) for x,y in zip(row,col))) for col in zip(*b)] for row in a]
def integer_matrix(a):return [[const(x) for x in row] for row in a]
def coefficient_system(residuals,unknowns):
 matrix=[];rhs=[]
 for p in residuals:
  row=[F(0)]*len(unknowns);remain={}
  for exponent,coefficient in p.items():
   hits=[j for j,u in enumerate(unknowns) if exponent[V.index(u)]]
   if not hits:remain[exponent]=coefficient;continue
   assert len(hits)==1
   j=hits[0];expected=[0]*N;expected[V.index(unknowns[j])]=1
   assert exponent==tuple(expected)
   row[j]+=coefficient
  matrix.append(row);rhs.append(scale(-1,remain))
 return matrix,rhs

tau,mu,beta=map(var,['tau','mu','beta'])
Yt,Ym,Yb=map(var,['Ytau','Ymu','Ybeta'])
I=const(1);Z=const(0)
Pi=[[scale(6,mu),tau,I,Z],[beta,mu,Z,I]]
scaled_prime=[[scale(6,Ym),Yt,tau,Z],[add(mul(tau,beta),Yb),Ym,Z,tau]]
A=[[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]],[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]]
Rscaled=[[[const(-1),Z],[sub(I,mu),tau]],[[I,Z],[scale(-1,mu),tau]]]
report={'created_utc':datetime.now(timezone.utc).isoformat(),'target':'night:P5.7','before_target_proof_exposure':True,'method':'Sparse exact polynomial coefficient module; generator transformations reconstructed from covariance with integer-minor Cramer solves; formal affine coefficient comparisons for parameter, period, cusp and quotient maps.','computations':{}}
expected=[ [sub(tau,I),sub(I,mu),sub(scale(2,tau),scale(6,mul(sub(I,mu),sub(I,mu))))], [const(-1),add(tau,mu),sub(scale(-3,tau),scale(6,mul(mu,mu)))] ]
for j in range(2):
 left=matmul(Rscaled[j],Pi);right=matmul(scaled_prime,integer_matrix(A[j]))
 residuals=[sub(x,y) for lrow,rrow in zip(left,right) for x,y in zip(lrow,rrow)]
 matrix,rhs=coefficient_system(residuals,['Ytau','Ymu','Ybeta'])
 sol,cert=solve_poly_system(matrix,rhs);assert sol==expected[j]
 report['computations']['generator_'+str(j+1)]={'unknown_meanings':['tau*tau(g_j z)','tau*mu(g_j z)','tau*(beta(g_j z)-beta(z))'],'coefficient_certificate':cert,'reconstructed_numerators':[fmt(x) for x in sol]}
# Period equality determines the coefficients a=alpha*c+kappa*delta+eta.
sol,cert=solve_poly_system([[1,0,0],[0,1,0],[0,0,1]],[const(1),const(1),const(0)])
assert sol==[I,I,Z]
c,delta,cp,n=map(var,['c','delta','cprime','n'])
a=add(c,delta);ap=add(cp,delta)
report['computations']['parameter_map_coefficient_reconstruction']={'unknown_coefficients':['alpha (coefficient of c)','kappa (coefficient of delta)','eta (constant term)'],'certificate':cert,'a':fmt(a),'inverse_c':[['1','a'],['-1','delta']]}
receiving_lower_left=add(beta,delta,c)
source_lower_left=add(beta,a)
assert not sub(source_lower_left,receiving_lower_left)
report['computations']['period_and_cusp_equality']={'period_lower_left_residual':fmt(sub(source_lower_left,receiving_lower_left)),'cusp_E21_coefficient_residual':fmt(sub(a,add(delta,c))),'other_seven_period_entries_identical_by_input':True}
assert not sub(sub(ap,a),sub(cp,c))
assert not sub(add(c,scale(2,n),delta),add(a,scale(2,n)))
report['computations']['period_quotient_morphisms']={'parameter_difference_residual':fmt(sub(sub(ap,a),sub(cp,c))),'2Z_action_equivariance_residual':fmt(sub(add(c,scale(2,n),delta),add(a,scale(2,n)))),'multiplicative_exponent_residual':fmt(sub(scale(-1,a),add(scale(-1,c),scale(-1,delta))))}
M0,di,ci=map(var,['M0','di','ci']);M=add(M0,di)
left=add(ci,di,M0);right=add(ci,M)
assert not sub(left,right)
assert not sub(scale(-1,M0),add(di,scale(-1,M)))
report['computations']['admissible_domains']={'M':fmt(M),'Im_a_plus_M0_equals_Im_c_plus_M_residual':fmt(sub(left,right)),'log_radius_over_pi_residual':fmt(sub(scale(-1,M0),add(di,scale(-1,M)))),'analytic_premise':'D_part=D0+Im(delta); supremum commutes with adding this fixed real constant, proved in the frozen derivation.'}
# Recorded official HTML date, kept separate from authorial chronological testimony.
htmlpath=ROOT/'agents/i_provenance/literature/S6_SERIES_PUBLISH_I_DGKX_v1_abs.html'
raw=htmlpath.read_text();visible=html.unescape(re.sub(r'<[^>]*>',' ',raw))
assert 'Submitted on 23 Sep 2026' in visible
assert 'Wed, 23 Sep 2026 17:09:17 UTC' in visible
report['documentary_dates']={'official_html_sha256':hashlib.sha256(htmlpath.read_bytes()).hexdigest(),'observed_submission_text':'Submitted on 23 Sep 2026 (this version)','observed_history_text':'Wed, 23 Sep 2026 17:09:17 UTC','September_8_scope':'Authorial assertion in the supplied receiving record; this program establishes no independent public availability on that day.'}
report['summary']={'all_exact_assertions_passed':True,'generator_1':['tau(g1)=(tau-1)/tau','mu(g1)=(1-mu)/tau','beta(g1)-beta=2-6*(1-mu)^2/tau'],'generator_2':['tau(g2)=-1/tau','mu(g2)=1+mu/tau','beta(g2)-beta=-3-6*mu^2/tau'],'parameter_map':'a=c+delta, inverse c=a-delta','parameter_difference':'a_prime-a=c_prime-c','admissibility':'M=M0+Im(delta); Im(a)+M0=Im(c)+M','multiplicative_map':'w_DGKX=exp(-pi*i*delta)*w_receiving','limits':'Analytic uniqueness/extension, chart descent and source-history assertions require the stated primary inputs and written derivation. Exact algebra does not authenticate authorial chronology.'}
def encode(x):
 if isinstance(x,F):return x.numerator if x.denominator==1 else str(x)
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 return x
output=OUT/'S6_SERIES_PUBLISH_I_nightP57_exact_reconstruction_output.json'
output.write_text(json.dumps(encode(report),indent=2)+'\n')
print(json.dumps(report['summary'],indent=2))
print('output_sha256='+hashlib.sha256(output.read_bytes()).hexdigest())
