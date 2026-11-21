#!/usr/bin/env python3
"""Bounded, guarded editorial pass over V's marked rank-six core."""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
original=(ROOT/'S6_SERIES_PUBLISH_V_core_original.tex').read_text()
text=original
paragraphs=re.split(r'\n\s*\n',original)
changes=[]

def location(s,at):
    labels=list(re.finditer(r'\\label\{((?:night:|maps:src:)[^}]+)\}',s[:at]))
    return labels[-1].group(1) if labels else 'part:marked-rank-six'

def change(old,new,kind,reason):
    global text
    if text.count(old)!=1:
        raise ValueError(f'Expected one match, got {text.count(old)}: {old[:180]}')
    at=text.index(old)
    changes.append(dict(type=kind,location=location(text,at),
        old_pdf_page='root to fill from corrected baseline',
        new_pdf_page='root to fill after final pagination',
        old_text=old,new_text=new,reason=reason))
    text=text.replace(old,new,1)

programs=[]
for m in re.finditer(r'\\texttt\{([^}]*\.py)\}',original):
    pre=original[max(0,m.start()-900):m.start()]
    u=re.search(r'\\href\{([^}]+)\}\{$',pre)
    programs.append(dict(filename=m.group(1).replace(r'\_','_'),
        location=location(original,m.start()),retained_url=u.group(1) if u else '',
        disposition='program table/check record; exact mathematical inputs, operation and results stay in the proof'))

edits=[
('This is also an integral certificate of the Smith assertion.',
 'This integral change of basis also proves the Smith assertion.', 'D08',
 'State the mathematical role of the displayed unimodular matrix.'),
('In its logarithmic central fibre, retain all arguments of the $x_j$',
 'In its logarithmic central fibre, use all arguments of the $x_j$', 'D08',
 'Describe the logarithmic phase coordinates directly.'),
('This proves the asserted failure of integral isomorphism and retains\n$j$ itself as the explicit rational isomorphism.',
 'Thus $j$ is the explicit rational isomorphism, and the determinant\nvaluation excludes an integral isomorphism.', 'D08',
 'Keep both proved conclusions and the exact obstruction; remove editorial wording.'),
('This supplies both integral arrows and retains the cup form',
 'These two integral maps preserve the cup form', 'D08',
 'Name the precise maps and the pairing they preserve.'),
('and the three stalk inclusions, so it retains their integral indices.',
 'and the three stalk inclusions, so it preserves their integral indices.',
 'D08','Describe the integral cellular morphism directly.'),
('Here are finite determinant certificates for its cohomology.  They\nuse precisely the ordered bases just given, so every matrix is\nspecified by the marked $M_i,S,C_i$ and exterior minors.',
 'We compute its cohomology by determinants in the ordered bases above.\nEvery matrix is specified by the marked $M_i,S,C_i$ and exterior minors.',
 'D08','Keep the reconstructible determinant calculation and all of its matrices.'),
('This supplies an integral isometry taking $p_1/2$ to $(1,1,1,1)$,\nand proves the claimed pair, not just its square.',
 'This gives an integral isometry taking $p_1/2$ to $(1,1,1,1)$.',
 'D02','Keep the proved integral morphism; remove the redundant comparison.'),
('matrix products and inverses retain those radii.  The order starts\nat $32$ and is increased by $16$ until $E_N<10^{-100}$.\nThere are $120$ steps for the zero meridian, $66$ for the infinity\nmeridian and $6$ for the open path, hence $192$ in total; the\nlargest order is $192$.',
 'matrix products and inverses propagate those radii. For each\nsegment, choose $N$ so that $E_N<10^{-100}$.',
 'D09','Keep the enclosure criterion; move implementation starting orders, increments and path-step counts to the record.'),
('matrix ball; the remaining equations are also checked to contain\nzero.  Their consistency is given by \\cref{night:P1.15}.',
 'matrix ball. Its consistency with the full system follows from\n\\cref{night:P1.15}.',
 'D09','Retain the exact existence/uniqueness justification and remove redundant numerical replay narration.'),
('\\Cref{night:P1.8} proves the existence and uniqueness of the full intersection;\nthe unused equation is checked with its interval radius retained.',
 '\\Cref{night:P1.8} proves the existence and uniqueness of the full\nintersection, so this subsystem encloses that intersection.',
 'D09','State the exact reason that the square subsystem encloses the required full-system solution.'),
('Existence of the exact intertwiner is supplied by',
 'Existence of the exact intertwiner follows from',
 'D08','Express the cited mathematical implication directly.'),
('\\item For completeness the ordinary/logarithmic comparison in this\ndegree is the exact residue resolution',
 '\\item The ordinary/logarithmic comparison in this degree is the\nexact residue resolution',
 'D08','Introduce the complete residue resolution directly.'),
('operator of $\\Omega_M^p$. No Kähler hypothesis occurs there.',
 'operator of $\\Omega_M^p$.',
 'D02','The preceding sentence already specifies the compact smooth complex manifold and the applicable operator.'),
]
for args in edits:change(*args)

# Complete verification narratives, kept verbatim in the before/after record.
def remove_tail(i,needle):
    p=paragraphs[i]
    old=p[p.index(needle):]
    change(old,'','D09','Move file names and replay scope to the program/check index; the preceding calculation is retained.')

remove_tail(10,'  The orders, characteristic polynomials, fixed-space dimensions,')
remove_tail(48,'  The discriminant, the nodal root and its transverse derivatives,')
change('They are checked over $\\mathbb Z$ in\n\\texttt{fourfolds\\_periods.py}.\n','',
       'D09','The preceding exact matrix products give the identities; move the replay reference.')

old=re.search(r'  The program \\href\{[^}]+reconstruct_V_cusp_06\.py\}\{\\texttt\{[^}]+\}\} enumerates all \$26\$ simplex classes and \$74\$ codimension-one incidences and computes these matrices exactly\.',text).group(0)
change(old,' There are $26$ simplex classes and $74$ codimension-one incidences;\nthe signed quotient formula above determines their integer matrices.',
       'D09','Retain the complete finite indexing set and its exact differential formula.')
old=re.search(r'The program \\href\{[^}]+reconstruct_V_cusp_06\.py\}\{\\texttt\{[^}]+\}\} constructs the induced maps\non integral cycle and quotient bases from the face projections and the\nPoincar\\\'e-dual Alexander--Whitney formula in step 9\.',text).group(0)
change(old,'On integral cycle and quotient bases, the face projections and the\nPoincar\\\'e-dual Alexander--Whitney formula in step~9 give the induced maps.',
       'D09','Keep the exact morphisms and bases underlying the integral collapse calculation.')
old=re.search(r' The invariant form, Picard--Lefschetz rank-one map,\nunimodular orbit matrix, integral inverse, reversal, based peripheral\nword and exterior-quotient identities are recomputed exactly in\n\\href\{[^}]+independent_V_markings_06\.py\}\{\\texttt\{[^}]+\}\}\.',text).group(0)
change(old,'','D09','Move the verification list; all displayed marking maps and their inverse remain.')
old=re.search(r' The polynomial reduction, all exact primitives, the horizontal\npolarization relation and all twenty-five quotient entries are reconstructed\nin \\href\{[^}]+independent_V_connection_spectra_06\.py\}\{\\texttt\{[^}]+\}\} and its JSON output\.',text).group(0)
change(old,'','D09','Keep the explicit polynomial reduction and quotient computation; move the program/output metadata.')
change(paragraphs[142],'\\end{enumerate}\n\\end{proof}',
       'D09','Move the two program names, library names, precision setting and replay statement into the records.')
old=re.search(r'The face incidences, unit Smith factors and the Alexander--Whitney\nproducts of the three coordinate cocycles are reconstructed in\n\\href\{[^}]+independent_V_analytic_06\.py\}\{\\texttt\{[^}]+\}\} and its JSON output\.\n',text).group(0)
change(old,'','D09','The quotient/face maps and exterior cup-product argument are retained; move the reconstruction reference.')
old=re.search(r'The full projected residue and both connecting determinants are\nrecomputed in \\href\{[^}]+independent_V_analytic_06\.py\}\{\\texttt\{[^}]+\}\}\.\nIts JSON output also records the root-line cohomology sums used below\.\n',text).group(0)
change(old,'','D09','Retain every residue entry, determinant and cohomology sum; move replay/output references.')
old=re.search(r'The exact Chern-number substitution and the resulting polynomial are\nverified in \\href\{[^}]+independent_V_analytic_06\.py\}\{\\texttt\{[^}]+\}\}\. It gives',text).group(0)
change(old,'The displayed polynomial gives','D09','The substitution and its polynomial are already printed in full.')
old=re.search(r'space \$\\mathbb QI\$, as recomputed in\n\\href\{[^}]+independent_V_extension_06\.py\}\{\\texttt\{[^}]+\}\}; their integral invertible',text).group(0)
change(old,'space $\\mathbb QI$ by rational row reduction. Their integral invertible',
       'D09','Keep the exact linear system, coefficient field and solution space in the proof.')
old=re.search(r'The norm-kernel ranks, primitive column bases, full identity\n\$\(B-I\)T=KZ\$ and Smith factors are recomputed exactly in\n\\href\{[^}]+independent_V_analytic_06\.py\}\{\\texttt\{[^}]+\}\}\.\n',text).group(0)
change(old,'','D09','The preceding primitive bases, full identity and Smith calculation remain verbatim.')
old=re.search(r'The exact anti-intertwiner equations, their one-dimensional rational\nsolution space, unimodularity of \$R\$, the based cusp block and the\nspecific ray obstruction below are recomputed in\n\\href\{[^}]+independent_V_markings_06\.py\}\{\\texttt\{[^}]+\}\} and its JSON output\.',text).group(0)
change(old,'','D09','Keep the exact anti-intertwiner matrix and proof; move its replay description.')

# Number the definitions and the cited comparison between proof blocks.
cohom=re.search(r'We keep the complex orientation[\s\S]*?and its reduced singular locus by \$D\$\.',text).group(0)
change(cohom,'\\begin{definition}[Root-orbifold notation]\\label{def:V:root-orbifold-notation}\n'+cohom.replace('We keep the complex orientation','Use the complex orientation')+'\n\\end{definition}',
       'D13','Number the root-curve, line-bundle and cusp notation; preserve all identities and their character justification.')
change('\\section{The boundary of the family}',
       '\\section{The boundary of the family}\n\n'
       '\\begin{definition}[Analytic extension at the parameter boundary]\\label{def:V:analytic-boundary-extension}',
       'D13','Number the analytic-extension definition without changing its hypotheses; guards leave the analytic agent free to update the parameter setup.')
change('and additional central components.',
       'and additional central components.\n\\end{definition}',
       'D13','Close the numbered analytic-extension definition before the cited deformation input.')
catanese=re.search(r'The stability of complex tori under deformation in the large is\nestablished in[\s\S]*?on the regular analytic open set used in the boundary argument\.',text).group(0)
change(catanese,'\\begin{remark}[Deformations of complex tori]\\label{rem:V:tori-deformations-input}\n'+catanese+'\n\\end{remark}',
       'D13','Number the known-source comparison between statements and retain its exact locator.')

before_labels=re.findall(r'\\label\{([^}]+)\}',original)
after_labels=re.findall(r'\\label\{([^}]+)\}',text)
assert set(before_labels)<=set(after_labels)
assert all(after_labels.count(x)==before_labels.count(x) for x in before_labels)
assert re.findall(r'\\hypertarget\{tag-[^}]+\}\{\}',original)==re.findall(r'\\hypertarget\{tag-[^}]+\}\{\}',text)
assert re.findall(r'\\tag\{[^}]+\}',original)==re.findall(r'\\tag\{[^}]+\}',text)
assert not re.search(r'\\texttt\{[^}]*\.py\}',text)
(ROOT/'S6_SERIES_PUBLISH_V_core_revised.tex').write_text(text)
(ROOT/'S6_SERIES_PUBLISH_V_core_replacements.json').write_text(json.dumps(changes,indent=2,ensure_ascii=False)+'\n')
for name,rows in [('S6_SERIES_PUBLISH_V_core_edits.tsv',changes),('S6_SERIES_PUBLISH_V_core_programs.tsv',programs)]:
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps(dict(edits=len(changes),program_mentions_moved=len(programs),
    original_labels_preserved=len(before_labels),new_numbered_labels=sorted(set(after_labels)-set(before_labels)),
    sha256=hashlib.sha256(text.encode()).hexdigest()),indent=2))
