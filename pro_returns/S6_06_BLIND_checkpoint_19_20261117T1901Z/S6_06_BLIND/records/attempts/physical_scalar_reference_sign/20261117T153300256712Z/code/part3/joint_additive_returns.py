#!/usr/bin/env python3
"""Exact certificates for the actual two-cap page and signed return proof."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S

mi, m0, ni, n0, e = S.symbols("m_infty m_0 n_infty n_0 epsilon")
alpha, gamma = S.symbols("alpha gamma")
D = m0*ni + mi*n0
M = mi*m0
relations = S.groebner([e**2-1, D-e], e, ni, n0, mi, m0, alpha, gamma)

def certificate_zero(expr):
    numerator = S.together(S.expand(expr)).as_numer_denom()[0]
    assert relations.reduce(numerator)[1] == 0, expr

phase = S.Matrix([[e*m0, -e*n0], [e*mi, e*ni]])
certificate_zero(phase.det()-e)
ph1, ph2 = phase*S.Matrix([gamma,alpha])
certificate_zero(m0*ph2-mi*ph1-alpha)
certificate_zero(1-e*m0*ni-e*mi*n0)
certificate_zero((1-e*m0*ni)/mi-e*n0)
certificate_zero((1-e*mi*n0)/m0-e*ni)
certificate_zero(e*e-1)

# The two root cap formulae give exactly the same ordinary phases.
u0 = m0*gamma-n0*alpha
ui = mi*gamma+ni*alpha
certificate_zero(-alpha/mi+e*m0*ui/mi-ph1)
certificate_zero(e*ui-ph2)
certificate_zero(e*u0-ph1)
certificate_zero(alpha/m0+e*mi*u0/m0-ph2)

# The two displayed holomorphic charts really satisfy the page equation.
z, tau = S.symbols("z tau")
Xpow_i = z**mi/(1-tau*z**mi)
Ypow_i = 1/(1-tau*z**mi)
Xpow_0 = 1/(z**m0-tau)
Ypow_0 = z**m0/(z**m0-tau)
assert S.simplify(Ypow_i-tau*Xpow_i-1) == 0
assert S.simplify(Ypow_0-tau*Xpow_0-1) == 0
assert S.simplify(Ypow_i/Xpow_i-z**(-mi)) == 0
assert S.simplify(Ypow_0/Xpow_0-z**m0) == 0

genus = (mi-1)*(m0-1)/2
ramification = m0*(mi-1)+mi*(m0-1)+(M-1)
assert S.expand(2*genus-2-(-2*M+ramification)) == 0

# Actual positive parameter origin, retaining its endpoint-fixed delta gauge.
s, v, theta, g, C, MM = S.symbols("s v theta g C M")
delta = S.Matrix([0,1])
gam = S.Matrix([g,-C-s-MM*v])
clean = lambda A: A.applyfunc(S.simplify)
for sign in (1,-1):
    ordinary = sign*S.Matrix([-g*s/MM,C*s/MM+s*s/(2*MM)+s*v])
    cusp = sign*S.Matrix([g*v,-C*v-MM*(v*v-v)/2])
    assert clean(ordinary.subs(v,v+1)-ordinary-sign*s*delta) == S.zeros(2,1)
    assert clean(cusp.subs(v,v+1)-cusp-sign*s*delta-sign*gam) == S.zeros(2,1)
    F = cusp-ordinary
    angular = clean(F.subs(v,v+theta)-F)
    assert clean(angular-sign*theta*gam+
                 sign*MM*theta*(theta-1)*delta/2) == S.zeros(2,1)
    assert clean(angular.subs(s,s+2*MM)-angular+
                 2*sign*MM*theta*delta) == S.zeros(2,1)

l, k = S.symbols("l k", integer=True, nonnegative=True)
raw = [
    ("F46 E6 good/good",6,1,6,8,3,0,0,3*l,4*k,0),
    ("F46 E6 good/reduced III",6,2,3,8,3,0,3,3*l,4*k+1,-3*l*k),
    ("F46 E6 reduced IV/good",6,3,2,8,3,4,0,3*l+2,4*k,-4*k*(2*l+1)),
    ("F46 E6 reduced IV/reduced III",6,6,1,8,3,4,3,3*l+2,4*k+1,
     -35*l*k-8*l-22*k-5),
    ("F47 E7 reduced III/reduced II",2,2,1,9,2,3,2,4*l+3,6*k+1,
     -22*l*k-3*l-15*k-2),
    ("F47 E7 reduced III/good II",2,2,1,9,2,3,0,4*l+3,6*k,
     -k*(22*l+15)),
    ("F47 E7 good III-star/reduced II",2,1,2,9,2,0,2,4*l,6*k+1,-4*l*k),
    ("F38 I1-star/reduced IV",12,6,2,7,4,2,4,S.Integer(2),6*l+1,-16*l-2),
    ("F38 I1-star/good IV",12,2,6,7,4,2,0,S.Integer(2),3*k,S.Integer(0)),
]
rows=[]
for label,d,a,b,ei,e0,eri,er0,rooti,root0,expected in raw:
    assert a*b==d
    degree=S.expand(rooti*root0)
    chi=S.expand((degree*(12-ei-e0)+root0*eri+rooti*er0)/12)
    height=S.expand(degree*S.Rational(a*a,d))
    square=-height
    PO=S.expand(height/2-chi)
    A=S.expand((12*square+24*chi)/24)
    assert S.expand(A-expected)==0
    assert S.expand(A+PO)==0
    rows.append(dict(
        label=label,d=d,a=a,b=b,
        m_infty=str(rooti),m_0=str(root0),
        root_euler_infty=eri,root_euler_0=er0,
        page_degree=str(degree),page_genus=str(S.expand((rooti-1)*(root0-1)/2)),
        chi=str(chi),height=str(height),line_square=str(square),
        section_intersection=str(PO),actual_A=str(A),
        required_sphere_equation="m_0*n_infty+m_infty*n_0=epsilon, epsilon=+1 or -1",
        root_domains="Positive indices for good roots; nonnegative for reduced roots; retain coprimality from sphere equation.",
        orientation="positive r-loop, lambda=r^(m_infty*m_0), beta=epsilon*gamma_out, pi_*x=+1",
    ))
    print(f"{label}: degree={degree}, chi={chi}, N^2={square}, PO={PO}, A={A}")

# The omitted good/good E7 sector has no sphere tuple: its determinant is even.
empty_D=S.expand(6*k*ni+4*l*n0)
assert all(int(c)%2==0 for c in S.Poly(empty_D,k,l,ni,n0).coeffs())

# One quadratic I1-star cap on either of its two actual source profiles.
chi_one=S.Rational(2*(12-7)+2,12)
height_one=S.Rational(2*36,12)
A_one=chi_one-height_one/2
assert (chi_one,height_one,A_one)==(1,6,-2)
print("F36 one I1-star cap, both profiles and both norms: chi=1, N^2=-6, A=-2")

out=dict(
    status="PASS",
    timestamp_utc=datetime.now(timezone.utc).isoformat(),
    scope="Exact algebraic certificate supplementing the actual norm/page/line/Thom maps in P3K.28.",
    proof="notes/part3_joint_additive_returns_working.md",
    topology_sources=[
        "notes/part3_i1star_caps.tex",
        "notes/part3_i1star_iv_caps.tex",
        "notes/part3_iv_star_iii_joint.tex",
        "notes/part3_iii_star_ii_joint.tex"],
    phase_matrix=[[str(x) for x in phase.row(i)] for i in range(2)],
    exact_relations=["epsilon^2=1","m_0*n_infty+m_infty*n_0=epsilon"],
    cap_cut_integer_changes={
        "infinity":["epsilon*n_0","-epsilon*n_infty"],
        "zero":["-epsilon*n_0","epsilon*n_infty"]},
    sheet_orbit_proof={
        "infinity":"Step -epsilon*m_0*n_infty modulo M has gcd m_0 with M; Bezout equation proves gcd(m_infty,n_infty)=gcd(m_infty,m_0)=1.",
        "zero":"Step -epsilon*m_infty*n_0 modulo M has gcd m_infty with M; same exact Bezout identity.",
        "representative_stabilizer":"n_i*k+m_i*h=0 => (k,h)=(m_i*j,-n_i*j); A_i^(m_i*j)B^(-n_i*j)=1."},
    genus=str(genus),
    coinvariants="Two actual closed lifts of the retained nodal meridian have primitive vanishing cycles v,Av with pairing +1 or -1.",
    rows=rows,
    excluded_sector={"label":"F47 E7 good/good","D":str(empty_D),"reason":"D is even, so cannot be +1 or -1."},
    one_star=dict(profiles=["I1*+I3+2I1","I1*+IV+I1"],a=6,b=2,m=2,n=[1,-1],
                  chi=1,height=6,line_square=-6,actual_A=-2),
)
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS: exact marked phase maps, both cap cuts, actual origin gauges, page charts, genus, nine joint rows, and both one-star profiles.")
