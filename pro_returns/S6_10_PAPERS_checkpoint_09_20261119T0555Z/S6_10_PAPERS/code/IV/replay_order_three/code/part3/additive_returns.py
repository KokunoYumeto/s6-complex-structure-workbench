#!/usr/bin/env python3
"""Exact physical ±norm identities and all one-cap page arithmetic."""
from pathlib import Path
import json
from math import gcd
import sympy as S

s,v,t,m,g,C=S.symbols('s v theta m g C')
delta=S.Matrix([0,1]);gamma=S.Matrix([g,-C-s-m*v])
clean=lambda x:x.applyfunc(S.simplify)
zero=S.zeros(2,1)
for n in [1,-1]:
 o=n*S.Matrix([-g*s/m,C*s/m+s*s/(2*m)+s*v])
 sigma=n*S.Matrix([g*v,-C*v-m*(v*v-v)/2])
 assert clean(o.subs(v,v+1)-o-n*s*delta)==zero
 assert clean(sigma.subs(v,v+1)-sigma-n*s*delta-n*gamma)==zero
 assert clean(o.subs(s,s+2*m)-o+2*n*gamma-2*m*n*delta)==zero
 F=sigma-o
 angular=clean(F.subs(v,v+t)-F)
 assert clean(angular-n*t*gamma+n*m*t*(t-1)*delta/2)==zero
 assert clean(angular.subs(s,s+2*m)-angular+2*m*n*t*delta)==zero
 alpha,Gamma=S.symbols('alpha Gamma')
 u=m*Gamma-n*alpha
 assert S.simplify(alpha/m+n*u/m-n*Gamma)==0
 assert n*n==1

l=S.symbols('l',integer=True,nonnegative=True)
raw=[
 ('E7-A/B reduced III',2,2,1,9,3,4*l+3,0,-3*l-2),
 ('E7-A/B good',2,1,2,9,0,4*l,1,S.Integer(0)),
 ('E6-A/B reduced IV',6,6,1,8,4,3*l+2,0,-8*l-5),
 ('E6-A/B good',6,2,3,8,0,3*l,1,S.Integer(0)),
 ('OS47 reduced III',14,14,1,3,3,4*l+1,0,-25*l-6),
 ('OS47 good III',14,7,2,3,0,4*l,1,-4*l),
 ('OS56 reduced III',30,30,1,3,3,4*l+1,0,-57*l-14),
 ('OS56 good III',30,15,2,3,0,4*l,1,-12*l),
 ('OS56 reduced IV',30,30,1,4,4,3*l+1,0,-43*l-14),
 ('OS56 good IV',30,10,3,4,0,3*l,1,-3*l),
]
for row,d in [(45,8),(47,14),(55,20)]:
 raw.extend([
  (f'OS{row} reduced II',d,d,1,2,2,6*l+1,0,-(3*d-5)*l+1-S.Rational(d,2)),
  (f'OS{row} good II',d,d,1,2,0,6*l,1,-(3*d-5)*l)])
out=[]
for label,d,a,b,e,er,mm,first,expected in raw:
 assert a*b==d
 chi=S.expand((mm*(12-e)+er)/12)
 height=S.expand(mm*S.Rational(a*a,d))
 PO=S.expand(height/2-chi);square=-height
 A_U=S.expand((12*square+24*chi)/24)
 assert S.simplify(A_U-expected)==0
 A=-A_U
 assert S.simplify(A-height/2+chi)==0
 assert S.simplify(square+2*chi+2*PO)==0
 slope=int(S.expand(A).coeff(l))
 period=1 if slope==0 else 28//gcd(abs(slope),28)
 residues=[int(A.subs(l,k))%28 for k in range(first,first+period)]
 out.append(dict(label=label,d=d,a=a,b=b,n_values=[1,-1],m=str(mm),
                 first_l=first,source_euler=e,root_euler=er,chi=str(chi),
                 height=str(height),line_square=str(square),section_intersection=str(PO),
                 auxiliary_dual_line_index=str(A_U),
                 actual_positive_return=str(A),residue_period=period,residues=residues,
                 physical_sign_map='P3K.68: actual physical circle line M=U^*, Sigma=lambda_M=-lambda_U; A_phys=H/2-chi',
                 scalar_parameter='lambda=r^m, one positive r loop',
                 proof='notes/part3_additive_returns_working.md; actual source/line and signed Thom comparisons required'))
 print(label,'m=',mm,'chi=',chi,'M²=',square,'PO=',PO,'A=',A,'residues=',residues)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
 status='PASS',scope='Exact arithmetic supplement to the actual map/line/Thom proof; no numerical substitution for those maps.',
 n_signs_same_by='actual beta=n*gamma_out and positive parameter n*gamma_out, with positive meridian U; K68 carries its dual to the actual physical circle line M',
 cases=out),indent=2)+'\n')
print('PASS: both physical norm signs, exact angular gauges, all sixteen root/arithmetic rows.')
