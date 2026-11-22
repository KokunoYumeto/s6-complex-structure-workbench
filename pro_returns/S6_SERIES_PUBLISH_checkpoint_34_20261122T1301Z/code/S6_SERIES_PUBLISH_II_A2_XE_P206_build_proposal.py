#!/usr/bin/env python3
"""Bind A2's P4.40/P206 proposal and four local-consumer citation edits.

Reads the canonical paper; writes only A2's work area. No canonical edit.
"""
from pathlib import Path
import difflib
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
folder=root/'agents/continuation2_A'
original=folder/'S6_SERIES_PUBLISH_II_A2_02XE_original_current_v1.tex'
old=original.read_text()
prop=(folder/'S6_SERIES_PUBLISH_II_A2_02XE_proposed_working.tex').read_text().rstrip()
lemma=(folder/'S6_SERIES_PUBLISH_II_A2_P206_proposed_working.tex').read_text().rstrip()
source=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
assert source.count(old)==1
new=old
guards=[]


def edit(before,after,defects,reason):
    global new
    assert new.count(before)==1,(before[:120],new.count(before))
    guards.append({'id':f'XE-P206-{len(guards)+1:03d}',
                   'old':before,'new':after,'expected_count':1,
                   'defect_ids':defects,'reason':reason})
    new=new.replace(before,after)


def proof_parts(block):
    p=block.index(r'\begin{proof}')
    end=block.index(r'\end{enumerate}',p)
    hits=list(re.finditer(r'\\item\b',block[p:end]))
    starts=[p+m.start() for m in hits]
    return block[:p],block[p:starts[0]],[block[a:b] for a,b in
           zip(starts,starts[1:]+[end])],block[end:]


old_statement,old_prefix,old_items,old_suffix=proof_parts(old)
new_statement,new_prefix,new_items,new_suffix=proof_parts(prop)
assert len(old_items)==4 and len(new_items)==2
edit(old_statement,new_statement,['D25','D04','D10','D16'],
     'The compact frozen example refutes the unqualified assertion. Add the necessary positive-Euler hypothesis and its refined alias; preserve the owner, tag and original labels; resolve the standing domain and title.')
edit(old_prefix,new_prefix,['D10'],
     'Remove the production-marker enumeration while preserving the proof environment.')
edit(old_items[0]+old_items[1],'',['D14','D04'],
     'Move the complete local hyperplane/model argument to numbered lemma P206 below; the same argument remains once, with explicit maps. Its final uniform-A1 application is retained in the proposition conclusion.')
edit(old_items[2],new_items[0],['D25','D04','D22'],
     'Exclude reduced horizontal divisors using their proved e=0 before the coefficient-two case. Preserve contraction and conductor-Euler steps; give the precise pushout and rational-normalization conclusion at positive Euler scope.')
edit(old_items[3],new_items[1],['D04','D22'],
     'Preserve the graph/Euler/counting contradiction. Give P4.26 for the global budget and apply the general R4 meridian presentation through the exact pushout; retain its displayed counts and retarget the local model classification to P206.')
if old_suffix!=new_suffix:
    edit(old_suffix,new_suffix,['D10'],
         'Keep the proof closure with consistent paragraph spacing.')
anchor=prop.splitlines()[0]
edit(anchor,lemma+'\n\n'+anchor,['D14','D16'],
     'Insert P206 immediately before its global application. All original local arguments are preserved or explicitly mapped; expanded restriction maps identify the same rings and ambient coordinate changes.')
assert new==lemma+'\n\n'+prop
replay=old
for row in guards:
    assert replay.count(row['old'])==row['expected_count']
    replay=replay.replace(row['old'],row['new'])
assert replay==new

def display_math(block):
    return [re.sub(r'\s+','',x) for x in re.findall(r'\\\[(.*?)\\\]',block,re.S)]

old_displays=display_math(old)
assert len(old_displays)==4
assert display_math(lemma)==old_displays[:3]
assert display_math(prop)==old_displays[3:]
assert all(x in re.findall(r'\\label\{([^}]+)\}',prop)
           for x in re.findall(r'\\label\{([^}]+)\}',old))
assert r'\hypertarget{tag-P206}' not in source
assert r'\label{ii:excess-one-curve-germs}' not in source

(folder/'S6_SERIES_PUBLISH_II_A2_XE_P206_combined_working.tex').write_text(new)
(folder/'S6_SERIES_PUBLISH_II_A2_XE_P206_guards_working.json').write_text(json.dumps(guards,indent=2)+'\n')
(folder/'S6_SERIES_PUBLISH_II_A2_XE_P206_working.diff').write_text(''.join(difflib.unified_diff(
    old.splitlines(True),new.splitlines(True),fromfile=str(original.relative_to(root)),
    tofile='P206_and_positive_Euler_P440')))

consumer_changes=[
 ('night:P4.42','02XG',
  'The exact excess-one classification in P4.40 identifies',
  r'The exact excess-one classification in \cref{ii:excess-one-curve-germs} identifies'),
 ('night:P4.46','02XK',
  'The exact classification in P4.40 shows that its only',
  r'The exact classification in \cref{ii:excess-one-curve-germs} shows that its only'),
 ('night:P4R.16','02Y9',
  'The analytic ring calculation in P4.40 supplies actual ambient\ncoordinates for this curve.',
  'Lemma~\\ref{ii:excess-one-curve-germs} gives ambient\ncoordinates for this curve.'),
 ('night:P4R.17','02YA',
  'The actual analytic ring calculation in P4.40 gives precisely',
  r'Lemma~\ref{ii:excess-one-curve-germs} gives precisely')]
consumer_rows=[]
diffs=[]
for owner,tag,before,after in consumer_changes:
    match=re.search(r'\\begin\{(?:proposition|lemma|theorem|corollary)\}[^\n]*\\label\{'+re.escape(owner)+r'\}',source)
    assert match,owner
    end=source.index(r'\end{proof}',match.start())+len(r'\end{proof}')
    block=source[match.start():end]
    changed=block
    header=next(line for line in block.splitlines() if line.startswith(r'\StatementRecord'))
    changed_header=header.replace(r'\SeriesRef{night:P4.40}',r'\SeriesRef{ii:excess-one-curve-germs}')
    assert header!=changed_header
    scoped=[]
    for a,b in [(header,changed_header),(before,after)]:
        assert changed.count(a)==1,(owner,a)
        assert source.count(a)==1,(owner,'source ambiguity')
        scoped.append({'id':f'XE-consumer-{len(consumer_rows)+1:02d}-{len(scoped)+1}',
                       'scope_owner':owner,'old':a,'new':b,'expected_count':1,
                       'defect_ids':['D04']+(['D08'] if 'actual' in a else []),
                       'reason':'This inference uses only the unchanged local excess-one ring classification, now lemma P206; it does not use the positive-Euler global exclusion.'})
        changed=changed.replace(a,b)
    assert 'P4.40' not in changed
    consumer_rows.append({'owner':owner,'tag':tag,
        'before_sha256':hashlib.sha256(block.encode()).hexdigest(),
        'after_sha256':hashlib.sha256(changed.encode()).hexdigest(),
        'before_bytes':len(block.encode()),'after_bytes':len(changed.encode()),
        'guards':scoped})
    diffs.append(''.join(difflib.unified_diff(block.splitlines(True),changed.splitlines(True),
                                          fromfile=owner,tofile=owner+' with P206 reference')))

(folder/'S6_SERIES_PUBLISH_II_A2_XE_consumer_guards_working.json').write_text(json.dumps(
    {'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'consumers':consumer_rows,
     'source_writes':[]},indent=2)+'\n')
(folder/'S6_SERIES_PUBLISH_II_A2_XE_consumer_working.diff').write_text('\n'.join(diffs))
program_row=r'''Excess-one curve rings, their cotangent dimensions and the conductor graph counts (\cref{ii:excess-one-curve-germs,night:P4.40}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/S6_SERIES_PUBLISH_II_A2_P206_curve_algebra.py}{\nolinkurl{S6_SERIES_PUBLISH_II_A2_P206_curve_algebra.py}} \\[3pt]
'''
(folder/'S6_SERIES_PUBLISH_II_A2_XE_P206_Programs_row_working.tex').write_text(program_row)
print(json.dumps({'combined_sha256':hashlib.sha256(new.encode()).hexdigest(),
 'combined_bytes':len(new.encode()),'owner_guards':len(guards),
 'consumer_guards':sum(len(x['guards']) for x in consumer_rows),
 'original_displays_preserved':len(old_displays),
 'canonical_source_sha256':hashlib.sha256(source.encode()).hexdigest()},indent=2))
