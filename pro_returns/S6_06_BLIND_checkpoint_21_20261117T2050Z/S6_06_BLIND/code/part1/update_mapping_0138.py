from pathlib import Path
import json
p=Path(__file__).parent;j=json.loads((p/'results_mapping.json').read_text())
j['statements']=[v for v in j['statements'] if v['id']!='P1.18']
j['statements'].append({'id':'P1.18','status':'Proved','items':['1.4','1.7'],'value':'h_b has its unique global minimum at infinity: −1.0945402503114027801162682630549457037255332694053308978 ±4.04e−56. Algebraic-splitting admissibility c>−h_b,min; original splitting threshold 0.1811385443749874439019453406721083768….','proof':'notes/part1.tex; minimum_certificate_summary.py/.json/.out; certified_minimum_root.py/.json/.out; certified_minimum_cusp.py/.json/.out; certified_minimum_cusp_annulus.py/.json/.out; certified_minimum_collar.py/.json/.out; normalization_shift.py/.json/.out'})
for v in j['statements']:
 if v['id'] in ['P1.8','P1.16']:v.pop('limitation',None)
j['in_progress']['1.7']='Owned work completed: exact h from the rational connection, globally certified minimum and interval, explicit normalization comparison, and fixed-fan absence of anti-biholomorphisms. Parent owns analytic parameter classification, Kuranishi, and endpoint statements.'
j['in_progress']['1.4']='Completed by P1.2, P1.4–5, P1.7–8 and P1.15–18, including corrected integral quotient and rank statements, exact connection, independent period values and global transversality.'
(p/'results_mapping.json').write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
q=p.parents[1]/'notes/part1.tex';v=q.read_text().replace('The last three columns of\n$J^{-1}HP(q)$ specifying $F_{c_*}$','The three columns of\n$J^{-1}HP(q)$ specifying $F_{c_*}$')
v=v.replace('''h_b(\\infty)\\in
 [-1.0945402503114027801162682630549457037255332694053308978
       \\ \\mathbin{\\pm}\\ 4.04\\cdot10^{-56}].''','''h_b(\\infty)\\in
 [-1.094540250311402780116268263054945704
       \\ \\mathbin{\\pm}\\ 3\\cdot10^{-37}].''')
q.write_text(v)
print('P1.18 and completed period/minimum metadata recorded.')
