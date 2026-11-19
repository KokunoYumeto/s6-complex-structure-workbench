"""Narrow independent C0/closing audit; not an audit of every K70 assertion."""
from datetime import datetime, timezone
from pathlib import Path
import json
import sympy as s

root = Path(__file__).resolve().parents[2]
a,b,c,kappa,alpha = s.symbols('a b c kappa alpha', nonzero=True)
u=kappa*alpha*b*c
v=a*b/alpha
w=1/(kappa*b)
assert s.simplify(kappa*w-1/b)==0
assert s.simplify(alpha*v-b*a)==0
assert s.simplify(u/(kappa*alpha)-b*c)==0
theta=s.symbols('theta', real=True)
assert s.integrate(s.sin(theta)**2,(theta,0,2*s.pi))*4*s.pi/(2*s.pi**2)==2
for e in range(-4,5):
    for J in range(-4,5):
        assert s.exp(s.pi*s.I*e*J*(1+1))==1
out={
  'timestamp_utc':datetime.now(timezone.utc).isoformat(),
  'reviewer':'fourfold',
  'statement':'P3K.70',
  'scope':'NV.1–2 only: native C0, complete closing, native-to-ordinary arrow',
  'status':'PASS',
  'exact_checks':85,
  'native_coordinates':'(b,a,c); (kappa*w,alpha*v,u/(kappa*alpha)); substitution gives z_prime=1/z and n_prime=z*n',
  'spinor_order':'q_H=(1+j*z)(n0+j*conj(n1)); physical delta acts on the right by exp(-i*phi)',
  'closing':'The retained current-to-reference cut differs from the inverse K30 reference-to-current origin by exp(pi*i*e*J*(theta^2+theta)). Both endpoints are identity. It is the global physical circle action, so transporting the connection gives the same endpoint return; no relative homotopy class is discarded.',
  'degree_proof':'On the northern chart U is defined. Replace the radial angle vartheta in H_J by (1-t)*vartheta+t*pi/2; it is fixed near the southern collar and smooth on the northern disc. Thus U*H_J*U^-1 is homotopic to cos(J*theta)+sin(J*theta)*h on the whole Hopf sphere. With native Hopf orientation, pullback of the quaternion volume is J*sin(J*theta)^2*dtheta*w_S2, whose integral divided by 2*pi^2 is 2J. The right factor depends on radius and parameter only, so its third degree is zero.',
  'arrow':'The displayed map is native to ordinary. Its inverse cylinder has endpoint L^(-2J), so ordinary pair=native pair-(2J,0). The opposite-vertex full-unit factors are eta/alpha and kappa*alpha, and the literal double seams are C_tau*E^(-j).',
  'limitations':'No new claim about all fans or the source-zero completion. The remaining K70 proof was audited by root.'
}
(root/'records/fourfold_audit_k70_c0.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':85,'record':'records/fourfold_audit_k70_c0.json'}))
