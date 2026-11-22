from pathlib import Path
import json, hashlib, datetime
from S6_SERIES_PUBLISH_editing import Editor

r = Path(__file__).resolve().parents[1]
p = r / 'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_batch7_guarded.json'
d = json.loads(p.read_text())
ed = Editor('I')
before_sha = hashlib.sha256(ed.text.encode()).hexdigest()
for x in d['patches']:
    kind = 'D16' if 'locator' in x['reason'] or 'primary' in x['reason'] else 'D09' if 'program' in x['reason'].lower() else 'D07'
    ed.replace(x['old'], x['new'], kind, x['reason'], ', '.join(x.get('statement_ids', [])))
ed.save()
(r / 'records/S6_SERIES_PUBLISH_I_boundary7_integration.json').write_text(json.dumps({
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'before_sha256': before_sha,
    'after_sha256': hashlib.sha256(ed.text.encode()).hexdigest(),
    'guard_file': str(p.relative_to(r)),
    'guard_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
    'guards': len(d['patches']),
    'scope': 'Root read all changed mathematical passages, deletion scopes, primary-locator diffs, and the complete agent comparison. The exact collar rational coordinate map and conductor differential calculation are retained. All labels and permanent targets are preserved. The 26 exposed rereads belong to the agent event bundle; this integration creates no additional check event.'
}, indent=2) + '\n')
