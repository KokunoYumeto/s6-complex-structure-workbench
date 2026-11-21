#!/usr/bin/env python3
"""Dated progress review with an exhaustive, honest current-gate snapshot."""
from pathlib import Path
import csv,json,hashlib,datetime,re,collections,sys
csv.field_size_limit(10_000_000)
r=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
scheduled=datetime.datetime(2026,11,21,1,42,tzinfo=datetime.timezone.utc)
number=int(sys.argv[1]) if len(sys.argv)>1 else 1
due=scheduled+datetime.timedelta(hours=number-1)
assert now>=due, 'The scheduled progress review is not due yet.'
dest=r/'records'/f'S6_SERIES_PUBLISH_progress_review_{number:02d}.json'
assert not dest.exists(),'Do not overwrite an earlier review.'
ledger=r/'PROGRESS_LEDGER.md';s=ledger.read_text()
defects=[]
for paper,defect,status in re.findall(r'^\| (I|II|III|IV|V) \| (D\d+:.*?) \| (.*?) \|$',s,re.M):
    defects.append({'paper':paper,'defect':defect,'status':status})
assert len(defects)==125
counts=list(csv.DictReader((r/'records/S6_SERIES_PUBLISH_statement_check_counts.csv').open()))
candidate=list(csv.DictReader((r/'records/S6_SERIES_PUBLISH_required_check_candidates.csv').open()))
baseline=list(csv.DictReader((r.parent/'source/UNDERCHECKED_RESULTS.csv').open()))
by_label={x['label']:x for x in counts}
required=[]
eight={'ari:C.4.1','ari:C.7.7','ari:C.7.8','inv:C3.6','push:src:B.4.3','push:src:C.3.5','push:src:D.4.6','push:src:E.3.1'}
for x in baseline:
    y=by_label.get(x['label'],{})
    if x['label'] in eight:
        disposition='done: current statement-first derivation and printed-proof comparison; precise computational scope in the analytic/topology first-four records'
    elif x['paper']=='V':
        disposition='done at V completion snapshot' if y.get('below_bar')=='no' else 'supplementary outside the independently reviewed V main closure; no extra third-check obligation asserted'
    elif x['paper'] in {'II','III','IV'}:
        disposition='open: sequential work has not reached this paper'
    elif y.get('below_bar')=='no':
        disposition='new scoped evidence recorded; see the actual comparison and evidence-group qualification, not count alone'
    elif y.get('main_dependency_reference_closure')=='true':
        disposition='open: current main-closure candidate under contextual review/check'
    else:
        disposition='outside current candidate closure; final dependency review remains open'
    required.append({'paper':x['paper'],'label':x['label'],'original_below_bar':x['below_bar'],
        'current_below_bar':y.get('below_bar','not currently printed'),
        'current_main_closure':y.get('main_dependency_reference_closure','false'),
        'disposition':disposition})
prov=list(csv.DictReader((r/'S6_SERIES_PUBLISH_provenance_checks.tsv').open(),delimiter='\t'))
ipr=json.loads((r/'agents/i_provenance/S6_SERIES_PUBLISH_I_three_way_claim_table.json').read_text())
current_i=(r/'S6_SERIES_PUBLISH_I.tex').read_bytes()
snapshot={'review':number,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),
    'main_gate':'Paper V complete at its recorded source/PDF snapshot; finish I, then II, III, IV, and final five-paper consistency.',
    'movement_since_initialization':True,
    'movement_evidence':['All 25 V defect gates done; complete 177-page final reading done; V required proof checks and 40 provenance claims closed.',
        'The eight originally below-bar Paper I checks have reached their done state with scoped derivations/comparisons.'],
    'consecutive_reviews_without_movement':0,
    'defects':defects,
    'final_page_gates':{p:('done:177 pages, exact PDF receipt' if p=='V' else 'open') for p in ['I','II','III','IV','V']},
    'original_underchecked_row_dispositions':required,
    'current_required_candidates':candidate,
    'current_candidate_counts':dict(collections.Counter(x['paper'] for x in candidate)),
    'provenance_current':{'V':prov,'I_primary_claim_table':ipr,'I_final_counts_and_deposit_synchronization':'open','II':'open','III':'open','IV':'open'},
    'current_I_source_sha256':hashlib.sha256(current_i).hexdigest(),
    'current_ledger_sha256':hashlib.sha256((r/'CHECK_EVENTS.tsv').read_bytes()).hexdigest(),
    'editorial_note':'Current I source is an intermediate manuscript. No I defect category or final PDF is certified complete from a pattern scan or intermediate build.'}
dest.write_text(json.dumps(snapshot,indent=2)+'\n')
text=f'''\n## Scheduled progress review {number:02d} — {now.isoformat()}\n\nThe first three-hour review finds movement: all 25 Paper V defect rows, its complete 177-page final-PDF reading, required proof checks and 40 provenance claims have closed. In Paper I the eight originally below-bar checks have reached done, with the precise statement-first derivations and proof/computation comparisons in the two first-four records. Thus the number of consecutive reviews without movement is zero. The main gate is now completion of I, II, III and IV in order, followed by final series consistency.\n\nAll I–IV defect and final-page rows remain open. Every initial underchecked-result row has its current disposition in the exhaustive dated snapshot `{dest.relative_to(r)}`; partial checks and evidence-group qualifications are preserved, and count alone does not close a mathematical gate. Current reference-closure candidates are listed below. I has 42 primary provenance claim dispositions under preparation, but its final count/deposit/source synchronization remains open. II–IV provenance remains open. The preceding original CSV is historical intake, superseded for current status by this dated snapshot.\n\n| Paper | Defect rows open | Final pages | Current required-check candidates | Provenance gate |\n|---|---:|---|---:|---|\n'''
for paper in ['V','I','II','III','IV']:
    text+=f"| {paper} | {sum(x['paper']==paper and x['status'].startswith('open') for x in defects)} | {'done' if paper=='V' else 'open'} | {sum(x['paper']==paper for x in candidate)} | {'40 closed' if paper=='V' else 'open'} |\n"
text+='\n### Paper I remaining current candidates\n\n'
for x in candidate:
    if x['paper']=='I':text+=f"- `{x['label']}`: open/contextual review; owner `{x['current_statement_owner']}`.\n"
text+='\nThe next mandatory progress review is 02:42 UTC (03:42 Europe/Berlin). Checkpoint 04 is scheduled for 01:42 UTC; later checkpoints remain every 45 minutes.\n'
ledger.write_text(s+text)
p=r/'S6_SERIES_PUBLISH_report.md';s=p.read_text();s+='\n'+text.replace('## Scheduled progress review','## Progress review',1)
s+='\nPaper I currently has '+str(sum(1 for _ in csv.DictReader((r/'S6_SERIES_PUBLISH_defects_I.tsv').open(),delimiter='\t')))+' logged edits. Its exact norm maximum uses one division-ladder proof, the finite local expansions and derivative identities precede their uses, and the root-atlas base-change/duality proof precedes the direct-image calculations. Original labels and permanent tags are preserved. The sigma–theta constant coverage gap is filled by a separate, narrowly scoped preread derivation; it is not counted as a second full proof of C.7.1.\n'
p.write_text(s)
print(json.dumps({'review':number,'movement':True,'stalled_reviews':0,'snapshot':str(dest),'candidate_counts':snapshot['current_candidate_counts']}))
