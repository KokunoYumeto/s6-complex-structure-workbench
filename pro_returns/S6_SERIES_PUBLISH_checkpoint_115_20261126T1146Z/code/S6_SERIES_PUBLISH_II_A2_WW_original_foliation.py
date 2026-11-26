#!/usr/bin/env python3
"""Exact algebra in the released original 02WW foliation proof.

Written after release. This checks coordinate and Chern computations; it does
not claim a new independent derivation or certify the analytic extension step.
"""
import json
import sympy as s

a, b, lam, h = s.symbols('alpha beta lambda h', nonzero=True)
z, w, u, v = s.symbols('z w u v')
n = s.symbols('n', integer=True, positive=True)
A, B = s.symbols('A B', integer=True, positive=True)

# On the span of (z,w^n), the resonant contraction is a Jordan matrix.
M = s.Matrix([[a, lam], [0, a]])
Mh = s.Matrix([[a**h, h*lam*a**(h-1)], [0, a**h]])
Mh1 = s.Matrix([[a**(h+1), (h+1)*lam*a**h], [0, a**(h+1)]])
recurrence = (M*Mh-Mh1).applyfunc(s.simplify)
assert recurrence == s.zeros(2)
assert Mh.subs(h, 0) == s.eye(2)
F = s.Matrix([a*z+lam*w**n, b*w])
X = s.Matrix([n*z, w])
weighted_invariance = (F.jacobian([z,w])*X-s.Matrix([n*F[0],F[1]])).applyfunc(s.simplify)
assert weighted_invariance == s.zeros(2,1)

charts = [s.Matrix([u,u*v]), s.Matrix([u*v,v])]
regular_lifts = []
saddle_lifts = []
regular_forms = []
saddle_forms = []
for chart in charts:
    J=chart.jacobian([u,v])
    regular_lifts.append((J.inv()*s.Matrix([1,0])).applyfunc(s.simplify))
    saddle_lifts.append((J.inv()*s.Matrix([B*chart[0],-A*chart[1]])).applyfunc(s.simplify))
    regular_forms.append(J.T*s.Matrix([0,1]))
    saddle_forms.append((J.T*s.Matrix([A*chart[1],B*chart[0]])).applyfunc(s.factor))
assert u*regular_lifts[0] == s.Matrix([u,-v])
assert v*regular_lifts[1] == s.Matrix([1,0])
assert saddle_lifts[0] == s.Matrix([B*u,-(A+B)*v])
assert saddle_lifts[1] == s.Matrix([(A+B)*u,-A*v])
assert saddle_forms[0] == s.Matrix([(A+B)*u*v,B*u*u])
assert saddle_forms[1] == s.Matrix([A*v*v,(A+B)*u*v])

K,V,R,k,z0,z1,c,eps,E = s.symbols('K V R k z0 z1 c epsilon E')
G=lambda K,V,R:R*R-K*R-V*R
chern_residual=s.expand((-K+V)**2-z0-(R-V)*(K-R)-z1)
reduced=s.expand(chern_residual.subs(K*K,-k).subs(K*V,V*V))
assert s.expand(reduced-(G(K,V,R)-k-z0-z1)) == 0

def blowup_reduce(poly):
    """Evaluate E^2=-1 and E orthogonal to all pulled-back classes."""
    result=0
    for mon,coef in s.Poly(s.expand(poly),K,V,R,E).terms():
        if mon[3] and any(mon[:3]):
            continue
        if mon[3]==2:
            result-=coef
        else:
            assert mon[3]==0
            result+=coef*K**mon[0]*V**mon[1]*R**mon[2]
    return s.expand(result)

delta_G=blowup_reduce(G(K+E,V+eps*E,R+c*E)-G(K,V,R))
delta_K2=blowup_reduce((K+E)**2-K*K)
delta_KV_V2=blowup_reduce((K+E)*(V+eps*E)-(V+eps*E)**2-(K*V-V*V))
assert s.expand(delta_G-(-c*c+(1+eps)*c)) == 0
assert delta_K2 == -1
assert delta_KV_V2 == eps*eps-eps
assert all(delta_KV_V2.subs(eps,j)==0 for j in [0,1])
assert s.expand(delta_G.subs(eps,0)-(s.Rational(1,4)-(c-s.Rational(1,2))**2)) == 0
assert s.expand(delta_G.subs(eps,1)-(1-(c-1)**2)) == 0

def column(v): return [str(x) for x in v]
print(json.dumps({
    'tag':'02WW','owner':'night:P4.24','timing':'after target proof release',
    'resonant_iteration_recurrence_residual':[[str(x) for x in row] for row in recurrence.tolist()],
    'weighted_vector_field_invariance_residual':column(weighted_invariance),
    'regular_chart_lifts':list(map(column,regular_lifts)),
    'saddle_chart_lifts':list(map(column,saddle_lifts)),
    'regular_transverse_forms':list(map(column,regular_forms)),
    'saddle_transverse_forms':list(map(column,saddle_forms)),
    'chern_identity_after_K_squared_and_KV_reductions':str(reduced),
    'delta_K_squared':str(delta_K2),
    'delta_KV_minus_V_squared':str(delta_KV_V2),
    'delta_G':str(delta_G),
    'integer_bound_epsilon_zero':'1/4-(c-1/2)^2 <= 0 for c integral',
    'bound_epsilon_one':'1-(c-1)^2 <= 1',
    'assertions_passed':True,
    'whole_geometric_proof_certified':False,
},indent=2,sort_keys=True))
