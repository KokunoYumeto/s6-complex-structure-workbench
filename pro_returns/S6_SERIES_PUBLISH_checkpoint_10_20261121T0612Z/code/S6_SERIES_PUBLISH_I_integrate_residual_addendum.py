from pathlib import Path
import datetime, hashlib, json
from S6_SERIES_PUBLISH_editing import Editor
r = Path(__file__).resolve().parents[1]
p = r / 'agents/i_analytic/S6_SERIES_PUBLISH_I_final_residual_addendum_guards.json'
d = json.loads(p.read_text());ed = Editor('I')
for g in d['guards']:
    ed.replace(g['old'], g['new'], 'D02', g['reason'], ', '.join(g['statement_ids']))
ed.save()
(r / 'records/S6_SERIES_PUBLISH_I_residual_addendum_integration.json').write_text(json.dumps({
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_sha256': hashlib.sha256(ed.text.encode()).hexdigest(),
    'guards_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
    'scope': 'Both guards and the complete accompanying analytic residual comparison read. The two exponents compare the stated upper envelopes only; they give no lower bound for actual field degrees. Same 28 agent exposed rows; no new root event.'
}, indent=2)+'\n')
