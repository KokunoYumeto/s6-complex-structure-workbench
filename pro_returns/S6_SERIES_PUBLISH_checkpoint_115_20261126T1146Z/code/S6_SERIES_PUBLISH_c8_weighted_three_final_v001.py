"""Finish four product occurrences of the read-back Borel symbol change."""
import csv
from datetime import datetime, timezone
import difflib
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root=Path(__file__).resolve().parent.parent
p=root/'agents/continuation8_iii_integration/units/weighted/three_primary_types.tex'
lane=root/'agents/continuation8_iii_weighted_units'
old=p.read_text();text=old
assert hashlib.sha256(p.read_bytes()).hexdigest()=='a5ae6c288d323100b5b91b90a37c3192239bb02ba22b1a1e6b4de3a581dfc7a6'
edits=[]
for token,new,count in [(r'\rho_3(Az)',r'\rho_3(Az_C)',2),
                        (r'\rho_9(A^3z^3)',r'\rho_9(A^3z_C^3)',1),
                        (r'\rho_9(A^3k^2T^2z)',r'\rho_9(A^3k^2T^2z_C)',1)]:
 assert text.count(token)==count,(token,text.count(token))
 for _ in range(count):
  at=text.index(token);owner='LF' if at<text.index(r'\subsubsection{Orders six') else 'LJ'
  edits.append((owner,text.count('\n',0,at)+1,token,new))
  text=text[:at]+new+text[at+len(token):]
units.check_permanent_identifiers(old,text)
table=lane/'S6_SERIES_PUBLISH_THREE_publication_defects.tsv'
with table.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
for i,(owner,line,before,after) in enumerate(edits,1):
 rows.append(dict(zip(fields,[f'III-C8-THREE-FINAL-{i:03d}-D20','D20',
  'maps:src:D.2.'+('39' if owner=='LF' else '42'),f'three_primary_types.tex final edit line{line}',
  'pending page concordance','weighted/three_primary_types.tex','pending final build',before,after,
  'Complete the same Borel hyperplane symbol change inside juxtaposed products; the full diff readback caught the word-boundary omission. No mathematical term or coordinate map changes.',
  'whole input/candidate and full correction diff read; final bounded readback pending; global gates open'])))
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p.write_text(text,newline='\n')
diff=''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile='THREE2355_readback',tofile='THREE2355_final'))
(lane/'S6_SERIES_PUBLISH_THREE_final_corrections.diff').write_text(diff,newline='\n')
print('UTC',datetime.now(timezone.utc).isoformat())
print('LINES',len(text.splitlines()),'FINAL_EDITS',len(edits),'TOTAL_ROWS',len(rows))
print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print(diff,end='')
