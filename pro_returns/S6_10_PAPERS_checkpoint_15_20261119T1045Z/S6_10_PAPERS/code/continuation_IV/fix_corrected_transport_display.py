#!/usr/bin/env python3
"""Split the known 19.07602pt K41 transport display after checkpoint09.

No equation is altered. The exact old/new text and source hashes are kept.
Run without --apply for a preview. Root owns canonical assembly/build.
"""
from pathlib import Path
import argparse,hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[2]
OLD=r'''\[
 F_1\psi_X=\psi_YF_0,\qquad
 A=E_Y^{-1}F_1E_XF_0^{-1},\qquad
 F_0\Phi_XF_0^{-1}=A^{-1}\Phi_Y,
 \quad\Phi_X=E_X^{-1}\psi_X,\quad\Phi_Y=E_Y^{-1}\psi_Y.
\]'''
NEW=r'''\[
\begin{aligned}
 F_1\psi_X&=\psi_YF_0,
 & A&=E_Y^{-1}F_1E_XF_0^{-1},\\
 F_0\Phi_XF_0^{-1}&=A^{-1}\Phi_Y,\\
 \Phi_X&=E_X^{-1}\psi_X,
 & \Phi_Y&=E_Y^{-1}\psi_Y.
\end{aligned}
\]'''
ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
receipt=[]
for rel in ['papers/IV/corrected_physical_items.tex','papers/IV/body.tex','papers/IV/body_source.tex','code/continuation_IV/corrected_items.py']:
 p=ROOT/rel;s=p.read_text();assert s.count(OLD)==1,(rel,s.count(OLD))
 t=s.replace(OLD,NEW,1)
 receipt.append(dict(path=rel,before_sha256=hashlib.sha256(s.encode()).hexdigest(),after_sha256=hashlib.sha256(t.encode()).hexdigest(),old=OLD,new=NEW))
 if a.apply:p.write_text(t)
out=dict(created_at=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),applied=a.apply,
 source_issue='Root observed19.07602pt overfull hbox at canonical IV line75231/PDFpage996 after the05:42:55 build snapshot.',
 scope='Line breaking only; all five equations and their order are unchanged.',files=receipt)
name='corrected_transport_layout_patch.json' if a.apply else 'corrected_transport_layout_preview.json'
(ROOT/'analysis/continuation_IV'/name).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'applied':a.apply,'files':len(receipt),'receipt':name}))
