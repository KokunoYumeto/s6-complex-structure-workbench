"""Place the complete weighted owners and reconcile their front navigation."""
from S6_SERIES_PUBLISH_c3_edit import *

changes = [
    (r'\section{Marked Hopf, ruled and elliptic supports with all multiplicities}',
     r'\section{Marked Hopf and ruled cycles}', 'CYCLE-SECTION-TITLE', 'sec:II:10'),
    (r'\subsection{Elliptic star data and inverse transforms}\label{subsec:II:elliptic-star-data}',
     '\\section{Elliptic stars and compact insertion}\\label{sec:II:elliptic-stars}\n\n\\subsection{Elliptic star data and inverse transforms}\\label{subsec:II:elliptic-star-data}',
     'STAR-SECTION', 'subsec:II:elliptic-star-data'),
    (r'\subsection{Weighted normal data on marked cycles}\label{subsec:II:weighted-cycle-data}',
     '\\section{Weighted cycles and finite root actions}\\label{sec:II:weighted-root-cycles}\n\n\\subsection{Weighted normal data on marked cycles}\\label{subsec:II:weighted-cycle-data}',
     'WEIGHTED-SECTION', 'subsec:II:weighted-cycle-data'),
    (r'\subsection{Hopf support graphs and rational-root trees}\label{subsec:II:hopf-support-tree-remainder}',
     '\\section{Hopf support graphs and elliptic trees}\\label{sec:II:hopf-support-elliptic-trees}\n\n\\subsection{Hopf support graphs and rational-root trees}\\label{subsec:II:hopf-support-tree-remainder}',
     'TREE-SECTION', 'subsec:II:hopf-support-tree-remainder')
]
before = SOURCE.read_text()
after = before
for old, new, key, unit in changes:
    assert after.count(old) == 1, key
    after = after.replace(old, new, 1)
restored = after
for old, new, key, unit in reversed(changes):
    restored = restored.replace(new, old, 1)
assert restored == before
for old, new, key, unit in changes:
    apply_edit(old, new, 'DII-C3-' + key, ['D14'], unit, 'Section boundary/title',
        'The complete marked-cycle, elliptic-star, weighted finite-root and support/tree arguments form four consecutive mathematical groups. Introduce section breaks at those existing boundaries without moving or rewriting any proof.',
        'Root read all complete cycle/star/weighted receiving proofs and the working contents. Conductor confirmed the remaining support/tree boundaries. Inverse replacement recovers the full prior source bytes. Original sec10 remainder and global structure stay open.')

for old, new, key, statement in [
    ('\\item \\cref{wbII:thm:cartier-duality}\\quad Duality for a compact Cartier divisor.\n',
     '\\item \\cref{wbII:thm:cartier-duality}\\quad Duality and trace pairings for compact Cartier divisors and full scheme-theoretic fibres.\n',
     'DUALITY-OWNER', 'wbII:thm:cartier-duality'),
    ('\\item \\cref{wbII:prop:cartier-duality-absolute}\\quad Absolute duality on a compact Cartier fibre.\n', '',
     'DUALITY-ALIAS', 'wbII:prop:cartier-duality-absolute'),
    ('\\item \\cref{cdp:st:C.2.UN.52}\\quad The weighted root criterion, exact inertia and compact occurrence.\n',
     '\\item \\cref{cdp:st:C.2.UN.56}\\quad The weighted Hopf and ruled root criterion, with exact inertia and compact elliptic-suspension realizations.\n',
     'WEIGHTED-OWNER', 'cdp:st:C.2.UN.52;cdp:st:C.2.UN.56'),
    ('\\item \\cref{cdp:st:C.2.UN.56}\\quad The complete weighted mixed-cycle criterion.\n', '',
     'WEIGHTED-ALIAS', 'cdp:st:C.2.UN.56')
]:
    apply_edit(old, new, 'DII-C3-FURTHER-' + key, ['D12', 'D15'], statement, 'Further results',
        'The two old references resolve to one complete admitted owner. Give that owner one navigation entry covering both the general statement and its exact specialization.',
        'Root read the complete current cited duality statement, the complete weighted merged statement and proof, and every old/new list item. All body labels and permanent targets remain.')

apply_edit(
    'the other discriminant value is $-4/27$. The central support and every nontrivial normalization-gluing line\n',
    'the disc bound excludes the second singular value $t=-4/27$ of the same cubic pencil. The central support and every nontrivial normalization-gluing line\n',
    'DII-C3-NODAL-PENCIL-RESTRICTION', ['D22'], 'series:II:A', 'Theorem A nodal family',
    'Identify the parameter restriction explicitly: the pencil equation over the full t-line has singular values 0 and -4/27, and its restriction to the displayed disc contains only zero.',
    'Root read the full main-theorem unit and the nodal-family discriminant computation, and reread the complete receiving paragraph. No theorem domain or conclusion changes.')
apply_edit(
    'Write $Z\\to T\\to S$ for the minimal resolution of the\nnormalization. The canonical evaluation and\n',
    'For a singular irreducible support $S$, write $Z\\to T\\to S$\nfor the minimal resolution of its normalization. The canonical evaluation and\n',
    'DII-C3-EULER-IRREDUCIBLE-CANONICAL-SCOPE', ['D22', 'D25'], 'cdp:st:C.2.G.1', 'Euler proof step 3',
    'The holomorphically torsion canonical-boundary line in this step uses the irreducible full fibre mS. State that domain explicitly before the same maps are used in step4; step5 treats reducible components under their rational Chern-class hypothesis through INT1–3.',
    'Root reread the entire current G.1 proof and all complete INT1–3 receiving proofs, including the same h, sigma, tau, conductor and full-multiplicity maps. Complete final G.1 receiving read and INT admission follow; D25 remains open until then.')
add_event('sec:II:10;series:II:A;wbII:thm:cartier-duality;cdp:st:C.2.UN.56',
    'II-C3-WEIGHTED-SECTIONS-FRONT', 'used and rechecked in this run',
    'Four heading edits separate existing marked-cycle, star, weighted-root and support/tree groups; inverse replacement proves all body bytes unchanged. Full cited Cartier-duality statement and merged weighted-cycle proof were read against their duplicate list entries, which are consolidated. The Theorem A radius explanation identifies the same pencil restricted to the disc. All complete Further-results entries were read; remaining body-driven front correspondence and final typography stay open. No original section10 closure or final-page credit.',
    'Section boundaries and first-part navigation', source=__file__)
print('Weighted section boundaries, two duplicate list owners and explicit scope explanations admitted.')
