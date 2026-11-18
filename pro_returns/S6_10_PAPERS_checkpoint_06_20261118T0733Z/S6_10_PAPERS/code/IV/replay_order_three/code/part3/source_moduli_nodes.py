#!/usr/bin/env python3
"""Exact selected-node parameter and local-coordinate identities."""
from pathlib import Path
from datetime import datetime,timezone
import json
from itertools import product
import sympy as S
u,x,X,y,q=S.symbols('u x X y q',nonzero=True)
r=(1-2*u**3)/(3*u**2)
t0=u**2-2/u
P=x**3+3*r*x**2+t0*x+1
assert S.factor(P-(x-u)**2*(x+u**-2))==0
assert S.factor(S.diff(r,u)+2*(1+u**3)/(3*u**3))==0
assert S.factor(S.diff(t0,u)-2*(1+u**3)/u**2)==0
a=u+u**-2
assert S.factor(P.subs(x,X+u)+q*(X+u)-
                (X**2*(X+a)+q*(X+u)))==0
q_actual=(y*y-X*X*(X+a))/(X+u)
xi=(y-X*S.sqrt(X+a))/S.sqrt(X+u)
eta=(y+X*S.sqrt(X+a))/S.sqrt(X+u)
assert S.factor(xi*eta-q_actual)==0
J=S.Matrix([[S.diff(v,w) for w in (X,y)] for v in (xi,eta)])
J0=S.simplify(J.det().subs({X:0,y:0}))
assert S.simplify(J0+2*S.sqrt(a)/u)==0
ap=S.diff(a,u)
num=S.together(ap-3).as_numer_denom()[0]
assert S.rem(S.Poly(num,u),S.Poly(u**3+1,u)).as_expr()==0
tt,rr=S.symbols('t r')
Delta=-4*tt**3+9*rr**2*tt**2+54*rr*tt-108*rr**3-27
fs=S.factor((tt-3*rr**2).subs({tt:t0,rr:r}))
Dt=S.factor(S.diff(Delta,tt).subs({tt:t0,rr:r}))
assert S.factor(fs+a*a/3)==0
assert S.factor(Dt+4*u*a**3)==0
assert S.factor(-6912*fs**3/Dt+64*a**3/u)==0
rho,XX,YY,QQ,aa=S.symbols('rho Xtilde Ytilde Q a')
selected=y**2-X**2*(X+aa)-q*(X+u)
zoom=S.expand(selected.subs({X:rho**2*XX,y:rho**3*YY,
                            q:rho**6*QQ,aa:rho**2})/rho**6)
assert S.expand(zoom-(YY**2-XX**2*(XX+1)-QQ*(u+rho**2*XX)))==0
assert S.factor(S.discriminant(XX**3+XX**2+u*QQ,XX)+u*QQ*(4+27*u*QQ))==0
Z,V,QT,PP,gg,lam=S.symbols('Z V qT P g scalar',nonzero=True)
node=lambda z,v:(QT/z,v)
old_deck=(QT*Z,PP*V)
new_inverse_deck=lambda z,v:(z/QT,PP*v)
assert all(S.simplify(a-b)==0 for a,b in zip(node(*old_deck),new_inverse_deck(*node(Z,V))))
old_B=(Z/gg,lam*V)
new_B=lambda z,v:(gg*z,lam*v)
assert all(S.simplify(a-b)==0 for a,b in zip(node(*old_B),new_B(*node(Z,V))))
assert all(S.simplify(a-b)==0 for a,b in zip(node(*node(Z,V)),(Z,V)))
height=S.Matrix([[-1,0,1],[0,1,0],[0,0,1]])
assert height**2==S.eye(3)
assert height*S.Matrix([0,1,0])==S.Matrix([0,1,0])
J=S.diag(-1,1)
assert J.applyfunc(lambda x:int(x)%2)==S.eye(2)
edge_cases=0
for vals in product(range(2),repeat=4):
    mat=S.Matrix(2,2,vals)
    if int(mat.det())%2!=1: continue
    vv=mat[:,0];ww=mat[:,1]
    classes={tuple(int(x)%2 for x in vec) for vec in (vv,ww,vv+ww)}
    assert classes=={(1,0),(0,1),(1,1)}
    edge_cases+=1
assert edge_cases==6
out=dict(status='PASS',timestamp_utc=datetime.now(timezone.utc).isoformat(),
         proof='notes/part3_source_moduli_loops_working.md',
         r=str(r),selected_node_value=str(t0),factorization=str(S.factor(P)),
         node_chart_product=str(q_actual),Jacobian=str(J0),
         selected_cusp_locus='u^3=-1',
         endpoint_node_chart='(xi,eta) -> (eta,xi)',
         source_f_at_node=str(fs),source_Delta_t_at_node=str(Dt),
         j_pole_coefficient=str(S.factor(-6912*fs**3/Dt)),
         actual_Tate_Cartier_map='(Z,V,qT) -> (qT/Z,V,qT)',
         height_matrix=[list(map(int,row)) for row in height.tolist()],
         mod2_unimodular_edge_cases=edge_cases,
         double_cover_zoom=str(zoom),
         unresolved='Actual smooth relative boundary transport and the return of the closed double source loop; global punctures u=0,infinity.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: selected-node normalization, exact node and Tate/Cartier maps, height reflection, all six mod2 edge bases, and the literal (2,3,6) zoom.')
