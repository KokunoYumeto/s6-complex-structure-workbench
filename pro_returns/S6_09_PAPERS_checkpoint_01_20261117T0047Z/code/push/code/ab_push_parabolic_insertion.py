#!/usr/bin/env python3
"""Exact polynomial and divisor data for the auxiliary parabolic Kato family.

Uniform convergence, analytic collar gluing, and properness are proved in
the accompanying source, not inferred from a finite numerical test.
"""
from pathlib import Path
import json
import sympy as s

base = Path(__file__).resolve().parent
z, w, v, p, a, kap = s.symbols('z w v p a kappa', nonzero=True)
checks = []
for n in range(1,13):
    f = s.Matrix([kap*z*(a*v+p)**n, a*v])
    df = f.jacobian([z,v]).subs({z:0,v:0})
    assert df == s.diag(kap*p**n,a)
    literal_factor = kap*(v+p)**n
    blowdown_factor = kap*(a*v+p)**n
    gauge = (v+p)**n
    assert s.cancel(literal_factor*gauge.subs(v,a*v)/gauge-blowdown_factor)==0
    # theta(av)=−v^{-1}theta(v): O(−n[−p]) has factor (v/p)^n.
    normal_after_blowups = kap*p**n*(v/p)**n
    assert s.cancel(normal_after_blowups-kap*v**n)==0
    assert s.cancel((kap*v**n)*(a*v)**n/v**n-kap*a**n*v**n)==0
    checks.append({'n':n,'fixed_point_derivative':str(df), 'normal_degree':-n,
                   'weighted_exceptional_restriction':f'{n}[−p]'})

# Exact finite product identities, with the displayed endpoint factors.
for ell in range(1,9):
    g = s.prod(1+a**j*v/p for j in range(1,ell+1))
    h = s.prod(1+a**j*p/v for j in range(ell))
    assert s.cancel(g.subs(v,a*v)*(1+a*v/p)-g*(1+a**(ell+1)*v/p))==0
    assert s.cancel(h.subs(v,a*v)*(1+a**(ell-1)*p/v)-h*(1+p/(a*v)))==0

# A concrete uniform compact-containment certificate (all n >= 1).
A, rho, K, R, delta = map(s.Rational,['1/4','1/2','2','1/4','1/10000'])
assert A*R+(1+A)*delta < rho*R
upper = K*K*(rho*R)**2+rho*rho
assert upper == s.Rational(5,16) < 1

# Elliptic quartic and T^1 degree vectors (E direction, P1 direction).
left = s.Matrix([8,-1])
hopf = s.Matrix([0,0])
triple = s.Matrix([0,1])
parabolic = s.Matrix([-8,0])
assert left+parabolic+triple == s.zeros(2,1)
assert -(left+hopf) == s.Matrix([-8,1])

# Positive base exceptional divisors retain only the toric invariants.
aa, bb = s.symbols('alpha beta', integer=True, nonnegative=True)
nontrivial_block = s.Matrix([[0,aa],[-aa-12*bb,0]])
assert s.expand(nontrivial_block.det()-aa*(aa+12*bb)) == 0

out = {
 'status':'PASS',
 'germ_and_normal_checks':checks,
 'finite_product_identity_lengths':list(range(1,9)),
 'uniform_domain_certificate':{'A':str(A),'rho':str(rho),'K':str(K),'R':str(R),
                               'delta':str(delta),'squared_norm_ratio_upper':str(upper)},
 'elliptic_quartic_normal_degree_vector':list(left),
 'bare_Hopf_required_effective_triple_degree':list(-(left+hopf)),
 'parabolic_degree8_normal_plus_triple_sum':list(left+parabolic+triple),
 'mixed_base_divisor_nonzero_block_determinant':str(nontrivial_block.det()),
 'scope':'Auxiliary compact Kato family and exact interface data; no global S6 gluing/smoothing.'
}
encoded=json.dumps(out,indent=2,default=str)
(base/'ab_push_parabolic_insertion.json').write_text(encoded+'\n')
print(encoded)
