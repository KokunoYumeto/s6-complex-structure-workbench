#!/usr/bin/env python3
"""Preserve v1 and refine explicit maps, punctuation and current table binding."""
from pathlib import Path
import hashlib,json,re,importlib.util
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[3]
AREA=ROOT/'agents/ii_infra/recovery_20261121'
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
old_path=AREA/'S6_SERIES_PUBLISH_II_WJ_WL_guards.json'
old=json.loads(old_path.read_text())
assert sha(old_path.read_bytes())=='3f807f4cf424134f07d6d3c233e501f441cce3d7dca9d48499f43c331bac5318'
spec=importlib.util.spec_from_file_location('p',ROOT/'code/S6_SERIES_PUBLISH_II_packets.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
src=p.parse_source(ROOT/'S6_SERIES_PUBLISH_II.tex','II')
out=AREA/'WJ_WL_blocks_v2';out.mkdir(exist_ok=False)
guards=json.loads(json.dumps(old['guards']))
intro=next(g for g in guards if g['id'].endswith('local_proof_intro'))
intro['before']+='Pulling';intro['after']+='pulling'
family=next(g for g in guards if g['id'].endswith('compact_families'))
before=r'''of $C_2$ is the disjoint union of two copies of $\Pp^1$, identified
to first order at the preimages of the tacnode. Exchanging these
copies with the same parameter preserves their local ring'''
after=r'''of $C_2$ is the disjoint union of two copies of $\Pp^1$, parametrized
by $[s:t]\mapsto[s:t:0]$ on the line and
$[s:t]\mapsto[s^2:st:t^2]$ on the conic. The parameters $t/s$ agree
at the two preimages of the tacnode. Exchanging these copies with
these parameters preserves their local ring'''
assert family['after'].count(before)==1
family['after']=family['after'].replace(before,after)
before=r'''The cyclic group acts transitively on the components of
$C_r\times E'$, so $X_r$ is irreducible. Its normalization is
$(\coprod_{j=1}^r\Pp^1\times E')/\langle(\sigma_r,\tau_r)\rangle$.
Restriction of this quotient map to one component is an isomorphism
from $\Pp^1\times E'$: each orbit meets that component exactly once.'''
after=r'''The cyclic group acts transitively on the components of
$C_r\times E'$, so $X_r$ is irreducible. Let $\widetilde\sigma_r$
be the lift to the normalization $\nu_r:C_r^\nu\to C_r$ induced
by the displayed parameter maps, so
$\nu_r\widetilde\sigma_r=\sigma_r\nu_r$. The normalization of $X_r$ is
$(\coprod_{j=1}^r\Pp^1\times E')/\langle(\widetilde\sigma_r,\tau_r)\rangle$.
Choose a component $C_{r,0}$ of $C_r^\nu$. Restriction of the quotient
map to $C_{r,0}\times E'$ is an isomorphism. Its inverse sends a class
represented by $(z,e)$ with $z\in\widetilde\sigma_r^j C_{r,0}$ to
$(\widetilde\sigma_r^{-j}z,\tau_r^{-j}e)$; this expression is unchanged
on each orbit and is holomorphic on every component.'''
assert family['after'].count(before)==1
family['after']=family['after'].replace(before,after)

inline=lambda s:re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',s,re.S)
display=lambda s:re.findall(r'\\\[(.*?)\\\]',s,re.S)
refs=lambda s:re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef)\{[^}]*\}|\\CompendiumRef\{[^}]*\}\{[^}]*\}|\\cite(?:\[[^\]]*\])?\{[^}]*\}',s)
blocks=[]
for tag,owner in [('02WJ','night:P4.12'),('02WL','night:P4.14')]:
 r=src['statement_labels'][owner]
 before=src['text'][r['start']:max([r['end']]+[q['end'] for q in r['proofs']])]
 old_block=next(x for x in old['blocks'] if x['tag']==tag)
 assert sha(before)==old_block['original_full_block_sha256']
 after=before
 gg=[g for g in guards if g['tag']==tag]
 for g in gg:
  assert before.count(g['before'])==1,(tag,g['id'])
  assert after.count(g['before'])==1
  after=after.replace(g['before'],g['after'],1)
  g['literal_math_map']={'inline_before':inline(g['before']),'inline_after':inline(g['after']),'display_before':display(g['before']),'display_after':display(g['after'])}
  g['literal_reference_map']={'before':refs(g['before']),'after':refs(g['after'])}
  g['source_sha256']=src['sha256']
 paths={}
 for side,text in [('before',before),('after',after)]:
  f=out/f'S6_SERIES_PUBLISH_II_{tag}_{side}.tex';f.write_text(text)
  key='original_full_block' if side=='before' else 'proposed_full_block';paths[key]=str(f.relative_to(ROOT));paths[key+'_sha256']=sha(text)
 for g in gg:g.update(paths)
 blocks.append({'tag':tag,'statement_id':owner,**paths,'guard_ids':[g['id'] for g in gg],
                'original_equals_v1_and_original_released_block':True,
                'displayed_target_statement_conclusions_identical':True,
                'global_math_reference_sequence_identity_claimed':False})
 print('COMPLETE PROPOSED V2 '+tag+'\n'+after)

table=next(g for g in guards if g['tag']=='program_table')
oldrow=table['after'].replace(table['before'].replace(r'\end{longtable}}',''),'',1) if False else None
row=re.search(r'Exact rational jet restrictions.*?\\\\\[3pt\]\n',table['after']).group()
s=src['text'];a=re.search(r'\\section\*?\{Programs\}',s).start();b=s.index(r'\begin{thebibliography}',a)
before=s[a:b];assert row not in before
after=before.replace(r'\end{longtable}}',row+r'\end{longtable}}')
assert after!=before and after.replace(row,'',1)==before
table['before']=before;table['after']=after;table['source_sha256']=src['sha256']
paths={}
for side,text in [('before',before),('after',after)]:
 f=out/f'S6_SERIES_PUBLISH_II_WL_program_table_{side}.tex';f.write_text(text)
 key='original_full_block' if side=='before' else 'proposed_full_block';paths[key]=str(f.relative_to(ROOT));paths[key+'_sha256']=sha(text)
table.update(paths)
print('COMPLETE PROPOSED V2 PROGRAM TABLE\n'+after)
record={'created_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':src['sha256'],
        'supersedes':{'path':str(old_path.relative_to(ROOT)),'sha256':sha(old_path.read_bytes()),'reason':'Explicit global cubic parameter maps and holomorphic inverse for the normalized quotient; correct the introductory lowercase; rebind current program table while preserving every existing row.'},
        'guards':guards,'blocks':blocks,'program_table':paths,
        'status':'UNAPPLIED; complete actual pair review and root approval required',
        'guard_count':len(guards),'owner_count':2,'events_added':0,'canonical_files_modified':False}
f=AREA/'S6_SERIES_PUBLISH_II_WJ_WL_guards_v2.json'
with f.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
print('FINAL_GUARDS',str(f.relative_to(ROOT)),sha(f.read_bytes()),len(guards))
