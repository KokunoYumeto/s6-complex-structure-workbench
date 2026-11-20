"""Record the scheduled substantive review, with exact open rows and gates."""
from pathlib import Path
from collections import Counter
import argparse,csv,json

R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--utc',required=True);a=p.parse_args()
rows=list(csv.DictReader((R/'S6_SERIES_GRIND_inventory.csv').open()))
openrows=[r for r in rows if r['status'] in ['open','proved under hypotheses H']]
closed=['night:P3K.109','night:P3K.110','night:P3K.113','night:P3K.114','night:P3K.115','night:P3K.116','night:P3K.117','night:P3K.118','night:P3K.119']
for label in closed:
 found=[r for r in rows if r['label']==label];assert found and all(r['status']=='proved' for r in found),label
gates={
 'five finished papers':'All five full sources and PDFs exist. Remaining: complete row-specific confidence/credit/disposition decisions, residual workflow/known-proof reductions, and their final format/layout integration. Exact verified formatting and source replacements remove the corresponding passages from that remaining work.',
 'inv:C3.8':'The complete proposed actual-atlas Cech construction and coefficient recursion now have a full receiving review and independent local computations. Preserve the older proved operator formulas, integrate the new theorem and exact source relationship, then build and render before promoting its publication status.',
 'ari:C.7.4':'The nontorsion diagonal relative-period exclusion H remains unproved, with the explicit smallest examples and failed criteria retained.',
 'inv:E2.3':'Construct a specified admissible smoothed12-tooth period section and its actual transition/Kodaira-Spencer matrices, then determine the rank-three kernel splitting.',
 'maps:src:D.2.4':'For the weighted OS45 instance, determine the actual framed odd torsion-cycle linking that selects0 or4 in Z/8. The integral D2.51 cone and h=1 marked kernel are checked; h>1 geometric torsion columns remain.',
 'night:P3K.75':'Complete the remaining marked source-moduli generators: OS45 I9, handle and infinity sectors, additional ordinary clutch slots with nonzero total norm, and endpoint loci outside the completed domains. Their actual source, line, root, annular and closing comparisons remain required.',
 'night:P3K.111':'The new regular common auxiliary fan and one endpoint are explicitly constructed. Finish zero/infinity endpoint lifts, the whole compact evaluation and completed marked physical-boundary comparison. The original unavailable array and its named IL/CFL values are not replaced without that comparison.',
 'night:P3K.112':'The relative fan/cap proof and all28 witnesses are independently checked. The absolute K111 original-source/reference seed remains its mathematical dependency.'}
record={'review_number':1,'utc':a.utc,'start_utc':'2026-11-19T18:40:01Z',
 'interval':'First scheduled review, approximately three hours after start',
 'mathematical_status_changes':closed,
 'strict_main_completion_reductions':[
 'Five full standardized papers with actual body/outline/tag/reference maps and exact change receipts replace the unstandardized six-paper start.',
 'Nine full endpoint arguments now have complete scoped comparisons and fresh arithmetic, and their complete blocks precede the final part.',
 'Ninety-four long proofs have mathematically identical numbered-level transports; the seven V analytic subclaims retain all outer reference numbers.',
 'Opened exact known-input citations and explicit source/line/fan/surgery transports replace the corresponding long or misattributed passages.',
 'The global V numerical certificate and separate saved-output verifier close the previously incomplete numerical gate.',
 'F10 determinant disagreement is settled by the exact matrix and all direct-use comparisons; the failing computation is preserved.',
 'The C3.8 constructive gate now has full explicit coefficient formulas and receiving comparison, leaving integration/source/form checks rather than an unknown global cochain.',
 'The K111 finite regularization-choice gate has exact integral morphisms; the new common fan and one endpoint remove those constructive subproblems from the alternate route.'],
 'movement':True,'consecutive_reviews_without_movement':0,
 'whole_row_completion_counts':dict(Counter(r['completion_state'] for r in rows)),
 'qualification':'A mathematical status change or targeted check does not automatically award whole-row completion. The displayed completion counts retain every remaining confidence and format gate. Packaging contributes no movement.',
 'open_rows':[{'label':r['label'],'tag':r['tag'],'paper':r['paper'],'status':r['status'],'remaining_risk':r.get('remaining_risk','')} for r in openrows],
 'main_gates':gates,'decision':'Continue the authorized work.','next_review_utc':'2026-11-19T22:40:01Z'}
path=R/'analysis/movement_reviews.json'
existing=json.loads(path.read_text()) if path.exists() else []
assert not existing,'First-review script cannot overwrite an existing review.'
path.write_text(json.dumps([record],indent=2)+'\n')
lines=[f'\n## {a.utc} — formal movement review1',
 '','Movement: YES. Consecutive reviews without movement:0. Continue. Next review:22:40:01 UTC.','',
 'Nine mathematical endpoint rows changed from open to proved: '+', '.join(closed)+'. Their full source, cap, reference and parameter scopes are retained. This does not automatically award whole-row completion.','',
 'Strict reductions of the main completion gate:','']
lines += ['- '+x for x in record['strict_main_completion_reductions']]
lines+=['','Current main gates:','']+['- **'+k+'**: '+v for k,v in gates.items()]
lines+=['','Every open mathematical inventory row at this review:','']
lines+=['- '+r['paper']+' '+r['label']+' ['+r['tag']+']: '+r['status']+'.' for r in openrows]
lines+=['',record['qualification'],'']
ledger=R/'PROGRESS_LEDGER.md';ledger.write_text(ledger.read_text()+'\n'.join(lines))
print(json.dumps({'review':1,'movement':True,'open_inventory_rows':len(openrows),'next_review_utc':record['next_review_utc']}))
