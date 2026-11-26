#!/usr/bin/env python3
"""Retain and correct the one failed LV clarification context, once."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib

root=Path(__file__).resolve().parents[1]
path=root/'agents/continuation7_iii_weighted_os45_graph/S6_SERIES_PUBLISH_III_02LV_global_sphere_and_critical_link.md'
failed=root/'code/S6_SERIES_PUBLISH_c7_lv_graph_clarification_failed_v001.patch'
raw=failed.read_text()
before=path.read_text()
old='@@\n-The possible differential\n-from H3(X;Z)=Z/8 into the free terms H2(X;Z)*T and Z*T^2 is zero;\n+The possible differential\n+from H^3(X;Z)=Z/8 into the free terms H^2(X;Z)*T and Z*T^2 is zero;'
new='@@\n-therefore writes c2^S1+T^2=alpha*T+k*T^2. The possible differential\n-from H3(X;Z)=Z/8 into the free terms H2(X;Z)*T and Z*T^2 is zero;\n+therefore writes c2^S1+T^2=alpha*T+k*T^2. The possible differential\n+from H^3(X;Z)=Z/8 into the free terms H^2(X;Z)*T and Z*T^2 is zero;'
assert raw.count(old)==1
corrected=raw.replace(old,new)
lines=corrected.splitlines(keepends=True)
assert lines[0]=='*** Begin Patch\n' and lines[-1]=='*** End Patch\n'
hunks=[]
for line in lines[2:-1]:
    if line.startswith('@@'):
        hunks.append([])
    else:
        assert line[0] in ' +-'
        hunks[-1].append(line)
after=before
for hunk in hunks:
    oldpart=''.join(line[1:] for line in hunk if line[0] in ' -')
    newpart=''.join(line[1:] for line in hunk if line[0] in ' +')
    assert after.count(oldpart)==1,oldpart
    after=after.replace(oldpart,newpart)

anchor='differential frame rho is invariant away from C.\n'
addition='''
The endpoint differential normalization is explicit after the push-off.
In its quotient chart put R2=|x|^2+|y|^2. The kernel column and
the horizontal column of df are (x,-y) and (bar y,bar x)/R2.
Their matrix has determinant one and inverse
[[bar x/R2,-bar y/R2],[y,x]]. Substituting (7) makes R2 everywhere
positive. Positive column rescaling gives the Bott matrix of
Section 7, with Hermitian-transpose inverse. These functions depend
only on the quotient disc, so the normalization is invariant under
the scalar action and descends to that disc. The collar formula
is unchanged where chi=0. On the core the same assertion follows
from the actual source-line matrix immediately below. Thus the
complete comparison of the moved differential quotient frame with
a chosen frame of TY over Sigma is a single map
Sigma -> GL2(C), including both endpoint Bott normalizations.
Its determinant and SU2 parts are nullhomotopic on Sigma=S2.
Pulling back therefore adds no degree-three term to (10).
'''
assert after.count(anchor)==1
after=after.replace(anchor,anchor+addition)
diff=''.join(difflib.unified_diff(before.splitlines(keepends=True),after.splitlines(keepends=True),fromfile='LV_graph_before_clarifications',tofile='LV_graph_after_clarifications'))
assert diff
diffpath=root/'code/S6_SERIES_PUBLISH_c7_lv_graph_clarification_v002.diff'
assert not diffpath.exists()
print('START',datetime.now(timezone.utc).isoformat())
print('FAILED_PATCH_SHA256',sha256(failed.read_bytes()).hexdigest())
print('BEFORE',len(before.splitlines()),sha256(before.encode()).hexdigest())
path.write_text(after)
diffpath.write_text(diff)
print('AFTER',len(after.splitlines()),sha256(path.read_bytes()).hexdigest())
print('DIFF',str(diffpath),sha256(diffpath.read_bytes()).hexdigest())
print('COMPLETE',len(hunks),'exact corrected hunks and one explicit endpoint paragraph; no mathematical execution rerun')
print('END',datetime.now(timezone.utc).isoformat())
