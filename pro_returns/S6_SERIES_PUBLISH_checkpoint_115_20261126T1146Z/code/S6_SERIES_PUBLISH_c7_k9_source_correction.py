#!/usr/bin/env python3
"""Stage the bounded K9 source correction; preserve prior frozen evidence."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import csv
import io
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/'agents/continuation5_iii_finite'
LANE=ROOT/'agents/continuation7_iii_k9_source'
BASE='S6_SERIES_PUBLISH_III_02K9_'
ID='maps:src:D.1.11'
canonical=ROOT/'S6_SERIES_PUBLISH_III.tex'
source_bytes=canonical.read_bytes()
assert sha256(source_bytes).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source=source_bytes.decode()
assert sha256((OLD/(BASE+'derivation.md')).read_bytes()).hexdigest()=='706475d9d51ea13a7d8ba53f827e6e077f38f7a6791eb71974eac6a920449339'
old_statement=(OLD/(BASE+'receiving_statement.tex')).read_text().rstrip('\n')
old_receiving_proof=(OLD/(BASE+'receiving_proof.tex')).read_text().rstrip('\n')
before_one=r'''In particular $b_3(M)=0$. We use the marked classification on
Zhubr's class $\mathfrak M_0$, defined by this rank condition in
\cite[Section~1.1, p.~793]{manZhubr75}.
Theorems~3 and~5 of that paper, on pp.~795--796, give the
classification through the injective map'''
after_one=r'''In particular $b_3(M)=0$. We use the marked classification
established in \cite[Theorem~3, p.~795; Section~4.1, p.~809]{manZhubr75}
for simply connected spin six-manifolds with zero free third homology.
That proof constructs the representative by killing
$H_3/\operatorname{Tor}H_3$ while preserving the prescribed
isomorphism on $H_2$. Its uniqueness argument changes the marked
spin bordism to an $h$-cobordism.
Theorem~5 of that paper, on p.~796, gives the injective map'''
before_two=r'''For $N_1,N_2\in\mathfrak M_0(G)$ and isomorphisms
$\phi_i:H_2(N_i;\mathbb Z)\to G$, equality of their marked
bordism classes yields a degree $+1$ diffeomorphism
$F:N_1\to N_2$ satisfying $\phi_2F_*=\phi_1$.
\footnote{The English text of \cite[Section~1.2, p.~794]{manZhubr75}
prints $r(N)=\operatorname{rank}H_2(N)$. The definition of
$\mathfrak M_0$ on p.~793 and the marked Theorem~3 state the
$b_3=0$ form used here.}'''
after_two=r'''For closed simply connected spin six-manifolds $N_1,N_2$
with $b_3(N_i)=0$ and isomorphisms
$\phi_i:H_2(N_i;\mathbb Z)\to G$, equality of their marked
bordism classes therefore yields a degree $+1$ diffeomorphism
$F:N_1\to N_2$ satisfying $\phi_2F_*=\phi_1$.
Its inverse induces $\phi_1^{-1}\phi_2$ on second homology.
\footnote{The English rank conditions in
\cite[Sections~1.1--1.2, pp.~793--794]{manZhubr75} use $H_2$.
Section~4.1, p.~809, constructs the representative by killing
the free part of $H_3$ while preserving $H_2\simeq G$;
that construction and its marked uniqueness proof supply the
$b_3=0$ scope used here.}'''
new_proof=old_receiving_proof
for before,after in [(before_one,after_one),(before_two,after_two)]:
    assert new_proof.count(before)==1
    new_proof=new_proof.replace(before,after,1)
receiver=old_statement+'\n\n'+new_proof+'\n'
(LANE/(BASE+'receiving.tex')).write_text(receiver,newline='\n')

metadata=json.loads((ROOT/'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packet_structure.json').read_text())
scope=next(g for g in metadata['metadata_groups'] if g['candidate_tags']==['02K9'])
sspan=scope['statement_lines']
pspan=scope['proof_spans'][0]
lines=source.splitlines()
original_statement='\n'.join(lines[sspan[0]-1:sspan[1]])
original_proof='\n'.join(lines[pspan['start_line']-1:pspan['end_line']])
assert original_proof.startswith(r'\begin{proof}') and original_proof.endswith(r'\end{proof}')
assert source.count(original_statement)==source.count(original_proof)==1
assert sha256(original_proof.encode()).hexdigest()==pspan['sha256'] or sha256((original_proof+'\n').encode()).hexdigest()==pspan['sha256']

def identities(text):
    return tuple(sorted(re.findall(pattern,text)) for pattern in
                 (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'))
assert identities(original_statement)==identities(old_statement)
assert identities(original_proof)==identities(new_proof)
assert identities(new_proof)==identities(old_receiving_proof)
assert old_statement==(OLD/(BASE+'receiving_statement.tex')).read_text().rstrip('\n')
reason=('Latest complete canonical-source replacement after the bounded primary-source correction. '
        'Supersedes continuation-five K9 application guards, while retaining their defect rows and '
        'all prior frozen check evidence. Only the receiving proof source-description paragraph '
        'and footnote change: p793 also prints H2; the exact zero-free-H3 construction and '
        'marked uniqueness scope are proved in Section4.1 p809. Every mathematical conclusion stands.')
guards=[dict(statement_id=ID,old_text=original_statement,new_text=old_statement,reason=reason),
        dict(statement_id=ID,old_text=original_proof,new_text=new_proof,reason=reason)]
trial=source
for row in guards:
    assert trial.count(row['old_text'])==1
    trial=trial.replace(row['old_text'],row['new_text'],1)
for row in reversed(guards):
    assert trial.count(row['new_text'])==1
    trial=trial.replace(row['new_text'],row['old_text'],1)
assert trial==source

def write_table(path,fields,rows):
    buffer=io.StringIO(newline='')
    writer=csv.DictWriter(buffer,fields,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(rows)
    path.write_text(buffer.getvalue(),newline='\n')

write_table(LANE/(BASE+'replacements.tsv'),['statement_id','old_text','new_text','reason'],guards)
defects=[]
for suffix,before,after in [('rank-definition',before_one,after_one),('repeated-source-footnote',before_two,after_two)]:
    defects.append(dict(change_id='c7-III-02K9-'+suffix,type='D25',statement_id=ID,
       old_location=str((OLD/(BASE+'receiving_proof.tex')).relative_to(ROOT))+':'+str(1+old_receiving_proof[:old_receiving_proof.index(before)].count('\n')),
       old_page='',new_location=str((LANE/(BASE+'receiving.tex')).relative_to(ROOT))+':'+str(1+receiver[:receiver.index(after)].count('\n')),
       new_page='',old_text=before,new_text=after,
       reason='The asserted p793 H3 rank definition is contradicted by the visually read primary page. Replace it by the literal H2 printing and the exact Section4.1 p809 construction/uniqueness scope, with the marked map and inverse. This is one source-description finding in two loci; the classification conclusion stands.',
       review_status='proposed; root comparison, canonical application and final page review pending'))
write_table(LANE/(BASE+'defects.tsv'),['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'],defects)
now=datetime.now(timezone.utc).isoformat()
where='; '.join([str((LANE/(BASE+x)).relative_to(ROOT)) for x in ['comparison.md','receiving.tex','replacements.tsv','defects.tsv']])
common=dict(statement_id=ID,date='2026-11-25',date_utc=now,
  who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
  source_file='S6_SERIES_PUBLISH_III.tex',source_row=sspan[0],
  evidence_group='publish:c7:III:02K9:primary-source-correction',
  publish_input_file=str((LANE/(BASE+'comparison.md')).relative_to(ROOT)),publish_input_row=1,
  phase='post-admission bounded primary-source correction; no new blind check',where=where)
events=[]
for suffix,kind,outcome in [
 ('rank-description-refined',"refuted, with the refined statement's id",
  'Refuted only the earlier receiving proof/source-record assertion that Zhubr p793 prints rank H3=0: the byte-verified rendered page prints H2. Corrected proof identity maps:src:D.1.11. Section4.1 p809 explicitly kills free H3 while preserving H2≅G and supplies marked h-cobordism uniqueness. No homology, refined invariant, full mu coordinate, realization or diffeomorphism conclusion changes. Two D25 loci record one finding; no source normalization is guessed.'),
 ('whole-source-scope-recheck','used and rechecked in this run',
  'Root visually read primary793–796,807,809,810, the entire original19-line proof, whole prior and corrected receiving proof, affected historical notes and all exact guards. Theorem5 injectivity, quarter-Pontryagin definition and Section4.1 marked maps support the exact b3=0 application even with free H2. Earlier frozen derivation/chronology preserved. Latest canonical replacements supersede prior application guards; old defect history retained. Shared evidence group, no additional targeted or independent-proof credit and no build/page credit.'),
]:
    events.append(dict(common,event_id='publish:c7:III:02K9:'+suffix,type=kind,source_event_type=kind,outcome=outcome))
write_table(LANE/(BASE+'CHECK_EVENTS.tsv'),['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)

progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
with progress.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
row=next(r for r in rows if r['tag']=='02K9')
assert row['status']=='done'
row.update(status='open',packet_status='primary_source_description_correction_pending',assigned_checker=str(LANE.relative_to(ROOT)))
row['notes']+=' Reopened '+now+' solely for the false p793 source description in the prior receiving proof; exact Section4.1 source-scope correction staged. The mathematical theorem is unchanged; prior frozen evidence remains.'
write_table(progress,fields,rows)
assert canonical.read_bytes()==source_bytes
print('SOURCE_CORRECTION_STAGED_UTC',now)
print('ORIGINAL_STATEMENT_LINES',sspan,'ORIGINAL_PROOF_LINES',pspan['start_line'],pspan['end_line'])
print('ORIGINAL_STATEMENT_READBACK')
print(original_statement)
print('PASS prior mathematical statement unchanged; two exact receiving-proof paragraphs corrected.')
print('PASS all permanent identities, separate canonical guards and joint inverse.')
print('PASS prior frozen derivation and canonical source unchanged; two D25 loci are one source-description finding.')
print('K9_REOPENED_FOR_SOURCE_CORRECTION; no other progress row changed.')
for suffix in ['receiving.tex','comparison.md','replacements.tsv','defects.tsv','CHECK_EVENTS.tsv']:
    path=LANE/(BASE+suffix)
    print('SHA256',sha256(path.read_bytes()).hexdigest(),str(path.relative_to(ROOT)))
