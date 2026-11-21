"""Bind root-frozen Paper I metadata; never edit TeX or root deliverables.

Execution is deliberately gated by explicit source and ledger SHA arguments.
Counts come from the root report and its hashed TSV. Page certification is
copied only from a matching, certified root coverage receipt.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,csv,hashlib,json,re,runpy

ap=argparse.ArgumentParser()
ap.add_argument('--source-sha',required=True)
ap.add_argument('--ledger-sha',required=True)
ap.add_argument('--ledger-rows',type=int,required=True)
ap.add_argument('--pdf-manifest',default=None)
ap.add_argument('--certified-coverage',default=None)
args=ap.parse_args()
W=Path('/workspace/scratch/653608133b22/work');O=W/'agents/i_provenance';NOW=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bound(p):return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)
def put(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
source=W/'S6_SERIES_PUBLISH_I.tex';ledger=W/'records/CHECK_EVENTS.tsv'
assert sha(source)==args.source_sha
assert sha(ledger)==args.ledger_sha
assert r'\bibitem[Neretin(2024)]{Neretin2024Beta}' in source.read_text()
ledger_rows=sum(1 for _ in csv.DictReader(ledger.open(),delimiter='\t'));assert ledger_rows==args.ledger_rows
tex=source.read_text();report_path=W/'records/S6_SERIES_PUBLISH_I_methodology_counts.json';report=json.loads(report_path.read_text())
counts_path=W/'records/S6_SERIES_PUBLISH_check_counts.tsv'
assert sha(ledger)==report['events_sha256']
assert sha(counts_path)==report['counts_sha256']
counts=next(r for r in csv.DictReader(counts_path.open(),delimiter='\t') if r['paper']=='I' and r['scope']=='current_printed_statements_and_definitions')
assert counts==report['counts']
keys=['targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"]
n=[int(counts[k]) for k in keys];env=int(counts['statements']);ids=int(counts['subject_identifiers']);assoc=int(counts['event_associations']);groups=int(counts['declared_evidence_groups']);outline=int(counts['outline_step_associations_separate']);assert sum(n)==assoc
method=re.search(r'\\subsection\{Methodology\}\s*(.*?)\s*\\subsection\{How the paper is organized\}',tex,re.S).group(1)
for number,phrase in zip(n,['examinations of proof steps','independent','computations or formal certificates','readings of the proofs and applications','uses of background results without a fault found','refutation']):
 assert re.search(str(number)+r'\s+'+re.escape(phrase),method),(number,phrase)
completion_path=W/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json';completion=json.loads(completion_path.read_text())
assert all(x['status']=='done' for x in completion['rows'].values() if x.get('paper')=='I')

# Create a current abstract/status scaffold only after every explicit gate above.
runpy.run_path(str(O/'code/S6_SERIES_PUBLISH_I_make_provenance_scaffold.py'),run_name='__scaffold__')
c=json.loads((O/'S6_SERIES_PUBLISH_I_three_way_claim_table_current.json').read_text());assert c['source_sha256']==args.source_sha and len(c['claims'])==42
assert all(x['source_occurrences']==1 for group in c['exact_main_status_binding'].values() for x in group.values())

prior_coverage=O/'S6_SERIES_PUBLISH_I_candidate11_complete_coverage_snapshot.json'
prior=json.loads(prior_coverage.read_text())
assert prior['all_pages_read'] and not prior['missing_pages']
assert prior['source_sha256']=='7479a42f0c18cb2853e483ba3b0b222087e800a6a720ca5f2a21313ff6706cc6'
assert prior['pdf_sha256']=='02033ddcb1602d22fc09bc05865e772392daadc54c93cb60da14c91f6dfe62cc'
assert prior['page_count']==341
pdf_info=None;certified=False;final_coverage=None
if args.pdf_manifest:
 mp=Path(args.pdf_manifest);man=json.loads(mp.read_text());pdf=Path(man['pdf']);assert sha(pdf)==man['pdf_sha256']
 pdf_info={**bound(pdf),'pages':man['pages'],'manifest':bound(mp),'reading_status':'pending'}
if args.certified_coverage:
 assert pdf_info is not None
 cp=Path(args.certified_coverage);co=json.loads(cp.read_text())
 assert co['source_sha256']==args.source_sha and co['pdf_sha256']==pdf_info['sha256']
 assert co['all_pages_read'] and co['certified'] and not co['missing_pages']
 assert co['covered_pages']==co['page_count']==pdf_info['pages']
 certified=True;final_coverage=bound(cp);pdf_info['reading_status']='complete; root certified coverage receipt bound'
gate=('Final rendered-page gate closed on the exact current source/PDF, as recorded in the root coverage receipt.' if certified else 'The earlier candidate11 was read completely on all 341 actual page images. Subsequent source corrections require their final changed-page rendering and root coverage certification; that gate remains pending.')
count_sentence=(f'Frozen root recomputation: {env:,} printed environments, {ids:,} tracked identifiers, {assoc:,} associations, {groups:,} declared evidence groups; {n[0]:,} targeted proof examinations, {n[1]:,} independent re-derivations, {n[2]:,} computations/formal certificates, {n[3]:,} used/reread associations, {n[4]:,} background associations, and {n[5]:,} refutation association'+('s' if n[5]!=1 else '')+f'. Separate outline associations: {outline:,}. Complete merged ledger: {ledger_rows:,} rows.')

d=json.loads((O/'S6_SERIES_PUBLISH_I_deposit_fields_scaffold.json').read_text())
for token,value in zip(['TARGETED','REPROOF','COMPUTATION','USED','BACKGROUND','REFUTED'],n):d['provenance']=d['provenance'].replace('{{'+token+'}}',f'{value:,}')
d['provenance']=d['provenance'].replace('The final ledger totals are to be inserted after the root source and CHECK_EVENTS freeze:','For the statements printed in this paper, the frozen ledger records').replace('1 refutations linked','1 refutation linked')
d['provenance']=d['provenance'].replace('Final statement/environment totals and evidence-group totals remain unbound in this scaffold.',count_sentence+' '+gate)
assert '{{' not in d['provenance']
put(O/'S6_SERIES_PUBLISH_I_deposit_fields.json',d)
binding=f'Source SHA-256: `{args.source_sha}`. CHECK_EVENTS SHA-256: `{args.ledger_sha}`. '+gate
if pdf_info:binding+=f" Current candidate PDF SHA-256: `{pdf_info['sha256']}` ({pdf_info['pages']} pages)."
section=['## Paper I','','### Title','',d['title'],'','### Abstract','',d['abstract'],'','### Comments','',d['comments'],'','### Provenance','',d['provenance'],'','### Subjects and classification','','Primary: '+d['subject']+'. Proposed cross-lists: '+', '.join(d['crossListSubjects'])+'. MSC2020: '+', '.join(d['mscCodes'])+'.','','Authorship mode: no human author claimed. Human understanding: none. License: CC0 1.0 Universal. Submission confirmations remain unset; no external submission was performed.','','### Source and review binding','',binding,'']
section_text='\n'.join(section);(O/'S6_SERIES_PUBLISH_I_deposit_fields.md').write_text('# Deposit fields — Paper I\n\n'+section_text);(O/'S6_SERIES_PUBLISH_I_methodology_bound.tex').write_text(method+'\n')

for row in c['claims']:
 row['deposit_location']='Paper I: Provenance; Comments; Abstract where applicable'
 row['remaining_gate']='None for the source/count/PDF metadata binding.' if certified else 'Final corrected candidate rendered-page coverage and exact source/PDF certification.'
 if row['id']=='I-P32':
  row.update(current_claim_or_issue='Duplicate keys, edition locators and protected title capitalization have been reconciled with the opened sources.',disposition='The duplicate DGKX/Grauert/Schroeer–Siebert keys are resolved and unused entries archived. BM95AB citations in Paper I are now consolidated under BM97 after actual comparison of the preprint and published result pages: analytic category (0.1)(2), p.208; Theorem1.6 and noncompact extension, p.215; Theorem1.10, p.216; Remark1.16 and canonical passage, p.221. The earlier arXiv v2 and its separate pagination remain explicit in the single printed entry and historical shared alias. Title capitalization, STW published metadata and the final citation-locator batches are applied. The complex beta identity is credited to the opened published Neretin source, with its exact parameter, measure and convergence-domain map retained in ari:C.8.7. Text-only Reyssat access is distinguished from page-image reads.',status='verified edition merger and bibliography corrections applied',primary_or_check_evidence='i_provenance/literature/S6_SERIES_PUBLISH_I_final_primary_locator_receipt.json; S6_SERIES_PUBLISH_I_Neretin2024_beta_locator_receipt.json; root/topology/marking exact primary locator receipts; guarded bibliography dispositions. No metadata opening is counted as a mathematical check.')
 if row['id']=='I-P35':row.update(disposition=count_sentence,status='current root count/source binding complete',count_comparison='Exact root report row, its count TSV hash and ledger hash agree; each current methodology value was checked. This binding adds no new count/check event.')
 if row['id']=='I-P36':row.update(current_claim_or_issue='Candidates follow each main result’s own outline and actual statement, immediate-proof and exact deferred-proof references.',disposition='The root parser attaches actual immediate and exact deferred proofs and each main theorem’s own outline, excluding hidden headers and unrelated further-results prose. Every Paper I required-check manifest row is done. Historical intake candidate counts remain historical metadata.',status='required dependency check completion bound',primary_or_check_evidence=str(completion_path))
 if row['id']=='I-P37':row.update(disposition='The original PDF was absent from the attached source directory and was recovered from the authenticated pinned checkpoint with the exact attached filelist hash. The 419-page destination/tag audit is a baseline mapping record, with no mathematical or final-page-reading credit.',status='attached absence and authenticated subsequent recovery recorded')
 if row['id']=='I-P39':row.update(disposition='The 78 operative source links in the end table are authenticated raw URLs at the full historical commit. Body computations retain their receiving-result map; new current-run checks are not attributed to that historical pin. Candidate11’s complete table was actually read; corrected table pagination is covered by the final rendering gate.',status='program authentication and body scope complete')
 if row['id']=='I-P42':row.update(disposition='The actual current Paper I abstract, scoped historical/current model facts and all 42 dispositions are synchronized with the frozen source and ledger. '+gate,status='exact current source/count/PDF binding complete' if certified else 'source/count synchronization complete; corrected-PDF gate pending',primary_or_check_evidence=str(prior_coverage)+('; '+str(final_coverage) if certified else '; current changed-page certificate pending'))
 if row['id']=='I-P34':row.update(disposition='Source and deposit identify the publication revision as 20–21 November 2026, current inherited effort without a separately exposed numeric setting, nonexclusive Sol contribution during 24 August–9 September and pinned README credit for Astra from 5 September. The historical inventory remains bounded rather than claiming all sessions/models.',status='historical/current model and date wording synchronized')

scope_receipts=[]
for p in [O/'literature/S6_SERIES_PUBLISH_I_final_primary_locator_receipt.json',O/'literature/S6_SERIES_PUBLISH_I_Drinfeld1973_locator_receipt.json',O/'literature/S6_SERIES_PUBLISH_I_candidate11_bibliography_metadata_receipt.json',O/'literature/S6_SERIES_PUBLISH_I_Neretin2024_beta_locator_receipt.json',O/'S6_SERIES_PUBLISH_I_candidate11_tail_comparison.json',O/'S6_SERIES_PUBLISH_I_candidate11_beta_comparison.json',W/'agents/root_primary/S6_SERIES_PUBLISH_I_root_primary_locator_receipt.json',W/'agents/i_topology/literature/S6_SERIES_PUBLISH_I_candidate11_primary_locator_closure.json',W/'records/S6_SERIES_PUBLISH_I_root_42_claim_review.json']:
 if p.exists():scope_receipts.append(bound(p))
c.update(recorded_utc=NOW,stage='source/count/PDF bound' if certified else 'source/count bound; corrected-PDF gate pending',counts=counts,counts_recomputed=False,counts_binding='Root frozen recomputation copied and verified; no separate mathematical event.',final_pdf=pdf_info,earlier_complete_page_coverage=bound(prior_coverage),final_coverage=final_coverage,additional_scope_receipts=scope_receipts,limitation=gate+' Historical model/date qualifications remain explicit.',mathematical_events_added=0)
put(O/'S6_SERIES_PUBLISH_I_three_way_claim_table_final.json',c)
def cell(x):return str(x).replace('|','\\|').replace('\n',' ')
md=['# Paper I: source/count-bound three-way provenance','',binding,'','| ID | Claim and location | Records / primary evidence | Current resolution |','|---|---|---|---|']
for row in c['claims']:md.append('| '+' | '.join(cell(x) for x in [row['id'],row['current_claim_or_issue']+' — '+row['current_location'],row['attached_record_comparison']+' '+row['primary_or_check_evidence'],row['disposition']+' '+row['status']])+' |')
(O/'S6_SERIES_PUBLISH_I_three_way_claim_table_final.md').write_text('\n'.join(md)+'\n')

shared_tsv=W/'S6_SERIES_PUBLISH_provenance_checks.tsv'
with shared_tsv.open() as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;prior_rows=[x for x in r if x['paper']!='I']
newrows=[]
for row in c['claims']:
 values=[row['id'],'I',row['current_location'],row['current_claim_or_issue'],row['attached_record_comparison'],row['count_comparison'],row['primary_or_check_evidence'],row['remaining_gate'],json.dumps({'source_sha256':args.source_sha,'ledger_sha256':args.ledger_sha,'count_report':str(report_path),'final_binding_receipt':str(O/'S6_SERIES_PUBLISH_I_final_source_count_binding.json')},ensure_ascii=False),row['current_claim_or_issue'],row['attached_record_comparison'],'Historical intake counts remain historical only.',row['primary_or_check_evidence'],row['current_location'],row['deposit_location'],row['status'],row['remaining_gate'],row['old_HEXAGON_METADATA_V_comparison'],row['disposition']]
 assert len(fields)==len(values)
 newrows.append(dict(zip(fields,values)))
def tsv(p,rows):
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
tsv(O/'S6_SERIES_PUBLISH_I_provenance_checks.tsv',newrows);tsv(O/'S6_SERIES_PUBLISH_provenance_checks_with_I_proposed.tsv',prior_rows+newrows)
shared_md=W/'S6_SERIES_PUBLISH_deposit_fields.md';sm=shared_md.read_text();m=re.search(r'^## Paper I\s*$',sm,re.M)
if m:
 rest=re.search(r'^## Paper (?:II|III|IV|V|VI|VII)\s*$',sm[m.end():],re.M);end=m.end()+rest.start() if rest else len(sm);sm=sm[:m.start()]+section_text+sm[end:]
else:sm=sm.rstrip()+'\n\n'+section_text
(O/'S6_SERIES_PUBLISH_deposit_fields_with_I_proposed.md').write_text(sm)
guard=dict(created_utc=NOW,scope='Replace/append Paper I rows and deposit section only; preserve all other paper data. '+gate,source_sha256=args.source_sha,ledger_sha256=args.ledger_sha,math_events_added=0,updates=[dict(target=str(shared_tsv),expected_sha256=sha(shared_tsv),replacement=bound(O/'S6_SERIES_PUBLISH_provenance_checks_with_I_proposed.tsv')),dict(target=str(shared_md),expected_sha256=sha(shared_md),replacement=bound(O/'S6_SERIES_PUBLISH_deposit_fields_with_I_proposed.md'))])
put(O/'S6_SERIES_PUBLISH_I_shared_provenance_deposit_guard.json',guard)
receipt=dict(created_utc=NOW,stage=c['stage'],source=bound(source),root_count_report=bound(report_path),root_count_report_source_sha256=report['source_sha256'],source_successor_scope='Current methodology values are checked against the frozen report. Any difference between its counting-source hash and the final source hash is recorded explicitly; no count recomputation is claimed.',counts_file=bound(counts_path),statement_counts_file=bound(W/'records/S6_SERIES_PUBLISH_statement_check_counts.csv'),ledger=bound(ledger),merged_ledger_rows=ledger_rows,counts=counts,candidate_pdf=pdf_info,earlier_complete_page_coverage=bound(prior_coverage),final_coverage=final_coverage,pdf_review_status='certified' if certified else 'corrected candidate pending',claim_count=42,all_21_exact_main_status_strings_present_once=True,completion_manifest=bound(completion_path),deposit_json=bound(O/'S6_SERIES_PUBLISH_I_deposit_fields.json'),deposit_md=bound(O/'S6_SERIES_PUBLISH_I_deposit_fields.md'),claim_table=bound(O/'S6_SERIES_PUBLISH_I_three_way_claim_table_final.json'),claim_tsv=bound(O/'S6_SERIES_PUBLISH_I_provenance_checks.tsv'),shared_update_guard=bound(O/'S6_SERIES_PUBLISH_I_shared_provenance_deposit_guard.json'),additional_scope_receipts=scope_receipts,mathematical_events_added=0,external_submission_performed=False)
put(O/'S6_SERIES_PUBLISH_I_final_source_count_binding.json',receipt)
print(json.dumps(dict(source=args.source_sha,ledger=args.ledger_sha,counts=counts,merged_rows=ledger_rows,claims=42,pdf_gate=receipt['pdf_review_status'],shared_guard=str(O/'S6_SERIES_PUBLISH_I_shared_provenance_deposit_guard.json')),indent=2))
