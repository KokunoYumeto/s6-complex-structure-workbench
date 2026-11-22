from pathlib import Path
import csv,datetime as dt,difflib,hashlib,io,json
R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def append_table(path,row):
 old=path.read_bytes();rd=csv.DictReader(io.StringIO(old.decode()),delimiter='\t');rows=list(rd)
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=rd.fieldnames,delimiter='\t',lineterminator='\n');w.writerow({k:row.get(k,'') for k in rd.fieldnames})
 with path.open('ab') as f:f.write(out.getvalue().encode())
 assert path.read_bytes().startswith(old)
 return dict(path=str(path.relative_to(R)),before_sha256=sha(old),after_sha256=sha(path.read_bytes()),before_rows=len(rows),added_rows=1)
rp=R/'records/S6_SERIES_PUBLISH_II_records_link_correction.json';assert not rp.exists()
src=R/'S6_SERIES_PUBLISH_II.tex';before=src.read_bytes();s=before.decode()
old=r'\newcommand{\SsixPublishRecords}{https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/1fb9194767aef92abcc06071e3820c2f226b9512/pro_returns/S6_SERIES_PUBLISH_checkpoint_10_20261121T0612Z/}'
new=r'\newcommand{\SsixPublishRecords}{https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/e3c65b6bfd9749f020aeb35aa37cd26d4148c6c1/pro_returns/S6_SERIES_PUBLISH_checkpoint_21_20261122T0026Z/}'
assert s.count(old)==1
newtext=s.replace(old,new,1)
assert s.split(r'\begin{document}',1)[1]==newtext.split(r'\begin{document}',1)[1]
assert newtext.count(r'\href{\SsixPublishRecords}')==1
ledger=(R/'CHECK_EVENTS.tsv').read_bytes()
diff=''.join(difflib.unified_diff(s.splitlines(True),newtext.splitlines(True),fromfile=src.name+'.before',tofile=src.name+'.after'))
diffpath=R/'records/S6_SERIES_PUBLISH_II_records_link_correction.diff';assert not diffpath.exists();diffpath.write_text(diff)
now=dt.datetime.now(dt.timezone.utc).isoformat()
provenance=R/'S6_SERIES_PUBLISH_provenance_checks.tsv'
assert not any(r['claim_id']=='II-C2-P01' for r in csv.DictReader(provenance.open(),delimiter='\t'))
src.write_text(newtext)
changes=[]
changes.append(append_table(R/'S6_SERIES_PUBLISH_defects_II.tsv',dict(change_id='II-C2-RECORDS-LINK-001',type='D15,D18',statement_id='Methodology',old_location='preamble SsixPublishRecords; methodology single records link',new_location='same macro and callsite',new_page='pending integrated PDF',old_text=old,new_text=new,reason='Continuation prompt section0.2/0.3 explicitly prescribes checkpoint21 as the interim records destination. The inherited macro still named checkpoint10. The final deposit will bind the final records commit.',review_status='Exact macro read and corrected; document body byte-identical. Primary online opening attempted and remains unverified.')))
changes.append(append_table(provenance,dict(claim_id='II-C2-P01',paper='II',locations='Preamble SsixPublishRecords and methodology records link',claim='Interim records link names the prescribed pinned checkpoint21 directory, pending final deposit records commit.',against_records='Exact URL and commit match the continuation prompt; attached checkpoint21 payload and base manifest were independently hash-verified at restoration.',by_recomputation='Exact old macro occurred once and was replaced once; the document body is byte-identical and the macro has one methodology href callsite.',against_primary_source='OPEN: GitHub pinned tree and raw pinned report opening attempts returned DisabledError; no successful online retrieval is claimed.',required_action='Open the pinned location successfully or verify through the final authenticated deposit repository; update the one macro to the final records folder at deposit.',evidence=str(rp.relative_to(R)),prior_claim=old,current_paper_location='Methodology single records link',current_deposit_location='Pending final PaperII deposit fields',resolution_status='Source corrected; primary-source and final-deposit binding open',remaining_gate='Successful primary pinned-link opening and final records commit',current_resolution='The user-prescribed checkpoint21 macro is in the current source. No claim of successful online availability or final provenance completion is made.')))
assert (R/'CHECK_EVENTS.tsv').read_bytes()==ledger
record=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(src.read_bytes()),old_macro=old,new_macro=new,body_exactly_unchanged=True,methodology_calls=1,ledger_unchanged=True,mathematical_events_added=0,page_reading_credit=0,primary_opening_attempts=[dict(url='https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/e3c65b6bfd9749f020aeb35aa37cd26d4148c6c1/pro_returns/S6_SERIES_PUBLISH_checkpoint_21_20261122T0026Z/',ref='turn294556595view0',outcome='DisabledError'),dict(url='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/e3c65b6bfd9749f020aeb35aa37cd26d4148c6c1/pro_returns/S6_SERIES_PUBLISH_checkpoint_21_20261122T0026Z/S6_SERIES_PUBLISH_report.md',ref='turn502747105view0',outcome='DisabledError')],diff=dict(path=str(diffpath.relative_to(R)),sha256=sha(diffpath.read_bytes())),table_appends=changes,other_paper_sources_opened=False)
rp.write_text(json.dumps(record,indent=2)+'\n')
note=f'\n\n## Paper II interim records link — {now}\n\nThe records macro now names the checkpoint21 folder and commit prescribed by the continuation prompt. The inherited checkpoint10 destination was an uncorrected provenance instance. Only the macro changed; the document body, all mathematics, and the event ledger are byte-identical. One D15/D18 instance and provenance claim II-C2-P01 are recorded in `{rp.relative_to(R)}`. Both online opening attempts returned DisabledError, so successful pinned-link retrieval and final-deposit binding remain open. No proof-check, defect-class completion or page-reading credit is assigned.\n'
for name in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
 with (R/name).open('a') as f:f.write(note)
print(json.dumps(dict(record=str(rp.relative_to(R)),source_sha256=sha(src.read_bytes()),claim='II-C2-P01',primary_gate='open'),indent=2))
