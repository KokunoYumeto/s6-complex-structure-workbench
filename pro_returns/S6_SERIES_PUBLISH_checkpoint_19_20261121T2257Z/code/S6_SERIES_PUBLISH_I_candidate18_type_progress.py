#!/usr/bin/env python3
"""Record individual source-type progress, with later actual findings held open."""
from pathlib import Path
import datetime, hashlib, json, re
R=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
assert sha(R/'S6_SERIES_PUBLISH_I.tex')==expected
dp=R/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate18_type_closure_preparation.json'
assert sha(dp)=='527c26a57e40204709ad4880756a688ef900de84b9dfa12cb2f91276832078b2'
d=json.loads(dp.read_text())
assert d['source_sha256']==expected and d['unique_edit_rows']==2196
assert d['continuation_unique_edit_rows']==243 and not d['final_certified']
assert sha(R/d['pdf_path'])==d['pdf_sha256']
assert sha(R/d['defect_log_path'])==d['defect_log_sha256']
assert sha(R/'CHECK_EVENTS.tsv')=='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
opened=['D02','D08','D23']
closed=[x['type_id'] for x in d['rows'] if x['type_id'] not in opened]
assert len(closed)==22
for x in d['rows']:
 if x['type_id'] in closed:assert x['source_clear_in_recorded_review_scope'] and not x['remaining_content_issues']
newly=['D09','D11','D12','D13','D18']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'recorded_utc':now,'paper':'I','source_sha256':expected,'pdf_sha256':d['pdf_sha256'],
 'dossier_path':str(dp.relative_to(R)),'dossier_sha256':sha(dp),'defect_log_sha256':sha(R/d['defect_log_path']),
 'types_closed':closed,'types_open':opened,'newly_closed_types':newly,
 'root_review':'Root read all25 individual current type dispositions, their required fixes, source-review explanations and remaining-issue dispositions. The previously read109 exact replacements and complete owning-block/entry comparisons are bound by the applied receipt. D09, D11, D12, D13 and D18 have no unresolved instance in those current reviewed scopes and reach done under rule0.3. New actual candidate18 findings supersede the earlier D02/D08 source-clear proposals; these types and D23 remain open. This review adds no page or mathematical-event credit.',
 'new_findings_superseding_earlier_dossier_proposals':[
  {'type':'D02','pages':[214,221],'state':'Page214 repetition confirmed by assigned full-proof reading; page221 orientation-local-system clause pending exact-context disposition.'},
  {'type':'D08','pages':[252,255,278],'state':'Assigned actual page reading has identified recap candidates; exact complete source comparisons pending.'},
  {'type':'D23','pages':[66,69,71,72,272,321],'state':'Four missing Neron–Severi accents have exact guards and whole-page confirmation; visible loose spacing at272 and321 has paragraph-only previews pending.'},
  {'type':'pending locator classification','pages':[259],'state':'The phrase clockwise convention on the first page is under exact target review. Any confirmed new defect will reopen its actual type explicitly.'}],
 'proof_preservation_exceptions':'The applied17→18 batch explicitly removed one duplicated inline mathcal V mention and one duplicated proposition reference from Remark22.30 and relocated the unchanged period/height convention across a proposition header. Its retained witnesses and full maps are bound; blanket inline/reference sequence identity for that prior batch is not claimed.',
 'mathematical_events_added':0,'new_page_credit':0,'final_pdf_certified':False}
out=R/'records/S6_SERIES_PUBLISH_I_candidate18_type_progress.json'
assert not out.exists();out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
lp=R/'PROGRESS_LEDGER.md';t=lp.read_text()
for typ in closed:
 t,n=re.subn(rf'^(\| I \| {typ}: .*? \|) [^|]* \|$',rf'\1 done; individually reviewed at candidate18 source3542f263; records/S6_SERIES_PUBLISH_I_candidate18_type_progress.json |',t,flags=re.M)
 assert n==1,typ
for typ in opened:
 t,n=re.subn(rf'^(\| I \| {typ}: .*? \|) [^|]* \|$',rf'\1 open; candidate18 actual-page findings; records/S6_SERIES_PUBLISH_I_candidate18_type_progress.json |',t,flags=re.M)
 assert n==1,typ
entry=f'\n## Paper I individual source rows at candidate18 — {now}\n\nD09, D11, D12, D13 and D18 reach done after the exact applied repairs and current per-type review. Twenty-two source types are closed; D02, D08 and D23 remain open for the new actual-page findings. Page259 has a pending locator review whose confirmed type will be reopened explicitly. The source is3542f263, the PDF702aaa0a and the log has2,196 unique edit rows. This operation gives no page-reading or mathematical-event credit. The changed-image, metadata, provenance and final page-map gates remain pending. Evidence: `records/S6_SERIES_PUBLISH_I_candidate18_type_progress.json`.\n'
lp.write_text(t+entry)
rp=R/'S6_SERIES_PUBLISH_report.md';rp.write_text(rp.read_text()+entry)
print(json.dumps({'record':str(out.relative_to(R)),'sha256':sha(out),'closed':len(closed),'open':opened,'newly_closed':newly}))
