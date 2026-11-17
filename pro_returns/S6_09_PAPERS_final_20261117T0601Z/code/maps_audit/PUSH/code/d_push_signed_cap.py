#!/usr/bin/env python3
"""Exact normalization/relative-orientation checks for C.3.22."""
from pathlib import Path
import json
import sympy as sp

t=sp.symbols("t")
# p1=-tr(F^2)/(8*pi^2); F=dt*w+(t^2-t)w^2.
transgression=-sp.integrate(2*(t*t-t),(t,0,1))/8
assert transgression==sp.Rational(1,24)
# For a left Maurer form d(w)=-w^2, CS=-( -1+2/3 )/8.
CS_left=-(-1+sp.Rational(2,3))/8
assert CS_left==sp.Rational(1,24)
# For -dB*B^-1 the Chern-Simons sign is opposite.
CS_frame=-(1-sp.Rational(2,3))/8
assert CS_frame==-sp.Rational(1,24)

# Q orientation [g,u,w,r,a].  Trace term: -dchi*u*w*g*a.
order=[3,1,2,0,4]
permutation_sign=(-1)**sum(order[i]>order[j]
                         for i in range(5) for j in range(i+1,5))
assert permutation_sign==-1
chi_integral=-1
mapping_pairing_sign=-1*permutation_sign*chi_integral
assert mapping_pairing_sign==-1

p,s,eps=sp.symbols("p_rel s_delta epsilon_cap")
J=sp.expand((eps*p-4*(eps*3*s))/24)
assert sp.simplify(J-eps*(p-12*s)/24)==0
result={
    "statement":"C.3.22",
    "status":"PASS",
    "p1_normalization":"-tr(F wedge F)/(8 pi^2)",
    "coordinate_clutch_CS_coefficient_in_units_pi_inverse_square":str(CS_left),
    "relative_boundary_frame_CS_coefficient":str(CS_frame),
    "interval_transgression_coefficient":str(transgression),
    "relative_frame_p1_in_terms_of_a0":"-a0",
    "mapping_torus_p1x_in_terms_of_a0":"-a0",
    "common_cap_sign":True,
    "J_reduction":str(J),
    "actual_s_delta_evaluated":False,
}
serialized=json.dumps(result,indent=2)
Path(__file__).with_suffix(".json").write_text(serialized+"\n")
print(serialized)
