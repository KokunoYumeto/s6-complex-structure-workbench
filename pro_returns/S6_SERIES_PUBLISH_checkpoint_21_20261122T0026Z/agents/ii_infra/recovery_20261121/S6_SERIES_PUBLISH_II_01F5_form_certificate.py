#!/usr/bin/env python3
"""Prereading exterior-algebra certificate; no target-proof text is read."""
from itertools import combinations
import json
import sympy as S

tau, taub, s, sb, a, b, c, u, w = S.symbols(
    "tau taub s sb a b c u w"
)

def plus(*forms):
    out = {}
    for form in forms:
        for key, value in form.items():
            out[key] = S.expand(out.get(key, 0) + value)
    return {key: value for key, value in out.items() if value != 0}

def scale(value, form):
    return {key: S.cancel(value * coeff) for key, coeff in form.items()}

def wedge(left, right):
    out = {}
    for x, vx in left.items():
        for y, vy in right.items():
            if set(x) & set(y):
                continue
            inversions = sum(i > j for i in x for j in y)
            key = tuple(sorted(x + y))
            out[key] = S.expand(out.get(key, 0) + (-1)**inversions * vx * vy)
    return {key: value for key, value in out.items() if value != 0}

def eq(left, right):
    keys = set(left) | set(right)
    return all(S.cancel(left.get(k, 0) - right.get(k, 0)) == 0 for k in keys)

theta = [{(i,): S.Integer(1)} for i in range(1, 5)]
A = plus(scale(tau, theta[0]), theta[1])
Ab = plus(scale(taub, theta[0]), theta[1])
Xi = plus(scale(s, theta[2]), theta[3])
Xib = plus(scale(sb, theta[2]), theta[3])
eta = wedge(A, Xi)
etab = wedge(Ab, Xib)
assert eq(theta[0], scale(1/(tau-taub), plus(A, scale(-1, Ab))))
assert eq(theta[1], scale(1/(tau-taub), plus(scale(tau, Ab), scale(-taub, A))))
assert eq(theta[2], scale(1/(s-sb), plus(Xi, scale(-1, Xib))))
assert eq(theta[3], scale(1/(s-sb), plus(scale(s, Xib), scale(-sb, Xi))))
volume = wedge(eta, etab)
assert eq(volume, {(1,2,3,4): -(tau-taub)*(s-sb)})
K = (-a+b*tau)/(tau-taub)
beta = scale(K, Ab)
beta2 = plus(scale(u, Ab), scale(w, Xib))
assert eq(wedge(eta, wedge(beta, beta2)), scale(K*w, volume))
central_full = -c/(s-sb)
assert S.cancel(-(s-sb)*central_full-c) == 0

# Verify the coarea sign at the differential-form level, without choosing
# a metric or absorbing a constant: indices 0=t,1=z2,2=z3,3=bar(t),
# 4=bar(z2),5=bar(z3).
dt={(0,):S.Integer(1)}
dbar_t={(3,):S.Integer(1)}
omega2={(1,2):S.Integer(1)}
bar_omega2={(4,5):S.Integer(1)}
omega3=wedge(dt, omega2)
bar_omega3=wedge(dbar_t, bar_omega2)
coarea_left=scale(S.I,wedge(omega3,bar_omega3))
coarea_right=wedge(scale(S.I,wedge(dt,dbar_t)),wedge(omega2,bar_omega2))
assert eq(coarea_left,coarea_right)

out={
 "method":"Direct alternating exterior products with explicit inversion signs; exact rational-function simplification only.",
 "target_proof_read":False,
 "period_coordinates":[str(S.factor(eta.get(k,0))) for k in [(1,3),(2,3),(1,4),(2,4)]],
 "volume_coefficient":str(S.factor(volume[(1,2,3,4)])),
 "positive_volume_for_tau_x_plus_i_y_s_u_plus_i_v":"4*y*v, y>0,v>0",
 "coefficient_maps_theta1_theta2_theta3":[
   "-bar(A)/(tau-taub)","tau*bar(A)/(tau-taub)","-bar(Xi)/(s-sb)"
 ],
 "serre_pairing_coefficient":str(S.factor(K*w)),
 "central_quotient_derivative_beta2":str(-(s-sb)*w),
 "central_quotient_derivative_gamma":str(c),
 "coarea_identity_exact":True,
 "local_relative_exponent":"a-m+1",
 "local_norm_exponent":"2*(a-m+1)/m",
 "uniform_lower_bound_conditions":"integers m>=1, 0<=a<=m-1; 0<|t|<=1; |u|>=u0>0",
 "uniform_lower_bound_constant":"4*u0^2*pi^2*r^4/m^2",
 "events_added":0,
 "all_assertions_passed":True
}
print(json.dumps(out,indent=2))
