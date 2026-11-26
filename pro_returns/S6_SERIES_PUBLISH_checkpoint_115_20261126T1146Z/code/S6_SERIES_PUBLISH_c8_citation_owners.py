"""Consolidate proved same-edition citation keys and one external-reference route."""
from datetime import datetime, timezone
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

mapping={'mapsAC26':'AC26','manEngel26':'E26','mapsEngel':'E26','mapsHatcher02':'Hatcher2002','manSchuettShioda10':'manSS10'}
edition={
 'mapsAC26':'Same108-page author alpo.ge/s6.pdf; unchanged Lemma6.5(ii) pp38-39 and Lemma7.4 proof p42.',
 'manEngel26':'Same arXiv:2609.38442v1,25-page edition; every existing statement/page locator is unchanged.',
 'mapsEngel':'Same arXiv:2609.38442v1,25-page edition; every existing statement/page locator is unchanged.',
 'mapsHatcher02':'Same Hatcher Algebraic Topology2002 author PDF and printed pagination; theorem/corollary locators unchanged.',
 'manSchuettShioda10':'Same arXiv:0907.0298v3,9 July2010 preprint pagination; LN staged source record fixes manSS10 to precisely this version.'}
pattern=re.compile(r'(\\cite(?:p|t|alp|author|year)?\*?(?:\[[^\]]*\])?\{)([^}]+)(\})')
source=u.repairs.SOURCE.read_text();candidate=source
df,ds=r.table(r.DEFECTS);changes=[];updates=[];counts={k:0 for k in mapping}
for p in sorted(u.WORK.rglob('*.tex')):
 if p.name in {'preamble.tex','bibliography.tex'}:continue
 old=p.read_text();local=[]
 def replace(m):
  keys=m.group(2).split(',');newkeys=[mapping.get(k.strip(),k.strip()) for k in keys]
  changed=[k.strip() for k in keys if k.strip() in mapping]
  if not changed:return m.group(0)
  new=m.group(1)+','.join(newkeys)+m.group(3)
  local.append((old[:m.start()].count('\n')+1,m.group(0),new,changed))
  for k in changed:counts[k]+=1
  return new
 new=pattern.sub(replace,old)
 if p.name=='os49_graph_caps.tex':
  route='\\cref{night:P3K.65}'
  assert new.count(route)==1
  line=new[:new.index(route)].count('\n')+1
  local.append((line,route,'\\SeriesRef{night:P3K.65}',[]))
  new=new.replace(route,'\\SeriesRef{night:P3K.65}',1)
 if new!=old:
  u.check_permanent_identifiers(old,new,set(),set())
  assert candidate.count(old)==1,p
  candidate=candidate.replace(old,new,1);updates.append((p,new))
  for line,before,after,ks in local:changes.append((p,line,before,after,ks))
assert counts=={'mapsAC26':2,'manEngel26':14,'mapsEngel':2,'mapsHatcher02':2,'manSchuettShioda10':6},counts
assert len(changes)==27
u.check_permanent_identifiers(source,candidate,set(),set())
for i,(p,line,before,after,ks) in enumerate(changes,1):
 types=['D06'] if ks else ['D04','D10']
 for kind in types:
  ident=f'III-C8-CITATION-OWNERS-{i:03d}-{kind}'
  assert not any(x['change_id']==ident for x in ds)
  reason=('Exact citation-key substitution to the same opened edition. '+ ' '.join(edition[k] for k in ks)+' The identity map on the cited source and the unchanged locator identifies each application; the old alias-to-owner correspondence is retained in this row.' if ks else 'The target night:P3K.65 belongs to Paper IV/tag02VC and already has the SRef mapping. Use that exact external route, as the other three uses in the same fragment do. The mathematical statement is unchanged.')
  ds.append(dict(change_id=ident,type=kind,statement_id='night:P3K.65' if not ks else '; '.join(ks),old_location=str(p.relative_to(u.ROOT))+':'+str(line),old_page='pending page concordance',new_location=str(p.relative_to(u.ROOT))+':'+str(line),new_page='pending final PDF',old_text=before,new_text=after,reason=reason,review_status='every bounded citation context and exact source-edition correspondence read; actual final changed tokens/streams pending readback; no criterion credit'))
for p,new in updates:p.write_text(new,encoding='utf-8',newline='\n')
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds)
print('UTC',datetime.now(timezone.utc).isoformat())
for p,line,before,after,ks in changes:
 print('EXACT_CHANGE',p.relative_to(u.ROOT),line)
 print('OLD',before);print('NEW',after)
print('CITATION_COUNTS',counts,'UPDATED_FRAGMENTS',len(updates),'EXACT_DEFECT_ROWS',sum(1 if x[4] else 2 for x in changes))
print('ALL_OLD_IDENTITIES_PRESERVED; MATHEMATICAL_TEXT_AND_LOCATORS_UNCHANGED; NO_CRITERION_INCREMENT')
