#!/usr/bin/env python3
"""Bounded notation-order improvements found in the complete final reading."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import csv,difflib
import S6_SERIES_PUBLISH_c8_integrate_units as units
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_later'
PATH=ROOT/'agents/continuation8_iii_integration/units/later/os49_construction.tex'
old=PATH.read_text()
assert sha256(old.encode()).hexdigest()=='98cfc3018aaa18ef5aac0d148ae57ac03639acf5d402f3de14b2adcd8b989b26'
new=old
changes=[]
def edit(before,after,kind,reason,sid):
    global new
    assert new.count(before)==1,(before,new.count(before))
    pos=new.index(before)
    changes.append(dict(type=kind,statement_id=sid,
        old_location='os49_construction.tex v003 line '+str(new[:pos].count('\n')+1),
        old_page='pending final concordance',new_location='same mathematical unit',
        new_page='pending final build',old_text=before,new_text=after,reason=reason,
        review_status='whole v003 read; exact notation/flow change readback pending'))
    new=new.replace(before,after)
start=new.index('Their exact relation to the homology\nmarking is')
end=new.index('We give the period calculation',start)
block=new[start:end]
edit(block,'','D20','Move the full basis diagram after the periods and all its variables have been defined; its insertion is the exact inverse relocation.','night:P3F.27')
anchor='The two units are holomorphic on the cusp disc.  Their full\nintegral change of marking and its inverse are'
edit(anchor,block+'The logarithms \\(U,C\\) are holomorphic on the cusp disc.\nThe full integral change of marking and its inverse are',
     'D20','Insert the complete unchanged basis map after its full-unit periods; distinguish the holomorphic logarithms from their nonvanishing exponentials.','night:P3F.27')
edit('Hence the specified affine generator is genuinely','Hence the specified affine generator is',
     'D08','State the constructed affine generator directly.','night:P3F.26')
edit('carry the same period columns, rather than changing the source.',
     'carry the full period columns of this source.',
     'D02','State the actual period-map consequence directly.','os49:rem:type-c-marking')
units.check_permanent_identifiers(old,new)
TABLE=OUT/'S6_SERIES_PUBLISH_III_os49_construction_publication_defects.tsv'
with TABLE.open(newline='') as handle:
    reader=csv.DictReader(handle,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for item in changes:
    item['change_id']='c8-III-os49_construction-'+str(len(rows)+1).zfill(3)
    rows.append(item)
PATH.write_text(new)
with TABLE.open('w',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=fields,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(rows)
(OUT/'S6_SERIES_PUBLISH_III_os49_construction_publication_v004.diff').write_text(
    ''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),
                               fromfile='construction_v003',tofile='construction_v004')))
print('UTC',datetime.now(timezone.utc).isoformat())
print('OUTPUT',len(new.splitlines()),sha256(new.encode()).hexdigest())
print('EDITS',len(changes),'EXACT_BASIS_DIAGRAM_RELOCATION; ALL_IDENTIFIERS_PRESERVED')
print('NO_NEW_MATHEMATICAL_CONCLUSION; NO_SHARED_WRITES')
