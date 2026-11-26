from S6_SERIES_PUBLISH_c3_edit import *

apply_edit('\\item Choose a proper holomorphic resolution of the pair\n$\\pi:U\'\\to U$ which is an isomorphism away from $S$ and over',
    '\\item Write $f:U\\to\\Delta$ for the degeneration and choose a proper\nholomorphic resolution of the pair $\\pi:U\'\\to U$ which is an\nisomorphism away from $S$ and over',
    'II-C3-NC-MAP-NAME', ['D22'], 'night:P4.13', 'Monodromy proof, first item',
    'Name the degeneration map explicitly before applying the source theorem to f composed with pi. The map and its domain are the original degeneration.')
outcomes = {
    'night:P4.6': 'Read the complete original and receiving proof. The normalization-immersion normal sequence, coordinate derivative, real Chern restrictions, conductor double cover with sign line, coherent Euler calculation and branch-count Euler formula are unchanged. Smoothness is stated explicitly in the domain used by all these maps and by duality.',
    'night:P4.7': 'Read the complete original and receiving proof. The Leray injection, smooth-fibre tangent sequence, Ehresmann bundle, Euler additivity and alternating middle pairing are unchanged; the smooth ambient domain required by these constructions is explicit.',
    'night:P4.12': 'Read the complete proof and its retained source locators. The primitive canonical generator, torsion adjunction, exceptional intersection matrix, discrepancy equations, formal-function vanishing, exceptional-cycle cohomology obstruction and nonnormal conductor poles remain unchanged. Removed only the trailing preview containing a literal run label. Mumford Section I p.6 was opened at the complete quadratic-form proof; the retained local-function adaptation supplies the analytic setting.',
    'night:P4.8': 'Read the entire normal-crossing normalization classification and all six proof items. Ruled blowup Euler formulas, finite unramified class-VII covers, conductor pullbacks, torsion-canonical exclusion, reducible-component intersection divisors and normalized cyclic base change are retained. No proof rewrite or new independent derivation is claimed.',
    'night:P4.13': 'Compared both complete proofs after opening A Campo Section 1, Section 2 proper analytic model and Section 3 trace argument. The resolution isomorphism identifies the source nearby fibre with F; its components and multiplicities give exactly the same Euler-weighted trace sum. The multiplicity-m specialization, local finite action, filtered quasi-unipotence, dual evaluation action and exterior-algebra determinant bound are unchanged. The known local trace re-proof is replaced by the precise source application.'
}
for statement, outcome in outcomes.items():
    add_event(statement, 'publish:c3:root:nc-read:' + statement, 'used and rechecked in this run', outcome,
        'Complete normal-crossing, canonical-torsion and monodromy units',
        group='publish:c3:root:nc-comparison', source='S6_SERIES_PUBLISH_defects_II.tsv; S6_SERIES_PUBLISH_c3_primary_readings.tsv')
for unit in ['night:P4.6', 'night:P4.12', 'night:P4.8']:
    for number in range(1, 26):
        kind = f'D{number:02}'
        status = 'open' if kind in ['D14', 'D23'] else 'done'
        detail = ('Final whole-paper placement is pending.' if kind == 'D14' else
            'Complete source typography checked; final rendered-page inspection is pending.' if kind == 'D23' else
            'Complete unit read; all actual instances corrected and logged, exact maps and original hypotheses retained or clarified explicitly. Known-source use compared at its stated scope.')
        set_unit_status(unit, kind, status, detail, 'S6_SERIES_PUBLISH_defects_II.tsv; CHECK_EVENTS.tsv')
    set_unit_status(unit, 'structure', 'open', 'Local premises are ordered; final whole-paper placement remains pending.', 'S6_SERIES_PUBLISH_II.tex')
print('Five exposed-reading events recorded; 63 previously open defect rows closed across three current units.')
