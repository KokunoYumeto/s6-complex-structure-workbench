"""Exact characteristic-number identities for Proposition B.6.15."""
import json
from pathlib import Path
import sympy as S
k, ell, r, eps = S.symbols('k ell r eps', nonzero=True)
p1sq=(ell+k)**2/k
mu=S.factor((p1sq-4*eps)/896-(ell+k)/192+k/384)
expected=(3*ell**2/k-8*ell-4*k-12*eps)/2688
assert S.simplify(mu-expected)==0
spin=S.factor(mu.subs(ell,4*k+24*r))
spin_expected=(k-eps+32*r+144*r*r/k)/224
assert S.simplify(spin-spin_expected)==0
index=S.factor(k/S.Integer(6)-ell/S.Integer(24))
assert S.simplify(index-(4*k-ell)/24)==0
out={'disk_p1_squared':str(p1sq),'disk_p1_z_squared':str(ell+k),'disk_z_fourth':str(k),'disk_signature':'sign(k)', 'mu':str(mu),'spin_substitution':str(spin),'twisted_spin_Dirac_index':str(index),'zero_shear_zero_p1':'all relative characteristic products and signature zero', 'scope':'Conditional model only; actual k, ell and fixed-curve surgery trace correction remain unknown.'}
path=Path(__file__).with_suffix('.out.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
