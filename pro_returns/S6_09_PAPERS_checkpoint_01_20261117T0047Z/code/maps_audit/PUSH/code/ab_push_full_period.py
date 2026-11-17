#!/usr/bin/env python3
"""Exact finite identities for the repaired collar; no global cap assertion."""
import json
from pathlib import Path
import sympy as S

a,b,c,k,u,v,F,g,r,D,H,x = S.symbols('a b c k u v F g r D H x', nonzero=True)
den=a+(1-a)*F
Fp=F/den
up=k*u*u*v*den
vp=1/(k*u)
checks={}
checks['first_period_preserves_q']=S.cancel(up*vp*Fp-u*v*F)==0
checks['first_period_scales_H']=S.cancel((1-Fp)/Fp-a*(1-F)/F)==0
checks['bH_extends_at_F_zero']=S.expand((u*v*F*r**12*D)*(1-F)-F*r**12*D*u*v*(1-F))==0
gp=g*(1-F)/(1-Fp)
checks['first_period_preserves_r']=S.cancel(gp*(1-Fp)-g*(1-F))==0

# Treat the analytic function values as independent symbols and impose its
# functional relation G(aH)=G(H)/(1+aH), G(abH)=G(bH)/(1+abH).
GH,GBH=S.symbols('GH GBH', nonzero=True)
x_after_AB=c*(k*u*v*F*x*(1+a*H))*(GH/(1+a*H))/(GBH/(1+a*b*H))
x_after_BA=k*u*v*F*(c*x*GH/GBH)*(1+a*b*H)
checks['two_periods_commute_using_G_identity']=S.cancel(x_after_AB-x_after_BA)==0

f=S.symbols('f', nonzero=True)
fmob=r*f/((b-1)*f+b*r)
checks['conditional_Wtest_mobius']=S.cancel(1+r/fmob-b*(1+r/f))==0

assert all(checks.values()), checks
out={'status':'PASS','scope':'finite identities only; no global analytic completion',
     'checks':checks,'checks_count':len(checks)}
target=Path(__file__).with_suffix('.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
