#!/usr/bin/env python3
"""Prepare 02OG and its author correction; never mutate canonical inputs.

Only the individually released theorem/proof, its narrowly checked Uses gap,
and the exact supplied Fukae entry are decoded from source. Other bytes serve
whole-file fingerprint, exact membership guards and line counts. In particular
the adjacent KP proof is neither decoded nor printed.
"""
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
OWN=ROOT/'agents/continuation6_iii_carriers'
PREFIX='S6_SERIES_PUBLISH_III_02OG'
LABEL='mapsD:repair:collision-realization'
SOURCE=ROOT/'S6_SERIES_PUBLISH_III.tex'
source_bytes=SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
fresh=OWN/(PREFIX+'_fresh_derivation.md')
FRESH_HASH='02537b4f3eacc02f60307619d8b7ec1bed4c4c4603e9e742921cfef343b26db1'
assert hashlib.sha256(fresh.read_bytes()).hexdigest()==FRESH_HASH
fresh_program=ROOT/'code'/(PREFIX+'_fresh_arithmetic.py')
assert hashlib.sha256(fresh_program.read_bytes()).hexdigest()=='94bb53093548838ba172e551d09080fc575e23a0cd1053750743f372ef05c873'
statement=(OWN/(PREFIX+'_released_statement.tex')).read_text()
statement=statement[statement.index('\\begin{theorem}'):].strip()
proof=(OWN/(PREFIX+'_released_proof.tex')).read_text()
proof=proof[proof.index('\\begin{proof}'):].strip()
assert hashlib.sha256(proof.encode()).hexdigest()=='fda43df0045b13aedfbdf253059f8722e1cff2ba7c353b677d0c7e085e65a45a'
assert len(proof.splitlines())==450
sb,pb=statement.encode(),proof.encode()
assert source_bytes.count(sb)==source_bytes.count(pb)==1
start=source_bytes.index(sb)
pstart=source_bytes.index(pb,start+len(sb))
uses=source_bytes[start+len(sb):pstart].decode().strip()
expected_uses=r"""\noindent\textsf{Uses:} the finite-index modular-curve construction
\cite[Propositions~2.16, 2.21; Theorem~2.22; Proposition~4.3 and
Remark~4.4]{mapsMilne2017}; the minimal Weierstrass criterion
\cite[\S4.5, Table~1; \S8.2--8.4]{manSS10}; and the junction
identification \cite[\S3.1, (4), (8), (9); Lemmas~3.1--3.2, 4.1;
Corollaries~4.2--4.3]{manFukae02}."""
assert uses==expected_uses
end=pstart+len(pb)
old=source_bytes[start:end].decode()
first=source_bytes.count(b'\n',0,start)+1
last=source_bytes.count(b'\n',0,end)+1
assert source_bytes.count(b'\n',0,pstart)+1==29978
assert last==30427
receiver=OWN/(PREFIX+'_receiving.tex')
new=receiver.read_text().strip()
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{(tag-[^}]+)\}']:
    assert Counter(re.findall(pattern,old))==Counter(re.findall(pattern,new))
assert len(re.findall(r'\\hypertarget\{tag-',new))==7
assert '\\StatementRecord' not in new
assert new.count('\\begin{proof}')==new.count('\\end{proof}')==1
assert '\\begin{enumerate}' not in new

old_bib=r'''\bibitem[Fukae(2002)]{manFukae02}
Kazuki Fukae.

\newblock Monodromies of rational elliptic surfaces and extremal elliptic {K3}
  surfaces, 2002.

\newblock URL \url{https://arxiv.org/pdf/math/0205062}.
\newblock \emph{Verified}.'''
assert source_bytes.count(old_bib.encode())==1
bib_start=source_bytes.index(old_bib.encode())
bib_first=source_bytes.count(b'\n',0,bib_start)+1
bib_last=bib_first+len(old_bib.splitlines())-1
new_bib=old_bib.replace('Kazuki Fukae.','Mitsuaki Fukae.',1)
assert new_bib.replace('Mitsuaki Fukae.','Kazuki Fukae.',1)==old_bib
(OWN/(PREFIX+'_bibliography_receiving.tex')).write_text(new_bib+'\n')

def write(path,fields,rows):
    with path.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)

replacements=[dict(statement_id=LABEL,old_text=old,new_text=new,
    reason='Entire individually released theorem and own proof; one printed '
           'realization with exact models, covering and peripheral inverse maps, '
           'integral section quotient and normalized height. Every auxiliary '
           'assertion compared and all seven permanent tag/label pairs preserved. '
           'Independent NS/Poincare derivation retained in frozen check evidence. '
           'Adjacent KP and all other targets excluded.'),
    dict(statement_id='bib:manFukae02',old_text=old_bib,new_text=new_bib,
    reason='Primary arXiv title page names Mitsuaki Fukae. Exact author-only '
           'correction; key, title, URL, year and existing annotation preserved. '
           'The existing Verified annotation is left to the later provenance pass.')]
write(OWN/(PREFIX+'_replacements.tsv'),['statement_id','old_text','new_text','reason'],replacements[:1])
write(OWN/(PREFIX+'_bibliography_replacements.tsv'),['statement_id','old_text','new_text','reason'],replacements[1:])
defects=[]

def defect(suffix,kind,before,after,reason,bibliography=False):
    baseold=old_bib if bibliography else old
    basenew=new_bib if bibliography else new
    assert before in baseold
    assert not after or after in basenew
    loc=(bib_first,bib_last) if bibliography else (first,last)
    dest=OWN/(PREFIX+('_bibliography_receiving.tex' if bibliography else '_receiving.tex'))
    defects.append(dict(change_id='c6-III-02OG-'+suffix,type=kind,
        statement_id='bib:manFukae02' if bibliography else LABEL,
        old_location=f'S6_SERIES_PUBLISH_III.tex:{loc[0]}-{loc[1]}',old_page='',
        new_location=dest.relative_to(ROOT).as_posix(),new_page='',old_text=before,
        new_text=after,reason=reason,review_status='proposed; complete comparison '
        'done; root admission and source/unit/page gates pending'))

hstart=statement.index('\\StatementRecord')
header=statement[hstart:statement.index('\n\n',hstart)]
defect('header','D10',header,'','Remove the multi-line machine header while retaining every permanent identity.')
defect('uses','D10',uses,'','Remove the separate Uses navigation block; retain mathematical citations at their proof steps. The exact nine-line statement/proof gap was narrowly read and checked after the first guard stopped.')
defect('proof-hierarchy','D10',
    '\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=0pt,labelsep=.5em]',
    '', 'Replace generated nested proof enumeration by connected mathematical '
        'sections. The six original steps and every auxiliary assertion were fully compared.')
defect('title','D16',
    '\\begin{theorem}[Realization of the archived marked profiles]',
    '\\begin{theorem}[Two marked rational elliptic surfaces]',
    'Give a mathematical title while preserving 02OG and its statement label.')
defect('file-prose','D09',
    'These are the exact marked data in the\narchived collision-profile file, not merely data with the same fibre\ntypes or the same height.',
    'The matrices act in an oriented integral\nhomology basis, and the cocycle uses a compatible integral logarithm branch.',
    'State the exact mathematical marking in the theorem. Its complete comparison '
    'with the supplied profile tuples is in the check evidence, with no weakening '
    'to a fibre-type or height comparison.')
defect('coordinate-conversion','D20',
    'Thus the explicit model can be marked by the first coset table.',
    'The exact\ncoordinate maps from the first model and their inverses are',
    'Give the exact Mobius and fibre-unit maps between the two proved model '
    'coordinates, including both infinity charts, plus the exact covering and '
    'period marking maps. The original existence conclusion is verified; this '
    'records the receiving normalization precision, not a refuted assertion.')
defect('author','D18','Kazuki Fukae.','Mitsuaki Fukae.',
    'The primary title page of arXiv:math/0205062v1 names Mitsuaki Fukae. '
    'Both checker and root opened that primary page. Correct only the author; '
    'preserve the existing key and publication identity.',bibliography=True)
write(OWN/(PREFIX+'_defects.tsv'),list(defects[0]),defects)

with (ROOT/'CHECK_EVENTS.tsv').open() as stream:
    fields=next(csv.reader(stream,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
eid='publish:c6:III:02OG:targeted'
row=dict.fromkeys(fields,'')
row.update(statement_id=LABEL,date=now[:10],
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately '
        'exposed; sixth-continuation carriers checker',
    type='targeted proof check',event_id=eid,
    phase='fresh derivation followed by individual authorized full comparison',
    outcome='Complete 663-line fresh derivation saved/read 2026-11-24T14:13:11UTC '
        '(SHA256 '+FRESH_HASH+'); root full fresh/program/primary review preceded '
        'individual release 2026-11-24T14:20:43.061673+00:00. Read the full '
        'released statement, narrow Uses block and all 450 own proof lines, every auxiliary assertion, '
        'and complete receiving proof. Checked both literal cubics, all singular '
        'and infinite charts, exact cover/sheet/peripheral maps and inverses, '
        'SL lifts and raw matrices, full integral cocycle/section maps and '
        'inverse branches, torsion and primitive generators, Fukae circuit/null '
        'conversion, all height terms and whole symbolic pairing. New 323-line '
        'comparison program/output read completely; it is post-release work. '
        'Primary Fukae pp.3,6-13,21-22, Milne2017 pp.34-38,49 and Schuett-Shioda p.14 opened/read after '
        'release, with rendered equation/quotient checks. No mathematical '
        'conclusion refuted; primary author corrected Kazuki to Mitsuaki Fukae. '
        'All seven tag/label pairs preserved. Receiver prints one realization; '
        'independent NS/Poincare derivation remains frozen evidence. Failed '
        'transcription/structural-equality attempts retained with no verification '
        'credit. One proposed targeted event only for 02OG. KP unexposed. Optional '
        'isolated TeX attempt stopped before parsing because pdflatex.fmt was '
        'unavailable; no build/page credit. Root admission and canonical/unit/page '
        'gates remain pending.',
    source_file='S6_SERIES_PUBLISH_III.tex',source_row=str(first),
    source_event_type='targeted proof check',evidence_group=eid,
    publish_input_file=(OWN/(PREFIX+'_CHECK_EVENTS.tsv')).relative_to(ROOT).as_posix(),
    publish_input_row='2',date_utc=now,
    where='; '.join([*(str((OWN/(PREFIX+'_'+suffix)).relative_to(ROOT)) for suffix in
        ['fresh_derivation.md','fresh_word_clarification.md','comparison.md',
         'comparison_primary_reading.md','receiving.tex','replacements.tsv',
         'bibliography_receiving.tex','bibliography_replacements.tsv']),
        'code/'+PREFIX+'_comparison_arithmetic.py',
        'code/'+PREFIX+'_comparison_arithmetic.out']))
write(OWN/(PREFIX+'_CHECK_EVENTS.tsv'),fields,[row])
for suffix in ['receiving.tex','bibliography_receiving.tex','comparison.md',
               'comparison_primary_reading.md','replacements.tsv','bibliography_replacements.tsv','defects.tsv','CHECK_EVENTS.tsv']:
    assert b'\r' not in (OWN/(PREFIX+'_'+suffix)).read_bytes()
assert SOURCE.read_bytes()==source_bytes
assert hashlib.sha256(fresh.read_bytes()).hexdigest()==FRESH_HASH
assert hashlib.sha256(fresh_program.read_bytes()).hexdigest()=='94bb53093548838ba172e551d09080fc575e23a0cd1053750743f372ef05c873'
print('02OG whole theorem/proof guard:',first,'-',last,'; own proof 450 lines; receiver',len(new.splitlines()),'lines')
print('02OG guard SHA256 without terminal LF:',hashlib.sha256(old.encode()).hexdigest())
print('Exact Fukae author guard:',bib_first,'-',bib_last)
print('All seven permanent tag/label pairs preserved; one target guard and one separate bibliography guard;',len(defects),'defects; one proposed targeted event:',eid)
print('Canonical source/global tables not mutated by this program; frozen fresh work unchanged; LF outputs complete',now)
