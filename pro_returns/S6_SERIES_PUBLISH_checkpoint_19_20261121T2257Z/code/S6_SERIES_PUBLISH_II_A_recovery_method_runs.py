"""Execute scoped recovered and reconstructed programs; write fresh run receipts."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
folder = root / 'agents/ii_checks_A/recovery_20261121T195642Z'
programs = [
    ('old_02WH', 'agents/ii_checks_A/S6_SERIES_PUBLISH_II_P410_prior_routine_recovery.py'),
    ('old_02WR_02X2', 'agents/ii_checks_A/S6_SERIES_PUBLISH_II_P42_P43_prior_routines_recovery.py'),
    ('new_02WR_prerelease_restored', 'code/S6_SERIES_PUBLISH_II_A_02WR_markings.py'),
    ('new_01FY_prerelease_restored', 'code/S6_SERIES_PUBLISH_II_A_01FY_local.py'),
    ('new_02X2_postrelease_reconstructed', 'code/S6_SERIES_PUBLISH_II_A_recovery_02X2_contraction.py'),
    ('new_02WH_postrelease_reconstructed', 'code/S6_SERIES_PUBLISH_II_A_recovery_02WH_interpolation.py'),
]
rows = []
for name, rel in programs:
    path = root / rel
    start = datetime.now(timezone.utc).isoformat()
    run = subprocess.run([sys.executable, str(path)], cwd=root, capture_output=True, text=True)
    end = datetime.now(timezone.utc).isoformat()
    out = folder / ('S6_SERIES_PUBLISH_II_A_recovery_'+name+'.out')
    out.write_text(run.stdout+run.stderr)
    row = {'scope': name, 'program_path': rel,
           'program_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
           'started_utc': start, 'finished_utc': end, 'exit_code': run.returncode,
           'output_path': str(out.relative_to(root)),
           'output_sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
           'timing_disposition': 'This is a fresh post-reset execution after target proof exposure; it adds no prereading credit.'}
    rows.append(row)
    print(json.dumps(row))
    assert run.returncode == 0, run.stderr
receipt = folder / 'S6_SERIES_PUBLISH_II_A_recovery_group02_03_method_runs.json'
receipt.write_text(json.dumps({'created_utc': datetime.now(timezone.utc).isoformat(),
                              'runs': rows, 'check_events_added': 0}, indent=2)+'\n')
print('RECEIPT', str(receipt.relative_to(root)), hashlib.sha256(receipt.read_bytes()).hexdigest())
