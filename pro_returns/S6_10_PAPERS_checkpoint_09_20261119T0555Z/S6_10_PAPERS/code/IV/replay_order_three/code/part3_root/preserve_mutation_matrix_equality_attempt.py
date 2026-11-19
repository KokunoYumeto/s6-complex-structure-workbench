"""Keep the first unsimplified symbolic-matrix comparison and its output."""
from pathlib import Path
from datetime import datetime,timezone
import json
import shutil

root=Path(__file__).resolve().parents[2]
dest=root/'code/part3_root/attempts/mutation_unsimplified_matrix_equality'
dest.mkdir(parents=True,exist_ok=True)
for suffix in ('py','out','err'):
    source=root/f'code/part3_root/source_cusp_mutation_diagnostic.{suffix}'
    target=dest/source.name
    assert not target.exists(),target
    shutil.copy2(source,target)
(dest/'correction.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),
 'cause':'The symbolic GF relation was tested by syntactic Matrix equality before rational simplification.',
 'correction':'Check every entry of the difference by exact simplification; retain all numerical states and conflicts.'},indent=2)+'\n')
print('Preserved the first symbolic comparison attempt.')
