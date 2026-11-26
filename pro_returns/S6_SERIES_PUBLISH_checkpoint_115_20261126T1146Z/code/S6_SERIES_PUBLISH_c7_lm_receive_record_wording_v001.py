#!/usr/bin/env python3
"""Narrow local D27 proposal correction: the zero element has order one."""
from pathlib import Path
from hashlib import sha256
import csv

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_residual_twenty_receiving'
STEM='S6_SERIES_PUBLISH_III_02LM_'
receiver=LANE/(STEM+'receiving.tex')
comparison=LANE/(STEM+'comparison.md')
def digest(p):return sha256(p.read_bytes()).hexdigest()
held={receiver:digest(receiver),comparison:digest(comparison)}
changes=[
 ('defects','reason','c7-III-02LM-smooth-types','change_id',
  'respectively2 versus0,0 versus2,5 versus10',
  'respectively 2 versus 1, 1 versus 2, and 5 versus 10'),
 ('CHECK_EVENTS','outcome','publish:c7:III:02LM:smooth-identification-refuted','event_id',
  'refined P of order2 versus0,0 versus2,or5 versus10',
  'refined P of orders 2 versus 1, 1 versus 2, or 5 versus 10'),
]
extra='; '.join('code/S6_SERIES_PUBLISH_c7_lm_receive_record_wording_v001'+ext
               for ext in ('.py','.out','.err'))
for name,field,identity,idfield,old,new in changes:
    p=LANE/(STEM+name+'.tsv');before=digest(p)
    with p.open(newline='') as f:
        reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames
        rows=list(reader)
    selected=[row for row in rows if row[idfield]==identity]
    assert len(selected)==1 and selected[0][field].count(old)==1
    selected[0][field]=selected[0][field].replace(old,new,1)
    if name=='CHECK_EVENTS':
        for row in rows:
            assert 'record_wording_v001' not in row['where']
            row['where']+='; '+extra
    with p.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)
    with p.open(newline='') as f:assert list(csv.DictReader(f,delimiter='\t'))==rows
    assert b'\r' not in p.read_bytes()
    print('EXACT_WORDING',name,repr(old),'->',repr(new),flush=True)
    print('BEFORE_SHA256',before,p.name,flush=True)
    print('AFTER_SHA256',digest(p),p.name,flush=True)
note=LANE/(STEM+'post_exposure_auxiliaries.md')
addition=(
 '\n## 7. Final proposal wording correction\n\n'
 'The first local records preparation succeeded, and its complete source and\n'
 'streams are retained. Its D27 reason and refutation event called the order\n'
 'of the zero refined class zero. The zero class has order one. The narrow\n'
 'retained record_wording_v001 source changes exactly those two phrases to\n'
 'orders 2 versus 1, 1 versus 2, and 5 versus 10, and adds its own evidence\n'
 'paths to the four events. The receiver and mathematical comparison are\n'
 'unchanged. The correction output records both proposal hashes before and\n'
 'after the edit, and its separate stderr is retained. No frozen fresh or\n'
 'canonical/global file is changed.\n')
assert '## 7. Final proposal wording correction' not in note.read_text()
note.write_text(note.read_text()+addition,newline='\n')
for p,h in held.items():assert digest(p)==h
print('RECEIVER_UNCHANGED_SHA256',digest(receiver),flush=True)
print('COMPARISON_UNCHANGED_SHA256',digest(comparison),flush=True)
print('AUXILIARY_NOTE_SHA256',digest(note),flush=True)
print('PASS narrow local wording correction, exact roundtrip and held mathematical bytes.',flush=True)
