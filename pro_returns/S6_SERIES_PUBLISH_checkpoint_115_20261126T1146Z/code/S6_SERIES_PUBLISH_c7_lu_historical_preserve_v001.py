"""Preserve the root-requested exact LU historical bodies inside the checkpoint."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('/tmp/S6_SERIES_PUBLISH_c7_LU_historical')
DESTINATION = ROOT/'agents/continuation7_iii_corrected_initial_receiving/historical'
DESTINATION.mkdir(exist_ok=True)
expected = {
    'S6_SERIES_PUBLISH_manifolds_corrected_initial.py':
    '0b3e4521d88814db7b37cb4932d90b5f76fcc2e2290be1c1cac841e970b4ba9e',
    'S6_SERIES_PUBLISH_manifolds_corrected_initial_audit.py':
    '2d0a5cd030a6e224f1598fd3506ca11e34cabc3aa3a8a9335d73ba3dc5ba1675',
    'S6_SERIES_PUBLISH_manifolds_corrected_initial_audit.json':
    '9a2a42f64554113985559bf8cbf78c70ae47fcf15461ece7b456a9cbc68722a0',
}
print('START', datetime.now(timezone.utc).isoformat(), flush=True)
for name, digest in expected.items():
    raw = (SOURCE/name).read_bytes()
    assert sha256(raw).hexdigest() == digest
    target = DESTINATION/name
    assert not target.exists()
    target.write_bytes(raw)
    assert target.read_bytes() == raw
    print('PRESERVED', target.relative_to(ROOT), 'BYTES', len(raw), 'SHA256', digest, flush=True)
print('COMPLETE', datetime.now(timezone.utc).isoformat(), flush=True)
