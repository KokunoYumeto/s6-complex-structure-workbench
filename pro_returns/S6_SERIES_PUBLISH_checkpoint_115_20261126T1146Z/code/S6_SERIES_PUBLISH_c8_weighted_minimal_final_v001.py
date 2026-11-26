"""Two exact notation follow-ups found in the fully read readback diff."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root=Path(__file__).resolve().parent.parent
p=root/'agents/continuation8_iii_integration/units/weighted/minimal_primary_types.tex'
lane=root/'agents/continuation8_iii_weighted_units'
original=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='1a3eeed4699e16a89a5a1501b4eb7f02002b4e2282e55fd57a5238be18c6c8c4'
text=original
edits=[(r' x=Cv,\qquad v=C_0^{-1}x,',r' x=C_0v,\qquad v=C_0^{-1}x,'),
       (r' \varphi(Cv)=-\psi(v)+L_0v.',r' \varphi(C_0v)=-\psi(v)+L_0v.')]
table=lane/'S6_SERIES_PUBLISH_MINIMAL_publication_defects.tsv'
with table.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
assert len(rows)==822
for i,(old,new) in enumerate(edits,1):
 assert text.count(old)==1
 line=text.count('\n',0,text.index(old))+1
 text=text.replace(old,new)
 rows.append(dict(zip(fields,[f'III-C8-MINIMAL-FINAL-{i:03d}-D20','D20','maps:src:D.2.35',f'minimal_primary_types.tex line{line}','pending page concordance','weighted/minimal_primary_types.tex','pending final build',old,new,'Complete the C0 matrix notation in both Cv products; the same coordinate map and its displayed inverse are unchanged. C remains the fixed curve.','whole candidate and complete readback diff read; exact final edit read; global gates open'])))
units.check_permanent_identifiers(original,text)
p.write_text(text,newline='\n')
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows)
print('UTC',datetime.now(timezone.utc).isoformat())
for old,new in edits: print('EXACT_CHANGE',repr(old),'TO',repr(new))
print('FINAL_LINES',len(text.splitlines()),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest(),'DEFECT_ROWS',len(rows),'EXACT_EDITS424; GLOBAL_GATES_OPEN; SHARED_WRITES0')
