#!/usr/bin/env python3
"""Archive the actual complete-proof comparison at candidate19 page66."""
from pathlib import Path
import datetime, hashlib, json, difflib, re
R=Path(__file__).resolve().parents[1]
O=R/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
s=(R/'S6_SERIES_PUBLISH_I.tex').read_text()
assert sha(s.encode())=='f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
label=r'\label{fam:src:F.3.2}'
pos=s.index(label)
a=s.rfind(r'\begin{proposition}',0,pos)
b=s.index(r'\end{proof}',pos)+len(r'\end{proof}')
x=s[a:b]
old='  This explicit comparison proves the assertion\nabout the compact-dual limit.'
assert x.count(old)==s.count(old)==1
y=x.replace(old,'',1)
assert y[:y.index(r'\end{proposition}')]==x[:x.index(r'\end{proposition}')]
assert re.findall(r'\\(?:label|hypertarget|ref|eqref|SeriesRef|cite)[^\n]*',x)==re.findall(r'\\(?:label|hypertarget|ref|eqref|SeriesRef|cite)[^\n]*',y)
for text,suffix in [(x,'_original.tex'),(y,'_proposed.tex'),(''.join(difflib.unified_diff(x.splitlines(True),y.splitlines(True),fromfile='candidate19/fam:src:F.3.2',tofile='candidate20-proposal/fam:src:F.3.2')),'.diff')]:
    p=O/('S6_SERIES_PUBLISH_I_candidate19_root_block_01'+suffix)
    assert not p.exists()
    p.write_text(text)
original='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_root_block_01_original.tex'
proposed='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate19_root_block_01_proposed.tex'
g={
'id':'I19-root-01','type':'D08','statement_id':'fam:src:F.3.2','page':66,
'source_sha256':sha(s.encode()),'old':old,'new':'',
'reason':'Delete the pure closing recap. The complete finite-cover matrices and monodromies, cusp asymptotics, proper-quotient escape, normalized covector limits u and -gamma, nonzero exterior-product limit, real span and Hodge-intersection calculation remain verbatim. The deleted sentence supplies no formula, map, hypothesis, number or reference.',
'original_full_block':original,'original_full_block_sha256':sha(x.encode()),
'proposed_full_block':proposed,'proposed_full_block_sha256':sha(y.encode()),
'root_review':{'reader':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; root, continuation of21 November2026','complete_original_statement_and_proof_actually_read':True,'complete_proposed_difference_actually_compared':True,'comparison_scope':'Full original proposition and attached proof read from source; proposed proof is the same complete block with the exact one-sentence deletion. This is a comparative rereading after exposure to the printed proof, with no independent derivation claim.'}}
r={'paper':'I','candidate':19,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':sha(s.encode()),'pdf_sha256':sha((R/'build/I_candidate19/S6_SERIES_PUBLISH_I.pdf').read_bytes()),'guards':[g],'canonical_source_changed':False,'mathematical_events_added_by_record':0,'event_accounting':'The actual complete rewritten-proof comparison is offered to the section4.3 manifest for one deduplicated used-and-rechecked event for this owner; final application remains a separate gate.'}
p=O/'S6_SERIES_PUBLISH_I_candidate19_root_guards.json';assert not p.exists();p.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'record':str(p.relative_to(R)),'sha256':sha(p.read_bytes()),'original_block_sha256':sha(x.encode()),'proposed_block_sha256':sha(y.encode()),'source_lines':[s[:a].count('\n')+1,s[:b].count('\n')+1],'block_characters':len(x)},indent=2))
