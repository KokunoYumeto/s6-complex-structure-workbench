from S6_SERIES_PUBLISH_c3_edit import *

outcomes={
    'night:P4.16':'Both complete original lattice proofs and the full common receiving proof were read. The exact specialization a=2 maps roots, exceptional chains, primitive kernel and square to the original two-branch calculation. The general graph cover, compactification, integral pair map, weighted scaling, unit-removal isomorphism and torus inclusion are all present. Both permanent identifiers share one owner; no independent derivation is claimed.',
    'night:P4.17':'The receiving common proof was compared with the whole original a-root proof and its two-root input. The general lattice A_(a-1)(-n), all parameter ranges, weighted homogeneity and complete normalization quotient map survive. Its normalization proof item is byte-identical. This is the same exposed comparison group as P4.16.',
    'night:P4.19':'Complete original and receiving proof read. The two conductor ideals, fibre-product description and explicit inverse maps to C* times C are unchanged. Compact-support extension by zero gives the same intersection conclusion. Its two unused hidden input declarations were removed.',
    'night:P4.20':'Complete original and receiving proof compared, including boundary submersivity, isolated critical values, stable normalization deformation, cross-cap coordinate maps, image equation and dependent-gradient perturbation. Its cross-cap application is explicitly (a,n)=(2,2). Its Morse quadratic is sent by the printed invertible linear map to (a,n)=(2,1), using the single earlier lattice calculation. All normal-crossing and full-fibre hypotheses remain unchanged.',
    'night:P4R.6':'Receiving proof reread after the second consolidation. The Morse quadratic is identified exactly with x^2-zy; the earlier lattice owner gives square -2. The same parameter and boundary transports carry the compact spherical class to h inverse(delta), and f=h^m embeds it in the same global torus fibre. The original contradiction and pole-support conclusion are unchanged.'
}
for owner,outcome in outcomes.items():
    group='II-C3-SPHERICAL-COMMON-OWNER' if owner in ['night:P4.16','night:P4.17'] else ''
    add_event(owner,'II-C3-ROOT-SPHERICAL-'+owner.replace(':','-').replace('.','-'),
        'used and rechecked in this run',outcome,
        'S6_SERIES_PUBLISH_II.tex; code/S6_SERIES_PUBLISH_c3_spherical_lattice.py; code/S6_SERIES_PUBLISH_c3_spherical_applications.py',
        group=group,source='code/S6_SERIES_PUBLISH_c3_spherical_review.py')
for unit in ['night:P4.16','night:P4.19']:
    for number in range(1,26):
        kind=f'D{number:02}'
        if kind in ['D10','D16']:continue
        status='open' if kind in ['D14','D23'] else 'done'
        detail=('Local premise order is now settled; final whole-paper placement remains open.' if kind=='D14'
            else 'Integrated build and final rendered-page reading remain open.' if kind=='D23'
            else 'Complete current unit read against this defect type. All identified instances are logged; both full original proofs and receiving maps were compared.')
        set_unit_status(unit,kind,status,detail,'code/S6_SERIES_PUBLISH_c3_spherical_review.py')
    set_unit_status(unit,'structure','open','Common proof ownership and local order settled; final whole-paper placement remains open.',
        'code/S6_SERIES_PUBLISH_c3_spherical_review.py')
print('Five exposed comparison associations in four evidence groups; two full unit reviews close 42 previously open defect rows.')
