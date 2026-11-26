"""Add explicit, checked statement-refutation events to the admission validator.

The extension requires an actual refined label in the reviewed proposed source.
It neither changes ledger bytes nor awards a check by itself.
"""
from pathlib import Path
import datetime as dt
import difflib
import hashlib
import json

R = Path(__file__).resolve().parents[1]
p = R / 'code/S6_SERIES_PUBLISH_continuation2_admit_v2.py'
before = p.read_bytes()
old = "            assert kind in ('targeted proof check','used and rechecked in this run','computation or formal certificate')\n"
new = '            assert kind in (\'targeted proof check\',\'used and rechecked in this run\',\'computation or formal certificate\',\n                            "refuted, with the refined statement\'s id")\n            if kind == "refuted, with the refined statement\'s id":\n                refined_id = e[\'refined_statement_id\']\n                assert refined_id and (\'\\\\label{\' + refined_id + \'}\') in proposed, refined_id\n                assert refined_id in e.get(\'scope\', e.get(\'outcome\', \'\')), refined_id\n'
source = before.decode()
assert source.count(old) == 1
after = source.replace(old, new, 1).encode()
compile(after, str(p), 'exec')
prefix = R / 'records/S6_SERIES_PUBLISH_continuation2_refutation_event_support'
assert not prefix.with_suffix('.json').exists()
diff = ''.join(difflib.unified_diff(source.splitlines(True), after.decode().splitlines(True),
    fromfile='admit_v2.py.before', tofile='admit_v2.py.after'))
prefix.with_suffix('.diff').write_text(diff)
sha = lambda b: hashlib.sha256(b).hexdigest()
receipt = dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
    path=str(p.relative_to(R)), before_sha256=sha(before), after_sha256=sha(after),
    diff=str(prefix.with_suffix('.diff').relative_to(R)),
    diff_sha256=sha(diff.encode()), ledger_writes=0, source_writes=0, check_credit=0,
    purpose="Accept the user's exact refutation event type only with a resolvable refined-statement label and explicit outcome identifier. Preserve the original ledger prefix and the one targeted check per owner requirement.")
p.write_bytes(after)
prefix.with_suffix('.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2))
