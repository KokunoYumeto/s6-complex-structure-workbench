"""Record scheduled review4 once, after refreshing the canonical inventory."""
from pathlib import Path
from collections import Counter
import csv, datetime, hashlib, json

R=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime(2026,11,20,0,40,1,tzinfo=datetime.timezone.utc)
p=R/'analysis/movement_reviews.json'; reviews=json.loads(p.read_text())
assert len(reviews)==3 and reviews[-1]['review_number']==3
with (R/'S6_SERIES_GRIND_inventory.csv').open() as f: rows=list(csv.DictReader(f))
done=[r for r in rows if r['completion_state'].startswith('done')]
pending=[r for r in rows if not r['completion_state'].startswith('done')]
labels=sorted({r['label'] for r in done})
new=sorted(set(labels)-set(reviews[-1]['completed_unique_labels']))
snapshot=R/'analysis/review04_all_open_rows.tsv'
fields=['label','tag','paper','status','completion_state','confidence_state','confidence_line','remaining_risk','format_check','layout_check']
with snapshot.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(pending)
math_open=[{k:r.get(k,'') for k in ['label','tag','paper','status','remaining_risk']} for r in rows if r['status'] in ['open','proved under hypotheses H']]
gates=dict(reviews[-1]['main_gates'])
gates['five finished papers']=f'{len(labels)} unique labels and {len(done)} source placements meet the recorded whole-row requirements; {len(pending)} placements retain their individual gates. Full snapshot: analysis/review04_all_open_rows.tsv.'
gates['Paper II sign-chain completion']='The seven main outlines and35steps have a complete current comparison with two explicit source guards integrated. The accepted UN labels and their exact counts are listed in the canonical inventory and completed-label set. Their retained full prereading receipts, receiving proofs, positive primary-source maps and current computations retain separate provenance. The remaining rows still require their individual source/reading/computation/format/layout decisions. A post-reading certificate or candidate count never closes them automatically.'
gates['Paper V global topology']='The989/914-check reconstruction and verifier and later140-check full integral chain isomorphism remain valid for the explicit algebraic complexes. Root found the unproved integral comparison to the marked finite-cap/affine-meridian diagram. The actual inverse-word polyhedral volumes cancel, but the diagram adapter remains open. P1.19 is explicitly open in the final part, preserving every original label/formula tag and the proved partial calculations. The actual manifold homology remains established separately by P1.12. This correction is not positive movement credit.'
gates['night:P3K.119']='Whole-row completion now includes the full frozen139-check derivation, complete four-block receiving comparison and88-check integral adapter, precise AC26/E26 source maps and seven actually viewed current pages. No absent historical renewed-credit file is claimed reopened.'
for label in ['night:P1.19','night:P1.4','night:P1.8','night:P1.17']:
    rr=[r for r in rows if r['label']==label]
    if rr:gates[label]='; '.join(dict.fromkeys(r['completion_state']+' — '+r['remaining_risk'] for r in rr))
receipts=[
 'analysis/K119_final_consolidation_08.json','analysis/V_source_credit_import_08.json',
 'analysis/UN36_and_P119_events_import_08.json','analysis/UN24_UN39_final_completion_08.json',
 'analysis/P1A6_final_completion_08.json','analysis/convention_and_UN24_UN39_integration_08.json',
 'audit_p119_fresh/AFTER_READING_03.md','audit_p119_fresh/receiving_chain_adapter.json',
 'audit_root/build30_V_visual_QA.json','audit_sign/II_build30_UN24_UN39_visual_QA_08.json',
 'analysis/current_reference_integrity.json','analysis/crosspaper_current_page_comparison.json']
extra=['analysis/P119_final_completion_08.json','analysis/P14_final_completion_08.json',
       'analysis/P119_polyhedral_guard_integration_08.json']
receipts += [x for x in extra if (R/x).exists()]
movement=bool(new)
streak=0 if movement else reviews[-1]['consecutive_reviews_without_movement']+1
reductions=[f'{len(new)} further unique labels reached whole-row completion at their exact recorded proof/source/computation/format/layout scopes. The label set and all source placements are preserved below.'] if new else []
record={'review_number':4,'utc':now.isoformat(),'scheduled_utc':'2026-11-20T00:40:01Z',
 'interval':'Fourth scheduled formal review, one hour after review3',
 'mathematical_status_changes':['night:P1.19: proved to open at the exact marked-diagram gate; correction, not positive movement credit'],'strictly_smaller_main_gates':reductions,
 'new_completed_unique_labels':new,'completed_unique_labels':labels,'completed_inventory_placements':len(done),
 'whole_row_completion_counts':dict(Counter(r['completion_state'] for r in rows)),
 'all_open_rows_snapshot':str(snapshot.relative_to(R)),
 'all_open_rows_snapshot_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),
 'all_open_inventory_placements':len(pending),'open_rows':math_open,'main_gates':gates,
 'movement':movement,'consecutive_reviews_without_movement':streak,
 'evidence_sha256':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in receipts},
 'qualification':'Only completed whole rows or strict mathematical gate reductions count. The local OS45 chart work, equivalent bundle-map reformulations, arithmetic corroboration, clean builds and packaging do not themselves count as a resolved main gate.',
 'decision':'Continue the authorized work.' if streak<2 else 'Apply the stopping rule and prepare the final incomplete package.',
 'next_review_utc':'2026-11-20T01:40:01Z'}
reviews.append(record);p.write_text(json.dumps(reviews,indent=2)+'\n')
rp=R/'analysis/run.json';run=json.loads(rp.read_text());run['next_movement_review_utc']=record['next_review_utc'];rp.write_text(json.dumps(run,indent=2)+'\n')
lines=[f'\n## {now.isoformat()} — formal movement review4\n',
       f'Movement: {movement}. Consecutive reviews without movement: {streak}. {record["decision"]} Next review: {record["next_review_utc"]}.\n',
       '### Strict reductions since review3\n']
lines += ['- '+x+'\n' for x in reductions]
lines += ['\nNew whole-row labels: '+', '.join(new)+'.\n','\n### Current main gates\n']
lines += ['- **'+k+'**: '+v+'\n' for k,v in gates.items()]
lines += ['\n### Every mathematically open placement\n']
lines += [f"- {r['paper']} {r['label']} [{r['tag']}]: {r['status']}.\n" for r in math_open]
lines += [f'\nThe full {len(pending)}-placement pending snapshot is `{snapshot.relative_to(R)}`, SHA256`{record["all_open_rows_snapshot_sha256"]}`.\n',record['qualification']+'\n']
with (R/'PROGRESS_LEDGER.md').open('a') as f:f.write('\n'.join(lines))
print(json.dumps({'review':4,'utc':now.isoformat(),'movement':movement,'new_done_labels':len(new),'done_labels':len(labels),'done_placements':len(done),'next_review':record['next_review_utc']}))
