#!/usr/bin/env python3
"""Write the explicit quadric coordinate inverse and one grammar repair."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from datetime import datetime,timezone
import csv,difflib,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_later'
PATH=ROOT/'agents/continuation8_iii_integration/units/later/conifold_constructions.tex'
old=PATH.read_text()
assert sha256(old.encode()).hexdigest()=='2d9b94c8959e1bed1b357db6d0df015173fd9c530dc8b3531e8b8c5a9fd0a40a'
new=old
edits=[]
before=r'''The equation $xy=u(zv-s)$ becomes
$\sum_{j=1}^4 a_j^2=\epsilon>0$ by an invertible complex linear
change of coordinates and a common phase. Writing $a=p+iq$,
its equations are $|p|^2-|q|^2=\epsilon$ and $p\cdot q=0$.'''
after=r'''For the fixed nonzero \(u,s\), choose \(c\in\mathbb C\) with
\(|c|=1\) and \(-c^2s=\epsilon=|s|\). The complex-linear map
and its inverse are
\[
 (a_1,a_2,a_3,a_4)
 =\frac c2\left(\frac{x}{u}+y,\frac{x/u-y}{i},
                         z-v,\frac{z+v}{i}\right),
\]
\[
 x=\frac u c(a_1+ia_2),\quad y=\frac1c(a_1-ia_2),\quad
 z=\frac1c(a_3+ia_4),\quad v=\frac1c(-a_3+ia_4).
\]
They preserve the complex orientations, and
\(\sum a_j^2=c^2(xy/u-zv)=\epsilon\).
Writing \(a=p+iq\), the quadric equations are
\(|p|^2-|q|^2=\epsilon\) and \(p\cdot q=0\).'''
edits.append(('D20','maps:src:D.3.2',before,after,
 'Display the exact complex-linear node-to-quadric map and inverse, retaining the fixed nonzero parameters and complex orientation; this expands the existing coordinate assertion.'))
edits.append(('D23','maps:src:E.2.2',
 '$\\dim_{\\mathbb C}Y+2$. For $Y=B\\times N$ with its projection,\nthen $P\\simeq X\\times N$ holomorphically, is diffeomorphic to',
 '$\\dim_{\\mathbb C}Y+2$. For $Y=B\\times N$ with its projection,\n$P\\simeq X\\times N$ holomorphically, is diffeomorphic to',
 'Remove the residual then after the direct product-specialization wording.'))
p=OUT/'S6_SERIES_PUBLISH_III_conifold_publication_defects.tsv'
with p.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==27
for kind,sid,before,after,reason in edits:
 assert new.count(before)==1
 pos=new.index(before)
 rows.append(dict(change_id='c8-III-conifold-'+str(len(rows)+1).zfill(3),type=kind,
  statement_id=sid,old_location='conifold publication v001 line '+str(new[:pos].count('\n')+1),
  old_page='pending final concordance',new_location='same result and complete proof',
  new_page='pending final build',old_text=before,new_text=after,reason=reason,
  review_status='whole v001 read; exact map manually checked; final changed-scope readback pending'))
 new=new.replace(before,after)
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
 assert Counter(re.findall(pattern,old))==Counter(re.findall(pattern,new))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
(OUT/'S6_SERIES_PUBLISH_III_conifold_publication_v002.diff').write_text(''.join(
 difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='conifold_v001',tofile='conifold_v002')))
PATH.write_text(new)
print('EDITED_UTC',datetime.now(timezone.utc).isoformat())
print('SOURCE_LINES',len(new.splitlines()),'SHA256',sha256(new.encode()).hexdigest())
print('LOCAL_DEFECT_ROWS',len(rows),'NEW_IDENTITIES',0)
print('EXACT_QUADRIC_MAP_AND_INVERSE; ALL_SCOPE_AND_IDENTITIES_PRESERVED')
