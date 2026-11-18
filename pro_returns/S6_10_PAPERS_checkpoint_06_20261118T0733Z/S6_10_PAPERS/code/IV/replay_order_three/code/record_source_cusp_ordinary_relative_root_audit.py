"""Record direct proof review, preserving the exact ordinary-product scope."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
proof = 'notes/part3_source_cusp_ordinary_relative_working.md'
certificate = 'code/part3/source_cusp_ordinary_relative.json'
cert = json.loads((root / certificate).read_text())
assert cert['status'] == 'PASS' and cert['checks_count'] == 13
assert cert['relative_coordinates'] == [6, -6, 1]
record = {
    'utc': datetime.now(timezone.utc).isoformat(), 'reviewer': 'root',
    'status': 'PASS', 'proof': proof,
    'proof_sha256': hashlib.sha256((root / proof).read_bytes()).hexdigest(),
    'certificate': certificate, 'checks_count': 13,
    'reviewed_sections': ['OR.1', 'OR.2', 'OR.3', 'OR.4'],
    'verified_maps': [
        'The literal second Hopf chart substitutes to (b^-1,ba,bc); physical q is retained.',
        'The actual-to-reference arrows give Gamma=bO composed with inverse bH.',
        'The displayed retraction fixes the bottom and side of D3 times the parameter interval.',
        'Relative smoothing and radial normalization extend the inverse factors as SU2 maps.',
        'For D3 orientation followed by parameter, Stokes gives side minus top and endpoint degrees (6,0).',
        'The fibrewise endpoint is L^6 through explicit relative coefficient homotopies, with no additional central factor.',
        'PO=PH psi satisfies the ordinary boundary product and yields L^6 R^-6 C.',
        'The product derivative is +12; the ambient dual cycle is negative, and the K31 frame correction is -V00=0.',
        'The two native nonfixed second charts substitute exactly to z^-1 and z times the ordered normal pair.',
        'Their native-to-ordinary factor degrees are (-6,0), yielding pure-left degree-six corrections without evaluating the native returns.'
    ],
    'fixed_curve_result': {'m': 6, 'n': -6, 's': 1, 'variation': 0,
                           'product_derivative': 12, 'ambient_dual_derivative': -12},
    'scope': 'Complete ordinary fixed-C0 relative-return calculation and the two exact nonfixed frame comparisons. Not yet numbered in checkpoint13 master47. Native nonfixed returns, mutual variations and general source-loop fan returns remain uncomputed.'
}
(root / 'records/root_audit_source_cusp_ordinary_relative.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'sections': record['reviewed_sections'],
                  'fixed_curve_result': record['fixed_curve_result']}, indent=2))
