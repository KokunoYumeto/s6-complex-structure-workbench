"""Independent exact verification of the displayed weighted OS45 cochains.

Inputs are formulas D.OL1--D.OL12 and the positive six-ray fan, typed from
the paper; no earlier program, certificate array or output is imported.
This verifies algebra and localization sums, not the missing framed cycle.
"""
from pathlib import Path
import json
import sympy as S
ROOT=Path(__file__).resolve().parents[1]
checks=0

def verify(value,message):
 global checks
 checks+=1
 assert value,message

def support(r,s):return 4*(r//8)+3*(r%8)*(s//2)
rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def plus(v,w):return (v[0]+w[0],v[1]+w[1])
def wall(v,j):
 return support(*v)+support(*plus(v,rays[j]))-support(*plus(v,rays[j-1]))-support(*plus(v,rays[(j+1)%6]))
# Prove every integer quasiperiod by symbolic quotient/remainder, retaining
# independent residue representatives rather than a finite coordinate window.
a,b=S.symbols('a b',integer=True)
def symbolic_support(r,s):
 rr=S.expand(r).coeff(a);ss=S.expand(s).coeff(b)
 # Only the whole-period coefficients 8a and 2b occur in these calls.
 r0=S.expand(r-8*a);s0=S.expand(s-2*b)
 verify(rr==8 and ss==2,'symbolic quotient coordinates')
 return 4*(a+int(r0)//8)+3*(int(r0)%8)*(b+int(s0)//2)
periods=[((8,-6),lambda r:4-r),((24,-16),lambda r:4)]
for r0 in range(8):
 for s0 in range(2):
  r=8*a+r0;s=2*b+s0;original=symbolic_support(r,s)
  for (dr,ds),expected in periods:
   diff=S.Poly(S.expand(symbolic_support(r+dr,s+ds)-original-expected(r)),a,b)
   verify(all(int(c)%8==0 for c in diff.coeffs()),'all-integer affine quasiperiod')
rows=[]
for r in range(8):
 for s in range(2):
  d=[wall((r,s),j) for j in range(6)]
  eta=[d[0]+d[1]+d[2],-d[0],-d[2],-d[4]]
  square=eta[0]**2-sum(x*x for x in eta[1:])
  i=2*r+s
  verify(square%16==(7 if i<14 else 15),'component Pontryagin square')
  mixed=(-1)**s*(eta[0]+eta[1])
  verify(mixed%8==(4 if r in [0,7] else 0),'primitive y mixed coordinate')
  vertical=support(r,s)+support(r,s+1)-support(r+1,s)-support(r-1,s+1)
  residue=vertical%8;lam=0 if s==0 else 3*r;mu=0 if s==0 else -1
  verify(residue==((4 if s==0 else 7) if r in [0,7] else (0 if s==0 else 3)),'fixed-curve degree')
  rows.append(dict(component=i,r=r,s=s,walls=d,eta=eta,square_mod16=square%16,mixed_y_mod8=mixed%8,d=residue,lam=lam,mu=mu))
sums={'sum_d':sum(x['d'] for x in rows),'sum_d_lambda':sum(x['d']*x['lam'] for x in rows),'sum_d_lambda2':sum(x['d']*x['lam']**2 for x in rows),'sum_upper_d':sum(x['d'] for x in rows if x['s']==1)}
verify(sums=={'sum_d':40,'sum_d_lambda':336,'sum_d_lambda2':5544,'sum_upper_d':32},'exact localization sums')
L,V=S.symbols('L V',integer=True);poly_receipts=[]
for sign in [-1,1]:
 expressions=[-3*sum(x['d']*(L+sign*x['lam'])**2 for x in rows),-2*sum(x['d']*(L+sign*x['lam'])*(V+x['mu']) for x in rows),-sum(x['d']*(V+x['mu'])**2 for x in rows)]
 for expr,modulus in zip(expressions,[8,16,8]):
  poly=S.Poly(S.expand(expr),L,V);verify(all(int(c)%modulus==0 for c in poly.coeffs()),'all-linearizations localization divisibility')
  poly_receipts.append({'sign':sign,'modulus':modulus,'polynomial':str(poly.as_expr()),'coefficients':[int(c) for c in poly.coeffs()]})
verify(S.binomial(17,3)==680,'free cubic coordinate count')
verify(S.binomial(16,2)==120,'free quadratic times torsion coordinate count')
# Exact transport between the common root-curve line divisors.
verify(S.Matrix([12,-3])==3*S.Matrix([4,-1]),'q5*L=T^3')
verify(5*S.Matrix([4,-1])-S.Matrix([5,-1])==S.Matrix([15,-4]),'q3*L to T^5 divisor of t/(t-1)')
# Realification of the given integrable tangent bundle and Yang's n=4 test.
c2square=3-1;c4=6;p1square=4*c2square;p2=c2square+2*c4
verify((p1square,p2)==(8,14),'Pontryagin-Chern transport')
verify(4*p2-p1square==8*(4+2),'Yang n=4 unstable compatibility')
verify((p2-c2square)%4==0 and p2-c2square==2*c4,'Mandal characteristic congruence and Euler equation')
output={'status':'PASS','assertions':checks,'inputs':'Printed D.OL1--12 and the marked fan; no old code or arrays','component_rows':rows,'exact_sums':sums,'all_linearization_polynomials':poly_receipts,'remaining_gate':'No evaluation of the embedded odd torsion 3-cycle or its reference frame; refined coordinate remains 0 versus 4 in Z/8.'}
out=ROOT/'code/outputs/III_weighted_OS45_checks.json';out.write_text(json.dumps(output,indent=2));print(json.dumps({k:v for k,v in output.items() if k not in ['component_rows','all_linearization_polynomials']}))
