#!/usr/bin/env python3
"""Bind the provenance reader's explicit complete-proof review attestations.

Inclusion is the manually enumerated scope below, not file/keyword discovery.
No CHECK_EVENTS file or canonical source is written.
"""
from pathlib import Path
from datetime import datetime, timezone
import collections
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=lambda p:{'path':str(p.relative_to(ROOT)),'sha256':sha(p)}

# These are the actual full-proof scopes recorded by this reader. The one
# statement-only revision inv:C3.1, bibliography, and a credit preface are absent.
allow={
 'candidate15':{'ari:C.7.11','ari:C.7.12','night:P5.7','night:P5.2'},
 'candidate16_first':{'fam:src:A.2.1','fam:src:A.4.2'},
 'candidate16_expanded':{'fam:src:F.2.2','night:P2.9','push:src:A.4.1','push:src:A.4.8',
   'push:src:B.4.10','push:src:B.4.11','push:src:B.4.12','push:src:B.4.14',
   'push:src:B.4.21','push:src:B.4.23','ari:C.8.14','inv:C3.7','fam:src:E.1.4'},
 'candidate16_recap':{'push:src:C.3.5'},
 'candidate17':{'push:src:E.2.1','night:P5.5','fam:src:B.4.2','mapsI:src:A.3.2','mapsI:src:A.3.3',
   'push:src:D.4.5','push:src:A.2.2','night:P2.10','push:src:A.2.5','push:src:A.4.2',
   'push:src:A.4.8','push:src:B.1.2','push:src:B.3.4','push:src:B.3.6','push:src:B.4.2',
   'push:src:A.1.2','push:src:B.4.10','push:src:B.4.16','push:src:B.4.17'},
 'candidate18':{'push:src:B.4.31','push:src:B.4.32','inv:B3.1','ari:C.6.R2','ari:C.6.R5'},
}
batch_files={
 'candidate15':'S6_SERIES_PUBLISH_I_candidate15_provenance_guard_receipt.json',
 'candidate16_first':'S6_SERIES_PUBLISH_I_candidate16_provenance_guards.json',
 'candidate16_expanded':'S6_SERIES_PUBLISH_I_candidate16_expanded_guard_receipt.json',
 'candidate16_recap':'S6_SERIES_PUBLISH_I_candidate16_recap_guards.json',
 'candidate17':'S6_SERIES_PUBLISH_I_candidate17_provenance_guard_receipt.json',
 'candidate18':'S6_SERIES_PUBLISH_I_candidate18_provenance_guard_receipt.json',
}
instances=[]
for batch,name in batch_files.items():
    receipt_path=OUT/name
    obj=json.loads(receipt_path.read_text())
    rows=obj if isinstance(obj,list) else obj.get('block_archives',obj.get('blocks',obj.get('full_block_comparisons',[])))
    found=set()
    for row in rows:
        sid=row.get('scope_id',row.get('statement_id'))
        if sid not in allow[batch]:continue
        assert sid not in found,(batch,sid)
        found.add(sid)
        old=row.get('before') if 'before_sha256' in row else row.get('original_full_block',row.get('original'))
        new=row.get('proposed_full_block',row.get('proposed'))
        old_sha=row.get('before_sha256',row.get('original_full_block_sha256',row.get('original_sha256')))
        new_sha=row.get('proposed_full_block_sha256',row.get('proposed_sha256'))
        original=ROOT/old;proposed=ROOT/new
        assert sha(original)==old_sha and sha(proposed)==new_sha,(batch,sid)
        before,after=original.read_text(),proposed.read_text()
        assert '\\begin{proof}' in before and '\\begin{proof}' in after
        old_proof=before[before.index('\\begin{proof}'):]
        new_proof=after[after.index('\\begin{proof}'):]
        assert old_proof!=new_proof,(batch,sid,'proof itself was not revised')
        instances.append({
            'statement_id':sid,'batch':batch,
            'manual_review_evidence':bind(receipt_path),
            'original_complete_statement_and_proof':bind(original),
            'proposed_complete_statement_and_proof':bind(proposed),
            'guard_ids':row.get('guards',row.get('guard_ids',[row.get('id')])),
            'complete_exposed_owning_proof_actually_read':True,
            'exact_rewording_actually_compared_in_full_proof_context':True,
            'proof_text_changed':True,
            'review_order':'After exposure to the proof; complete original/current proof read, exact proposed passages manually compared, unchanged mathematical context bound by the literal full-block map.',
            'independent_derivation_performed':False,
        })
    assert found==allow[batch],(batch,found^allow[batch])

by=collections.defaultdict(list)
for inst in instances:by[inst['statement_id']].append(inst)
current=json.loads((OUT/'S6_SERIES_PUBLISH_I_candidate18_recount.json').read_text())
order={row['id']:i for i,row in enumerate(current['statements'])}
assert all(sid in order for sid in by)
assert len(instances)==44 and len(by)==42
rows=[{'statement_id':sid,'proposed_type':'used and rechecked in this run',
       'event_candidates':1,'review_instances':by[sid]}
      for sid in sorted(by,key=order.get)]
excluded=[
 {'scope':'I:standard-deformation-credit','reason':'An unnumbered literature-credit preface; no attached proof in the compared block.'},
 {'scope':'inv:C3.1 / I16-prov-16','reason':'The complete original statement/proof was read, but this change removes only a statement announcement; its attached proof bytes are unchanged. Excluded from this narrow reworded-proof manifest.'},
 {'scope':'All13 candidate15 bibliography replacements and all candidate17 bibliography research/proposals','reason':'Metadata authentication and citation formatting; no proof-reading event.'},
 {'scope':'All rendered-page receipts, context occurrence scans, source-count bindings and private layout image alone','reason':'No extra event is inferred from a page record, bounded phrase review, automatic archive or software comparison.'},
 {'scope':'Definition2.1 target locator review','reason':'Existing definition/reference witness, without an attached rewritten proof.'},
]
record={
 'recorded_utc':datetime.now(timezone.utc).isoformat(),'paper':'I',
 'reviewer':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation provenance agent',
 'effort':'Inherited reasoning effort; no separate numerical setting exposed.',
 'actual_review_date':'2026-11-21','attestation_scope':'Actual complete exposed proof readings and exact rewording comparisons manually performed in this continuation. The enumerated scope is attested here; archive presence is used only to bind those readings to bytes.',
 'source18_sha256':current['source_sha256'],'ledger_base_sha256':current['ledger_sha256'],
 'unique_owning_printed_statements':42,'actual_comparison_instances':44,
 'event_grouping':'One used-and-rechecked candidate per owning printed statement across repeated candidate versions and cosmetic edits. Further overlap with root/editor/infra must be merged before ledger append.',
 'events':rows,'excluded':excluded,
 'no_independent_derivation_claimed':True,'no_targeted_or_computational_credit_claimed':True,
 'historical_zero_receipts':'Earlier mathematical_events_added=0 fields report that no ledger rows were written by those operations. Those immutable records are retained. This separate manifest assigns the actual complete exposed-proof rereadings to the category required by prompt4.3; it does not create a new derivation or recast page/metadata inspection as proof work.',
 'canonical_ledger_mutated':False,'events_appended':0,
}
path=OUT/'S6_SERIES_PUBLISH_I_continuation_proof_reread_attestation_provenance.json'
path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(path.relative_to(ROOT)),'sha256':sha(path),'unique_statements':len(rows),'actual_comparison_instances':len(instances),'ledger_mutated':False},indent=2))
