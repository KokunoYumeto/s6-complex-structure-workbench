#!/usr/bin/env python3
"""Bounded publication edits after whole readings of both OS49 fragments."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import difflib
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation8_iii_later'
LATER = ROOT / 'agents/continuation8_iii_integration/units/later'
paths = {key: LATER / (key + '.tex') for key in ('os49_construction','os49_graph_caps')}
old = {key: path.read_text() for key, path in paths.items()}
assert sha256(old['os49_construction'].encode()).hexdigest() == 'c1ee6e77847b8bf87ebee4cc24568e543ebea2b92012b092a5c65c6a888e52bc'
assert sha256(old['os49_graph_caps'].encode()).hexdigest() == 'abb1d60838515c1f2890c113b44ec528d6da3a9ab979fb86fee46d841ac8aa77'
new = dict(old)
rows = {key: [] for key in paths}
fields = ['change_id','type','statement_id','old_location','old_page','new_location',
          'new_page','old_text','new_text','reason','review_status']

def owner(text, pos):
    found = list(re.finditer(r'\\label\{(night:P3F\.[0-9]+)\}', text[:pos+1]))
    return found[-1][1] if found else 'sec:III:os49-night'

def record(key, kind, before, after, reason, pos, sid=None):
    rows[key].append(dict(change_id=f'c8-III-{key}-{len(rows[key])+1:03}', type=kind,
        statement_id=sid or owner(new[key],pos),
        old_location=key + '.tex sequential edit line ' + str(new[key][:pos].count('\n')+1),
        old_page='pending final page concordance', new_location='same retained result or recorded exact relocation',
        new_page='pending final build', old_text=before, new_text=after, reason=reason,
        review_status='whole repaired source and complete available admitted comparisons read; final readback pending'))

def change(key, before, after, kind, reason, count=1, sid=None):
    assert new[key].count(before) == count, (key,before,new[key].count(before),count)
    for match in re.finditer(re.escape(before), new[key]):
        record(key,kind,before,after,reason,match.start(),sid)
    new[key] = new[key].replace(before,after)

C, G = 'os49_construction','os49_graph_caps'
change(C, 'The OS49 construction and every free affine cap', 'The OS49 family', 'D16',
       'Use a mathematical section title for the source, periods, page and cap calculations that follow.')
intro = ('We retain the explicit marked construction and its complete integral cap calculation. The coprime statement '
         '\\cref{maps:src:D.2.11} is extended in \\cref{night:P3F.34}; its printed coprimality hypothesis remains part of its scope.\n\n')
change(C,intro,'','D01','Remove the production-facing retention sentence and duplicate forward scope pointer; all coprime and free-cap hypotheses remain in their mathematical statements.')
titles = [
    ('02S2','26','An explicit sphere filling','An explicit OS49 sphere'),
    ('02S3','27','The angular clutch','Angular clutch for the OS49 family'),
    ('02S4','28','Iterates of the section line','Section-line iterates and direct images'),
    ('02S5','29','Coprime finite caps','Integral topology of coprime OS49 caps'),
]
for tag, num, subsection, title in titles:
    existing = ('\\begin{theorem}[Angular clutch for the OS49 family]' if tag == '02S3' else '\\begin{theorem}')
    marker = existing + '\\hypertarget{tag-' + tag + '}{}'
    replacement = '\\subsection{' + subsection + '}\n\\begin{theorem}[' + title + ']\\hypertarget{tag-' + tag + '}{}'
    change(C,marker,replacement,'D14','Create a genuine subsection with one mathematical statement and its complete existing proof.',sid='night:P3F.'+num)

change(C,'The explicit $IV^*+II+I_2$ source with $M=\\mathcal O(G-O)$ and $Q=3G$ has component-supported linearization divisor $C_0$. Its specified local fillings and order-three cap give a simply connected integral homology six-sphere, hence the standard smooth $S^6$.',
       'The explicit $IV^*+II+I_2$ source with $M=\\mathcal O(G-O)$ and $Q=3G$ has component-supported linearization divisor $C_0$. Its original type-$II$ filling, specified full-lattice toric filling at $I_2$ and order-three affine cap give a simply connected integral homology six-sphere, hence the standard smooth $S^6$.',
       'D20','Name the three exact fillings already constructed in the sole proof; the input family and all attaching maps are unchanged.',sid='night:P3F.26')

phase_start = new[C].index('The raw suspension class satisfies')
phase_end = new[C].index('\nThe positive-fan return index zero', phase_start)
phase_old = new[C][phase_start:phase_end]
change(C,phase_old,'','D14','Move this auxiliary phase calculation to the existing graph-page proof after its incoming graph is defined; the exact new marking fixes psi and the quotient graph point.',sid='night:P3F.27')
route_start = new[C].index('The positive-fan return index zero')
route_end = new[C].index('\\end{proof}',route_start)
route_old = new[C][route_start:route_end]
change(C,route_old,'','D11','The positive return and negative-fan comparison already have their single full statement/proof in P3F.31--32 and their specified Paper-IV destination; remove only this repeated routing overview.',sid='night:P3F.27')
phase_new = r'''The suspension class satisfies
\(\psi(H_*)=-1\) and \(\psi(K_*)=2\).
The displayed change of marking fixes \(\psi\), with its inverse
fixing the same covector. On the incoming graph its phase is
\(-h_*+2g_\epsilon(p)\). Its restriction to the \(H_*\)-circle
has degree \(-1\), and therefore takes every phase.
'''
graph_anchor = 'The incoming graph is\n\\(\\tau_*=g_\\epsilon(p)\\).\n'
change(G,graph_anchor,graph_anchor+phase_new,'D14','Place the complete suspension-phase argument at its defined incoming graph; old/new phase coordinates are transported by the displayed L and L inverse, both fixing psi.',sid='night:P3F.31')
change(G,'\\end{gathered}\nThe graph cutoff is flat at zero',
       '\\end{gathered}\n\\]\nThe graph cutoff is flat at zero','D23',
       'Close the actual open display after the graph/outer-trace/normal-quotient formulas. This is the missing display closer identified by root and confirmed in the whole source read.',sid='night:P3F.31')

old_s4 = ('The actual OS49 linearization gives the exact sequence $0\\to T^*M\\to M\\to\\mathcal O_{C_0}(-1)\\to0$. '
          'Its iterates alternate the two components, and all the translated source-line direct images vanish. '
          'The direct mixed-circle symbol comparison remains an auxiliary route. The actual positive-fan index is computed in P3F.31--32, and P3K.65 computes the corrected negative-fan sphere class by the native Cox arrow.')
new_s4 = ('The OS49 linearization gives the exact sequence\n'
          '$0\\to T^*M\\to M\\to\\mathcal O_{C_0}(-1)\\to0$.\n'
          'Its iterates alternate the two components, and\n'
          '$R\\pi_*(T^{j*}M)=0$ for every $j\\in\\mathbb Z$.\n'
          'On the compact degree-three regular-binding model constructed in the proof,\n'
          'the section line $M\' =\\mathcal O(G\'-O\')$ and its translate\n'
          '$T\'^*M\'=M\'(-\\sum_i C_{0,i})$ both have square $-2$\n'
          'and zero derived direct image.')
change(C,old_s4,new_s4,'D13','State the complete sheaf and compact-model conclusions actually proved here; remove the duplicate route commentary, retaining the full common-resolution correction and all translated maps.',sid='night:P3F.28')
closing = ('This proves the stated sheaf and iterate assertions, including the\n'
           'specified compact auxiliary pullback and its modification.\n'
           'The return-index applications use the graph page, normal line and\n'
           'boundary identifications in \\SeriesRef{night:P3F.31} and\n'
           '\\SeriesRef{night:P3F.32}; \\SeriesRef{night:P3K.65} gives the native\n'
           'negative-fan comparison with its specified closing and orientation.\n')
change(C,closing,'','D11','The completed direct-image calculation closes the proof. Its applications occur with their full page/normal construction in the following subsections; no auxiliary mathematical calculation is removed.',sid='night:P3F.28')

edits = [
 ('Here is an explicit period marking of this source.','Choose the following period marking of this source.','D08','State the period choice directly, retaining its complete modular and source comparison.'),
 ('Poincare','Poincar\\\'e','D23','Typeset the name consistently with the mathematical citation.'),
 ('In particular it fixes both reduced meridians\nand leaves no unrecorded translation in the exterior attachment.',
  'These extending representatives fix both reduced meridians\nand the exterior attachment.','D02','Use the explicitly constructed section and inverse iterate as the affirmative attachment statement.'),
 ('specialization has the complete images above, without torsion\nkernel.',
  'specialization is injective with the complete images above.','D02','State the proved full-lattice injection directly; the cyclic-cell computation and its free source remain.'),
 ('We also fix the possible intrinsic differential before computing\nthe translation contribution.',
  'The intrinsic differential is determined by the following auxiliary filling.','D08','Introduce the actual coarse-cap comparison by its mathematical purpose.'),
 ('There are no higher differentials\nor extension ambiguities, so',
  'The two-dimensional base permits only these differentials, and\neach surviving total-degree filtration has one term. Hence','D22','Give the base dimension and filtration reason for the already proved absence of a higher differential or extension.'),
 ('For completeness, the physical unit circle is semifree on this','The physical unit circle is semifree on this','D08','State the retained circle assertion directly.'),
 ('Here are complete integral maps for the preceding calculation.  Columns use',
  'The following integral maps give the parabolic calculation. Columns use','D08','Name the exact displayed contractions without proof-process narration.'),
 ('No image is saturated.','The middle groups use the exact image lattices.','D02','Retain the nonsaturation requirement positively; the displayed image sections prove equality with those lattices.'),
 ('Use the admitted homology marking','Use the homology marking of \\SeriesRef{night:P3F.26}','D07','Remove admission language from the mathematical proof; cite the preceding marked construction.'),
 ('For the raw logarithmic point','For the logarithmic point','D08','Use the actual coordinate name without a work-record qualifier.'),
 ('This last identity\nuses the actual moving period lattice, rather than silently\nidentifying it with the starting lattice.',
  'This identity uses the moving period \\(K(s,v+\\theta)\\).','D02','Retain the precise moving endpoint from the displayed equation.'),
 ('There is therefore no remaining torsion stalk at a singular fibre,\nand \\(R\\pi_*M=0\\).',
  'The connecting map has zero kernel and cokernel at every fibre,\nso \\(R\\pi_*M=0\\).','D02','State the exact scalar-isomorphism consequence on all fibres.'),
 ('Cech','\\v{C}ech','D23','Typeset the name in the exact cochain-map paragraph.'),
 ('The auxiliary compact model in the comparison is specified as\nfollows.  For a regular binding value',
  'For a regular binding value','D08','Introduce the auxiliary compact model as a mathematical construction.'),
 ('Here is the exact comparison with the ordinary degree-three\npullback of \\(M\\).',
  'Compare this line with the ordinary degree-three\npullback of \\(M\\) on the following common resolution.','D08','Name the morphism where its full Cartier correction is computed.'),
 ('these maps give the exact requested\nattachment','these maps give the marked\nattachment','D05','Remove a reference to an external request while retaining the exact overlap maps.'),
 ('In the original notation this is the explicit change','In the boundary basis the explicit change is','D08','Keep both coordinate identifications without historical wording.'),
 ('Hence all four cokernels are cyclic, of orders \\((m,k,k,m)\\).',
  'Hence all four cokernels are cyclic.','D11','The same index tuple remains in its retained displayed equation below; remove only its immediately repeated inline copy.'),
]
for before, after, kind, reason in edits:
    count = new[C].count(before)
    assert count > 0, before
    change(C,before,after,kind,reason,count=count)

equations = [
 ('P3F.26.1','Q303','os49:eq:source-cubic'),
 ('P3F.26.3','Q304','os49:eq:cohomology-monodromy'),
 ('P3F.26.2','Q305','os49:eq:cusp-deck'),
 ('P3F.27.1','Q306','os49:eq:primitive-periods'),
 ('P3F.27.2','Q307','os49:eq:full-cusp-periods'),
 ('P3F.28.2','Q308','os49:eq:one-step-line'),
 ('P3F.28.1','Q309','os49:eq:two-step-line'),
 ('P3F.28.3','Q30A','os49:eq:translated-direct-images'),
 ('P3F.29.1','Q30B','os49:eq:coprime-cap-vector'),
 ('P3F.29.3','Q30C','os49:eq:coprime-specialization-indices'),
 ('P3F.29.2','Q30D','os49:eq:coprime-homology'),
]
for token, tag, label in equations:
    before = '\\tag{' + token + '}'
    after = before + '\\hypertarget{tag-' + tag + '}{}\\label{' + label + '}'
    change(C,before,after,'D19','Give the previously manual-only equation a descriptive permanent label and small-tag anchor before converting its counter. The exact former token is retained in the alias table.')

headers, changes, issues = presentation.statement_records_to_small_tags(new[C])
assert not issues, issues
for item in changes:
    record(C,item.kind,item.old,item.new,item.reason,item.start,item.statement_label)
new[C] = headers
change(C,r'\textnormal{\small tag 02S3.}',r'{\normalfont\scriptsize tag 02S3}\par','D10','Use the common small-tag form for the existing statement identity.',sid='night:P3F.27')
numbered, changes, issues, aliases = presentation.remove_manual_equation_tags(new[C])
assert not issues, issues
for item in changes:
    record(C,item.kind,item.old,item.new,item.reason,item.start)
new[C] = numbered
unresolved = presentation.unresolved_literal_equation_references(new[C], aliases)
assert not unresolved, unresolved
units.check_permanent_identifiers(old[C],new[C],
    allowed_labels=[row[2] for row in equations], allowed_targets=['tag-'+row[1] for row in equations])
units.check_permanent_identifiers(old[G],new[G])
assert new[C].count('\\begin{proof}') == new[C].count('\\end{proof}') == 4
assert new[C].count('\\subsection{') == 4
assert new[G].count('\\begin{proof}') == new[G].count('\\end{proof}') == 4

for key in paths:
    paths[key].write_text(new[key])
    diff_path = OUT / ('S6_SERIES_PUBLISH_III_' + key + '_publication_v002.diff')
    diff_path.write_text(''.join(difflib.unified_diff(old[key].splitlines(True),new[key].splitlines(True),
                                                   fromfile=key+'_input',tofile=key+'_v002')))
    table = OUT / ('S6_SERIES_PUBLISH_III_' + key + '_publication_defects.tsv')
    assert not table.exists()
    with table.open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields,delimiter='\t',lineterminator='\n')
        writer.writeheader(); writer.writerows(rows[key])

alias_path = OUT / 'S6_SERIES_PUBLISH_III_os49_equation_aliases.tsv'
with alias_path.open('w',newline='') as handle:
    writer=csv.writer(handle,delimiter='\t',lineterminator='\n')
    writer.writerow(['old_printed_token','new_tag','new_label','source_file'])
    for token,tag,label in equations:
        writer.writerow([token,tag,label,str(paths[C].relative_to(ROOT))])

print('UTC',datetime.now(timezone.utc).isoformat())
for key in paths:
    print('OUTPUT',key,len(new[key].splitlines()),sha256(new[key].encode()).hexdigest(),'LOCAL_EDITS',len(rows[key]))
print('NEW_EQUATION_IDENTITIES',len(equations),'Q303--Q30D; OLD_IDENTIFIERS_PRESERVED')
print('PHASE_RELOCATION','P27_to_P31; L_fixes_psi; graph_point_and_inverse_retained')
print('GRAPH_D23_CLOSER_INSERTED; GRAPH_WHOLE_EDIT_REMAINS_PENDING; NO_SHARED_WRITES')
