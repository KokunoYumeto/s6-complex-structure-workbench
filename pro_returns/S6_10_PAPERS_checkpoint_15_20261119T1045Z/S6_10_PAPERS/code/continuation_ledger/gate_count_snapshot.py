#!/usr/bin/env python3
"""Report explicit renewal receipts and remaining printed proof work.

Reads owner receipts directly. Event presence, source matching, mathematical
status and compilation never close a gate here. Writes audit derivatives only.
"""
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import collections, csv, hashlib, importlib.util, io, json, re

csv.field_size_limit(16 * 1024 * 1024)
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'analysis/continuation_ledger'
PAPERS = ['I','II','III','IV','V','VI']
GATES = ['proof_rederivation_before_reading','new_independent_computations','renewed_main_result_credit_check']
PROOF_TYPES = {'targeted proof check','independent re-proof'}
INPUT_BYTES={}
def read_once(path):
    path=path.resolve()
    if path not in INPUT_BYTES:INPUT_BYTES[path]=path.read_bytes()
    return INPUT_BYTES[path]
read_once(ROOT/'code/continuation_ledger/metadata_patch_map.py')
spec=importlib.util.spec_from_file_location('typed_metadata_map',ROOT/'code/continuation_ledger/metadata_patch_map.py')
metadata_map=importlib.util.module_from_spec(spec);spec.loader.exec_module(metadata_map)

def sha(raw): return hashlib.sha256(raw).hexdigest()
def read_table(path, delimiter=','):
    return list(csv.DictReader(io.StringIO(read_once(path).decode(),newline=''),delimiter=delimiter))
def write_table(name, rows, fields):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
def obj(s):
    try:return json.loads(s)
    except (TypeError,ValueError):return {}
def completed(value): return bool(re.match(r'^complete\b',str(value),re.I))
def semantic_status(value):
    text=value.strip().lower()
    if text.startswith(('proved under hypotheses','proved conditionally')):return 'proved under hypotheses H'
    if text.startswith(('false as stated','refuted')):return 'false as stated'
    if text.startswith('open'):return 'open'
    if text.startswith(('proved','known')):return 'proved'
    return None

def main():
    now=datetime.now(timezone.utc).isoformat()
    inventory_path=ROOT/'S6_10_PAPERS_inventory.csv'
    event_path=ROOT/'CHECK_EVENTS.tsv'
    inventory=read_table(inventory_path)
    events=read_table(event_path,'\t')
    by_label=collections.defaultdict(list)
    for index,row in enumerate(inventory,2):by_label[row['label']].append((index,row))
    by_event=collections.defaultdict(list)
    for event in events:by_event[event['statement_id']].append(event)
    input_paths=[inventory_path,event_path,ROOT/'code/continuation_ledger/metadata_patch_map.py',Path(__file__)]

    receipts=collections.defaultdict(dict)
    receipt_sources=collections.defaultdict(list)
    for path in sorted((ROOT/'analysis').glob('continuation_*/completed_row_gates.json')):
        input_paths.append(path);values=json.loads(read_once(path))
        for label,gates in values.items():
            if label not in by_label:raise ValueError('Unknown owner-receipt label: '+label)
            if not isinstance(gates,dict) or set(gates)-set(GATES):raise ValueError('Unexpected gate fields: '+label)
            for gate,value in gates.items():
                if gate in receipts[label] and receipts[label][gate]!=value:raise ValueError('Conflicting explicit owner receipts: '+label+'/'+gate)
                receipts[label][gate]=value
            receipt_sources[label].append({'source':str(path.relative_to(ROOT)),'sha256':sha(read_once(path)),'gates':gates})

    restore_path=ROOT/'analysis/continuation_root/restore_verification.json'
    restore=json.loads(read_once(restore_path));input_paths.append(restore_path)
    restored_gate_paths=[r['path'] for r in restore['records'] if re.search(r'^analysis/continuation_[^/]+/completed_row_gates\.json$',r['path'])]
    if restored_gate_paths:raise ValueError('Renewal baseline needs explicit comparison with restored owner receipts')
    baseline={'requested_start_utc':'2026-11-19T03:37:00+00:00','verified_restore_timestamp_utc':restore['timestamp_utc'],
              'restored_files_verified':restore['verified'],'restored_owner_gate_receipt_files':restored_gate_paths,
              'renewed_all_three_gate_count':0,
              'basis':'The renewed obligation starts in this continuation. The exact restored manifest has no continuation owner-gate receipt files. Earlier proof/citation records remain historical and are not counted as this renewal.'}

    rows=[]
    for label,aliases in by_label.items():
        papers={r['paper'] for _,r in aliases}
        if len(papers)!=1:raise ValueError('Receiving label assigned to multiple papers: '+label)
        paper=next(iter(papers));statuses={r['status'] for _,r in aliases}
        if len(statuses)!=1:raise ValueError('Conflicting alias statuses: '+label)
        status=next(iter(statuses));printed_aliases=[r for _,r in aliases if not r['in_compendium_only_because'].strip()]
        printed=bool(printed_aliases)
        reasons=sorted({r['in_compendium_only_because'] for _,r in aliases if r['in_compendium_only_because']})
        kinds=sorted({r['kind'] for _,r in aliases})
        roles=sorted({r['main_or_supporting'] for _,r in aliases})
        actual=[e for e in by_event[label] if e['phase']=='continuation' and not metadata_map.metadata_operation(e)]
        proof_events=[e for e in actual if e['type'] in PROOF_TYPES]
        computation_events=[e for e in actual if e['type']=='computation or formal certificate']
        source_events=[e for e in actual if e['type']=='used and rechecked in this run']
        gate_values={g:receipts[label].get(g,'pending; no explicit complete owner receipt') for g in GATES}
        done={g:completed(v) for g,v in gate_values.items()}
        all_three=all(done.values())
        if printed:
            category='historical false assertion / refutation audit' if status=='false as stated' else 'printed receiving proof or asserted-identity review'
        elif any(reason.startswith('known or second proof:') for reason in reasons):category='compendium mixed known / second proof'
        elif any(reason.startswith(('known:','classical:')) for reason in reasons):category='compendium known or classical'
        elif any(reason.startswith('second proof:') for reason in reasons):category='compendium second proof'
        elif all(reason.startswith('apparatus:') for reason in reasons):category='compendium apparatus'
        else:category='compendium allocation requiring source-scope decision'
        proof_required=printed and status!='false as stated'
        proof_state=('complete explicit owner receipt' if done[GATES[0]] else
                     'partial recorded proof scope; whole gate pending' if proof_events else
                     'pending; no explicit whole receipt or continuation proof event')
        source_required=not printed and category!='compendium apparatus'
        row={'paper':paper,'label':label,'inventory_row_count':len(aliases),'printed_inventory_row_count':len(printed_aliases),
             'compendium_inventory_row_count':len(aliases)-len(printed_aliases),
             'inventory_source_rows':';'.join(str(n) for n,_ in aliases),
             'source_keys':'; '.join(r['source_run']+':'+r['source_id'] for _,r in aliases),
             'placement':'printed' if printed else 'compendium-only','review_category':category,
             'kind':' | '.join(kinds),'mathematical_status':status,'main_or_supporting':' | '.join(roles),
             'new_printed_proof_required':proof_required,'proof_scope_state':proof_state,
             'proof_gate_complete':done[GATES[0]],'computation_gate_complete':done[GATES[1]],'credit_gate_complete':done[GATES[2]],
             'all_three_explicit_gates_complete':all_three,'new_all_three_since_0337':all_three,
             'proof_receipt':gate_values[GATES[0]],'computation_receipt':gate_values[GATES[1]],'credit_receipt':gate_values[GATES[2]],
             'owner_receipt_sources':'; '.join(x['source'] for x in receipt_sources[label]),
             'renewed_proof_event_ids':'; '.join(e['event_id'] for e in proof_events),
             'renewed_proof_event_scopes':' || '.join(e['outcome'] for e in proof_events),
             'renewed_computation_event_ids':'; '.join(e['event_id'] for e in computation_events),
             'renewed_source_event_ids':'; '.join(e['event_id'] for e in source_events),
             'renewed_source_event_scopes':' || '.join(e['outcome'] for e in source_events),
             'compendium_source_verification_required':source_required,
             'compendium_source_verification_state':('complete explicit owner credit/source receipt' if done[GATES[2]] else 'pending explicit renewed source-verification receipt') if source_required else 'not in compendium-only source queue',
             'compendium_reason':' | '.join(reasons),
             'known_input_with_printed_local_application':any('Known cited input with source-specific local application'==k for k in kinds)}
        rows.append(row)
    rows.sort(key=lambda r:(PAPERS.index(r['paper']),r['label']))

    # A vocabulary rewrite is not a change in a mathematical conclusion.
    status_path=OUT/'status_changes_history.tsv';input_paths.append(status_path)
    history=read_table(status_path,'\t');semantic_changes=[];vocabulary_only=0;unparsed_old=0
    metadata_status_reasons={}
    for metadata_receipt in [OUT/'receiving_counterexample_status_corrections.json',ROOT/'analysis/continuation_V/receiving_status_correction.json']:
        if metadata_receipt.exists():
            input_paths.append(metadata_receipt)
            metadata_status_reasons.update(json.loads(read_once(metadata_receipt)).get('reasons',{}))
    # Exact source/receiving-assertion metadata repairs keep the earlier raw
    # status but do not represent a theorem newly settled in this session.
    for row in inventory:
        notice=obj(row['notes']).get('continuation_receiving_counterexample_status')
        if notice:metadata_status_reasons[row['label']]=notice['reason']
    metadata_status_changes=[]
    for change in history:
        old=semantic_status(change['old_status']);new=semantic_status(change['new_status'])
        if old is None:unparsed_old+=1;continue
        if old==new:vocabulary_only+=1;continue
        if new is None:raise ValueError('Unknown new status: '+change['new_status'])
        value=dict(change,old_semantic_status=old,new_semantic_status=new)
        if change['label'] in metadata_status_reasons:
            value['interpretation']=metadata_status_reasons[change['label']]
            if value not in metadata_status_changes:metadata_status_changes.append(value)
            continue
        if value not in semantic_changes:semantic_changes.append(value)
    for change in semantic_changes:
        if change['label']=='ari:C.7.4':
            change['interpretation']='Restored and freshly checked exact source implication with named BPSS Conjecture4.7 hypothesis H. H, including conductor361, and the unconditional question remain open. This is no proof of H.'
        else:change['interpretation']='Exact recorded semantic status change; see owner status override and mathematical receipt.'

    stats=[]
    for paper in PAPERS:
        rr=[r for r in rows if r['paper']==paper]
        printed=[r for r in rr if r['placement']=='printed']
        required=[r for r in rr if r['new_printed_proof_required']]
        partial=[r for r in required if not r['proof_gate_complete'] and r['renewed_proof_event_ids']]
        stats.append({'paper':paper,'inventory_rows':sum(r['inventory_row_count'] for r in rr),'distinct_inventory_labels':len(rr),
                      'printed_rows':sum(r['printed_inventory_row_count'] for r in rr),'distinct_printed_labels':len(printed),
                      'new_printed_proof_rows':len(required),'complete_proof_receipts':sum(r['proof_gate_complete'] for r in required),
                      'remaining_new_printed_proofs':sum(not r['proof_gate_complete'] for r in required),
                      'partial_proof_rows':len(partial),'remaining_without_recorded_proof_event':sum(not r['proof_gate_complete'] and not r['renewed_proof_event_ids'] for r in required),
                      'all_three_completed':sum(r['all_three_explicit_gates_complete'] for r in printed),
                      'proof_complete_other_gate_pending':sum(r['proof_gate_complete'] and not r['all_three_explicit_gates_complete'] for r in required),
                      'false_assertion_refutation_rows':sum(r['mathematical_status']=='false as stated' for r in printed),
                      'open_mathematical_rows':sum(r['mathematical_status']=='open' for r in printed),
                      'compendium_only_rows':sum(r['compendium_inventory_row_count'] for r in rr),
                      'compendium_only_labels':sum(r['placement']=='compendium-only' for r in rr),
                      'mixed_printed_and_compendium_alias_labels':sum(r['printed_inventory_row_count']>0 and r['compendium_inventory_row_count']>0 for r in rr),
                      'compendium_source_verification_rows':sum(r['compendium_source_verification_required'] for r in rr),
                      'compendium_renewed_source_receipts_complete':sum(r['compendium_source_verification_required'] and r['credit_gate_complete'] for r in rr)})
    total={k:sum(x[k] for x in stats) for k in stats[0] if k!='paper'}
    total['all_owner_proof_gate_receipts']=sum(r['proof_gate_complete'] for r in rows)
    total['all_owner_computation_gate_receipts']=sum(r['computation_gate_complete'] for r in rows)
    total['all_owner_credit_gate_receipts']=sum(r['credit_gate_complete'] for r in rows)
    assert total['distinct_printed_labels']==total['new_printed_proof_rows']+total['false_assertion_refutation_rows']
    assert total['inventory_rows']==total['printed_rows']+total['compendium_only_rows']
    assert total['new_printed_proof_rows']==total['complete_proof_receipts']+total['remaining_new_printed_proofs']
    assert total['remaining_new_printed_proofs']==total['partial_proof_rows']+total['remaining_without_recorded_proof_event']
    assert len(rows)==len(by_label)

    all_three=[r for r in rows if r['all_three_explicit_gates_complete']]
    partial=[r for r in rows if r['new_printed_proof_required'] and not r['proof_gate_complete'] and r['renewed_proof_event_ids']]
    remaining=[r for r in rows if r['new_printed_proof_required'] and not r['proof_gate_complete']]
    compendium=[r for r in rows if r['placement']=='compendium-only']
    source_hashes={str(p.resolve().relative_to(ROOT)):sha(read_once(p)) for p in input_paths}
    changed=[str(p) for p,raw in INPUT_BYTES.items() if p.read_bytes()!=raw]
    if changed:raise ValueError('Input changed during snapshot; rerun after owner write: '+', '.join(changed))
    fields=list(rows[0])
    for name,rr in [('gate_count_rows.tsv',rows),('completed_three_gate_rows.tsv',all_three),
                    ('partial_printed_proof_scopes.tsv',partial),('remaining_new_printed_proofs.tsv',remaining),
                    ('compendium_source_verification.tsv',compendium)]:write_table(name,rr,fields)
    status_fields=['label','paper','old_status','new_status','basis','old_semantic_status','new_semantic_status','interpretation']
    write_table('mathematical_status_changes.tsv',semantic_changes,status_fields)
    write_table('receiving_status_metadata_changes.tsv',metadata_status_changes,status_fields)
    write_table('gate_count_by_paper.tsv',stats,list(stats[0]))
    payload={'timestamp_utc':now,'baseline':baseline,'totals':total,'by_paper':stats,
             'complete_three_gate_labels':[r['label'] for r in all_three],
             'partial_printed_proof_labels':[r['label'] for r in partial],
             'semantic_status_changes':semantic_changes,
             'receiving_status_metadata_corrections':metadata_status_changes,
             'status_history_audit':{'total_entries':len(history),'same_semantic_status_vocabulary_entries':vocabulary_only,'old_status_not_itself_a_mathematical_verdict':unparsed_old,'receiving_assertion_metadata_correction_entries':len(metadata_status_changes),'changed_semantic_mathematical_status_entries':len(semantic_changes)},
             'explicit_receiving_additions':{'corrected_conclusion_labels':[r['label'] for r in rows if r['label'].startswith('iv:correction:')],
                 'source_proved_receiving_open_cp36_labels':[r['label'] for r in rows if re.fullmatch(r'night:P3K\.(109|11[0-9])',r['label']) and r['mathematical_status']=='open'],
                 'scope':'The33 corrected consequences receive separate labels and proofs; their original33 false statements remain false as stated. Eleven cp36 source-Proved rows are receiving-open pending current proof work. Neither allocation/intake operation alone settles a new mathematical question.'},
             'source_hashes':source_hashes,'owner_receipts':dict(receipt_sources),'row_files':{'all':'gate_count_rows.tsv','complete_three':'completed_three_gate_rows.tsv','partial':'partial_printed_proof_scopes.tsv','remaining_new_printed':'remaining_new_printed_proofs.tsv','compendium_source':'compendium_source_verification.tsv'},
             'method':[
                 'Distinct receiving labels are the counting unit. Inventory aliases and their exact source-row indices are retained in the row table.',
                 'All three means three explicit complete owner fields; no absent or supporting-row credit field is silently treated as complete.',
                 'The proof queue contains printed receiving assertions, identities and local applications except original assertions whose status is false as stated. Open conclusions retain their partial-proof review scope and remain mathematically open.',
                 'Original false assertions have a separate refutation/correction audit queue. Their false statements are not requested to be proved.',
                 'Compendium-only known/classical and retained second proofs are excluded from new printed-proof counts. Their exact source-verification requirement remains visible; apparatus is separately classified.',
                 'Partial means a nonadministrative continuation targeted/independent proof event exists but no owner whole proof receipt exists. It records bounded scope, never completion.',
                 'Metadata operations use the same exact-outcome classifier as the printed metadata map. Compilation, event totals, imported producing checks and source matches never close a proof gate.',
                 'Owner computation receipts may explicitly record that a qualitative proof has no separate finite computation; those stated scopes are preserved verbatim.',
                 'The source-verification queue reports only explicit renewed owner credit/source completion. Older bounded source loci and current source events remain evidence with their individual scopes.'
             ]}
    (OUT/'gate_count_snapshot.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# Renewal gate snapshot','',f'As of {now}. Requested baseline: 19 November 2026, 03:37 UTC.','',
           f"**{len(all_three)} distinct printed labels have all three explicit renewal receipts.** The restored baseline has zero receipts for this newly requested renewal. Historical reviews remain preserved separately.",'',
           '| Paper | Printed labels | New printed proof rows | Complete proof receipts | Remaining proof rows | Partial proof scope | All three complete |',
           '|---|---:|---:|---:|---:|---:|---:|']
    for x in stats:
        lines.append(f"| {x['paper']} | {x['distinct_printed_labels']} | {x['new_printed_proof_rows']} | {x['complete_proof_receipts']} | {x['remaining_new_printed_proofs']} | {x['partial_proof_rows']} | {x['all_three_completed']} |")
    lines.append(f"| **Total** | **{total['distinct_printed_labels']}** | **{total['new_printed_proof_rows']}** | **{total['complete_proof_receipts']}** | **{total['remaining_new_printed_proofs']}** | **{total['partial_proof_rows']}** | **{total['all_three_completed']}** |")
    lines += ['',f"There are {total['inventory_rows']} inventory rows and {total['distinct_inventory_labels']} distinct receiving labels. The {total['printed_rows']} printed inventory rows represent {total['distinct_printed_labels']} distinct labels. Alias rows do not multiply completed work.",'',
              f"The {total['remaining_new_printed_proofs']} remaining proof rows include {total['partial_proof_rows']} with a recorded bounded proof check and {total['remaining_without_recorded_proof_event']} with no continuation proof event or complete owner proof receipt. A complete proof receipt with another gate pending occurs on {total['proof_complete_other_gate_pending']} printed rows. The latter rows are not counted as three-gate complete.",'',
              '## Exact labels newly closed since the requested baseline','']
    for paper in PAPERS:
        labels=[r['label'] for r in all_three if r['paper']==paper]
        lines.append(f"- **{paper}:** "+(', '.join('`'+x+'`' for x in labels) if labels else 'none')+'.')
    lines+=['','The exact owner text, file hashes and source-row mappings are in `completed_three_gate_rows.tsv` and `gate_count_snapshot.json`. Every unlisted gate remains pending.','',
            '## Compendium source verification and historical refutations','',
            '| Paper | Compendium-only labels | Source-verification queue | Explicit renewed source receipts | Historical false labels |',
            '|---|---:|---:|---:|---:|']
    for x in stats:lines.append(f"| {x['paper']} | {x['compendium_only_labels']} | {x['compendium_source_verification_rows']} | {x['compendium_renewed_source_receipts_complete']} | {x['false_assertion_refutation_rows']} |")
    lines+=['',f"The {total['compendium_only_labels']} compendium-only labels are outside the new printed-proof queue. Their source dispositions remain in `compendium_source_verification.tsv`, including bounded older citations and any actual continuation source events. The {total['false_assertion_refutation_rows']} printed original false assertions retain their refutations and corrected-conclusion links; their original claims are not treated as proved conclusions.",'',
            'The two printed known-input applications `night:P3F.19` and `night:P3F.20` remain in the receiving proof/application queue. Their external input credit does not close the source-specific local application gate.','',
            '## Mathematical status changes','']
    for x in semantic_changes:lines.append(f"- `{x['label']}`: {x['old_semantic_status']} to {x['new_semantic_status']}. {x['interpretation']}")
    if not semantic_changes:lines.append('No semantic mathematical-status change is recorded in the continuation history.')
    lines+=['', 'Thirty-three corrected consequences now have separate receiving labels and explicit corollary proofs; the original thirty-three false assertions retain that status. These splits expose already established corrected conclusions and their dependencies. The eleven new cp36 source-Proved rows remain receiving-open. Statement/reference refinements and proof replacements that preserve a conclusion are reported through their exact receipts, rather than counted as a change from open to proved.','',
            'Receiving counterexample assertions whose old Refuted source tags referred to the rejected positive claims have their negative/corrected conclusions labelled proved. These exact assertion/status repairs are recorded separately in `receiving_status_metadata_changes.tsv`; they add no mathematical settlement or renewal receipt.','',
            '## Reading the remaining work','',
            '`remaining_new_printed_proofs.tsv` is the per-label routing list. `partial_printed_proof_scopes.tsv` retains every relevant current event outcome so a reviewer can identify the steps actually derived and the whole-proof gap. K116 retains its open receiving status and its remaining complete input-chain/topology review; its checked source/Cartier/theta coefficients alone do not close that row.','',
            'Counts use explicit owner receipts and recorded scopes. They do not count status-vocabulary reconciliation, incoming source proofs, layout repairs, metadata application or successful builds as renewed mathematical checking.','',
            'Refresh with `python code/continuation_ledger/gate_count_snapshot.py` after the event union and owner receipts are current. This report changes no canonical record or gate.','']
    (OUT/'gate_count_snapshot.md').write_text('\n'.join(lines))
    print(json.dumps({'timestamp_utc':now,'all_three':len(all_three),'totals':total,'by_paper':stats,'semantic_status_changes':semantic_changes},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
