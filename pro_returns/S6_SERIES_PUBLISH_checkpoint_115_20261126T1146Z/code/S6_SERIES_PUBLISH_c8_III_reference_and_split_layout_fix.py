"""Repair the three observed spaced keys and the two-pair aligned display."""
from datetime import datetime, timezone
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now=datetime.now(timezone.utc).isoformat()
source=u.repairs.SOURCE.read_text(encoding='utf-8');candidate=source
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
front=u.WORK/'root/front_matter.tex';front_old=front.read_text(encoding='utf-8');front_new=front_old
labels=set(re.findall(r'\\label\{([^{}]+)\}',source))
changed=[]
for m in re.finditer(r'\\(?:ref|eqref|cref|Cref|autoref|pageref)\*?\{([^{}]+)\}',source):
    keys=m[1].split(',')
    if any(k!=k.strip() for k in keys):
        assert all(k.strip() in labels for k in keys)
        old=m[0];new=old[:old.index('{')+1]+','.join(k.strip() for k in keys)+'}'
        assert candidate.count(old)==front_new.count(old)==1
        candidate=candidate.replace(old,new,1);front_new=front_new.replace(old,new,1)
        changed.append((old,new,'D04','series:III:main-theorems' if len(changed)<2 else 'the-proofs-in-outline','Actual pass01 warnings expose a newline-produced leading blank in one key. Each retained comma-separated key now equals its exact existing label; the complete key list and order are unchanged. Root read all three complete arguments and their surrounding claims.'))
assert len(changed)==3
needle=r' Q&=D_0\overline T^{-1}p\overline U,&'
p=candidate.index(needle);a=candidate.rfind(r'\begin{split}',0,p);b=candidate.index(r'\end{split}',p)+len(r'\end{split}')
old=candidate[a:b];new=old.replace(r'\begin{split}',r'\begin{aligned}',1).replace(r'\end{split}',r'\end{aligned}',1)
assert old.count('&')==7
fragments=[p for p in u.WORK.rglob('*.tex') if p.name!='front_matter.tex' and old in p.read_text(encoding='utf-8')]
assert len(fragments)==1
fragment=fragments[0];fragment_old=fragment.read_text(encoding='utf-8');assert fragment_old.count(old)==1
fragment_new=fragment_old.replace(old,new,1);candidate=candidate.replace(old,new,1)
changed.append((old,new,'D23','maps:src:D.2.43','Actual pass02 stops at end-split with Extra alignment tab. Its first two rows each have two aligned equality pairs; aligned admits those pairs. Every Q,sigma,A1,A2,H expression and all seven ampersands remain literal; only the environment names change. Root read the complete displayed chain maps, surrounding matrices and inverse homotopy identities.'))
u.check_permanent_identifiers(source,candidate,set(),set())
for i,(old,new,kind,sid,reason) in enumerate(changed,1):
    ident=f'III-C8-TEX-KEYS-SPLIT-{i:02d}';assert not any(x['change_id']==ident for x in ds)
    ds.append(dict(change_id=ident,type=kind,statement_id=sid,old_location='actual pass01/02 source context, guarded exact text',old_page='incomplete pass01/02; no final PDF',new_location='same reference or chain-map display',new_page='pending successful full PDF',old_text=old,new_text=new,reason=reason,review_status='exact bounded root reading and repair '+now+'; actual successor build/pages pending; no mathematical scope or check increment'))
for uid,kind in [('series:III:main-theorems','D04'),('the-proofs-in-outline','D04')]:
    rows=[x for x in ps if x['paper']=='III' and x['unit_id']==uid and x['defect_type']==kind];assert len(rows)==1
    rows[0].update(status='open',date_utc=now,evidence='code/S6_SERIES_PUBLISH_c8_III_reference_and_split_layout_fix.py',detail='Actual leading-space key warning repaired with exact existing labels; convergence of current PDF references remains to be observed.')
rows=[x for x in ps if x['paper']=='III' and x['unit_title']=='Triangular caps and their integral homology' and x['defect_type']=='D23'];assert len(rows)==1
rows[0].update(status='open',date_utc=now,evidence='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass02.out; code/S6_SERIES_PUBLISH_c8_III_reference_and_split_layout_fix.py',detail='Actual extra-alignment-tab error repaired using aligned for the two equality pairs per row; successor compilation and visual page remain.')
eid='publish:c8:III:tex-keys-and-split';assert not any(x['event_id']==eid for x in es)
event={k:'' for k in ef};event.update(statement_id='III:layout-keys-and-split',date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome='All three exact spaced-key contexts and the complete failed split display with surrounding integral chain-map identities read. Actual pass02 exit1/fatal tail/empty stderr and preserved log recorded; full log reading belongs to runtime reviewer. Exact syntactic repairs keep all mathematical keys and expressions. No independent/required proof or page credit.',event_id=eid,phase='continuation8 actual TeX repairs',source_file='code/S6_SERIES_PUBLISH_c8_III_reference_and_split_layout_fix.py',source_event_type='used and rechecked in this run',evidence_group=eid,date_utc=now,where='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass02.out');es.append(event)
front.write_text(front_new,encoding='utf-8',newline='\n');fragment.write_text(fragment_new,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now,'EXACT_EDITS',len(changed),'REOPENED_SOURCE_ROWS',3,'FRAGMENT',fragment)
for old,new,kind,sid,reason in changed:print('ACTUAL_REPAIR',kind,sid,'\n'+new)
