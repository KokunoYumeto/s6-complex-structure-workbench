#!/usr/bin/env python3
"""Correct the one component-map reference after checking the admitted KT heading."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
ROOT = Path(__file__).resolve().parents[1]
p = ROOT/'agents/continuation7_iii_corrected_initial_receiving/S6_SERIES_PUBLISH_III_02LU_receiving.tex'
old = p.read_text()
assert sha256(p.read_bytes()).hexdigest() == '9c8c91eb13392909533127cb1a075308d72e1abc6b8f0662791492df87dac699'
a = r'\ref{maps:src:D.2.20}. The nontrivial orders are'
b = r'\ref{maps:src:D.2.19}. The nontrivial orders are'
assert old.count(a) == 1
new = old.replace(a,b)
print('START', datetime.now(timezone.utc).isoformat())
print(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='receiver-before',tofile='receiver-after')),end='')
p.write_text(new)
print('LINES',len(new.splitlines()),'SHA256',sha256(p.read_bytes()).hexdigest())
print('END',datetime.now(timezone.utc).isoformat())
