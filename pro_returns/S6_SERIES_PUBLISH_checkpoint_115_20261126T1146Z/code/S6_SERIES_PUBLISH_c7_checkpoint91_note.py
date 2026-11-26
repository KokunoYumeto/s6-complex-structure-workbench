"""Retain the executed packer and replace its dated note with current scope."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'code/S6_SERIES_PUBLISH_c7_checkpoint.py'
before = path.read_text()
backup = ROOT / 'code/S6_SERIES_PUBLISH_c7_checkpoint_pre91.py'
assert not backup.exists()
first = before.index("    section = f'''\n")
last = before.index("    for name in ('S6_SERIES_PUBLISH_report.md', 'PROGRESS_LEDGER.md'):", first)
replacement = '''    section = f\'\'\'

## Checkpoint {args.number} — {now.isoformat()}

Paper III has {len(done)}/128 required checks complete. Newly closed
since the previous checkpoint: {', '.join(newly_closed) or 'none'}.
LS was admitted at10:58:36.188625 UTC after the full original,
787-line receiver, all auxiliaries, exact maps and actual streams
were read. Its two guarded replacements, five defects and three
scoped events are retained; the canonical source is unchanged.

LT's historical220-line source was replayed unchanged and reproduced
all120275 saved JSON bytes. Root read all488 new audit lines and the
exact byte-inverse reader. Its two bounded auxiliary repairs have
complete maps and concrete examples. The973-line receiver and313-line
comparison are staged; root whole reading and admission remain open.

LV's complete936-line fresh proof froze11:16:04.388868 UTC. It proves
the full invariant package, actual global primitive sphere, reference
parity one and direct critical-chain intersection minus one. Every
fresh source/actual output and all2591 graph JSON lines were read.
The individual original was released11:18:22.502431 UTC, proof lines
21514--22383, after that completed derivation. Its full comparison
remains open. The failed first location guard and actual traceback
are retained. LT/LV close no invented required identities.

LG remains the sole required identity open. Its new raw-fixture
catalogue has been executed and agent-read; the complete fresh
synthesis and root whole reading still await LT/LV final comparisons.
LG's original and historical target inputs remain closed.

All {unit_open['III']} III unit criteria and all66 IV required checks
and {unit_open['IV']} IV unit criteria remain open. III's source SHA256
is {source_sha}. Provenance, final build and every-page review follow
the required checks and final unit pass. IV follows III; I/II/V wait
for the joint final step. Review63 recorded movement; the consecutive
no-movement count is zero. Packaging earns no movement credit.
Next checkpoint: {(due + timedelta(minutes=45)).isoformat()}.
Next hourly review: {next_review.isoformat()}. The report is INCOMPLETE.
\'\'\'
'''
after = before[:first] + replacement + before[last:]
backup.write_text(before, newline='\n')
path.write_text(after, newline='\n')
print('UPDATED', datetime.now(timezone.utc).isoformat())
print('PREVIOUS_SOURCE', len(before.encode()), sha256(before.encode()).hexdigest())
print('CURRENT_SOURCE', len(after.encode()), sha256(after.encode()).hexdigest())
print('EXACT_REPLACEMENT_BEGIN')
print(replacement, end='')
print('EXACT_REPLACEMENT_END')
