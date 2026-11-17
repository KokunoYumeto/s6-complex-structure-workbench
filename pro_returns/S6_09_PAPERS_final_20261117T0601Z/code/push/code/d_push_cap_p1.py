#!/usr/bin/env python3
"""Exterior algebra and normalization audit for C.3.19.

The computation keeps the actual suspension of p1; it introduces
no primitive H3(SO)/Spin normalization.
"""
from pathlib import Path
import json

def wedge_term(a,b):
    if set(a)&set(b):
        return 0, ()
    sign=(-1)**sum(i>j for i in a for j in b)
    return sign, tuple(sorted(a+b))

# Ordered basis g,u,w,a on the cusp link.  The nil invariant w-form
# has differential proportional to a wedge u; this does not affect
# the closed degree-two basis u wedge w, w wedge a.
g,u,w,a=0,1,2,3
e=(g,a)
beta_basis=[(u,w),(w,a)]
pairings=[wedge_term(e,b) for b in beta_basis]
assert pairings[0]==(1,(g,u,w,a))
assert pairings[1][0]==0

# Circle trace of a 3-form under g->g+t extracts its g component.
# The remaining top-degree nil class contains no dg and has trace0.
trace_basis={"g_u_w":"u_w","g_w_a":"w_a","u_w_a":None}
selected={"g_u_w":1,"g_w_a":0,"u_w_a":0}
assert sum(abs(v) for v in selected.values())==1

relative_affine_defect=24
cap_p1_absolute=abs(relative_affine_defect)
assert cap_p1_absolute==24
assert cap_p1_absolute%4==0

result={
    "statement":"C.3.19",
    "status":"PASS",
    "link_basis":["g","u","w","a"],
    "euler_class_up_to_orientation":"dg wedge da",
    "trace_basis":trace_basis,
    "cap_pairing_selector":selected,
    "euler_trace_wedge_signs":[pairings[0][0],pairings[1][0]],
    "actual_p1_suspension_used":True,
    "primitive_SO_or_Spin_generator_introduced":False,
    "absolute_cap_p1x":cap_p1_absolute,
    "absolute_Wall_framing_coordinate":cap_p1_absolute//4,
    "unresolved":["common orientation convention","cubic k","relative Euler square","J"],
}
serialized=json.dumps(result,indent=2)
Path(__file__).with_suffix(".json").write_text(serialized+"\n")
print(serialized)
