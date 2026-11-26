#!/usr/bin/env python3
"""Prepare one exact 02KQ guard, defect rows and a proposed check event.

Canonical source and global tables are read-only. Only the individually
released statement/proof and their three-LF gap are decoded from source;
all adjacent KR bytes remain undecoded. No arithmetic program is rerun.
"""
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT/'agents/continuation6_iii_carriers'
P = 'S6_SERIES_PUBLISH_III_02KQ'
LABEL = 'maps:src:D.2.16'
SOURCE = ROOT/'S6_SERIES_PUBLISH_III.tex'
source_bytes = SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
frozen = {
    OWN/(P+'_fresh_derivation.md'): 'a64ebff609bf84becaa9e9e1432952edec534ac2c3298ab582c84de082e30c6d',
    ROOT/'code'/(P+'_fresh_arithmetic.py'): 'db9f6d182d05ea019128399f4154a210d8de5bd28398756e2eb2f4ad8912a1e6',
    ROOT/'code'/(P+'_fresh_arithmetic.out'): '1c5d9fe5300e31c56c6c64692a853fbdfc7087c42994ad2f1f5dbd3c6ca1aafa',
    ROOT/'code'/(P+'_post_exposure.py'): '16a567bdfa9877fc21861657a8f536adc8d3d10d89ef51ae11d4923b68cdef47',
    ROOT/'code'/(P+'_post_exposure.out'): '6bfd1c09244c82a234e9360c9f25138f7782c1b3e4e05c74c48ab80ca8007368',
    OWN/(P+'_receiving.tex'): '158bf0a6b7ce56d97d3acb32066c68a3c628dabc30502a3fd7e7c9ab4dd4fc45',
    OWN/(P+'_comparison.md'): 'd101a077490653962c7401cb07f1dff2674f2cb8abbf167fdd36ff9cfd086273',
}
for path,digest in frozen.items():
    assert hashlib.sha256(path.read_bytes()).hexdigest() == digest,str(path)
assert (ROOT/'code'/(P+'_post_exposure.err')).stat().st_size == 0
assert (ROOT/'code'/(P+'_post_exposure.out')).read_text().rstrip().endswith(
    'All 32 full H1/H2 maps, inverse reductions, star powers, boundary groups and PL maps passed.')

statement = (OWN/(P+'_released_statement.tex')).read_text()
statement = statement[statement.index('\\begin{theorem}'):].strip()
proof = (OWN/(P+'_released_proof.tex')).read_text()
proof = proof[proof.index('\\begin{proof}'):].strip()
assert len(proof.splitlines()) == 255
assert hashlib.sha256(proof.encode()).hexdigest() == 'ced3c980ac493d4cea8c2f5c330d59bdf686b54156cf1ded88c001c79133525d'
assert len(re.findall(r'^\\item',proof,re.M)) == 12
sb,pb = statement.encode(),proof.encode()
assert source_bytes.count(sb) == source_bytes.count(pb) == 1
start,ps = source_bytes.index(sb),source_bytes.index(pb)
assert source_bytes[start+len(sb):ps] == b'\n\n\n'
end = ps+len(pb)
old = source_bytes[start:end].decode()
first = source_bytes.count(b'\n',0,start)+1
last = source_bytes.count(b'\n',0,end)+1
assert (first,last) == (10762,11074)
assert source_bytes.count(b'\n',0,ps)+1 == 10820
new = (OWN/(P+'_receiving.tex')).read_text().strip()
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
    assert Counter(re.findall(pattern,old)) == Counter(re.findall(pattern,new))
assert len(re.findall(r'\\hypertarget\{tag-',new)) == 11
assert new.count('\\begin{theorem}') == new.count('\\end{theorem}') == 1
assert new.count('\\begin{proof}') == new.count('\\end{proof}') == 1
assert '\\StatementRecord' not in new and '\\begin{enumerate}' not in new
assert '.py' not in new and '.json' not in new
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',new):
    kind,name=m.groups()
    if kind=='begin': stack.append(name)
    else: assert stack.pop()==name
assert not stack and new.count('\\[')==new.count('\\]')
balance=0
for m in re.finditer(r'(?<!\\)[{}]',new):
    balance += 1 if m.group()=='{' else -1
    assert balance>=0
assert balance==0 and len(re.findall(r'(?<!\\)\$',new))%2==0


def write(suffix,fields,rows):
    with (OWN/(P+'_'+suffix)).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)


write('replacements.tsv',['statement_id','old_text','new_text','reason'],[
    dict(statement_id=LABEL,old_text=old,new_text=new,
         reason='Entire individually released theorem and own 255-line proof, '
         'source 10762--11074; blank gap exactly three LF bytes. One receiving '
         'theorem/proof preserves every parameter, all groups, both oriented '
         'signs and all eleven permanent pairs. Explicit original-star maps, '
         'integer inverses, all-parameter log proof and direct framed '
         'reconstruction; all original auxiliary assertions compared. Adjacent '
         'KR and every other statement excluded; canonical application pending.')])

defects=[]


def defect(suffix,kind,before,after,reason):
    assert before in old,(suffix,'old')
    assert not after or after in new,(suffix,'new')
    oi=old.index(before)
    loc=first+old.count('\n',0,oi)
    defects.append(dict(change_id='c6-III-02KQ-'+suffix,type=kind,
        statement_id=LABEL,old_location=f'S6_SERIES_PUBLISH_III.tex:{loc}',
        old_page='',new_location=f'agents/continuation6_iii_carriers/{P}_receiving.tex',
        new_page='',old_text=before,new_text=after,reason=reason,
        review_status='proposed; full comparison complete; root admission and canonical/unit/page gates pending'))


header=next(line for line in statement.splitlines() if line.startswith('\\StatementRecord'))
defect('header','D10',header,'','Remove the machine status/use header; preserve the theorem identity and cite inputs at their mathematical steps.')
defect('hierarchy','D10',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
       '', 'Replace generated proof-step apparatus by connected mathematical paragraphs. All twelve original items are fully compared.')
defect('title-case','D23',r'\begin{theorem}[original odd-star fillings and all regular logs]',
       r'\begin{theorem}[Original odd-star fillings and all regular logs]',
       'Capitalize the existing mathematical title; its scope is unchanged.')
defect('group-notation','D20',
       r'G=\mathbb Z/t\oplus\mathbb Z/m\oplus\mathbb Z/(m|n|/t)',
       r'\mathcal G=\mathbb Z/t\oplus\mathbb Z/m\oplus\mathbb Z/(m|n|/t)',
       'Distinguish the torsion group from the section generator G. Identity on the displayed cyclic coordinates is the complete notation transport; use calligraphic T similarly.')
defect('retaining-process','D08',
       'Retain the original $I_j^*$ filling,',
       'Use the original $I_j^*$ filling,',
       'State the selected original filling as mathematical construction data.')
defect('primitive-model-process','D08',
       'The $I_3$ quotient is the actual primitive nodal\nmodel, by its unit component action.',
       'The component action at the original $I_3$ is a unit cycle.',
       'Remove workflow emphasis; the following displayed unimodular maps identify the primitive nodal model and inverse.')
defect('mapping-torus-map','D22',
       "Straightening this unit and the two section logarithms gives\na smooth family of contracting quotients with marked boundary.",
       "The angular orbit space has the\nliteral description",
       'Replace the shortened deformation step with the variable-roof diffeomorphism, inverse, cutoff translation and angular gauges. Q0=-q_tor identifies the original positive mapping torus exactly; no sign error in the original is asserted.')
defect('angular-winding','D02',
       'without an additional angular winding.',
       'The local linearization extends as a\nnonzero unit over the disc and has zero winding.',
       'State the positive winding calculation at the extending sweeps, with the integral gamma gauge and its inverse given once.')
defect('boundary-comparison','D02',
       "This argument retains the star fibre's integral component\ninformation. Replacing it by a product with an untwisted\nelliptic surface, or by an order-two good-reduction filling,\nwould give a different boundary problem.",
       "For the product marking $\\operatorname{diag}(-A^j,I_2)$ the relation\nSmith entries are $(1,4,0,0)$ and boundary $H_1$ is",
       'Replace the unspecific comparison by the exact boundary H1 torsion obstruction and the squared-monodromy intertwiner obstruction, both proved and newly computed.')
defect('constant-certificate','D09',
       'The exact constant integral certificates give',
       'Here is an explicit integral formula for the inverse used in this\ndisplay.',
       'Print the adjugate/Bezout formulas and component-cylinder maps needed to reproduce the computation, with their domains and inverses.')
defect('area-defence','D02',
       'without an unspecified fibre-area correction.',
       'The constant vertical\nform vanishes on every fixed-loop normal sweep, fixing this splitting.',
       'Give the positive fibre-area normalization by the period-triangle chain map.')
defect('canonical-descent','D22',
       'the canonical two-form on the minimal elliptic neighbourhood\nis nonvanishing and translation-invariant, and its wedge\nwith $dw/w$ descends through the contraction.',
       'In a holomorphic line frame\n$\\Omega=\\eta\\wedge dw/w$ is independent of that frame.',
       'Supply the exact canonical-line map, its frame independence and contraction descent, with SS Theorem 6.8 p.26 read after release. The original assertion is proved, not refuted.')
defect('cancellation-reference','D06',
       'Cancel the common $S^3\\times S^3$\nusing the full Zhubr invariants exactly as in \\ref{maps:src:D.2.14}.',
       'Combined with the preceding reconstruction\nthey give the oriented diffeomorphism',
       'The admitted receiving KO construction uses a direct framed map. Replace the reference to unspecified cancellation data by a complete direct reconstruction for the present free component ranks, including zero Euler class on the punctured quotient. No false abstract cancellation theorem or changed final diffeomorphism type is asserted.')
program_start=proof.index(r'\item The program ')
program_end=proof.index(r'\end{enumerate}',program_start)
defect('historical-run','D09',proof[program_start:program_end].strip(),'',
       'Remove historical program path and 1462/194 execution counts from the proof. Old scripts/outputs remain closed; no credit is assigned to those counts. The new all-parameter proof and separately recorded 32-case post-exposure computation support the result.')
write('defects.tsv',list(defects[0]),defects)

with (ROOT/'CHECK_EVENTS.tsv').open() as f:
    fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
eid='publish:c6:III:02KQ:targeted'
row=dict.fromkeys(fields,'')
row.update(statement_id=LABEL,date=now[:10],
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; sixth-continuation carriers checker',
    type='targeted proof check',event_id=eid,
    phase='complete fresh derivation followed by individual authorized full original and receiving comparison',
    outcome='Frozen 1049-line fresh proof, 385-line new program and 91-line output '
      'were written/read before original exposure; root full proof/program/maps/primary '
      'review completed 16:04:03 UTC before individual release 2026-11-24T16:04:46.930387+00:00. '
      'Then read the entire theorem, blank gap and all 255 original proof lines, '
      'all twelve items including every auxiliary assertion, and the complete 1112-line '
      'receiving proof. Checked both original odd-star fillings and exact component '
      'quotient, inverse-forward mapping torus, angular gauges, coefficient-four '
      'specialization and complete boundary/PL maps; all graph/fibre quotient maps '
      'and integer inverses; every free regular log and all-prime Smith calculation; '
      'both zero-n free cycle lifts and every integral degree; canonical-line descent, '
      'normal fan/Hopf framing, quotient Theta and inverse, zero Euler class on the '
      'whole punctured quotient, direct oriented suspension/neck maps, both n signs '
      'and even m, sphere case and every Y/B5 surgery/Euler/spin auxiliary. New 269-line '
      'post-exposure program and all 47 successful output lines read; 32 parameter/profile '
      'cases each check both full 19x19 and 14x15 maps and inverse reductions, plus '
      'star powers, boundary Smith data, PL maps and printed constants. SS Theorem 6.8 '
      'p.26 opened/read after release; printed proof sketch only. One receiver B2 '
      'block-order transcription was caught by its new check and corrected before '
      'the successful run; frozen fresh proof unchanged. Historical 1462/194 counts '
      'not verified or credited. Cancellation-method reference replaced by the '
      'constructed framed diffeomorphism; no final theorem conclusion refuted. '
      'All eleven permanent pairs and ten equation tags preserved. Structural '
      'guards pass; isolated TeX attempt stopped before parsing for absent '
      'pdflatex.fmt, so no build/page credit. A final TSV membership assertion '
      'decoded the complete canonical string inside Python but returned no '
      'manuscript passage; this was disclosed immediately and gives no proof '
      'reading or fresh credit. No KR proof content was inspected. One proposed '
      'targeted event only; root admission and canonical/unit/page gates pending.',
    source_file='S6_SERIES_PUBLISH_III.tex',source_row=str(first),
    source_event_type='targeted proof check',evidence_group=eid,
    publish_input_file=f'agents/continuation6_iii_carriers/{P}_CHECK_EVENTS.tsv',
    publish_input_row='2',date_utc=now,
    where='; '.join([*(f'agents/continuation6_iii_carriers/{P}_{s}' for s in
      ['fresh_derivation.md','fresh_work.md','primary_reading.md','fresh_maps.json',
       'released_statement.tex','released_proof.tex','post_exposure_derivation.md',
       'post_exposure_maps.json','comparison.md','receiving.tex','replacements.tsv','defects.tsv']),
      f'code/{P}_fresh_arithmetic.py',f'code/{P}_fresh_arithmetic.out',
      f'code/{P}_post_exposure.py',f'code/{P}_post_exposure.out']))
write('CHECK_EVENTS.tsv',fields,[row])
for suffix in ['receiving.tex','comparison.md','post_exposure_derivation.md',
               'replacements.tsv','defects.tsv','CHECK_EVENTS.tsv']:
    assert b'\r' not in (OWN/(P+'_'+suffix)).read_bytes()
assert SOURCE.read_bytes()==source_bytes
for path,digest in frozen.items():
    assert hashlib.sha256(path.read_bytes()).hexdigest()==digest
print('02KQ exact theorem/own-proof guard:',first,'-',last,'; proof 255 lines; receiver',len(new.splitlines()),'lines')
print('Whole guard SHA256 without terminal LF:',hashlib.sha256(old.encode()).hexdigest())
print('Eleven permanent pairs and ten explicit equation tags preserved; one replacement;',len(defects),'defects; one proposed event',eid)
print('No canonical/global mutation; frozen fresh work unchanged; LF outputs complete',now)
