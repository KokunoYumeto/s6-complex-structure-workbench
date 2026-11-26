#!/usr/bin/env python3
"""Finish the receiver readback: valid multi-column alignment, accents, no closing recap."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'agents/continuation7_iii_corrected_initial_receiving/S6_SERIES_PUBLISH_III_02LU_receiving.tex'
old=p.read_text()
assert sha256(p.read_bytes()).hexdigest()=='13d769e14a5163e451a7d897bb086d6aeea43186da639728faa3069935e7dd00'
assert old.count(r'\begin{split}')==old.count(r'\end{split}')==1
new=old.replace(r'\begin{split}',r'\begin{aligned}').replace(r'\end{split}',r'\end{aligned}')
new=new.replace('Bezout',r"B\'ezout")
ending='''Thus the specified original-cap inputs, all supplied
integral corrections in their proved local scope, and
all finite affine parameters enter one finite exact
presentation and homology construction.
'''
assert new.count(ending)==1
new=new.replace(ending,'')
print('START',datetime.now(timezone.utc).isoformat())
print(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='receiver-before',tofile='receiver-after')),end='')
p.write_text(new)
print('LINES',len(new.splitlines()),'SHA256',sha256(p.read_bytes()).hexdigest())
print('END',datetime.now(timezone.utc).isoformat())
