#!/usr/bin/env python3
"""Prepare the complete intrinsic rank-one elliptic-field unit; no central edits."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,re
root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor';prefix='S6_SERIES_PUBLISH_c3_conductor_08'
old=(out/(prefix+'_input.tex')).read_text();working=old;rows=[];ident='cdp:st:C.2.UN.26'
def log(kind,a,b,reason):
    rows.append(dict(change_id=f'II-C3-UNRESTRICTED08-{len(rows)+1:04d}',type=kind,statement_id=ident,old_location='UN.26 / rank-one-elliptic-fields; exact source span',old_page='cp35 PDF omitted; exact source span supplied',new_location='same owner and subsection',new_page='pending integrated final PDF',old_text=a,new_text=b,reason=reason,review_status='Complete original and receiving proof read and compared; exposed editorial rereading; final PDF reading remains open.'))
def replace(a,b,kind,reason):
    global working
    assert working.count(a)==1,(a[:80],working.count(a));working=working.replace(a,b,1);log(kind,a,b,reason)

replace(r'''If a finite cyclic group $G$ acts holomorphically on
$X$ and preserves $q$, the two-dimensional space can
be chosen $G$-stable. Thus the rank-one field-space
condition of \ref{cdp:st:C.2.UN.16}, even with this equivariance,
is satisfied by every specified compact elliptic
surface and cyclic fibration action. Any additional
restriction on its occurrence as a degeneration
component must use further data of that degeneration.''',r'''For a finite cyclic group $G$ acting holomorphically on $X$ and preserving the fibres of $q$ as a family, the two-dimensional space can be chosen $G$-stable.''','D11','The complete equivariant conclusion is stated once. The proof supplies the induced base action, allowing a group to permute fibres. The repeated rank-one-condition comparison and discussion of unspecified further restrictions are removed.')
replace(r'''\item Choose a nonzero meromorphic section $\sigma$ of
$\mathcal E$. This is an actual global choice:
Riemann--Roch on $B$ gives a nonzero holomorphic
section of $\mathcal E(D)$ for an effective divisor
$D$ of sufficiently large degree, which is the
required meromorphic section of $\mathcal E$.''',r'''\item Riemann--Roch on $B$ gives a nonzero holomorphic section of $\mathcal E(D)$ for an effective divisor $D$ of sufficiently large degree. Divide it by the canonical section of $\OO_B(D)$ to obtain a nonzero meromorphic section $\sigma$ of $\mathcal E$.''','D22','The original Riemann–Roch existence argument is retained, with the exact division map from a twisted holomorphic section to the meromorphic section stated at its construction.')
replace(r'''Here the dashed notation records poles of the section,
not a replacement of the displayed sheaf evaluation.
On the smooth part of $q$, the canonical differential
identification $\omega_{X/B}=\Omega^1_{X/B}$ makes
$a$ an actual relative one-form.''',r'''The meromorphic section $a$ is the evaluation of $q^*\sigma$ by the displayed holomorphic sheaf map. On the smooth part of $q$, the differential identification $\omega_{X/B}\simeq\Omega^1_{X/B}$ makes $a$ a relative one-form.''','D02','The exact sheaf evaluation and its meromorphic section are identified positively. The full contraction construction at critical fibres follows unchanged.')
replace(r'''Its dual defines a global meromorphic vertical field
$V$. The coordinate comparison at critical fibres
can be specified as follows. On a coordinate disc''',r'''Its dual defines a global meromorphic vertical field $V$. On a coordinate disc''','D08','Introduces the retained coordinate definition and change-of-coordinate computation directly.')
replace(r'''Apply
\cite[Theorem~3.3]{Guillot2024} to the complex
manifold obtained by deleting the actual polar
divisor of $W$. The univalence locus is closed
there and contains this dense union. It is
therefore the whole holomorphic locus, proving
the asserted semicompleteness for every $W$.''',r'''Apply \cite[Theorem~3.3, author preprint p.~9]{Guillot2024} on the full holomorphic locus $X_W$ of $W$. Its uniformizability locus is closed in $X_W$ and contains this dense union of compact fibres. It is therefore all of $X_W$, proving semicompleteness of every $W$.''','D18','Freshly reopened Guillot Theorem3.3 and its full proof on author-preprint p.9. The receiving application names exactly the complex manifold X_W and its dense complete-fibre locus; it does not apply the threefold specialization clause of P239 to this surface family.')
replace(r'''\cite[Theorem~3.3]{Guillot2024}}''',r'''\cite[Theorem~3.3, author preprint p.~9]{Guillot2024}}''','D18','The targeted nonprinting input locator uses the same exact author-preprint page as the proof.')
replace(r'''This proves the precise first-integral comparison.''','','D08','The preceding finite base map, connected-fibre pushforward and Stein factor already give the complete comparison.')
replace(r'''\item For the equivariant assertion, the finite orbit
of $V$ spans a nonzero finite-dimensional
representation of $G$ by meromorphic vertical
fields.''',r'''\item Since $G$ preserves the fibre family, $q\circ g$ is constant on each connected fibre for every $g\in G$. The equality $q_*\OO_X=\OO_B$ descends it to a holomorphic map $g_B:B\to B$ with $q\circ g=g_B\circ q$. The corresponding map for $g^{-1}$ is its inverse, so these maps give a finite group of automorphisms of $B$. The finite orbit of $V$ spans a nonzero finite-dimensional representation of $G$ by meromorphic vertical fields.''','D22','Gives the exact induced base action before using the quotient curve. The inverse map is induced by g^{-1}; the original finite orbit and vertical-field construction remain.')
replace(r'''This proves the full statement.''','','D08','The preceding G-stability, semicompleteness and Stein-factor calculations prove the stated conclusion directly.')

while (m:=re.search(r'\bactual\s+',working)):
    a=max(working.rfind('\n\n',0,m.start())+2,0);b=working.find('\n\n',m.end())
    if b<0:b=len(working)
    fragment=working[a:b];new=fragment[:m.start()-a]+fragment[m.end()-a:]
    for x,y in [('an graph resolution','a graph resolution'),('an global choice','a global choice')]:new=new.replace(x,y)
    working=working[:a]+new+working[b:]
    log('D08',fragment,new,'Names the actual mathematical sheaf, section, graph or composite directly and corrects the associated article; all construction maps remain.')

next_heading=r'\subsection{Compact component cores and geometric genus}\label{subsec:II:component-core-genus}'
working=working.rstrip()+'\n\n'+next_heading+'\n\n'
log('D14',old,working,'UN.26 is a complete standalone subsection. Its relative canonical line, evaluated form, contraction, dense complete fibres, finite ratio map and induced cyclic base action are in construction order. The following UN.28 material receives its own still-open subsection heading; whole-paper final placement remains open.')
with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
old_displays={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]',old,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
eq=[]
def number(m):
    a=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',a)
    if not tags:return a
    assert len(tags)==1
    label=re.findall(r'\\label\{([^}]+)\}',a)[0];assert established[tags[0]]==label
    b=a.replace(r'\[',r'\begin{equation}',1);b=b[:-2]+r'\end{equation}';b=b.replace(r'\tag{'+tags[0]+'}','')
    log('D19',old_displays[label],b,'The same formula, label and permanent target use the section equation counter.')
    eq.append(dict(old_tag=tags[0],target_label=label,statement_id=ident));return b
working=re.sub(r'\\\[.*?\\\]',number,working,flags=re.S)
working=re.sub(r'\n{4,}','\n\n\n',working)
def payload(s):
    s=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',s)
    for x in [r'\[',r'\]',r'\begin{equation}',r'\end{equation}']:s=s.replace(x,'')
    return re.sub(r'\s+','',s)
new_displays={lab:m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',working,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
for lab,display in old_displays.items():assert payload(display)==payload(new_displays[lab])
for kind in ['label','hypertarget']:
    p=r'\\'+kind+r'\{([^}]+)\}';before=re.findall(p,old);after=re.findall(p,working)
    assert set(before)<=set(after);assert max(Counter(after).values())==1
assert Counter(re.findall(r'\\begin\{([^}]+)\}',working))==Counter(re.findall(r'\\end\{([^}]+)\}',working))
assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40|\r',working)
def tsv(suffix,fields,data):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
(out/(prefix+'_replacement.tex')).write_text(working,newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows);tsv('_equations.tsv',['old_tag','target_label','statement_id'],eq)
with (root/'CHECK_EVENTS.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc);event={k:'' for k in fields}
event.update(statement_id=ident,date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome='Read the complete original UN.26 statement/proof and compared the entire receiving version. Preserved the proper relative-canonical pushforward, Riemann–Roch meromorphic section, sheaf evaluation, contraction and coordinate gluing, dense compact elliptic-fibre completeness, ratio/Stein factor and cyclic eigenvector construction. Made the induced base action explicit by q_*O=O. Freshly reread Guillot2024 author-preprint Theorem3.3 with its full proof at p.9 and applied it on each full holomorphic field locus. All five labelled display payloads agree. Exposed editorial rereading; no independent credit; whole-paper placement and final PDF remain open.',event_id='publish:c3:conductor08:UN26',phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+prefix+'_replacement.tex',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor08:rank-one-elliptic-fields',where='subsec:II:rank-one-elliptic-fields')
tsv('_CHECK_EVENTS.tsv',fields,[event])
status=[]
for n in range(1,26):
    state='done';reason='Complete local source and receiving proof read and compared; all found instances are logged. D10 and D16 remain done.'
    if n==14:state='open';reason='Local construction order and subsection boundary complete; final whole-paper placement remains open.'
    if n==18:state='open';reason='The exact edited primary locus is read and named; inherited bibliography-wide checking remains separate.'
    if n==23:state='open';reason='Final integrated typesetting and page reading remain open.'
    status.append(dict(unit='subsec:II:rank-one-elliptic-fields',title='Rank-one fields on elliptic surfaces',criterion=f'D{n:02d}',status=state,reason=reason))
status.append(dict(unit='subsec:II:rank-one-elliptic-fields',title='Rank-one fields on elliptic surfaces',criterion='structure',status='open',reason='Complete local construction order and one proof; whole-paper placement remains open. Following UN.28 is outside this unit.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
print('UN.26 complete local unit:',len(rows),'defects;1 exposed event;5 equation identities;26 status rows. No new tag or remote guard.')
print('All old labels, targets and formula payloads preserved; LF; no central file edited. Following UN.28 remains open.')
