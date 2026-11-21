#!/usr/bin/env python3
"""Prepare seven exact Paper I source guards without touching canonical files."""
from pathlib import Path
from datetime import datetime, timezone
import collections
import difflib
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SOURCE_SHA='3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
PDF_SHA='702aaa0abd1a4d8376e213ecaf03a0296592e22063f26db324d805502987e66e'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
digest=lambda t:hashlib.sha256(t.encode()).hexdigest()
source=ROOT/'S6_SERIES_PUBLISH_I.tex'
assert sha(source)==SOURCE_SHA
text=source.read_text()
directory=OUT/'candidate18_guard_review_blocks'
blocks=json.loads((directory/'block_index.json').read_text())
preview=ROOT/'agents/continuation_infra/layout_I18_20261121T174535794945Z'
preview_receipt=ROOT/'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate18_underfull_preview_receipt.json'
assert sha(preview_receipt)=='20bb3c1b1edd7c96c71bf1cc457a202c45a901cc0ee901ab19861ef8a44fbce7'
assert sha(preview/'page_272.png')=='80de43f19c44dc9a14492c8516895c6b99b66ec80b2e55930d64a398cc2c8a24'
items=[
    (1,252,'D08',1,'The argument uses the monomial equations with their displayed\npositive multiplicities.\n','',
     'Delete the standalone method recap. The proposition already states positive integral multiplicities; step5 retains r=x^a y^b with a,b>0 and its primitive-circle map, and step7 retains the positive monodromy exponent and exact kernel computation. All eleven proof steps, matrices and finite-orbit arguments remain.'),
    (2,255,'D08',2,' This proves every stated assertion.','',
     'Delete the empty closing recap after the trace/bounded-logarithm proof. The normalized endpoint-period map, root transformation, section independence, flat patching, trace equation and bounded-character preservation of the zero class remain.'),
    (3,259,'D06',3,'clockwise convention on the first page.',r'clockwise convention of Definition~\ref{def:common-conventions}.',
     'Replace the stale first-page locator by the existing Definition2.1, which explicitly fixes clockwise root generators, counterclockwise base meridians and endpoint identification. Current page1 was read as title/abstract; the source definition and aux bind the convention to2.1,p18. All affine-generator powers and group relations remain.'),
    (4,272,'D23',4,(preview/'peer_p272_original.tex').read_text(),(preview/'peer_p272_proposed.tex').read_text(),
     'Separate the real-period input groups into paragraphs to remove visibly stretched spacing. Only paragraph breaks, the semicolon after tau=iT becoming a period, and the following for becoming For change. Every word otherwise, every formula, row index, T value, sign and bound remains. The private preview was viewed in full and has normal spacing.'),
    (5,278,'D08',5,'One can also see the factor geometrically. ', '',
     'Delete the empty opening announcement in step8. The complete normalized Poincare-bundle pullback, diagonal line-bundle identity, absolute/relative height conversion by [K:Q]=2 and final height equality remain. The geometric derivation itself is retained in full.'),
    (6,279,'D02',5,'The first $10280$ terms are summed directly. Segment boundaries\nare multiples of $257$, so no coefficient is omitted or repeated.',
     'The first $10280$ terms are summed directly. The remaining\ncoefficients are partitioned into segments whose boundaries\nare multiples of $257$.',
     'State the exactly-once summation scope positively. The direct first10280 terms and segment boundaries at multiples of257 are unchanged. For each remaining summation index, belonging to exactly one segment is the same condition as belonging to neither zero nor multiple segments; the new partition wording retains this existing scope. All block recurrences, cutoff, integration advances, error bounds and rational-separation proof remain.'),
    (7,278,'D08',5,"This is the factor from the Poincar\\'e pairing and the base field.\n",'',
     'Delete the pure closing recap of step8. The immediately preceding paragraph retains the Poincare pullback and diagonal factor2, the exact field degree [K:Q]=2, and the displayed equality h_K(Y)=4h_O(Y_d)=a_i^2 h_O(P_i). Thus the entire geometric reason and resulting factor remain explicit before the deleted sentence.')
]
math_re=re.compile(r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|(?<!\\)\$(?!\$)[\s\S]*?(?<!\\)\$')
commands=lambda s:re.findall(r'\\[A-Za-z@]+|\\.',s)
references=lambda s:re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef)\{[^}]+\}',s)
citations=lambda s:re.findall(r'\\cite[a-zA-Z*]*(?:\[[^\]]*\])*\{[^}]*\}',s)
guards=[]
by_block=collections.defaultdict(list)
for index,page,kind,block_number,before,after,reason in items:
    block=blocks[block_number-1]
    original=ROOT/block['path']
    assert sha(original)==block['sha256']
    full=original.read_text()
    assert full.count(before)==text.count(before)==1,(index,'before match')
    assert math_re.findall(before)==math_re.findall(after),(index,'math fragment')
    guard={
        'id':f'I18-prov-{index:02d}','page':page,'type':kind,'statement_id':block['statement_id'],
        'line':text.count('\n',0,text.index(before))+1,'before':before,'after':after,'reason':reason,
        'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'status':'proposed, not applied',
        'original_full_block':block['path'],'original_full_block_sha256':block['sha256'],
        'complete_original_owning_statement_and_proof_actually_read':True,
        'replacement_and_preservation_scope_manually_reviewed':True,
        'mathematical_events_added':0,'source_changes_applied':False,
        'full_page_reading_credit_added':0,
    }
    if index==3:
        p=directory/'D06_target_witness.json'
        guard.update({'allowed_added_reference':r'\ref{def:common-conventions}',
                      'reference_exception_witness':str(p.relative_to(ROOT)),
                      'reference_exception_witness_sha256':sha(p)})
    if index==4:
        guard.update({'private_preview_receipt':str(preview_receipt.relative_to(ROOT)),
                      'private_preview_receipt_sha256':sha(preview_receipt),
                      'preview_image':str((preview/'page_272.png').relative_to(ROOT)),
                      'preview_image_sha256':sha(preview/'page_272.png'),
                      'preview_complete_page_actually_viewed':True,
                      'preview_image_does_not_add_canonical_page_credit':True})
    if index==7:
        guard['allowed_removed_text_accent_command']=r"\'"
    guards.append(guard);by_block[block_number].append(guard)

review_rows=[]
for block_number, group in by_block.items():
    block=blocks[block_number-1];before=(ROOT/block['path']).read_text();after=before
    for g in group:
        assert after.count(g['before'])==1
        after=after.replace(g['before'],g['after'],1)
    assert math_re.findall(before)==math_re.findall(after),(block_number,'all full-block math')
    assert before.split(r'\end{proposition}',1)[0]==after.split(r'\end{proposition}',1)[0]
    assert citations(before)==citations(after)
    if block_number==3:
        assert collections.Counter(commands(after))-collections.Counter(commands(before))=={r'\ref':1}
        assert not collections.Counter(commands(before))-collections.Counter(commands(after))
        assert collections.Counter(references(after))-collections.Counter(references(before))=={r'\ref{def:common-conventions}':1}
        assert not collections.Counter(references(before))-collections.Counter(references(after))
    elif block_number==5:
        removed=next(g['before'] for g in group if g['id']=='I18-prov-07')
        command_index=len(commands(before[:before.index(removed)]))
        seq=commands(before)
        assert seq[command_index]==r"\'"
        assert seq[:command_index]+seq[command_index+1:]==commands(after)
        assert references(before)==references(after)
    else:
        assert commands(before)==commands(after)
        assert references(before)==references(after)
    proposed=directory/f'block_{block_number:02d}_proposed.tex'
    diff=directory/f'block_{block_number:02d}.diff'
    proposed.write_text(after)
    diff.write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=Path(block['path']).name,tofile=proposed.name)))
    for g in group:
        g.update({'proposed_full_block':str(proposed.relative_to(ROOT)),
                  'proposed_full_block_sha256':sha(proposed),
                  'all_mathematical_segments_identical':True,'statement_bytes_identical':True,
                  'all_citations_identical':True,
                  'reference_change':'Exactly one added ref{def:common-conventions} in I18-prov-03.' if block_number==3 else 'Reference sequence identical.'})
    review_rows.append({'statement_id':block['statement_id'],'guard_ids':[g['id'] for g in group],
                       'original':block['path'],'original_sha256':block['sha256'],
                       'proposed':str(proposed.relative_to(ROOT)),'proposed_sha256':sha(proposed),
                       'diff':str(diff.relative_to(ROOT)),'diff_sha256':sha(diff),
                       'all_inline_display_mathematical_segments_identical':True,
                       'statement_bytes_identical':True,'citation_sequence_identical':True,
                       'reference_exception':block_number==3})

path=OUT/'S6_SERIES_PUBLISH_I_candidate18_provenance_guards.json'
path.write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n')
receipt={
    'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':18,
    'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'guards':str(path.relative_to(ROOT)),
    'guards_sha256':sha(path),'guard_count':7,'complete_owning_source_blocks_read':5,
    'types':{'D08':4,'D06':1,'D23':1,'D02':1},'full_block_comparisons':review_rows,
    'named_reference_exception':'I18-prov-03 adds exactly ref{def:common-conventions}; its definition and aux witnesses are separately bound. No other reference is added, removed or reordered.',
    'named_text_formatting_exception':"I18-prov-07 deletes the single text accent command \\' together with the word Poincare in the empty closing recap. All mathematical segments, reference and citation sequences are unchanged by that deletion.",
    'manual_review_scope':'All five complete original statements/proofs were actually read in current source. Each exact proposed prose/format substitution was manually reviewed against its mathematical scope; every other full-block byte is retained by the literal map. This record distinguishes that comparison from a claim of an independently reconstructed proof.',
    'canonical_source_unchanged':sha(source)==SOURCE_SHA,'mathematical_events_added':0,
    'ledger_classification_note':'No CHECK_EVENTS row is written here. The prompt4.3 classification of actual edited-proof rereadings is being assessed separately; no independent derivation is claimed.',
    'historical_reading_records_modified':False,'current_reading_record_modified':False,
    'final_provenance_gate_open':True,
}
rp=OUT/'S6_SERIES_PUBLISH_I_candidate18_provenance_guard_receipt.json'
rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
md=['# Paper I candidate18: exact provenance-agent source proposals','',
    'Seven unapplied guards follow complete readings of five owning source statements/proofs. The33-page image record remains immutable. No ledger or canonical source file was changed.','',
    '| Guard | Page | Type | Statement | Purpose |','|---|---:|---|---|---|']
for g in guards:md.append(f"|{g['id']}|{g['page']}|{g['type']}|{g['statement_id']}|{g['reason']}|")
md+=['',f'Guards SHA-256: `{sha(path)}`','',f'Receipt SHA-256: `{sha(rp)}`','',
     'The D06 guard adds only the named existing-definition reference. All five statement texts, every inline/display mathematical segment and all citations are unchanged. The D02 replacement preserves the existing exactly-once summation condition as a partition. The D23 input-group formatting was actually inspected in the private preview, which reports zero underfull/overfull boxes.','']
path.with_suffix('.md').write_text('\n'.join(md))
print(json.dumps({'guards':str(path.relative_to(ROOT)),'guards_sha256':sha(path),
                  'receipt':str(rp.relative_to(ROOT)),'receipt_sha256':sha(rp),
                  'count':7,'blocks':5,'canonical_source_unchanged':sha(source)==SOURCE_SHA},indent=2))
