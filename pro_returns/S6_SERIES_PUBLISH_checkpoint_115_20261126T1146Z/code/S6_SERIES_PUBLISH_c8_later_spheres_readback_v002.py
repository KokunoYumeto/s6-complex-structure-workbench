#!/usr/bin/env python3
"""Two bounded prose readback edits; mathematical maps are unchanged."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import difflib
ROOT=Path(__file__).resolve().parents[1]
UNIT=ROOT/'agents/continuation8_iii_integration/units/later/elliptic_sphere_outputs.tex'
OUT=ROOT/'agents/continuation8_iii_later'
old=UNIT.read_text()
assert sha256(old.encode()).hexdigest()=='1650edff1ae21859205bf10f0159c8e85ddc333fc5f29fa1ebccbffc61b8b2ff'
new=old
changes=[
 ('D11',r'\(R_i(v_i)=m_it_i(v_i)\), and the exterior degree-two group is'+'\n'+r'free, so multiplication by \(m_i\) is injective there. Injectivity of multiplication by \(m_i\) determines the fibre coefficient uniquely. The primitive source relation',
  r'\(R_i(v_i)=m_it_i(v_i)\), and the exterior degree-two group is'+'\n'+r'free. Multiplication by \(m_i\) is therefore injective and determines'+'\n'+'the fibre coefficient uniquely. The primitive source relation',
  'Merge the repeated injectivity wording into one sentence; retain the same free-group argument and unique fibre coefficient.'),
 ('D23','\nneck. \n','\nneck.\n','Remove the trailing space left by the preceding exact sentence deletion.')]
table=OUT/'S6_SERIES_PUBLISH_III_spheres_publication_defects.tsv'
with table.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
assert len(rows)==136
for kind,before,after,reason in changes:
 assert new.count(before)==1
 line=new[:new.index(before)].count('\n')+1
 rows.append(dict(change_id=f'c8-III-spheres-{len(rows)+1:03}',type=kind,
  statement_id='maps:src:D.2.25',old_location='elliptic_sphere_outputs.tex readback line '+str(line),
  old_page='pending final page concordance',new_location='same proof paragraph',new_page='pending final build',
  old_text=before,new_text=after,reason=reason,
  review_status='exact readback edit reviewed; whole final reading and root admission pending'))
 new=new.replace(before,after,1)
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
(OUT/'S6_SERIES_PUBLISH_III_spheres_publication_v002.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='spheres_v001',tofile='spheres_v002')),newline='\n')
UNIT.write_text(new,newline='\n')
print('UTC',datetime.now(timezone.utc).isoformat())
print('OUTPUT',len(new.splitlines()),sha256(new.encode()).hexdigest())
print('READBACK_EDITS',len(changes),'TOTAL_LOCAL_DEFECT_ROWS',len(rows))
print('NO_MATHEMATICAL_OR_IDENTIFIER_CHANGE; NO_SHARED_WRITES')
