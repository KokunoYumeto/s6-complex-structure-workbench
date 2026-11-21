#!/usr/bin/env python3
"""Bind all 250 historic bounded D08/D09 rows to candidate19.

All 27 changed page-text contexts were actually read before this receipt was
written.  This correspondence computation adds no whole-page or proof credit.
"""
from pathlib import Path
from datetime import datetime,timezone
import collections,copy,csv,difflib,hashlib,json,re
import fitz
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
priorp=O/'S6_SERIES_PUBLISH_I_candidate16_D08_D09_dispositions.json'
assert sha(priorp)=='a6bf9e2580dc34dda0694054601c5069a2d8290d3d754b96e318ea58e585ca81'
prior=json.loads(priorp.read_text())
src=O/'candidate19_review_blocks/S6_SERIES_PUBLISH_I_candidate19_source_snapshot.tex'
pdf=R/'build/I_candidate19/S6_SERIES_PUBLISH_I.pdf'
assert sha(src)=='f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
assert sha(pdf)=='e7a48c79d7bc5588f272b7d138f82fef8bbc504e86626f06a01c0bd86de32f7f'
patterns={'D08':re.compile(r'\b(?:actual|retain\w*|supplied|specified|fresh|executed|saved|receipt|candidate|survivor|verified|probe)\b',re.I),
 'D09':re.compile(r'\.py\b|\.jsonl?\b|code/|audit_|receipt|SHA-256|rows \(4|columns numbered|identities at their recorded scopes|--fresh',re.I)}
current=collections.defaultdict(list)
for page in fitz.open(pdf):
    text=' '.join(page.get_text().split())
    for kind,pattern in patterns.items():
        for m in pattern.finditer(text):current[kind].append({'page':page.number+1,'hit':m[0],
            'context':text[max(0,m.start()-100):m.end()+200],'offset':m.start()})
assert {k:len(v) for k,v in current.items()}=={'D08':188,'D09':58}
removed={332:'I15-edits-19',339:'I15-prov-10',70:'I16-prov-16',127:'I16-prov-19'}
mapping={};moved=[]
for kind in patterns:
    old=[x for x in prior['rows'] if x['type']==kind and x['candidate16_occurrence_present'] and x['scan_row_index_1based'] not in removed]
    ins=[];deleted=[]
    for tag,a,b,c,d in difflib.SequenceMatcher(None,[x['hit'] for x in old],[x['hit'] for x in current[kind]],autojunk=False).get_opcodes():
        if tag=='equal':
            for x,y in zip(old[a:b],current[kind][c:d]):mapping[x['scan_row_index_1based']]=y
        elif tag=='insert':ins+=current[kind][c:d]
        elif tag=='delete':deleted+=old[a:b]
        else:raise AssertionError((kind,tag))
    if kind=='D08':
        assert len(ins)==len(deleted)==1 and deleted[0]['scan_row_index_1based']==130
        assert deleted[0]['candidate16_context']==ins[0]['context']
        mapping[130]=ins[0]
        moved.append({'row':130,'reason':'The exact Figure3 caption context moved in page-text extraction order; its mathematical retain phrase and complete captured context are byte-identical.',
            'old_page':deleted[0]['candidate16_page'],'new_page':ins[0]['page'],'exact_context':ins[0]['context']})
    else:assert not ins and not deleted
assert len(mapping)==246

reviews={
2:'Only a table-of-contents page number changes; retaining the cusp factor remains the same mathematical section title.',
114:'The preceding proof announcement was removed. The real marking, holomorphic period matrix and translation construction named by retain are unchanged.',
133:'The same specified surjection and boundary-identification context ends at a different page break; the following section starts on the next page.',
135:'The cusp coordinate and retained collar integer are unchanged; the page now ends before the next numbered step.',
144:'The finite-twist and admissibility context is unchanged; the same period/descent formulas now follow on the current page rather than the next.',
147:'The page starts with step2. Verified refers to the exact numbered norm identity and unchanged formula, with its normal-form deduction.',
173:'Supplied refers to the explicit Engel construction and its exact published locator. The next step now begins on the same page.',
241:'The specified analytic disc and proper global family are unchanged; the current page ends earlier in the next sentence.',
247:'The specified marked-core hypothesis is unchanged; the proof now begins on the following page.',
248:'The specified finite modification retains its mathematical meaning. A separate redundant scope sentence was removed in the approved source18 batch; the next concrete period computation is unchanged.',
250:'The specified fibre twist and tangent-cohomology conclusion are unchanged; the attached proof now starts on the same page.',
263:'The two specified base opens and their affine marking are unchanged; the proof now begins on the following page.',
266:'The specified holomorphic overlap map, cover and gluing remain unchanged; the next Hausdorffness step now starts on the same page.',
272:'The comparison with the compact family and finite target P1 minus infinity are unchanged; the next section now begins on this page.',
273:'The finite target specified in Omega remains unchanged; the following section now shares the page.',
289:'The mathematical title retaining the cusp factor starts a fresh page; the preceding normal-degree text is on the preceding page.',
290:'Retain names the exact period columns and logarithms. The same formulas now follow the end of the preceding proposition on this page.',
292:'Retain names the unique irreducible component and its proper dominating map. Only the preceding scope sentence context changed under the approved guard.',
304:'Retained names the ordered local branches used to handle self-crossings. The following section now starts on the next page.',
307:'Retaining names the explicit rational function used in the line-bundle comparison. The adjacent section-algebra announcement was replaced by its positive mathematical input; all displayed identities persist.',
333:'Retain identifies the curve, point and real logarithm in the fixed CM coordinate convention. The next proposition now starts on the same page.',
334:'Specified points to the exact numbered power relation. The following algebraic-direction formulas now lie on the same page.',
335:'Specified names the fixed model value for a removable zero or pole. The subsequent interpolation step moved across the page boundary.',
382:'The permitted Programs-table filename and exact associated calculation are unchanged; only the terminal page number changes332 to331.',
383:'The permitted Programs-table filename is unchanged; only the terminal page number changes332 to331.',
402:'The permitted Programs-table filenames and theorem/corollary links are unchanged; only the terminal page number changes333 to332.',
403:'The permitted Programs-table filename is unchanged; only the terminal page number changes333 to332.'}
changed=[];rows=[]
for old in prior['rows']:
    row=copy.deepcopy(old);n=row['scan_row_index_1based']
    if n in removed:
        row.update(candidate19_occurrence_present=False,candidate19_page=None,candidate19_context='',
            candidate19_disposition='Removed by the named exact applied guard; the historical finding and reopening remain preserved.',
            removed_by_applied_guard=removed[n],candidate19_pending_guard_ids=[],confirmed_defect=False)
    else:
        cur=mapping[n];same=old['candidate16_context']==cur['context']
        if not same:changed.append(n);assert n in reviews
        row.update(candidate19_occurrence_present=True,candidate19_page=cur['page'],candidate19_context=cur['context'],
            candidate19_text_offset=cur['offset'],candidate16_to19_context_exactly_equal=same,
            candidate19_context_review=reviews[n] if not same else 'Exact previously reviewed captured context is preserved.',
            candidate19_disposition='Mathematical use of the selected word or permitted Programs-table link, under the bound occurrence correspondence.',
            candidate19_pending_guard_ids=[],confirmed_defect=False)
    rows.append(row)
assert set(changed)==set(reviews) and len(changed)==27

chain=[
O/'S6_SERIES_PUBLISH_I_candidate17_source_count_rebinding.json',
O/'S6_SERIES_PUBLISH_I_candidate18_source_count_rebinding.json',
O/'S6_SERIES_PUBLISH_I_candidate19_source_count_rebinding.json']
apply16=R/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_combined_apply_receipt.json'
applied=json.loads(apply16.read_text());assert {'I16-prov-16','I16-prov-19'}<={x['guard_id'] for x in applied['changes']}
for gid in ['I16-prov-16','I16-prov-19']:
    c=next(x for x in applied['changes'] if x['guard_id']==gid)
    assert c['old'] not in src.read_text()
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':19,
    'source_sha256':sha(src),'pdf_sha256':sha(pdf),'source_snapshot':bind(src),'pdf':bind(pdf),
    'prior_completed_250_row_disposition':bind(priorp),'source_transformation_chain':[bind(x) for x in chain],
    'original_rows':250,'surviving_original_occurrences':246,'current_counts':{'D08':188,'D09':58},
    'removed_original_rows':removed,'moved_identical_context':moved,
    'surviving_contexts_exactly_equal_to_candidate16':219,'changed_contexts_actually_read':27,
    'changed_context_row_indices':changed,'rows':rows,
    'explicit_earlier_D08_reopenings':[bind(O/'S6_SERIES_PUBLISH_I_candidate15_D08_reopening_receipt.json'),bind(R/'records/S6_SERIES_PUBLISH_I_candidate15_D08_reopen.json')],
    'expanded_and_recap_dispositions':[bind(O/'S6_SERIES_PUBLISH_I_candidate16_D08_expanded_dispositions.json'),bind(O/'S6_SERIES_PUBLISH_I_candidate16_D08_recap_dispositions.json'),bind(O/'S6_SERIES_PUBLISH_I_candidate17_first_person_here_dispositions.json')],
    'D09_bounded_result':'All58 selected current D09 occurrences retain their permitted Programs-table meanings; four captured contexts change only a printed footer page number.',
    'D08_bounded_result':'All188 selected surviving occurrences retain mathematical or permitted title/caption meanings. Four original selected occurrences have been removed by exact recorded guards. This bounded selected-word correspondence does not replace the later full-proof/whole-page D08 reviews.',
    'later_candidate19_complete_proof_reviews':[bind(R/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_root_guards_v2.json'),bind(R/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_edits_full_pair_review.json'),bind(R/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_edits_additional_full_pair_review.json'),bind(O/'S6_SERIES_PUBLISH_I_candidate19_provenance_full_pair_review.json')],
    'later_candidate19_recaps_pending_application':True,'D08_final_type_closed':False,
    'full_page_credit_added':0,'mathematical_events_added':0,'shared_files_modified':False,
    'scope':'Actual reading of every changed captured text context and an exact correspondence to the historically completed bounded audit. Figure3 has an explicitly witnessed extraction-order move. No new complete-proof or full-page reading is inferred from the software comparison.'}
dest=O/'S6_SERIES_PUBLISH_I_candidate19_D08_D09_dispositions.json';assert not dest.exists()
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'receipt':str(dest.relative_to(R)),'sha256':sha(dest),'counts':result['current_counts'],'changed_contexts_actually_read':27,'current_bounded_defects':0,'D08_final_type_closed':False},indent=2))
