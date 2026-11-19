#!/usr/bin/env python3
"""Fresh chi_y calculation by exponential-series division and root pairing."""
from pathlib import Path
import json
import sympy as s
y,z,u,v=s.symbols('y z u v')
q=[]
# Divide numerator and denominator by their common leading formal t.
den=[(-1)**n*z**(n+1)/s.factorial(n+1) for n in range(5)]
num=[z*(1+y)]+[y*z*(-z)**n/s.factorial(n) for n in range(1,5)]
for n in range(5):
 q.append(s.expand((num[n]-sum(den[j]*q[n-j] for j in range(1,n+1)))/den[0]))
assert all(s.expand(sum(den[j]*q[n-j] for j in range(n+1))-num[n])==0 for n in range(5))
prod=[s.Integer(1)]+[s.Integer(0)]*4
for root in (u,-u,v,-v):
 terms=[c.subs(z,root) for c in q]
 prod=[s.expand(sum(prod[j]*terms[n-j] for j in range(n+1))) for n in range(5)]
degree4=s.Poly(prod[4],u,v)
A=s.expand(degree4.coeff_monomial(u**4))
B=s.expand(degree4.coeff_monomial(u**2*v**2)-2*A)
reconstruction=s.expand(A*(u*u+v*v)**2+B*u*u*v*v)
assert s.expand(prod[4]-reconstruction)==0
assert s.expand(A-(1+y)**4/240)==0
assert s.expand(B-(-1-124*y+474*y*y-124*y**3-y**4)/720)==0
actual=s.expand(2*A+6*B)
assert actual == -y+4*y*y-y**3
# Euler and Todd specializations are independent consistency checks.
assert s.expand(actual.subs(y,-1)-6)==0
assert s.expand(actual.subs(y,0))==0
result={'all_passed':True,'method':'Formal exponential quotient division; product at paired roots; exact reconstruction in c2^2,c4.',
 'quotient_coefficients_by_t_degree':[str(x) for x in q],
 'coefficient_c2_squared':str(A),'coefficient_c4':str(B),'chi_y_actual':str(actual),
 'chi_p':[str(actual.coeff(y,k)) for k in range(5)],'checks':11,
 'scope':'Only the RR Chern-root step; no Hodge table or prior geometric input reproof claimed.'}
root=Path(__file__).resolve().parents[2]
out=root/'analysis/continuation_V_ledger/P1A2_RR_fresh.output.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
