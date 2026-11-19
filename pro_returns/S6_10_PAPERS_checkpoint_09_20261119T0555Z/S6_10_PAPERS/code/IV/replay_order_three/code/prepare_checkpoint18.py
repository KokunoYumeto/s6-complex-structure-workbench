"""Finalize the exact checkpoint18 paper QA and required eighteenth-hour review."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,hashlib,json,re
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
p=root/'records/master62_audit.json'; a=json.loads(p.read_text())
assert hashlib.sha256((root/'S6_06_BLIND_paper.pdf').read_bytes()).hexdigest()==a['pdf_sha256']
a.update(status='PASS',direct_visual_review_utc=now)
a['direct_visual_review']={
 'reviewer':'root','contact_sheets_viewed':list(range(1,8)),
 'individual_pages_viewed':[515,532],
 'findings':'All 42 rendered pages directly inspected in seven contact sheets; full-page follow-ups on new local-map and analytic-endpoint pages. Equations, matrices, witness table, line maps and endpoint diagrams are legible, intact and within margins. Seven K78 standalone pages were independently directly reviewed by blind_control, with two further root full-page views.'}
p.write_text(json.dumps(a,indent=2)+'\n')
qa={'utc':now,'checkpoint':18,'master_build':62,'pages':a['pages'],
 'overfull_boxes':a['overfull_boxes'],'overfull_over_2pt':0,
 'max_overfull_pt':a['max_overfull_pt'],'before_over_2pt':0,
 'after_overfull_over_2pt':0,'rendered_pages':a['rendered_pages'],
 'rendered_page_count':len(a['rendered_pages']),
 'new_proof_ranges':{'P3K.77':[522,527],'P3K.78':[527,533]},
 'modified_proof_ranges':{'P3K.75':[512,515]},
 'contact_sheets':a['contact_sheets'],
 'sample_policy':a['policy'],
 'visual_inspection':'PASS: root directly inspected all 42 master pages in seven contact sheets, with full-page follow-ups on pages515 and532. The six-page K77 standalone and seven-page K78 standalone received full-page direct reviews; both have zero overflows. The complete 662-page boundary audit found no out-of-page words. Master62 has no undefined reference, missing character or unresolved rerun warning.',
 'source_log':'S6_06_BLIND_paper.log',
 'visual_review_records':['records/master60_audit.json','records/master62_audit.json',
  'records/k77_standalone_visual_qa.json','records/k78_standalone_visual_qa.json'],
 'pdf_bytes':a['pdf_bytes'],'pdf_sha256':a['pdf_sha256']}
(root/'records/typesetting_checkpoint18.json').write_text(json.dumps(qa,indent=2)+'\n')
progress={
 'checked_utc':now,'decision':'CONTINUE',
 'reason':'The main monodromy question and its remaining sectors advanced: the complete OS49 all-fan return and smooth ordinary-clutch comparison are proved, and the unresolved source-zero attachment and full fixed-source endpoint automorphisms have new exact maps and active audits.',
 'main_question_progress':[
  'K77 proves the actual OS49 return on every GL2Z lattice-basis fan, including the exact shorter endpoint and fixed-source cap-data iterates. The exact image is gcd(k,28)Z/28; all28 k=1 witnesses have166 independent fresh target-prism solves.',
  'K78 proves the full integral OS49 smooth order-one clutch comparison: H2 of the extending-period root groupoid is Z plus Z/k, the signed norm is D=n+m sum psi(ell), and actual holomorphic source/line/root/fan maps identify all sphere sectors with K77.',
  'K78 retains the literal parameter period deck, explicit annular Isom connection and radial ODE, and typed inverse-endpoint conjugacy; it does not infer loop transport from fibrewise comparisons.'
 ],
 'other_open_item_progress':[
  'The source-zero comparison now has the complete two-node Morse/Tate/Cartier map, full charged quaternion charts, exact finite source/target faces, canonical local spin lift and a positive-width ambient comparison to the radial arm.',
  'The whole fixed trace and its two actual caps retain both normal clutch windings and all c2 cross terms; an explicit cap-replacement bordism proves their index cancellation. The global finite-strip/upper-arm ownership remains under audit and no value of e is assigned.',
  'A new fixed-source OS49 endpoint working proof computes the exact centralizer and tests its linear signs with the integral affine-torsor class. It is pending local/root audit and is not yet a numbered completed result.'
 ],
 'next_main_steps':[
  'Complete the upper-arm domain and the full source-zero finite-strip/outside boundary equation, including the separate a=1 two-step chamber.',
  'Finish the exact full OS49 endpoint-automorphism audit.',
  'Continue the remaining ordinary/singular-site and marked source-moduli sectors.'
 ],
 'next_progress_check_due_utc':'2026-11-17T18:49:44+00:00'}
(root/'records/progress_check_18_hours.json').write_text(json.dumps(progress,indent=2)+'\n')
hashes={
 'notes/part5.tex':'f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f',
 'notes/part5_blind.md':'ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'}
for name,h in hashes.items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==h
rows=list(csv.DictReader((root/'S6_06_BLIND_results.csv').open()))
counts=dict(Counter(r['status'] for r in rows))
assert len(rows)==258 and counts=={'Proved':219,'Refuted':35,'Known':3,'Open':1},counts
ready={'utc':now,'status':'PAPER_AND_PROOF_RECORDS_VERIFIED_FOR_CHECKPOINT18',
 'checkpoint':18,'due_utc':'2026-11-17T17:49:44+00:00',
 'master_build':62,'pages':a['pages'],'pdf_bytes':a['pdf_bytes'],
 'pdf_sha256':a['pdf_sha256'],'statements':counts,
 'full_page_boundary_audit':'PASS662','rendered_and_directly_reviewed_pages':42,
 'contact_sheets':7,'overfull_above2pt':0,'max_overfull_pt':a['max_overfull_pt'],
 'blind_part5_hashes':hashes,'next_scheduler':'code/await_checkpoint19.py',
 'next_scheduler_session':52692,
 'scope':'Only the hourly complete snapshot will be created; working proofs remain explicitly unpromoted.'}
(root/'records/checkpoint18_ready.json').write_text(json.dumps(ready,indent=2)+'\n')
print(json.dumps({'status':'PASS','pages':662,'statements':counts,'pdf_sha256':a['pdf_sha256']},indent=2))

