"""Exact Cayley expansions for a possible analytic critical-point exclusion."""
from pathlib import Path
import json
import sympy as S

v,z=S.symbols('v z')
N=24
a=[S.Rational(0)]*(N+1);b=a.copy();c=a.copy();b[0]=S.Rational(1)
def conv(x,y,n):return sum(x[j]*y[n-j] for j in range(n+1))
for n in range(N):
 a[n+1]=(b[n]-conv(a,a,n))/(3*(n+1))
 b[n+1]=S.Rational(4,3)*(c[n]-conv(a,b,n))/(n+1)
 c[n+1]=2*(conv(b,b,n)-conv(a,c,n))/(n+1)
B=sum(b[2*j]*z**j for j in range(N//2+1))
J=sum(c[2*j+1]*z**j/2 for j in range(N//2))
sq=S.series(S.sqrt(J),z,0,10).removeO()
DD=S.series((B**3-4*z*J**2)/J**S.Rational(3,2),z,0,10).removeO()
H=sum(-DD.coeff(z,n)*z**n/(16*n*n-1) for n in range(10))
V=S.series(sq/B,z,0,10).removeO()
for label,p in [('F4',B),('J',J),('D',DD),('H',H),('V',V),('V(H+4zHprime)',S.series(V*(H+4*z*S.diff(H,z)),z,0,10).removeO())]:
 print(label)
 for n in range(min(10,S.degree(p,z)+1)):print(n,p.coeff(z,n),S.N(p.coeff(z,n),12))
 print()
Path(__file__).resolve().parents[1].joinpath('records/Ccritical_cayley.json').write_text(json.dumps({name:[str(p.coeff(z,n)) for n in range(10)] for name,p in [('F4',B),('J',J),('D',DD),('H',H),('V',V)]},indent=2)+'\n')
