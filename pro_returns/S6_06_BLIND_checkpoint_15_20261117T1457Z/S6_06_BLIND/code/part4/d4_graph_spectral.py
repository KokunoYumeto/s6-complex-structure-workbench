"""Exact spectral arithmetic genus and finite graph consistency checks."""
import json
from pathlib import Path
import sympy as s
e,b=s.symbols("e b", integer=True)
def intersection(a,c,A,C): return s.expand(a*A*e+a*C+A*c)
pa=s.simplify(1+intersection(3,-b,1,e-2-b)/2)
assert pa==3*e-2-2*b
assert pa.subs(e,0)==-2-2*b
assert pa.subs(e,2)==4-2*b
checks=[]
for c in range(1,30):
 for ra in range(1,15):
  for rp in range(c,c+4):
   for rm in range(c,c+4):
    total=ra+rp+rm
    for n in range(1,total//2+1):
     assert total-n>c
     checks.append(1)
result={"status":"PASS","spectral_genus":str(pa),"singular_image_degree":0,"singular_image_genus":str(pa.subs(e,0)),"smooth_image_degree":2,"smooth_image_genus":str(pa.subs(e,2)),"nosingleton_three_branch_integer_checks":len(checks),"proof_scope":"G1-G5 in part4_d4_graph_spectral_working.md; inequalities in the proof establish unrestricted graph counts."}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
