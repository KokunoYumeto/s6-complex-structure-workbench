"""Admit terminal contractions/collars and consolidate the Hopf covering proof."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_12_'
old_fragment=(folder/(prefix+'input.tex')).read_text()
new_fragment=(folder/(prefix+'replacement.tex')).read_text()
before=SOURCE.read_text()
assert before.count(old_fragment)==1
after=before.replace(old_fragment,new_fragment,1)
root_changes=[]

def change(old,new,key,types,statement,reason):
    global after
    assert after.count(old)==1,(key,after.count(old))
    after=after.replace(old,new,1)
    for i,kind in enumerate(types,1):
        root_changes.append(dict(change_id=f'{key}-{i:02}',type=kind,
            statement_id=statement,old_location='Complete compared owner/application',
            old_page='checkpoint35 source; final concordance pending',
            new_location='Same mathematical application and earlier shared owner',
            new_page='integrated build pending',old_text=old,new_text=new,reason=reason,
            review_status='Complete original and receiving proofs read by assigned reviewer; root read complete receiving UN64/P325/P326/UN65 and complete UN43, UN38 and comparison. Exact receiving transfer rechecked; no independent or final-page credit.'))

anchor=r'\begin{proposition}[Hopf curves in the fibre boundary]\hypertarget{tag-01DH}{}\label{cdp:st:C.2.UN.38}'
lemma=r'''\begin{lemma}[Central primary coverings of Hopf surfaces]\hypertarget{tag-P327}{}\label{lem:II:central-primary-hopf-cover}
\StatementRecord{lem:II:central-primary-hopf-cover}{proved}{P327}{\cite[arXiv v1, \S2.3.1, p.~8]{AbashevaDeev2024AB}; \cite[arXiv v2, normal forms (1), p.~3; Theorem~2.1, p.~5]{Khaled2024Hopf}}
Let $H=W/\Gamma$ be a compact Hopf surface, with universal cover
$W=\C^2\setminus\{0\}$. There is a contraction $F\in\Gamma$
such that $\langle F\rangle$ is central and has finite index in
$\Gamma$. The quotient map
$\pi:P=W/\langle F\rangle\to H$ is a finite unramified primary
Hopf covering. Pullback identifies $\mathcal M(H)$ with a subfield
of $\mathcal M(P)$ over which $\mathcal M(P)$ is algebraic;
in particular $a(P)=a(H)$.
\end{lemma}
\begin{proof}
The finite primary-cover description in
\cite[arXiv v1, \S2.3.1, p.~8]{AbashevaDeev2024AB}
gives a finite unramified cover $P_0\to H$; use the identity
when $H$ is primary. Its covering injection
$\pi_1(P_0)\hookrightarrow\pi_1(H)=\Gamma$ identifies an infinite
cyclic subgroup of index equal to the covering degree.
The primary normal forms in
\cite[arXiv v2, normal forms (1), p.~3; Theorem~2.1, p.~5]{Khaled2024Hopf}
identify a generator with a contraction of $W$.
The intersection of the finitely many conjugates of this cyclic
subgroup is a normal subgroup of finite index in $\Gamma$ and
of finite index in the original cyclic subgroup. It is therefore
$\langle F\rangle$ for a positive power $F$ of that contraction.

Every deck transformation and its inverse extend holomorphically
across the origin by Hartogs. The extensions are inverse
automorphisms of $\C^2$, since their compositions are the identity
on $W$ and hence everywhere. Each fixes the origin: its restriction
maps $W$ bijectively to $W$, so the remaining point maps to itself.
The chain rule therefore makes
$\gamma\mapsto\log|\det(d\gamma)_0|$ a homomorphism
$\Gamma\to\R$. It is invariant under conjugation and is
nonzero on the contracting $F$. Conjugation on the normal
infinite cyclic group can send $F$ only to $F$ or $F^{-1}$;
the character excludes $F^{-1}$. Thus $F$ is central.
The action of $\Gamma/\langle F\rangle$ on
$P=W/\langle F\rangle$ is free: a fixed orbit would give a deck
transformation $F^{-n}\gamma$ fixing a point of $W$, so
$\gamma=F^n$. This yields the asserted finite unramified map.

For $g\in\mathcal M(P)$, take the elementary symmetric functions
of its values on the finitely many local sheets of $\pi$.
They are unchanged by the sheet permutations, so glue to
meromorphic functions on $H$. Their monic polynomial annihilates
$g$. Since the surjective map $\pi$ makes pullback injective,
this proves the stated algebraic field inclusion. Algebraic
extensions have the same transcendence degree over $\C$,
which is the asserted equality of algebraic dimensions.
\end{proof}

'''
change(anchor,lemma+anchor,'II-C3-ROOT-CENTRAL-HOPF-OWNER',
    ['D12','D14','D17','D20','D22'],'lem:II:central-primary-hopf-cover',
    'Transfer the general finite-index normal-core/determinant-character proof from UN43/P325 and the identical finite-sheet meromorphic-function proof from UN38 to one earlier owner. Prove Hartogs extension, the fixed origin, the exact covering group, and the algebraic pullback inclusion explicitly.')

start=r'\item Let $\pi:H\prime\to H$'
# The existing displayed prime is the ordinary TeX apostrophe.
start="\\item Let $\\pi:H'\\to H$ be a finite unramified primary cover,"
a=after.index(start)
b=after.index('In the diagonal case, a relation',a)
old=after[a:b]
new=r'''\item Apply \cref{lem:II:central-primary-hopf-cover} to this
Hopf normalization $H$ and write its finite unramified primary
cover as $\pi:H'\to H$. Put $B'=\pi^{-1}B$.
Its pullback of meromorphic-function fields is exactly the one
in that lemma, so $a(H')=a(H)=0$.

'''
change(old,new,'II-C3-ROOT-HOPF-BOUNDARY-COVER',
    ['D12','D20','D22'],'cdp:st:C.2.UN.38',
    'Apply the central-primary-cover owner to the identical H and its finite unramified covering. The same field pullback proves the needed algebraic dimension zero, and the boundary remains the exact inverse image pi^{-1}B.')

p=after.index(r'\label{cdp:st:C.2.UN.43}')
a=after.index(r'\item \par\medskip\noindent\textbf{The actual deck group.}',p)
b=after.index(r'\item',a+6)
old=after[a:b]
new=r'''\item Write $W=\C^2\setminus\{0\}$ and $H=W/\Gamma$.
Apply \cref{lem:II:central-primary-hopf-cover} to this given
surface. Its central contraction $F\in\Gamma$ gives
\[
                 P=W/\langle F\rangle\longrightarrow H.
\tag{C.SH.2}\hypertarget{tag-0119}{}\label{cdp:eq:C.SH.2}
\]
The pullback of meromorphic-function fields in that lemma
gives $a(P)=a(H)=0$ for this same covering.

'''
change(old,new,'II-C3-ROOT-SECONDARY-HOPF-COVER',
    ['D08','D12','D20','D22'],'cdp:st:C.2.UN.43',
    'The general central-cover argument now has one earlier proof. UN43 applies it to exactly its W,Gamma,H; C.SH.2 retains its label and target, and its algebraic-dimension-zero premise follows through the same field pullback.')

p=after.index(r'\label{lem:II:reduced-anticanonical-hopf}')
a=after.index(r'Write $H=W/\Gamma$.',p)
b=after.index('Use the complete primary normal-form list',a)
old=after[a:b]
new=r'''Write $H=W/\Gamma$ and apply
\cref{lem:II:central-primary-hopf-cover} to this Hopf surface.
It gives the central contraction $F$ and the finite unramified
primary cover $\pi:P=W/\langle F\rangle\to H$.
The divisor $D_P=\pi^{-1}D$ is reduced, with disjoint smooth
elliptic components. The unramified differential and the
pullback divisor give
$K_P(D_P)\simeq\pi^*(K_H(D))\simeq\OO_P$.

'''
change(old,new,'II-C3-ROOT-ANTICANONICAL-HOPF-COVER',
    ['D12','D20','D22'],'lem:II:reduced-anticanonical-hopf',
    'Apply the same general central-primary-cover owner to the entire compact-Hopf scope, without an algebraic-dimension restriction. The unramified differential and reduced divisor pullback identify K_P(D_P) with pi^*K_H(D).')

preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _, rows=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))
print('Root transfers',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',root_changes,'change_id'))

fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
old_unit='cdp:st:C.2.UN.64'
assert sum(r['paper']=='II' and r['unit_id']==old_unit for r in progress)==26
retained=[r for r in progress if not(r['paper']=='II' and r['unit_id']==old_unit)]
_, statuses=read_tsv(folder/(prefix+'unit_status.tsv'))
for row in statuses:
    unit=old_unit if row['unit']=='subsec:II:terminal-ruled-contractions' else row['unit']
    kind=row['criterion']
    status=row['status'];detail=row['reason']
    if unit=='subsec:II:anticanonical-hopf-boundaries' and kind=='D12':
        status='done';detail='P327 now owns the full general central-primary-cover proof, and P325 applies it to the same H,D with the unramified canonical and divisor maps. The rest of the boundary proof has one owner.'
    retained.append(dict(zip(fields,['II',unit,row['title'],
        'structure' if kind=='structure' else 'defect', '' if kind=='structure' else kind,
        status,now(),'CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR12-ADMISSION',detail])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in retained]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,retained)

_, sources=read_tsv(folder/(prefix+'sources.tsv'))
source_rows=[dict(source=r['source_id'],url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],
    own_word_summary=r['own_paraphrase'],
    use='Complete package12 comparison gives exact terminal contraction, central Hopf cover, canonical residue and classification applications.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',source_rows,'source'))
add_event('cdp:st:C.2.UN.64;cdp:st:C.2.UN.65;lem:II:reduced-anticanonical-hopf;lem:II:normal-product-collars;lem:II:central-primary-hopf-cover;cdp:st:C.2.UN.38;cdp:st:C.2.UN.43',
    'II-C3-ROOT-CONDUCTOR12-ADMISSION','used and rechecked in this run',
    'The conductor reviewer read every complete original and receiving UN64/UN65/P325/P326 proof, the whole original UN43 and UN46, and the exact supplied dependencies. Root read the complete receiving package and comparison, the complete UN43 and UN38, and all root receiving covering transfers. The original finite-index normal-core/determinant-character proof and finite-sheet field comparison now have one earlier owner P327, with precise maps at UN38/UN43/P325. The revised nonlinear-axis citation uses the exact Abasheva–Deev v1 section2.2.2 p4 statement; P248 is not assigned that unstated conclusion. UN64 retains the given ruling contraction, full normal extension with endpoint frames, all Euler changes and compact realizations. P325 retains the nonempty reduced elliptic-boundary and K_H(D)=O hypotheses, all eigenfunction cases and the axis-switch sign argument. P326 gives the exact smooth divisor-section product and attaching maps at the general no-triple-point scope. UN65 retains every residue, HRR, clutching, vertex-injection, degree-zero and volume-form calculation. Local classes are admitted; later UN46/UN57 collar transfers and final global order remain open. No independent or final-page credit.',
    'Complete terminal contraction, anticanonical Hopf and canonical-flat units; common central covering owner',source=__file__)
print('Package12 and P327 admitted; UN64 stable unit identity retained.')
