from S6_SERIES_PUBLISH_c3_edit import *
import hashlib

apply_edit('Let $X$ be a compact complex threefold with $b_2(X)=0$, and let $F$ be a',
    'Let $X$ be a smooth compact complex threefold with $b_2(X)=0$, and let $F$ be a',
    'II-C3-NC-SMOOTH-1', ['D22'], 'night:P4.6', 'Normal-crossing Euler formula: ambient hypothesis',
    'Make explicit the manifold domain used throughout the proof by T_X, its vector-bundle normal sequence, analytic Riemann--Roch and Poincare duality. The standing torus-fibration setting and every displayed application have this domain. No singular-ambient extension or refutation is asserted.')
apply_edit('fibres from a compact complex threefold satisfying $b_1(X)=b_2(X)=0$',
    'fibres from a smooth compact complex threefold satisfying $b_1(X)=b_2(X)=0$',
    'II-C3-NC-SMOOTH-2', ['D22'], 'night:P4.7', 'Normal-crossing fibration: ambient hypothesis',
    'Make explicit the same smooth-manifold domain as the normal-crossing Euler input, the standing setting, the tangent-bundle restriction, Ehresmann theorem and duality used in this proof. No mathematical conclusion or application changes.')
apply_edit('The ruled-genus and nonnormal-conductor arguments needed after\nthis reduction are proved below and completed in P4.58.\n', '',
    'II-C3-NC-RECAP', ['D04', 'D13'], 'night:P4.12', 'Paragraph after canonical-torsion proof',
    'Remove the orphan preview and its literal research-run identifier. The later labelled arguments and final classification retain their complete statements and proofs.')

s = SOURCE.read_text()
section_start = s.index('\\begin{proposition}[Monodromy and the smooth locus of an irreducible fibre]')
start = s.index('\\item At a point on $k$ branches,', section_start)
end = s.index('\\item For a common multiple $N$', start)
old = s[start:end]
new = r'''\item Apply the proper analytic normal-crossing model of
\cite[\S2, pp.~237--243, and \S3, pp.~243--245]{ACampo1975}
to $f\circ\pi:U'\to\Delta$. Write $E_j$ for its central components,
$n_j$ for their multiplicities and $E_j^\circ$ for each component
with the other components removed. The map $\pi$ identifies its nearby
fibre with the nearby torus $F$ of $f$. For the induced cohomology
monodromy $T$, the cited local trace calculation and global Leray
sequence give
\[
 L(T^d;H^*(F;\C))=\sum_{n_j\mid d}n_j e(E_j^\circ).
\]
For $d=m$ the strict transform is the sole contribution, and its
open stratum is $S_{\mathrm{reg}}$.

'''
apply_edit(old, new, 'II-C3-NC-ACAMPO', ['D17'], 'night:P4.13',
    'Monodromy proof, second item',
    'Read A Campo 1975 Section 2 proper smooth analytic setting and its global Leray construction, plus Section 3 local trace and spectral-sequence argument. The same map is f composed with pi; pi is an isomorphism on the nearby fibre. Replace the repeated known local trace proof by this exact source application, retaining the full formula and its multiplicity-m specialization.')
apply_edit('\\item For a common multiple $N$\nof the $n_j$, the $N$th power of monodromy acts trivially on all local\nnearby-cohomology sheaves, hence on the $E_2$ page.',
    '\\item In the normal-crossing local model, monodromy permutes the\ncomponents and translates the torus factors. For a common multiple $N$\nof the $n_j$, its $N$th power acts trivially on all local\nnearby-cohomology sheaves, hence on the $E_2$ page.',
    'II-C3-NC-LOCAL-MODEL', ['D17'], 'night:P4.13', 'Monodromy proof, third item',
    'Keep the precise branch-permutation and torus-translation description at its remaining use in the quasi-unipotence argument. This is the same local action previously stated in the preceding item.')

readings = ROOT / 'S6_SERIES_PUBLISH_c3_primary_readings.tsv'
fields = ['source', 'url', 'version', 'locus', 'date_utc', 'sha256', 'own_word_summary', 'use']
if not readings.exists():
    write_tsv(readings, fields, [])
with readings.open('a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writerow(dict(zip(fields, ["A'Campo 1975", 'https://www.e-periodica.ch/cntmng?bot=1&pid=com-001%3A1975%3A50%3A%3A27',
        'Comment. Math. Helv. 50 (1975), 233–248; attached original-paper transcription',
        'Section 1, Theorem 1, pp.234–235; Section 2 setup and model, pp.237–240; Section 2(4), pp.242–243; Section 3, pp.243–245', now(),
        'text: 9f489627aa7a58f2c409e14c8e4b528daeaede9e2627e09b0f4343440e8fe66f; original PDF hash in supplied retrieval record: 8562e8ca2b2ab297873b2c07929d73910585072b286e390d4c0dbf028a75c03d',
        'The global construction starts with a proper holomorphic map from a smooth analytic space to a disc and a normal-crossing central divisor. Its retraction gives the Leray sequence for nearby-fibre cohomology. Local iterated traces are zero on crossing strata and equal the component multiplicity on the single-branch stratum exactly when that multiplicity divides the iterate. Alternating traces yield the Euler-weighted sum used here.',
        'night:P4.13: f composed with the resolution has the required domain, and its nearby fibre is identified with the original torus by the resolution map. Known local trace proof replaced by citation.'])))
    writer.writerow(dict(zip(fields, ['Mumford 1961', 'https://www.numdam.org/item/PMIHES_1961__9__5_0.pdf',
        'Publications mathematiques IHES 9 (1961), 5–22; Numdam scan',
        'Section I, unnumbered intersection-matrix assertion and complete proof, printed p.6', now(),
        'attached text: cf7e8d72ccbfa60d5341ecf3ffd981f7489f92cc59604217d7cfb1f7dfc1a6b6; web scan opened',
        'A positive exceptional cycle obtained from a function divisor scales the intersection matrix to nonnegative off-diagonal entries and nonpositive row sums. A strict row sum in each connected component makes the quadratic form negative definite.',
        'night:P4.12: retained short analytic adaptation. A local holomorphic function supplies the same effective cycle and matrix identity; the cited paper states the algebraic-surface setting.'])))
print('Three adjacent units edited; original and receiving mathematical comparisons recorded after rereading the changed contexts.')
