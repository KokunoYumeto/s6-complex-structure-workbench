"""Give component geometry and compact occurrence readable section boundaries."""
from S6_SERIES_PUBLISH_c3_edit import *

before = SOURCE.read_text()
after = before
changes = []

def edit(old, new, key, reason, types=('D14',)):
    global after
    assert after.count(old) == 1, key
    after = after.replace(old, new, 1)
    for n, kind in enumerate(types, 1):
        changes.append(dict(change_id=f'{key}-{n:02}', type=kind,
            statement_id='II', old_location=old.splitlines()[0],
            old_page='804-page integrated working PDF', new_location=new.splitlines()[0],
            new_page='next integrated build', old_text=old, new_text=new, reason=reason,
            review_status='Root read the complete current contents and these mathematical boundaries. Statements, proofs and existing subsection identities are unchanged; no full-proof or subdivision completion credit.'))

old = r'''\part{The sign theorem for every degeneration}
This part studies the Euler topology and component geometry of torus
degenerations with arbitrary central supports. The global sign statements
use the setting of \cref{def:II:standing-torus-fibration}; the local
degenerations and comparison constructions have the hypotheses in their
statements. We begin with Euler parity and vertical modifications, then
study component covers, compact realizations and contractions.'''
new = r'''\part{Component geometry and Euler criteria}\label{part:II:component-geometry}
For a degeneration with arbitrary full central fibre, cyclic component
covers carry saturated translation fields, elliptic pencils and integral
monodromy maps. Their surface models and conductor curves determine the
local Euler contributions. The global sign statements use the setting
of \cref{def:II:standing-torus-fibration}; each local degeneration and
comparison construction has the hypotheses stated with its result.'''
edit(old, new, 'II-C3-STRUCTURE-COMPONENT-PART',
     'The component/criterion development receives its own part. The compact occurrence and canonical-reduction constructions below receive their own parts at unchanged mathematical boundaries.', ('D08','D14','D24'))
edit(r'\section{Unrestricted Euler topology and component covers}',
     r'\section{Euler topology and compact modifications}',
     'II-C3-STRUCTURE-EULER-MODIFICATIONS',
     'The first group contains parity, vertical modifications and compact torus fillings; component-field and lattice groups receive separate sections.')

breaks = [
    ('Cyclic component covers', 'Component covers and meromorphic fields', 'sec:II:component-field-geometry'),
    ('Cyclic quotients of two-tori', 'Cyclic quotients and minimal component models', 'sec:II:component-model-classification'),
    ('Integral component lattices and monodromy', 'Integral component lattices and support topology', 'sec:II:component-lattices-topology'),
    ('Secondary Kodaira components', 'Kodaira, Enriques and Kummer components', 'sec:II:kodaira-enriques-occurrence'),
    ('Elliptic torsors and Hopf components', 'Equivariant elliptic fillings and Hopf occurrence', 'sec:II:equivariant-hopf-occurrence'),
]
for n, (subsection, title, label) in enumerate(breaks, 1):
    old = r'\subsection{' + subsection + '}'
    new = r'\section{' + title + r'}\label{' + label + '}' + '\n\n' + old
    edit(old, new, f'II-C3-STRUCTURE-LATER-SECTION-{n:02}',
         'Insert a descriptive section break at an existing actual subsection. The former 77-page component section becomes four groups of about 9, 18, 26 and 24 working pages; the former 53-page occurrence section becomes groups of about 17, 12 and 24 pages. All existing proof and statement bytes remain in their order.')

old = r'\section{Semistable torus fillings}'
new = r'''\part{Compact occurrence and marked supports}\label{part:II:compact-occurrence}
The component classes above occur in compact torus fibrations through
polyhedral fillings, signed root fibrations and finite quotient maps.
Marked elliptic lattices and normal-line characters determine the
gluings of Hopf and ruled components. The constructions specify the
full fibre multiplicities, punctured families and component inclusions.

\section{Semistable torus fillings}'''
edit(old, new, 'II-C3-STRUCTURE-OCCURRENCE-PART',
     'Separate the complete realization and marked-support constructions from the preceding component classification, without changing their dependency order.', ('D14','D24'))
edit(r'\section{Compact occurrence of prescribed component classes}',
     r'\section{Signed roots and compact component constructions}',
     'II-C3-STRUCTURE-SIGNED-ROOT-TITLE',
     'Name the initial signed-root, elliptic-root, cuspidal-product and Kummer constructions; the later class-specific occurrence groups have their own sections.')

old = r'\section{Terminal contractions and canonical-flat fibres}'
new = r'''\part{Canonical reduction and the Euler sign}\label{part:II:canonical-reduction}
The divisor of a canonical evaluation form assigns an order to each
component. Boundary intersection equations and normal-line morphisms
control contractions, while cyclic roots compare these orders with full
fibre multiplicities. The resulting reductions determine the Euler
equality cases and the finite generation statements.

\section{Terminal contractions and canonical-flat fibres}'''
edit(old, new, 'II-C3-STRUCTURE-CANONICAL-PART',
     'Give the canonical-order, contraction and final Euler-sign chain its own mathematical part. Every preceding normal-product and component-classification input stays earlier.', ('D14','D24'))
edit(r'\part{Results not yet established}',
     r'\part{The remaining splitting problem}\label{part:II:remaining-splitting}',
     'II-C3-STRUCTURE-OPEN-PART',
     'Use the mathematical name of the single open problem in this final part; its complete stated scope and reduction remain unchanged.', ('D08','D14'))

preserve_identifiers(before, after)
for old, new in zip(identifiers(before), identifiers(after)):
    assert all(new[k] == v for k, v in old.items())
    assert all(new[k] == 1 for k in new - old)
# Every complete proof and numbered mathematical environment keeps its bytes.
proofs_before = re.findall(r'\\begin\{proof\}[\s\S]*?\\end\{proof\}', before)
proofs_after = re.findall(r'\\begin\{proof\}[\s\S]*?\\end\{proof\}', after)
assert proofs_before == proofs_after
SOURCE.write_text(after, newline='\n')
print('Defect rows', append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', changes, 'change_id'))
add_event('II', 'II-C3-LATER-STRUCTURE-PLACEMENT', 'used and rechecked in this run',
          'Root compared the 804-page contents and the exact mathematical boundaries. Five section breaks separate component fields, component classification, integral topology, Kodaira/Enriques occurrence and equivariant Hopf occurrence. Separate component, occurrence and canonical-reduction parts describe their existing chains; the final part is named for its single splitting problem. All complete proof blocks are byte-identical and every old identifier retains exact multiplicity. Original sec07/10/11 remainders remain open. This structural edit creates no proof-check, final-page or subdivision completion credit; final placement/dependency and front-matter gates remain pending.',
          'Component geometry, compact occurrence and canonical reduction', source=__file__)
print('Five section boundaries and mathematical part introductions integrated; proof bytes unchanged.')
