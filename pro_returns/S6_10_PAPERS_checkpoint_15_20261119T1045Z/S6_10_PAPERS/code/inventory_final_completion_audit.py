"""Final receiving-completion audit. Writes only its own analysis receipts.

The canonical TeX, bibliography, PDFs, previews and AUX are read-only inputs.
No source-opening, alias or computation is turned into a proof verdict.
"""
from pathlib import Path
import collections, csv, datetime, hashlib, importlib.util, json, re

W=Path(__file__).resolve().parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def j(name): return json.loads((W/name).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
inventory=list(csv.DictReader((W/'S6_10_PAPERS_inventory.csv').open()))
status=j('analysis/inventory_manuscript_status.json')
aliases=j('analysis/inventory_receiving_statement_aliases.json')
same=j('analysis/sign_current_alias_identity.json')
events=j('analysis/inventory_current_events_by_label.json')
opening=j('analysis/inventory_opening_coverage_review.json')
citations=j('analysis/cited_source_audit.json')
counts=j('analysis/inventory_counts.json')
merge=j('analysis/inventory_current_event_merge.json')
verification=j('analysis/current_bibliography_verification.json')
dependency=j('analysis/inventory_night_dependency_reviews.json')
dependency_history=j('analysis/inventory_night_dependency_review_history.json')
known=j('analysis/inventory_final_known_input_matches.json')
iii_history=j('analysis/III_historical_checker_name_reconciliation.json')

spec=importlib.util.spec_from_file_location('final_event_reader',W/'code/inventory_current_events.py')
reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
fresh=collections.defaultdict(list)
for e in reader.events():fresh[e['label']].append(e)
assert dict(fresh)==events, 'Current event map is stale against its exact live ledgers.'
assert len(inventory)==1480 and counts['night_checkpoint']=='30'
assert not merge['unmatched_event_labels']
assert not aliases['conflicting_declarations']
assert aliases['statement_records']==1084

canonical={k:v[0]['canonical_label'] for k,v in aliases['by_label'].items()}
identity_map={x['alias']:x['canonical'] for x in same}
assert len(same)==14 and all(x['exact_identity'] for x in same)
for x in same:
    p=x['provenance'];assert len(p)==2
    assert all(p[0][k]==p[1][k] for k in ['source_file','start','end','sha256'])
    for q in p:
        text=(W.parents[1]/q['source_file']).read_text()
        assert hashlib.sha256(text[q['start']:q['end']].encode()).hexdigest()==q['sha256']
    assert any(e['type']=='A-identity' for e in events[x['alias']])

def resolve(label):
    seen=set()
    while label not in canonical and label in identity_map:
        assert label not in seen;seen.add(label);label=identity_map[label]
    return canonical.get(label)

row_ledger=[]
paper_dispositions=collections.defaultdict(collections.Counter)
for n,row in enumerate(inventory,2):
    notes=json.loads(row['notes'])
    for key in ['receiving_integration_pending','changed_proof_review_pending','new_checkpoint_proof_review_pending','current_dependency_metadata_audit_pending']:
        assert not notes.get(key),(row['label'],key)
    for g in notes.get('dependency_metadata_gates',[]):assert not g['pending'],row['label']
    is_compendium=bool(row['in_compendium_only_because'])
    target=resolve(row['label'])
    assert is_compendium or target,('No exact disposition',row['label'])
    d='compendium-only' if is_compendium else 'receiving statement or exact shared proof'
    paper_dispositions[row['paper']][d]+=1
    row_key=notes.get('row_key',row['source_run']+':'+row['source_id'])
    row_ledger.append(dict(csv_row=n,row_key=row_key,paper=row['paper'],label=row['label'],source_run=row['source_run'],source_id=row['source_id'],disposition=d,receiving_canonical_label=target or '',identity_rule='same source interval/hash and explicit A-identity event' if row['label'] in identity_map else 'literal declaration labels' if target else '',historical_source_status=notes.get('source_status',''),current_status=row['status'],current_event_count=len(events.get(row['label'],[])),reason=row['in_compendium_only_because']))
assert len({r['row_key'] for r in row_ledger})==1480
assert sum(x['disposition']=='compendium-only' for x in row_ledger)==364
assert sum(x['disposition']!='compendium-only' for x in row_ledger)==1116

empty_fields=['missing_inventory','wrong_paper_assignment','genuinely_unreviewed_receiving_arguments','partial_computation_or_disposition_scopes','lacking_argument_review_event','retained_refutations_without_argument_event','selection_labels_not_declared_in_body','provisional_exports_not_in_frozen_manuscript']
paper_summary={}
input_hashes={}
record_by_label={}
for p,r in status['papers'].items():
    for k in empty_fields:assert not r[k],(p,k,r[k])
    text='\n'.join((W/f).read_text() for f in r['source_paths'])
    assert hashlib.sha256(text.encode()).hexdigest()==r['source_sha256'],('stale manuscript snapshot',p)
    for f in r['source_paths']:input_hashes[f]=sha(W/f)
    paper_summary[p]={k:r[k] for k in ['statement_records','known_input_records','receiving_records','argument_review_or_exact_identity','exact_identity_records','refutation_review_records','open_records','bounded_audit_records']}
    paper_summary[p]['inventory_rows']=sum(x['paper']==p for x in inventory)
    paper_summary[p]['compendium_only_rows']=paper_dispositions[p]['compendium-only']
    paper_summary[p]['receiving_candidate_rows']=paper_dispositions[p]['receiving statement or exact shared proof']
    for rr in r['rows']:record_by_label[rr['label']]=rr

four={
 'inv:C3.8':'Paper I formal Open with a bounded operator check; no closed atlas theorem is asserted.',
 'inv:wb:uniform-nontorsion-provenance':'Paper II provenance-only record; no mathematical argument review is inferred.',
 'maps:src:D.2.2':'Paper III bounded archived computation/audit; its recorded scope is not a proof of the open classification.',
 'maps:src:D.2.4':'Paper III formal Open with the precise remaining classification scope.'}
nonarg={r['label'] for p in status['papers'].values() for r in p['rows'] if not r['compendium_or_known_input'] and not r['argument_reading_or_exact_identity_recorded']}
assert nonarg==set(four),(nonarg,four)
open_scopes={
 'ari:C.7.4':'Normalized theta-norm/transcendence question; the identities are proved and the unresolved conclusion remains Open in the final arithmetic section.',
 'inv:C3.8':'Literal coefficient atlas for global Bott–Chern representatives; the bounded operator verification is retained.',
 'inv:E2.3':'Remaining comb-kernel splitting data; the displayed partial results retain their current argument review.',
 'maps:src:D.2.4':'The remaining classification question, with its exact stated scope.',
 'night:P3K.75':'Remaining selected-I3 M2 compact-return/cap/norm/fan comparisons, additional marked singular sites and remaining holomorphic endpoints. Completed M6 selected-I3/all-reduced-cap and M2 order-three-good-cap scopes are removed by the proved six-step reduction.'}
assert {x for p in status['papers'].values() for x in p['open_records']}==set(open_scopes)
assert {r['label'] for r in inventory if r['status'].startswith('open')}==set(open_scopes)
assert all('Open' in r['kind'] for r in inventory if r['label']=='ari:C.7.4')

ii=status['papers']['II']['rows']
ii_d=[r for r in ii if 'argument_review' in r['event_kinds']]
assert len(ii_d)==246
assert sum(r['open'] for r in ii_d)==1
assert [r['label'] for r in ii if 'refutation_review' in r['event_kinds']]==['night:P3K.36']
assert paper_summary['II']['receiving_records']==248
assert all(v['state']=='checked' for v in dependency.values())
assert not opening['pending_groups'] and not opening['invalid_step_counts']
assert opening['proof_ladders']==68 and opening['rung_count']==69
plan=[g for g in opening['groups'] if re.fullmatch(r'(?:I|II|III|IV|V|VI)\.\d+',g['plan_item'])]
assert len(plan)==59,len(plan)
assert all(g['disposition']=='covered' for g in opening['groups'])

expected_nonoperative={'CrRubin1991','bertrand1984','pham2025sigma','silverman1983specialization','tate1983variation'}
assert set(citations['I']['pending_keys'])==expected_nonoperative
assert set(citations['I']['unverified_nonoperative_keys'])==expected_nonoperative
source_summary={}
for p,c in citations.items():
    assert not c['operative_pending_keys'] and not c['missing_bib_entries'],p
    if p!='I':assert not c['pending_keys'],p
    source_summary[p]=dict(cited_keys=len(c['cited_keys']),bounded_verified_keys=len(c['bounded_reading_keys']),unverified_nonoperative_keys=c['unverified_nonoperative_keys'],operative_pending_keys=[],missing_bib_entries=[])
assert len(verification['matched_keys'])==348
assert known['rows_changed']==11 and known['cells_changed']==22
assert all('exact citation pending current verification' not in r['in_compendium_only_because'] for r in inventory if r['paper']=='II')

remaining_gate_dispositions=[]
for label,ee in events.items():
    for e in ee:
        raw=e['raw_event'];gate=raw.get('remaining_gates','')
        if not gate:continue
        if gate.startswith('None in this reviewed scope;'):
            disposition='explicitly closed within this scope'
        elif e['type'].lower().startswith('bounded local') or raw.get('event_id') in {'IV-INV-U-001','IV-INV-U-002','IV-INV-U-003','IV-INV-U-004','IV-INV-U-005'}:
            assert 'Refuted' in gate
            disposition='deliberate local-use boundary; the historical compound remains Refuted, not an unreviewed retained argument'
        elif label=='night:P3K.107' and raw.get('event_id')=='IV-INV-D-010':
            assert gate.startswith('Final canonical cross-reference and layout review remains separate;')
            disposition='global canonical build QA retained as a separate parent task; all receiving mathematical and integration scopes closed by the later CP30 event'
        else:raise AssertionError(('Unclassified remaining gate',label,raw.get('event_id'),gate))
        remaining_gate_dispositions.append(dict(label=label,event_id=raw.get('event_id'),verbatim=gate,disposition=disposition))

historical_night=[r for r in inventory if r['source_run']=='S6_06_BLIND']
night_status=collections.Counter(json.loads(r['notes']).get('source_status') for r in historical_night)
assert dict(night_status)=={'Proved':249,'Refuted':35,'Known':3,'Open':1},night_status
assert all(r['status'].startswith('refuted compound source claim') for r in historical_night if json.loads(r['notes']).get('source_status')=='Refuted')

ledger_path=W/'analysis/inventory_final_row_dispositions.tsv'
with ledger_path.open('w',newline='') as f:
    cw=csv.DictWriter(f,fieldnames=list(row_ledger[0]),delimiter='\t');cw.writeheader();cw.writerows(row_ledger)

receipt_inputs=['S6_10_PAPERS_inventory.csv','analysis/inventory_manuscript_status.json','analysis/inventory_current_events_by_label.json','analysis/inventory_receiving_statement_aliases.json','analysis/sign_current_alias_identity.json','analysis/inventory_opening_coverage_review.json','analysis/inventory_opening_ladders.json','analysis/cited_source_audit.json','analysis/current_bibliography_verification.json','analysis/final_source_gate_dispositions.json','analysis/inventory_final_known_input_matches.json','analysis/III_historical_checker_name_reconciliation.json','analysis/IV_sign_third_batch_receiving_receipt.json','analysis/inventory_iv_receiving_integration_verification.json','analysis/inventory_night_dependency_reviews.json','analysis/inventory_night_dependency_review_history.json','analysis/I_final_arithmetic_presentation.json','analysis/sign_final_opening_coverage_receipt.json','analysis/inventory_final_row_dispositions.tsv']
input_hashes.update({p:sha(W/p) for p in receipt_inputs})
receipt=dict(recorded_at=NOW,checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)',scope='Read-only comparison of final receiving fragments, exact current event ledgers, aliases, source dispositions and opening map. This audit creates no new theorem/independence credit. Only the separately authorized administrative eleven-row reason refresh and current-event merge preceded it; canonical sources/AUX are not edited by this audit.',receiving_mathematical_completion=True,true_completion_blockers=[],inventory_rows=len(inventory),source_counts={k:counts[k] for k in ['source_s6_09_rows','source_unique_s6_09_labels','source_night_rows','night_checkpoint','source_night_statuses','supplementary_source_rows','new_writing_rows','unregistered_night_export_rows']},compendium_only_rows=364,receiving_candidate_rows=1116,row_disposition_ledger='analysis/inventory_final_row_dispositions.tsv',statement_record_declarations=1084,known_cited_input_declarations=11,receiving_records=1073,receiving_argument_deduction_identity_or_refutation_coverage=1069,coverage_count_is_not_independent_proved_theorem_count=True,papers=paper_summary,II_precise_breakdown=dict(receiving_records=248,D_scopes=246,completed_argument_scopes=245,proved_partial_results_for_open_inv_E2_3=1,provenance_records=1,historical_compound_refutation_records=1,inventory_D_scopes_including_compendium_RAT6=247,explicit_same_reading_aliases=14),four_nonargument_receiving_records=four,formal_open_questions=open_scopes,formal_open_unique_labels=5,formal_open_inventory_rows=7,all_historical_refuted_night_compounds_preserved=35,live_event_labels=len(events),inventory_rows_with_scoped_events=merge['source_rows_with_current_events'],unclosed_receiving_proof_gates=[],unclosed_receiving_identity_gates=[],unclosed_dependency_intake_gates=[],unclosed_operative_source_gates=[],remaining_gate_text_dispositions=remaining_gate_dispositions,literal_declaration_labels=len(aliases['by_label']),shared_literal_declarations=aliases['shared_header_statements'],conflicting_declarations=[],opening=dict(proof_ladders=68,rung_zero_blocks=69,series_orientation_blocks_without_ladder=1,numbered_plan_items=59,extra_prompt_groups=3,new_night_main_groups=6,mapping_groups=len(opening['groups']),pending_groups=[],invalid_step_counts=[],record='analysis/inventory_opening_coverage_review.json'),bibliography=dict(distinct_bounded_verified_keys=348,papers=source_summary,unverified_nonoperative_keys=sorted(expected_nonoperative),source_dispositions='analysis/final_source_gate_dispositions.json'),administrative_repairs=dict(known_input_rows=11,known_input_cells=22,known_input_record='analysis/inventory_final_known_input_matches.json',III_checker_name_record='analysis/III_historical_checker_name_reconciliation.json',III_distinct_historical_labels=23,III_instances_including_preview=46,no_new_proof_credit=True),global_delivery_scope='Final canonical PDF/cross-reference/layout/package QA is owned by the root build receipts; it is not silently inferred from this mathematical coverage audit.',input_sha256=input_hashes)
(W/'analysis/inventory_final_completion_receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')

md=[f'# Final receiving-completion receipt\n\nRecorded {NOW}; checker: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro).\n',
'The final receiving audit finds **no unclosed receiving argument, exact-identity, added-dependency or operative-source gate**. The five expressly open mathematical conclusions retain Open status. This is a coverage and disposition audit; it adds no theorem or independent-review credit. Canonical PDF, cross-reference and layout completion is established separately by the root build receipts.\n',
'## Exact receiving counts\n\n| Paper | Metadata declarations | Known cited inputs | Receiving records | Argument/deduction/identity/refutation coverage |\n|---|---:|---:|---:|---:|']
for p,r in paper_summary.items():md.append(f"| {p} | {r['statement_records']} | {r['known_input_records']} | {r['receiving_records']} | {r['argument_review_or_exact_identity']} |")
md += ['| **Total** | **1084** | **11** | **1073** | **1069** |\n',
'The coverage column counts recorded scopes, not independent proved theorems. Paper II has 246 D scopes: 245 completed arguments and the verified partial results of Open `inv:E2.3`; its other two records are one provenance record and the explicit refutation of `night:P3K.36`. Its inventory-wide 247 D labels also include compendium-only `cdp:st:C.2.RAT.6`. Fourteen exact source aliases share reviewed proofs and add no independent review. Paper I includes one exact same-reading identity; Paper IV includes one short summary deduction and the fully reviewed corrected local arguments whose historical compounds remain refuted.\n',
'The four receiving records outside that coverage count are:\n']
for label,scope in four.items():md.append(f'- `{label}` — {scope}')
md += ['\n## Disposition of all source rows\n',
'All **1480 inventory rows** have a recorded destination: **364 compendium-only** rows with reasons and **1116 receiving candidates**, including preserved source duplicates and explicit aliases. The row-by-row TSV maps every candidate to its actual receiving statement or an exact shared proof. There are no unplaced rows, missing inventory labels, wrong-paper declarations or conflicting declarations. The source intake is CP30: 1184 S6_09 rows, 288 registered night rows, three supplementary source rows and five new writing rows. All 35 historical Refuted night compounds remain Refuted. The 1099 labels/1128 rows with current scoped events are provenance counts.\n',
'## Main-result openings and sources\n',
'There are **68 proof ladders**, each with 3–7 steps, plus one series-orientation rung-zero block. The exact opening map covers all **59 numbered plan items**, three additional prompt groups and six groups of new night main results. The repaired I.7, II.12 and II.13 openings are included. No main-result ladder or opening-scope gap remains.\n',
'The bibliography audit has **348 distinct bounded verified keys**, no missing entries and no operative pending key. Per-paper cited/matched counts are I 127/122, II 77/77, III 60/60, IV 57/57, V 16/16 and VI 50/50. The five unverified originals are explicitly nonoperative: `CrRubin1991`, `bertrand1984`, `pham2025sigma`, `silverman1983specialization` and `tate1983variation`; their exact dispositions and operative reproductions remain recorded. No source-reading credit was manufactured for those originals.\n',
'## Five formal Opens\n']
for label,scope in open_scopes.items():md.append(f'- `{label}` — {scope}')
md += ['\n## Administrative reconciliation\n',
'Eleven archived known-result reason cells and their eleven notes cells now cite their exact current source matches. The original pending wording remains in history; the change log records all 22 cells. The current-event merge includes the final sign receiving-text verification. Paper III’s 23 historical reviewer aliases (46 instances including preview) now use the exact model, effort and date from the source JSON; this gives no new proof credit.\n',
'The JSON receipt locks every audited receiving input by SHA256. The companion row-disposition TSV accounts for all 1480 rows. The audit did not edit canonical TeX, bibliography, PDFs, previews or AUX.\n']
(W/'analysis/inventory_final_completion_receipt.md').write_text('\n'.join(md))
print(json.dumps({k:receipt[k] for k in ['recorded_at','receiving_mathematical_completion','true_completion_blockers','inventory_rows','statement_record_declarations','receiving_records','receiving_argument_deduction_identity_or_refutation_coverage','formal_open_unique_labels']},indent=2))
