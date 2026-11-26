#!/usr/bin/env python3
"""Stage statement-only KU inputs and the pinned response archive."""
from pathlib import Path
import csv
import io
import json

root = Path(__file__).resolve().parents[1]
temporary = root.parents[1] / 'ku_archived_temp'
folder = root / 'agents/continuation7_iii_ku'
folder.mkdir(exist_ok=True)
raw = folder / 'raw_responses'
raw.mkdir(exist_ok=True)
files = sorted(temporary.glob('all21_*.json')) + sorted(temporary.glob('semistable_*_clutch*.json'))
assert len(files) == 58
assert sum(p.name.startswith('all21_') for p in files) == 50
for path in files:
    data = path.read_bytes()
    assert b'\r\n' not in data
    obj = json.loads(data)
    assert all(key in obj for key in ('input', 'response', 'url'))
    target = raw / path.name
    assert not target.exists() or target.read_bytes() == data
    target.write_bytes(data)

claims = (root / 'agents/continuation5_iii_infra/S6_SERIES_PUBLISH_III_02LX_claim_inputs.tex').read_text()
claim = claims.split('% Dependency 02KU:', 1)[1]
claim = claim[claim.index('\\begin{computed}'):]
assert claim.rstrip().endswith('\\end{computed}')
compendium = root.parent / 'S6_GRIND_4_s6_09_compendium/S6_09_PAPERS_III.tex'
source = compendium.read_text()
start = source.rfind('\\begin{proposition}', 0, source.index('\\label{maps:src:D.2.1}'))
end = source.index('\\end{proposition}', start) + len('\\end{proposition}')
definition = source[start:end]
assert '\\begin{proof}' not in definition
packet = folder / 'S6_SERIES_PUBLISH_III_02KU_claim_inputs.tex'
packet.write_text('% Exact mathematical claim and catalogue statement only.\n'
                  '% KU original audit narrative and all earlier algorithms remain embargoed.\n\n'
                  + claim.rstrip() + '\n\n% Exact catalogue statement input.\n'
                  + definition + '\n', newline='\n')

progress = root / 'S6_SERIES_PUBLISH_required_progress_III.tsv'
with progress.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row = next(r for r in rows if r['tag'] == '02KU')
assert row['status'] == 'open' and row['proof_status'] == 'embargoed'
row['statement_packet'] = str(packet.relative_to(root))
row['packet_status'] = 'statement_ready_for_fresh_check'
row['statement_status'] = 'exact_claim_only_packet'
row['notes'] += (' Continuation-seven claim-only packet and 58 pinned archived responses are staged. '
                 'Retrieval is no mathematical check. Root has read the original audit narrative; '
                 'a separately unexposed checker must write the new bounded audit before release.')
buf = io.StringIO(newline='')
writer = csv.DictWriter(buf, fields, delimiter='\t', lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
progress.write_text(buf.getvalue(), newline='\n')
print('Staged 50 main and 8 clutch response inputs, with exact claim/catalogue statements.')
print('KU original audit remains embargoed; no computation or closure credit.')
