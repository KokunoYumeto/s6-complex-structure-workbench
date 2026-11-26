#!/usr/bin/env python3
"""Replace the global principal-divisor wording by the proved cohomology map."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import difflib
root=Path(__file__).resolve().parents[1]
p=root/'agents/continuation7_iii_weighted_os45_graph/S6_SERIES_PUBLISH_III_02LV_global_sphere_and_critical_link.md'
before=p.read_text();after=before
changes=[
('classes are individually zero as well, by their weight-zero\nframes and the principal whole-fibre class.\n',
 'classes are individually zero as well. For a base line of degree\nk, its ordinary pulled-back first Chern class is k times the\nalready-proved integral relation sum_i D_i=0. Its equivariant\nclass therefore equals mT by the degree-two Borel sequence. At\na fixed point the base action and its line weight are zero, so\nrestriction gives m=0. This proves the equivariant vanishing\nfor L and the Hodge line, without asserting that an effective\nglobal fibre divisor is holomorphically principal.\n'),
('makes all coefficients equal on the connected graph; their sum\nis the principal whole fibre. Since H^2(X;Z) is free, alpha=0.\n',
 'makes all coefficients equal on the connected graph; their class\nis a multiple of the proved integral relation sum_i D_i=0.\nSince H^2(X;Z) is free, alpha=0.\n')]
for a,b in changes:
    assert after.count(a)==1,a
    after=after.replace(a,b)
q=root/'code/S6_SERIES_PUBLISH_c7_lv_graph_equivariant_scope_v004.diff'
assert not q.exists()
diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='LV_graph_before_equivariant_scope',tofile='LV_graph_exact_equivariant_scope'))
print('START',datetime.now(timezone.utc).isoformat())
print('BEFORE',len(before.splitlines()),sha256(before.encode()).hexdigest())
p.write_text(after);q.write_text(diff)
print('AFTER',len(after.splitlines()),sha256(p.read_bytes()).hexdigest())
print('DIFF',sha256(q.read_bytes()).hexdigest())
print('COMPLETE',len(changes),'exact cohomology scope replacements; no mathematical execution rerun')
print('END',datetime.now(timezone.utc).isoformat())
