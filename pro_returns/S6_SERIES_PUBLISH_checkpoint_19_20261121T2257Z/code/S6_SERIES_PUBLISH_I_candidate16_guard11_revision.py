#!/usr/bin/env python3
"""Archive the root-requested relocation; preserve the original 11-guard file."""
from pathlib import Path
import collections
import datetime
import difflib
import hashlib
import importlib.util
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
spec=importlib.util.spec_from_file_location('candidate16_guards',ROOT/'code/S6_SERIES_PUBLISH_I_candidate16_edits_guards.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)

def main():
    source=ROOT/'S6_SERIES_PUBLISH_I.tex';frozen=source.read_bytes();s=frozen.decode()
    assert sha(frozen)==helper.SOURCE_SHA
    original_file=OUT/'S6_SERIES_PUBLISH_I_candidate16_edits_guards.json'
    original_bytes=original_file.read_bytes()
    assert sha(original_bytes)=='0a287201f4b4ca77560f45edf416405ae73b3805893bab77159d91de1e03048c'
    original=json.loads(original_bytes);g=original['guards'][-1];assert g['id']=='I16-edits-11'
    old_start=s.index(g['before'])
    statement=s.index(r'\begin{proposition}',old_start)
    input_start=s.index('Use the curve, point and real logarithm',statement)
    old=s[old_start:input_start]
    prefix=s[statement:input_start]
    retained='Use the curve and conjugation of\n\\cref{I:CM-enlargement-coordinates}.'
    new=prefix+retained+'\n\n'
    assert old==g['before']+'\n\n'+prefix
    a=(ROOT/g['full_block_archive']['original']).read_text()
    assert sha(a.encode())==g['full_block_archive']['original_sha256'] and a.count(old)==1
    b=a.replace(old,new,1)
    # The only extra change from the initial proposed block is the exact move
    # of the retained sentence from the section preface into its proposition.
    initial=(ROOT/g['full_block_archive']['proposed']).read_text()
    assert initial.count(retained)==1
    moved=initial.replace(retained+'\n\n','',1)
    pos=moved.index('Use the curve, point and real logarithm')
    moved=moved[:pos]+retained+'\n\n'+moved[pos:]
    assert moved==b
    assert helper.math_segments(a)==helper.math_segments(b)
    commands=lambda t:re.findall(r'\\[A-Za-z@]+\*?|\\.',t)
    assert collections.Counter(commands(a))==collections.Counter(commands(b))
    assert commands(a)!=commands(b)
    for p in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:assert re.findall(p,a)==re.findall(p,b)
    refs=lambda t:re.findall(r'\\(?:eqref|ref|cref|Cref|cite|citet|citep|SeriesRef)(?:\[[^\]]*\])?\{[^}]+\}',t)
    assert collections.Counter(refs(a))==collections.Counter(refs(b)) and refs(a)!=refs(b)
    pa=OUT/'S6_SERIES_PUBLISH_I_candidate16_guard11_revision_original.tex'
    pb=OUT/'S6_SERIES_PUBLISH_I_candidate16_guard11_revision_proposed.tex'
    pd=OUT/'S6_SERIES_PUBLISH_I_candidate16_guard11_revision.diff'
    pa.write_text(a);pb.write_text(b);pd.write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='ari:C.7.11/candidate16',tofile='ari:C.7.11/revised-convention-placement')))
    pos=s.index(old);proposed=s[:pos]+new+s[pos+len(old):]
    assert proposed[:pos]+old+proposed[pos+len(new):]==s
    archive={'statement_id':'ari:C.7.11','original':str(pa.relative_to(ROOT)),'original_sha256':sha(pa.read_bytes()),'proposed':str(pb.relative_to(ROOT)),'proposed_sha256':sha(pb.read_bytes()),'diff':str(pd.relative_to(ROOT)),'diff_sha256':sha(pd.read_bytes()),'all_mathematical_segments_identical':True,'all_label_target_sequences_identical':True,'command_and_reference_multisets_identical':True,'command_and_reference_order_identical':False,'complete_statement_and_proof_read':True}
    guard={'id':'I16-edits-11r1','supersedes_guard_id':'I16-edits-11','type':'D08/D13','page':307,'statement_id':'ari:C.7.11','source_line':s[:pos].count('\n')+1,'before':old,'after':new,
           'reason':'Remove the section roadmap and move its exact retained curve/conjugation convention, with its numbered reference, inside the owning proposition immediately after StatementRecord. The convention is unchanged; the existing proposition sentence, formulas, hypotheses and complete proof remain. Its reference command moves across the proposition header and StatementRecord commands, so command/reference order is explicitly not claimed identical.',
           'source_sha256':helper.SOURCE_SHA,'pdf_sha256':helper.PDF_SHA,'status':'root-requested revised proposal awaiting exact review; not applied','full_block_archive':archive,'inline_math_mentions_removed':[],'inline_math_mentions_added':[],
           'all_mathematical_segments_identical':True,'all_labels_targets_identical':True,'tex_command_multiset_identical':True,'tex_command_order_identical':False,'citation_reference_multiset_identical':True,'citation_reference_order_identical':False,
           'relocated_exact_text':retained,'relocation_from':'Unnumbered section preface after the Section 26.6 heading','relocation_to':'Inside ari:C.7.11 after StatementRecord and before its existing first sentence','reference_order_before':refs(old),'reference_order_after':refs(new),'mathematical_events_added':0}
    result={'paper':'I','candidate':16,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':helper.SOURCE_SHA,'pdf_sha256':helper.PDF_SHA,'superseded_guard_file':str(original_file.relative_to(ROOT)),'superseded_guard_file_sha256':sha(original_bytes),'superseded_guard_ids':['I16-edits-11'],'guards':[guard],'full_blocks':[archive],'source_modified':False,'original_guard_file_unchanged':True,'reading_record_unchanged':True,'mathematical_events_added':0,'additional_full_page_credit':0}
    p=OUT/'S6_SERIES_PUBLISH_I_candidate16_edits_guard11_revision.json';p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    assert source.read_bytes()==frozen and original_file.read_bytes()==original_bytes
    assert sha((OUT/'S6_SERIES_PUBLISH_I_final_candidate16_reading_edits.json').read_bytes())==helper.READING_SHA
    print(json.dumps({'guard_file':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'guard_id':guard['id'],'type':guard['type'],'mathematical_segments_identical':True,'command_reference_order_identical':False,'source_modified':False,'mathematical_events_added':0},indent=2))

if __name__=='__main__':main()
