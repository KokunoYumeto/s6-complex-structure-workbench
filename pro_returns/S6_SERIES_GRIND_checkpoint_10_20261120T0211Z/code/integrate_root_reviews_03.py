"""Apply the exact receiving changes reviewed before checkpoint 03.

Every replacement is guarded and recorded. Run once on the checkpoint-02
continuation; a repeated invocation stops rather than duplicating content.
"""
from pathlib import Path
import csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
csv.field_size_limit(10**9)
receipt=[]
def sha(t):return hashlib.sha256(t.encode()).hexdigest()
iv=ROOT/'parts/IV.body.linked.tex'
t=iv.read_text();original=t
for p in json.loads((ROOT/'audit_paper_i/iv_os45/K117_smooth_contraction_patches.json').read_text()):
    assert t.count(p['old'])==1,p['id']
    t=t.replace(p['old'],p['new'],1);receipt.append(p)

# A complete local notation adapter, with no change to any return index.
a=t.index('\\begin{theorem}\\label{night:P3F.35}')
b=t.index('\\end{proof}',a)+len('\\end{proof}')
old=t[a:b];new=old.replace('T(v,w)','T_+(v,w)').replace('T(v-w,w)','T_+(v-w,w)').replace('T(v+w,w)','T_+(v+w,w)')
anchor='for an integral basis \\((v,w)\\).'
adapter=r'''for an integral basis \((v,w)\).
The later return formulas use
\[
 T(u,v)=\{(0,u,v),(u,v,u+v)\}+\mathbb Z^2.
\]
The exact equality is $T_+(u,v)=T(u,-v)$: translating both
representative triangles on the right by $v$ gives the two triangles
on the left in reverse order. In particular,
$T_+(e_1+j e_2,e_2)=T(e_1+(j+1)e_2,e_2)$.
Every return index below refers to its displayed $T$ fan.'''
assert new.count(anchor)==1
new=new.replace(anchor,adapter)
t=t[:a]+new+t[b:]
receipt.append({'id':'IV-F35-fan-convention','old':old,'new':new,'reason':'Name the positive-diagonal convention and prove its exact lattice-translation adapter; preserve later return indices.'})

# Source comparison is a checked statement with a full numbered proof.
source=(ROOT/'audit_corrections/IV_source_morphisms.tex').read_text()
source=source[source.index('\\begin{remark}'):]
source=source.replace('Section~2 and Remark~8.5','Definition~2.3, p.~5, and Remark~8.5, p.~24')
source=source.replace('Proposition~2.8]{Engel2026}','Proposition~2.8, pp.~6--7]{Engel2026}')
source=source.replace('Engel\'s displayed equation','Engel\'s displayed equation on p.~3')
intro,body=source.split('For the original member\n',1)
intro=intro.replace('\\label{iv:source_transports}','\\label{iv:source_transports}\n\\StatementRecord{iv:source_transports}{proved}{}{\\cref{night:P3F.21}, \\cref{night:P3F.35}; \\cite[Definition~2.3, p.~5; Proposition~2.8, pp.~6--7; Remark~8.5, p.~24]{Engel2026}; \\cite[Proposition~9.24 and Remarks~9.25--9.26, pp.~82--83]{AC26}}')
intro=intro.replace('The following maps fix the scope of that credit.','The coordinate and point-line maps below identify the specified source\nand its regular quotient with the cited construction, and identify the\nreference toroidal triangles with the stated integral basis.')
body='For the original member\n'+body.replace('\\end{remark}','').strip()
for start in ['There is also an explicit relation','For the other rational elliptic sources','For the reference cusp']:
    assert body.count(start)==1
    body=body.replace(start,'\\item '+start)
newremark=intro+'\\end{remark}\n\\begin{proof}\n\\begin{enumerate}[label=\\arabic*.]\n\\item '+body+r'''

\item The exact source equation and inverse, the chronological Miller
telescopes, and the periodic fan adapter are checked by
\path{code/IV_source_transport_fresh.py}.
It uses symbolic rational substitution and translation orbits of actual
triangles; its output records 403 exact assertions, including 360
unimodular bases. The point-line quotient degrees are $1,4,9,36$.
\end{enumerate}
\end{proof}

'''
insert=t.index('\\begin{theorem}\\label{night:P3F.35}')
t=t[:insert]+newremark+t[insert:]
receipt.append({'id':'IV-source-transports','new':newremark,'reason':'Put the opened-source credit beside exact coordinate, line, scalar and lattice morphisms.'})
iv.write_text(t)

iii=ROOT/'parts/III.body.linked.tex';u=iii.read_text()
start=u.index('The exact implementation is\n\\path{code/III/manifolds_invariant_chern_caps.py}.')
end=u.index('\n\n\\begin{theorem}',start)
old=u[start:end]
new=r'''The exact computation is
\path{code/III_invariant_chern_cone_fresh.py}, with output
\path{code/outputs/III_invariant_chern_cone_fresh.json}.
It constructs an integral cycle basis by Bezout column operations and
computes Smith forms on the resulting relation lattice. It retains the
actual $\delta\gamma$ and multiplicity cycles, computes the order of
the former by a lattice-index ratio, and checks the primitive free
area image. The 6817 exact assertions cover 390 full chain models,
172 torsion models and 19 explicitly marked additive-component models.
The latter use their displayed component permutations, intersection
matrices and rank-two monodromy to check the component order and
logarithm denominator. These finite calculations corroborate the
all-integer elimination in \eqref{maps:eq:D.IC9}. The unresolved
$h>1$ mixed and fixed-normal torsion columns retain the scope stated
in the theorem.'''
u=u[:start]+new+u[end:];iii.write_text(u)
receipt.append({'id':'III-D251-current-certificate','old':old,'new':new,'reason':'Name the supplied newly written independent program and its exact verified scope; retain historical counts in the check record.'})

notation=ROOT/'S6_SERIES_GRIND_notation_sheet.md'
with notation.open('a') as f:f.write(r'''

## Exact source and fan adapters

Paper IV's `iv:source_transports` records the coordinate map
$\tau=4/(27t+4)$, $X=(9/2)\tau^2x$,
$Y=27\tau^3y/(2\sqrt2)$, its inverse and its unit changes at each
minimal singular-fibre germ. It maps $G=(0,t)$ to
$P=(0,\sqrt2\tau^2(1-\tau))$; the Hom linearization covers the
inverse translation, hence $-6G$ corresponds to $-6P$.

For $M_a=\mathcal O([aG]-[O])$ and the actual Miller divisor
$\operatorname{div}f_a=a[G]-[aG]-(a-1)[O]$, the map
$\mathcal F_a(p,v)=(p,f_a(p)v^a)$ obeys
$\mathcal F_a\mathcal B_1=\mathcal B_a^{\circ a}\mathcal F_a$.
The scalar normalization is $\lambda_a C_a=\lambda_1 C_1$.
The regular compact quotient degree is $a^2$, from the degree-$a$
point-line map and the index-$a$ suspension subgroup.

For the periodic fans, write
$T_+(u,v)=\{(0,u,u+v),(0,v,u+v)\}+\mathbb Z^2$ and
$T(u,v)=\{(0,u,v),(u,v,u+v)\}+\mathbb Z^2$.
Then $T_+(u,v)=T(u,-v)$: translate the two representatives on the
right by $v$ and interchange them. Thus
$T_+(e_1+j e_2,e_2)=T(e_1+(j+1)e_2,e_2)$.
P3F.35 uses $T_+$; the later return formulas retain their displayed
$T$ convention and their original indices. AC26's two triangles
are $T_+(e_1,-e_2)$ after translating its representatives by $e_2$;
the physical cocharacter $\delta=e_2$ equals $-w$ in that basis.
''')

inv=ROOT/'S6_SERIES_GRIND_inventory.csv'
with inv.open() as f:rows=list(csv.DictReader(f));fields=list(rows[0])
assert not any(r['label']=='iv:source_transports' for r in rows)
row={k:'' for k in fields}
row.update(paper='IV',label='iv:source_transports',source_run='S6_SERIES_GRIND',source_id='source-transports',kind='Remark',status='proved',main_or_supporting='supporting',source_inventory_row='series-source-transport:IV',source_paper='IV',credited_to='Engel2026 Definition2.3 p5, Proposition2.8 pp6–7 and Remark8.5 p24; AC26 Proposition9.24 and Remarks9.25–9.26 pp82–83',notes='Exact source, line, scalar and fan maps with full numbered derivation; fresh symbolic and lattice-orbit corroboration.',placement_state='printed in IV',writing_state='full numbered derivation',confidence_state='exact morphisms checked',completion_state='pending rendered-layout review',literature_searches='Original arXiv2609.38442 PDF reopened, equation p3, Definition2.3 p5, Proposition2.8 pp6–7, Remark8.5 p24; attached AC26 original source locators opened by corrections reviewer.')
rows.append(row)
with inv.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)

events=ROOT/'audit_root/CHECK_EVENTS.tsv'
with events.open() as f:erows=list(csv.DictReader(f,delimiter='\t'));efields=list(erows[0])
for label,event,typ,outcome in [
 ('iv:source_transports','root-IV-source-transports-proof','targeted proof check','Receiving comparison of the full coordinate inverse, minimal germ units, actual Miller divisor and chronological identity, quotient degrees, scalar transport and AC26 triangle adapter. Original Engel PDF equation p3, Definition2.3 p5, Proposition2.8 pp6–7 and Remark8.5 p24 opened and matched. No extension beyond the stated regular-locus comparison inferred.'),
 ('iv:source_transports','root-IV-source-transports-fresh','computation or formal certificate','Fresh IV_source_transport_fresh.py:403 exact assertions,360 unimodular bases; rational source substitution and inverse, four full chronological telescopes, triangle translation-orbit identities and smooth SU2 disc boundary/norm. PASS.'),
 ('night:P3F.35','root-IV-fan-convention','targeted proof check','Renamed the positive-diagonal convention T_+ and proved its literal translated-triangle equality T_+(u,v)=T(u,-v), including the vertical index relation. Later return indices unchanged. Fresh360basis equality check agrees.'),
 ('night:P3K.117','root-IV-smooth-SU2-receiving','targeted proof check','Applied three exact smooth-disc patches. First column (sin(pi r/2)e^{i phi},cos(pi r/2)); full SU2 matrix, exact old-radius substitution rho=sin(pi r/2), inverse, smooth centre and unchanged boundary diagonal retained.')]:
    assert not any(e['event_id']==event for e in erows)
    erows.append(dict(statement_id=label,date='2026-11-19',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort; S6_SERIES_GRIND root',type=typ,outcome=outcome,event_id=event,phase='S6_SERIES_GRIND'))
with events.open('w',newline='') as f:w=csv.DictWriter(f,efields,delimiter='\t');w.writeheader();w.writerows(erows)
receipt.append({'IV_before_sha256':sha(original),'IV_after_sha256':sha(t)})
(ROOT/'analysis/root_receiving_changes_03.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'changes':len(receipt)-1,'inventory_rows':len(rows),'root_events':len(erows)}))
