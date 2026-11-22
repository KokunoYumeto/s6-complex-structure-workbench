from pathlib import Path
import datetime as dt
import hashlib
import json

R = Path(__file__).resolve().parents[1]
def bind(p):
    return {'path': p, 'sha256': hashlib.sha256((R / p).read_bytes()).hexdigest()}
old = 'records/S6_SERIES_PUBLISH_II_continuation2_batch52_config.json'
cfg = json.loads((R / old).read_text())
assert bind('S6_SERIES_PUBLISH_II.tex')['sha256'] == cfg['source_before_sha256']
assert bind('CHECK_EVENTS.tsv')['sha256'] == cfg['ledger_before_sha256']
assert not (R / 'records/S6_SERIES_PUBLISH_II_clean_checks_52').exists()
cfg['review_evidence'] = [b for v in cfg['review_evidence']
                          for b in (v if isinstance(v, list) else [v])]
record = 'records/S6_SERIES_PUBLISH_II_batch52_preflight_recovery.json'
assert not (R / record).exists()
(R / record).write_text(json.dumps(dict(
    created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
    original_config=bind(old),
    failure='Admitter preflight rejected a nested list in review_evidence; its check() requires a flat list of file bindings.',
    canonical_source_unchanged=bind('S6_SERIES_PUBLISH_II.tex'),
    canonical_ledger_unchanged=bind('CHECK_EVENTS.tsv'),
    admission_directory_absent=True,
    correction='Flatten only the already reviewed source-receipt bindings. No proof, guard, event, mathematical claim or original config is changed.'
), indent=2) + '\n')
cfg['review_evidence'].append(bind(record))
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch52_config_v2.json'
assert not (R / out).exists()
(R / out).write_text(json.dumps(cfg, indent=2) + '\n')
print(json.dumps(bind(out), indent=2))
