#!/usr/bin/env python3
"""Independent exact local normal-form algebra for the prereading comparison."""
from pathlib import Path
import sympy as s,json
X,Y,Z,A,B,C,a,b,c=s.symbols('X Y Z A B C a b c')
p=Y**3+A*Y**2+B*Y+C
depressed=s.expand(p.subs(Y,Y-A/3))
expected=Y**3+(B-A**2/3)*Y+C-A*B/3+2*A**3/27
assert s.expand(depressed-expected)==0
actual=s.factor(depressed.subs({A:X*a,B:X**2*b,C:X**2*c})-Y**3)
assert s.rem(actual,X**2,X)==0
beta=b-a**2/3;gamma=c-X*a*b/3+2*X*a**3/27
assert s.expand(actual-X**2*(beta*Y+gamma))==0
pinch=X**2+Y**2*Z;cusp=Y**3+X**2*Z
Hp=s.hessian(pinch,(X,Y));Hc=s.hessian(cusp,(X,Y))
assert Hp.subs({X:0,Y:0})==s.diag(2,2*Z)
assert Hc.subs({X:0,Y:0})==s.diag(2*Z,0)
assert Hp.subs({X:0,Y:0,Z:0}).rank()==1
assert Hc.subs({X:0,Y:0,Z:0}).rank()==0
assert s.expand((X+s.I*Y)*(X-s.I*Y)-(X**2+Y**2))==0
out={'status':'PASS','written_before_target_proof_and_old_producing_code':True,
 'depressed_cubic':str(depressed),'divisible_remainder':str(actual),
 'beta':str(beta),'gamma':str(gamma),
 'pinch_transverse_Hessian':str(Hp.subs({X:0,Y:0})),
 'cusp_transverse_Hessian':str(Hc.subs({X:0,Y:0})),
 'scope':'Exact coordinate identities only. Uniform boundary transversality, proper discriminant and sphere transport are established in CR4_UN9_before_read.md and are not numerical claims.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
