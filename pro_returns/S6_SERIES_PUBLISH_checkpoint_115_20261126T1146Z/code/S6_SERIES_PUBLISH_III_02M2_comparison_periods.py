"""Post-release check of M2's printed Neron-Severi calculation.

The fresh form/divisor/field/cohomology derivation was fixed before
2026-11-23T19:40:21Z. This additional calculation receives no pre-proof
or independent-event credit.
"""
from itertools import combinations
import sympy as S

mu,tau,beta=S.symbols('mu tau beta')
A,B,C,D,E,F=S.symbols('A B C D E F')
pairs=list(combinations(range(4),2))
sigma1=S.Matrix([6*mu,tau,1,0])
sigma2=S.Matrix([beta,mu,0,1])
two=[sigma1[i]*sigma2[j]-sigma1[j]*sigma2[i] for i,j in pairs]
coeff=[A,B,C,D,E,F]
def sign(order):
    return (-1)**sum(order[i]>order[j]
                     for i in range(4) for j in range(i+1,4))
value=0
for i,p in enumerate(pairs):
    for j,q in enumerate(pairs):
        if len(set(p+q))==4:value+=sign(p+q)*coeff[i]*two[j]
expected=A-B*tau+(6*D-C)*mu+E*beta+F*(6*mu**2-tau*beta)
assert S.expand(value-expected)==0
print('Type-(1,1) coefficient:',S.expand(value))
assert S.expand(value.subs(beta,beta+1)-value)==E-F*tau
print('New-zero monodromy difference: E-F*tau')
reduced=S.expand(value.subs({E:0,F:0}))
assert S.expand(reduced.subs(tau,tau-1)-reduced)==B
print('Cusp monodromy difference after E=F=0: B')
assert S.expand(reduced.subs(B,0)-A-(6*D-C)*mu)==0
print('Remaining relation: A+(6D-C)*mu')
assert S.expand(value.subs({A:0,B:0,C:6*D,E:0,F:0}))==0
Q=S.zeros(4)
Q[1,2]=1;Q[2,1]=-1
Q[0,3]=6;Q[3,0]=-6
assert Q.det()==36
print('Integral solution lattice: Z*(0,0,6,1,0,0)')
print('Invariant alternating form determinant:',Q.det())
print('ALL POST-RELEASE PERIOD IDENTITIES PASSED')
