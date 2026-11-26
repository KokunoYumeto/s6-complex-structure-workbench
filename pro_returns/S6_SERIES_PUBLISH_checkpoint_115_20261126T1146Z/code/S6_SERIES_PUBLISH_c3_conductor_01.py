#!/usr/bin/env python3
"""Prepare the read-and-compared cotangent section; never edit the shared source.

The output is a replacement fragment, individual defect rows, actual rereading
events, and a unit-status table.  No derived inventory or admission record is
generated.  Text output uses LF throughout.
"""
from pathlib import Path
import csv
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_conductor'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_II.tex'
PRE = 'S6_SERIES_PUBLISH_c3_conductor_01'
START = r'\section{Cotangent torsion, conductor and the printed endpoint error}'
END = r'\section{Normalization, conductor genus and local torus exclusions}'
original_source = SOURCE.read_text()
start = original_source.index(START)
end = original_source.index(END)
original = original_source[start:end]
working = original
rows = []
changed_owners = set()

def owner_at(text, pos):
    ms = list(re.finditer(r'\\StatementRecord\{([^{}]+)\}', text[:pos]))
    return ms[-1].group(1) if ms else 'sec:II:04'

def log(kind, old, new, reason, owner=None, location=None):
    if owner is None:
        p = original.find(old)
        owner = owner_at(original, p) if p >= 0 else 'sec:II:04'
    p = original.find(old)
    old_line = original_source[:start + max(p, 0)].count('\n') + 1
    rows.append(dict(
        change_id=f'II-C3-COT-{len(rows)+1:04d}', type=kind,
        statement_id=owner, old_location=location or f'cp35 source line {old_line}',
        old_page='cp35 PDF omitted from supplied checkpoint; source locus given',
        new_location=location or owner, new_page='pending integrated final PDF',
        old_text=old, new_text=new, reason=reason,
        review_status='Original and receiving mathematical context read and compared; final PDF reading remains open.'
    ))
    if owner != 'sec:II:04':
        changed_owners.add(owner)

def replace(old, new, kind, reason, owner=None, count=1):
    global working
    assert working.count(old) == count, (old[:120], working.count(old), count)
    if count == 1:
        log(kind, old, new, reason, owner)
    else:
        offset = 0
        for _ in range(count):
            p = working.index(old, offset)
            log(kind, old, new, reason, owner or owner_at(working, p))
            offset = p + len(old)
    working = working.replace(old, new)

replace(START, r'\section{Cotangent torsion and the Campana--Demailly--Peternell endpoint argument}',
        'D14', 'The section title names its sheaf calculation and the published argument to which it applies.', 'sec:II:04')
replace(r'Put $K=\ker(V\to Q)$.',
        r'Put $K=\ker(V\to Q)$; we also write $\widetilde\Omega_S^1=Q$ for the quotient of $\Omega_S^1$ by $T$.',
        'D20', 'The two cotangent symbols are explicitly identified by their common quotient map.', 'def:II:conormal-data')

# Cite the already established inclusion; retain the excess-kernel and
# conductor-pushout morphisms, which are the additional form used here.
old_trace = working[working.index(r'\item Trace duality gives $JB\subset R$.'):working.index(r'\item The module $D$ consists exactly')]
new_trace = r'''\item Apply \cite[Proposition~3.4, pp.~9--10, and Corollary~3.5, p.~10, arXiv v7]{GS2014} with their reduced hypersurface $D=S$ and local equation $h=F$. Their residue module is
$\mathcal R_D=\operatorname{Hom}_R(J,R)=J^{-1}$, where a meromorphic multiplier $q$ acts by $b\mapsto qb$; their conductor is $\mathcal C_D=\operatorname{Ann}_R(B/R)=\mathfrak c$.
Their inclusions give $J\subset\mathfrak c$ and $B\subset J^{-1}$.
Tensoring the latter inclusion by $N^*$ and using \eqref{cdp:eq:A.2} and the finite projection formula gives the last inclusion in \eqref{cdp:eq:A.3}.

'''
replace(old_trace, new_trace, 'D17',
        'Opened the complete Proposition 3.4 and Corollary 3.5 in the attached Granger--Schulze arXiv source. The identity of local rings, derivative ideals, multiplier maps and conductors is written explicitly. Removed the independent trace-duality proof of these known inclusions; retained the exact excess-kernel and conductor-section maps.', 'cdp:st:A.2.2')
old_gs = r'''The fractional ideal appearing in (A.2) has an established interpretation. Granger--Schulze, Proposition~3.4 and Corollary~3.5 of \cite{GS2014}, identify $J^{-1}$ with the module of logarithmic residues and prove the inclusions in \eqref{cdp:eq:A.3}. The preceding proof gives the maps needed here directly. Their Theorems~1.1 and~1.3 also give the following exact extension of the normal-crossings case.'''
replace(old_gs, '', 'D13', 'The residue identification and its exact source locator now occur in the owning proof of A.2.2. The following explicit normal-crossing generator formula keeps its own proof.', 'cdp:st:A.2.2')
replace('\\item \n\n\\end{enumerate}\n\\end{proof}', '\\end{enumerate}\n\\end{proof}',
        'D23', 'Removed the empty third proof item after the two completed pinch-point and cusp calculations.', 'cdp:st:A.2.4')
old_criterion = r'''For ordinary surfaces the exact ambient-vanishing criterion is (A.1) with $K\otimes A=\eta_*\eta^*(N^*\otimes A)$. For surfaces with cuspidal-edge charts it is (A.1) with the locally specified sheaf $N^*\otimes t^{-1}B$. These specify the first group and the target of the connecting homomorphism, including the extra polar term at the cusp. Under $H^0(QA)=0$ they reduce respectively to the vanishing of these explicitly computed kernel sections. The general criterion (A.4)--(A.5) retains the full conductor and applies without a singularity-type restriction.'''
replace(old_criterion, '', 'D12', 'Every formula in this recap already occurs once with its map: the section criterion in A.1.1, the ordinary/cusp kernels in A.2.4, and the conductor maps in A.2.2. No additional assertion or hypothesis is removed.', 'cdp:st:A.2.5')
log('D13', old_criterion, '', 'Removed the same unnumbered recap between the residue-pole proof and the critical-curve example.', 'cdp:st:A.2.5')
old_bridge = r'''The construction in Statement \ref{cdp:st:B2} supplies the compact local counterexample, including its bundles, cohomology groups and direct-image lengths. The universal assertion under every hypothesis of CDP20 Theorem 2.2 is proved in \ref{cdp:st:C4e} below: positive third Chern number forces one fixed irreducible nonnormal reduced support whose normalization has the required nonzero group for every ambient Picard twist. Its proof uses the full-fibre comparisons of A.3 and the conductor arguments of A.5. The named-family tests are \ref{cdp:st:C4g}.'''
replace(old_bridge, '', 'D13', 'Removed the orphan synopsis. B2 contains the complete example, C4e contains the universal assertion, and C4g contains its applications. No conclusion is transferred to the projective example, whose hypotheses and topology remain in B3.', 'cdp:st:B3')
log('D06', old_bridge, '', 'The same deleted synopsis was the sole A.3/A.5 topic shorthand in this unit. Its mathematical owners remain the actual labelled statements.', 'cdp:st:B3')

old_thick = r'''This finite-translation argument supplies the thickening step intended in Remark~7.2 once ambient vanishing on the smooth support is established. On a smooth support, the conormal sequence has $Q=\Omega_S^1$ and $K=N^*$, so the two requisite support vanishings do establish that ambient vanishing. Remark~7.4 requires the same argument on a singular support; a statement solely about $Q=\widetilde\Omega_S^1$ leaves the kernel in \ref{cdp:st:A.1.1} to be checked. Thus the thickening operation itself has a complete exact treatment, while the cited singular-support assertion cannot supply its missing kernel hypothesis. Example \ref{cdp:st:A.3.2} disproves the inference from a single support vanishing even with torsion conormal; it does not refute a generic-vanishing assertion already established for all the finitely translated twists.'''
new_thick = r'''\begin{remark}[Thickening and the conormal criterion]\hypertarget{tag-P221}{}\label{rem:II:thickening-endpoint}
\StatementRecord{rem:II:thickening-endpoint}{proved}{P221}{}
On a smooth support the conormal filtration in \cref{cdp:st:A.1.1} has $K=N^*$ and $Q=\Omega_S^1$. Thus the vanishing of the two end groups gives ambient vanishing, and the finite translations in \cref{cdp:st:A.3.3} give the thickening step of \cite[Remark~7.2, p.~693]{CDP2020}. On a singular support the same section sequence contains $H^0(S,K\otimes A)$, with $K=N^*\otimes\mathcal J^{-1}$ by \cref{cdp:st:A.2.1}; this is the additional kernel group required in the application to \cite[Remark~7.4, p.~695]{CDP2020}. In \cref{cdp:st:A.3.2}, the successive invariant characters give zero sections on $S$ and three on $mS$; the finite-translation criterion requires vanishing at every displayed translated twist.
\end{remark}'''
replace(old_thick, new_thick, 'D13', 'Placed the published thickening comparison in one numbered mathematical remark. The conormal quotient, inverse-Jacobian kernel and invariant-character inclusions state the exact relations used in the comparison; the example and translation criterion are not restated as new theorems.', 'rem:II:thickening-endpoint')
log('D11', old_thick, new_thick, 'Replaced repeated negative scope commentary by the exact two section sequences and the finite family of twists required by the criterion.', 'rem:II:thickening-endpoint')
replace(r'No splitting of the thickening, cyclic base change, or assumption about the normal bundle has been used.', '', 'D02', 'The complete ideal-quotient and locally-free tensor maps already establish the asserted scope; removed the closing defensive clause.', 'cdp:st:A.3.1')
replace(r'Under the hypotheses of CDP20 Proposition~7.3,', r'Under the hypotheses of \cite[Proposition~7.3, p.~693]{CDP2020},', 'D18', 'Bound the published hypothesis reference to its bibliography key and precise statement/page.', 'cdp:st:A.3.4')
replace(r'The assertion includes the entire scheme-theoretic fibre, with every nilpotent layer.', '', 'D11', 'The statement already gives its group on mS, and the proof specifies each ideal-power layer. Removed the repeated scope sentence.', 'cdp:st:A.3.4')
replace(r'The conclusion follows from this kernel calculation, not from numerical upper semicontinuity alone.', '', 'D02', 'The displayed mutually inverse kernel maps and determinantal rank locus already prove the conclusion; removed the defensive contrast.', 'cdp:st:A.3.4')
replace(r'This proves the simultaneous generic assertion and the smooth-multiple conclusion of Remark~7.2. For a singular support the identical root cover retains its singularities and the kernel $N^*\otimes\mathcal J^{-1}$; the present proof does not erase that term in Remark~7.4.', '', 'D11', 'The statement contains the simultaneous conclusion, and the single numbered thickening remark owns the published comparison with the exact kernel map.', 'cdp:st:A.3.4')
replace(r'These results apply to compact Hermitian manifolds without a K\"ahler hypothesis.',
        r'These results apply to compact Hermitian manifolds.', 'D02',
        'State the exact positive class to which the cited Green and Hodge identities apply.', 'cdp:st:A.3.4')
replace(r'Multiplication of $F$ by a unit and changes of coordinates were checked in \ref{cdp:st:A.2.1}. Formula \eqref{cdp:eq:A.6} is the restriction of the canonical fractional-ideal map, so it glues without a chosen branch ordering, equation, or coordinate system.',
        r'The equation and coordinate transition maps are those of \cref{cdp:st:A.2.1}. They preserve the canonical fractional-ideal map whose restriction is \eqref{cdp:eq:A.6}; permutation of the branches permutes the same direct-sum factors and terms. Thus the local formulas glue to that canonical morphism.',
        'D02', 'Write the equation, coordinate and branch-permutation maps that prove the canonical gluing, replacing the negative list of choices.', 'cdp:st:A.1.2')
log('D08', r'Multiplication of $F$ by a unit and changes of coordinates were checked in \ref{cdp:st:A.2.1}.',
    r'The equation and coordinate transition maps are those of \cref{cdp:st:A.2.1}.',
    'Replaced checking language by the mathematical transition maps.', 'cdp:st:A.1.2')

# The source states nonvanishing and the quotient vanishing.  The dimension-one
# sharpening remains as the short application of this paper's conormal map.
credit = r'''The nonvanishing on the compact example and the torsion-free-cotangent vanishing are contained in \citet[Theorem~10.5 and Section~10.4]{AC26}.'''
replace(credit, '', 'D13', 'Moved the exact known inputs into the proof where they are used, with the original manuscript page numbers.', 'cdp:st:A.4.1')
a = working.index(r'\begin{proposition}[Cotangent groups on the rational normalization fibre]')
b = working.index(r'\begin{proposition}[Constant twists on an elliptic ruled surface]')
block = working[a:b]
proof_start = block.index(r'\begin{proof}')
proof_end = block.index(r'\end{proof}') + len(r'\end{proof}')
old_proof = block[proof_start:proof_end]
new_proof = r'''\begin{proof}
For every $B\in\Pic(X)$, the triviality of $\eta^*(B|_W)$ is \cite[Theorem~10.5, proof Step~1, p.~88]{AC26}. The normalization differential and its injection on the torsion-free quotient are the maps of \cite[\S10.4, pp.~89--90]{AC26}:
\[
 Q\otimes B|_W\hookrightarrow
 \eta_*\bigl(\Omega^1_{\operatorname{dP}_6}\otimes\eta^*(B|_W)\bigr).
\]
The same source gives $H^0(\operatorname{dP}_6,\Omega^1)=0$, so the projection formula proves the quotient vanishing. This applies to $B=K_X\otimes L^{-1}$ and to arbitrary $B$.

The full reduced fibre $W$ has trivial conormal. By \cref{cdp:st:A.1.2},
$K\otimes A=\eta_*\eta^*A=\eta_*\OO_{\operatorname{dP}_6}$.
The normalization is connected and compact, so this sheaf has section space $\C$. The exact sequence \eqref{cdp:A:filtration2}, together with the quotient vanishing just proved, identifies that section space with $H^0(W,\Omega_X^1|_W\otimes A)$.
\end{proof}'''
replace(old_proof, new_proof, 'D17', 'Read original AC26 printed pp.87--90, including complete Lemma 10.3, Theorem 10.5 and section 10.4. Cited its Picard pullback and quotient-form calculations through their actual maps. Retained the dimension-one sharpening, which follows by the already proved canonical normal-crossing kernel identification.', 'cdp:st:A.4.1')

replace(r'Such a surface has no holomorphic one-forms, by birational invariance as proved in \ref{cdp:st:A.4.1}.',
        r'To compare its one-forms with those on $\PP^2$, take a common resolution by point blowups. At each blowup, restriction away from the exceptional curve and Hartogs extension of the coefficients over the blown-up point give the inverse of pullback on global one-forms. The resulting isomorphism identifies this group with $H^0(\PP^2,\Omega^1_{\PP^2})=0$.',
        'D14', 'Placed the general rational-surface one-form comparison in its owner A.4.5. The inverse pullback map is the same Hartogs extension formerly used in A.4.1; that earlier specialization now cites AC26 and no longer claims to prove the general comparison.', 'cdp:st:A.4.5')

replace(r'The divisor Riemann--Roch calculation in \ref{cdp:st:A.5.2} gives $\chi(\OO_S)=0$ under the stated rational cohomology hypothesis, yielding $h^1=2$.',
        r'Under $H^2(Y,\Q)=0$, one has $c_1(\OO_Y(S))=0$ rationally. The divisor sequence and Hirzebruch--Riemann--Roch therefore give $\chi(\OO_S)=\chi(\OO_Y)-\chi(\OO_Y(-S))=0$, yielding $h^1=2$.',
        'D14', 'Expanded the exact one-line divisor Riemann--Roch calculation at its first use. This is the same computation in A.5.2, now stated before the cohomology conclusion; the canonical-bundle evaluation construction is unchanged.', 'cdp:st:A.4.4')
replace(r'For completeness we also give the Inoue calculation, rather than assuming a generic-vanishing theorem for its cotangent bundle.',
        r'For an Inoue surface, we compute the same two local-system groups from its mapping-torus presentation.',
        'D02', 'The following mapping-torus maps, eigenvalues and exact cohomology sequence supply precisely this calculation; removed the imagined alternative proof.', 'cdp:st:A.4.9')
replace(r'No constancy of its complex surface type is needed for these maps.', '',
        'D02', 'The preceding displayed diffeomorphism pullback and local-system isomorphism prove the transport; removed the closing defensive sentence.', 'cdp:st:A.4.9')
replace(r'This completes the degree-one calculation for every surface type in \ref{cdp:st:C.3.1}.', '',
        'D08', 'The preceding case calculations already prove the stated groups; removed the closing recapitulation.', 'cdp:st:A.4.9')
replace(r'This proves the statement of Proposition~7.3. The invalid genus-two deduction in its printed proof remains refuted by \ref{cdp:st:A.4.2}; the proof above replaces that argument through the explicit maps (A.20)--\eqref{cdp:eq:A.24}.', '',
        'D01', 'The exact published genus-one counterexample remains in A.4.2, and the proposition states its conclusion in full. Removed the closing recapitulation and retrospective wording.', 'cdp:st:A.4.9')

# Plain mathematical verbs preserve the displayed objects and maps.
for old, new in [
    ('the actual Picard family', 'the Picard family'),
    ('these actual maps', 'these maps'),
    ('an actual diffeomorphism', 'a diffeomorphism'),
    ('the actual local-system isomorphism', 'the local-system isomorphism'),
    ('Take the transgression section supplied by', 'Take the transgression section of'),
]:
    if old in working:
        replace(old, new, 'D08', 'The same explicitly defined map, family or section is retained; removed workflow emphasis.', count=working.count(old))
for label in ['cdp:st:B1','cdp:st:B2']:
    old = 'Statement \\ref{' + label + '}'
    if old in working:
        replace(old, '\\cref{' + label + '}', 'D04', 'The reference now prints the actual statement kind and current number from its unchanged label.', count=working.count(old))

# Reorder whole blocks only.  Every proof remains with its owner.
env_pat = re.compile(r'^\\begin\{(?:definition|proposition|theorem|lemma|corollary|cited|remark|example)\}', re.M)
matches = list(env_pat.finditer(working))
heading = working[:matches[0].start()].strip() + '\n\n'
blocks = {}
for i,m in enumerate(matches):
    text = working[m.start():matches[i+1].start() if i+1 < len(matches) else len(working)].strip() + '\n\n'
    ident = re.search(r'\\StatementRecord\{([^{}]+)\}', text).group(1)
    assert ident not in blocks, ident
    blocks[ident] = text
groups = [
 ('Conormal filtration and the Jacobian fractional ideal', 'cotangent-filtration', ['def:II:conormal-data','cdp:st:A.1.1','cdp:st:A.2.1','cdp:st:A.2.2','cdp:st:A.1.2']),
 ('Residue poles and singular critical curves', 'cotangent-residues', ['cdp:st:A.2.4','cdp:st:A.2.5','cdp:st:A.2.6']),
 ('Nodal families and the endpoint groups', 'cotangent-nodal', ['cdp:st:B1','cdp:st:B2','cdp:st:B3']),
 ('Unitary twists on reduced fibre supports', 'cotangent-unitary', ['cdp:st:A.4.2','cdp:st:A.4.7','cdp:st:A.4.8','cdp:st:A.4.9']),
 ('Multiple and reducible fibres', 'cotangent-multiple', ['cdp:st:A.3.1','cdp:st:A.3.2','cdp:st:A.3.3','rem:II:thickening-endpoint','cdp:st:A.3.4','cdp:st:A.3.5']),
 ('Irreducible normal-crossings fibres', 'cotangent-normal-crossings', ['cdp:st:A.4.1','cdp:st:A.4.3','cdp:st:A.4.4','cdp:st:A.4.5','cdp:st:A.4.6']),
]
assert sorted(blocks) == sorted(x for _,_,ids in groups for x in ids)
pieces = [heading]
owner_units = {}
for title, slug, ids in groups:
    pieces.append('\\subsection{'+title+'}\\label{subsec:II:'+slug+'}\n\n')
    for ident in ids:
        owner_units[ident] = slug
        pieces.append(blocks[ident])
        new_header=blocks[ident].split('\n\n',1)[0]
        old_header=new_header if new_header in original else ''
        log('D14', old_header, new_header,
            'Moved the complete labelled statement and its complete proof together. The unitary local-system construction precedes its smooth-multiple-fibre application; the conormal calculation precedes the examples and all applications.', ident)
        rows[-1]['new_location']='subsec:II:'+slug+'; position '+str(ids.index(ident)+1)
working = ''.join(pieces)

# Equation numbering.  Exact existing identities are retained, and historical
# aliases continue to point at the same mathematical display.
tag_rows = []
known_map = {}
with (ROOT / 'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    for row in csv.DictReader(f, delimiter='\t'):
        if row['old_tag']:
            known_map[row['old_tag']] = row['target_label']

def convert_bracket(m):
    block = m.group(0)
    tags = re.findall(r'\\tag\{([^{}]+)\}', block)
    if not tags:
        return block
    assert len(tags) == 1
    tag = tags[0]
    labels = re.findall(r'\\label\{([^{}]+)\}', block)
    label = labels[0] if labels else known_map.get(tag, 'eq:II:manual:'+tag)
    assert tag not in {r['old_tag'] for r in tag_rows}
    new = block.replace(r'\[',r'\begin{equation}',1)
    new = new[:-2] + r'\end{equation}'
    new = new.replace(r'\tag{'+tag+'}', '' if labels else r'\label{'+label+'}')
    ident = owner_at(working,m.start())
    tag_rows.append(dict(old_tag=tag,target_label=label,statement_id=ident))
    log('D19',block,new,'Changed the numbering wrapper only; the mathematical display, existing labels and targets are retained. The label gives the exact old-to-new equation identity.',ident)
    return new

working = re.sub(r'\\\[.*?\\\]',convert_bracket,working,flags=re.S)
for m in list(re.finditer(r'\\tag\{([^{}]+)\}',working))[::-1]:
    tag=m.group(1)
    lo=working.rfind(r'\begin{',0,m.start())
    hi=working.find(r'\end{',m.end())
    context=working[lo:hi]
    labels=re.findall(r'\\label\{([^{}]+)\}',context)
    assert labels and r'\begin{multline}' in context, (tag,context[:80])
    label=labels[0]
    ident=owner_at(working,m.start())
    tag_rows.append(dict(old_tag=tag,target_label=label,statement_id=ident))
    log('D19',m.group(),'', 'The multline environment already uses the equation counter; removed only its manual tag.',ident)
    working=working[:m.start()]+working[m.end():]

all_map = known_map | {r['old_tag']:r['target_label'] for r in tag_rows}
for tag,label in sorted(all_map.items(),key=lambda x:len(x[0]),reverse=True):
    if not re.fullmatch(r'[A-Za-z0-9.]+',tag):
        continue
    old='('+tag+')'
    # This unit has no one-letter equation citations; parenthesized A, B, etc.
    # are mathematical arguments and are intentionally untouched.
    if len(tag)==1 or old not in working:
        continue
    replace(old,r'\eqref{'+label+'}','D19','Replaced a prose citation of the old equation number by the same equation label.',count=working.count(old))

# Remove one-item enumerations, keeping their proof text verbatim.
def single_item(m):
    block=m.group()
    if len(re.findall(r'\\item\b',block))!=1:
        return block
    new=re.sub(r'^\\begin\{enumerate\}\[label=\\arabic\*\.,leftmargin=\*\]\s*\\item\s*','',block)
    new=re.sub(r'\s*\\end\{enumerate\}$','',new)
    ident=owner_at(working,m.start())
    log('D23',block,new,'The proof has one paragraph; removed its vacuous item number without changing the paragraph.',ident)
    return new
working=re.sub(r'\\begin\{enumerate\}\[label=\\arabic\*\.,leftmargin=\*\].*?\\end\{enumerate\}',single_item,working,flags=re.S)

assert not re.search(r'\\tag\{',working)
old_labels=set(re.findall(r'\\label\{([^{}]+)\}',original))
new_labels=set(re.findall(r'\\label\{([^{}]+)\}',working))
assert old_labels <= new_labels, old_labels-new_labels
old_targets=set(re.findall(r'\\hypertarget\{([^{}]+)\}',original))
new_targets=set(re.findall(r'\\hypertarget\{([^{}]+)\}',working))
assert old_targets <= new_targets,old_targets-new_targets
assert new_targets-old_targets == {'tag-P221'}
assert working.count(r'\begin{proof}') == working.count(r'\end{proof}') == original.count(r'\begin{proof}')

OUT.mkdir(parents=True,exist_ok=True)
def write_tsv(name,fields,data):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(data)

(OUT/(PRE+'_replacement.tex')).write_text(working,newline='\n')
with (ROOT/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:
    defect_fields=next(csv.reader(f,delimiter='\t'))
write_tsv(PRE+'_defects.tsv',defect_fields,rows)
write_tsv(PRE+'_equations.tsv',['old_tag','target_label','statement_id'],tag_rows)

now=datetime.now(timezone.utc)
with (ROOT/'CHECK_EVENTS.tsv').open() as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
events=[]
event_owners=[x for _,_,ids in groups for x in ids]
for alias in ['wbII:lem:gluing-bundle','wbII:lem:extending-gluing','wbII:rem:scope']:
    owner_units[alias]='cotangent-nodal'
    event_owners.append(alias)
for ident in event_owners:
    row={k:'' for k in event_fields}
    row.update(statement_id=ident,date=now.date().isoformat(),date_utc=now.isoformat(),
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',
        type='used and rechecked in this run',
        outcome='Read the complete cp35 statement/proof and compared the receiving text. Preserved hypotheses, conclusions, explicit sheaf and cohomology maps; the recorded citation replacements use the exact primary loci. Equation wrappers now use section numbering; all original labels and targets survive. This is an exposed editorial rereading, not an independent reproof or computation.',
        event_id='publish:c3:conductor01:'+ident,phase='publication editorial comparison',
        source_file='agents/continuation3_conductor/'+PRE+'_replacement.tex',
        source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor01:'+owner_units[ident],
        where='subsec:II:'+owner_units[ident])
    events.append(row)
write_tsv(PRE+'_CHECK_EVENTS.tsv',event_fields,events)

status=[]
for title,slug,ids in groups:
    for n in range(1,26):
        state='done'
        reason='Complete unit read against this defect class; all identified instances are logged in the unit defect rows.'
        if n==18:
            state='open'
            reason='Exact new Granger--Schulze and AC26 locators checked; complete paper bibliography form and all inherited primary locators await the common bibliography pass.'
        if n==23:
            state='open'
            reason='Empty item and one-item enumerations corrected; integrated typesetting and page reading remain open.'
        status.append(dict(unit='subsec:II:'+slug,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit='subsec:II:'+slug,criterion='structure',status='done',reason='Complete statement/proof owners grouped by their mathematical use; the unitary construction now precedes the multiple-fibre application. External construction inputs remain their earlier labelled owners.'))
write_tsv(PRE+'_unit_status.tsv',['unit','criterion','status','reason'],status)

print('Prepared cotangent replacement:',len(original),'->',len(working),'characters')
print('Defect instances:',len(rows),'; exposed rereading rows:',len(events),'; equation identities:',len(tag_rows))
print('New permanent tag: P221. All old labels and targets retained.')
print('Open: inherited bibliography locator/form pass, integrated typesetting, final rendered-page reading.')
