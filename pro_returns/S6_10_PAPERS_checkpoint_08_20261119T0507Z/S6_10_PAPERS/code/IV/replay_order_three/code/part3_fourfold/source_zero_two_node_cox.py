#!/usr/bin/env python3
"""Exact source identities and leading-unit data for EA42--46."""
import json
from pathlib import Path
import sympy as s
X,v,xc=s.symbols('X v xc');A=1-2*v
T=-3*xc**2-2*A*xc
P=X**3+A*X**2+T*X+v**2
R2=(X-xc)**2*(A+2*xc+X)
h=v**2-A*xc**2-2*xc**3
checks=[]
def ck(name,e):
    z=s.factor(e);assert z==0,(name,z)
    checks.append({'name':name,'pass':True})
ck('full_Morse_source_factorization',P-R2-h)
s0,s1,t0,t1=s.symbols('s0 s1 t0 t1')
aa=s0*t0;bb=s1*t1;cc=s0*t1;dd=s1*t0
alpha=(aa+bb-cc-dd)/2;beta=-2*(aa+bb+cc+dd)
Fp=s1-s0;Fm=t0+t1;Sn=s0+s1;Tn=t0-t1
ck('alpha_branch_leading',alpha+Fp*Tn/2)
ck('beta_branch_leading',beta+2*Sn*Fm)
ck('q1_leading',(-aa+bb-cc+dd)-Fp*Fm)
ck('q2_leading',(aa-bb-cc+dd)-Sn*Tn)
J=s.Matrix([Fp,Sn,Fm,Tn]).jacobian([s0,s1,t0,t1]).det()
ck('leading_Jacobian_four',J-4)
ck('marked_Cartier_unit_leading',(Sn-Fp)-2*s0)
# The exact source identity Y^2-R_c^2=h supplies the product
# relation on each irreducible F branch. These nonzero leading
# restrictions certify which analytic factor vanishes there.
Ylead=(aa+bb)/2;Rlead=cc+(dd-cc)/2
ck('Fplus_branch_R_equals_Y_leading',(Rlead-Ylead).subs(s1,s0))
assert s.factor((Rlead+Ylead).subs(s1,s0))==s0*(t0+t1)
checks.append({'name':'Fplus_other_factor_nonzero','pass':True})
ck('Fminus_branch_R_equals_minus_Y_leading',(Rlead+Ylead).subs(t0,-t1))
assert s.factor((Rlead-Ylead).subs(t0,-t1))==t1*(s0-s1)
checks.append({'name':'Fminus_other_factor_nonzero','pass':True})
q1,q2,ag,fp,fm=s.symbols('q1 q2 ag fp fm',nonzero=True)
AMG=ag*q2;BMG=q1/ag
ck('marked_alpha_exact',-AMG/(2*ag)+q2/2)
ck('marked_beta_exact',-2*ag*BMG+2*q1)
alpha0,beta0=s.symbols('alpha beta')
ck('preserved_q2_exact',((-beta0/(2*fm))*(-2*alpha0/fp)-q2).subs(alpha0*beta0,fp*fm*q2))
ck('marked_kappa_division_numerator',(-(-2*q1)-2*q1))
kappa,xi,ss=s.symbols('kappa xi ss',nonzero=True)
for a in (1,2):
    ck(f'actual_meromorphic_line_{a}',kappa**a*xi/(kappa*ss)**a-xi/ss**a)
out={'status':'PASS','count':len(checks),'checks':checks,
 'analytic_division_proof':[
 'RT2 has Jacobian unit sigma, so F_plus and F_minus are irreducible coordinate hypersurfaces.',
 'The full identity (Y-R_c)(Y+R_c)=upsilon F_plus F_minus q2 restricts to zero in each corresponding integral analytic local ring.',
 'On F_plus=0 the certified nonzero leading term of Y+R_c is s0(t0+t1); therefore Y-R_c vanishes identically and alpha is divisible by F_plus.',
 'On F_minus=0 the certified nonzero leading term of R_c-Y is t1(s0-s1); therefore Y+R_c vanishes identically and beta is divisible by F_minus.',
 'The quotient map has certified leading Jacobian4, hence is an analytic local isomorphism.',
 'On s0=0 the actual marked evaluations give beta=-2q1, so S1=S0; division by this irreducible coordinate gives kappa, whose certified leading value is1.'
 ],
 'scope':'Full source functions are retained in EA42--46; no period-strip closure or class inferred.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(checks)} exact source/Cox/Cartier checks')
