"""Correct the accent-loop readback defect at its six exact source lines."""
from datetime import datetime,timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
p=u.WORK/'root/local_kummer.tex';before=p.read_text();after=before
fields,rows=r.table(r.DEFECTS);changes=[]
for old in before.splitlines():
 new=re.sub(r"(?:\\')*etale",lambda m:r"\'etale",old)
 if new==old:continue
 assert after.count(old)==1
 after=after.replace(old,new,1)
 ident='III-C8-KUMMER-ACCENT-READBACK-'+str(len(changes)+1)
 assert not any(x['change_id']==ident for x in rows)
 changes.append(dict(change_id=ident,type='D23',statement_id='maps:src:C.1.1; maps:src:C.1.2; maps:src:C.1.3',old_location='final Kummer spelling readback',old_page='pending page concordance',new_location='same exact source line',new_page='pending final PDF',old_text=old,new_text=new,reason='The earlier spelling loop reselected its already accented first substring. Replace each actual mathematical word once with its correct TeX accent, recording both the editor-origin defect and all remaining exact occurrences.',review_status='actual changed contexts read after application; final PDF remains open'))
assert len(changes)==6,len(changes)
s=u.repairs.SOURCE.read_text();assert s.count(before)==1;c=s.replace(before,after,1);u.check_permanent_identifiers(s,c,set(),set())
p.write_text(after,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(c,encoding='utf-8',newline='\n');r.write_table(r.DEFECTS,fields,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat());print('EXACT_ACCENT_ROWS',len(changes))
for x in changes:print(x['new_text'])
