from S6_SERIES_PUBLISH_c3_edit import *

apply_edit(r'\subsection{Cuspidal transverse type and the ruled equality case}',
    r'\subsection{Cuspidal transverse type}',
    'II-C3-CUSP-HEADING',['D14'],'night:P4.28','Cuspidal transverse type',
    'The complete unit proves the local cusp rigidity theorem. The ruled conductor-pushout result has its own next subsection, so the current heading names this unit alone.')
apply_edit('Here is its boundary verification and the required\nfibre map. Fix a Milnor ball whose sphere is transverse',
    'Fix a Milnor ball whose sphere is transverse',
    'II-C3-CUSP-BOUNDARY-INTRODUCTION',['D11'],'night:P4.28',
    'Local rigidity of a transverse cusp, item1',
    'The following complete boundary proof and maps give their content directly; remove only the advance summary.')
add_event('night:P4.28','II-C3-ROOT-CUSP-COORDINATES',
    'used and rechecked in this run',
    'Complete original and receiving eight-item proofs read. The normal Hessian over the discrete valuation ring, two preparation branches, nested balls and all fibre transports remain. Both binomial reductions now print their exact sign/permutation coordinate maps; the lattice specialization is explicitly (a,n)=(2,3). No hypothesis, intersection value, normalization map or conclusion changes.',
    'S6_SERIES_PUBLISH_II.tex; code/S6_SERIES_PUBLISH_c3_cusp_coordinates.py',
    source='code/S6_SERIES_PUBLISH_c3_cusp_review.py')
for number in range(1,26):
    kind=f'D{number:02}'
    if kind in ['D10','D16']:continue
    status='open' if kind in ['D14','D23'] else 'done'
    detail=('Final whole-paper placement remains open.' if kind=='D14'
        else 'Integrated build and final rendered-page reading remain open.' if kind=='D23'
        else 'Complete current cusp unit read against this defect type; every found instance is logged and the entire receiving proof compared to its original.')
    set_unit_status('night:P4.28',kind,status,detail,'code/S6_SERIES_PUBLISH_c3_cusp_review.py')
set_unit_status('night:P4.28','structure','open','Exact local maps and proof ownership reviewed; final whole-paper placement remains open.',
    'code/S6_SERIES_PUBLISH_c3_cusp_review.py')
print('The complete cusp unit review closes 21 previously open defect rows; no independent-check credit.')
