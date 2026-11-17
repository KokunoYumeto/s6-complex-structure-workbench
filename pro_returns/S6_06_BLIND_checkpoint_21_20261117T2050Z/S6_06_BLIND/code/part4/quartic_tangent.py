from pathlib import Path
import json
import sympy as s
I=s.I
rows=[]
for M in range(6):
    chi=4*(7-M)
    char=[chi,0,0,0]
    mult=[s.simplify(sum(char[k]*I**(-j*k) for k in range(4))/4) for j in range(4)]
    assert mult==[7-M]*4
    lower=3*(7-M)
    assert lower>M
    rows.append({'M':M,'Euler':chi,'virtual_character_multiplicities':[int(v) for v in mult],'nontrivial_H2_rank_lower':lower,'zero_form_rank_upper':M,'contradiction':True})
solutions=[]
for d in range(3,9):
 for n in range(1,5):
  for a in range(3):
   if (d-2)*n+a==2:
    solutions.append({'multiplicity':d,'ambient_exception_order':n,'new_pole_coefficient':a})
assert solutions==[{'multiplicity':3,'ambient_exception_order':1,'new_pole_coefficient':1},{'multiplicity':3,'ambient_exception_order':2,'new_pole_coefficient':0},{'multiplicity':4,'ambient_exception_order':1,'new_pole_coefficient':0}]
out={'status':'PASS','quartic_character_bounds':rows,'pole_coefficient_solutions':solutions}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Quartic tangent and zero-form bounds: PASS')
for row in rows: print('M=%d: nontrivial rank >=%d > %d'%(row['M'],row['nontrivial_H2_rank_lower'],row['zero_form_rank_upper']))
print('Pole coefficient solutions:',solutions)
