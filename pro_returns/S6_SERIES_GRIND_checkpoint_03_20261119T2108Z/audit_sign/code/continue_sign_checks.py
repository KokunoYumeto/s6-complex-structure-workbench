"""Fresh independent exact certificates for UN.11 and UN.29.
Does not import any code from earlier S6 sessions.
"""
from pathlib import Path
from itertools import product
import json, re, math
import sympy as s
outdir=Path(__file__).resolve().parents[1]
x,z,t=s.symbols('x z t')
# Enumerate all degree-four products of cyclotomic polynomials with determinant one.
indices=[1,2,3,4,5,6,8,10,12]
rows=[]
for exps in product(range(5),range(5),range(3),range(3),range(2),range(3),range(2),range(2),range(2)):
 if sum(int(s.totient(n))*a for n,a in zip(indices,exps))!=4: continue
 P=s.Poly(s.prod(s.cyclotomic_poly(n,x)**a for n,a in zip(indices,exps)),x)
 if P.TC()!=1: continue
 M=math.lcm(*[n for n,a in zip(indices,exps) if a])
 a={}
 for n in s.divisors(M):
  value=sum(s.mobius(n//d)*s.resultant(P.as_expr(),1-x**d,x) for d in s.divisors(n))/n
  assert value.is_Integer
  if value: a[int(n)]=int(value)
 rows.append({'cyclotomic_factors':{str(n):a for n,a in zip(indices,exps) if a},'order':int(M),'stratum_signature':a})
assert len(rows)==19
# Read the printed statement table as input data only, and compare every row.
blocks=json.load(open(outdir/'blocks.json'))
stmt=next(b['statement'] for b in blocks if b['label']=='cdp:st:C.2.UN.11')
printed=[]
for line in stmt.splitlines():
 if not line.startswith('$\\Phi_'): continue
 factors={int(n):int(a or 1) for n,a in re.findall(r'\\Phi_\{(\d+)\}(?:\^\{?(\d+)\}?)?',line.split('&')[0])}
 order=int(line.split('&')[1].strip())
 vals={int(n):int(v) for n,v in re.findall(r'a_\{(\d+)\}=(-?\d+)',line)}
 printed.append((factors,order,vals))
assert len(printed)==19
for fs,order,vals in printed:
 row=next(r for r in rows if {int(k):v for k,v in r['cyclotomic_factors'].items()}==fs)
 assert row['order']==order and row['stratum_signature']==vals,(row,vals)
# General d leading coefficient identity is recorded in the prose proof. Here
# exhaustively test formal coefficient extraction at d=1,...,6, retaining all
# potentially interfering coefficients through the required order.
checks=[]
for d in range(1,7):
 a=s.Function('a')(z); psi=s.Function('psi')(z)
 A=sum(s.Function(f'a{k}')(z)*t**(d+k) for k in range(d+1))
 A=A.subs(s.Function('a0')(z),a)
 phi=z+psi*t**d+sum(s.Function(f'p{k}')(z)*t**(d+k) for k in range(1,d+1))
 # Taylor composition avoids sympy O/derivative ambiguities.
 shift=phi-z
 Acomp=sum(s.diff(A,z,k)*shift**k/s.factorial(k) for k in range(3))
 residual=s.expand(Acomp-A*s.diff(phi,z))
 coeff=s.simplify(residual.coeff(t,2*d))
 expected=s.diff(a,z)*psi-a*s.diff(psi,z)
 assert s.simplify(coeff-expected)==0
 for n in range(d,2*d): assert s.simplify(residual.coeff(t,n))==0
 H=s.Function('H')(z); delta=s.Function('delta0')(z)
 h=H+sum(s.Function(f'h{k}')(z)*t**k for k in range(1,d+1))
 hcomp=sum(s.diff(h,z,k)*shift**k/s.factorial(k) for k in range(d+1))
 residual2=s.expand(hcomp-h-A*s.diff(delta,z))
 coeff2=s.simplify(residual2.coeff(t,d))
 expected2=s.diff(H,z)*psi-a*s.diff(delta,z)
 assert s.simplify(coeff2-expected2)==0
 checks.append({'d':d,'first_identity_at_2d':str(coeff),'second_identity_at_d':str(coeff2),'all_lower_first_coefficients_zero':True})
res={'UN11_complete_19_row_table':rows,'UN11_every_printed_table_row_matches':True,'UN29_formal_return_germs':checks,'scope':'Exact finite computations. Does not certify existence of return germs, monodromy theorem, or all geometric realization claims.'}
(outdir/'continued_sign_checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
