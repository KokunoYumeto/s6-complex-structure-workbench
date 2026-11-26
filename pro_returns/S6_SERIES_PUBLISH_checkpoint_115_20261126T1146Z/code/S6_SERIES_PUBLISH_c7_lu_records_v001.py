#!/usr/bin/env python3
"""Stage LU replacements, exact guards, defects and narrowly typed check events."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv, io, re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_corrected_initial_receiving'
PREFIX='S6_SERIES_PUBLISH_III_02LU_'
SID='maps:src:D.2.52'
canonical_path=ROOT/'S6_SERIES_PUBLISH_III.tex'
canonical=canonical_path.read_text()
assert sha256(canonical.encode()).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
fresh=ROOT/'agents/continuation7_iii_corrected_initial/S6_SERIES_PUBLISH_III_02LU_fresh_derivation.md'
assert sha256(fresh.read_bytes()).hexdigest()=='c9439d8819da0dbf1ba285687e37a5ddce780e2afafeafb1a9f61297f71b29e1'
receiver_path=LANE/(PREFIX+'receiving.tex');receiver=receiver_path.read_text()
assert sha256(receiver.encode()).hexdigest()=='b004d43a7ff659502f5d0a5d9434fe1b485be4c82fb0a070b79fed582dd0e90d'
comparison_path=LANE/(PREFIX+'comparison.md');comparison=comparison_path.read_text()
assert sha256(comparison.encode()).hexdigest()=='371dae23b01926088a4826fb161a2553a7f005894d9bf20a2504860650b09657'
source_path=LANE/(PREFIX+'source_checks.md');source=source_path.read_text()
assert sha256(source.encode()).hexdigest()=='71f9ac44b262491542a7ed36974de4c5ee23fcf720a898afd6513b4b25cf3a20'

def environment(text,name):
    start=text.index('\\begin{'+name+'}')
    end=text.index('\\end{'+name+'}',start)+len('\\end{'+name+'}')
    return text[start:end]

old_statement=environment((LANE/(PREFIX+'released_statement.tex')).read_text(),'theorem')
old_proof=environment((LANE/(PREFIX+'released_proof.tex')).read_text(),'proof')
old_aux=(LANE/(PREFIX+'released_following_auxiliary.tex')).read_text()
assert len(old_statement.splitlines())==56 and len(old_proof.splitlines())==92 and len(old_aux.splitlines())==15
assert sha256(old_proof.encode()).hexdigest()=='ea81e990ecc1e2776b67c0489febe497ca1c0faf8f70cf732c76816a35e6b5bc'
assert sha256(old_aux.encode()).hexdigest()=='965b174a829a975402c49ae4f60c658d14733d57159b0cf0d4ba5a856a06ce53'
new_statement,new_proof=environment(receiver,'theorem'),environment(receiver,'proof')
blocks={'statement':old_statement,'proof':old_proof,'following_auxiliary':old_aux}
starts={}
for name,block in blocks.items():
    assert canonical.count(block)==1,name
    starts[name]=canonical.index(block)
assert starts['statement']<starts['proof']<starts['following_auxiliary']
old_all=old_statement+old_proof+old_aux
identities={}
for command in ('label','hypertarget','tag'):
    pattern=r'\\'+command+r'\{([^{}]+)\}'
    identities[command]=re.findall(pattern,receiver)
    assert sorted(re.findall(pattern,old_all))==sorted(identities[command]),command
assert receiver.count(r'\begin{theorem}')==receiver.count(r'\end{theorem}')==1
assert receiver.count(r'\begin{proof}')==receiver.count(r'\end{proof}')==1
stack=[]
for action,name in re.findall(r'\\(begin|end)\{([^{}]+)\}',receiver):
    if action=='begin':stack.append(name)
    else:
        assert stack and stack.pop()==name,(action,name)
assert not stack
assert r'\StatementRecord' not in receiver and r'\path{' not in receiver

replacements=[];guards=[]
for name,new in [('statement',new_statement),('proof',new_proof),('following_auxiliary','')]:
    old=blocks[name];start=canonical[:starts[name]].count('\n')+1
    end=start+len(old.splitlines())-1
    replacements.append(dict(statement_id=SID,old_text=old,new_text=new))
    guards.append(dict(statement_id=SID,kind=name,start_line=start,end_line=end,
                       old_sha256=sha256(old.encode()).hexdigest(),new_sha256=sha256(new.encode()).hexdigest()))
assert (guards[1]['start_line'],guards[1]['end_line'])==(21351,21442)
assert (guards[2]['start_line'],guards[2]['end_line'])==(21443,21457)

def location(block,text):
    assert text in blocks[block],(block,text)
    offset=starts[block]+blocks[block].index(text)
    return 'S6_SERIES_PUBLISH_III.tex:'+str(canonical[:offset].count('\n')+1)

def excerpt(needle,following_lines=8,text=new_proof):
    at=text.index(needle)
    return '\n'.join(text[at:].splitlines()[:following_lines])

items=old_proof.split('\\item ')[1:]
assert len(items)==6
items[-1]=items[-1].split('\\end{enumerate}')[0]
newloc=str(receiver_path.relative_to(ROOT));rows=[]
def defect(suffix,typ,block,old,new,reason,new_location=None):
    rows.append(dict(change_id='c7-III-02LU-'+suffix,type=typ,statement_id=SID,
        old_location=location(block,old),old_page='',new_location=new_location or newloc,
        new_page='pending final typeset page concordance',old_text=old,new_text=new,
        reason=reason,review_status='staged for root comparison; canonical application and final page review pending'))

header=next(line for line in old_statement.splitlines() if line.startswith(r'\StatementRecord'))
defect('machine-header','D10','statement',header,r'\textup{\scriptsize[02LU]}',
       'Remove the machine dependency/status header, preserving both permanent theorem identities and the small printed tag.')
defect('implementation-placement','D09','statement',r'\path{code/III/manifolds_corrected_initial.py}',
       'There is a finite exact integral algorithm for the fundamental\ngroup and every integral homology group with the following fillings:',
       'Replace the file claim in the theorem by the complete mathematical algorithm; preserve the pinned historical implementation scope in comparison/source checks.')
defect('relative-frame-scope','D26','statement',
       '\\item every original multiplicative cap with its\nuncorrected degree vector, as in \\ref{maps:src:D.2.46};',
       '\\item original multiplicative caps with the uncorrected line,\ndegree vector and relative frame of \\ref{maps:src:D.2.46};',
       'Make the original-cap input marking explicit. The actual historical guard accepts literal d=0 and rejects nonzero k mu even with unchanged degree. The proof gives I_D inverse E_D=q^(-k) and its inverse, hence the opposite meridian shears. This is an inherited scope ambiguity, not a refutation of the theorem.')
defect('scope-placement','D11','statement',
       'It does not identify original multiplicative caps\nwith their nonzero vertical corrections, nor the\nunresolved marked $h>1$ additive caps.',
       excerpt('Its original-cap choices specify the line and',8,new_statement),
       'State the original-cap line/frame and local-boundary-map input once, positively, with the exact whole-fibre map in the proof.')
defect('line-and-period-maps','D22','proof',items[0].strip(),
       excerpt('For the difference lines',16),
       'Supply the tensor/difference-line conjugation and reciprocal inverses, the transported rational L lattice maps, all-height integrality and literal ordered product. The original conclusion stands.')
defect('cap-scope-explanation','D02','proof',
       'No extension of the vertical divisor over a different\noriginal cap is being inferred from this fact.',
       excerpt('specified base weights thus agree under this map',2),
       'Express the exact punctured domain positively and use the original-cap maps only with their stated relative frame; no cap or fan identification is inferred from equal monodromy.')
defect('additive-cone-quotient','D22','proof',items[2].strip(),
       excerpt('The circle bundle over the component wedge',25),
       'Derive the full h=1 cone and all quotient/section maps, eta and partial-sum bounding chains, primitive gamma quotient, H3 freeness and H4 orbit count at the literal component action. The cited LT statement is proved in the exact needed scope without opening its original.')
defect('primitive-area-and-normals','D22','proof',
       'The fibre degree-two kernel is the actual\nprimitive area kernel \\eqref{maps:eq:D.IC7}, and both literal\nfixed-normal tori bound.',
       excerpt('The class $W$ with orbit coordinates',27),
       'Give the q-fold long-cover/logarithm inverse, q-area map and Bezout section, then the full scalar-corrected bounding chain for each literal normal. Freeness permits the stated transfer cancellation; no finite index is dropped.')
defect('normal-closure-inverse','D22','proof',items[3].strip(),
       excerpt('For completeness its vertical normal closure',37),
       'Prove termination via finite generation of the union; use the integral Cayley-Hamilton inverse for inverse stability; identify additive translates with conjugates and read fibre exponents for the inverse. HNF preserves the unsaturated subgroup and all remaining relators.')
defect('normal-closure-positive-scope','D02','proof',
       'No saturation or assumed abelian quotient replaces\nthis presentation.',
       excerpt('Before the cap and power relators',14),
       'State the conjugate/exponent isomorphism and its quotient in the full presentation directly, preserving all subsequent cap/power relations.')
defect('relative-section-and-ranks','D22','proof',items[4].strip(),
       excerpt('Here is an integral section and its inverse.',22),
       'Give the finite-first injection, actual component-disc Gamma columns, injective relation basis P, Mz=Pz-prime inverse, closing cycles and full integral splitting. Preserve D.CI1, all cap torsion, Euler sum and all seven homology groups.')
defect('complete-residue-count','D22','proof',items[5].strip(),
       excerpt('The component orders in the table are pairwise coprime',42),
       'Prove the exact45 count by raw component orders and CRT maps/inverses; give all pairs and the literal IC8 component permutation, divisor and eta chain. This supplies the numerical reason while keeping every all-parameter conclusion.')
defect('proof-organization','D14','proof',
       r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
       r'\smallskip\noindent\emph{Corrected lines and marked periods.}',
       'Use one proof ordered by line/period, local cone, marked fibre/normal maps, complete count, group/closure and integral gluing; retain all six original proof items.')
defect('implementation-proof-diction','D08','proof',
       'The implementation therefore adds these exact\nlocal columns to the common bar presentation.',
       excerpt('At the new original additive caps insert the full kernel,',10),
       'State the actual mathematical relation-map assembly rather than its software execution; implementation/source evidence is in the check records.')
defect('archived-comparison-scope','D09','following_auxiliary',
       'The independent replay script\n\\path{code/III/manifolds_corrected_initial_audit.py}\ncompares the full matrices against the earlier\n\\ref{maps:src:D.2.46} implementation and the sixteen independently\ncomputed \\ref{maps:src:D.2.50} examples.',
       excerpt('The audit source asserts full H2-matrix equality',19,comparison),
       'Preserve the exact historical assertion with its observed scope:42 full-matrix source assertions but only saved homology tables;16 full saved example matrices and formula checks, not a second imported LS matrix table. All273 full records and42 tables are checked by the new program under exact quotient/input maps.',
       str(comparison_path.relative_to(ROOT)))
defect('following-auxiliary-placement','D13','following_auxiliary',old_aux,'',
       'Delete only the released15-line following gap. Preserve every mathematical/count/coverage claim in the complete proof or comparison; retain all historical sources, actual outputs and precise new computation scope outside the paper body.')

now=datetime.now(timezone.utc).isoformat();events=[]
default_who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation seven graph LU'
def event(suffix,typ,outcome,source_file,phase,date=now,group=None,who=default_who):
    events.append(dict(statement_id=SID,date='2026-11-25',who=who,type=typ,outcome=outcome,
        event_id='publish:c7:III:02LU:'+suffix,phase=phase,source_file=source_file,source_row='1',
        source_event_type=typ,evidence_group=group or 'publish:c7:III:02LU:'+suffix,
        publish_input_file=str((LANE/(PREFIX+'CHECK_EVENTS.tsv')).relative_to(ROOT)),
        publish_input_row=str(len(events)+2),date_utc=date,where=str(comparison_path.relative_to(ROOT))))
event('fresh-complete','targeted proof check',
      'Root derived the complete 698-line theorem before LU original exposure from the clean LU/LT statements and attributed admitted/fresh inputs: actual roof/cone maps, h=1 quotient/inverse, q-cover primitive area and both normals, literal IC8 permutation, all-height period/unit transport and complete global group/homology assembly. Graph and KS peer scrutiny is attributed, not a second independent reproof; fresh hash c9439d... remains frozen.',
      str(fresh.relative_to(ROOT)),'before original exposure','2026-11-25T09:19:58+00:00','publish:c7:III:02LU:fresh',
      'GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation seven root LU')
event('fresh-cone-and-star-computations','computation or formal certificate',
      'Root new 254-line cone program ran once successfully: 29 exact cones, including 14 h=1 examples with full quotient/section/eta/error-preimage maps; all 33 stdout lines and actual empty stderr read. New 62-line star-order program ran once successfully: both full D5/D7 matrices, literal divisors, permutations/inverses/degrees/eta; all 5 stdout lines and empty stderr read. These finite checks accompany the universal proof; no failed fresh mathematical execution or historical target input.',
      'code/S6_SERIES_PUBLISH_c7_lu_additive_cone_v001.py','before original exposure','2026-11-25T09:19:58+00:00','publish:c7:III:02LU:fresh',
      'GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation seven root LU')
event('attributed-peer-review','used and rechecked in this run',
      'Read the complete root 698-line fresh derivation, clean LU 56-line and clean LT 112-line statements, full 319-line LS period support and bounded LS fresh Sections 2-5, full cone/star sources and all 33/5 stdout lines plus actual empty stderr. Checked h=1 cone quotient/inverse, q-area and normal maps, literal IC8 and global assembly. Attributed peer review only; no LU/LT/LS original exposure or independent-fresh credit.',
      'agents/continuation7_iii_corrected_initial/S6_SERIES_PUBLISH_III_02LU_graph_peer_review.md',
      'before original exposure','2026-11-25T09:19:28+00:00')
event('additional-residue-pairs','computation or formal certificate',
      'After release, a new 155-line program derives the exact 45 additional pairs from raw 21-profile periods, denominator/component maps, CRT inverse and physical component divisors. One successful execution; all 70 stdout lines including all 45 complete records and actual empty stderr read. No old LS count or historical target output used for this derivation; no failed version/rerun.',
      'code/S6_SERIES_PUBLISH_c7_lu_residue_pairs_v001.py','after original exposure','2026-11-25T09:28:18.282132+00:00')
event('complete-archived-comparison','computation or formal certificate',
      'New 290-line checker executed once successfully; all 321 stdout lines and actual empty stderr read. Checks 42 old homology tables and 273 full records, 1151 local maps, H2 integer relation lattices and H1 lattices under the explicit inverse peripheral map, all groups/closures/powers, complete 212-case multiset and 45 extras. Exact default ordered-kernel/first-success rule equality and attributed p=0 literal divisor proof are written. Both whole historical sources read; only their isolated original-multiplicative rejection conditional executed, no historical module rerun. No old stdout/runtime or manual whole-JSON reading claimed.',
      'code/S6_SERIES_PUBLISH_c7_lu_archived_comparison_v001.py','after original exposure')
event('whole-original-receiving','used and rechecked in this run',
      'Read complete 56-line original statement, all 92 proof lines/six items and exact 15-line following gap. Compare every mathematical and execution auxiliary; all conclusions/counts stand. Clarify D26 literal divisor/relative meridian scope with both frame maps, without a theorem refutation. One 652-line receiver preserves 2 labels/2 targets/1 equation tag and supplies all maps/inverses, full 45 count, unsaturated closure and relative split. All assembly sources/actual outputs retained and read. Three separate guards stage statement/proof/gap replacement; canonical/global/build/page gates remain with root.',
      str(comparison_path.relative_to(ROOT)),'after original exposure')

def serialize(headers,records):
    buffer=io.StringIO(newline='')
    writer=csv.DictWriter(buffer,fieldnames=headers,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(records)
    return buffer.getvalue()

contents={
 'replacements.tsv':serialize(['statement_id','old_text','new_text'],replacements),
 'guards.tsv':serialize(['statement_id','kind','start_line','end_line','old_sha256','new_sha256'],guards),
 'defects.tsv':serialize(['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'],rows),
 'CHECK_EVENTS.tsv':serialize(['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)
}
assert all(not (LANE/(PREFIX+name)).exists() for name in contents)
assert len(rows)==16 and len(events)==6
assert all(e['type']!='refuted' for e in events)
assert canonical_path.read_text()==canonical
assert sha256(fresh.read_bytes()).hexdigest()=='c9439d8819da0dbf1ba285687e37a5ddce780e2afafeafb1a9f61297f71b29e1'
print('START',now)
for name,text in contents.items():
    p=LANE/(PREFIX+name);p.write_text(text)
for guard in guards:print('GUARD',guard['kind'],guard['start_line'],guard['end_line'],guard['old_sha256'],guard['new_sha256'])
for row in rows:print('DEFECT',row['change_id'],row['type'],row['old_location'])
for check in events:print('EVENT',check['event_id'],check['type'],check['phase'])
print('IDENTITIES',identities)
print('COMPLETE',len(guards),'guards',len(rows),'defects',len(events),'events; canonical/global/frozen inputs unchanged.')
comparison_add='''
The record writer c7_lu_records_v001 stages three exact replacements,
sixteen defects and six narrowly typed event proposals. Its actual
source/stdout/separate stderr are retained. It checks the released
statement/proof/following-gap hashes, all permanent identities and
balanced environments, and restricts every defect location search to
its released block. The complete output and all rows are read before
root admission. The receiver remains held at its stated hash.
'''
source_add='''
Record assembly is code/S6_SERIES_PUBLISH_c7_lu_records_v001.py with its
actual .out and separate .err. It writes only this receiving lane:
three replacements/guards, sixteen defect rows and six check-event
proposals. All original locations are bounded by the released block;
canonical/frozen hashes and every label, target and equation tag are
checked. No admission helper, global table or census is written.
'''
comparison_path.write_text(comparison+comparison_add)
source_path.write_text(source+source_add)
for name in ('receiving.tex','comparison.md','source_checks.md','staged_bibliography.bib',*contents):
    p=LANE/(PREFIX+name)
    print('FILE',p.relative_to(ROOT),'LINES',len(p.read_text().splitlines()),'SHA256',sha256(p.read_bytes()).hexdigest())
print('END',datetime.now(timezone.utc).isoformat())
