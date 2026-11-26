from S6_SERIES_PUBLISH_c3_edit import *

for owner,detail in [
    ('night:P4.15','Full original and receiving proof read. The maximal-minor exact sequence and Chern identity, numerical alternatives, nonempty conductor, two ruled conductor cases and finite unramified branch map are unchanged. P244 is applied only after the exact smooth/minimal/negative-Kodaira and b2=0 plus nonempty-curve hypotheses have been established.'),
    ('night:P4R.2','Full original and receiving proof read. The homeomorphism nu, isomorphism p_*q_*(nu_*) inverse, finite-index surface-group argument, Euler formulas and equality converse remain. The shared surface classification and finite-cover recognition have one earlier proved owner with identical maps.')]:
    add_event(owner,'II-C3-ROOT-SURFACE-'+owner.replace(':','-').replace('.','-'),
        'used and rechecked in this run',detail,
        'S6_SERIES_PUBLISH_II.tex; agents/continuation3_foundations/S6_SERIES_PUBLISH_P244_conclusion_map.tsv',
        source='code/S6_SERIES_PUBLISH_c3_surface_models_review.py')
for unit in ['night:P4.14','night:P4R.2']:
    for number in range(1,26):
        kind=f'D{number:02}'
        if kind in ['D10','D16']:continue
        status='open' if kind in ['D14','D23'] else 'done'
        detail=('Final whole-paper placement remains open.' if kind=='D14'
            else 'Integrated build and final rendered-page reading remain open.' if kind=='D23'
            else 'Full current unit read against this defect type, including P242/P244 where present. Every changed instance is logged; both original and receiving complete proofs and exact maps were compared.')
        set_unit_status(unit,kind,status,detail,'code/S6_SERIES_PUBLISH_c3_surface_models_review.py')
    set_unit_status(unit,'structure','open','Single owners and local premise order reviewed; final whole-paper placement remains open.',
        'code/S6_SERIES_PUBLISH_c3_surface_models_review.py')
print('Two complete unit passes close 42 previously open defect rows; no independent-check credit.')
