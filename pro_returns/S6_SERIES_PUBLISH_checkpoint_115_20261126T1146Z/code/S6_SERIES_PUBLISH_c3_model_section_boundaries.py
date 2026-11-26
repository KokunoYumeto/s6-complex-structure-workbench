"""Separate existing mathematical groups without changing their proof text."""
from S6_SERIES_PUBLISH_c3_edit import *

before = SOURCE.read_text()
changes = [
    (r'\section{Irreducible and reducible torus-fibre Euler criteria}',
     r'\section{Normal supports, class VII and contracted boundaries}',
     'EULER-SECTION-TITLE', 'sec:II:07',
     'The first eighteen working pages treat normal supports, class VII boundaries and contracted ruled boundaries; the remaining horizontal and interface arguments now have a separate section.'),
    (r'\subsection{Reduced horizontal boundaries}\label{subsec:II:reduced-horizontal-boundaries}',
     '\\section{Horizontal conductors and elliptic interfaces}\\label{sec:II:horizontal-conductor-interfaces}\n\n\\subsection{Reduced horizontal boundaries}\\label{subsec:II:reduced-horizontal-boundaries}',
     'HORIZONTAL-SECTION', 'subsec:II:reduced-horizontal-boundaries',
     'Start the rational horizontal-conductor and elliptic-interface group at its existing mathematical boundary. Its ongoing complete proof comparison remains open.'),
    (r'\subsection{Elliptic fibrations with vertical boundary}\label{subsec:II:elliptic-alignment}',
     '\\section{Torsion-normal boundaries and elliptic cores}\\label{sec:II:torsion-boundaries-elliptic-cores}\n\n\\subsection{Elliptic fibrations with vertical boundary}\\label{subsec:II:elliptic-alignment}',
     'ELLIPTIC-CORE-SECTION', 'subsec:II:elliptic-alignment',
     'Separate the eleven-page terminal/canonical-flat group from the alignment, common marked surface models, elliptic-core contraction and rational toric pair group. Their dependency order is unchanged.'),
    (r'\section{Actual contractions, canonical reduction and finite generation}',
     r'\section{Maximum components and canonical-flat toric models}',
     'REDUCTION-SECTION-TITLE', 'sec:II:11',
     'The first group contains the local maximum-component criterion and canonical-flat central log spaces with compact toric occurrence. Replace the process adjective and describe that mathematical group.'),
    (r'\subsection{Local modifications and overlap maps}\label{subsec:II:modification-records}',
     '\\section{Canonical reduction and weighted descent}\\label{sec:II:canonical-reduction-weighted-descent}\n\n\\subsection{Local modifications and overlap maps}\\label{subsec:II:modification-records}',
     'CANONICAL-DESCENT-SECTION', 'subsec:II:modification-records',
     'Group the local modification maps, canonical-flat reduction, cyclic roots and weighted toric descent in their existing proof order.'),
    (r'\subsection{Maximal Hopf component reduction}\label{subsec:II:maximal-hopf-reduction}',
     '\\section{Hopf orders and exceptional configurations}\\label{sec:II:hopf-orders-exceptional-configurations}\n\n\\subsection{Maximal Hopf component reduction}\\label{subsec:II:maximal-hopf-reduction}',
     'HOPF-ORDER-SECTION', 'subsec:II:maximal-hopf-reduction',
     'Group maximum Hopf reduction, its compact negative-curve example, exceptional configurations, maximal leaves and the comparison above the Hopf maximum.'),
    (r'\subsection{Canonical-flat root descent}\label{subsec:II:canonical-flat-root-descent}',
     '\\section{Root descent and finite reduction}\\label{sec:II:root-descent-finite-reduction}\n\n\\subsection{Canonical-flat root descent}\\label{subsec:II:canonical-flat-root-descent}',
     'FINITE-REDUCTION-SECTION', 'subsec:II:canonical-flat-root-descent',
     'Group canonical-flat root descent, no-triple contractions and finite rooted generation before the final Euler theorem.')
]
after = before
for old, new, key, unit, reason in changes:
    assert after.count(old) == 1, key
    after = after.replace(old, new, 1)
preserve_identifiers(before, after)
restored = after
for old, new, key, unit, reason in reversed(changes):
    assert restored.count(new) == 1, key
    restored = restored.replace(new, old, 1)
assert restored == before
for old, new, key, unit, reason in changes:
    kinds = ['D14'] + (['D08'] if key == 'REDUCTION-SECTION-TITLE' else [])
    apply_edit(old, new, 'DII-C3-' + key, kinds, unit, 'Section boundary/title', reason,
        'Root read the current contents, section spans and mathematical group headings. Foundations confirmed that the remaining proof work uses these boundaries. Inverse replacement recovers the full original source byte-for-byte; no statement, formula or proof text changes. Original remainder identities and every global structure row remain open.')
assert SOURCE.read_text() == after
add_event('sec:II:07;sec:II:11;sec:II:canonical-flat-classification',
    'II-C3-MODEL-SECTION-BOUNDARIES', 'used and rechecked in this run',
    'Read current working PDF outline and section spans: the Euler group had63pages, terminal/canonical-flat group32, and originalsec11 group57. Added five section boundaries at existing mathematical subsection starts and retitled two existing sections. Exact inverse replacements recover all original source bytes, proving that every statement, proof, label and target is preserved. Foundations confirmed the pending proof-package boundaries. No whole-unit, final-placement, final-build or final-page closure is claimed; originalsec07 andsec11 remainder identities remain open.',
    'Current mathematical section groups; source-only boundary changes', source=__file__)
print('Seven heading changes admitted; all mathematical bodies unchanged.')
