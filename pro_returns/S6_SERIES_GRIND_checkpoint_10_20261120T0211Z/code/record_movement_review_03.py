"""Record the third scheduled review, preserving the full open-row snapshot."""
from pathlib import Path
from collections import Counter
import csv,datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime(2026,11,19,23,39,40,tzinfo=datetime.timezone.utc)
reviews_path=R/'analysis/movement_reviews.json';reviews=json.loads(reviews_path.read_text())
assert len(reviews)==2 and reviews[-1]['review_number']==2
rows=list(csv.DictReader((R/'S6_SERIES_GRIND_inventory.csv').open()))
done=[r for r in rows if r['completion_state'].startswith('done')]
pending=[r for r in rows if not r['completion_state'].startswith('done')]
done_labels=sorted({r['label'] for r in done})
new_labels=sorted(set(done_labels)-set(reviews[-1]['completed_unique_labels']))
assert {'night:P1.16','night:P1.18'}<=set(done_labels)
for label in ['night:P3K.111','night:P3K.112']:
    rr=[r for r in rows if r['label']==label]
    assert rr and all(r['status']=='proved' for r in rr)
snapshot=R/'analysis/review03_all_open_rows.tsv'
fields=['label','tag','paper','status','completion_state','confidence_state','confidence_line','remaining_risk','format_check','layout_check']
with snapshot.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(pending)
receipts=[
 'analysis/K111_K112_integration_06.json','audit_corrections/IV_whole_row_completion_final_06.json',
 'audit_paper_i/checkpoint06_I_counts.json','audit_paper_i/closure_07/WHOLE_ROW_ASSESSMENTS.md',
 'audit_paper_i/closure_07/build26_V_visual_QA.json','audit_root/build26_V_changed_visual_QA.json',
 'audit_corrections/V_topology_receiving_07.md','audit_corrections/V_topology_receiving_receipt_07.json',
 'analysis/received_proof_integration_07.json','audit_sign/K111_whole_step_exposure_scope_07.json',
 'code/outputs/III_OS45_boundary_prisms_07.json']
hashes={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in receipts}
gates={
 'five finished papers':f'{len(done_labels)} unique labels and {len(done)} source placements are done at their exact recorded scopes; {len(pending)} placements remain. The full pending-row snapshot is analysis/review03_all_open_rows.tsv. Current changes have actual page-specific visual receipts. Build27 refreshes the final LR numbering, three IV dependency lines and cross-paper pages; only observed current results count.',
 'ari:C.7.4':'The nontorsion diagonal relative-period/norm exclusion remains unproved. Exact CM isogeny and kernel witnesses and their actual period-basis transport are now supplied with39 exact and10 interval checks; these do not establish the missing exclusion. The tensor/subquotient route remains under examination.',
 'inv:E2.3':'Construct the specified admissible smoothed12-tooth period section, its actual transition and Kodaira–Spencer matrices, then determine the rank-three kernel splitting. No rank/degree-only inference is made.',
 'maps:src:D.2.4':'The weighted OS45 example still requires an embedded odd three-cycle, its actual reference framing and critical-specialization linking to choose0 or4 in Z/8. The full core, cochain and annulus programs are now present. The new explicit prism calculation bounds alpha=e1 wedge delta in the exterior and the cap core quotients, and bounds2alpha on the cusp mapping torus; its mod2 detector proves order2. These algebraic witnesses do not resolve the framed linking. Other star-log sectors and h>1 original-additive-cap torsion markings remain.',
 'night:P3K.75':'The remaining marked source-moduli generators include OS45 I9, handle/infinity sectors, additional ordinary clutch slots with nonzero total norm and endpoint loci outside completed domains. Actual source, line, root, annular and closing maps remain required.',
 'night:P3K.111':'Mathematical status is proved through the complete auxiliary-filling boundary comparison, integrated before the final part. Current exact code-claim and numbering repairs have actual image receipts. The full before-reading derivation requirement still has precisely documented analytic/cap/Stokes scopes; mechanism-only freezes are not promoted to full-step checks.',
 'night:P3K.112':'Mathematical status is proved with the actual K111 seed, full relative fan/cap maps and all28 witnesses. Its own receipt and dependency exposure scopes control whole-row completion.',
 'iv:open:K111:original_auxiliary_arrays':'The unavailable original CFL/IL chart arrays and their original subtotals remain unreconstructed as a separately labelled alternative construction in the final part. The new auxiliary proof does not assert equality of absent old arrays.',
 'Paper II sign-chain completion':'The116-page actual visual sample and exact per-row/dependency evidence join are complete. The earlier broad readiness count was withdrawn; whole-step chronology, computational applicability and concrete source credit are being decided row by row. No Paper II row is marked done by a numerical candidate count.',
 'Paper V global topology':'The complete corrected mapping-cone reconstruction passes989 assertions and its separate saved-output verifier914 assertions. Actual integral cycle bases, cokernel maps, local relative duality and chain homotopies are integrated and visually inspected. P1.19 retains its whole-before-reading methodological gate; no global duality shortcut or absent historical execution is claimed.'}
math_open=[{k:r.get(k,'') for k in ['label','tag','paper','status','remaining_risk']} for r in rows if r['status'] in ['open','proved under hypotheses H']]
reductions=[
 'K111 and K112 have changed from open to proved, with the full new proof and exact seed dependency integrated before the final part.',
 f'{len(new_labels)} further unique labels have whole-row completion recorded since review2; their full set is included below. The current count preserves every scope qualification.',
 'P1.16 now has a complete current192-step outward-rounded loop/period certificate, an independently authored980-check saved-data validator, receiving comparison and actual inspection of its entire proof. P1.18 has complete current-proof inspection and its retained full aggregate derivation/certificate evidence.',
 'The full global P1.19 chain calculation has explicit integral maps and homotopies and current executed989/914-check programs. Its computational/reproducibility gate is closed while its separate before-reading gate remains.'
]
review={'review_number':3,'utc':now.isoformat(),'scheduled_utc':'2026-11-19T23:40:01Z',
 'interval':'Third scheduled formal review, one hour after the second',
 'mathematical_status_changes':['night:P3K.111','night:P3K.112'],
 'strictly_smaller_main_gates':reductions,'new_completed_unique_labels':new_labels,
 'completed_unique_labels':done_labels,'completed_inventory_placements':len(done),
 'whole_row_completion_counts':dict(Counter(r['completion_state'] for r in rows)),
 'all_open_rows_snapshot':str(snapshot.relative_to(R)),'all_open_rows_snapshot_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),
 'all_open_inventory_placements':len(pending),'open_rows':math_open,'main_gates':gates,
 'movement':True,'consecutive_reviews_without_movement':0,'evidence_sha256':hashes,
 'qualification':'Status changes and strictly closed obligations count. Packaging, candidate-count revisions, page sampling and the OS45 boundary-prism corroboration alone do not count as resolution of the remaining framed-linking gate.',
 'decision':'Continue the authorized work.','next_review_utc':'2026-11-20T00:40:01Z'}
reviews.append(review);reviews_path.write_text(json.dumps(reviews,indent=2)+'\n')
rp=R/'analysis/run.json';run=json.loads(rp.read_text());run['next_movement_review_utc']=review['next_review_utc'];rp.write_text(json.dumps(run,indent=2)+'\n')
lines=[f'\n## {now.isoformat()} — formal movement review3\n',
 'Movement: YES. Consecutive reviews without movement:0. Continue. Next review:20 November00:40:01 UTC.\n',
 '### Strict reductions since review2\n']
lines+=['- '+x+'\n' for x in reductions]
lines+=['\nNew whole-row labels: '+', '.join(new_labels)+'.\n','\n### Current main gates\n']
lines+=['- **'+k+'**: '+v+'\n' for k,v in gates.items()]
lines+=['\n### Every mathematically open placement\n']
lines +=[f"- {r['paper']} {r['label']} [{r['tag']}]: {r['status']}.\n" for r in math_open]
lines +=[f'\nAll{len(pending)} not-yet-done placements, including exact confidence/format/layout states, are preserved in `{snapshot.relative_to(R)}` with SHA256`{review["all_open_rows_snapshot_sha256"]}`.\n',review['qualification']+'\n']
with (R/'PROGRESS_LEDGER.md').open('a') as f:f.write('\n'.join(lines))
print(json.dumps({'review':3,'utc':now.isoformat(),'movement':True,'new_done_labels':len(new_labels),'done_labels':len(done_labels),'done_placements':len(done),'next_review':review['next_review_utc']}))
