"""Postrelease exact polynomial certificate, separate from the printed reciprocal bound."""
from pathlib import Path
import sympy as s, json, datetime, os
k,l,x,y=s.symbols('k l x y', positive=True)
A=12*k*l;D=k*l-3*k-4*l
ratio_residual=s.cancel(D/A-(s.Rational(1,12)-1/(4*l)-1/(3*k)))
positive=s.Poly(s.expand((D+A).subs({k:x+1,l:y+1})),x,y)
assert ratio_residual==0
assert all(c>0 for c in positive.coeffs())
assert positive.coeff_monomial(1)==6
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'timing':'After target release; prerelease hand derivation already frozen.','method':'Translate the integer quadrant by k=x+1,l=y+1, expand D+A in the nonnegative monomial basis, and verify every coefficient is positive. The printed proof instead estimates the two reciprocal terms separately.','ratio_identity_residual':str(ratio_residual),'D_plus_A':str(positive.as_expr()),'monomials_and_coefficients':[[list(m),int(c)] for m,c in positive.terms()],'constant_lower_bound':6,'conclusion':'For integers k,l>=1, D+A>=6>0, hence D/A>-1. This gives the contradiction to the analytic D<-A bound.','historical_routine':'No historical program is cited in the target proof; no historical-program read or rerun is claimed.','events_added':0}
p=Path(__file__).with_suffix('.json');tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');os.replace(tmp,p);print(json.dumps(out,indent=2))
