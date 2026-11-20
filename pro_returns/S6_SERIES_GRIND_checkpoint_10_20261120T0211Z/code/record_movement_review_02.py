"""Record the second scheduled review from the actual current inventory."""
import csv
import datetime
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
path = ROOT / 'analysis/movement_reviews.json'
reviews = json.loads(path.read_text())
assert len(reviews) == 1 and reviews[0]['review_number'] == 1
with (ROOT / 'S6_SERIES_GRIND_inventory.csv').open() as stream:
    rows = list(csv.DictReader(stream))
assert all(r['status'] == 'proved' for r in rows if r['label'] == 'inv:C3.8')
done = [r for r in rows if r['completion_state'].startswith('done at the stated scope')]
assert done
receipt_paths = [
    'audit_corrections/K111_auxiliary_boundary_comparison_05.md',
    'audit_corrections/K111_auxiliary_boundary_receipt_05.json',
    'audit_paper_i/I_whole_row_completion_proposals_06.json',
    'audit_paper_i/build21_I_focused_visual_QA.json',
    'audit_paper_i/build21_I_continuation_visual_QA.json',
    'audit_root/build21_visual_QA.json',
    'analysis/I_adjacent_program_integration_06.json',
    'analysis/I_cusp_program_integration_06.json',
]
receipts = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in receipt_paths}
gates = {
    'five finished papers': 'The 26 named Paper I assessments now close 42 inventory placements at their exact reviewed build21 scopes. Five further Paper I rows have only changed-page inspection pending. The other row-specific confidence, credit and formatting gates remain. Build22 must inspect subsequent changed pages and refresh cross-paper destinations.',
    'inv:C3.8': 'Mathematical status changed to proved. The complete original-atlas coefficient construction, independent quadratic-tensor route and receiving comparison close the previous cochain gate. All13 receiving steps are covered by39 pre-reading and45 receiving exact checks; the original DGKX v1 source and exact family/line transport are credited. Current build21 pages375–383 were actually viewed.',
    'ari:C.7.4': 'The nontorsion diagonal relative-period exclusion H remains unproved. A new specialized primary-literature/arithmetic attack has started; no status change is inferred.',
    'inv:E2.3': 'Construct a specified admissible smoothed12-tooth period section and its actual transition/Kodaira-Spencer matrices, then determine the rank-three kernel splitting.',
    'maps:src:D.2.4': 'The weighted OS45 refined odd-cycle linking still selects between0 and4 in Z/8. The primitive cubic reconstruction closes its separate computational obligation; reconstruction of the actual integral core matrix and peripheral cochain has now begun from the displayed geometric inputs. No odd-linking conclusion follows from the even null-chain task.',
    'night:P3K.75': 'Complete the remaining marked source-moduli generators: OS45 I9, handle and infinity sectors, additional ordinary clutch slots with nonzero total norm, and endpoint loci outside the completed domains. Their actual source, line, root, annular and closing comparisons remain required.',
    'night:P3K.111': 'The new endpoint construction, physical compact-owner calculation, moving cap and lower bodies are complete at their recorded scopes. Root independently recomputed484310 compact and378 moving checks. The separate receiving review closes the exterior point/O maps, all lower source stars, moving normal/NC maps, finite-isotropy Stokes and inherited F41/F46/K96/K94 maps, with137749+2464+18 fresh assertions. Remaining publication gate: integrate this new proof, segregate every unavailable older execution and verify the resulting sources/PDF. The body still reads open at this review; the old interior graph crossings remain explicitly recorded.',
    'night:P3K.112': 'The relative fan/cap and28-witness proof is checked. Its absolute input is the now geometrically verified new K111 seed; integrate the precise dependency and new seed before changing the body status and final-part placement.'
}
current_open = [{k:r.get(k,'') for k in ('label','tag','paper','status','remaining_risk')} for r in rows if r['status'] in ('open','proved under hypotheses H')]
review = dict(
    review_number=2, utc=now, scheduled_utc='2026-11-19T22:40:01Z',
    interval='Second scheduled formal review, one hour after the first',
    mathematical_status_changes=['inv:C3.8 (all three source placements)'],
    strictly_smaller_main_gates=[
        'The original-atlas cochain question has become a proved, credited and rendered result with its independent receiving gate closed.',
        'Twenty-six exact Paper I whole-row assessments close42 inventory placements; the later changed-page checks remain explicitly attached to subsequent edits.',
        'The formerly missing K111 zero/infinity fan, complete compact evaluation and moving/lower cap data are supplied, independently recomputed and compared on the same atlas.',
        'The K111 geometric receiving gate now closes through actual exterior modules, NC normal-bundle bordism, complete IL charts and the exact inherited sphere path. The remaining gate is concrete proof integration and source/layout validation.',
        'Fourteen unavailable Paper I checker references now have supplied fresh exact programs and scope-matched replacements, including the complete12-element cusp fan action derived from side and character transport.'
    ],
    movement=True, consecutive_reviews_without_movement=0,
    whole_row_completion_counts=dict(Counter(r['completion_state'] for r in rows)),
    completed_unique_labels=sorted({r['label'] for r in done}),
    completed_inventory_placements=len(done),
    qualification='Counts refer to exact scoped evidence and actual reviewed build21 pages. No unavailable historical code, different-model-family review, formal proof-assistant certification, or unperformed newer PDF inspection is claimed. Packaging is not movement.',
    open_rows=current_open, main_gates=gates, evidence_sha256=receipts,
    decision='Continue the authorized work.', next_review_utc='2026-11-19T23:40:01Z'
)
reviews.append(review)
path.write_text(json.dumps(reviews,indent=2)+'\n')
runpath=ROOT/'analysis/run.json'
run=json.loads(runpath.read_text())
run['next_movement_review_utc']=review['next_review_utc']
runpath.write_text(json.dumps(run,indent=2)+'\n')
lines=[f'\n## {now} — formal movement review2\n',
       'Movement: YES. Consecutive reviews without movement:0. Continue. Next review:23:40:01 UTC.\n',
       'The exact inventory snapshot and evidence hashes are retained in analysis/movement_reviews.json. Packaging is not movement.\n',
       '### Strict reductions since review1\n']
lines.extend('- '+x+'\n' for x in review['strictly_smaller_main_gates'])
lines.append('\n### Current main gates\n')
lines.extend('- **'+k+'**: '+v+'\n' for k,v in gates.items())
lines.append('\n### Every mathematically open inventory placement\n')
lines.extend(f"- {r['paper']} {r['label']} [{r['tag']}]: {r['status']}.\n" for r in current_open)
lines.append('\nWhole-row completion counts: '+json.dumps(review['whole_row_completion_counts'])+'\n')
with (ROOT/'PROGRESS_LEDGER.md').open('a') as stream: stream.write('\n'.join(lines))
print(json.dumps({'review':2,'utc':now,'movement':True,'completed_unique_labels':len(review['completed_unique_labels']),'completed_inventory_placements':len(done),'next_review':review['next_review_utc']}))
