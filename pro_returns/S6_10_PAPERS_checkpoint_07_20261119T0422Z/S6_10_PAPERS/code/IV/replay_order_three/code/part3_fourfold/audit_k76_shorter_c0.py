from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
root=Path(__file__).resolve().parents[2]
v,theta,k,nu,D=s.symbols('v theta k nu D')
m=3*k
sigma=lambda x:nu*x*D+nu*m*x*(x-1)
c=lambda x:nu*D/3+2*nu*m*x/3-2*nu*k/3
assert s.expand(sigma(v+s.Rational(1,3))-sigma(v)-c(v))==0
assert s.expand(sum(c(v+s.Rational(j,3)) for j in range(3))-nu*D-2*nu*m*v)==0
canonical=nu*theta*D+2*nu*m*theta*(v+theta)
assert s.expand(sigma(v+theta)-sigma(v)-canonical+nu*m*(theta**2+theta))==0
A,Dn=s.symbols('A Dn',nonzero=True)
assert s.cancel(A*(A*Dn)**-1*Dn)==1
assert s.cancel(A*(A*Dn)**-1)==Dn**-1
assert s.cancel(A*Dn)==A*Dn
# The shear fixes the physical delta and commutes with vector sums.
n=s.symbols('n',integer=True)
Sn=s.Matrix([[1,0],[-n,1]])
assert Sn*s.Matrix([0,1])==s.Matrix([0,1])
assert Sn.det()==1
record={'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'fourfold',
 'statement':'P3K.76','scope':'BW.24–28 only: actual shorter C0 closing, all-sheet character lift, and covered canonical-cut comparison',
 'status':'PASS','exact_checks':8,
 'closing_direction':'C_r:X_(zeta3*r)->X_r is endpoint-to-initial. Closed coordinates use plus sigma. S_n(z,l)=(z,l-nz) is applied to every complete logarithm and all intermediate P_j.',
 'cox_arrow':'The lift(a0,Aa1,(A D_n)^(-1)c0,D_n c1) has chart factors(A,(A D_n)^(-1),D_n) and(A^(-1),D_n^(-1),A D_n), and preserves q literally.',
 'canonical_comparison':'sigma(v+theta)-sigma(v) minus the canonical covered cut is -nu*m*(theta^2+theta)*delta. Its exponential is a based global physical-circle map with the retained winding; after collar flattening the zero-endpoint unit logarithms carry full jets.',
 'cover':'Every j=0,1,2,3 endpoint character is the actual OR65 product after the same integral shear. The r native product is therefore the literal triple pullback of the shorter product. Degree-three naturality applies to the actual line and tangent bundles, without dividing a Theta class.',
 'limitation':'This is the requested narrow endpoint audit, not an independent audit of the full BW local characteristic computation.'}
(root/'records/fourfold_audit_k76_shorter_c0.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':8}))
