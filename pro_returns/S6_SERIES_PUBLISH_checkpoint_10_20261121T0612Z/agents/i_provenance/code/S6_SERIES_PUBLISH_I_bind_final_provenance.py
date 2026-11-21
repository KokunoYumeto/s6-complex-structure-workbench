from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

W=Path('/workspace/scratch/653608133b22/work')
O=W/'agents/i_provenance'
NOW=datetime.now(timezone.utc).isoformat()
EXPECTED='7479a42f0c18cb2853e483ba3b0b222087e800a6a720ca5f2a21313ff6706cc6'
PDF_EXPECTED='02033ddcb1602d22fc09bc05865e772392daadc54c93cb60da14c91f6dfe62cc'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bound(p):return {'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
def put(p,j):p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
source=W/'S6_SERIES_PUBLISH_I.tex'; tex=source.read_text()
assert sha(source)==EXPECTED
report_path=W/'records/S6_SERIES_PUBLISH_I_methodology_counts.json'
report=json.loads(report_path.read_text())
counts_path=W/'records/S6_SERIES_PUBLISH_check_counts.tsv'
ledger=W/'records/CHECK_EVENTS.tsv'
assert sha(ledger)==report['events_sha256']
assert sha(counts_path)==report['counts_sha256']
rows=list(csv.DictReader(counts_path.open(),delimiter='\t'))
counts=next(r for r in rows if r['paper']=='I' and r['scope']=='current_printed_statements_and_definitions')
assert counts==report['counts']
keys=['targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"]
assert [int(counts[k]) for k in keys]==[767,10,143,689,194,1]
assert sum(int(counts[k]) for k in keys)==1804
assert [int(counts[k]) for k in ['statements','subject_identifiers','event_associations','declared_evidence_groups','outline_step_associations_separate']]==[331,351,1804,1605,0]
assert sum(1 for _ in csv.DictReader(ledger.open(),delimiter='\t'))==7824
method=re.search(r'\\subsection\{Methodology\}\s*(.*?)\s*\\subsection\{How the paper is organized\}',tex,re.S).group(1)
for n,phrase in [(767,'examinations of proof steps'),(10,'independent'),(143,'computations or formal certificates'),(689,'readings of the proofs and applications'),(194,'uses of background results without a fault found'),(1,'refutation')]:
 assert re.search(str(n)+r'\s+'+re.escape(phrase),method),(n,phrase)
manifest=json.loads((W/'render/I_candidate11/manifest.json').read_text())
assert manifest['pdf_sha256']==PDF_EXPECTED and manifest['pages']==341
pdf=Path(manifest['pdf']);assert sha(pdf)==PDF_EXPECTED
completion=json.loads((W/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())
assert all(r['status']=='done' for r in completion['rows'].values() if r.get('paper')=='I')

d=json.loads((O/'S6_SERIES_PUBLISH_I_deposit_fields_scaffold.json').read_text())
tokens=['TARGETED','REPROOF','COMPUTATION','USED','BACKGROUND','REFUTED']
for token,key in zip(tokens,keys):d['provenance']=d['provenance'].replace('{{'+token+'}}',counts[key])
d['provenance']=d['provenance'].replace('The final ledger totals are to be inserted after the root source and CHECK_EVENTS freeze:','For the statements printed in this paper, the frozen ledger records').replace('1 refutations linked','1 refutation linked')
d['provenance']=d['provenance'].replace('Final statement/environment totals and evidence-group totals remain unbound in this scaffold.','The current source contains 331 printed theorem-like environments with 351 tracked statement identifiers, including retained aliases. These give 1,804 event-to-statement associations and 1,605 declared evidence groups; there are no separate outline-step associations in this scope. The complete merged series ledger has 7,824 rows. These counts are bound to the current source and frozen count files in the accompanying receipt. The final rendered-PDF review remains pending.')
assert '{{' not in d['provenance']
put(O/'S6_SERIES_PUBLISH_I_deposit_fields.json',d)
section=['## Paper I','','### Title','',d['title'],'','### Abstract','',d['abstract'],'','### Comments','',d['comments'],'','### Provenance','',d['provenance'],'','### Subjects and classification','','Primary: '+d['subject']+'. Proposed cross-lists: '+', '.join(d['crossListSubjects'])+'. MSC2020: '+', '.join(d['mscCodes'])+'.','','Authorship mode: no human author claimed. Human understanding: none. License: CC0 1.0 Universal. Submission confirmations remain unset; no external submission was performed.','','### Source and review binding','',f'Source SHA-256: `{EXPECTED}`. Candidate 11 PDF SHA-256: `{PDF_EXPECTED}` (341 pages). Source and count synchronization is complete; actual final-PDF reading is pending.','']
section_text='\n'.join(section)
(O/'S6_SERIES_PUBLISH_I_deposit_fields.md').write_text('# Deposit fields — Paper I\n\n'+section_text)
(O/'S6_SERIES_PUBLISH_I_methodology_bound.tex').write_text(method+'\n')

c=json.loads((O/'S6_SERIES_PUBLISH_I_three_way_claim_table_current.json').read_text())
assert c['source_sha256']==EXPECTED and len(c['claims'])==42
assert all(v['source_occurrences']==1 for group in c['exact_main_status_binding'].values() for v in group.values())
overrides={
 'I-P01':('Current title and Paper I identity are copied to the deposit fields. The exact seven mechanism, status and known/new rows each occur once in the frozen source.','source/deposit identity synchronized'),
 'I-P07':('The completed targeted isogeny-distribution check is included in the frozen ledger under its original event identity and scope; no extra computation or re-proof credit is created by this table.','check merged; source/count binding complete'),
 'I-P11':('The credited appendix retains the supplied 8 September working-edition history as attributed historical information. Official arXiv metadata verifies the DGKX version-1 date of 23 September. The later pinned README and observed backlink do not independently authenticate the exact earlier proof publication date.','historical scope qualified and applied'),
 'I-P34':('The source and deposit both give the publication revision as 20–21 November 2026 and the current effort as inherited, with no separate numerical setting exposed. No current numerical effort setting is invented.','production wording and final numeric fields synchronized'),
 'I-P35':('Frozen root recomputation: 331 printed environments, 351 tracked identifiers, 1,804 associations, 1,605 declared evidence groups; 767 targeted proof examinations, 10 independent re-derivations, 143 computations/formal certificates, 689 used/reread associations, 194 background associations, and one refutation association. Separate outline associations: zero. Complete merged ledger: 7,824 rows.','final source/count binding complete'),
 'I-P36':('The root parser attaches actual immediate and exact deferred proofs and each main theorem\'s own outline, excluding hidden headers and unrelated further-results prose. All Paper I entries in the required-check completion manifest are done, including inv:B1.0 and night:P5.7. Historical intake candidate counts remain historical metadata.','required dependency checks completed; final scope frozen'),
 'I-P37':('The original PDF was absent from the attached source directory. It has now been recovered from the authenticated pinned checkpoint with the filelist hash. The 419-page baseline destination/tag sample audit is recorded separately; it is neither mathematical checking nor final rendered-page reading.','attached absence and subsequent authenticated recovery both recorded'),
 'I-P42':('Paper I deposit and all 42 provenance dispositions are bound to the frozen current source and root count files. The candidate-11 PDF hash is recorded, but its 341-page final rendered reading remains pending; no Paper V page certification is transferred.','source/count synchronization complete; final PDF gate pending')}
for r in c['claims']:
 if r['id'] in overrides:r['disposition'],r['status']=overrides[r['id']]
 else:r['status']=r['status'].replace('final gate open','final rendered-PDF gate pending').replace('final PDF gate remains open','final rendered-PDF gate pending').replace('final PDF gate open','final rendered-PDF gate pending')
 r['deposit_location']='Paper I: Provenance; Comments; Abstract where applicable'
 r['remaining_gate']='Actual complete candidate-11 rendered-page review and resulting final review receipt.'
 if r['id']=='I-P35':r['count_comparison']='Exact root frozen-count row and methodology values agree; bound hashes are in the final source/count receipt.'
 if r['id']=='I-P36':r['primary_or_check_evidence']='Root precise immediate/deferred-proof dependency scope and S6_SERIES_PUBLISH_required_check_completion_manifest.json; every Paper I manifest row is done.'
 if r['id']=='I-P37':r['primary_or_check_evidence']='Attached filelist and source inventory; recovered baseline SHA e4a7f4abd0e21a776e8ec0d1ab7e643d2346493465782c91ac5b1832fa69daba; S6_SERIES_PUBLISH_I_baseline_tag_sample_audit.json.'
c.update(recorded_utc=NOW,stage='source and count bound; rendered-PDF gate pending',counts_recomputed=False,counts_binding='Frozen root recomputation copied and checked against its exact count row, ledger hash and current methodology; no second independent count event.',counts=counts,final_pdf={'path':str(pdf),'sha256':PDF_EXPECTED,'pages':341,'reading_status':'pending'},limitation='No final rendered-PDF certification is made by this metadata receipt. The bounded historical session/date attribution limitations remain explicit.',mathematical_events_added=0)
put(O/'S6_SERIES_PUBLISH_I_three_way_claim_table_final.json',c)
md=['# Paper I: source/count-bound three-way provenance','','Source and count synchronization is complete. Final rendered-page review remains pending. No mathematical event is created by this record.','',f'Source SHA-256: `{EXPECTED}`.','','| ID | Claim and location | Records / primary evidence | Current resolution |','|---|---|---|---|']
def cell(x):return str(x).replace('|','\\|').replace('\n',' ')
for r in c['claims']:md.append('| '+' | '.join(cell(x) for x in [r['id'],r['current_claim_or_issue']+' — '+r['current_location'],r['attached_record_comparison']+' '+r['primary_or_check_evidence'],r['disposition']+' '+r['status']])+' |')
(O/'S6_SERIES_PUBLISH_I_three_way_claim_table_final.md').write_text('\n'.join(md)+'\n')
shared_tsv=W/'S6_SERIES_PUBLISH_provenance_checks.tsv'
with shared_tsv.open() as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;previous=list(reader)
assert not any(r['paper']=='I' for r in previous)
newrows=[]
for r in c['claims']:
 newrows.append(dict(zip(fields,[r['id'],'I',r['current_location'],r['current_claim_or_issue'],r['attached_record_comparison'],r['count_comparison'],r['primary_or_check_evidence'],'Finish and bind the actual candidate-11 rendered-page review.',json.dumps({'source_sha256':EXPECTED,'count_report':str(report_path),'final_binding_receipt':str(O/'S6_SERIES_PUBLISH_I_final_source_count_binding.json')},ensure_ascii=False),r['current_claim_or_issue'],r['attached_record_comparison'],'Historical intake counts remain historical only.',r['primary_or_check_evidence'],r['current_location'],r['deposit_location'],r['status'],r['remaining_gate'],r['old_HEXAGON_METADATA_V_comparison'],r['disposition']])))
def tsv(p,rows):
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
tsv(O/'S6_SERIES_PUBLISH_I_provenance_checks.tsv',newrows)
tsv(O/'S6_SERIES_PUBLISH_provenance_checks_with_I_proposed.tsv',previous+newrows)
shared_md=W/'S6_SERIES_PUBLISH_deposit_fields.md'
(O/'S6_SERIES_PUBLISH_deposit_fields_with_I_proposed.md').write_text(shared_md.read_text().rstrip()+'\n\n'+section_text)
guard={'created_utc':NOW,'scope':'Append only the 42 source/count-bound Paper I provenance rows and Paper I deposit section; preserve existing Paper V rows/text. PDF review remains pending.','updates':[{'target':str(shared_tsv),'expected_sha256':sha(shared_tsv),'replacement':bound(O/'S6_SERIES_PUBLISH_provenance_checks_with_I_proposed.tsv')},{'target':str(shared_md),'expected_sha256':sha(shared_md),'replacement':bound(O/'S6_SERIES_PUBLISH_deposit_fields_with_I_proposed.md')}],'source_sha256':EXPECTED,'math_events_added':0}
put(O/'S6_SERIES_PUBLISH_I_shared_provenance_deposit_guard.json',guard)
hist=O/'S6_SERIES_PUBLISH_I_historical_model_qualification_guard.json'
hj=json.loads(hist.read_text());hj['root_selected_source_present']=True;hj['final_observed_source_sha256']=EXPECTED;hj['final_observed_utc']=NOW;put(hist,hj)
receipt={'created_utc':NOW,'stage':'source/count synchronization complete; final rendered-PDF gate pending','source':bound(source),'root_count_report':bound(report_path),'root_count_report_source_sha256':report['source_sha256'],'source_successor_scope':'Parent reports the only successor change was moving the identical full repository commit onto a centered line to fix an overfull box. Count values and the full current methodology have been checked here; no count rerun or mathematical event is claimed.','counts_file':bound(counts_path),'statement_counts_file':bound(W/'records/S6_SERIES_PUBLISH_statement_check_counts.csv'),'ledger':bound(ledger),'merged_ledger_rows':7824,'counts':counts,'candidate_pdf':bound(pdf),'candidate_pages':341,'pdf_review_status':'pending','claim_count':42,'all_21_exact_main_status_strings_present_once':True,'completion_manifest':bound(W/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'),'deposit_json':bound(O/'S6_SERIES_PUBLISH_I_deposit_fields.json'),'deposit_md':bound(O/'S6_SERIES_PUBLISH_I_deposit_fields.md'),'claim_table':bound(O/'S6_SERIES_PUBLISH_I_three_way_claim_table_final.json'),'claim_tsv':bound(O/'S6_SERIES_PUBLISH_I_provenance_checks.tsv'),'shared_update_guard':bound(O/'S6_SERIES_PUBLISH_I_shared_provenance_deposit_guard.json'),'historical_model_scope_receipt':bound(hist),'mathematical_events_added':0,'external_submission_performed':False}
put(O/'S6_SERIES_PUBLISH_I_final_source_count_binding.json',receipt)
print(json.dumps({'source_sha256':EXPECTED,'counts':counts,'claims':42,'ledger_rows':7824,'pdf_review':'pending','shared_guard':str(O/'S6_SERIES_PUBLISH_I_shared_provenance_deposit_guard.json')}))
