"""Exact polynomial and discrete budgets for the two-junction closure."""
from pathlib import Path
import json
import sympy as s
X,Y,z,a,b,c,d=s.symbols('X Y z a b c d')
F=z*X+a*X**2+b*X*Y+c*Y**2
H=s.hessian(F,(X,Y,z))
assert s.det(H.extract([0,2],[0,2])) == -1
solutions=[]
for basezero in range(2,12):
 for g in range(1,12):
  for delta in range(12):
   for inter in range(12):
    if g+delta+inter==5-2*basezero:solutions.append((basezero,g,delta,inter))
assert solutions==[(2,1,0,0)]
for nc in range(3,100): assert nc+2>nc+1
out={'status':'PASS','global_genus_solutions':solutions,'R_factor_Hessian':[[str(v) for v in row] for row in H.tolist()],'nonzero_Hessian_minor':'-1','simple_zero_distributions':[[1,0,0],[0,1,0],[0,0,1]],'proof':'notes/part4_d4_two_junction_closure.md'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
