#!/usr/bin/env python3
"""Immediately record a web source opened in this blind subtask."""
from pathlib import Path
from datetime import datetime,timezone
import argparse
p=argparse.ArgumentParser()
p.add_argument('url');p.add_argument('--reason',required=True);p.add_argument('--material',required=True)
a=p.parse_args()
root=Path(__file__).resolve().parents[2]
with (root/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened `'+a.url+'`; reason: '+a.reason+'; material: '+a.material+'.\n')
