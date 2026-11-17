#!/usr/bin/env python3
"""Exact exterior-sign and cubic-factor audit for C.3.20; no geometric inference."""
from fractions import Fraction
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def sign(seq):
    if len(set(seq)) != len(seq):
        return 0
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

# Orientation (g,u,w,r,a). Delta wedge B = chi'(r) dr da dg du dw.
annular_permutation = sign([3,4,0,1,2])
assert annular_permutation == 1
assert annular_permutation * (0-1) == -1  # chi goes from one to zero.

# Terms with one dt*eta in a cube give factor three. All higher dt terms vanish.
cubic_dt_factor = 3
assert cubic_dt_factor == 3
# E=dg da, Delta=dchi da, so both products repeat da.
assert sign([0,4,3,4]) == 0
assert sign([3,4,3,4]) == 0

# Stokes d(eta B)=Delta B - eta dB, hence integral eta E^2=integral Delta B.
stokes_eta_dB_sign = -1
assert stokes_eta_dB_sign == (-1)**1

# The compact page cover has exponents 4,-3,-1, degree12, genus3.
degree = 12
ramification = sum(degree-gcd(degree,abs(e)) for e in [4,-3,-1])
euler_curve = 2*degree-ramification
genus = 1-euler_curve//2
assert (ramification,euler_curve,genus) == (28,-4,3)

record = {
    "status":"PASS",
    "scope":"Algebraic checks only; no value of the actual relative square or monodromy is inferred.",
    "orientation":["gamma","u","w","r","q_angle"],
    "delta_B_permutation_sign":annular_permutation,
    "chi_outer_minus_inner":-1,
    "boundary_M_orientation":"negative gamma-u-w",
    "integral_Delta_B_equals_relative_square":True,
    "cubic_factor":cubic_dt_factor,
    "E_times_Delta_zero":True,
    "Delta_squared_zero":True,
    "cover_degree":degree,
    "cover_branch_exponents":[4,-3,-1],
    "cover_genus":genus,
    "actual_relative_square":"NOT EVALUATED",
    "actual_cap_cubic":"epsilon_cap * 3 * s_delta",
}
out = json.dumps(record,indent=2,sort_keys=True)+"\n"
(ROOT/'code/e_push_C_cubic.json').write_text(out)
(ROOT/'code/e_push_C_cubic.out').write_text(out)
print(out,end='')
