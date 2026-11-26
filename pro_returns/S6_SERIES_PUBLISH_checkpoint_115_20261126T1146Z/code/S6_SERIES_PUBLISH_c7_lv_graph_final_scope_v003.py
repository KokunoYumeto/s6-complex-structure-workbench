#!/usr/bin/env python3
"""Exact final scope clarifications for the LV fresh graph note."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import difflib
root=Path(__file__).resolve().parents[1]
p=root/'agents/continuation7_iii_weighted_os45_graph/S6_SERIES_PUBLISH_III_02LV_global_sphere_and_critical_link.md'
before=p.read_text();after=before
changes=[
('Its inverse is z1=x*w and z0=sqrt(1-|x|^2)*bar(w), after the\nfixed harmless rescaling of the endpoint radial interval. At the\n',
 'Its inverse is z1=x*w and z0=sqrt(1-|x|^2)*bar(w). Choose the\nendpoint interval small enough to lie in the displayed chart. At the\n'),
('its full U M V=Delta decomposition, the inverse matrices, (12)--(15),\n',
 'its full U M V=Delta decomposition and (12)--(15). The inverse\nmatrices are the integral adjugates divided by their determinants\n+1 or -1, with the same coordinate ordering. It records\n'),
('The ordinary class c2 is zero. The degree-four Borel filtration\ntherefore writes c2^S1+T^2=alpha*T+k*T^2. The possible differential\n',
 'The ordinary class c2 is zero. Normalize every degree-two Borel\nlift by subtracting its character at one fixed point times T;\nrestriction at that point is the inverse character reading. The\ndegree-four Borel filtration therefore writes\nc2^S1+T^2=alpha*T+k*T^2 with this normalized alpha. The possible differential\n')]
for a,b in changes:
    assert after.count(a)==1,a
    after=after.replace(a,b)
diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='LV_graph_before_final_scope',tofile='LV_graph_final_scope'))
q=root/'code/S6_SERIES_PUBLISH_c7_lv_graph_final_scope_v003.diff'
assert not q.exists()
print('START',datetime.now(timezone.utc).isoformat())
print('BEFORE',len(before.splitlines()),sha256(before.encode()).hexdigest())
p.write_text(after);q.write_text(diff)
print('AFTER',len(after.splitlines()),sha256(p.read_bytes()).hexdigest())
print('DIFF',sha256(q.read_bytes()).hexdigest())
print('COMPLETE',len(changes),'exact scope clarifications; no mathematical execution rerun')
print('END',datetime.now(timezone.utc).isoformat())
