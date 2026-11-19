"""Record the bounded primary-source read without saving the full article."""
from datetime import datetime, timezone
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
utc = datetime.now(timezone.utc).isoformat()
record = {
    'recorded_utc': utc,
    'read_interval_utc': ['2026-11-17T11:59:35Z', '2026-11-17T12:06:50Z'],
    'reason': 'Verify the spin-c characteristic formula for the actual source-zero mapping-torus boundary, including its nonzero first cohomology.',
    'searches': [
        {'engine':'system2', 'query':'"Eells-Kuiper" "spin" "coboundary" "spin^c"', 'result':'No result returned'},
        {'engine':'system2', 'query':'"Eells-Kuiper" "spin-c" formula', 'result':'No result returned'},
        {'engine':'system1', 'query':'Eells Kuiper invariant spin c coboundary formula Crowley Goette Kreck Stolz'},
        {'engine':'system1', 'query':'Eells Kuiper invariant circle action fixed point localization bounding manifold'}
    ],
    'successful_read': {
        'title':'Exotic G2-manifolds',
        'authors':['Diarmuid Crowley','Johannes Nordstrom'],
        'url':'https://link.springer.com/article/10.1007/s00208-020-02009-1',
        'ref_ids':['turn352search0','turn353view0','turn359view0','turn359view1'],
        'verified_parts':['Lemma2.1(i)', 'Section2.2, equation(2.1)', 'publication metadata'],
        'use':'The spin-c boundary formula in Z/28 for H4(M;Z)=0; exact algebra and all relative-product and orientation transfers are proved in the current-run working note.',
        'unused_scope':'The subsequent two-connected smooth-classification theorem is not invoked.'
    },
    'failed_open': {
        'url':'https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms.12222',
        'ref_id':'turn353view1',
        'status':'403',
        'material_used':'none'
    },
    'followup': 'The same polynomial had already been proved for homotopy-sphere boundaries in P3R.1 from Jiang2014; the new read checks the exact mapping-torus scope and relative degree-two ambiguity.',
    'blindness':'No prohibited earlier-run proof or repository was opened.'
}
(root/'records/source_zero_spin_c_primary_read.json').write_text(json.dumps(record, indent=2)+'\n')
entry = (
    '\n| '+utc+' (recorded; read interval11:59:35–12:06:50 UTC) | '
    'Crowley–Nordstrom, Exotic G2-manifolds, Math.Ann.381(2021),29–74, '
    'https://link.springer.com/article/10.1007/s00208-020-02009-1 | '
    'Verify the characteristic formula for the actual source-zero mapping-torus boundary | '
    'Read Lemma2.1(i), Section2.2 equation(2.1), and publication metadata. '
    'The definition applies to closed spin seven-manifolds with torsion-free H4; '
    'the two-connected classification theorem is unused. The primary Wiley '
    'classification DOI10.1112/plms.12222 returned403 and supplied no input. '
    'Exact searches, read bounds and the independent reduction appear in '
    'records/source_zero_spin_c_primary_read.json and '
    'notes/part3_source_zero_spin_c_boundary_working.md. |\n'
)
with (root/'S6_06_BLIND_literature_log.md').open('a') as f:
    f.write(entry)
print('Recorded verified primary formula, metadata, failed retrieval and read bounds.')
