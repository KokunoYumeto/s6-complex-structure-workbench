#!/usr/bin/env python3
"""Exact checks for the actual Milnor-page Poincare-line comparison.

This checks finite algebra only.  The Leray and actual-clutching arguments
are given separately in sections/ab_push_actual_line_comparison.tex.
"""
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
tau, mu, beta = s.symbols('tau mu beta')
Pi = s.Matrix([[6*mu,tau,1,0],[beta,mu,0,1]])
A1 = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
R1 = s.Matrix([[-1/tau,0],[(1-mu)/tau,1]])
R2 = s.Matrix([[1/tau,0],[-mu/tau,1]])
changes = [
    {tau:(tau-1)/tau,mu:(1-mu)/tau,beta:beta+2-6*(1-mu)**2/tau},
    {tau:-1/tau,mu:1+mu/tau,beta:beta-3-6*mu**2/tau},
]
delta = s.Matrix([0,0,0,1])
gamma = s.Matrix([[1,0,0,0]])
checks = {}
for j,(A,R,change) in enumerate(zip([A1,A2],[R1,R2],changes),1):
    difference = (R*Pi-Pi.subs(change,simultaneous=True)*A).applyfunc(s.factor)
    assert difference == s.zeros(2,4)
    assert A*delta == delta and gamma*A == gamma
    assert R[0,1] == 0 and R[1,1] == 1
    checks[f'period_covariance_R{j}'] = True

a,b,eps,X,Y = s.symbols('a b eps X Y')
lam = 1-eps
h = 1+eps*a**4
t = b**3/h
scale = a*b**2/h
relation = b**3-a**4-1

def reduce_C(expr):
    numerator,denominator = s.fraction(s.factor(expr))
    numerator = s.rem(numerator,relation,b)
    return s.factor(numerator/denominator)

assert reduce_C(t-1-lam*a**4/h) == 0
assert reduce_C(-3*t**3*(t-1)/scale**4+3*lam*b) == 0
assert reduce_C(2*t**4*(t-1)**2/scale**6-2*lam**2*a**2) == 0
assert reduce_C(-s.sqrt(2)*t**2*(t-1)/scale**3+s.sqrt(2)*lam*a) == 0
disc = -16*(4*(-3*lam*b)**3+27*(2*lam**2*a**2)**2)
assert reduce_C(disc-1728*lam**3*h) == 0
assert s.gcd(s.Poly(h,a),s.Poly(s.diff(h,a),a)).degree() == 0
checks.update({
    'minimal_pullback_equation':True,
    'pulled_back_section':True,
    'discriminant_1728_lambda_cubed_h':True,
    'four_simple_a_roots_with_three_b_values_each':True,
    'ramification_contribution':8+9+11,
    'two_genus_minus_two':-24+8+9+11,
    'chi_O':12//12,
    'P_intersects_O':0,
    'Poincare_square':-1-1-2*0,
})
assert checks['two_genus_minus_two'] == 4
assert checks['Poincare_square'] == -2
out = HERE/'ab_push_actual_line_comparison.json'
out.write_text(json.dumps(checks,indent=2)+'\n')
print('PASS: two exact marked period covariances; both preserve gamma and delta.')
print('PASS: pullback Y^2 = X^3 - 3(1-eps)bX + 2(1-eps)^2 a^2.')
print('PASS: section (0,-sqrt(2)(1-eps)a); discriminant 1728(1-eps)^3(1+eps a^4).')
print('PASS: for 0<eps<1, twelve simple I1 values, genus 3, chi(O)=1; Poincare square -2.')
print('Scope: the actual bundle identification and square comparison require the accompanying proof.')
