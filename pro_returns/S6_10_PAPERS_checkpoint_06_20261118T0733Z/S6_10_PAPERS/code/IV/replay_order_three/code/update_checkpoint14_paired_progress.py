"""Retain the newly completed paired source-zero working consequence."""
from datetime import datetime,timezone
from pathlib import Path
import ast
import json
import shutil

root=Path(__file__).resolve().parents[1]
target=root/'code/update_report.py'
old=target.read_text()
needle='The global rho-family working relation retains both source-zero fan objects, every scalar closing arrow, the half-source period/reflection map and the full infinity source/Cartier/root dictionary.'
replacement=(needle+' Its completed working corollary, for N=k*m and the initial/reflected fan pair, gives the source-zero paired sum-1 in the good branch(1,2,4p), and-2+2k(1-3p) in the reduced branch(2,1,4p-1), modulo28. This uses the actual infinity root winding-2k and the two-parameter scalar square; it assigns neither individual fan return.')
assert old.count(needle)==2 and "'" not in replacement
new=old.replace(needle,replacement)
ast.parse(new)
dest=root/'records/checkpoint14_before_paired_corollary'
dest.mkdir(exist_ok=True)
for source in [target,root/'records/progress_check_14_hours.json']:
    output=dest/source.name
    assert not output.exists(),output
    shutil.copy2(source,output)
target.write_text(new)
path=root/'records/progress_check_14_hours.json'
progress=json.loads(path.read_text())
progress['audit_updated_utc']=datetime.now(timezone.utc).isoformat()
progress['main_question_progress'].append('The audited full groupoid and infinity arrows now determine the paired source-zero sums-1 and-2+2k(1-3p) modulo28 for the good and reduced initial/reflected fan pairs. Both individual returns remain open; no class is divided.')
path.write_text(json.dumps(progress,indent=2)+'\n')
print('Paired-return working corollary recorded; the numbered master remains236 statements.')
