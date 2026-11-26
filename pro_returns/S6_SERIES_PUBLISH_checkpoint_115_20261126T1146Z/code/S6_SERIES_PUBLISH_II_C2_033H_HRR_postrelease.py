"""Post-release exact recomputation of the Riemann--Roch coefficient in 033H.
Written from the splitting-principle definitions of ch and td; no earlier
program or output is read. This supplements the already frozen proof.
"""
import sympy as sp
import json
from pathlib import Path
x,y,z,t=sp.symbols('x y z t'); roots=(x,y,z)
ch=sum(sum((r*t)**j/sp.factorial(j) for j in range(4)) for r in roots)
td=sp.prod(1+r*t/2+(r*t)**2/12 for r in roots)
p=sp.expand(ch*td).coeff(t,3)
c1=x+y+z;c2=x*y+x*z+y*z;c3=x*y*z
expected=c1**3/2-sp.Rational(19,24)*c1*c2+c3/2
assert sp.expand(p-expected)==0
# Equality is verified as a polynomial in the three independent Chern roots.
result={'method':'exact rational Chern-root multiplication','ch_times_td_degree3_in_roots':str(p),'degree3_in_Chern_classes':'c1^3/2 - 19*c1*c2/24 + c3/2','c1_zero_c2_zero':'c3/2','six_sphere_c3_euler':2,'chi_TX':1,'identity_residual':str(sp.expand(p-expected)),'independent_evidence_group':'S6_SERIES_PUBLISH_II_C2_033H_20261122','timing':'written and run after target-proof release; no extra independent group'}
q=Path(__file__).with_suffix('.json');q.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
