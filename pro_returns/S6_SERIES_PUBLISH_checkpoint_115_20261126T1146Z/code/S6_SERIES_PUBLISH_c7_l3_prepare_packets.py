#!/usr/bin/env python3
"""Stage the entire L3 comparison, with exact guards and scoped records."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import io
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_profile_synthesis'
BASE='S6_SERIES_PUBLISH_III_02L3_'
ID='maps:src:D.2.28'
source_bytes=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(source_bytes).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source=source_bytes.decode()
frozen={
 LANE/(BASE+'fresh_derivation.md'):'1936234b624552e0147523383cedee44efd304b13e592b0017d4ddbf20a6255a',
 ROOT/'code/S6_SERIES_PUBLISH_c7_l3_profiles.py':'6fea4368d1b0d4e5fc6f87f99e673a5e18c22dc53d040439dde642c947d319e6',
 ROOT/'code/S6_SERIES_PUBLISH_c7_l3_profiles.out':'b340c7f982f79ab0c6a9cd25e8f529b24582483aefa8cd6177836906bfd6f254',
}
for path,digest in frozen.items():
    assert sha256(path.read_bytes()).hexdigest()==digest

def released(kind,env):
    lines=(LANE/(BASE+'released_'+kind+'.tex')).read_text().splitlines()
    assert all(x.startswith('%') for x in lines[:5])
    value='\n'.join(lines[5:])
    assert value.startswith('\\begin{'+env+'}') and value.endswith('\\end{'+env+'}')
    assert source.count(value)==1
    first=1+source[:source.index(value)].count('\n')
    return value,(first,first+value.count('\n'))

old_statement,sspan=released('statement','corollary')
old_proof,pspan=released('proof','proof')
assert pspan==(13419,13435)
assert sha256(old_proof.encode()).hexdigest()=='fb6429bf9ee4bd112583c4d01e51c8a37ec84dd045b47589e9ac933ed73925df'
assert len(re.findall(r'\\item\b',old_proof))==1
receiver_path=LANE/(BASE+'receiving.tex')
new=receiver_path.read_text().rstrip('\n')
new_statement,new_proof=new.split(r'\begin{proof}',1)
new_statement=new_statement.rstrip('\n')
new_proof=r'\begin{proof}'+new_proof

def identities(value):
    return tuple(sorted(re.findall(pattern,value)) for pattern in
                 (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'))

assert identities(old_statement)==identities(new_statement)
assert identities(old_proof)==identities(new_proof)
assert tuple(map(len,identities(new)))==(2,2,1)
assert all(new.count('\\label{'+label+'}')==1 for label in identities(new)[0])

def escaped(value,index):
    backslashes=0
    index-=1
    while index>=0 and value[index]=='\\':
        backslashes+=1
        index-=1
    return backslashes%2==1

level=0
for i,char in enumerate(new):
    if char in '{}' and not escaped(new,i):
        level += 1 if char=='{' else -1
        assert level>=0
assert level==0
stack=[]
for command,env in re.findall(r'\\(begin|end)\{([^}]+)\}',new):
    if command=='begin':
        stack.append(env)
    else:
        assert stack and stack.pop()==env
assert not stack
math=[]
for match in re.finditer(r'\\\[|\\\]|\\\(|\\\)|(?<!\\)\$',new):
    token=match.group()
    if token in (r'\[',r'\('):
        assert not math
        math.append(token)
    elif token in (r'\]',r'\)'):
        assert math.pop()=={r'\]':r'\[',r'\)':r'\('}[token]
    elif math==['$']:
        math.pop()
    else:
        assert not math
        math.append('$')
assert not math
labels=set(re.findall(r'\\label\{([^}]+)\}',source))
assert set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',new))<=labels
assert not re.search(r'\\(?:path|StatementRecord)\b',new)
print('PASS frozen fresh proof/program/output and canonical source unchanged.')
print('PASS full17-line original proof with its sole enumerated item; all auxiliaries compared.')
print('GUARDS statement',sspan,'proof',pspan)
print('IDENTITIES 2 labels,2 hypertargets,1 equation tag preserved exactly and uniquely.')
print('SOURCE_CHECKS braces, environment nesting, math delimiters and all references pass; no TeX build or page reading claimed.')

def write_table(suffix,fields,rows):
    buffer=io.StringIO(newline='')
    writer=csv.DictWriter(buffer,fields,delimiter='\t',lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    (LANE/(BASE+suffix+'.tsv')).write_text(buffer.getvalue(),newline='\n')

reason=('Complete251-line fresh synthesis and new raw-only151-line program with all86 output lines '
        'preceded individual exposure. Whole original statement, all17 proof lines and every '
        'auxiliary read against the complete receiver. All21 counts,59 patterns,50 initial rows, '
        'the12/4/5 multiplicity split and all affine conditions stand. Exact admitted local/global '
        'maps and inverses supply the proof and standard oriented S6 identification. No D25,D26,D27, '
        'historical execution or new primary-source credit. Canonical/unit/build/page gates remain open.')
guards=[]
for kind,before,after,span in [('statement',old_statement,new_statement,sspan),('proof',old_proof,new_proof,pspan)]:
    guards.append(dict(statement_id=ID,old_text=before,new_text=after,
                      reason=f'Separate {kind} guard at lines{span[0]}--{span[1]}. '+reason))
write_table('replacements',['statement_id','old_text','new_text','reason'],guards)
trial=source
for guard in guards:
    assert trial.count(guard['old_text'])==1
    trial=trial.replace(guard['old_text'],guard['new_text'],1)
for guard in reversed(guards):
    assert trial.count(guard['new_text'])==1
    trial=trial.replace(guard['new_text'],guard['old_text'],1)
assert trial==source
print('PASS both individual guards and their combined exact inverse.')

def between(value,start,end):
    first=value.index(start)
    return value[first:value.index(end,first+len(start))].rstrip('\n')

defects=[]
def defect(suffix,kind,before,after,why):
    hits=[(part,span) for part,span in [(old_statement,sspan),(old_proof,pspan)] if before in part]
    assert len(hits)==1
    part,span=hits[0]
    assert part.count(before)==1 and after in new
    old_line=span[0]+part[:part.index(before)].count('\n')
    new_line=1+new[:new.index(after)].count('\n')
    defects.append(dict(change_id='c7-III-02L3-'+suffix,type=kind,statement_id=ID,
                        old_location=f'S6_SERIES_PUBLISH_III.tex:{old_line}',old_page='',
                        new_location=str(receiver_path.relative_to(ROOT))+f':{new_line}',new_page='',
                        old_text=before,new_text=after,reason=why,
                        review_status='proposed; root admission, canonical application and final page review pending'))

defect('header','D10',next(x for x in old_statement.splitlines() if x.startswith(r'\StatementRecord')),
       r'\textup{\small(tag 02L3)}','Keep the small permanent tag and remove the machine navigation header.')
defect('title','D14',old_statement.splitlines()[0],new_statement.splitlines()[0],
       'Name the classified sphere outputs directly while retaining the same corollary identity.')
defect('pattern-definition','D02',
       'A pattern means\na marked initial section/zero/additive-filling row, not an\nindividual complex structure or a sample of its multiplicities.',
       'A pattern consists of a marked initial section pair, zero position\nand additive filling choice.',
       'Give the positive marked-data definition; the proof supplies the explicit projection forgetting the additive choice.')
defect('pattern-file','D09',
       'Their full individual\nconditions, including all affine parameters, are \\eqref{maps:eq:D.HY3}--\\eqref{maps:eq:D.HY5}\nand the complete table\n\\path{records/manifolds_nonstar_sphere_patterns.csv}.',
       between(new_statement,'There are $59$ patterns','Thus twelve profiles'),
       'Resolve the complete list and every affine/group condition within the paper by their mathematical statement identities.')
defect('summary-file','D09',
       'The profile summary is also saved as\n\\path{records/manifolds_complete_natural_sphere_profiles.csv}.',
       between(new_proof,'For each initial row take','Every additive profile'),
       'Prove the complete count by the component tests and pattern projection; keep file paths in the later programs/records apparatus.')
defect('machine-item','D10',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
       'The finite initial reduction in \\ref{maps:src:D.2.22} applies to',
       'Replace the single machine-numbered item with a connected mathematical proof.')
defect('certificate-narration','D09',
       between(old_proof,'The exact program',r'\end{enumerate}'),
       between(new_proof,'For each initial row take','Every additive profile'),
       'Replace historical program bookkeeping with the actual finite method and result. The admitted L2 proof supplies its star auxiliaries; no historical execution is claimed.')
defect('smooth-map','D22',
       'Their\nsimply connected homology-sphere outputs are homotopy spheres\nby Hurewicz and Whitehead, and $\\Theta_6=0$ gives the stated\nsmooth type, as in \\ref{maps:src:D.3.2}.',
       between(new_proof,'Finally \\ref{maps:src:D.2.26}',r'\end{proof}'),
       'Use the exact oriented comparison and inverse supplied by L1, followed by the explicit suspension rotation and radial map. Every original mathematical conclusion stands.')
defect('complete-proof','D14',old_proof,new_proof,
       'Give one complete aggregation proof: exhaustive inputs, every excluded cap, full integral and group criterion, profile count, unbounded parameters and oriented smooth identification. Whole old and new proofs have been read.')
defect('statement-scope-order','D14',old_statement,new_statement,
       'Retain the entire scope and unchanged D.ST13 table while organizing the list, precise parameter references and smooth conclusion without record-file dependencies.')
defect_fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page',
               'old_text','new_text','reason','review_status']
write_table('defects',defect_fields,defects)
assert len(defects)==10 and not any(x['type'] in ('D25','D26','D27') for x in defects)
for row in defects:
    print('DEFECT',row['type'],row['change_id'],row['old_location'])

now=datetime.now(timezone.utc).isoformat()
fresh_paths=[str(path.relative_to(ROOT)) for path in frozen]
fresh_paths += [str((LANE/(BASE+'fresh_data.json')).relative_to(ROOT)),
                str((LANE/(BASE+'fresh_patterns.tsv')).relative_to(ROOT)),
                'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02L3_fresh_root_review.md']
post_paths=[str((LANE/(BASE+suffix)).relative_to(ROOT)) for suffix in
            ['released_statement.tex','released_proof.tex','receiving.tex','comparison.md','replacements.tsv','defects.tsv']]
assert all((ROOT/path).exists() for path in fresh_paths+post_paths)
common=dict(statement_id=ID,date='2026-11-25',date_utc=now,
            who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
            source_file='S6_SERIES_PUBLISH_III.tex',source_row=sspan[0],
            evidence_group='publish:c7:III:02L3:check-sequence',
            publish_input_file=str((LANE/(BASE+'comparison.md')).relative_to(ROOT)),publish_input_row=1)
events=[]
for suffix,kind,phase,outcome,where in [
 ('fresh-complete-derivation','targeted proof check','before individual original L3 exposure',
  'Complete251-line fresh synthesis derives the exact21-profile scope from admitted integral local/global maps, full Seifert conditions, all affine conjugacies and inverses, and explicit oriented S6 comparison. It covers every permitted filling and refinement, all59 patterns and50 initial rows, and the12/4/5 split. Fresh completion01:33:43 UTC precedes release01:35:58 UTC. Author review adds no independent-proof credit.',fresh_paths),
 ('fresh-raw-component-enumeration','computation or formal certificate','before individual original L3 exposure',
  'New151-line program reads only the raw matrices/cocycles/component coordinates. Primitive nullspace extraction, full cyclic zero-component testing, literal component-order calculation and exact rational fixed-long tests reconstruct172 natural rows and all59 sphere patterns on50 rows. All86 output lines and empty stderr read. Every profile count and the unique two-finite pattern is printed. No multiplicity sample replaces the unbounded proof; no historical target program or derived catalogue read.',fresh_paths),
 ('whole-original-comparison','used and rechecked in this run','after whole original L3 exposure',
  'Entire original statement and17-line proof, sole item and every auxiliary compared against the complete receiver. All21 counts,59/50 totals,12/4/5 split, full affine conditions and standard smooth conclusion stand. Original star computation narration is replaced by the admitted L2 full mathematics and new profile tally; no historical execution claimed. Exact statement/proof guards,2 labels,2 hypertargets and D.ST13 preserved with joint inverse. Ten defect rows, no D25/D26/D27. Source syntax earns no build/unit/page credit. All three events share one evidence group.',fresh_paths+post_paths),
]:
    events.append(dict(common,event_id='publish:c7:III:02L3:'+suffix,type=kind,
                       source_event_type=kind,phase=phase,outcome=outcome,where='; '.join(where)))
event_fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row',
              'source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
write_table('CHECK_EVENTS',event_fields,events)
(LANE/(BASE+'staged_bibliography.bib')).write_text('% No new bibliography entry or primary-source retrieval in this comparison.\n',newline='\n')
assert (ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()==source_bytes
print('EVENTS',len(events),'one shared evidence group; no additional independent-proof credit.')
for suffix in ['receiving.tex','comparison.md','replacements.tsv','defects.tsv','CHECK_EVENTS.tsv']:
    path=LANE/(BASE+suffix)
    print('SHA256',sha256(path.read_bytes()).hexdigest(),str(path.relative_to(ROOT)))
print('STAGED_UTC',now)
print('CANONICAL_UNCHANGED',sha256(source_bytes).hexdigest())
