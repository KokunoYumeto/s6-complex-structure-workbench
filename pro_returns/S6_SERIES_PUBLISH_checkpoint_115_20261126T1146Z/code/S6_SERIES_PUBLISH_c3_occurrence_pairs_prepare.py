"""Prepare shared signed roots and the complete paired/secondary occurrence units."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_occurrence_root'
prefix='S6_SERIES_PUBLISH_c3_occurrence_pairs_'
current=SOURCE.read_text()
start=r'\subsection{Paired roots and projective elliptic components}'
end=r'\begin{proposition}[An essential Enriques surface occurs in a compact zero-Euler torus filling]'
old=current[current.index(start):current.index(end)]
text=old;rows=[];counter=0

def edit(old_text,new_text,types,statement,reason):
    global text,counter
    assert text.count(old_text)==1,(statement,old_text[:120],text.count(old_text))
    text=text.replace(old_text,new_text,1)
    for kind in types:
        counter+=1
        rows.append(dict(change_id=f'II-C3-ROOT-OCCURRENCE-PAIRS-{counter:03}',type=kind,
            statement_id=statement,old_location='Complete paired-root and secondary Kodaira occurrence units',
            old_page='checkpoint35 source; final concordance pending',
            new_location='Signed-root owner and paired/secondary occurrence subsections',
            new_page='integrated final build pending',old_text=old_text,new_text=new_text,reason=reason,
            review_status='Complete original statements/proofs read by root; receiving rereading required before admission. Exposed comparison only.'))

for statement in ['cdp:st:C.2.UN.18','cdp:st:C.2.UN.21']:
    record=next(line for line in text.splitlines() if line.startswith('\\StatementRecord{'+statement+'}'))
    changed=record.replace(r'\SeriesRef{cdp:st:C.2.UN.3}',r'\cref{lem:II:signed-root-fibration,lem:II:hopf-curve-restriction,lem:II:nonuniruled-divisors}')
    changed=changed.replace(r'Example~3.4(1)]',r'Example~3.4(1), p.~99]')
    edit(record,changed,['D12','D18'],statement,
         'The hidden input declaration follows the exact earlier shared owners now applied in the receiving proof; the public header remains unchanged.')

# Transfer the ambient construction to its full stated surface domain.
a=text.index(r'\item Let $V$ be the blowup')
b=text.index(r'\item Write $B\simeq E$',a)
construction_old=text[a:b]
construction_new=r'''\item The logarithmic-transform occurrence in \cite[Example~3.4(1), p.~99]{Fujimoto1988Log} has a Kodaira-dimension-one component. Here the two opposite signs give the following projective component and fixed punctured family. Let $V$ be the blowup of $E\times\Delta$ at $(p_+,0)$ and $(p_-,0)$, with exceptional curves $R_+,R_-$. Put
\[
 D=R_+-R_-,\qquad L=\OO_V(D),\qquad
 \operatorname{div}(\sigma)=D,
 \tag{C.PE.4}\hypertarget{tag-00UH}{}\label{cdp:eq:C.PE.4}
\]
and apply \cref{lem:II:signed-root-fibration} with
$(D_+,D_-,m,q)=(R_+,R_-,m,e^{-2\pi})$.
Its two equations \eqref{cdp:eq:C.PE.5}--\eqref{cdp:eq:C.PE.6}
are the equations on these same line bundles and sections.
The identity on $(v,\ell,a)$, using $(\ell^{-1},a^{-1})$
in the negative chart, intertwines the gluing and deck maps.
Thus its quotient is the smooth threefold $U_m$ and its proper
projection is $\rho:U_m\to V$. Formula \eqref{cdp:eq:C.PE.9}
identifies its restriction over $\Delta^*$ with
$(E\times E)\times\Delta^*$, with inverse $[c]=[a^{-1}]$.

'''
edit(construction_old,construction_new,['D08','D12','D14','D18','D20','D22'],
    'cdp:st:C.2.UN.18;lem:II:signed-root-fibration',
    'The signed root construction, proper local quotient, product inverse and deck maps have the single earlier owner P339 with their full disjoint-divisor domain. The application identifies every input and the identical chart maps; the original result is unchanged.')
a=text.index(r'\item The coherent groups also retain exact maps.')
b=text.index(r'\item For a primary Hopf surface',a)
coherent_old=text[a:b]
coherent_new=r'''\item Apply \eqref{cdp:eq:C.PE.21} to this same compact $V$ and $\rho:Y_m\to V$. Its frame is the additive cocycle of the identical generator \eqref{cdp:eq:C.PE.7}. Since $h^k(V,\OO_V)=(1,1,0)$, the two nonzero Leray rows give $h^k(Y_m,\OO_{Y_m})=(1,2,1,0)$: every possible differential has target in $H^j(V,\OO_V)=0$ for $j\ge2$. Restrict the same finite product charts to the strict curve $B=E$. Their base changes are the charts of $P_m\to E$, so the invariant direct-image calculation and this deck frame give $\OO_E$ in degrees zero and one. Leray on the curve gives $h^k(P_m,\OO_{P_m})=(1,2,1)$.

'''
edit(coherent_old,coherent_new,['D08','D12','D20','D22'],
    'cdp:st:C.2.UN.18;lem:II:signed-root-fibration',
    'Transfer the global direct-image lemma PE21 to P339; identify the same generator and the transverse base-change charts for P_m. Name the vanishing target of the only possible Leray differential.')
a=text.index(r'\item For a primary Hopf surface')
b=text.index('The coherent normalization sequence',a)
edit(text[a:b],r'''\item Apply \cref{lem:II:hopf-curve-restriction} to
$Q_\pm=(\C^2\setminus0)/q^{m\Z}$ and to the same axis
inclusions $J_\pm\hookrightarrow Q_\pm$. It gives
$h^\bullet(Q_\pm,\OO)=(1,1,0)$ and restriction isomorphisms
$H^1(Q_\pm,\OO)\to H^1(J_\pm,\OO)$, represented by the
cocycle with value one on the generator $q^m$.
''',['D08','D12','D17','D20'],'cdp:st:C.2.UN.18',
    'Apply the earlier complete primary/secondary Hopf owner to the same scalar surfaces and elliptic axis inclusions; the coherent normalization computation remains.')
a=text.index(r'\item This is an explicit signed logarithmic-transform')
b=text.index(r'\end{enumerate}',a)
edit(text[a:b],'',['D01','D08','D12','D13'],'cdp:st:C.2.UN.18',
    'Integrate the exact Fujimoto credit at the construction and remove the closing history paragraph.')
edit('The inverse-map resolution\ncomparison in \\ref{cdp:st:C.2.UN.3} prevents contraction\nof any of these surfaces in a bimeromorphic\nmap between smooth threefold fillings.',
     'Apply \\cref{lem:II:nonuniruled-divisors} to these compact non-uniruled central divisors of the smooth proper disc filling $U_m$. Its strict-transform correspondence carries each surface birationally onto a divisor in every smooth bimeromorphic filling.',
     ['D12','D20','D22'],'cdp:st:C.2.UN.18','Use the complete general divisor owner with the exact smooth filling and the three proved non-uniruled divisors.')
edit('\\item Write $B\\simeq E$ for the strict central curve of $V$.',
     '\\item Write $B\\simeq E$ for the strict central curve of $V$ and $p:P_m\\to B$ for the restriction of $\\rho$.',
     ['D20'],'cdp:st:C.2.UN.18','Name the same elliptic projection used in the canonical and direct-image formulas.')
edit("The comparison can also be made by taking\nthe finite \\'etale Galois closure of \\eqref{cdp:eq:C.PE.12}, a\nprojective surface, and its finite algebraic quotient.",'',
     ['D12'],'cdp:st:C.2.UN.18','One projectivity argument suffices; the explicit finite étale cover and its full Jacobian proof remain.')
for a,b in [
 ('in the actual surface coordinates','in the surface coordinates'),
 ('its\nquotient gives actual differentiable products','its\nquotient gives differentiable products'),
 ('For the support use the actual union','For the support use the union')]:
    edit(a,b,['D08'],'cdp:st:C.2.UN.18','Remove the process qualifier; the exact coordinate, product or union map remains.')

anchor=r'\begin{proposition}[A free half-period quotient realizes secondary Kodaira normalization]'
edit(anchor,r'\subsection{Secondary Kodaira components}\label{subsec:II:secondary-kodaira-occurrence}'+'\n\n'+anchor,
     ['D14'],'cdp:st:C.2.UN.21','Give the complete half-period quotient and its integral/coherent calculations an actual subsection.')
edit('The full schemes in \\eqref{cdp:eq:C.SKD.1}, in contrast to their\nreductions, each have coherent dimensions $(1,2,1)$.',
     'Each full scheme fibre in \\eqref{cdp:eq:C.SKD.1} has coherent dimensions $(1,2,1)$.',
     ['D02'],'cdp:st:C.2.UN.21','State the full scheme dimensions directly; the distinct reduced dimensions remain in their labelled table.')
edit('by the actual quadratic base change at the first','by the quadratic base change at the first',
     ['D08'],'cdp:st:C.2.UN.21','The final displayed normalization map specifies the quadratic base change.')
edit('\\item Start with the compact version of \\ref{cdp:st:C.2.UN.3} at $n=1$:',
     '\\item Apply \\cref{lem:II:signed-root-fibration} to the compact surface and line bundle',
     ['D12','D20'],'cdp:st:C.2.UN.21','Use the earlier construction with m=1, retaining the exact ordinary line-bundle quotient map below.')
edit('where $R$ is the exceptional curve. Let $\\sigma$ be\nthe canonical section of $L$. The projection',
     'where $R$ is the exceptional curve, with $(D_+,D_-,m)=(R,\\varnothing,1)$ and the same $q$. Let $\\sigma$ be the canonical section of $L$. Projection from the hypersurface $\\sigma=a\\ell$ to $L^\\times$ has inverse $\\ell\\mapsto(\\ell,a=\\sigma/\\ell)$. These maps commute with the deck action and identify the constructed quotient with the displayed $\\widetilde Y$. The projection',
     ['D12','D20','D22'],'cdp:st:C.2.UN.21','Give the inverse projection identifying the m=1 root space with the same nonzero line bundle, including the exceptional divisor.')
edit('These are the\nactual line-bundle quotient maps of \\ref{cdp:st:C.2.UN.3}.',
     'The restrictions of this same quotient to the strict elliptic curve and the exceptional curve give these two components.',
     ['D08','D12','D20'],'cdp:st:C.2.UN.21','Name the two restrictions of the constructed map.')
edit('\\item We give the topology through actual mapping\ntori. Choose','\\item Choose',
     ['D08'],'cdp:st:C.2.UN.21','The explicit mapping-torus isomorphism gives the topological comparison.')
edit('\\item This also determines its integral groups,\nnot only their ranks. Writing','\\item Writing',
     ['D02'],'cdp:st:C.2.UN.21','State the integral groups with the following Wang and universal-coefficient maps.')
edit('For completeness, $B$ is also the product of an','The quotient $B$ is the product of an',
     ['D08'],'cdp:st:C.2.UN.21','The mapping-torus description is the proof of the additional integral groups.')
edit('The Hopf and elliptic rows were\ncomputed from their actual deck cocycles\nin \\ref{cdp:st:C.2.UN.18}. In particular\n$H^1(Q,\\OO_Q)\\to H^1(J,\\OO_J)$ is\nnonzero and hence onto.',
     'Apply \\cref{lem:II:hopf-curve-restriction} to the scalar Hopf quotient in \\eqref{cdp:eq:C.SKD.6} and its elliptic axis $J$. It gives the Hopf row and the isomorphism $H^1(Q,\\OO_Q)\\to H^1(J,\\OO_J)$ for this inclusion; the elliptic row is $h^\\bullet(J,\\OO_J)=(1,1)$.',
     ['D08','D12','D20'],'cdp:st:C.2.UN.21','Replace the indirect duplicate Hopf calculation by the same exact earlier owner used in UN18.')
edit('\\item We finally verify the full scheme fibres.\nUpstairs let','\\item Upstairs let',
     ['D08'],'cdp:st:C.2.UN.21','The following invariant thickening calculation proves the full scheme assertion directly.')
edit('The actual inverse image','The inverse image',['D08'],'cdp:st:C.2.UN.21','Remove the process qualifier; the full scheme inverse-image identity is preserved.')
edit('This comparison retains both\nthe nilpotent direction and its sign.','The invariant generator is $e$ or $te$ according to its stated sign.',
     ['D08'],'cdp:st:C.2.UN.21','Express the nilpotent/sign conclusion by the exact invariant basis.')
edit('The invariant generator is $e$ or $te$ according to its stated sign.','',
     ['D12'],'cdp:st:C.2.UN.21','The preceding invariant-basis calculation already gives this exact conclusion.')
edit('The inverse-map resolution comparison\nof \\ref{cdp:st:C.2.UN.3} therefore proves their\nessentiality.',
     'Apply \\cref{lem:II:nonuniruled-divisors} to these compact central divisors in the smooth quotient filling. The proved absence of rational curves gives its non-uniruled hypotheses, and the strict-transform correspondence proves their essentiality.',
     ['D12','D20','D22'],'cdp:st:C.2.UN.21','Identify the general divisor comparison and every geometric input explicitly.')
edit('this\nactual quadratic base change.\nThe construction supplies an\nexplicit secondary Kodaira component;\nno birational persistence of its\nsecondary type under that base change\nis asserted.',
     'this quadratic base change.',
     ['D02','D08','D11'],'cdp:st:C.2.UN.21','The normalization morphism already states exactly which primary Kodaira component is recovered; remove the closing scope disclaimer.')

# Resolve all visible inherited equation names before changing their numbers.
for match in list(re.finditer(r'\((C\.[A-Z]+\.[0-9]+)\)',text)):
    literal=match.group(0);label='cdp:eq:'+match.group(1)
    if text.count(literal)==1:
        edit(literal,r'\eqref{'+label+'}',['D04','D19'],'cdp:st:C.2.UN.18;cdp:st:C.2.UN.21',
             'Resolve the inherited literal equation reference through its unchanged label.')
for match in list(re.finditer(r'\\\[(.*?)\\\]',text,re.S)):
    block=match.group(0)
    if re.search(r'\\tag\{[^}]+\}',block):
        converted='\\begin{equation}'+re.sub(r'\\tag\{[^}]+\}','',match.group(1))+'\\end{equation}'
        edit(block,converted,['D04','D19'],'cdp:st:C.2.UN.18;cdp:st:C.2.UN.21',
             'Use the section equation counter, retaining each formula, original label and permanent target.')

text+=r'\subsection{Enriques and further elliptic components}\label{subsec:II:enriques-elliptic-occurrence}'+'\n\n'
owner=(folder/'S6_SERIES_PUBLISH_P339.tex').read_text()
anchor=r'\subsection{Elliptic root fillings}\label{subsec:II:elliptic-root-fillings}'
preserve_identifiers(old,text+owner)
for old_ids,new_ids in zip(identifiers(old),identifiers(text+owner)):
    assert all(new_ids[k]==v for k,v in old_ids.items())
    assert all(new_ids[k]==1 for k in new_ids-old_ids)
for kind in ['D12','D14','D20','D22']:
    counter+=1
    rows.append(dict(change_id=f'II-C3-ROOT-OCCURRENCE-PAIRS-{counter:03}',type=kind,
        statement_id='lem:II:signed-root-fibration',old_location='UN18 signed ambient construction and global higher direct images',
        old_page='checkpoint35 source; final concordance pending',new_location='Earlier signed-root-fibrations subsection',
        new_page='integrated final build pending',old_text=construction_old+coherent_old,new_text=owner,
        reason='State and prove the shared root construction for a smooth surface with disjoint smooth signed divisors, including an empty side and m=1. The same local root maps, invariant direct images and global deck frame prove every asserted case. UN18 and UN21 are exact applications; the pending bounded UN6 transfer is separate.',
        review_status='Complete old construction and direct-image proof read; complete new owner and receivers require rereading before admission. No independent credit.'))
(folder/(prefix+'replacement.tex')).write_text(text,newline='\n')
(folder/(prefix+'guards.json')).write_text(json.dumps([
    {'key':'signed-root-owner','old':anchor,'new':owner+anchor},
    {'key':'paired-secondary-occurrence','old':old,'new':text}],ensure_ascii=False,indent=2)+'\n',newline='\n')
write_tsv(folder/(prefix+'defects.tsv'),read_tsv(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv')[0],rows)
print('Prepared',len(owner.splitlines()),'owner lines and',len(text.splitlines()),'receiving occurrence lines;',len(rows),'defects. No main write.')
