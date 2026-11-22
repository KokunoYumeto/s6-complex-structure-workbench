from pathlib import Path
import csv,datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
p='agents/ii_infra/S6_SERIES_PUBLISH_II_allocation_proposal.csv'
with (R/p).open(newline='') as f: rows=list(csv.DictReader(f))
matches=[r for r in rows if r['tag']=='02UH'];assert len(matches)==1
a=matches[0];assert a['label']=='night:P3K.36' and a['current_statement_owner']=='ii:LR:covering'
manifest='records/S6_SERIES_PUBLISH_II_clean_checks_49/manifest.json';m=json.loads((R/manifest).read_text())
c=next(x for x in m['checks'] if x['tag']=='02UH');assert c['owner']=='ii:LR:covering'
assert 'refuted historical fan-value claim' in m['scope']
receipt='records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json';assert not (R/receipt).exists()
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),required_row='check:night:P3K.36',permanent_required_tag='02UH',printed_owner='ii:LR:covering',printed_owner_tag='01RO',
 resolution='The required-check allocation explicitly assigns the retained covering scope to ii:LR:covering. Batch49 completed exactly that scope. This is a recorded disposition map from a required historical row to its proved retained subclaim, not an assertion that the original compound claim and the retained theorem have equal statements. The historical universal fan polynomial remains refuted.',
 evidence=[bind(p),bind(manifest),bind('agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02UH_statement_inputs.tex')],
 review16_effect='Review16 raw row table showed165 done and32 open, while the completion manifest correctly counted166 resolved retained scopes. The one-row mismatch is this disposition. The review remains immutable. Next review records the exact status/evidence reconciliation separately and excludes it from new mathematical movement.',
 new_mathematical_events=0,new_independent_checks=0,source_changes=0)
(R/receipt).write_text(json.dumps(record,indent=2)+'\n')
old='code/S6_SERIES_PUBLISH_continuation2_progress_review.py';s=(R/old).read_text()
s=s.replace("   owner=row['id'][len('check:'):]", "   historical_owner=row['id'][len('check:'):]\n   owner={'night:P3K.36':'ii:LR:covering'}.get(historical_owner,historical_owner)")
s=s.replace("    row['evidence']={k:e[k] for k in ['evidence_path','evidence_sha256']}","    row['evidence']={k:e[k] for k in ['evidence_path','evidence_sha256']}\n    if owner!=historical_owner:\n     resolution=R/'records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json'\n     row['evidence'].update(current_statement_owner=owner,required_row_disposition=str(resolution.relative_to(R)),required_row_disposition_sha256=sha(resolution.read_bytes()))")
s=s.replace(" movement=bool(newly_done);counter=0 if movement else counter+1", " administrative_resolutions=[x for x in newly_done if x=='check:night:P3K.36']\n newly_done=[x for x in newly_done if x not in administrative_resolutions]\n movement=bool(newly_done);counter=0 if movement else counter+1")
s=s.replace("  exact_row_changes=changes,newly_done_rows=newly_done,", "  exact_row_changes=changes,administrative_resolved_owner_rows=administrative_resolutions,newly_done_rows=newly_done,")
s=s.replace(" text+='\\nNewly completed rows: '", " if administrative_resolutions:text+='\\nAdministrative required-owner reconciliation, excluded from new movement: '+', '.join(administrative_resolutions)+'. See records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json; the historical compound claim remains refuted.\\n'\n text+='\\nNewly completed rows: '")
assert s!=(R/old).read_text();compile(s,'progress_review_v2','exec')
new='code/S6_SERIES_PUBLISH_continuation2_progress_review_v2.py';assert not (R/new).exists();(R/new).write_text(s)
record['progress_program_before']=bind(old);record['progress_program_after']=bind(new)
(R/receipt).write_text(json.dumps(record,indent=2)+'\n')
note='\n\n## Required-row disposition reconciliation — '+record['created_utc']+'\n\nThe raw review16 row table undercounted resolved Paper II scopes by one: required historical row `night:P3K.36` is assigned in the existing allocation to printed retained theorem `ii:LR:covering`, completed in batch49. This exact disposition is recorded in `'+receipt+'`. The historical compound fan claim remains refuted. The completion-manifest total166 at checkpoint25 was correct. Review16 remains immutable; the next review records the row reconciliation separately, without new mathematical movement or an additional check event. Use `'+new+'` for subsequent reviews.\n'
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 q=R/name;q.write_text(q.read_text()+note)
print(json.dumps({'receipt':bind(receipt),'new_progress_program':bind(new)},indent=2))
