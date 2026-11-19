from pathlib import Path
from itertools import product
import importlib.util
import sympy as s
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('tupledata',root/'background/data/fourfold_tuple.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
Rs=[d.M1[1:,1:],d.M2[1:,1:]]
vecs=[s.Matrix(v) for v in product([-1,0,1],repeat=5) if any(v)]
print('search_bounds_all_coordinates',[-1,1],'vectors',len(vecs))
for v in vecs:
 K=s.Matrix.hstack(*[Rs[0]**j*v for j in range(5)])
 if abs(K.det())==1:
  print('R1_conjugator',K,'det',K.det(),'model',K.inv()*Rs[0]*K);break
else:print('R1 no witness in box')
ws=[w for w in vecs if Rs[1]*w==-w]
print('R2_minus_eigenvectors_in_box',len(ws))
found=False
for v in vecs:
 vs=[Rs[1]**j*v for j in range(4)]
 for w in ws:
  K=s.Matrix.hstack(*vs,w)
  if abs(K.det())==1:
   print('R2_conjugator',K,'det',K.det(),'model',K.inv()*Rs[1]*K);found=True;break
 if found:break
if not found:print('R2 no witness in box')
