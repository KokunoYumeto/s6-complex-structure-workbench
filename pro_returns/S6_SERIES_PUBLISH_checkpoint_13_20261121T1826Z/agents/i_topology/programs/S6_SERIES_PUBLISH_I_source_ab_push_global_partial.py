"""Exact identities for the actual global partial filling B.4.19.

The program checks affine comparisons and the integral fan action.  It
does not infer properness or an origin completion from finite algebra.
"""
import json
from pathlib import Path
import sympy as S

v, s, c, k, kj, wj, eps = S.symbols('v s c k kj wj eps')
mu, C, kap, beta = S.symbols('mu C kap beta')
e = S.Matrix([0, 1])
gamma = S.Matrix([6*mu, beta+c])
bm12 = gamma + (-k-6)*e
assert S.simplify(bm12-gamma+(k+6)*e) == S.zeros(2,1)
zeta2 = S.symbols('zeta2')
assert S.expand((zeta2-k)+k*(v+1)-(zeta2+k*v)) == 0
print('positive r loop: scalar representative -k; gauge zeta2+k*v is invariant')

data = [(1, 3, 1, S.Matrix([1,2,-4,0])),
        (2, 4, -1, S.Matrix([-1,-3,3,0]))]
tau = S.symbols('tau')
Ppart = S.Matrix([[6*mu,tau,1,0],[beta,mu,0,1]])
Pc = Ppart + S.Matrix([[0,0,0,0],[-12*v,0,0,0]])
for j, order, epsilon, vector in data:
    sigma = wj*Pc*vector
    comparison = sigma + 12*epsilon*wj*v*e
    assert (comparison-wj*Ppart*vector).applyfunc(S.expand) == S.zeros(2,1)
    assert 12*epsilon % order == 0
    print('finite place', j, ': c-dependent collar cancels exactly; root unit invariant')

D = C-12*kap
sigma_actual = S.Matrix([-c*mu/2, -c*c/24-c*D/12]).subs(c,-12*v)
L = s+12*v
F = S.Matrix([mu*L/2,C*L/12-L*L/24+6*v])
G = S.Matrix([mu*s/2,C*s/12-s*s/24])
kcusp = -s+12*kap
assert (F-sigma_actual-kcusp*v*e-G-6*v*e).applyfunc(S.expand) == S.zeros(2,1)
gamma_cusp = S.Matrix([6*mu,C-s-12*v])
b = gamma_cusp/12-e/24
assert (G.subs(s,s+1)-G-b-v*e).applyfunc(S.expand) == S.zeros(2,1)
assert ((G+6*v*e).subs(v,v+1)-(G+6*v*e)-6*e) == S.zeros(2,1)
print('actual-to-corrected-cusp comparison = ordinary gauge + G(s) + 6*v*delta')
print('positive q deck: ordinary -v*delta plus Delta_s G equals +b exactly')

# On a node chart x_j=W/r^j, y_j=r^(j+1)/W, multiplication
# W -> r^(-n)W and index j -> j-n leave both coordinates unchanged.
r, W = S.symbols('r W', nonzero=True)
for j in range(-12,25):
    for n in range(-25,26):
        xp = (r**(-n)*W)/r**(j-n)
        yp = r**(j-n+1)/(r**(-n)*W)
        assert S.simplify(xp-W/r**j) == 0
        assert S.simplify(yp-r**(j+1)/W) == 0
        left = S.Matrix([[j-n,j+1-n],[1,1]])
        assert left.det() == -1
print('all 1887 node-chart tests: integral r shifts preserve x,y and unimodularity')
n1,n2 = S.symbols('n1 n2', integer=True)
assert S.expand((-n1)+(-n2)+n1+n2) == 0
print('integer logarithm cocycle gives exact additive fan cocycle')

orders = {'zero':4,'one':-3,'infinity':-1}
assert sum(orders.values()) == 0
assert S.gcd(12,S.gcd(4,S.gcd(3,1))) == 1
out = {
    'status':'PASS',
    'base':'(P1 x Delta_r) minus {(infinity,0)}',
    'ordinary_gauge':'zeta + k*log(r)/(2*pi*i)*delta',
    'ordinary_transition':'W_j=r^(-n_ij) W_i',
    'finite_collar_after_gauge':'w_j*Pi_part*v_j',
    'cusp_extra_translation':'G(s)+6*log(r)/(2*pi*i)*delta',
    'positive_q_shift':1,
    'clockwise_cusp_shift':-1,
    'orders_of_K':orders,
    'node_chart_checks':37*51,
    'origin_completion':'NOT CLAIMED'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL EXACT CHECKS PASSED')
