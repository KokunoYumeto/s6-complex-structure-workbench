#!/usr/bin/env python3
"""Exact literal scalar/cap/Albanese endpoint audit for P3K.36."""
from pathlib import Path
import json, datetime
import sympy as s
R=Path(__file__).resolve().parents[2]
D=s.Matrix([[1,1,0,0],[-2,-1,-1,0],[0,0,1,0],[0,0,0,1]])
delta=s.Matrix([-1,0,2,0]); gamma=s.Matrix([0,0,0,1])
assert D**4==s.eye(4)
assert D*delta==delta and D*gamma==gamma
assert (D-s.eye(4)).rank()==2
U=s.eye(4)+delta*gamma.T
assert U*gamma==gamma+delta and U*D==D*U
norm=sum((D**j for j in range(4)),s.zeros(4))
assert norm*(gamma/4)==gamma
assert U*(gamma/4)-gamma/4==delta/4
# Exact complex lattice and root deck, with tau retained symbolically.
tau=s.symbols('tau'); ii=s.I
L=s.Matrix([[2,1+ii,1,0],[0,0,s.Rational(1,2),tau]])
assert s.simplify(s.diag(-ii,1)*L-L*D)==s.zeros(2,4)
assert L*delta==s.Matrix([0,1])
assert L.subs(tau,tau+1)==L*U
assert L*gamma==s.Matrix([0,tau])
# The Albanese periods are second-coordinate lattice periods plus R's shift.
# Normalize by 1/2: the new ratio is tau/2 + 2*kappa.
kappa=s.symbols('kappa')
periods=[s.Integer(0),s.Integer(0),s.Rational(1,2),tau,tau/4+kappa]
assert s.expand(4*periods[-1]-tau)==4*kappa
assert s.simplify(((tau+1)/4+kappa)/(s.Rational(1,2))-(tau/4+kappa)/(s.Rational(1,2)))==s.Rational(1,2)
q=s.symbols('q'); N=9
E4=1+240*sum(s.divisor_sigma(n,3)*q**n for n in range(1,N+2))
E6=1-504*sum(s.divisor_sigma(n,5)*q**n for n in range(1,N+2))
num=s.series(1728*E4**3,q,0,N+2).removeO()
den=s.series(E4**3-E6**2,q,0,N+2).removeO()
assert den.coeff(q,1)==1728
F=s.series(num/(den/q),q,0,6).removeO()
assert F.subs(q,0)==1
j=s.expand(F/q)
difference=s.expand(q*(j-j.subs(q,-q)))
assert difference.subs(q,0)==2
S=s.symbols('S'); k=s.Integer(-3); ell=s.Integer(-12)
index=s.Rational(4*k-ell,24)
assert index==0
fan=index+ell*(S-1)/8-k*(S*S-1)/8
assert s.factor(fan)==3*(S-3)*(S-1)/8
assert -ell/4==3 and -(4*k-ell)/4==0
out={'statement':'P3K.36','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS',
'deck':list(map(list,D.tolist())),'delta':list(delta),'parameter_shear':U.tolist(),
'central_lattice':[[str(v) for v in row] for row in L.tolist()],
'Albanese_periods':['1/2','tau/4+kappa'],'Albanese_Tate_parameter':'exp(4*pi*i*kappa)*sqrt(c*u)',
'one_turn':'tau -> tau+1; a -> a+delta/4; Q_Alb -> -Q_Alb',
'q_times_j_difference_series':str(difference),'j_series':str(j),
'corrected_parameter':'u=w^2','corrected_pair':[-3,-12],'relative_pair':[3,0],
'fan_class':str(s.factor(fan)),'proof':'notes/part3_liu_rollenske_parameter.md'}
(R/'code/part3/liu_rollenske_parameter.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print('PASS: exact deck, invariant lattice, scalar shear, affine norm, Albanese periods and j branch change.')
print('j(q) =',j)
print('q*(j(q)-j(-q)) =',difference)
print('Corrected u=w^2; (k,ell)=(-3,-12); fan class=',s.factor(fan))
