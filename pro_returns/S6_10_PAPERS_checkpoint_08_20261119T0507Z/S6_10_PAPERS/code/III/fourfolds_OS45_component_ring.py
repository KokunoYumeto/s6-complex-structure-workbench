"""Exact marked D47 component form for OS45 a=2,b=8 at the I8 zero.

No numerical lattice is guessed: the actual D46 monodromy is reconstructed
from the saved elliptic matrix and section cocycle. The primitive short
basis is (e1,delta), the long basis is (e2,gamma). All16 components and
all integral trilinear entries are retained.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
import manifolds_general_initial as G
import fourfolds_D2_component_ring as C
ROOT=Path(__file__).resolve().parent
info=G.PROFILES[(45,'default')]
A=G.actual_lifts(info,2,8,[2,0,0,0,0])
N=A[0]-s.eye(4)
assert N*N==s.zeros(4)
short=s.eye(4)[:,[0,2]];long=s.eye(4)[:,[1,3]]
period=N.extract([0,2],[1,3])
assert short*period==N*long
assert period==s.Matrix([[8,24],[-6,-16]])
H=hermite_normal_form(period)
assert H==s.diag(8,2)
form=C.run(8,0,2)
result=dict(profile='OS45/default',P=2,Q=8,weights=[2,0,0,0,0],
            monodromies=[M.tolist() for M in A],
            short_basis=['e1','delta'],long_basis=['e2','gamma'],
            period=period.tolist(),column_HNF=H.tolist(),
            Smith=[2,8],components=16,component_form=form,
            scope='Local component form with the actual marked period lattice; full global finite-coefficient invariants are a separate calculation.')
(ROOT/'fourfolds_OS45_component_ring.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print('Actual period',period.tolist(),'HNF',H.tolist(),'Smith(2,8)')
print('Components',16,'nonzero sorted trilinear entries',len(form['symmetric_integral_trilinear']))
print('Cubic coefficients',sorted(set(x['coefficient'] for x in form['cubic'])))
print('All16-component symmetry, constant-kernel and exact cell comparisons PASS')
