#!/usr/bin/env python3
"""Bind the original 250 occurrences to candidate16, including explicit reopenings."""
from pathlib import Path
from datetime import datetime, timezone
import collections
import copy
import csv
import hashlib
import json
import re
import fitz
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=lambda p:{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size}
SOURCE_SHA='61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
PDF_SHA='4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2'
source=OUT/'candidate16_review_blocks/S6_SERIES_PUBLISH_I_candidate16_source_snapshot.tex'
pdf=ROOT/'build/I_candidate16/S6_SERIES_PUBLISH_I.pdf'
prior_path=OUT/'S6_SERIES_PUBLISH_I_candidate15_D08_D09_dispositions.json'
raw_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_D09_correspondence_raw.json'
source_bind_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_source_count_rebinding.json'
assert sha(source)==SOURCE_SHA and sha(pdf)==PDF_SHA
assert sha(prior_path)=='07cdeb400b108f906a9ea4ef3e9a8045cd55f9602cdab500c4d51007bcc1a40a'
prior=json.loads(prior_path.read_text());raw=json.loads(raw_path.read_text());sb=json.loads(source_bind_path.read_text())
assert raw['source_sha256']==sb['source']['sha256']==SOURCE_SHA
assert raw['pdf_sha256']==PDF_SHA and sb['exact_whole_source_reconstruction_from_62_edits']
patterns={
 'D08':re.compile(r'\b(?:actual|retain\w*|supplied|specified|fresh|executed|saved|receipt|candidate|survivor|verified|probe)\b',re.I),
 'D09':re.compile(r'\.py\b|\.jsonl?\b|code/|audit_|receipt|SHA-256|rows \(4|columns numbered|identities at their recorded scopes|--fresh',re.I)}
current=collections.defaultdict(list)
doc=fitz.open(pdf)
for page in doc:
    text=' '.join(page.get_text().split())
    for kind,pattern in patterns.items():
        for m in pattern.finditer(text):current[kind].append({'page':page.number+1,'hit':m[0],'context':text[max(0,m.start()-100):m.end()+200],'offset':m.start()})
assert {k:len(v) for k,v in current.items()}=={'D08':190,'D09':58}
raw_by_index={r['scan_row_index_1based']:r for r in raw['rows']}
removed_by_index={r['scan_row_index_1based']:r for r in raw['removed']}
assert set(removed_by_index)=={332,339}
reviewed={
67:'Actually read both contexts: the free cyclic quotient, conormal and unit are unchanged; the only text change is the approved accent correction etale to étale.',
333:'Actually read both contexts: the exact CM coordinate definition is unchanged; the previous next-proposition prefix now lies on the next page and the current page footer is 303.',
334:'Actually read both contexts: the fixed-field assertion and equation reference are unchanged; the following derivative statement now begins on the next page, outside this page-local context.',
340:'Actually read both contexts and the complete current PNG page 320: the sign conversion, moving lift and connecting class are unchanged; the preceding nonzero-class sentence now lies on the previous page.'}
assert {r['scan_row_index_1based'] for r in raw['changed_rows']}==set(reviewed)
reopened={
70:('I16-prov-16','Expanded row R034 and compute row C003 revisit the statement-level announcement containing specified. The exact source credit, Chern map and Green operator remain under the approved guard. The older retained-word disposition is reopened for this whole sentence.'),
127:('I16-prov-19','The final recap pass revisits We have now verified all three comparisons and their inverses. The full coherent-closing proposition and proof were read; all exact comparison maps and inverses remain under the deletion guard. The older retained-word disposition is reopened.')}
rows=[];ordinals=collections.Counter();changed=[]
for original in prior['rows']:
    row=copy.deepcopy(original);i=row['scan_row_index_1based'];kind=row['type']
    row['inherited_candidate15_disposition']=row['disposition']
    row['inherited_candidate15_reason']=row['reason']
    if i in removed_by_index:
        old=removed_by_index[i]
        row.update({'candidate16_occurrence_present':False,'candidate16_page':None,
                    'candidate16_context':'','removed_by_applied_guard':old['removing_guard'],
                    'candidate16_disposition':'Removed by an exact candidate15-to16 applied guard; no current occurrence.',
                    'confirmed_defect':False,'current_pending_guard_ids':[]})
    else:
        cur=current[kind][ordinals[kind]];ordinals[kind]+=1
        assert cur['hit']==row['hit']
        rawrow=raw_by_index[i]
        assert cur=={k:rawrow[k] for k in ['page','hit','context','offset']}
        same=cur['context']==row['candidate15_context']
        row.update({'candidate16_occurrence_present':True,'candidate16_page':cur['page'],
                    'candidate16_context':cur['context'],'candidate16_text_offset':cur['offset'],
                    'candidate15_to16_context_exactly_equal':same,
                    'candidate16_context_review':reviewed[i] if not same else 'Exact page-text context preserved from the completed candidate15 review.',
                    'candidate16_disposition':'Inherited mathematical use or permitted Programs-table text, through exact occurrence correspondence.',
                    'current_pending_guard_ids':[]})
        if not same:changed.append(i)
        if i in reopened:
            gid,reason=reopened[i]
            row.update({'confirmed_defect':True,'candidate16_disposition':'Prior bounded disposition reopened: standalone D08 announcement/recap, exact guard pending application.',
                        'current_pending_guard_ids':[gid],'reopening_reason':reason})
    rows.append(row)
assert len(rows)==250 and ordinals=={'D08':190,'D09':58}
assert set(changed)==set(reviewed)
fuller=copy.deepcopy(prior['fuller_previously_examined_source_passages'])
source_text=source.read_text()
for passage in fuller:
    assert source_text.count(passage['text'])==1
    passage['candidate16_exact_passage_preserved']=True
    passage['candidate16_excerpt_start_line']=source_text.count('\n',0,source_text.index(passage['text']))+1
    if passage['label']=='three comparison maps and inverses':
        passage['later_contextual_reopening']='I16-prov-19 removes only the recap inside this passage; every mathematical map and inverse remains. This candidate16 passage is still the exact pre-application text.'
reopening=OUT/'S6_SERIES_PUBLISH_I_candidate15_D08_reopening_receipt.json'
expanded=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_expanded_dispositions.json'
recaps=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_recap_dispositions.json'
result={
 'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':16,
 'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'source_snapshot':bind(source),'pdf':bind(pdf),'page_count':len(doc),
 'inherited_completed_context_review':bind(prior_path),'source_delta_binding':bind(source_bind_path),
 'raw_correspondence':bind(raw_path),'source_exact_reconstruction_from_62_applied_edits_verified':True,
 'correspondence':'The case-sensitive within-type hit sequences agree after removing exactly original rows 332 and 339. Every one of the 248 surviving occurrences has an order-preserving current page/context match. The two removals are bound to I15-edits-19 and I15-prov-10 in the exact applied source map.',
 'original_rows':250,'current_counts':{'D08':190,'D09':58},'removed_original_row_indices':[332,339],
 'current_contexts_exactly_equal_to_candidate15':244,'changed_contexts_actually_read':4,'changed_context_row_indices':changed,
 'rows':rows,'fuller_previously_examined_source_passages':fuller,
 'candidate15_visual_D08_reopening_receipt':bind(reopening),
 'candidate15_visual_D08_fixes_applied':['I15-prov-04','I15-prov-12'],
 'reopening_history':'Two D08 passages outside the earlier selected-keyword set were found by actual candidate15 page reading and explicitly reopened the bounded D08 disposition. Both fixes are among the 62 applied candidate16 edits. Candidate16 review additionally reopened existing selected-hit rows 70 and 127; their exact guards are recorded here. The expanded scans provide further contextual findings outside the selected hit list.',
 'candidate16_expanded_D08_dispositions':bind(expanded),'candidate16_final_recap_dispositions':bind(recaps),
 'current_prior_pattern_rows_reopened':[70,127],
 'pending_guard_ids_for_reopened_rows':['I16-prov-16','I16-prov-19'],
 'D08_final_type_closed':False,
 'D09_bounded_audit_result':'All 58 current selected D09 hits retain their exact prior contexts and permitted Programs-table dispositions. No new D09 defect was found in this bounded pass.',
 'mathematical_events_added':0,'page_reading_credit_added':0,'shared_files_modified':False,
 'scope':'Current source/PDF occurrence correspondence with actual review of every changed context, explicit row-level reopenings and the two earlier visual discoveries. This adds no full-page reading credit, mathematical check event or unconditional final defect-type closure.'}
dest=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_D09_dispositions.json';dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
fields=['scan_row_index_1based','type','hit','candidate15_page','candidate16_page','candidate16_occurrence_present','candidate15_to16_context_exactly_equal','candidate16_disposition','current_pending_guard_ids','confirmed_defect']
with dest.with_suffix('.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
print(json.dumps({'receipt':str(dest.relative_to(ROOT)),'sha256':sha(dest),'current_counts':result['current_counts'],'contexts_exactly_equal':244,'changed_contexts_actually_read':4,'reopened_original_rows':[70,127],'D08_final_type_closed':False},indent=2))
