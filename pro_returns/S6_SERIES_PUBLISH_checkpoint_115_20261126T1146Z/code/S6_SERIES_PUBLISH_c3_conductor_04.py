#!/usr/bin/env python3
"""Prepare the first unrestricted-Euler unit and its exact shared prerequisites."""
from pathlib import Path
from datetime import datetime, timezone
import csv,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_conductor'
PRE='S6_SERIES_PUBLISH_c3_conductor_04'
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()

def block(ident):
    p=source.index(r'\StatementRecord{'+ident+'}')
    starts=list(re.finditer(r'^\\begin\{(?:proposition|lemma|theorem|corollary|example|remark|cited|definition)\}',source[:p],re.M))
    a=starts[-1].start();b=source.index(r'\end{proof}',p)+len(r'\end{proof}')
    return source[a:b]

u1=block('cdp:st:C.2.UN.1');u2=block('cdp:st:C.2.UN.2');c2b=block('cdp:st:C2b');meridian=block('night:P4R.1')
start=source.index(r'\section{Unrestricted Euler topology and component covers}')
stop=source.index(r'\begin{proposition}[The same punctured torus family',start)
original=source[start:stop]
heading=original[:original.index(r'\begin{proposition}')].strip()
rows=[]

def log(kind,owner,old,new,reason,newloc=None):
    p=source.find(old);line=source[:p].count('\n')+1 if p>=0 else ''
    rows.append(dict(change_id=f'II-C3-EUL-{len(rows)+1:04d}',type=kind,statement_id=owner,
        old_location=f'pre-admission source line {line}; {owner}',old_page='cp35 PDF omitted; exact source span supplied',
        new_location=newloc or owner,new_page='pending integrated final PDF',old_text=old,new_text=new,reason=reason,
        review_status='Complete original and receiving proof read and compared; exposed editorial reading; final PDF page reading remains open.'))

tube=r'''\begin{lemma}[Compact analytic fibre tubes]\hypertarget{tag-P233}{}\label{lem:II:compact-analytic-tube}
\StatementRecord{lem:II:compact-analytic-tube}{proved}{P233}{\cite[p.~85, paragraph following Definition~1]{BobadillaKollar2012}; \cite[Proposition and Lemma, p.~154]{Ehresmann1952Connections}}
Let $f:X\to\Delta$ be a proper holomorphic map from a smooth complex threefold to a disc, smooth over $\Delta\setminus\{0\}$. Put $S=(f^{-1}(0))_{\rm red}$. For every sufficiently small radius $R>0$, the closed tube $U_R=f^{-1}(\overline\Delta_R)$ is a compact oriented smooth six-manifold with boundary, and the inclusion $S\hookrightarrow U_R$ is a homotopy equivalence. Its boundary is the mapping torus of the monodromy on a smooth fibre. For $0<\rho<R$, the radial collar over $\rho\le |t|\le R$ gives a deformation retraction $U_R\to U_\rho$ fixed on $U_\rho$.
\end{lemma}
\begin{proof}
Choose $R$ with $\overline\Delta_R\subset\Delta$. Properness gives compactness, and smoothness over $|t|=R$ makes that inverse image a smooth boundary. The complex orientation orients the tube and the smooth fibres. Ehresmann transport \cite[Proposition and Lemma, p.~154]{Ehresmann1952Connections} on the punctured disc identifies the boundary with the mapping torus. On the closed annulus $\rho\le|t|\le R$, lift the inward radial vector field using a smooth horizontal distribution. Properness makes its transport complete across the annulus. It identifies the annular inverse image with $f^{-1}(|t|=\rho)\times[\rho,R]$. Clamping the second coordinate to $\rho$, while fixing $U_\rho$, gives a homotopy $R_s:U_R\to U_R$ with $R_0=\operatorname{id}$ and $R_1(U_R)=U_\rho$.

Apply the neighbourhood-retraction statement of \cite[p.~85, paragraph following Definition~1]{BobadillaKollar2012} to the proper restriction over the open disc $\Delta_R$. It gives an open neighbourhood $0\in V\subset\Delta_R$ and a deformation retraction $H_W$ of $W=f^{-1}(V)$ onto $S$, with final map $r:W\to S$. Choose $\rho>0$ with $\overline\Delta_\rho\subset V$. Then $U_\rho\subset W\subset U_R$, and the composite
\[
 q=r\circ R_1:U_R\longrightarrow S
\]
is a homotopy inverse to the inclusion. Indeed, the concatenated homotopy is $R_{2s}$ for $0\le s\le\tfrac12$ and $H_W(R_1(-),2s-1)$ for $\tfrac12\le s\le1$. Its two pieces agree at the joining time; their images lie in $U_R$, and they fix $S$. Its endpoint is the inclusion composed with $q$, while $q|_S=\operatorname{id}$. The full fibre and its reduction have the same underlying space, so this comparison includes all multiplicities.
\end{proof}
'''
log('D17','lem:II:compact-analytic-tube',
    u1[u1.index(r'\item Take a sufficiently small closed coordinate disc'):u1.index(r'\item We give the parity calculation')]+meridian[meridian.index(r'\item The neighbourhood-retraction statement'):meridian.index(r'\item Put $U_i^*')],tube,
    'Opened the exact proper-analytic neighbourhood statement in Bobadilla–Kollár p.85 and the Ehresmann lift construction p.154. The explicit radial collar and concatenation transfer the open-neighbourhood statement to the closed round tube used by the parity and meridian proofs; no radial shape of V is assumed.',
    'Before night:P4R.1 in the earlier Euler section')

old1=u1[u1.index(r'\item Take a sufficiently small closed coordinate disc'):u1.index(r'\item We give the parity calculation')]
new1=r'''\item Choose a coordinate disc about $b$ containing no other critical value, and apply \cref{lem:II:compact-analytic-tube} to its proper restriction. For a small closed subdisc put $U=f^{-1}(\overline\Delta)$ and $M=\partial U$. The inclusion of $S=(Y_b)_{\rm red}$ is the homotopy equivalence constructed there, so $e(S)=\chi(U)$. The boundary is the mapping torus of the orientation-preserving monodromy of a real four-torus.

'''
assert old1 in u1;u1=u1.replace(old1,new1,1)
log('D12','cdp:st:C.2.UN.1',old1,new1,'The exact compact tube and mapping-torus input is now supplied once by P233 for this same restricted holomorphic map.')
old=r'\item We give the parity calculation entirely over $\Q$.'
new=r'\item Use homology with coefficients in $\Q$.'
assert old in u1;u1=u1.replace(old,new,1)
log('D08','cdp:st:C.2.UN.1',old,new,'States the coefficient field used in the calculation directly.')

def display(text,tag):
    return next(m.group() for m in re.finditer(r'\\\[.*?\\\]',text,re.S) if r'\tag{'+tag+'}' in m.group())
eq5=display(u2,'C.UN.5');eq6=display(u2,'C.UN.6')
curve=c2b[c2b.index(r'\item Let $C_2$'):c2b.index(r'\item Blow up $A\times')]
firstblow=c2b[c2b.index(r'\item Blow up $A\times'):c2b.index('Euler additivity gives')]
repeat=u2[u2.index(r'\item Blow up that section'):u2.index(r'\item Finally blow up')]
points=u2[u2.index(r'\item Finally blow up'):u2.index(r'\item Each curve blowup')]
repeat=repeat.replace('Blow up that section and repeat, always using','Blow up that section and repeat until there have been $k$ curve blowups, always using',1)
repeat=repeat.replace(r'as in \ref{cdp:st:C2b}',r'as in the first blowup chart',1)
merged=r'''\begin{proposition}[All even Euler numbers and projective blowup families]\hypertarget{tag-01CX}{}\label{cdp:st:C.2.UN.2}
\StatementRecord{cdp:st:C.2.UN.2}{proved}{01CX}{\cref{cdp:st:C.2.UN.1}}
\hypertarget{tag-01FH}{}\label{cdp:st:C2b}
\StatementRecord{cdp:st:C2b}{proved}{01FH}{}
The set of Euler numbers of reduced fibres among compact smooth threefolds fibred in complex two-tori is exactly $2\Z$. For every $k\ge1$ and $m\ge0$, there is a smooth projective threefold $Y_{k,m}\to\PP^1$ with connected fibres and smooth general fibre an abelian surface, whose only singular reduced fibre $S_{k,m}$ is normal crossing and satisfies \eqref{cdp:eq:C.UN.5}. It consists of an abelian surface blown up at $m$ distinct points, a chain of $k$ ruled surfaces over a genus-two curve attached to it, and $m$ projective-plane leaves attached to the abelian component. For $m=0$ the map on the abelian component is the identity. The central fibre is reduced. The total space $Y_{k,m}$ has torsion-free integral cohomology with Betti numbers \eqref{cdp:eq:C.UN.6}, and its structure-sheaf cohomology dimensions are $(1,2,1,0)$.

The choices $(k,m)=(1,0)$ and $(1,1)$ give Euler numbers $-2$ and zero, with respectively two and three components. The choices $m=k$ give the zero-Euler family with arbitrarily long chains of ruled components.
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''+curve+firstblow+r'''
The smooth horizontal surface $R=C_2\times\PP^1$ has strict transform isomorphic to itself because the centre is a Cartier divisor in $R$. In the exceptional bundle $\PP(K_{C_2}\oplus\OO_{C_2})$, it meets the section corresponding to the base-normal direction. This section is disjoint from the section meeting the strict abelian component. In the chart $u=t\upsilon$ the map is $f=t$ and the strict transform of $R$ is $\upsilon=0$, so the map is a submersion there.

'''+repeat+points+r'''
\item Each curve blowup increases the Euler number of the central support by $e(C_2)=-2$: its exceptional projective bundle has Euler number $2e(C_2)$ and the intersection with the old component has Euler number $e(C_2)$. Each point blowup increases it by two: the old surface gains one, the exceptional plane contributes three, and their intersection subtracts two. Starting from $e(A)=0$ gives
'''+eq5+r'''
For any integer $n$, choose $k\ge\max(1,-n)$ and $m=k+n$. This realizes $2n$; \cref{cdp:st:C.2.UN.1} gives the reverse inclusion. For $(k,m)=(1,0)$ the fibre is $A\cup\PP(K_{C_2}\oplus\OO_{C_2})$ with intersection $C_2$. For $(1,1)$ it has components $\operatorname{Bl}_p A$, $\PP(K_{C_2}\oplus\OO_{C_2})$ and $\PP^2$, with pairwise intersections $C_2$ and $\PP^1$ and no triple intersection. Taking $m=k$ gives every stated zero-Euler family.

\item The integral Betti numbers of $A\times\PP^1$ are $(1,4,7,8,7,4,1)$. Excision for the exceptional projective bundle and its hyperplane class identifies the new cohomology summands of a curve blowup with $H^{j-2}(C_2,\Z)$ in degree $j$. A point blowup adds one generator in degrees two and four. These are free summands, so the full cohomology remains torsion-free, and the $k$ curve and $m$ point blowups give
'''+eq6+r'''
In particular the two initial specializations have Betti numbers $(1,4,8,12,8,4,1)$ and $(1,4,9,12,9,4,1)$. The alternating sum is the value in \eqref{cdp:eq:C.UN.5}. Each blowup has structure-sheaf direct image $\OO$ and zero positive direct images, so Leray preserves the dimensions $(1,2,1,0)$ of $A\times\PP^1$.
\end{enumerate}
\end{proof}
'''
log('D12','cdp:st:C.2.UN.2',u2,merged,'Combined the general k-curve/m-point family with its duplicated C2b initial construction. Both complete original proofs were read; the embedded genus-two curve, both blowup charts, normal splitting, incidence chain, Euler formula, integral cohomology and structure-sheaf cohomology remain.', 'subsec:II:unrestricted-euler-parity')
log('D14','cdp:st:C2b',c2b,merged,'The exact maps identify C2b with k=1,m=0 and k=1,m=1 in the shared family. Both statement labels and permanent tags remain on one proposition; removal of the later C2b block resolves the former forward construction premise.', 'cdp:st:C.2.UN.2; alias cdp:st:C2b')
log('D08','cdp:st:C2b','For completeness the integral cohomology is torsion-free.',r'The total space $Y_{k,m}$ has torsion-free integral cohomology with Betti numbers \eqref{cdp:eq:C.UN.6}, and its structure-sheaf cohomology dimensions are $(1,2,1,0)$.','Promoted the full existing cohomological conclusion into its mathematical owner, identified its total-space domain, and retained its excision/projective-bundle reason.')
log('D21','cdp:st:C.2.UN.2','Its Euler characteristic is independently $2(m-k)$.','The alternating sum is the value in \\eqref{cdp:eq:C.UN.5}.','The proof records the exact consequence of the displayed Betti numbers, with no claim of an independent computation.')
log('D14','sec:II:06',heading,heading+'\n\n'+r'\subsection{Euler parity and projective blowup families}\label{subsec:II:unrestricted-euler-parity}', 'The first completed subsection groups parity with its exact projective realizations. Remaining section owners are not included in this unit proposal.')

# Read and compare the full receiving meridian proof, retaining its statement.
proof_start=meridian.index(r'\begin{proof}')
tail_start=meridian.index(r'\item The image of $\Lambda$')
tail=meridian[tail_start:]
meridian_new=meridian[:proof_start]+r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Let $U$ be the small closed tube of \cref{lem:II:compact-analytic-tube}, and put $U^*=U\setminus S$. The inclusion $S\hookrightarrow U$ and its homotopy inverse identify their fundamental groups. The proper smooth fibration $U^*\to\overline\Delta^*$ has fibre $T^4$. Its homotopy sequence, with $\pi_2(\overline\Delta^*)=0$, gives
\[
 \pi_1(U^*)=\Lambda\rtimes_A\langle t\rangle.
\]
The splitting chooses $t$ over the positive generator of the infinite cyclic base group; every element is uniquely $\lambda t^n$.

\item The inclusion $U^*\to U$ is surjective on fundamental groups. A loop can be perturbed off the real-codimension-two smooth stratum of $S$ and its higher-codimension singular strata. A null-homotopy disc avoids the singular strata and meets $S_{\rm reg}$ transversely in finitely many points. Deleting small discs around those intersections expresses the kernel as the normal closure of smooth-support meridians. The smooth locus of the irreducible $S$ is connected. A path in it and a trivialization of its complex normal line give an annulus of positive meridians, so all of them are conjugate.

At a smooth point of $S$, write $f=vz^m$ with $v$ a holomorphic unit. On a small coordinate neighbourhood, $z'=z\exp((\log v)/m)$ is a holomorphic normal coordinate and $f=(z')^m$. The positive circle $z'=a\exp(2\pi i\theta)$, $0\le\theta\le1$, maps to $a^m\exp(2\pi im\theta)$. Its image in the base group is $m$, so its class is $\mu=\lambda t^m$. The kernel calculation and the inclusion-induced identification $\pi_1(S)=\pi_1(U)$ give the stated normal-closure presentation, including the regular-fibre map.

'''+tail
log('D12','night:P4R.1',meridian,meridian_new,'The complete receiving statement/proof was read. P233 supplies the exact inclusion-induced group isomorphism via a genuine closed-tube homotopy inverse. The semidirect product, transversality kernel, meridian coordinate, normal subgroup, cyclic quotient and rational abelianization remain; only the repeated nested-neighbourhood comparison is removed.')

working=heading+'\n\n'+r'\subsection{Euler parity and projective blowup families}\label{subsec:II:unrestricted-euler-parity}'+'\n\n'+u1.strip()+'\n\n'+merged.strip()+'\n\n'
equations=[]
def number(m):
    old=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',old)
    if not tags:return old
    assert len(tags)==1
    lab=re.findall(r'\\label\{([^}]+)\}',old)[0]
    new=old.replace(r'\[',r'\begin{equation}',1);new=new[:-2]+r'\end{equation}';new=new.replace(r'\tag{'+tags[0]+'}','')
    owner='cdp:st:C.2.UN.1' if tags[0] in ['C.UN.1','C.UN.2','C.UN.3','C.UN.4'] else 'cdp:st:C.2.UN.2'
    equations.append(dict(old_tag=tags[0],target_label=lab,statement_id=owner));log('D19',owner,old,new,'The unchanged formula and stable labels/targets use the section equation counter.')
    return new
working=re.sub(r'\\\[.*?\\\]',number,working,flags=re.S)
with (ROOT/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
assert all(established[r['old_tag']]==r['target_label'] for r in equations)
for kind in ['label','hypertarget']:
    pat=r'\\'+kind+r'\{([^}]+)\}';old=set(re.findall(pat,original+c2b+meridian));new=re.findall(pat,working+tube+meridian_new)
    assert old<=set(new),(kind,old-set(new));assert len(new)==len(set(new)),(kind,'duplicate')
assert not re.search(r'night:P4R\.13|night:P4\.40',working+tube+meridian_new)

def tsv(suffix,fields,data):
    with (OUT/(PRE+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)

(OUT/(PRE+'_replacement.tex')).write_text(working,newline='\n')
(OUT/(PRE+'_tube_owner.tex')).write_text(tube,newline='\n')
(OUT/(PRE+'_remote_meridian_replacement.tex')).write_text(tube+'\n'+meridian_new+'\n',newline='\n')
remote=[dict(statement_id='cdp:st:C2b',old_text=c2b,new_text='',reason='Merged into UN.2 with both labels and tags and the full specializations preserved.'),
        dict(statement_id='night:P4R.1',old_text=meridian,new_text=tube+'\n'+meridian_new,reason='P233 precedes the meridian theorem and supplies its exact inclusion-induced homotopy comparison.'),
        dict(statement_id='sec:II:08',old_text=r'\subsection{The specialization fundamental group}',new_text=r'\subsection{The specialization fundamental group}\label{subsec:II:specialization-fundamental-group}',reason='A stable label for the complete revised subsection, preserving its title and boundary.')]
log('D14','sec:II:08',remote[-1]['old_text'],remote[-1]['new_text'],'The common compact-tube prerequisite precedes P4R.1 within its unchanged subsection boundary; a stable label identifies this complete revised unit.','subsec:II:specialization-fundamental-group')
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],remote)
with (ROOT/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:df=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',df,rows);tsv('_equations.tsv',['old_tag','target_label','statement_id'],equations)
with (ROOT/'CHECK_EVENTS.tsv').open() as f:ef=next(csv.reader(f,delimiter='\t'))
events=[];now=datetime.now(timezone.utc)
for ident in ['lem:II:compact-analytic-tube','night:P4R.1','cdp:st:C.2.UN.1','cdp:st:C.2.UN.2','cdp:st:C2b']:
    row={k:'' for k in ef};unit='subsec:II:specialization-fundamental-group' if ident in ['lem:II:compact-analytic-tube','night:P4R.1'] else 'subsec:II:unrestricted-euler-parity'
    row.update(statement_id=ident,date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',
        outcome='Read the complete original statement/proof and compared the complete receiving proof, including the exact compact-tube maps or shared blowup-family specializations. Bobadilla–Kollár p.85 and Ehresmann p.154 were opened before the new citation application. This is exposed editorial rereading, not an independent reproof or computation. Integrated PDF reading remains open.',
        event_id='publish:c3:conductor04:'+ident,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+PRE+'_replacement.tex',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor04:'+unit,where=unit)
    if ident=='lem:II:compact-analytic-tube':row['outcome']='Read the complete original tube paragraphs of UN.1 and P4R.1, the exact proper-analytic neighbourhood statement in Bobadilla–Kollár p.85, and the complete receiving P233 proof. The enclosing open R-disc, smaller closed rho-disc, radial collar and concatenation give an actual homotopy inverse fixed on S. Ehresmann p.154 was opened before its application. Exposed editorial rereading; no independent reproof or computation credit. Integrated PDF reading remains open.'
    if unit.endswith('fundamental-group'):row['source_file']='agents/continuation3_conductor/'+PRE+'_remote_meridian_replacement.tex'
    events.append(row)
tsv('_CHECK_EVENTS.tsv',ef,events)
status=[]
for unit,title in [('subsec:II:unrestricted-euler-parity','Euler parity and projective blowup families'),('subsec:II:specialization-fundamental-group','The specialization fundamental group')]:
    for n in range(1,26):
        state='done';reason='Complete original and receiving unit read; every identified occurrence is recorded. D10 and D16 remain done.'
        if n==18:state='open';reason='New exact source applications opened; inherited bibliography-wide checking remains separate.'
        if n==23:state='open';reason='Integrated typesetting and final PDF page reading remain open.'
        status.append(dict(unit=unit,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit=unit,title=title,criterion='structure',status='done',reason='P233 precedes all uses; C2b and UN.2 have one statement/proof with exact preserved aliases. Apply the accompanying remote removal and replacement together. The remaining sec06 owners are outside this completed unit.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
print('First unrestricted-Euler unit:',len(original),'->',len(working),'characters')
print('Defects',len(rows),'; exposed events',len(events),'; equation identities',len(equations),'; new tag P233')
print('Remote actions: remove the later C2b block; insert P233 and replace P4R.1 proof together; label its unchanged subsection heading.')
print('No central edits. D18 inherited bibliography and D23 final PDF reading remain open.')
