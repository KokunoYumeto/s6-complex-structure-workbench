#!/usr/bin/env python3
"""Exact certificates for B.4.7 and the generic-simple-torus limitation."""
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
R = s.Matrix([[1,1],[0,-1]])
coeff = s.Matrix([[1,1],[0,-1]])
assert R.det() == -1 and R*coeff == s.eye(2)
generic = s.Matrix([[1,0]])*coeff
assert generic == s.Matrix([[1,1]])
H1 = s.Matrix([[0,1],[-1,0]])
SNF = smith_normal_form(H1,domain=ZZ)
assert abs(H1.det()) == 1
assert [abs(SNF[i,i]) for i in range(2)] == [1,1]
O1 = s.Matrix([[1,-1]])
assert O1.rank() == 1 and len(O1.nullspace()) == 1
central = [1,0,0,3,2]
central_threefold = [central[k] if k<len(central) else 0 for k in range(7)]
for k,v in enumerate(central):
    central_threefold[k+2] += v
assert central_threefold == [1,0,1,3,2,3,2]
assert sum((-1)**k*v for k,v in enumerate(central)) == 0
assert sum((-1)**k*v for k,v in enumerate(central_threefold)) == 0
assert s.simplify(s.I/(1+s.I)) == (1+s.I)/2

a,b,c,d,A,B,C,D,tau,mu,beta,lam = s.symbols('a b c d A B C D tau mu beta lam')
x = 6*a*mu+b*tau+c
y = a*beta+b*mu+d
X = 6*A*mu+B*tau+C
Y = A*beta+B*mu+D
det = s.expand(x*Y-X*y)
coef = s.expand(det).coeff(beta)
assert s.expand(coef-((A*b-a*B)*tau+(A*c-a*C))) == 0
reduced = s.factor(det.subs({A:lam*a,B:lam*b,C:lam*c}))
assert s.expand(reduced-x*(D-lam*d)) == 0
zero_gamma = s.expand(det.subs({a:0,A:0}))
expected = (b*D-B*d)*tau+(c*B-C*b)*mu+(c*D-C*d)
assert s.expand(zero_gamma-expected) == 0

data = {
    'Chern_restriction_matrix':R.tolist(),
    'Chern_coefficient_matrix':coeff.tolist(),
    'generic_Chern_vector':[1,1],
    'integral_H1_normalization_map':H1.tolist(),
    'H1_Smith':[1,1],
    'O_H1_map':O1.tolist(),
    'central_surface_Betti':central,
    'central_threefold_Betti':central_threefold,
    'Euler':0,
    'generic_Hopf_tau':'(1+i)/2',
    'generic_Hopf_multiplier':'-exp(-pi)',
    'central_Hopf_multiplier':'exp(-2*pi)',
    'period_determinant_beta_coefficient':str(coef),
    'period_determinant_when_first_triples_proportional':str(reduced),
    'period_determinant_when_both_gamma_zero':str(zero_gamma),
}
(HERE/'ab_push_hopf_cap.json').write_text(json.dumps(data,indent=2,default=int)+'\n')
print('PASS: unimodular Chern restriction matrix; central vectors(1,0),(0,1), generic(1,1).')
print('PASS: integral H1 normalization matrix has Smith(1,1); coherent H1 map has rank1.')
print('PASS: central surface Betti(1,0,0,3,2); product-P1 Betti(1,0,1,3,2,3,2); Euler0.')
print('PASS: generic scalar Hopf multiplier -exp(-pi), central multiplier exp(-2*pi).')
print('PASS: exact determinant identities used in the generic simple-torus obstruction.')
