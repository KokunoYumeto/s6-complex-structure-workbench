"""Add verified printed locators and record the bounded source comparisons."""
from S6_SERIES_PUBLISH_c4_edit import *
import hashlib

edits = [
    (r'\citep{AC26,Engel2026}',
     r'\citep[Theorem~8.1, pp.~63--64]{AC26}' + '\n' +
     r'\citep[Theorem~4.1, p.~12]{Engel2026}',
     'II-C4-LOC-FAMILY', 'series:II:main-theorems', 'Section 1.1',
     'The two construction credits now point to the exact recognition theorems. Both statements and proofs were opened; AC26 uses its same compact glued space of Theorem 6.2.'),
    (r'in the construction of \cite{Viaclovsky2026Combs}, in particular',
     r'in the construction of \cite[Theorem~1.1, p.~2]{Viaclovsky2026Combs}, in particular',
     'II-C4-LOC-COMBS', 'series:II:main-theorems', 'Theorem F',
     'The cited source theorem specifies the constructed m>=12 family and its fibration-preserving diffeomorphism. The present broader positive-comb scope and exact Kuranishi formula are unchanged.'),
    (r'\cite[arXiv version~3, \S3, (14)]{Rossi2017}',
     r'\cite[arXiv version~3, \S3, (14), p.~9]{Rossi2017}',
     'II-C4-LOC-ROSSI', 'cdp:st:C.2.UN.8', 'Weierstrass coordinate identification',
     'Fresh version-3 PDF page 9 gives equation (14); the receiving coordinate map is exactly (x_Rossi,y_Rossi)=(y,x), B(t)=t^6-1.'),
    (r'\cite[Section~7]{CDP2020}',
     r'\cite[Section~7, p.~692]{CDP2020}',
     'II-C4-LOC-CDP-CONORMAL', 'cdp:st:B3', 'Topology of the Weierstrass product',
     'The source page containing the conormal reduction was opened in this continuation. The displayed example retains H2=Z^11 and algebraic dimension three, and its exact scope remains explicit.'),
]
text = SOURCE.read_text()
for old, new, ident, statement, location, reason in edits:
    if text.count(old) != 1:
        raise ValueError((ident, text.count(old)))
for old, new, ident, statement, location, reason in edits:
    apply_edit(old, new, ident, ['D18'], statement, location, reason,
               review='Exact primary locus and current receiving citation context read by root; only the locator changes.')

fields, prior = read_tsv(ROOT / 'S6_SERIES_PUBLISH_c4_primary_readings.tsv')
def row(key, path, url, version, locus, summary, use):
    return dict(source=key, url=url, version=version, locus=locus,
                date_utc=now(), sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                own_word_summary=summary, use=use)
rows = [
    row('II-C4-ENGEL-4.1', '/tmp/S6_SERIES_PUBLISH_c4_primary/Engel-v1.pdf',
        'https://arxiv.org/pdf/2609.38442v1', 'arXiv version 1', 'Theorem 4.1 and complete proof, p.12',
        'The specified primitive local-translation data give the compact complex manifold diffeomorphic to the standard six-sphere. The proof combines simple connectedness, integral homology and the six-dimensional homotopy-sphere classification.',
        'Section 1.1 construction credit; exact construction parameters retained.'),
    row('II-C4-ROSSI-EQ14', '/tmp/S6_SERIES_PUBLISH_c4_primary/Rossi-v3.pdf',
        'https://arxiv.org/pdf/1211.6329v3', 'arXiv version 3', 'Section 3, equation (14), and Proposition 3 with proof, p.9',
        'The rational elliptic Weierstrass model with six simple zeros of its degree-six coefficient has six cuspidal fibres; its self-product has the displayed local cubic-cusp equation.',
        'UN8 identifies the coordinate interchange (x_Rossi,y_Rossi)=(y,x) and coefficient B=t^6-1 explicitly. The locator adds page 9 and changes no construction.'),
    row('II-C4-COMBS-1.1', '/tmp/S6_SERIES_PUBLISH_c4_primary/Combs-v1.pdf',
        'https://arxiv.org/pdf/2610.10451v1', 'arXiv version 1', 'Theorem 1.1, complete statement, p.2; attached introduction source also read',
        'For m at least twelve the constructed fibrations preserve the original smooth map, monodromy, critical values, multiplicities and reduced critical fibres, and give the stated structure-sheaf cohomology and a lower Kuranishi-dimension bound.',
        'Theorem F credits exactly this constructed family; the exact dimension 8m+1 is the receiving theorem and is not attributed to this source statement.'),
    row('II-C4-AC26-INTRO', ROOT.parent / 'S6_GRIND_6_literature/original/AC26_original_manuscript.pdf',
        'https://alpo.ge/s6.pdf', 'Attached 108-page PDF, same printed locators reopened online in this continuation',
        'Theorem 6.2, p.36; Theorem 8.1 and complete proof, pp.63-64',
        'The gluing embeddings give the compact threefold and its torus fibration. The recognition theorem applies the computed fundamental group and integral homology to that same manifold and identifies its smooth type.',
        'Section 1.1 credits the six-sphere construction at Theorem 8.1. This hash identifies the attached bytes; the web opening supplies no new binary-identity claim.'),
]
print('Primary reading additions:', append_rows(ROOT / 'S6_SERIES_PUBLISH_c4_primary_readings.tsv', rows, 'source'))
for statement, ident, outcome in [
    ('series:II:main-theorems', 'II-C4-LOCATORS-FRONT', 'Construction credits compared with Engel Theorem 4.1, AC26 Theorem 8.1 and Viaclovsky Combs Theorem 1.1 at their exact printed pages. Only the locators changed; no independent proof or final global theorem check is claimed.'),
    ('cdp:st:C.2.UN.8', 'II-C4-LOCATORS-UN8', 'Rossi version 3 equation (14) and Proposition 3 read on page 9; the manuscript gives the identical coefficient B=t^6-1 after its explicit coordinate interchange. Page locator added.'),
    ('cdp:st:B3', 'II-C4-LOCATORS-B3', 'The CDP20 section-7 conormal step was read at published page 692. The receiving example keeps its ambient H2 and algebraic-dimension values, so the cited fibrewise inference is identified without enlarging the counterexample scope.'),
]:
    add_event(statement, ident, 'used and rechecked in this run', outcome,
              'S6_SERIES_PUBLISH_c4_primary_readings.tsv; S6_SERIES_PUBLISH_II.tex',
              source='code/S6_SERIES_PUBLISH_c4_exact_locators.py')
print('Four locator defects recorded; final inventory and counts left for text freeze.')
