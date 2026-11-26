"""Replay the reconstructed Packet helper against ten retained candidates.

The baselines are recovered by the already-reviewed exact inverse fragments.
They and the complete temporary candidates stay outside the checkpoint.
This program does not change proposal packets or canonical records.
"""
from pathlib import Path
import csv
import hashlib
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT.parents[1] / "tmp"
TAGS = ['02LS', '02LB', '02LC', '02LE', '02LF', '02LJ', '02LT', '02S9', '02SB', '02L9']
guarded = [ROOT / 'S6_SERIES_PUBLISH_III.tex', ROOT / 'CHECK_EVENTS.tsv',
           ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv']
for tag in TAGS:
    guarded.extend((ROOT / 'agents' / f'continuation9_{tag}_notation').glob('*'))
before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in guarded if p.is_file()}
for tag in TAGS:
    candidate = TMP / f'c9_{tag}_notation' / f'S6_SERIES_PUBLISH_c9_{tag}_proposed.tex'
    text = candidate.read_text()
    packet = ROOT / 'agents' / f'continuation9_{tag}_notation' / f'S6_SERIES_PUBLISH_c9_{tag}_notation_defects.tsv'
    rows = list(csv.DictReader(packet.open(), delimiter='\t'))
    for row in reversed(rows):
        assert text.count(row['new_text']) == 1, (tag, row['change_id'], 'inverse uniqueness')
        text = text.replace(row['new_text'], row['old_text'], 1)
    baseline = candidate.parent / f'S6_SERIES_PUBLISH_c9_{tag}_reconstructed_baseline.tex'
    baseline.write_text(text)
    env = dict(os.environ, S6_NOTATION_SOURCE=str(baseline),
               S6_NOTATION_EXPECTED_CANDIDATE=str(candidate), S6_NOTATION_VERIFY_ONLY='1')
    run = subprocess.run([sys.executable, str(ROOT / 'code' / f'S6_SERIES_PUBLISH_c9_{tag}_notation.py')],
                         env=env, cwd=ROOT, text=True, capture_output=True)
    print(run.stdout, end='')
    assert run.returncode == 0, (tag, run.stderr)
for p, value in before.items():
    assert hashlib.sha256(p.read_bytes()).hexdigest() == value, (p, 'unexpected write')
print('All ten exact candidate replays passed. Every admitted packet, event, canonical source and canonical record retained its bytes.')
