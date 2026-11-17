"""Persist root's independent proof review and exact D47 replay."""
from pathlib import Path
import datetime
import hashlib
import json

root = Path(__file__).resolve().parents[1]
output = root / 'records/root_component_ring_audit.out'
assert 'ALL127 HNFs index<=12 PASS' in output.read_text()
proof = root / 'sections/fourfolds_D2_component_ring.tex'
record = {
    'reviewed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'decision': 'PASS: D.2.47 approved for registration',
    'proof_sha256': hashlib.sha256(proof.read_bytes()).hexdigest(),
    'exact_replay': str(output.relative_to(root)),
    'number_of_period_HNFs': 127,
    'maximum_period_index': 12,
    'independent_geometric_checks': [
        'Derived the Cartier restriction as neighbor coefficient minus the current component coefficient, using the total principal divisor.',
        'Checked self-neighbor cancellation without embedded adjunction, and the distinction between the immersion normal line and the pulled-back Cartier normal line.',
        'Checked the integral trilinear formula and its quotient-cell expansion, including actual loops, repeated labels and multiplicities.',
        'Checked relative compact support versus the absolute triviality of the total central line bundle.',
        'Checked local invariant volume extension at xyz=q and the immersion tangent sequence with normal K_dP6.',
        'Checked the c2 and p1 evaluations and both example lattice families.',
    ],
    'scope_limit': 'Component divisor triple products and characteristic pairings only; no assertion of a complete torsion ring, fundamental-class invariant or global smooth classification.',
}
(root / 'records/root_D47_completion_audit.json').write_text(json.dumps(record, indent=2) + '\n')
path = root / 'records/root_completion_audit11.json'
combined = json.loads(path.read_text())
combined['D.2.47'] = record
path.write_text(json.dumps(combined, indent=2) + '\n')
print(json.dumps(record, indent=2))
