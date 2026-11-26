#!/usr/bin/env python3
"""Record root's four exact source-type closures under continuation rule0.3."""
from pathlib import Path
import datetime, hashlib, json, re
R=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dp=R/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_type_closure_preparation_v2.json'
assert sha(dp)=='83b26f4fd14fd48602a39b6d998dd49cade1831a18396701d99bc535882c367c'
d=json.loads(dp.read_text());s=R/'S6_SERIES_PUBLISH_I.tex';l=R/'CHECK_EVENTS.tsv';f=R/'S6_SERIES_PUBLISH_defects_I.tsv'
assert sha(s)==d['source_sha256']=='f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
assert sha(l)==d['check_ledger_sha256'] and sha(f)==d['defect_log_sha256']
selected=['D02','D06','D11','D23']; rows=[r for r in d['rows'] if r['type_id'] in selected]
assert len(rows)==4 and all(r['source_clear_in_recorded_review_scope'] and not r['remaining_content_issues'] for r in rows)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=R/'records/S6_SERIES_PUBLISH_I_candidate19_type_progress.json';assert not p.exists()
record={'paper':'I','recorded_utc':now,'source_sha256':sha(s),'pdf_sha256':d['pdf_sha256'],'ledger_sha256':sha(l),'defect_log_sha256':sha(f),'dossier':{'path':str(dp.relative_to(R)),'sha256':sha(dp)},'root_review_scope':'Root read the exact required-fix, current source-review, inherited scope, absence-evidence and remaining-issue fields for each of these four types in bounded output. The full21-guard input review and applied block maps were separately checked; root had read the complete affected proof scopes before application. The versioned dossier retains the additional D08 page66 finding. No closure is inferred solely from keyword absence.','closed_types':selected,'rows':[{'type_id':r['type_id'],'status':'done','source_review':r['source_review'],'source_absence_evidence':r['source_absence_evidence']} for r in rows],'open_types':['D08'],'final_pdf_certified':False,'remaining_paper_gates':['Apply the separately archived D08 recap correction','Record actual proof rereadings and update exact methodology counts','Complete final rebuild and changed-page reading','Bind final metadata, mapped defects, A–G scope,42 provenance claims and deposit'],'mathematical_events_added':0,'additional_page_reading_credit':0}
p.write_text(json.dumps(record,indent=2)+'\n')
progress=R/'PROGRESS_LEDGER.md';txt=progress.read_text()
for typ in selected:
 txt,n=re.subn(r'^(\| I \| '+typ+r': .*? \|) [^|]* \|$',r'\1 done; candidate19 source instances resolved and logged; records/S6_SERIES_PUBLISH_I_candidate19_type_progress.json |',txt,flags=re.M);assert n==1
entry=f'\n## Paper I candidate19 type progress — {now}\n\nThe exact applied21-guard batch resolves the recorded D02, D06, D11 and D23 instances in the current source. Root reviewed their individual source dispositions and closed these four rows under section0.3. Paper I now has24 source-type rows done; D08 remains open for the newly read page66 closing recap, whose complete proof comparison and exact guard are archived. The candidate19 build has346 pages and zero underfull/overfull boxes, undefined references/citations, missing fonts/characters or duplicate destinations. The complete final-PDF and provenance gates remain open. This status operation adds no check event or page-reading credit. Evidence: `records/S6_SERIES_PUBLISH_I_candidate19_type_progress.json`.\n'
progress.write_text(txt+entry)
report=R/'S6_SERIES_PUBLISH_report.md';report.write_text(report.read_text()+entry)
assert sha(s)==record['source_sha256'] and sha(l)==record['ledger_sha256'] and sha(f)==record['defect_log_sha256']
print(json.dumps({'record':str(p.relative_to(R)),'sha256':sha(p),'closed':selected,'open':['D08']},indent=2))
