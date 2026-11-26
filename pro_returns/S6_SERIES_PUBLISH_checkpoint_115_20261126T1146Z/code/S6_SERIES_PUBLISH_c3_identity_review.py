from S6_SERIES_PUBLISH_c3_edit import *

apply_edit('induced maps into the aspherical space $A\\times P$; in particular they\nretain the degree-two contribution of the clutch.',
    'induced maps into the aspherical space $A\\times P$; they include\nthe degree-two contribution of the clutch.',
    'II-C3-IDENTITY-CLUTCH-WORDING', ['D08'], 'night:P4.4', 'Overlap-map calculation',
    'The term x wedge g_i is unchanged. State directly that it is included in the displayed induced map.')
apply_edit('\\item We verify integral surjectivity by hand. Eliminating the local $H_1$',
    '\\item Eliminating the local $H_1$', 'II-C3-IDENTITY-ELIMINATION-WORDING', ['D08'],
    'night:P4.4', 'Integral homology proof, fourth item',
    'The full integral elimination immediately follows; remove the redundant description of how it is checked.')

outcomes = {
    'def:II:standing-torus-fibration': 'Read the complete original and revised setting. The smooth ambient threefold, Betti assumptions, connected torus-fibre map and additional irreducible-or-normal-crossings hypothesis remain explicit. The normalization and resolution maps now name the same data directly.',
    'def:II:identity-example-lattice': 'Read the former setup and new numbered definition. E, q, A, the ordered lattice, exponential comparison and meridian orientations are unchanged; the common conventions already give complex orientations.',
    'night:P4.1': 'Read the complete original and receiving proof. The two blowup charts, line-bundle transitions, canonical-section trivialization, primitive Chern class and tautological Hopf-component map remain unchanged.',
    'night:P4.2': 'Read the complete original and receiving proof. The logarithmic clutch, all three Gaussian-integer markings and their explicit inverses, proper Hausdorff gluing, and induced identity lattice monodromy remain unchanged.',
    'night:P4.3': 'Read the complete original and receiving proof. The blowup homotopy pushout, circle-bundle model, two integral cellular cancellation pairs, free quotient homology and bounding meridian products remain unchanged. The duplicate differential arrays were matched entrywise to these definitions.',
    'night:P4.4': 'Read both complete proofs and every removed array. The marking matrices and exact exterior-power quotient definitions moved inside the proof. All clutch-induced maps, integral elimination matrices, ordered determinants and van Kampen relations remain. All 18 duplicate arrays are exact evaluations of retained maps, as the separate exposed computation confirms. No independent re-proof is claimed.',
    'night:P4.5': 'Read both complete proofs and all of the earlier E1 proof. Euler additivity, complex-orientation top Chern class, duality and the UCT torsion argument remain unchanged. The repeated divisor/meromorphic-descent argument is replaced by E1 with its exact hypotheses checked for f and the same pullback field isomorphism displayed.',
}
for statement, outcome in outcomes.items():
    add_event(statement, 'publish:c3:root:identity-read:' + statement, 'used and rechecked in this run',
        outcome, 'Identity-monodromy example: complete original and receiving text',
        group='publish:c3:root:identity-comparison', source='S6_SERIES_PUBLISH_defects_II.tsv')
for statement in ['night:P4.3', 'night:P4.4']:
    add_event(statement, 'publish:c3:root:identity-matrices:' + statement,
        'computation or formal certificate',
        'After proof exposure, reconstructed the local quotient matrices from the three marking isomorphisms, their inverses and exterior squares; reconstructed cellular differential and Mayer--Vietoris blocks from the printed maps. All 18 printed arrays agree entrywise. Differential composites vanish; det RH1=-1, det RH2=1, det F1=-1; Smith factors are all units, with ranks 15 and 29. This verifies the duplicate arrays, not an independent geometric derivation.',
        'Exact duplicate-array comparison', group='publish:c3:root:identity-matrices',
        source='code/S6_SERIES_PUBLISH_c3_example_matrices.py; code/S6_SERIES_PUBLISH_c3_example_matrices.out')
for number in range(1, 26):
    kind = f'D{number:02}'
    status = 'open' if kind in ['D14', 'D23'] else 'done'
    detail = ('Final whole-paper placement remains pending.' if kind == 'D14' else
              'Source typography inspected; receiving PDF pages require visual inspection.' if kind == 'D23' else
              'Complete original/receiving unit read; all instances recorded, mathematical data and exact maps retained; D10/D16 continue completed.')
    set_unit_status('night:P4.1', kind, status, detail, 'S6_SERIES_PUBLISH_defects_II.tsv; CHECK_EVENTS.tsv')
set_unit_status('night:P4.1', 'structure', 'open',
    'The example is internally ordered and each proof has one owner; final whole-paper placement remains pending.',
    'S6_SERIES_PUBLISH_II.tex')
print('Seven exposed-reading events and two associations to one exact computation recorded; 21 previously open defect rows closed in the example unit.')
