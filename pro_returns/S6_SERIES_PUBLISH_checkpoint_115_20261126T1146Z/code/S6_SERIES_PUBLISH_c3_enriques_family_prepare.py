"""Prepare the complete Enriques/elliptic occurrence consolidation and covers."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_occurrence_root'
prefix='S6_SERIES_PUBLISH_c3_enriques_family_'
current=SOURCE.read_text(); rows=[]; counter=0; guards=[]

def log(old,new,types,statement,reason):
    global counter
    for kind in types:
        counter+=1
        rows.append(dict(change_id=f'II-C3-ROOT-ENRIQUES-FAMILY-{counter:03}',type=kind,
            statement_id=statement,old_location='Complete UN18/25/27/30 occurrence proofs',
            old_page='checkpoint35 source; final concordance pending',
            new_location='Shared projective-root cover and Enriques/Kummer occurrence subsections',
            new_page='integrated final build pending',old_text=old,new_text=new,reason=reason,
            review_status='Root read complete original statements and proofs; complete receiving reading and exact application comparison recorded at admission.'))

# PE11--13 move once to their general curve-domain owner.
cover_old=(folder/'S6_SERIES_PUBLISH_P347_UN18_old.tex').read_text()
cover_new=r'''\item Apply \cref{lem:II:torsion-root-product-cover} with
$B=E$, $D_+=[p_+]$, $D_-=[p_-]$, the same $m,q$, and
$L_B=\OO_E(p_+-p_-)$. This line is torsion because the
difference $p_+-p_-$ is a torsion point of $E$.
Choose the lemma's torsion $m$th root $N$ with its isomorphism
$N^{\otimes m}\simeq L_B$. Its cyclic curve is
\eqref{cdp:eq:C.PE.11}; its genus formula gives $g(C)=m$.
The same cover $C'\to C$, frame $n$, and meromorphic
coordinate $y=y_0n$ give exactly \eqref{cdp:eq:C.PE.12}.
The identity on $(\ell,a)$ intertwines its positive chart
with the restriction of $\rho$, and the reciprocal
$(\ell^{-1},a^{-1})$ does so at $p_-$. Thus the target
is this $P_m$, and the lemma gives its finite unramified
product cover and projectivity. Both branch Jacobians
are those of \eqref{cdp:eq:C.PE.13} with these same frames.

'''
assert current.count(cover_old)==1
guards.append(dict(key='UN18-shared-product-cover',old=cover_old,new=cover_new))
owner=(folder/'S6_SERIES_PUBLISH_P347.tex').read_text()
anchor=r'\subsection{Paired roots and projective elliptic components}\label{subsec:II:paired-root-occurrence}'
assert current.count(anchor)==1
guards.append(dict(key='P347-before-all-cover-consumers',old=anchor,new=owner+anchor))
log(cover_old,owner+cover_new,['D12','D14','D17','D18','D20','D22'],
    'lem:II:torsion-root-product-cover;cdp:st:C.2.UN.18',
    'One complete curve-domain covering proof retains the cyclic equation, torsion trivialization, product map, both exact Jacobians and all original labels. The UN18 inputs and target are identified explicitly. Projectivity uses the opened finite-fibre case of Coltoiu--Gasitoi--Joita Theorem2 p241 on this exact map.')

# The Enriques construction is the r=2 member of the complete family.
a=current.index(r'\subsection{Enriques and further elliptic components}\label{subsec:II:enriques-elliptic-occurrence}')
b=current.index(r'\begin{proposition}[The fixed Kummer punctured family',a)
family_old=current[a:b]
family_new=(folder/'S6_SERIES_PUBLISH_enriques_family_merged.tex').read_text()
guards.append(dict(key='UN25-UN27-one-statement-one-proof',old=family_old,new=family_new))
log(family_old,family_new,['D12','D14'], 'cdp:st:C.2.UN.25;cdp:st:C.2.UN.27',
    'Merge the complete statements and proofs into the r>=2 construction, retaining both permanent statement identities. Every r=2 specialization is the stated identity on the curves, covers, group actions, incidence components and edge maps. The compact base, all full multiplicities, parity cases, canonical forms, floor pushforward, cohomology and unchanged essential component survive. No mathematical conclusion is dropped.')

def excerpt(s,start,end):
    x=s.index(start);return s[x:s.index(end,x)]

old25=family_old[:family_old.index(r'\begin{proposition}[A fixed punctured torus family')]
old27=family_old[len(old25):]
transfer_specs=[
 (r'\item Blow up the four points',r'\item We identify the component',
  r'\item Blow up the $2r$ points',r'\item The restriction of $L_r$',
  ['D08','D12','D20','D22'],'P339 is applied to the exact paired exceptional divisors and m=2. The dualization and its conjugation of the deck generator remain explicit; punctured identities use the blowdown V to V0.'),
 (r'\item We identify the component',r'\item On $C$,',
  r'\item The restriction of $L_r$',r'\item At infinity, $Y/z^r',
  ['D08','D12','D20','D22'],'The cyclic cover and its product map have the full earlier owner P347. General r specializes at r=2 by the identity on z,Y,u, including the parity sign and all old covering labels.'),
 (r'\item On $C$,',r'\item It remains to realize',
  r'For $r=2$, both $j$',r'\item We realize this resolution',
  ['D08','D12','D18','D20','D22'],'Keep one Enriques identification via the explicit free involution of the K3 resolution; choose origins identifying k with inversion and apply the exact cyclic quotient row. The alternative duplicate canonical-character proof is removed; the general canonical calculation remains.'),
 (r'\item It remains to realize',r'\item The full incidence calculation',
  r'\item We realize this resolution',r'\item The complete incidence table',
  ['D02','D08','D12','D20'],'Retain the complete ambient A1 charts, transverse volumes, normal bundle and multiplicities for both parities. Rename only the local resolution coordinate r to r0 to distinguish it from the family integer.'),
 (r'\item The full incidence calculation',r'\item For the compact construction',
  r'\item The complete incidence table',r'\item At infinity, the base involution',
  ['D08','D12','D20'],'One incidence table contains every double and triple stratum. EN16 and ENS1 are aliases of this same table with the explicit r=2 identity; the same monomial chart proves SNC and the same Euler terms remain.'),
 (r'\par\medskip\noindent\textbf{The reduced support and its exact cohomology.}',r'\end{enumerate}',
  r'\item On $M_r$ the full fibre divisors',r'\item The positive pluricanonical sections',
  ['D08','D09','D12','D20','D22'],'Consolidate the complete cohomology proofs at arbitrary r. The affine-D4 relation, half-fibre independence, all alternating maps and ranks, exact Hopf restrictions, full-support Gysin maps and derived Cartier comparison are preserved. The r=2 specialization identifies every original edge map; program paths already stand in appendix160.'),
]
for os,oe,ns,ne,kinds,reason in transfer_specs:
    log(excerpt(old25,os,oe),excerpt(family_new,ns,ne),kinds,
        'cdp:st:C.2.UN.25;cdp:st:C.2.UN.27',reason)
for match in re.finditer(r'\\tag\{([^}]+)\}',family_old):
    log(match.group(0),'Section equation counter at the unchanged label/target.',
        ['D04','D19'],'cdp:st:C.2.UN.25;cdp:st:C.2.UN.27',
        'The corresponding formula is retained or explicitly identified by r=2 specialization at its single general owner. Each permanent label and target occurs exactly once.')
for match in re.finditer(r'\((C\.EN(?:\.[A-Z])?\.[0-9]+|C\.EN\.[A-Z][0-9]+|C\.KM\.S[0-9]+|C\.PE\.[0-9]+)\)',family_old):
    log(match.group(0),r'\eqref{cdp:eq:'+match.group(1)+'}',
        ['D04','D19'],'cdp:st:C.2.UN.25;cdp:st:C.2.UN.27',
        'Replace the printed inherited reference by its unchanged hyperlinked equation label in the receiving proof or consolidate it at that equation owner.')
for line in family_old.splitlines():
    if any(x in line for x in [r'\texttt{code/',r'\path{code/',r'\texttt{.out}']):
        log(line,'The mathematical input, exact method and output remain in the proof; the program is already in appendix160.',
            ['D09'],'cdp:st:C.2.UN.25;cdp:st:C.2.UN.27',
            'Remove the proof-body path/output bookkeeping without changing the already admitted program table.')
log('These checks are saved in',
    'The Euclidean algorithm applied to the displayed discriminant and its derivative gives gcd one.',
    ['D08','D09'],'cdp:st:C.2.UN.25','The computation is stated by its input, exact algorithm and result; the appendix owns the path.')

# Complete Kummer-family receiver.
a=current.index(r'\begin{proposition}[The fixed Kummer punctured family')
b=current.index(r'\begin{proposition}[Every fixed-modulus elliptic quasi-bundle',a)
kum_old=current[a:b]; text=kum_old

def edit(old,new,kinds,reason):
    global text
    assert text.count(old)==1,(old[:100],text.count(old))
    text=text.replace(old,new,1)
    log(old,new,kinds,'cdp:st:C.2.UN.30',reason)

a=text.index(r'\item Perform the signed order-two root construction')
b=text.index(r'\item Away from the root curves',a)
edit(text[a:b],r'''\item Apply \cref{lem:II:signed-root-fibration} to the same
$V,L,\sigma$ with $D_+=\sum R_j$, $D_-=\sum R_{-j}$,
$m=2$ and $q=e^{-2\pi}$. The identity in the positive
coordinates $(\ell,a)$ and the reciprocal change
$(\ell',a')=(\ell^{-1},a^{-1})$ identify its two charts
with the restrictions along these signed curves. Its deck
map is $(\ell,a)\mapsto(q^2\ell,q^{-1}a)$, and its
proper quotient is the smooth compact $\widetilde Y\to V$.
Dualization over $h$ sends the meromorphic pair to
$(\ell^{-1},a^{-1})$ and conjugates that deck map to its
inverse. Thus it defines the involution on this same quotient.

''',['D08','D12','D20','D22'],
    'Apply P339 at its full disjoint-divisor domain, with the exact line, section, sign convention and deck action, retaining the lifted involution.')
a=text.index(r'\item Let $B_r$ be the component above the')
b=text.index(r'\item The involution on $B_r$ covers inversion',a)
cover_kum=r'''\item Let $B_r$ be the component above the strict central
elliptic curve $E_0$. It has $2r$ smooth double fibres at
$p_j,-p_j$, and its restricted line is
\[
 L|_{E_0}\simeq\OO_{E_0}\left(\sum_{j=1}^r[p_j]-[-p_j]\right).
\tag{C.ET.7}\hypertarget{tag-00JE}{}\label{cdp:eq:C.ET.7}
\]
The group sum of this divisor is $2\sum p_j$, a torsion
point, so this line is torsion. Apply
\cref{lem:II:torsion-root-product-cover} with $B=E_0$,
$D_+=\sum[p_j]$, $D_-=\sum[-p_j]$, $m=2$, the same
$q$, and this restricted section. Denote its torsion
square root by $\mathcal N$ (the line $N$ in that lemma);
its connected normalized curve $C$ has
$g(C)=r+1$. Its finite unramified cover $C'\to C$ has
the frame $n$ of $\mathcal N$ and coordinate $y=y_0n$, giving
\[
 C'\times E\longrightarrow B_r,\qquad
 (z,[u])\longmapsto[\ell=u^2n^2,a=y_0/u].
\tag{C.ET.8}\hypertarget{tag-00JF}{}\label{cdp:eq:C.ET.8}
\]
This is the same map \eqref{cdp:eq:C.PE.12} on the same
root charts. Its two Jacobians are $2$ and $-2u^{-2}$,
the $m=2$ instances of \eqref{cdp:eq:C.PE.13}.
The lemma proves that this map is finite unramified
everywhere and that $B_r$ is projective.

'''
edit(text[a:b],cover_kum,['D08','D12','D20','D22'],
    'One general product-cover proof owns the root curve, torsion frame and both branch Jacobians. The exact elliptic divisor class and all inputs are checked before the application; ET7/ET8 retain their maps.')
edit('proved by the actual Hopf\nelliptic Leray map in \\ref{cdp:st:C.2.UN.25}.',
    'given by \\cref{lem:II:hopf-curve-restriction} for these same primary scalar Hopf surfaces and elliptic axis inclusions. The restriction identifies the additive deck class with the nonzero class on the axis.',
    ['D08','D12','D20'],'Use the complete Hopf restriction owner at the exact same embeddings.')
edit('essential by \\ref{cdp:st:C.2.UN.14}, and',
    'essential by \\cref{lem:II:nonuniruled-divisors} applied to these compact divisors in the smooth proper fillings, and',
    ['D12','D20','D22'],'Identify the common divisor correspondence and its same-surface/filling hypotheses.')
edit('Its quotient\nhas sixteen $A_1$ singularities; let\n$M_r$ be their minimal resolution.',
    'Its quotient has sixteen $A_1$ singularities. Apply \\cite[Theorem~2, p.~241]{ColtoiuGasitoiJoita2012} to the finite map from the projective $B_r$ to this normal quotient; every fibre has dimension zero. The quotient is projective, and its blowup resolving the sixteen $A_1$ points is the projective surface $M_r$.',
    ['D17','D18','D22'],'Give the exact known projectivity theorem on the finite quotient, and identify the ordinary algebraic resolution used.')
for old,new in [
 ('Under that actual\nidentification','Under that identification'),
 ('the actual product formula','the product formula'),
 ('the actual direct-image\nequality','the direct-image equality'),
 ('The actual invariant quadratic\nblowup charts','The invariant quadratic\nblowup charts'),
 ('For completeness the support\ncohomology','The support cohomology'),
 ('the\nactual Cartier pullback','the Cartier pullback'),
 ('its actual canonical','its canonical'),
 ('same\nspecified punctured family','same punctured family')]:
    if old in text:edit(old,new,['D08'],'State the unchanged coordinate, divisor or cohomology comparison directly.')
edit('\\item We now specify the ambient resolution.',
    '\\item The ambient quotient has the following resolution.',
    ['D08'],'Introduce the resolution by its mathematical object.')
edit('all beginning at fresh\nsmooth points of its plane',
    'all beginning at distinct\nsmooth points of its plane',
    ['D08'],'State the disjoint choice of centres mathematically.')
record=next(line for line in text.splitlines() if line.startswith('\\StatementRecord{cdp:st:C.2.UN.30}'))
edit(record,record.replace(r'\SeriesRef{cdp:st:C.2.UN.18}',
    r'\cref{lem:II:signed-root-fibration,lem:II:torsion-root-product-cover,lem:II:hopf-curve-restriction,lem:II:nonuniruled-divisors}'),
    ['D12','D18'],'The hidden prerequisite record names the exact shared owners used by the receiving proof.')
for match in list(re.finditer(r'\((C\.[A-Z]+\.[A-Z]?[0-9]+)\)',text)):
    old=match.group(0)
    if text.count(old)==1:
        edit(old,r'\eqref{cdp:eq:'+match.group(1)+'}',['D04','D19'],'Resolve the inherited literal equation reference through its unchanged label.')
for match in list(re.finditer(r'\\\[(.*?)\\\]',text,re.S)):
    block=match.group(0)
    if re.search(r'\\tag\{[^}]+\}',block):
        edit(block,'\\begin{equation}'+re.sub(r'\\tag\{[^}]+\}','',match.group(1))+'\\end{equation}',
            ['D04','D19'],'Number the unchanged formula by section and retain every label and permanent target.')
text=r'\subsection{Elliptic components in the Kummer family}\label{subsec:II:kummer-elliptic-occurrence}'+'\n\n'+text
text+=r'\subsection{Elliptic torsors and Hopf components}\label{subsec:II:enriques-elliptic-occurrence}'+'\n\n'
(folder/(prefix+'UN30_receiving.tex')).write_text(text,newline='\n')
guards.append(dict(key='UN30-complete-receiver',old=kum_old,new=text))

# Exact opened primary source, sorted between Claude and Cox.
anchor=r'\bibitem[Cox et~al.(2011)Cox, Little, and Schenck]{CoxLittleSchenck2011}'
bib=r'''\bibitem[Col\c{t}oiu et~al.(2012)Col\c{t}oiu, Ga\c{s}i\c{t}oi, and Joi\c{t}a]{ColtoiuGasitoiJoita2012}
Mihnea Col\c{t}oiu, Natalia Ga\c{s}i\c{t}oi, and Cezar Joi\c{t}a.
\newblock On the image of an algebraic projective space.
\newblock \emph{Comptes Rendus Math\'ematique}, 350(5--6):\penalty0 239--241, 2012.
\newblock \doi{10.1016/j.crma.2012.02.002}.
\newblock URL \url{https://www.numdam.org/item/10.1016/j.crma.2012.02.002.pdf}.

'''
assert 'ColtoiuGasitoiJoita2012' not in current
guards.append(dict(key='opened-projectivity-source',old=anchor,new=bib+anchor))
log('',bib,['D18'],'lem:II:torsion-root-product-cover;cdp:st:C.2.UN.27;cdp:st:C.2.UN.30',
    'Add the exact opened primary article and its DOI; the complete Theorem2 and printed proof p241 were read, with the finite-fibre case attributed there to Remmert--van de Ven. No reproof credit is claimed.')

after=current
for g in guards:
    assert after.count(g['old'])==1,g['key']
    after=after.replace(g['old'],g['new'],1)
preserve_identifiers(current,after)
for x,y in zip(identifiers(current),identifiers(after)):
    assert all(y[k]==v for k,v in x.items())
    assert all(y[k]==1 for k in y-x)
(folder/(prefix+'guards.json')).write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n',newline='\n')
write_tsv(folder/(prefix+'defects.tsv'),read_tsv(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv')[0],rows)
print('Prepared',len(guards),'guards;',len(rows),'defect rows;',len(text.splitlines()),'UN30 receiving lines. No shared write.')
