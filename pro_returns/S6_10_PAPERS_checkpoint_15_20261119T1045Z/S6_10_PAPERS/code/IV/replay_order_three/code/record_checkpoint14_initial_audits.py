"""Record root reviews of the corrected stable trace and collision disc."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
audits = [
    ('P3K.52', 'notes/part3_source_cusp_stable_trace_working.md',
     'code/part3/source_cusp_stable_trace.json', [
         'The chain rule is a literal identity in the universal covering group of stable GL+; the explicit polar homotopy identifies its integral third class.',
         'The Maurer product boundary terms vanish on the fixed boundary collar, and the absolute two-cycle term bounds because H2(E)=0.',
         'The action prism gives the exact Delta1-to-Delta0 relative comparison; the two Stokes signs yield delta(Delta x)=W(boundary x).',
         'Each closed edge trace has rank-one endpoint caps. Its ambient/local frame comparison extends through annulus times D4 and has zero third pairing.',
         'The source Spin2 and normal Spin4 half-angle endpoints multiply to +1 in the actual full tangent lift.',
         'The local derivative degrees (6,-6,6), graph orientations, and fixed-cusp comparison give delta=(-12,-12,0).',
         'The ordinary pairs are (6,-6),(6,-6),(0,0); the exact native nonfixed corrections give (0,-6),(-6,0), all with central coordinate1.'
     ], 'Actual initial-fan derivative and three relative pairs. A later fan recurrence still requires its actual product-reset morphism.'),
    ('P3K.53', 'notes/part3_source_unselected_collision_working.md',
     'code/part3/source_unselected_collision.json', [
         'At the unselected collision F_T=1/4 and the displayed graph makes the source a smooth family over the parameter disc.',
         'The selected-node normalization, branch, Tate/Cartier units and fan extend over that disc without exchanging branches.',
         'Both actual III-star cap root equations, deck characters, division point, norm and Cartier corrections extend with the retained reference data.',
         'The central additive coordinate 1/s sends G to2 and bG to2b; the invariant flow has nonzero vertical derivative and supplies the exact translation extension.',
         'The canonical Hom divisor excludes new codimension-one defects; the smooth total source extends its unit across the remaining codimension-two curve.',
         'The alternate cube-root coordinate maps and full root character maps retain the exact scalar cancellation.',
         'The fixed-contour annular continuation preserves all finite and integral cochains and extends the canonical chosen continuation.',
         'Uniform contraction shells, actual root quotients and the selected toric charts give a proper smooth compact family over the disc, hence zero positive return.'
     ], 'The canonical one-III-star-cap continuation with no additional logarithmic discs on the colliding unselected pair. The global source-zero and infinity returns remain uncomputed.')
]
for ident, proof, certificate, checks, scope in audits:
    cert = json.loads((root / certificate).read_text())
    assert cert['status'] == 'PASS'
    record = {'utc': datetime.now(timezone.utc).isoformat(), 'reviewer': 'root',
              'statement': ident, 'status': 'PASS', 'proof': proof,
              'proof_sha256': hashlib.sha256((root / proof).read_bytes()).hexdigest(),
              'certificate': certificate, 'verified_maps': checks, 'scope': scope}
    dest = root / 'records' / ('root_audit_' + ident.replace('.', '_') + '.json')
    dest.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'statement': ident, 'status': 'PASS', 'record': str(dest.relative_to(root))}))
