"""Apply the fully compared tail consolidation and presentation guards once."""
import datetime, hashlib, json
from pathlib import Path
from S6_SERIES_PUBLISH_editing import Editor

root = Path(__file__).resolve().parents[1]
path = root / 'agents/i_provenance/S6_SERIES_PUBLISH_I_candidate11_tail_guards.json'
data = json.loads(path.read_text())
ed = Editor('I')
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha(ed.before.encode()) == data['source_sha256']
for g in data['changes']:
    kind = ('D12' if g['id'].endswith('T16') else 'D06' if g['id'].endswith(('T07','T08','T09'))
            else 'D08' if g['id'].endswith('T10') else 'D02' if g['id'].endswith(('T17','T18')) else 'D23')
    ed.replace(g['old'], g['new'], kind, g['reason'], g['statement'])
ed.save()
receipt = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'guard_sha256': sha(path.read_bytes()), 'source_before_sha256': data['source_sha256'],
           'source_after_sha256': sha(ed.text.encode()), 'applied_guards': len(data['changes']),
           'proof_comparison': 'agents/i_provenance/S6_SERIES_PUBLISH_I_candidate11_tail_comparison.md',
           'root_reading': 'All18 old/new guards read; the full old/new night:P5.5 proof compared. Other complete proof comparisons delegated and recorded by provenance.',
           'new_events_by_root': 0,
           'existing_events': 'The two exposed Aut-label associations reuse the one agent evidence group.'}
(root / 'records/S6_SERIES_PUBLISH_I_candidate12_tail_applied.json').write_text(json.dumps(receipt, indent=2) + '\n')
