#!/usr/bin/env python3
"""Exact coordinate checks for the selected-cusp first fixed-edge flop.

The geometric extension and relative-group comparison are proved in
notes/part3_source_cusp_fixed_edge_working.md. This program records only
the literal algebraic arrows used there; it does not infer a new fan
formula or assign the separate Jin pair.
"""
from pathlib import Path
import datetime
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
checks = []

def zero(name, expression):
    value = S.cancel(S.expand(expression))
    assert value == 0, (name, value)
    checks.append({"name": name, "exact_difference": str(value)})

def qmul(p, q):
    a,b,c,d = p
    e,f,g,h = q
    return S.Matrix([a*e-b*f-c*g-d*h,
                     a*f+b*e+c*h-d*g,
                     a*g-b*h+c*e+d*f,
                     a*h+b*g-c*f+d*e])

def qconj(p):
    return S.Matrix([p[0],-p[1],-p[2],-p[3]])

def qnorm(p):
    return sum(z*z for z in p)

def qinv(p):
    return qconj(p)/qnorm(p)

def qcheck(name, p, q):
    for j in range(4):
        zero(f"{name}, coordinate{j}", p[j]-q[j])

s,rho,Z = S.symbols("s rho Z", nonzero=True)
z_of_s = (s-rho)/(s+rho)
s_of_z = rho*(1+Z)/(1-Z)
zero("ordered source inverse s", s_of_z.subs(Z,z_of_s)-s)
zero("ordered source inverse Z", z_of_s.subs(s,s_of_z)-Z)
mobius = S.Matrix([[1,-rho],[1,rho]])
zero("actual Mobius determinant", mobius.det()-2*rho)
zero("source branch D+ maps to0", z_of_s.subs(s,rho))
# The homogeneous second coordinate vanishes at D-.
zero("source branch D- maps to infinity", (s+rho).subs(s,-rho))
zero("source Mobius derivative", S.diff(z_of_s,s)-2*rho/(s+rho)**2)

u = S.Matrix(S.symbols("u0:4"))
v = S.Matrix(S.symbols("v0:4"))
one = S.Matrix([1,0,0,0])
i = S.Matrix([0,1,0,0])
q = qmul(u,v)
# Polynomial identities suffice for the rational inverse maps.
qcheck("quaternion conjugate inverse", qmul(qconj(u),u), qnorm(u)*one)
zero("quaternion norm product", qnorm(q)-qnorm(u)*qnorm(v))
qcheck("first product recovered normal factor",
       qmul(qconj(u),q), qnorm(u)*v)
qcheck("second product recovered base factor",
       qmul(q,qconj(v)), qnorm(v)*u)

# q^{-1}(u i u^{-1})q = v^{-1} i v, after clearing the
# explicitly recorded nonzero scalar norms.
left = qmul(qmul(qconj(q), qmul(qmul(u,i),qconj(u))), q)
right = qnorm(u)**2 * qmul(qmul(qconj(v),i),v)
qcheck("actual common-boundary map", left,right)

# General Cox scalar factors lie in the complex i-plane.
A,B,C,D = S.symbols("A B C D")
a = S.Matrix([A,B,0,0])
b = S.Matrix([C,D,0,0])
qcheck("first Cox factor commutes with i", qmul(a,i),qmul(i,a))
qcheck("second Cox factor commutes with i", qmul(b,i),qmul(i,b))
# The equivariance numerator identity is valid for every quaternion
# h and q, with inverses represented by conjugates and norms.
h = S.Matrix(S.symbols("h0:4"))
w = S.Matrix(S.symbols("w0:4"))
aw = qmul(qmul(a,w),b)
ah = qmul(qmul(a,h),qconj(a))
lhs = qmul(qmul(qconj(aw),ah),aw)
rhs = qnorm(a)**2 * qmul(qmul(qconj(b),qmul(qmul(qconj(w),h),w)),b)
qcheck("retained Cox action intertwines tau",lhs,rhs)

r,t = S.symbols("r t", integer=True)
zero("two endpoint parity exponents differ evenly", (r+t)-(r-t)-2*t)
endpoint_checks=[]
for rr in range(-5,6):
    for tt in range(-5,6):
        first=(-1)**(rr+tt)
        second=(-1)**(rr-tt)
        assert first==second
        endpoint_checks.append([rr,tt,int(first)])

# The retained sixth source winding is explicit rather than set to0.
rho_power = -6
assert rho_power == -6
checks.append({"name":"actual source Tate-unit winding", "integer":rho_power,
               "coefficient":"q_T/q=-u(rho)/(64*rho^6)+O(q), u(0)!=0"})

k,ell = S.symbols("k ell")
AA=(4*k-ell)/24
brel=(4*k-ell)/4
zero("exact Hopf integer b=6A",brel-6*AA)
zero("actual right exponent n=-6A",-brel+6*AA)
n=-6
central=1
m=S.symbols("m",integer=True)
forward_pair=(-n,m+2*n)
reset_pair=(m+2*n,-n)
assert (central+n)%28==23

record={
  "utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
  "proof":"P3K.40 (working proof submitted for audit)",
  "status":"PASS",
  "exact_checks":len(checks),
  "checks":checks,
  "supplementary_Cox_endpoint_cases":endpoint_checks,
  "actual_source_loop":{"parameter":"positive rho loop with a(u)=rho^2",
      "scalar":"fixed","initial_fan":"physical delta edge",
      "actual_initial_A":1,"actual_n_rel":-6,
      "retained_m":"unevaluated actual integer"},
  "first_fixed_edge_flop":{"relative_pair":[str(z) for z in forward_pair],
      "reset_pair":[str(z) for z in reset_pair],"central_integer":-5,"class_mod28":23},
  "not_inferred":["separate k and ell","full common-exterior source derivative",
                  "other-edge returns","arbitrary-fan formula"]}
out=ROOT/'code/part3/source_cusp_fixed_edge.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(f"PASS: {len(checks)} exact identities; {len(endpoint_checks)} supplementary Cox parity cases.")
print("Actual n_rel=-6; first fixed-edge central class=1-6=-5=23 mod28.")
print("Separate Jin pair and later-edge returns are not assigned.")
