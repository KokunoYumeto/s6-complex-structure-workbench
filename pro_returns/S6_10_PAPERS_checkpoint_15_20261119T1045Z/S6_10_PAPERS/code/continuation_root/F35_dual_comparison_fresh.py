#!/usr/bin/env python3
"""Post-comparison exact homology/cohomology convention and companion cusp."""
from pathlib import Path
from functools import reduce
from math import gcd
import sympy as s,json
Cf=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
Cg=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
T=(Cf.inv()*Cg).inv();N=T-s.eye(4)
assert N.rank()==1 and N*N==s.zeros(4)
assert reduce(gcd,[abs(int(x)) for x in N])==1
dual=T.inv().T;assert dual-s.eye(4)==-N.T
assert (dual-s.eye(4))**2==s.zeros(4)
out={'status':'PASS','chronology':'Written after isolated printed-item comparison; no prior producing code read',
 'homology_cusp_matrix':str(T),'homology_logarithm':str(N),
 'cohomology_cusp_matrix':str(dual),'cohomology_logarithm':str(-N.T),
 'image_rank':1,'primitive_entry_gcd':1,'nilpotent_square':'zero'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
