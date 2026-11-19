import csv,json,hashlib,datetime,shutil,sys
from pathlib import Path
csv.field_size_limit(16*1024*1024)
R=Path(__file__).resolve().parents[2];A=R/'analysis/continuation_II_ledger';lab='cdp:st:A.3.3'
rel=['records/continuation_II_ledger_events.tsv','analysis/continuation_II_ledger/completed_row_gates.json','analysis/continuation_II_ledger/printed_scope_overrides.json','S6_10_PAPERS_inventory.csv']
receipt=A/'A3_3_registration_receipt.json';backup=A/'A3_3_registration_before'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
if '--revert' in sys.argv:
    x=json.loads(receipt.read_text())
    assert all(h(R/p)==x['after_sha256'][p] for p in rel),'Files changed after this registration; review before reverting.'
    for i,p in enumerate(rel):shutil.copyfile(backup/f'{i:02d}_{Path(p).name}',R/p)
    print('Exact pre-registration files restored.');sys.exit()
assert not receipt.exists(),'Registration already exists; do not duplicate events.'
backup.mkdir(exist_ok=False)
before={}
for i,p in enumerate(rel):before[p]=h(R/p);shutil.copyfile(R/p,backup/f'{i:02d}_{Path(p).name}')
target=json.loads((A/'A3_3_target_opening_receipt.json').read_text())
proofsha=target['target_proof_sha256_without_trailing_newline']
gates=json.loads((R/rel[1]).read_text());assert lab not in gates
gates[lab]={
 'proof_rederivation_before_reading':f'complete: entire current one-step proof derived at 09:44:23 UTC before target reading; exact Picard cocycle translations/inverses, finite componentwise density, ideal-power multiplication and all unsplit lifting sequences matched. Current proof SHA256 {proofsha}. Evidence analysis/continuation_II_ledger/A3_3_before_read_receipt.json and A3_3_current_comparison.md.',
 'new_independent_computations':'complete: newly authored exact rational program A3_3_fresh.py passed 459 checks before target reading, including nonzero extension blocks, all tested filtration truncations/layers and component translation inverses. Bounds explicit; universal proof separate.',
 'renewed_main_result_credit_check':'complete for supporting-row source scope: original Stacks Tags 0B3P/0C4T, Divisors p26, and Tag 01DZ, Cohomology pp2-3 reopened and matched through the actual analytic Cartier and cohomology maps. Positive classical credit and hashes in A3_3_renewed_source_receipt.json; main-result repeated searches not applicable.'}
(R/rel[1]).write_text(json.dumps(gates,ensure_ascii=False,indent=2)+'\n')
scopes=json.loads((R/rel[2]).read_text());assert lab not in scopes
scopes[lab]={'date':'2026-11-19','scope_tex':'The whole current proof was independently derived at 09:44:23 UTC before target reading: actual Picard cocycle translations and inverses, finite dense-open intersections in the specified components, all Cartier graded-factor maps and the unsplit full-fibre induction. The new exact rational program passed 459 checks within its stated finite bounds; the universal proof is written separately. The original Stacks Cartier and cohomology inputs were reopened at Tags 0B3P and 0C4T, Divisors p.~26, and Tag 01DZ, Cohomology pp.~2--3. These inputs are classical; the supporting-row source gate is complete.','basis':'analysis/continuation_II_ledger/A3_3_current_comparison.md; analysis/continuation_II_ledger/A3_3_renewed_source_receipt.json'}
(R/rel[2]).write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
p=R/rel[0];rows=list(csv.DictReader(p.open(),delimiter='\t'));fields=list(rows[0]);who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation'
new=[('independent re-proof','Whole current A.3.3 proof independently derived and frozen at 09:44:23 UTC before reading the receiving proof; every current sentence matched. Actual Picard cocycle translations/inverses, componentwise dense finite intersections, ideal-power graded maps and all unsplit full-fibre induction steps are written. Evidence analysis/continuation_II_ledger/A3_3_before_read_receipt.json and A3_3_current_comparison.md. No source change or new mathematical-status change.'),('computation or formal certificate','Newly authored A3_3_fresh.py passed 459 exact rational checks before target reading: filtered maps with nonzero extension blocks for m=1..9 and dimensions1..3, every truncation/layer, and component translations/inverses for1..9 components. All bounded scopes explicit; universal proof is separate. Output code/continuation_II_ledger/A3_3_fresh.output.json.'),('used and rechecked in this run','Reopened original Stacks Divisors p26, Tags0B3P/0C4T, and Cohomology pp2-3, Tag01DZ; matched actual Cartier multiplication/unit transitions and the left-exact cohomology maps used through A.3.1. Classical input credit appended; this is a supporting-row source completion, not a main-result novelty claim. Evidence analysis/continuation_II_ledger/A3_3_renewed_source_receipt.json.')]
rows.extend(dict(statement_id=lab,date='2026-11-19',who=who,type=t,outcome=o) for t,o in new)
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=R/rel[3];rowsi=list(csv.DictReader(p.open()));fieldsi=list(rowsi[0]);matched=[]
for row in rowsi:
 if row['label']==lab:
  matched.append(dict(row));credit='Renewed 19 November 2026: the effective-Cartier multiplication and cohomology inputs are classical, explicitly verified in the original Stacks Divisors p26 Tags0B3P/0C4T and Cohomology pp2-3 Tag01DZ. The Picard cocycle inverse, density and full filtration induction were independently written here; no new main-result priority claim.'
  row['credited_to']=row['credited_to']+' | '+credit
  notes=json.loads(row['notes']);notes['continuation_A3_3_renewal']='All three applicable supporting-row gates complete; exact current-proof comparison, 459-check bounds and primary-source hashes in analysis/continuation_II_ledger/A3_3_current_comparison.md and A3_3_renewed_source_receipt.json. Existing proved status unchanged.';row['notes']=json.dumps(notes,ensure_ascii=False)
assert len(matched)==1
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fieldsi);w.writeheader();w.writerows(rowsi)
x={'registered_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'label':lab,'proof_sha256':proofsha,'added_raw_events':3,'owner_raw_events':len(rows),'all_three_registered':True,'source_mathematical_text_changed':False,'mathematical_status_changed':False,'before_sha256':before,'after_sha256':{p:h(R/p) for p in rel},'old_inventory_rows':matched,'evidence_sha256':{str(p.relative_to(R)):h(p) for p in [A/'A3_3_before_read_receipt.json',A/'A3_3_current_comparison.md',A/'A3_3_renewed_source_receipt.json']},'revert':'python code/continuation_II_ledger/register_A3_3.py --revert; hash guards prevent overwriting subsequent changes.'}
receipt.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'label':lab,'registered_at':x['registered_at'],'events':len(rows),'all_three':True,'receipt_sha256':h(receipt)}))
