from pathlib import Path
import csv,hashlib,json,datetime
P=Path(__file__).resolve().parents[1]
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
out=json.loads((P/'code/independent_IV_low_F_completion.json').read_text())
assert out['status']=='PASS' and out['assertions']==61
scopes={
'night:P3F.4':'the exact Hopf Mayer–Vietoris matrix determinant',
'night:P3F.5':'the genus-three canonical fibre coefficient and the characteristic-class square',
'night:P3F.7':'the conifold coordinate map, integral Mayer–Vietoris determinant, and explicit smooth SU(2) contraction at its center and boundary',
'night:P3F.9':'the exact orbit-chart derivative and positive radial derivative for nonnegative squared norms, including the zero-fibre solution',
'night:P3F.10':'the physical line square under fibre shifts, reference page expression, and the literal ordered Seifert relation matrix determinant +1',
'night:P3F.11':'the actual phase-line Chern product, adjoint first Pontryagin class, framing-index cancellation and integer sixfold additivity',
'night:P3F.12':'the full literal commutator, its membership in the cyclic cover subgroup, integral coinvariant unimodularity, connected degree-twelve character and genus-three normalization',
'night:P3F.13':'the literal ordinary and cusp origins, full angular/deck differences, both gauge endpoints, winding −12, and all four local small-resolution substitutions',
'night:P3F.15':'the full Laurent node-chart units, twelvefold phase and scalar exponents, source translation, all nontrivial label powers, winding −12 and central base valuation',
'night:P3F.17':'the symbolic coprime weighted-page Riemann–Hurwitz, genus, Euler, signature, height, all-multiple intersection, line square, relative Pontryagin and page formulas',
'night:P3F.18':'both completed page Euler numbers, degree-four height, all-multiple intersection and section-line square',
'night:P3F.20':'the actual monomial matrix and primitive ray, physical circle image and order-two stabilizer, and the OS49 height correction'
}
fields=['statement_id','date','who','type','outcome','event_id','phase']
f=P/'CHECK_EVENTS.tsv'; rows=list(csv.DictReader(f.open(),delimiter='\t'));old=len(rows);ids={r['event_id'] for r in rows}
new=[]
def add(label,kind,desc,key):
 eid='s6sg:'+hashlib.sha256(key.encode()).hexdigest()[:20]
 r=dict(zip(fields,[label,'2026-11-19',actor,kind,desc,eid,'current']))
 if eid not in ids: rows.append(r);new.append(r);ids.add(eid)
for label,scope in scopes.items():
 names=[x['name'] for x in out['checks'] if x['label']==label]
 assert names
 add(label,'computation or formal certificate',f'Fresh code/independent_IV_low_F_completion.py completed PASS61 exact assertions in0.991seconds, using independently written SymPy differentiation/polynomial reduction and formal Laurent exponent vectors with no earlier program or certificate imports. This row receives only {len(names)} named checks: '+', '.join(names)+'. These verify '+scope+'. Complete code and output are supplied; code SHA256 '+out['code_sha256']+'. Written after receiving-proof readings; no before-reading whole-proof claim or unavailable historical-atlas replay. The first failed F10 determinant target and intermediate syntax repair are preserved under code/independent_IV_low_F_completion_attempt02_syntax.* and attempt03_F10.*. Source realization, analytic extension, orientation and global topology retain their separately recorded proofs.',label+'|low_F_completion_61|'+out['code_sha256'])
add('night:P3F.10','targeted proof check','Fresh exact arithmetic disproved only the evaluated sign in the literal ordered relation matrix [[3,0,-1],[0,4,1],[1,1,0]]: its determinant is −3+4=+1. The failed expected−1 assertion is retained. The root independently recomputed +1 and integrated the one-sentence correction (analysis/IV_F10_correction_04.json). Read the receiving F10 argument and all six direct-use passages F17,F21,F25,K6,K7,K10. Those uses invoke unimodularity, the actual page invariants or the separate framed geometric maps; none imports the erroneous determinant sign. The corrected scalar evaluation changes no relation, meridian, line convention, orientation map or return class. Exact old/new text and passages: IV_F10_determinant_correction.json, IV_F10_direct_use_passages.json. This is a correction to a proof calculation, not a refutation of the theorem.','F10|actual determinant correction +1|2026-11-19')
with f.open('w',newline='') as z:
 w=csv.DictWriter(z,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
t=P/'IV_known_input_specializations.tsv';ks=list(csv.DictReader(t.open(),delimiter='\t'));cols=list(ks[0]);preserved=[]
for r in ks:
 if r['label']=='night:P3F.10':
  preserved.append(dict(r));r['retained_map_or_calculation']=r['retained_map_or_calculation'].replace('actual Seifert matrix determinant−1','actual ordered Seifert relation matrix determinant+1')
  r['opening_and_check_scope']='Receiving proof and all six direct uses read. The fresh61-check program detected and corrected the printed determinant sign; root independently obtained+1. Unimodularity and the actual geometric orientation maps are retained.'
with t.open('w',newline='') as z:
 w=csv.DictWriter(z,fieldnames=cols,delimiter='\t');w.writeheader();w.writerows(ks)
g=P/'code/build_IV_known_input_review.py'
if g.exists():
 s=g.read_text();s=s.replace('actual Seifert matrix determinant−1','actual ordered Seifert relation matrix determinant+1');g.write_text(s)
receipt={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'old_events':old,'new_events':len(rows),'added':new,'old_F10_table_row':preserved,'scope':'Stable IDs deduplicate on re-run. The separately saved actual-F19 event remains already integrated into CP03; this script adds no duplicate of it.'}
(P/'IV_low_F_completion_event_receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'old':old,'new':len(rows),'added':len(new),'labels':list(scopes)},ensure_ascii=False))
