"""Bind the local coordinate aliases and matching cusp radius explicitly."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
path=u.WORK/'root/quotient_maps.tex';before=path.read_text(encoding='utf-8');after=before
df,rows=r.table(r.DEFECTS)
edits=[
 ('LONG-ALIAS','maps:src:B.3.1','The exact coordinate identity is\n$v=',r'In this differential calculation $u:=u_{\rm long}$ is the real'+ '\n'+r'two-coordinate column of Definition~\ref{mapsIII:def:cusp-suspension-maps};'+ '\n'+r'the inverse notation change is $u_{\rm long}:=u$. The coordinate identity is'+ '\n'+r'$v='),
 ('MATCHING-RADIUS','mapsIII:def:core-collapse','For the original sphere quotient write','For the original sphere quotient use $R=\\epsilon$ and write'),
 ('CORE-CHARACTER','mapsIII:def:core-collapse','The map $q_1:X\\to C$ is the prescribed Seifert quotient on the\nexterior. On the punctured cusp it is',r'Put $\theta_\gamma(x)=e^{2\pi i(u_{\rm long}(x))_1}$ on the punctured cusp.'+'\n'+r'The map $q_1:X\to C$ is the prescribed Seifert quotient on the'+'\n'+'exterior. On the punctured cusp it is'),
 ('REPLACEMENT-REPETITION','maps:src:B.3.3','Choose the quotient replacement $e$ with its replacement supported','Choose the quotient replacement $e$ supported')
]
for key,label,old,new in edits:
 assert after.count(old)==1,key
 after=after.replace(old,new,1)
 ident='III-C8-QUOTIENT-MAPS-READBACK-'+key
 assert not any(x['change_id']==ident for x in rows)
 rows.append(dict(change_id=ident,type='D23' if key=='REPLACEMENT-REPETITION' else 'D20',statement_id=label,old_location='complete quotient-unit readback',old_page='pending page concordance',new_location='Retained-coordinate quotient maps',new_page='pending final PDF',old_text=old,new_text=new,reason='Make the already used coordinate alias, matching base-disc radius or first character literal; the inverse coefficient map and exact quotient maps are unchanged.' if key!='REPLACEMENT-REPETITION' else 'Remove the repeated noun after renaming the construction.',review_status='whole unit read; exact final changes read in actual output; final PDF open'))
source=u.repairs.SOURCE.read_text(encoding='utf-8');assert source.count(before)==1
candidate=source.replace(before,after,1);u.check_permanent_identifiers(source,candidate)
path.write_text(after,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n');r.write_table(r.DEFECTS,df,rows)
print('UTC',datetime.now(timezone.utc).isoformat())
for key,_,_,new in edits: print(key+'\n'+new)
print('EXACT_READBACK_ROWS',len(edits),'ALL_OLD_IDENTITIES_PRESERVED')
