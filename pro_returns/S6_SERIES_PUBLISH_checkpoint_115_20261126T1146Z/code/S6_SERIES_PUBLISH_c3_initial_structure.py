"""Place the complete cotangent criterion before the extended sign analysis.

The moves preserve every statement and proof byte. Section breaks follow
existing mathematical units; they create no subdivision completion credit.
"""
from S6_SERIES_PUBLISH_c3_edit import *

before = SOURCE.read_text()
after = before
changes = []

def record(key, types, statement, old_location, new_location, old, new, reason):
    for i, kind in enumerate(types, 1):
        changes.append(dict(change_id=f'{key}-{i:02}', type=kind,
            statement_id=statement, old_location=old_location,
            old_page='800-page working PDF before this structure pass',
            new_location=new_location, new_page='integrated build pending',
            old_text=old, new_text=new, reason=reason,
            review_status='Root read the complete moved statements and proofs and compared their exact bytes; the section changes add no mathematical premise or conclusion. Existing subsection identities and their open global gates remain.'))

start = before.index(r'\subsection{Global cohomology tests}')
end = before.index(r'\subsection{Hexagonal fibres and normalization cohomology}', start)
criterion = before[start:end]
boundary = before.index(r'\section{Irreducible supports: topology, conductor and equality}')
labels = {m[1]:m.start() for m in re.finditer(r'\\label\{([^}]+)\}', before)}
references = set()
for m in re.finditer(r'\\(?:[Cc]ref|[Ee]qref|ref|SeriesRef)\*?\{([^}]+)\}', criterion):
    references.update(x.strip() for x in m[1].split(','))
late = [r for r in references if r in labels and labels[r] > boundary and not start <= labels[r] < end]
assert not late, late
assert after.count(criterion) == 1
after = after.replace(criterion, '', 1)
new_heading = r'\section{The global normalization criterion}\label{sec:II:global-normalization-criterion}' + '\n\n'
anchor = r'\section{Irreducible supports: topology, conductor and equality}'
assert after.count(anchor) == 1
after = after.replace(anchor, new_heading + criterion + anchor, 1)
record('II-C3-STRUCTURE-GLOBAL-CRITERION', ['D14'],
       'cdp:st:C4c;cdp:st:C4a;cdp:st:C4b;cdp:st:C4d;lem:II:persistent-normalization-pullback;cdp:st:C4e;cdp:st:C4f',
       'Tangent cohomology, first two subsections, formerly after the 141-page irreducible-sign section',
       'The global normalization criterion, immediately after the normalization and local-conductor inputs',
       criterion, new_heading + criterion,
       'Move the complete finite cohomology tests and normalization criterion to their first available position. Every current-paper reference is already before the new boundary or inside the moved block. The body proof of the headline criterion no longer follows the long irreducible-sign development.')

start = before.index(r'\section{Direct images and divisor vanishing}')
end = before.index(r'\section{Canonical pencils in smooth specializations}', start)
direct = before[start:end]
assert after.count(direct) == 1
assert not re.search(r'\\(?:[Cc]ref|[Ee]qref|ref|SeriesRef)\*?\{', direct)
after = after.replace(direct, '', 1)
anchor = r'\section{Integral specialization, coherent restrictions and component counts}'
assert after.count(anchor) == 1
after = after.replace(anchor, direct + anchor, 1)
record('II-C3-STRUCTURE-DIRECT-IMAGES', ['D14'],
       'sec:II:direct-image-comparisons',
       'After the period-rank section, formerly working pages 333--335',
       'After the index and Picard-component section', direct, direct,
       'The complete self-contained direct-image/divisor section has no internal forward premise. Moving its unchanged statements and proofs places the explicit CDP98 corrections beside the initial index/Picard discussion and before their later canonical-pencil use.')

def change_heading(old, new, key, reason):
    global after
    assert after.count(old) == 1, key
    after = after.replace(old, new, 1)
    record(key, ['D14'], 'II', old, new, old, new, reason)

change_heading(r'\section{Index, Picard components and endpoint cohomology}',
    r'\part{Cotangent obstructions and fibre geometry}\label{part:II:cotangent-fibre-geometry}' + '\n\n' +
    r'\section{Index, Picard components and endpoint cohomology}',
    'II-C3-STRUCTURE-COTANGENT-PART',
    'Give the initial body its own mathematical part, containing the index/Picard, direct-image, smooth-fibre, cotangent, normalization and global-criterion arguments.')

change_heading(r'\section{Normalization, conductor genus and local torus exclusions}',
    r'\section{Normalization, Picard twists and ruled surfaces}',
    'II-C3-STRUCTURE-NORMALIZATION-TITLE',
    'The first group contains duality, persistent Picard twists and ruled-normalization genus. The remaining local exclusions receive their own sections at existing subsection boundaries.')

breaks = [
    ('Conductor jets and the genus bound', 'Conductor jets and binomial torus exclusions', 'sec:II:conductor-binomial-exclusions'),
    ('Binary products and cubic jets', 'Plane-curve conductors and rational boundary complements', 'sec:II:plane-conductor-boundaries'),
    ('Ordinary double curves and normal surface alternatives', 'Double curves and normalization models', 'sec:II:double-curve-normalizations'),
    ('Conductor curves at ruled Euler equality', 'Ruled Euler equality and its conductor', 'sec:II:ruled-euler-equality'),
    ('Conductor graphs and rational Euler numbers', 'Local exclusions and uniform transverse types', 'sec:II:uniform-transverse-types'),
    ('Further uniform transverse sectors', 'Tacnodal conductor sectors', 'sec:II:tacnodal-conductor-sectors'),
    ('The horizontal image in the unrestricted ruled remainder', 'Contracted sections and cubic spectral covers', 'sec:II:contracted-cubic-covers'),
    ('The conductor graph and the horizontal spectral cover', 'Conductor junctions and the irreducible classification', 'sec:II:irreducible-conductor-junctions'),
]
for i, (subsection, title, label) in enumerate(breaks, 1):
    old = r'\subsection{' + subsection + '}'
    new = r'\section{' + title + r'}\label{' + label + '}' + '\n\n' + old
    change_heading(old, new, f'II-C3-STRUCTURE-SECTION-{i:02}',
        'Insert a descriptive section boundary at an existing fully reviewed mathematical subsection. The previous 57-page normalization section and 141-page irreducible section become coherent groups of roughly 13--26 working pages. All original subsections, statements, proofs, labels and their order within each group remain unchanged. Final spans will be checked in the integrated PDF.')

change_heading(r'\section{Irreducible supports: topology, conductor and equality}',
    r'\part{Irreducible supports and Euler equality}\label{part:II:irreducible-euler}' + '\n\n' +
    r'\section{Irreducible supports: topology and canonical orders}',
    'II-C3-STRUCTURE-IRREDUCIBLE-PART',
    'Give the complete irreducible-support analysis its own part and name its initial topology/canonical-order group. The standing setting remains the same numbered definition immediately below.')

change_heading(r'\section{Tangent cohomology, normalization restrictions and resonance}',
    r'\section{Twisted tangent cohomology of the marked families}',
    'II-C3-STRUCTURE-TWISTED-TITLE',
    'After moving the global criterion, the existing section contains hexagonal-fibre comparisons, normalization-map cohomology and integral/nonintegral Picard resonance for the marked families.')

old_intro = '''The Euler-sign theorem determines the global topological
constraint on the fibrations considered here. We next study
their coherent cohomology and variation: fixed-fibre sections
and normalization maps, period extension under trivial
monodromy, resonance of Picard twists, and local deformation
spaces. These computations identify the cohomological
mechanisms of the constructed families and the hypotheses
needed for their direct-image comparisons.'''
new_intro = r'''The marked periods determine the Picard resonance loci and
Kodaira--Spencer maps of the constructed torus fibrations.
The fibrewise cup products and normalization maps relate
their coherent cohomology to fibration stability and local
deformation spaces. The source, period and affine attachment
conventions are those of \cref{def:II:marked-conventions}.'''
assert after.count(old_intro) == 1
after = after.replace(old_intro, new_intro, 1)
record('II-C3-STRUCTURE-PERIOD-SCOPE', ['D15','D24'],
       'part:II:periods-tangent-deformations', 'Periods part introduction',
       'Periods part introduction after the criterion/direct-image moves',
       old_intro, new_intro,
       'State the mathematical scope of the remaining period/cohomology/deformation part. The global criterion and direct-image section now have earlier homes; their old placement is no longer described.')

preserve_identifiers(before, after)
for old, new in zip(identifiers(before), identifiers(after)):
    assert all(new[k] == v for k, v in old.items())
    assert all(new[k] == 1 for k in new - old)
assert after.count(criterion) == 1 and after.count(direct) == 1
SOURCE.write_text(after, newline='\n')
print('Defect rows', append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', changes, 'change_id'))
add_event('II', 'II-C3-INITIAL-STRUCTURE-PLACEMENT', 'used and rechecked in this run',
          'Root read the complete 474-line global-cohomology/normalization-criterion block and 297-line direct-image/divisor section before their move, including all proofs. Their bytes are preserved exactly. Every current-paper reference of the criterion resolves before its new position or inside the moved block; the direct-image section has no current-paper reference. The prior 57/141-page sections are divided at eight existing mathematical subsection boundaries, retaining every old label/target and the subsection unit identities. Two part headings and descriptive section titles organize the same material. The periods introduction now describes its remaining mathematics. Final integrated page spans, whole-paper dependencies, first-part reconciliation and all final-page rows remain open. No independent check, required-check increment or subdivision movement credit.',
          'Initial cotangent/normalization part; irreducible-support part; bounded periods part introduction', source=__file__)
print('Complete criterion and direct-image blocks moved byte-for-byte; eight section boundaries and two part headings inserted.')
