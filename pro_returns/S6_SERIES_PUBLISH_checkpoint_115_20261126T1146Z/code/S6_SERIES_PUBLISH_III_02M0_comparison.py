#!/usr/bin/env python3
"""Post-release M0 comparison: explicit cutoffs, branch maps and joint base.

This is comparison evidence, not an additional independent target check.
The frozen derivation preceded release at 2026-11-23T20:10:44Z.
"""
from datetime import datetime, timezone
import sympy as S

u=S.symbols('u',nonzero=True)
ap,bp,r,a,b,t,A,Z,Y,B,Xold,Vold=S.symbols('ap bp r a b t A Z Y B Xold Vold')
# Ordered coordinates in the printed node are (x,y,z_old,v_old).
# theta exchanges the two elliptic-node branches z_new and v_new.
old_chart_A=S.Matrix([A*Z,Y,Z,A*Y/u])
old_chart_B=S.Matrix([Xold,B*Vold,B*Xold,Vold/u])
fresh_chart_1_after_theta=S.Matrix([u*ap*r,bp,ap,bp*r])
fresh_chart_0_after_theta=S.Matrix([u*a,b*t,a*t,b])
assert S.simplify(old_chart_A.subs({A:u*r,Z:ap,Y:bp},simultaneous=True)-fresh_chart_1_after_theta)==S.zeros(4,1)
assert S.simplify(old_chart_B.subs({B:t/u,Xold:u*a,Vold:u*b},simultaneous=True)-fresh_chart_0_after_theta)==S.zeros(4,1)
inverse_A={r:A/u,ap:Z,bp:Y}
inverse_B={t:u*B,a:Xold/u,b:Vold/u}
assert S.simplify(fresh_chart_1_after_theta.subs(inverse_A,simultaneous=True)-old_chart_A)==S.zeros(4,1)
assert S.simplify(fresh_chart_0_after_theta.subs(inverse_B,simultaneous=True)-old_chart_B)==S.zeros(4,1)
fresh_transition={ap:a*t,bp:b*t,r:1/t}
assert S.simplify(fresh_chart_1_after_theta.subs(fresh_transition,simultaneous=True)-fresh_chart_0_after_theta)==S.zeros(4,1)
old_transition={B:1/A,Xold:A*Z,Vold:A*Y}
assert S.simplify(old_chart_B.subs(old_transition,simultaneous=True)-old_chart_A)==S.zeros(4,1)
print('PASS both printed resolution charts and their inverses after the explicit z/v branch exchange')
print('PASS fresh and printed overlap maps agree under the branch exchange')
branch=S.Matrix([[1,0,0],[0,-1,1],[0,0,1]])
assert branch*branch==S.eye(3) and branch.det()==-1
ray1=S.Matrix([1,0,1]);ray2=S.Matrix([0,1,1])
assert branch*ray1==S.Matrix([1,1,1])
assert branch*ray2==S.Matrix([0,0,1])
print('PASS branch character involution (X,z,q)->(X,q/z,q), determinant -1, and exact diagonal endpoints')
q,s,x,y,z,v=S.symbols('q s x y z v')
joint=S.Matrix([q,u*(q-s)])
assert joint.jacobian((q,s)).det()==-u
inverse={q:z*v,s:z*v-x*y/u}
assert S.simplify(joint.subs(inverse,simultaneous=True)-S.Matrix([z*v,x*y]))==S.zeros(2,1)
assert S.expand((x*y-u*(z*v-s)).subs(s,z*v-x*y/u))==0
regular=S.Matrix([s+x*y/u,s])
assert S.simplify((regular[0]-regular[1])-x*y/u)==0
print('PASS joint-base coordinates (Q,R)=(q,u*(q-s))=(z*v,x*y), with inverse s=Q-R/u')
print('PASS smooth-zero chart q=s+x*y/u and its nodal-curve projection')
printed_r=S.Rational(1,5)
fresh_a=S.Rational(1,4);fresh_b=S.Rational(1,2)
delta=S.Rational(1,32)
assert 0<printed_r<fresh_a<2*printed_r<fresh_b<1
assert delta<printed_r**2 and delta<fresh_a**2
assert delta/printed_r<fresh_b
assert printed_r<fresh_a and 1/fresh_a<1/printed_r
assert printed_r<2*printed_r<fresh_b<1/printed_r
assert printed_r<1/fresh_b<1/(2*printed_r)<1/printed_r
assert 3*printed_r/2<7*printed_r/4<2*printed_r
assert delta/(3*printed_r/2)<7*printed_r/4
print('PASS printed r=1/5 and fresh (a,b)=(1/4,1/2) have inverse collar identifications')
print('PASS all printed and fresh compact-representative bounds at delta=1/32')
for m in (3,4):
    for n in range(0,4*m+1):
        quotient,remainder=divmod(n,m)
        assert 0<=remainder<m and n==m*quotient+remainder
    print(f'PASS root exponent decomposition t=sigma^{m}, basis 1,...,sigma^{m-1}')
print('ALL POST-RELEASE M0 COMPARISON IDENTITIES PASS')
print('Completed UTC:',datetime.now(timezone.utc).isoformat())
