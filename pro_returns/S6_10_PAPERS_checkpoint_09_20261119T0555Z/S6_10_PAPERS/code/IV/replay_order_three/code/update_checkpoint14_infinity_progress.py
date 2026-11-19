"""Reconcile the completed infinity audit into the checkpoint14 report."""
from datetime import datetime,timezone
from pathlib import Path
import ast
import json
import shutil

root=Path(__file__).resolve().parents[1]
target=root/'code/update_report.py'
old=target.read_text()
needle='Its relative circle-quotient excision comparison and fixed-surface determinant pairing are undergoing complete-map audit; no infinity value from that draft is included among the proved results.'
replacement=('Its complete working excision proof has passed the source, Cartier, cap, finite-isotropy and orientation audit. The actual Hopf-lift transfer gives fixed-scalar positive epsilon return classes0 and1 in the good and reduced branches, respectively, on the initial and reflected vertical-edge fans. The full source/partial-filling construction and this working proof are retained for the next self-contained numbered manuscript addition; neither is included in the236 registered statements of this checkpoint.')
assert old.count(needle)==2 and "'" not in replacement
new=old.replace(needle,replacement)
ast.parse(new)
dest=root/'records/checkpoint14_before_infinity_audit'
dest.mkdir(exist_ok=True)
for source in [target,root/'records/progress_check_14_hours.json']:
    output=dest/source.name
    assert not output.exists(),output
    shutil.copy2(source,output)
target.write_text(new)
path=root/'records/progress_check_14_hours.json'
progress=json.loads(path.read_text())
progress['audit_updated_utc']=datetime.now(timezone.utc).isoformat()
progress['main_question_progress'][5]=('The complete source-infinity working proof now passes the actual partial-attachment, relative-excision and Hopf-transfer audits. Its fixed-scalar positive epsilon return classes are0 and1 in the good and reduced branches, on the initial/reflected vertical-edge fans. All source, root, Cartier, Euler-line, finite-isotropy and orientation maps are retained; the self-contained numbered export follows this checkpoint.')
progress['next_main_steps'][0]='Export the full infinity construction and completed excision proof, then the actual global groupoid and its paired source-zero relation, retaining both individual unknown fan returns.'
path.write_text(json.dumps(progress,indent=2)+'\n')
print('Recorded the completed infinity audit in both report occurrences and the progress decision.')
