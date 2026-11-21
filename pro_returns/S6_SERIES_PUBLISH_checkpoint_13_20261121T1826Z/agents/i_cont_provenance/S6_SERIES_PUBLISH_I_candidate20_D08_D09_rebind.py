#!/usr/bin/env python3
"""Bind the completed bounded occurrence audit to the candidate20 source/PDF."""
from pathlib import Path
from datetime import datetime,timezone
import collections,copy,hashlib,json,re
import fitz
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
pp=O/'S6_SERIES_PUBLISH_I_candidate19_D08_D09_dispositions.json'
assert sha(pp)=='93a16466b664374156b01f55fd427ad071c4c50c550f379de20a36a59bec0202'
prior=json.loads(pp.read_text());src=R/'S6_SERIES_PUBLISH_I.tex';pdf=R/'build/I_candidate20/S6_SERIES_PUBLISH_I.pdf'
assert sha(src)=='179fcc4e85fb7902aaf978bcd809cf9928ebc0a46cda5628d5096e6fa0011d74'
assert sha(pdf)=='62d84285f35aa6e6ce03b83efbcf2a96e880fda6206eb24c05ab8e66fe799dd6'
patterns={'D08':re.compile(r'\b(?:actual|retain\w*|supplied|specified|fresh|executed|saved|receipt|candidate|survivor|verified|probe)\b',re.I),
 'D09':re.compile(r'\.py\b|\.jsonl?\b|code/|audit_|receipt|SHA-256|rows \(4|columns numbered|identities at their recorded scopes|--fresh',re.I)}
cur=collections.defaultdict(list)
for page in fitz.open(pdf):
    t=' '.join(page.get_text().split())
    for kind,pat in patterns.items():
        for m in pat.finditer(t):cur[kind].append({'page':page.number+1,'hit':m[0],
            'context':t[max(0,m.start()-100):m.end()+200],'offset':m.start()})
assert {k:len(v) for k,v in cur.items()}=={'D08':188,'D09':58}
mapping={}
for kind in patterns:
    old=sorted([x for x in prior['rows'] if x['type']==kind and x['candidate19_occurrence_present']],
               key=lambda x:(x['candidate19_page'],x['candidate19_text_offset']))
    assert [x['hit'] for x in old]==[x['hit'] for x in cur[kind]]
    for x,y in zip(old,cur[kind]):
        assert x['candidate19_context']==y['context']
        assert x['candidate19_page']==y['page']
        mapping[x['scan_row_index_1based']]=y
rows=[]
for old in prior['rows']:
    row=copy.deepcopy(old);n=row['scan_row_index_1based']
    if old['candidate19_occurrence_present']:
        x=mapping[n]
        row.update(candidate20_occurrence_present=True,candidate20_page=x['page'],candidate20_context=x['context'],
            candidate20_text_offset=x['offset'],candidate19_to20_context_and_page_exactly_equal=True,
            candidate20_disposition='Inherited completed mathematical-use or permitted Programs-table disposition; exact page and captured-context identity is verified.',
            candidate20_pending_guard_ids=[])
    else:
        assert n in [70,127,332,339]
        row.update(candidate20_occurrence_present=False,candidate20_page=None,candidate20_context='',
            candidate20_disposition='Historical selected occurrence removed by the previously bound exact applied guard.',candidate20_pending_guard_ids=[])
    rows.append(row)
ap=R/'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate19_combined_apply_receipt.json';app=json.loads(ap.read_text())
assert app['mode']=='applied' and len(app['changes'])==7
countp=R/'records/S6_SERIES_PUBLISH_I_methodology_count_apply_receipt.json';count=json.loads(countp.read_text())
assert count['before_source_sha256']==app['after_source_sha256'] and count['after_source_sha256']==sha(src)
result={'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':20,
    'source_sha256':sha(src),'pdf_sha256':sha(pdf),'source':bind(src),'pdf':bind(pdf),
    'source_snapshot':bind(O/'continuation_reread_append/I_source_after_count.tex'),
    'inherited_completed_bounded_context_audit':bind(pp),
    'current_source_count_rebinding':bind(O/'S6_SERIES_PUBLISH_I_candidate20_source_count_rebinding.json'),
    'source_application_receipts':[bind(ap),bind(countp)],
    'original_rows':250,'current_counts':{'D08':188,'D09':58},'surviving_occurrences':246,
    'all246_surviving_captured_contexts_and_page_numbers_exactly_identical_to_candidate19':True,
    'new_changed_contexts':0,'removed_original_rows':prior['removed_original_rows'],
    'earlier_identical_Figure3_extraction_order_move':prior['moved_identical_context'],
    'rows':rows,'explicit_earlier_D08_reopenings':prior['explicit_earlier_D08_reopenings'],
    'expanded_and_recap_dispositions':prior['expanded_and_recap_dispositions'],
    'candidate19_complete_proof_comparisons':prior['later_candidate19_complete_proof_reviews'],
    'all7_candidate19_body_recap_guards_applied':True,
    'pending_confirmed_defects_in_this_bounded_occurrence_audit':[],
    'D09_bounded_result':'All58 selected Programs-table occurrences retain their completed permitted-link dispositions.',
    'D08_bounded_result':'All188 selected surviving mathematical/title/caption occurrences retain their completed dispositions. The earlier explicit reopenings and later full-proof recap corrections remain bound separately.',
    'full_type_closure_scope':'The root-owned25-type dossier combines these bounded rows with the actual complete-proof comparisons and certified final full-image coverage. Selected-word correspondence alone supplies no universal absence claim.',
    'full_image_coverage_not_certified_by_this_record':True,
    'mathematical_events_added_by_this_binding':0,'additional_page_reading_credit':0,'shared_files_modified':False}
p=O/'S6_SERIES_PUBLISH_I_candidate20_D08_D09_dispositions.json';assert not p.exists()
p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'receipt':bind(p),'current_counts':result['current_counts'],'exact_surviving_contexts':246,'new_context_or_page_credit':0},indent=2))
