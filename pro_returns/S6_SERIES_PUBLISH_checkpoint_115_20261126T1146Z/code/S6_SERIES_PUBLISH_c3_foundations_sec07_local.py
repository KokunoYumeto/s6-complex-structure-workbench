from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations/sec07'
source = (OUT / 'S6_SERIES_PUBLISH_II_sec07_input.tex').read_text()
rows = []
guards = []
equations = []

def block(key):
    p = source.index(r'\label{'+key+'}')
    a = source.rfind(r'\begin{', 0, p)
    b = source.index(r'\end{proof}', p) + len(r'\end{proof}')
    return source[a:b]

def row(kinds, owner, old, new, reason):
    for kind in kinds.split(','):
        rows.append(dict(change_id=f'II-C3-S07-L-{len(rows)+1:03}', type=kind,
            statement_id=owner, old_location='sec:II:07 / '+owner,
            old_page='cp35; page concordance pending',
            new_location='subsec:II:local-numerical-conductor-inputs / '+owner,
            new_page='integrated build pending', old_text=old, new_text=new,
            reason=reason, review_status='Complete original read; receiving comparison pending.'))

def edit(text, old, new, kinds, owner, reason):
    assert old in text, (owner, old[:120])
    for i in range(text.count(old)):
        row(kinds, owner, old, new, reason+f' [Occurrence {i+1}.]')
    return text.replace(old, new)

def equation_numbers(text, owner):
    def convert(m):
        body=m.group(1)
        tag=re.search(r'\\tag\{([^{}]+)\}',body)
        if not tag:
            return m.group(0)
        label=re.search(r'\\label\{([^{}]+)\}',body).group(1)
        equations.append(dict(old_tag=tag.group(1),label=label,owner=owner))
        new='\\begin{equation}'+re.sub(r'\\tag\{[^{}]+\}','',body)+'\\end{equation}'
        row('D19',owner,m.group(0),new,'Use section equation numbering; retain the permanent label and tag target.')
        return new
    return re.sub(r'\\\[([\s\S]*?)\\\]',convert,text)

mh1_original=block('cdp:st:C.2.MH.1')
mh1=mh1_original
mh1=edit(mh1,'the actual morphism','the morphism','D08','cdp:st:C.2.MH.1','The support-to-restriction arrow is already displayed explicitly.')
mh1=edit(mh1,'Neither a K\\"ahler metric on $U$ nor a projective\ncompactification of $U$ is needed for this comparison.','', 'D02,D11','cdp:st:C.2.MH.1','The statement gives the smooth analytic ambient domain and its projective-strata hypothesis once.')
a=mh1.index('The tensor product in \\eqref{cdp:eq:C.MH.2}')
b=mh1.index('\n\\item Totalizing',a)
old=mh1[a:b]
new=r'''In normal-crossing coordinates the ideal of $C$ is preserved by the logarithmic differential, so \eqref{cdp:eq:C.MH.2} is a complex. Give it the quotient residue filtration and the filtration by form degree. The local filtered comparison in \cite[\S3, Theorem~1 and Corollary~2, pp.~5--7]{Steenbrink1999} identifies the quotient map from the restricted logarithmic complex with a filtered quasi-isomorphism to \eqref{cdp:eq:C.MH.2}; its rational realization is $i_C^*Rj_*\mathbb Q_{U'\setminus D}$, where $j$ is the open inclusion. The source's proof uses the holomorphic normal-crossing coordinates and iterated residue maps. Those maps are defined here on the same divisor line bundles and agree on overlaps. Every residue stratum $D_J\cap C$ is projective by hypothesis, so its shifted de Rham complex, with Tate twist, has the purity used in that proof. This supplies the mixed Hodge complex on the compact stratum in the present analytic ambient space.
'''
mh1=edit(mh1,old,new,'D17,D18','cdp:st:C.2.MH.1','Opened Steenbrink arXiv:math/9902134v1, printed pp.5–7, and read Theorem1/full proof and Corollary2. Retain the exact analytic extension map: the source has an algebraic global ambient, while its local residue construction transfers to the same compact projective strata here. The general analytic statement is proved here, not attributed wholesale to the source.')
mh1=edit(mh1,r'\cite[Section~4, equation~(3)]{Steenbrink1999}',r'\cite[\S4, equation~(3), p.~9]{Steenbrink1999}','D18','cdp:st:C.2.MH.1','The exact support-cone source locus was opened and read; its use is through the local excision comparison, whose analytic extension is retained.')
mh1=edit(mh1,'For completeness, the weight bound on the source can\nbe checked without invoking an invariant-cycle theorem.','The weight bound on the support complex follows from its residue comparison.','D02,D08','cdp:st:C.2.MH.1','State the weight argument directly; retain the full support spectral sequence and comparison maps.')
mh1=edit(mh1,'use the actual support triangle','use the support triangle','D08','cdp:st:C.2.MH.1','The triangle and its maps are displayed.')
mh1=edit(mh1,'Thus \\eqref{cdp:eq:C.MH.3} compares the actual support\ncomplex, including its arrow to $K(D)$, rather than\nonly its unfiltered vector spaces.','Thus \\eqref{cdp:eq:C.MH.3} compares the support complex and its arrow to $K(D)$ as filtered complexes.','D02,D08','cdp:st:C.2.MH.1','Keep the filtered compatibility proved by the residue induction.')
mh1=equation_numbers(mh1,'cdp:st:C.2.MH.1')

mh2_original=block('cdp:st:C.2.MH.2')
mh2=mh2_original[:mh2_original.index(r'\begin{proof}')]
mh2=edit(mh2,'The calculation retains all multiplicities in the full\nfibre and places no normal crossings assumption on $S$.','', 'D02,D11','cdp:st:C.2.MH.2','The full fibre mS and irreducible reduced support are already the stated domain.')
mh2=edit(mh2,mh2[mh2.index(r'\StatementRecord'):mh2.index('\n',mh2.index(r'\StatementRecord'))],r'\StatementRecord{cdp:st:C.2.MH.2}{proved}{01C5}{\cref{cdp:st:D.1.9,cdp:st:D.1.8,lem:II:torus-tube-character}}','D12,D14','cdp:st:C.2.MH.2','The local character calculation has one earlier owner; this corollary applies the global integral class to that owner.')
mh2+=r'''\begin{proof}
The integral class of \cref{cdp:st:D.1.9} restricts nontrivially to $S$ and, by \cref{cdp:st:D.1.8}, to the nearby torus. On a small disc $\Delta$ the integral Leray edge map is the isomorphism
\[
 H^1(f^{-1}\Delta,\mathbb Z)\simeq
 H^0(\Delta,R^1f_*\mathbb Z),
\]
because the two adjacent groups $H^1(\Delta,\mathbb Z)$ and $H^2(\Delta,\mathbb Z)$ vanish. It therefore gives the same tube class as the homotopy equivalence in \cref{lem:II:compact-analytic-tube}: both restrict to the stated class on $S$. Apply \cref{lem:II:torus-tube-character} to this class and to the given normalization resolution. Its rational and ruled alternatives are exactly \eqref{cdp:eq:C.MH.6} and \eqref{cdp:eq:C.MH.7}.
\end{proof}
'''
row('D12,D14','cdp:st:C.2.MH.2',mh2_original[mh2_original.index(r'\begin{proof}'):],mh2[mh2.index(r'\begin{proof}'):],'Move the cyclic cover, Koszul contraction, support duality, projective-strata purity, conductor descent, exceptional-matrix map and all coefficient dimensions to P289. Retain the integral Leray tube-lift map as this global application, and preserve MH.8–14 and UI.9–11 at that single owner.')
mh2=equation_numbers(mh2,'cdp:st:C.2.MH.2')

local=(OUT/'S6_SERIES_PUBLISH_II_sec07_local_numerical.tex').read_text()
character=(OUT/'S6_SERIES_PUBLISH_II_sec07_character.tex').read_text()
row('D22,D25','lem:II:torus-tube-character','Every nonzero class gamma_S extends; the later Euler alternatives were separated from that quantifier.','Choose a nonzero class gamma_S in H1(S,Z); every subsequent local system and Euler conclusion uses this chosen class.','Make the inherited nonzero-class premise an explicit datum for the entire extracted lemma, as in original UN.7. This is a clarification of the receiving statement’s scope before admission, not a refutation of the original statement or an unconditional Euler assertion.')
fragment=r'\subsection{Local numerical and conductor criteria}\label{subsec:II:local-numerical-conductor-inputs}'+'\n\n'+local+'\n'+mh1+'\n\n'+character+'\n'+mh2
fragment=re.sub(r'\n{3,}','\n\n',fragment).strip()+'\n'
(OUT/'S6_SERIES_PUBLISH_II_sec07_local_inputs.tex').write_text(fragment,newline='\n')

# The local owner replaces only the indicated proof blocks at its consumers.
for key,start,end,new,reason in [
 ('cdp:st:C.2.UN.7',r'\item \medskip\noindent\textbf{The actual canonical and Chern-class comparisons.}',r'\item \par\medskip\noindent\textbf{The proper analytic Lefschetz formula.}',r'''\item \textbf{Canonical and Chern classes.}
Choose a small disc $\Delta$ around the chosen value and put $U=f^{-1}(\Delta)$. Apply \cref{lem:II:torus-tube-numerical} to the full fibre $mS$ and its minimal normalization resolution. It supplies the torsion canonical and adjunction lines, $\chi(\OO_S)=0$, the two vanishing Chern classes and the degree-zero restrictions in \eqref{cdp:eq:C.UI.2}--\eqref{cdp:eq:C.UI.4}.

''','P281 owns the full local canonical/Cartier-filtration/radial-cycle calculation, at the same proper smooth local torus scope.'),
 ('cdp:st:C.2.UN.7',r'\item \par\medskip\noindent\textbf{The local degree-one class and the finite-character comparison.}',r'\item \par\medskip\noindent\textbf{Strict positivity for a rational normalization.}',r'''\item \textbf{Finite-character comparison.}
For each nonzero class $\gamma_S\in H^1(S,\mathbb Z)$, \cref{lem:II:torus-tube-character} gives its tube extension, its nonzero restriction to the smooth fibre, and the finite augmentation local system. When $Z$ is rational or ruled, its normalization and resolution maps are exactly \eqref{cdp:eq:C.MH.10}--\eqref{cdp:eq:C.MH.12}, and \eqref{cdp:eq:C.UI.11} gives respectively $e(S)=2$ or $e(S)=2-2g$. Since $H^1(S,\mathbb Z)$ is a lattice in $H^1(S,\mathbb Q)$, the nonzero rational condition in item~1 supplies such an integral class.

''','P289 contains the full local character proof, preceding this theorem and its global MH.2 application; all UI.9–11/MH.8–14 identifiers remain there.'),
 ('cdp:st:C.2.UN.10',r'\item We first supply the comparisons',r'\item Here are the parts of that argument',r'''\item Apply \cref{lem:II:torus-tube-numerical} to the stated proper map and full fibre. Its identities \eqref{cdp:eq:C.UNCR.1}--\eqref{cdp:eq:C.UNCR.2} give $\omega_S$ torsion and $\chi(\OO_S)=0$; \eqref{cdp:eq:C.UI.4} gives $K_Z+D=h^*\omega_S$ for the divisor $2C+V$ in the statement.

''','The two canonical/Cartier equations are aliases at P281; the contracted-section proof uses exactly their torsion and Euler conclusions.'),
 ('cdp:st:C.2.UN.12',r'\item We first check the classification',r'\item Every positive pluricanonical section',r'''\item Choose a sufficiently small fibre tube $U$. By \cref{lem:II:torus-tube-numerical}, $K_U$ and $\omega_S$ are torsion, $\chi(\OO_S)=0$, and the resolution conductor satisfies $K_Z+D=h^*\omega_S$. For nonnormal $S$, this effective divisor is nonempty.

''','Replace the repeated local canonical and filtration proof by the same earlier numerical owner, preserving its unrestricted proper local domain.')
]:
    original=block(key);a=original.index(start);b=original.index(end,a);old=original[a:b]
    guards.append(dict(key=key+' / '+start[:60],old=old,new=new,reason=reason))
    row('D12,D14',key,old,new,reason)

old='formula used in \\SeriesRef{cdp:st:C4e}.'
new='formula of \\cref{lem:II:plane-branch-conductor}.'
guards.append(dict(key='IRR1 earlier branch-conductor owner',old=old,new=new,reason='P282 extracts the exact RAT.3 factorization and finite-duality calculation; the later tangent-cohomology C4e supplies no additional premise here.'))
row('D12,D14','cdp:st:C.2.IRR.1',old,new,'Use the earlier exact plane-branch formula. P4.34 residue identity and RAT.3 factorization were fully read; no conclusion or hypothesis of C4e is moved or weakened.')
old=r'\SeriesRef{cdp:st:C4e}'
new=r'\cref{lem:II:plane-branch-conductor}'
record=block('cdp:st:C.2.IRR.1').splitlines()[1]
guards.append(dict(key='IRR1 hidden conductor dependency',old=record,new=record.replace(old,new),reason='Match the hidden dependency to the exact earlier owner.'))
row('D18','cdp:st:C.2.IRR.1',record,record.replace(old,new),'The hidden dependency follows the proof application; its permanent tag and label remain.')

rat=block('cdp:st:C.2.RAT.3');a=rat.index('To verify the displayed');b=rat.index('Thus there are at most two',a)
old=rat[a:b];new='The residue comparison of \\cref{lem:II:plane-branch-conductor} gives this exponent with $c_i=2$. '
guards.append(dict(key='RAT3 earlier plane-branch formula',old=old,new=new,reason='P282 now owns this exact residue-factorization proof for every reduced plane curve.'))
row('D12,D14','cdp:st:C.2.RAT.3',old,new,'The coefficient-two equality, the count of other branches and the r_dom bound remain at RAT.3; only the repeated general formula proof moves to P282.')

for old_tag,label in [('C.UI.2','cdp:eq:C.UI.2'),('C.UNCR.1','cdp:eq:C.UNCR.1'),('C.UI.3','cdp:eq:C.UI.3'),('C.UNCR.2','cdp:eq:C.UNCR.2'),('C.UI.4','cdp:eq:C.UI.4'),('C.UI.9','cdp:eq:C.UI.9'),('C.UI.10','cdp:eq:C.UI.10'),('C.UI.11','cdp:eq:C.UI.11')]+[(f'C.MH.{n}',f'cdp:eq:C.MH.{n}') for n in range(8,15)]:
    equations.append(dict(old_tag=old_tag,label=label,owner='lem:II:torus-tube-numerical' if 'UNCR' in old_tag or old_tag in ('C.UI.2','C.UI.3','C.UI.4') else 'lem:II:torus-tube-character'))
    row('D19',label,old_tag,label,'The old printed tag is replaced by section equation numbering. The existing label and target survive, with SsixEquationAliases where two original equations have one owner.')

# Admission anchor matches the receiving boundary communicated by root.
anchor=r'\subsection{Local numerical and conductor criteria}\label{subsec:II:local-numerical-conductor-inputs}'
history_start=source.index('The statements \\ref{cdp:st:C.2.CR.1}')
history_end=source.index(r'\begin{proposition}[Topology and coefficients',history_start)
history=source[history_start:history_end]
guards.insert(0,dict(key='local inputs at receiving boundary',old=anchor,new=fragment.rstrip()+'\n\n'+r'\subsection{Contracted ruled boundaries}\label{subsec:II:contracted-ruled-boundaries}',reason='Put the full local numerical and character prerequisites before their consumers.'))
guards.extend([dict(key='remove moved MH1',old=mh1_original,new='',reason='The complete proposition and its proof stand once in the earlier local-input subsection.'),dict(key='remove moved MH2',old=mh2_original,new='',reason='The global character corollary and its exact tube-class map stand after the single local owner.'),dict(key='remove contracted history bridge',old=history,new='',reason='The subsequent numbered theorems state their hypotheses, bounds and exclusion; the draft-history summary adds no separate mathematical assertion.')])
row('D01,D13,D14','sec:II:07',history,'','Delete the historical bridge; preserve each cited result at its numbered statement, and put their prerequisite proofs first.')
row('D12,D14','cdp:st:C.2.MH.1',mh1_original,mh1,'Move the complete analytic purity proposition before the local-character application, with the exact opened-source comparison and all five equation identifiers.')
row('D14','sec:II:07',anchor,fragment[:fragment.index('\\begin{lemma}')],'The local numerical/character subsection has its complete prerequisite proofs and closes before the contracted-boundary subsection. Further sec07 restructuring remains separate.')

for pattern in (r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}'):
    removed='\n'.join(g['old'] for g in guards if g['new']=='')
    for identity in re.findall(pattern,removed):
        assert len(re.findall(re.escape(identity),fragment))>=1,identity
    identities=re.findall(pattern,fragment)
    assert len(identities)==len(set(identities)),[x for x in identities if identities.count(x)>1]
assert '\r' not in fragment
(OUT/'S6_SERIES_PUBLISH_sec07_local_guards.json').write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n',newline='\n')
for suffix,data,fields in [('defects',rows,list(rows[0])),('equation_map',equations,['old_tag','label','owner'])]:
    with (OUT/f'S6_SERIES_PUBLISH_sec07_local_{suffix}.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
print(f'Local inputs prepared: {len(fragment.splitlines())} lines; {len(guards)} guards; {len(rows)} defect rows. Receiving read still pending.')
