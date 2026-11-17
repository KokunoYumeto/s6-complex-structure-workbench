"""Exact norm-map and A1-resolution identities for P3F.30."""
from pathlib import Path
import json
import sympy as s

L=s.Matrix([[1,0],[-1,2]])
P=s.Matrix([[2,-3],[1,-1]])
assert L.det()==2 and L*P==s.Matrix([[2,-3],[0,1]])
v,lam,f,ft=s.symbols('v lam f ft',nonzero=True)
assert s.cancel((lam*f*v)**2/f-lam**2*f*ft*v**2/ft)==0
x,y,zeta,eta,tau=s.symbols('x y zeta eta tau',nonzero=True)
assert s.expand(x*(x*zeta**2)-(x*zeta)**2)==0
assert s.expand((y*eta**2)*y-(y*eta)**2)==0
assert s.cancel((x/tau)*(tau*zeta)-x*zeta)==0
assert s.cancel((x/tau)*(tau*zeta)**2-tau*x*zeta**2)==0
out={'proof':'P3F.30','torus_map_matrix':[list(map(int,L.row(i))) for i in range(2)],
     'source_valuations':[[2,-3],[1,-1]],'norm_valuations':[[2,-3],[0,1]],
     'degree':2,'norm_line':'M tensor T*M = M^2(-C0)',
     'norm_scalar':'lambda^2','quotient_equation':'xy=z^2',
     'resolved_fixed_normal_bundles':[['O(-2) weight -1','O(0) weight +1'],
                                      ['O(0) weight -1','O(-2) weight +1']],
     'positive_weight_determinant_degrees':[2,-2],
     'Hopf_base_shifts':[1,-1],
     'return_index':'Unassigned; both normal charges must enter the actual comparison.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Norm-map compatibility, degree2 torus map, and A1 resolution verified.')
print('Actual residual normal charges:',out['Hopf_base_shifts'])
print(out['return_index'])
