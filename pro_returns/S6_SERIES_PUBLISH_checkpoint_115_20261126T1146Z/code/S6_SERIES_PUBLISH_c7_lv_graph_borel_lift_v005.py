#!/usr/bin/env python3
"""State the final normalized Borel-lift inverse; no mathematical rerun."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import difflib
root=Path(__file__).resolve().parents[1]
lane=root/'agents/continuation7_iii_weighted_os45_graph'
p=lane/'S6_SERIES_PUBLISH_III_02LV_global_sphere_and_critical_link.md'
scope=lane/'S6_SERIES_PUBLISH_III_02LV_graph_input_and_execution_scope.md'
before=p.read_text();oldscope=scope.read_text()
assert sha256(before.encode()).hexdigest()=='3223e470396d5055df09a54a142b7db6c0447559359754f73c5f7af376a8fb29'
a='Since H^2(X;Z) is free, alpha=0.\nWe have proved the exact integral identity\n'
b='Since H^2(X;Z) is free, the ordinary class underlying alpha is\nzero. Its Borel lift is then mT. The chosen normalized character\nat the fixed point is zero, so m=0; hence alpha=0 in H^2(B;Z).\nWe have proved the exact integral identity\n'
assert before.count(a)==1
after=before.replace(a,b)
assert oldscope.count('The three retained text-only editors are\n')==1
newscope=oldscope.replace('The three retained text-only editors are\n','The four retained text-only editors are\n')
a='`c7_lv_graph_final_scope_v003.py`, and\n`c7_lv_graph_equivariant_scope_v004.py`, each with the common\n'
b='`c7_lv_graph_final_scope_v003.py`,\n`c7_lv_graph_equivariant_scope_v004.py`, and\n`c7_lv_graph_borel_lift_v005.py`, each with the common\n'
assert newscope.count(a)==1
newscope=newscope.replace(a,b)
diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='LV_graph_before_final_Borel_lift',tofile='LV_graph_final_Borel_lift'))
diff+=''.join(difflib.unified_diff(oldscope.splitlines(True),newscope.splitlines(True),fromfile='LV_scope_before_v005',tofile='LV_scope_after_v005'))
q=root/'code/S6_SERIES_PUBLISH_c7_lv_graph_borel_lift_v005.diff'
assert not q.exists()
print('START',datetime.now(timezone.utc).isoformat())
p.write_text(after);scope.write_text(newscope);q.write_text(diff)
print(diff,end='')
print('PROOF',len(after.splitlines()),sha256(p.read_bytes()).hexdigest())
print('SCOPE',len(newscope.splitlines()),sha256(scope.read_bytes()).hexdigest())
print('DIFF',sha256(q.read_bytes()).hexdigest())
print('COMPLETE exact final bridge and editor-scope update; no mathematical rerun')
print('END',datetime.now(timezone.utc).isoformat())
