"""Preserve the first certificate's syntactic matrix-equality failure."""
from pathlib import Path
from datetime import datetime, timezone
import json, shutil
root = Path(__file__).resolve().parents[2]
dest = root / 'code/part3_root/attempts/general_fan_unsimplified_matrix_equality'
dest.mkdir(parents=True, exist_ok=False)
for suffix in ['py', 'out', 'err']:
    source = root / ('code/part3_root/source_cusp_general_fan_product.' + suffix)
    shutil.copy2(source, dest / source.name)
record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'failure': 'SymPy structural equality compared R*P to I before reducing its rational entries.',
    'correction': 'Check every entry of R*P-I after exact rational simplification.',
    'mathematical_scope': 'No change to the exact character or period maps.'
}
(dest / 'erratum.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
