#!/usr/bin/env python3
"""Correct live boilerplate; do not modify any immutable checkpoint archive."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for rel in ('checkpoints.md', 'code/refresh_report.py', 'code/record_checkpoint07.py'):
    p = root / rel
    s = p.read_text()
    count = s.count('approximately19:39UTC')
    if count:
        p.write_text(s.replace('approximately19:39UTC', 'approximately19:42UTC'))
        print(rel, count, 'timestamps corrected; immutable archive untouched')
