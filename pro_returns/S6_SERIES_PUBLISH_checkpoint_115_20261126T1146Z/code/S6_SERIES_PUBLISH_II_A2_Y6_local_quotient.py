#!/usr/bin/env python3
"""Exact local exploration for unopened R13; no whole-target check credit.

Checks only polynomial/rational identities for the explicit I2 model and
the displayed central-fibre coordinate maps.  Properness, freeness, and
normalization are proved in the accompanying exploration record.
"""
import json
import sympy as sp

x, y, s, t, w, u, v = sp.symbols("x y s t w u v")


def zero(expr):
    value = sp.factor(sp.cancel(expr))
    assert value == 0, value
    return str(value)


f = (x*x-s*s)*(x-1)
Xp = s+2*s*(s-1)/(x-s)
Yp = 2*s*(s-1)*y/(x-s)**2
curve = zero((Yp**2-(Xp**2-s*s)*(Xp-1)).subs(y*y, f))
X2 = sp.factor(-s+2*s*(s+1)/(Xp+s))
Y2 = sp.factor(2*s*(s+1)*Yp/(Xp+s)**2)
XB = (x-s*s)/(x-1)
YB = (s*s-1)*y/(x-1)**2
composition = [zero(X2-XB), zero(Y2-YB)]
B_square = [
    zero((XB-s*s)/(XB-1)-x),
    zero((s*s-1)*YB/(XB-1)**2-y),
]

A = (x*(1+t)-2)/(1-t)
xq, tq = t*A, -x/A
wq = 2*(x*t-1)*w/((1-t)**2*A)
node_base = zero(xq*tq+x*t)
node_curve = zero((wq*wq-(1-tq*tq)*(xq-1)).subs(w*w, (1-t*t)*(x-1)))
node_multiplier = sp.factor((wq/w).subs({x:0,t:0}))
assert node_multiplier == 1

uc = (1-w*w)/(1+w*w)
vc = 2*w/(1+w*w)
conic = zero(uc*uc+vc*vc-1)
back_to_P = sp.factor(vc/(uc-1))
assert back_to_P == -1/w
lam = (w-sp.I)/(w+sp.I)
lambda_B = zero(lam.subs(w,-1/w)+lam)

disc = sp.factor(sp.discriminant(f,x))
assert disc == 4*s*s*(s-1)**2*(s+1)**2

print(json.dumps({
    "scope":"Uncredited pre-release local exploration only; no compact ambient realization or target conclusion is tested.",
    "cubic_discriminant":str(disc),
    "psi_curve_residual":curve,
    "psi_minus_s_after_psi_s":{
        "x":str(X2),"y":str(Y2),"translation_B_residuals":composition,
        "translation_B_square_residuals":B_square},
    "resolved_node_chart":{
        "A":str(A),"x_prime":str(xq),"t_prime":str(tq),
        "w_prime":str(wq),"base_residual":node_base,
        "surface_residual":node_curve,"node_w_multiplier":str(node_multiplier)},
    "central_component_maps":{
        "P_to_E_u":str(uc),"P_to_E_v":str(vc),"conic_residual":conic,
        "composition_w":str(back_to_P),"lambda":str(lam),
        "lambda_translation_B_plus_lambda_residual":lambda_B},
    "group_action":"gamma^2=(e+2b,T_B(q),s); gamma^4=identity; b has exact order four",
    "geometric_claims_not_automated":[
        "properness of the resolved projective family",
        "extension of psi at the central points mapping to infinity",
        "free quotient is a smooth complex manifold",
        "generic fibres are two-dimensional tori",
        "central normalization and two conductor-image curves",
        "compatibility with any compact ambient b1=b2=0 manifold"]
},indent=2)+"\n")
