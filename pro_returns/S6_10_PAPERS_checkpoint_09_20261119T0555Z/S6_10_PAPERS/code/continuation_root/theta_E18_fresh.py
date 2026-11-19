"""Fresh rational q-coefficient and symbolic verification for CDP E18.

No program from an earlier run is imported or used. The q coefficient check
uses integer convolution and the logarithmic-product divisor sum; it is an
exact finite check, not an interval certificate of the infinite identity.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import sympy as s

N=120
def mul(a,b):
    c=[F(0)]*(N+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:N+1-i]):
                if y:c[i+j]+=x*y
    return c
theta3=[F(0)]*(N+1);theta4=theta3.copy()
theta3[0]=theta4[0]=F(1)
for n in range(1,12):
    if n*n<=N:
        theta3[n*n]=F(2);theta4[n*n]=F(2*(-1)**n)
t3_4=mul(mul(theta3,theta3),mul(theta3,theta3))
t4_4=mul(mul(theta4,theta4),mul(theta4,theta4))
elliptic=[-(a+b)/12 for a,b in zip(t3_4,t4_4)]
product=[F(0)]*(N+1);product[0]=F(-1,6)
for n in range(1,N//2+1):
    for k in range(1,N//(2*n)+1):
        product[2*n*k]-=4*n*(-1)**(k-1)
assert elliptic==product
h,muprime,wp,E2,pi=s.symbols('h muprime wp E2 pi', nonzero=True)
hz=-wp-pi**2*E2/3
bprime=(hz+h*h)/(4*pi*pi)+E2/12+s.I*muprime*h/pi
det=s.det(s.Matrix([[1,muprime],[muprime,bprime]]))
target=-(muprime-s.I*h/(2*pi))**2-wp/(4*pi*pi)
assert s.expand(det-target)==0
# The actual wedge boundary in the basis u1,u2; no rank inference from
# a numerical sample is used. A rank-two kappa has invertible coefficient A.
a,b,c,d=s.symbols('a b c d')
A=s.Matrix([[a,b],[c,d]])
W=s.Matrix([[-b,a],[-d,c]])
assert s.expand(W.det()-A.det())==0
result={
 'program':'theta_E18_fresh.py',
 'arithmetic':'fractions.Fraction and exact SymPy polynomial algebra',
 'coefficient_comparison':{'q_orders':N+1,'equal':True,
    'first_nonzero_coefficients':{str(i):str(v) for i,v in enumerate(product) if v and i<=16}},
 'general_determinant_difference':str(s.expand(det-target)),
 'wedge_rank_determinant_difference':str(s.expand(W.det()-A.det())),
 'scope':'Exact finite q-series and polynomial checks. The analytic proof and strict negativity at tau=i are in the written derivation.'}
out=Path(__file__).with_suffix('.output.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
