#!/usr/bin/env python3
"""Exact Chern-character coefficient check and blowup sign diagnostic for 02WW.

This verifies the polynomial computation in the new derivation. It does not
certify the geometric finiteness, purity, or bundle-factorization arguments.
"""
import json
import sympy as s

t, a, c, b, d, new_c2 = s.symbols("t a c b d new_c2")
ch_old = 2 + a*t + (a*a/2-b)*t*t
ch_new = 2 + (a+c)*t + ((a+c)**2/2-new_c2)*t*t
ch_quotient = c*t + (d-c*c/2)*t*t
solution = s.solve(s.expand(ch_new-ch_old-ch_quotient).coeff(t, 2), new_c2)[0]
increment = s.expand(solution-b)
tor_degree = d-c*c
image_kernel_degree = (a+c)*c-d
assert s.expand(increment-image_kernel_degree) == 0
assert s.expand(increment-(a*c-tor_degree)) == 0

# Use independent pairing variables for evaluating an intersection number.
ac, cc = s.symbols("a_dot_C C_squared")
pairing_increment = ac+cc-d
pairing_kernel = ac+cc-d
pairing_tor = d-cc
blowup = {ac: 1, cc: -1, d: 1}
assert pairing_increment.subs(blowup) == -1
assert pairing_kernel.subs(blowup) == -1
assert pairing_tor.subs(blowup) == 2

# In the blowup chart (x,y)=(u,u*v), the exceptional tangent is d/dv.
u, v = s.symbols("u v")
blowup_map = s.Matrix([u, u*v])
jacobian = blowup_map.jacobian([u, v])
assert jacobian.det() == u
exceptional_tangent_image = (jacobian*s.Matrix([0, 1])).subs(u, 0)
assert exceptional_tangent_image == s.zeros(2, 1)

output = {
    "owner": "night:P4.24",
    "tag": "02WW",
    "scope": "exact coefficient computation and blowup diagnostic only",
    "chern_character_difference_residual": str(s.expand((ch_new-ch_old-ch_quotient).subs(new_c2, solution))),
    "new_c2": str(solution),
    "increment": str(increment),
    "image_kernel_degree": str(image_kernel_degree),
    "tor_degree": str(tor_degree),
    "increment_minus_image_kernel": str(s.expand(increment-image_kernel_degree)),
    "increment_minus_tor_degree": str(s.expand(increment-tor_degree)),
    "blowup": {
        "C_squared": -1,
        "c1_old_dot_C": 1,
        "quotient_line_degree": 1,
        "chern_increment": int(pairing_increment.subs(blowup)),
        "image_kernel_degree": int(pairing_kernel.subs(blowup)),
        "tor_line_degree": int(pairing_tor.subs(blowup)),
        "jacobian": [[str(x) for x in row] for row in jacobian.tolist()],
        "determinant": str(jacobian.det()),
        "exceptional_tangent_image": [str(x) for x in exceptional_tangent_image],
    },
    "assertions_passed": True,
    "geometric_claims_certified_by_program": False,
}
print(json.dumps(output, indent=2, sort_keys=True))
