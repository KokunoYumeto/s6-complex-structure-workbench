from pathlib import Path
import json
p=Path(__file__).parent;j=json.loads((p/'results_mapping.json').read_text())
j['statements']=[v for v in j['statements'] if v['id']!='P1.19']
j['statements'].append({'id':'P1.19','status':'Proved','items':['1.3'],'value':'Independent full global cellular calculation completed. The actual cusp secondary class is odd under psi; explicit integral chain automorphisms and homotopies reduce it to the exported corrected case. Chain ranks (4,26,87,162,200,156,79,23,3); free homology (1,0,0,0,4,0,0,0,1).','proof':'notes/part1.tex; global_ext_cases.py/.json/.out; cusp_ext_reduction.py/.json/.out; global_cell_certificate.py/.json/.out; cusp_ext_ambiguity.py/.json/.out','method':'Local cusp Poincare–Lefschetz duality fixes the secondary class; global Poincare duality is not used.'})
for v in j['statements']:
 if v['id']=='P1.12':v.pop('limitation',None)
for c in j['comparisons']:
 if c['id'] in ['F.2.5','F.2.6','F.4.1'] and 'P1.19' not in c['proof_ids']:c['proof_ids'].append('P1.19')
j['in_progress']['1.3']='Completed independently by P1.19, including the nonzero cusp Ext correction, its integral reduction, and full Smith matrices in every degree.'
j['in_progress']['1.5']='Parent owns analytic invariants, completed in P1A.1–4; characteristic numbers and topology are P1.13 and P1.19.'
j['owned_work_status']='All Part 1 work owned by this agent is proved or corrected with a proved exact replacement. Parent-owned analytic and endpoint statements complete the remaining subitems.'
(p/'results_mapping.json').write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
md=p.parents[1]/'notes/part1.md';old=md.read_text();tail=old.split('\n---\n\n',1)[1] if '\n---\n\n' in old else old
head='''# Current proof status (updated 2026-11-17 01:44 UTC)\n\nThe complete current derivations are in `notes/part1.tex`, statements P1.1–P1.19. The working notes below are retained as a chronological record; their earlier provisional entries are superseded by those proofs. Current exact status and permitted stated-value comparisons are in `code/part1/results_mapping.json`. Parent-owned analytic invariants, parameter classification and endpoints are in `notes/part1_analytic.tex` and `notes/part1_endpoints.tex`.\n\nAll work owned here is complete. In particular P1.18 proves the unique global minimum of h_b at infinity by a complete certified interval cover, and P1.19 supplies the independent full global cellular calculation with its necessary nonzero cusp Ext term. The latter exports every corrected differential and all Smith change-of-basis matrices; it does not rely on the global duality argument of P1.12.\n\n---\n\n'''
md.write_text(head+tail)
tex=p.parents[1]/'notes/part1.tex';v=tex.read_text();v=v.replace('''It satisfies
\\[
 r d_{\\partial,5}=0''','''In the ordered 35-dimensional boundary chain group it is
$r=-e_{17}^{t}-e_{18}^{t}$.  It satisfies
\\[
 r d_{\\partial,5}=0''');tex.write_text(v)
print('P1.19 complete; all independently computed comparisons updated; provisional work log clearly superseded.')
