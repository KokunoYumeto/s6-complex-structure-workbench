#!/usr/bin/env python3
"""Symbolic verification of the exact ES–Koide–S6 morphisms."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

p=sp.symbols('p', positive=True, real=True)
R,u,T,a,v=sp.symbols('R u T a v', nonzero=True, real=True)
H,X,Y=sp.symbols('H X Y', real=True)
r1,r2,r3=sp.symbols('r1 r2 r3', real=True)

results={}

# Terminal relation matrix and exact adjugate factorization.
A=sp.Matrix([[R,-u],[4,-T]])
Adj=sp.Matrix([[T,-u],[4,-R]])
results['terminal_adjugate_difference']=sp.simplify(A*Adj-(R*T-4*u)*sp.eye(2))
assert results['terminal_adjugate_difference']==sp.zeros(2)

# Rank-one symmetric completion.
Gamma=sp.Matrix([[u,a],[a,v]])
results['rank_one_determinant']=sp.factor(Gamma.det())

# Koide orthogonal coordinates.
F=sp.Matrix([
    [1/sp.sqrt(3),1/sp.sqrt(3),1/sp.sqrt(3)],
    [1/sp.sqrt(2),0,-1/sp.sqrt(2)],
    [1/sp.sqrt(6),-2/sp.sqrt(6),1/sp.sqrt(6)],
])
r=sp.Matrix([r1,r2,r3])
L=F*r
QK=sp.Rational(2,3)*(r1+r2+r3)**2-(r1**2+r2**2+r3**2)
results['F_orthogonal']=sp.simplify(F*F.T)
results['QK_minus_Lorentz']=sp.simplify(QK-(L[0]**2-L[1]**2-L[2]**2))
assert results['F_orthogonal']==sp.eye(3)
assert results['QK_minus_Lorentz']==0

# Native and raw coefficient dictionaries.
t,m,b=sp.symbols('t m b', real=True)
Lnative=sp.Matrix([t+b/6,2*m,t-b/6])
Dmap=sp.Matrix([2*t,sp.sqrt(sp.Rational(2,3))*m,b/3])
PK_of_L=sp.Matrix([Lnative[0]+Lnative[2],Lnative[1]/sp.sqrt(6),Lnative[0]-Lnative[2]])
results['dictionary_commutator']=sp.simplify(PK_of_L-Dmap)
assert results['dictionary_commutator']==sp.zeros(3,1)
G=sp.Matrix([[2*t,2*m],[2*m,b/3]])
results['native_determinant_identity']=sp.factor(G.det()-sp.Rational(2,3)*(t*b-6*m**2))
assert results['native_determinant_identity']==0

# Selector state maps.
state_sub={t:u/2,m:a/2,b:3*v}
results['selector_G_minus_Gamma']=sp.simplify(G.subs(state_sub)-Gamma)
results['selector_native_discriminant']=sp.factor((t*b-6*m**2).subs(state_sub))
assert results['selector_G_minus_Gamma']==sp.zeros(2)
assert sp.simplify(results['selector_native_discriminant']-sp.Rational(3,2)*(u*v-a**2))==0

# Complement reflection in the original Koide coordinates.
WK=sp.Rational(1,3)*sp.Matrix([[2,2,-1],[2,-1,2],[-1,2,2]])
AQ=sp.Rational(2,3)*sp.ones(3)-sp.eye(3)
results['WK_squared']=sp.simplify(WK**2)
results['WK_orthogonal']=sp.simplify(WK.T*WK)
results['WK_determinant']=sp.factor(WK.det())
results['WK_QK_invariance']=sp.simplify(WK.T*AQ*WK-AQ)
assert results['WK_squared']==sp.eye(3)
assert results['WK_orthogonal']==sp.eye(3)
assert results['WK_determinant']==-1
assert results['WK_QK_invariance']==sp.zeros(3)

# Exact channel maps on Lorentz coordinates.
JL=sp.diag(1,-1,-1)
Bp=sp.Matrix([
    [(p**2+1)/2,0,(p**2-1)/2],
    [0,p,0],
    [(p**2-1)/2,0,(p**2+1)/2],
])
results['exterior_Lorentz_multiplier']=sp.simplify(Bp.T*JL*Bp-p**2*JL)
results['middle_Lorentz_multiplier']=sp.simplify((p*sp.eye(3)).T*JL*(p*sp.eye(3))-p**2*JL)
assert results['exterior_Lorentz_multiplier']==sp.zeros(3)
assert results['middle_Lorentz_multiplier']==sp.zeros(3)


# Exterior channel is p times a Lorentz boost of rapidity log(p).
Kboost=sp.Matrix([[0,0,1],[0,0,0],[1,0,0]])
results['cosh_log_identity']=sp.simplify(
    sp.cosh(sp.log(p))-(p+p**-1)/2
)
results['sinh_log_identity']=sp.simplify(
    sp.sinh(sp.log(p))-(p-p**-1)/2
)
boost_algebraic=sp.Matrix([
    [(p+p**-1)/2,0,(p-p**-1)/2],
    [0,1,0],
    [(p-p**-1)/2,0,(p+p**-1)/2],
])
results['boost_generator_lorentz_skew']=sp.simplify(Kboost.T*JL+JL*Kboost)
results['exterior_boost_factorization']=sp.simplify(Bp-p*boost_algebraic)
assert results['cosh_log_identity']==0
assert results['sinh_log_identity']==0
assert results['boost_generator_lorentz_skew']==sp.zeros(3)
assert results['exterior_boost_factorization']==sp.zeros(3)

# Exact quarter-coordinate composition under the exterior slope map theta -> theta/p.
theta_q=sp.symbols('theta_q', positive=True, real=True)
zetaE=-p*theta_q/(p+theta_q)**2
zetaMscaled=-(theta_q/p)/(1+theta_q/p)**2
results['quarter_channel_composition']=sp.simplify(zetaE-zetaMscaled)
assert results['quarter_channel_composition']==0

# Exact middle-channel shell bound factorization.
hh,rr,ss,kk=sp.symbols('hh rr ss kk', positive=True, integer=True)
pp=4*hh*rr*ss-R
middle_factor=sp.expand(pp+4-(4*kk-1)*R)
results['middle_shell_bound_factorization']=sp.factor(
    middle_factor.subs(kk,(rr+ss)/R)-4*((hh-1)*rr*ss+(rr-1)*(ss-1))
)
assert results['middle_shell_bound_factorization']==0

# Congruence-free formulas for the full shell and quarter coordinate.
d,e,N=sp.symbols('d e N', positive=True, real=True)
Ts=(d+e)/2
Ws=(d-e)/2
zeta_rhs=-sp.Rational(1,4)+sp.Rational(1,4)*(Ws/(Ts+N))**2
# Under de=N^2, the quarter coordinate equals -N/[2(Ts+N)].
results['quarter_identity_after_null_relation']=sp.factor(
    (zeta_rhs + N/(2*(Ts+N))).subs(e,N**2/d)
)
assert sp.simplify(results['quarter_identity_after_null_relation'])==0

# Positive-sector polynomial roots.
theta=sp.symbols('theta', positive=True, real=True)
poly=(1+sp.sqrt(2))*theta**2-2*sp.sqrt(3)*theta+(sp.sqrt(2)-1)
roots=sp.solve(poly,theta)
results['positive_sector_roots']=[sp.simplify(x) for x in roots]
expected=[(sp.sqrt(3)-sp.sqrt(2))/(1+sp.sqrt(2)),(sp.sqrt(3)+sp.sqrt(2))/(1+sp.sqrt(2))]
assert all(sp.simplify(x-y)==0 for x,y in zip(roots,expected))

serial={}
for k,val in results.items():
    if isinstance(val,list):
        serial[k]=[str(x) for x in val]
    else:
        serial[k]=str(val)

out=Path(__file__).with_name('symbolic_verification_results.json')
out.write_text(json.dumps(serial,indent=2)+'\n',encoding='utf-8')
print(json.dumps(serial,indent=2))
