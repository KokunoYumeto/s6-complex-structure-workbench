#!/usr/bin/env python3
"""Immutable hourly review; movement is a recorded row transition, never packaging."""
from pathlib import Path
import csv,json,hashlib,datetime,re,collections,sys
csv.field_size_limit(100_000_000)
r=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
number=int(sys.argv[1])
due=datetime.datetime(2026,11,21,1,42,tzinfo=datetime.timezone.utc)+datetime.timedelta(hours=number-1)
assert now>=due,'The scheduled progress review is not due yet.'
dest=r/'records'/f'S6_SERIES_PUBLISH_progress_review_{number:02d}.json'
assert not dest.exists(),'Do not overwrite an earlier review.'
assert number>1
prev=json.loads((r/'records'/f'S6_SERIES_PUBLISH_progress_review_{number-1:02d}.json').read_text())
ledger=r/'PROGRESS_LEDGER.md';s=ledger.read_text()
defects=[{'paper':a,'defect':b,'status':c} for a,b,c in re.findall(r'^\| (I|II|III|IV|V) \| (D\d+:.*?) \| (.*?) \|$',s,re.M)]
assert len(defects)==125
counts=list(csv.DictReader((r/'records/S6_SERIES_PUBLISH_statement_check_counts.csv').open()))
candidate=list(csv.DictReader((r/'records/S6_SERIES_PUBLISH_required_check_candidates.csv').open()))
baseline=list(csv.DictReader((r.parent/'source/UNDERCHECKED_RESULTS.csv').open()))
by_label={x['label']:x for x in counts}
manifest=json.loads((r/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())
for label,x in manifest['rows'].items():
 assert x['status']=='done'
 assert hashlib.sha256((r/x['evidence_path']).read_bytes()).hexdigest()==x['evidence_sha256'],label
oldrows={x['label']:x for x in prev['original_underchecked_row_dispositions']}
required=[]
for x in baseline:
 label=x['label'];y=by_label.get(label,{});old=oldrows[label]
 if old['disposition'].startswith('done'):
  disposition=old['disposition']
 elif label in manifest['rows']:
  disposition='done: '+manifest['rows'][label]['scope']
 elif x['paper'] in {'II','III','IV'}:
  disposition='open: sequential work has not reached this paper'
 elif x['paper']=='V':
  disposition=old['disposition']
 elif y.get('below_bar')=='no':
  disposition='new scoped evidence recorded; see actual comparison and evidence-group qualification, not count alone'
 elif y.get('main_dependency_reference_closure')=='true':
  disposition='open: current main-closure candidate under contextual review/check'
 else:
  disposition='outside current candidate closure; final dependency review remains open'
 required.append({'paper':x['paper'],'label':label,'original_below_bar':x['below_bar'],
  'current_below_bar':y.get('below_bar','not currently printed'),
  'current_main_closure':y.get('main_dependency_reference_closure','false'),'disposition':disposition})
new_done=[x['label'] for x in required if x['disposition'].startswith('done') and not oldrows[x['label']]['disposition'].startswith('done')]
olddef={(x['paper'],x['defect']):x['status'] for x in prev['defects']}
defect_done=[(x['paper'],x['defect']) for x in defects if x['status'].startswith('done') and not olddef[(x['paper'],x['defect'])].startswith('done')]
page_gates={p:('done:177 pages, exact PDF receipt' if p=='V' else 'open') for p in ['I','II','III','IV','V']}
page_done=[p for p,v in page_gates.items() if v.startswith('done') and not prev['final_page_gates'][p].startswith('done')]
movement=bool(new_done or defect_done or page_done)
stalled=0 if movement else prev['consecutive_reviews_without_movement']+1
prov=list(csv.DictReader((r/'S6_SERIES_PUBLISH_provenance_checks.tsv').open(),delimiter='\t'))
ipr=json.loads((r/'agents/i_provenance/S6_SERIES_PUBLISH_I_three_way_claim_table.json').read_text())
snapshot={'review':number,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),
 'main_gate':'Paper V complete at its recorded source/PDF snapshot; finish I, then II, III, IV, and final five-paper consistency.',
 'movement_since_previous_review':movement,'newly_done_original_check_rows':new_done,
 'newly_done_defect_rows':defect_done,'newly_done_final_page_rows':page_done,
 'movement_evidence':['Each named check row has a complete scoped comparison record with hash bound in the completion manifest. Editorial edit totals and packaging are excluded from movement.'],
 'consecutive_reviews_without_movement':stalled,'mandatory_stop':stalled>=2,
 'defects':defects,'final_page_gates':page_gates,'original_underchecked_row_dispositions':required,
 'completion_manifest':manifest,'current_required_candidates':candidate,
 'current_candidate_counts':dict(collections.Counter(x['paper'] for x in candidate)),
 'provenance_current':{'V':prov,'I_primary_claim_table':ipr,'I_final_counts_and_deposit_synchronization':'open','II':'open','III':'open','IV':'open'},
 'current_I_source_sha256':hashlib.sha256((r/'S6_SERIES_PUBLISH_I.tex').read_bytes()).hexdigest(),
 'current_ledger_sha256':hashlib.sha256((r/'CHECK_EVENTS.tsv').read_bytes()).hexdigest(),
 'editorial_note':'Current I source is intermediate. No I defect category or final PDF is certified complete by a pattern scan or intermediate build. The corrected visible-reference dependency parser adds previously hidden candidates; this is disclosed and does not count as mathematical movement.'}
dest.write_text(json.dumps(snapshot,indent=2)+'\n')
text=f'\n## Scheduled progress review {number:02d} — {now.isoformat()}\n\n'
text+=f'This review records {len(new_done)} original required-check rows newly done since review {number-1:02d}, {len(defect_done)} newly done defect rows and {len(page_done)} newly done final-page rows. Consecutive reviews without movement: {stalled}. '
text+='The comparison uses the preceding immutable row dispositions and the scoped completion manifest, with exact evidence hashes. Editorial activity, counts alone and packaging do not count as movement.\n\n'
text+='The main gate remains completion of Paper I, then II, III and IV in order, followed by final five-paper consistency. Paper V is complete at its recorded snapshot. All I–IV defect and final-page gates remain open. Paper I final provenance/count/deposit synchronization remains open; II–IV provenance remains open.\n\n'
if new_done:text+='Newly completed original rows: '+', '.join('`'+x+'`' for x in new_done)+'.\n\n'
else:text+='No original check row changed to done in this interval.\n\n'
text+=f'Every one of the {len(required)} original underchecked rows and {len(defects)} defect rows has a current disposition in `{dest.relative_to(r)}`. Current candidate counts are below. The current visible-reference graph includes newly exposed prerequisites; their discovery is a parser correction, not proof completion.\n\n'
text+='| Paper | Defect rows open | Final pages | Current required-check candidates | Provenance gate |\n|---|---:|---|---:|---|\n'
for paper in ['V','I','II','III','IV']:
 text+=f"| {paper} | {sum(x['paper']==paper and x['status'].startswith('open') for x in defects)} | {'done' if paper=='V' else 'open'} | {sum(x['paper']==paper for x in candidate)} | {'40 closed' if paper=='V' else 'open'} |\n"
text+='\n### Paper I remaining current candidates\n\n'
for x in candidate:
 if x['paper']=='I':text+=f"- `{x['label']}`: open/contextual review; owner `{x['current_statement_owner']}`.\n"
next_due=due+datetime.timedelta(hours=1)
text+=f'\nThe next mandatory progress review is {next_due.strftime("%H:%M")} UTC ({(next_due+datetime.timedelta(hours=1)).strftime("%H:%M")} Europe/Berlin). Checkpoints continue on their separate 45-minute schedule.\n'
if stalled>=2:text+='\nThe mandatory two-review stop rule is now triggered; package the exact incomplete state and stop the work.\n'
ledger.write_text(s+text)
report=r/'S6_SERIES_PUBLISH_report.md';report.write_text(report.read_text()+'\n'+text.replace('## Scheduled progress review','## Progress review',1))
print(json.dumps({'review':number,'movement':movement,'newly_done_original_rows':new_done,'stalled_reviews':stalled,'mandatory_stop':stalled>=2,'snapshot':str(dest),'candidate_counts':snapshot['current_candidate_counts']}))
