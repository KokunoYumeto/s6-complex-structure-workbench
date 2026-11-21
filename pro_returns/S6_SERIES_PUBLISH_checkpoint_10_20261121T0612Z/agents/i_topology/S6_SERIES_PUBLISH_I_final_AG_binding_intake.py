#!/usr/bin/env python3
"""Read-only final-source transport of the existing A--G global evidence."""
from pathlib import Path
import collections,csv,datetime,difflib,hashlib,json,re

R=Path('/workspace/scratch/653608133b22/work')
O=R/'agents/i_topology'
P='S6_SERIES_PUBLISH_I_final_AG'
sha=lambda t:hashlib.sha256(t if isinstance(t,bytes) else t.encode()).hexdigest()
s=(R/'S6_SERIES_PUBLISH_I.tex').read_text()
assert sha(s)=='26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e'
applied_path=R/'records/S6_SERIES_PUBLISH_I_candidate13_visual_finalize_applied.json'
applied=json.loads(applied_path.read_text())
old=s
for g in reversed(applied['changes']):
    assert old.count(g['new'])==1, g['reason']
    old=old.replace(g['new'],g['old'])
assert sha(old)==applied['before_source_sha256']=='38fd3831cb7be2eb60d856024571f9f8ec9105df45b445714251c41932580bbb'
(O/(P+'_reconstructed_candidate12.tex')).write_text(old)
(O/(P+'_current_source_26a.tex')).write_text(s)
ledger=R/'CHECK_EVENTS.tsv'
assert sha(ledger.read_bytes())=='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
with ledger.open() as f:events=list(csv.DictReader(f,delimiter='\t'))
assert len(events)==7866

ENV=re.compile(r'\\begin\{(maintheorem|theorem|proposition|corollary|lemma|definition|remark|cited|computed)\}')
def location(t,label):
    p=t.index('\\label{'+label+'}')
    m=list(ENV.finditer(t[:p]))[-1]
    e=t.index('\\end{'+m[1]+'}',p)+len('\\end{'+m[1]+'}')
    return m,e
def root_block(t,label,proof=True):
    m,e=location(t,label)
    if proof and re.match(r'\s*\\begin\{proof\}',t[e:]):
        e=t.index('\\end{proof}',e)+len('\\end{proof}')
    return t[m.start():e]
def abc_block(t,label):
    m,e=location(t,label)
    nxt=re.search(r'\\begin\{(proof|maintheorem|theorem|proposition|corollary|lemma|definition|remark|cited|figure)\}',t[e:])
    if nxt and nxt[1]=='proof':
        e=t.index('\\end{proof}',e+nxt.start())+len('\\end{proof}')
    return t[m.start():e]
def fg_block(t,label):
    p=t.index('\\label{'+label+'}');a=t.rfind('\\begin{',0,p)
    e=t.index('\\end{proof}',p)+len('\\end{proof}')
    return t[a:e]
def outline(t,x):
    a=t.index('\\hypertarget{outline-I-'+x+'}');e=t.index('\\end{enumerate}',a)+len('\\end{enumerate}')
    return t[a:e]
def diff(a,b,title):
    return '\n'.join(difflib.unified_diff(a.splitlines(),b.splitlines(),fromfile=title+' prior',tofile=title+' current',n=5))

abc_path=R/'agents/i_analytic/S6_SERIES_PUBLISH_I_global_ABC_final_applied_binding.json'
de_path=R/'records/S6_SERIES_PUBLISH_I_global_DE_final_binding.json'
fg_path=O/'S6_SERIES_PUBLISH_I_final_FG_e9_applied_binding.json'
abc=json.loads(abc_path.read_text());de=json.loads(de_path.read_text());fg=json.loads(fg_path.read_text())
records=[];diffs=[]
for label,item in abc['blocks'].items():
    a=item['text'];b=abc_block(s,label)
    records.append({'scope':'ABC','label':label,'prior_source_sha256':abc['source_sha256'],'prior_block_sha256':sha(a),'current_block_sha256':sha(b),'bytes_identical':a==b,'prior_block':a,'current_block':b})
    if a!=b:diffs.append(diff(a,b,'ABC '+label))
for item in de['direct_receiving_blocks']:
    label=item['label'];a=root_block(old,label);b=root_block(s,label)
    assert sha(a)==item['sha256'],label
    records.append({'scope':'DE','label':label,'prior_source_sha256':de['source_sha256'],'prior_block_sha256':sha(a),'current_block_sha256':sha(b),'bytes_identical':a==b,'prior_block':a,'current_block':b,'prior_scope_includes_immediate_proof':item['immediate_proof_in_block']})
    if a!=b:diffs.append(diff(a,b,'DE '+label))
h0=abc_block(old,'inv:A3.1');h=abc_block(s,'inv:A3.1')
assert sha(h0)==de['credited_hodge_full_proof_sha256']
records.append({'scope':'DE explicit credited Hodge proof','label':'inv:A3.1','prior_source_sha256':de['source_sha256'],'prior_block_sha256':sha(h0),'current_block_sha256':sha(h),'bytes_identical':h0==h,'prior_block':h0,'current_block':h})
for item in fg['current_full_proof_blocks']:
    label=item['statement_id'];a=item['current_complete_block'];b=fg_block(s,label)
    assert sha(a)==item['current_block_sha256']
    records.append({'scope':'FG','label':label,'prior_source_sha256':fg['current_source_sha256'],'prior_block_sha256':sha(a),'current_block_sha256':sha(b),'bytes_identical':a==b,'prior_block':a,'current_block':b})
    if a!=b:diffs.append(diff(a,b,'FG '+label))

headlines={};heads=[]
for x in 'ABCDEFG':
    label='series:I:'+x;current=root_block(s,label,False);out=outline(s,x)
    if x in 'ABC':
        prior=abc['blocks'][label]['text'];priorout=abc['outlines'][x];prior_source=abc['source_sha256']
    elif x in 'DE':
        prior=root_block(old,label,False);priorout=outline(old,x);prior_source=de['source_sha256']
        assert sha(prior)==de['main_statement_hashes'][label]
    else:
        prior=fg['complete_headlines_and_outlines_actually_read'][x]['statement'];priorout=fg['complete_headlines_and_outlines_actually_read'][x]['outline'];prior_source=fg['current_source_sha256']
    headlines[x]={'label':label,'statement':current,'outline':out,'statement_sha256':sha(current),'outline_sha256':sha(out),'outline_items':len(re.findall(r'\\item(?:\s|\\)',out)),
                  'prior_source_sha256':prior_source,'prior_statement_sha256':sha(prior),'prior_outline_sha256':sha(priorout),'statement_bytes_identical':current==prior,'outline_bytes_identical':out==priorout,'statement_diff':diff(prior,current,x+' headline'),'outline_diff':diff(priorout,out,x+' outline')}
    heads.append('\n===== CURRENT THEOREM '+x+' =====\n'+current+'\n\n===== CURRENT OUTLINE '+x+' =====\n'+out+'\n')
    if out!=priorout:diffs.append(diff(priorout,out,x+' outline'))
    if current!=prior:diffs.append(diff(prior,current,x+' headline'))
a=old.index(r'\hypertarget{outline-I-D}{}');b=old.index(r'\hypertarget{outline-I-F}{}',a)
assert sha(old[a:b])==de['complete_outlines_sha256']

# The positive restatement was not a direct F/G receiving block: compare it explicitly.
counter_old=fg_block(old,'push:src:D.2.2');counter_new=fg_block(s,'push:src:D.2.2')
po=counter_old[counter_old.index(r'\begin{proof}'):];pn=counter_new[counter_new.index(r'\begin{proof}'):]
assert po==pn
counter={'label':'push:src:D.2.2','prior_block':counter_old,'current_block':counter_new,'proof_bytes_identical':True,'proof_sha256':sha(po),'diff':diff(counter_old,counter_new,'D2.2 positive restatement')}
diffs.append(counter['diff'])

marker_maps=[g for g in applied['changes'] if 'proof marker' in g['reason'] or 'proof alias' in g['reason']]
labels=lambda t:collections.Counter(re.findall(r'\\label\{([^}]+)\}',t))
tags=lambda t:collections.Counter(re.findall(r'\\hypertarget\{tag-([^}]+)\}',t))
assert labels(old)==labels(s) and tags(old)==tags(s)
event_ids=list(abc['unchanged_event_ids'])+['publish-I-global-DE-exposed-comparison-D','publish-I-global-DE-exposed-comparison-E','publish-I-global-DE-consistency-computation-D','publish-I-global-DE-consistency-computation-E']+fg['reused_event_ids']
event_by={e['event_id']:e for e in events};assert all(x in event_by for x in event_ids)
intake={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Intake: pending actual current-headline/outline and changed-input reading',
        'current_source_sha256':sha(s),'ledger_sha256':sha(ledger.read_bytes()),'ledger_rows':len(events),'candidate12_reconstruction_sha256':sha(old),
        'input_receipts':[{ 'path':str(p),'sha256':sha(p.read_bytes())} for p in [applied_path,abc_path,de_path,fg_path]],
        'prior_evidence_event_rows':[event_by[x] for x in event_ids],
        'block_comparisons':records,'headlines':headlines,'counterexample_presentation_comparison':counter,'changes_since_candidate12':applied['changes'],
        'all_label_and_tag_multiplicities_preserved':True,'new_events':0,'new_independent_credit':0,'new_mathematical_computations':0}
(O/(P+'_binding_intake.json')).write_text(json.dumps(intake,indent=2)+'\n')
(O/(P+'_current_headlines_outlines.txt')).write_text('\n'.join(heads))
(O/(P+'_actual_input_diffs.txt')).write_text('\n\n'.join(diffs)+'\n')
(O/(P+'_D22_complete_old_current.txt')).write_text('===== CANDIDATE12 COMPLETE BLOCK =====\n'+counter_old+'\n\n===== CURRENT COMPLETE BLOCK =====\n'+counter_new+'\n')
print(json.dumps({'source':sha(s),'ledger':sha(ledger.read_bytes()),'ledger_rows':len(events),'blocks':len(records),'unchanged':sum(x['bytes_identical'] for x in records),'changed':[{k:r[k] for k in ['scope','label','prior_block_sha256','current_block_sha256']} for r in records if not r['bytes_identical']],
                  'headlines':{x:{k:r[k] for k in ['statement_bytes_identical','outline_bytes_identical','outline_items']} for x,r in headlines.items()}},indent=2))
