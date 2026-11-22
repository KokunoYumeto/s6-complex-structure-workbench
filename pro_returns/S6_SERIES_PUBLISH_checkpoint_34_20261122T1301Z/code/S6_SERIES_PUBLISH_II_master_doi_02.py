from pathlib import Path
import csv,datetime as dt,difflib,hashlib,io,json,re

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):
 b=(R/p).read_bytes();return dict(path=p,sha256=sha(b),bytes=len(b))
p=R/'S6_SERIES_PUBLISH_references.bib';before=p.read_bytes();s=before.decode()
assert sha(before)=='ae2198dfab9d8d5c8967ee4797c6ef2f52a430b78cab64ef23465cfa6b3667f1'
source=bind('S6_SERIES_PUBLISH_II.tex');ledger=bind('CHECK_EVENTS.tsv')
updates=[('AKMW2002','https://arxiv.org/pdf/math/9904135','10.1090/S0894-0347-02-00396-X'),('Fujimoto1988Log','https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf','10.1215/kjm/1250520560')]
changes=[]
for key,url,doi in updates:
 m=re.search(r'@[A-Za-z]+\{'+key+r',',s);assert m
 depth=1;i=m.end()
 while depth:
  if s[i]=='{':depth+=1
  elif s[i]=='}':depth-=1
  i+=1
 old=s[m.start():i];anchor='  url = {'+url+'},'
 assert old.count(anchor)==1 and not re.search(r'\n\s*doi\s*=',old)
 new=old.replace(anchor,'  doi = {'+doi+'},\n  url = {https://doi.org/'+doi+'},',1)
 assert s.count(old)==1;s=s.replace(old,new,1)
 changes.append(dict(key=key,old=old,new=new,doi=doi))
after=s.encode();out=R/'records/S6_SERIES_PUBLISH_II_master_doi_02';assert not out.exists()
dp=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=dp.read_bytes();rd=csv.DictReader(io.StringIO(db.decode(),newline=''),delimiter='\t');prior=list(rd);fields=rd.fieldnames
rows=[]
for c in changes:
 r={k:'' for k in fields};r.update(change_id='II-MASTER-DOI02-'+c['key'],type='D18',statement_id='Bibliography:'+c['key'],
  old_location='Master references entry '+c['key'],new_location='Master references entry '+c['key'],old_page='not applicable',new_page='not applicable',old_text=c['old'],new_text=c['new'],
  reason='Synchronize the existing reference record with the exact publisher-deposited DOI and DOI URL verified through Crossref; retain every historical primary-reading and scope note.',review_status='Both complete old/new reference entries and Crossref metadata read by root.')
 rows.append(r)
assert len({r['change_id'] for r in prior+rows})==len(prior)+len(rows)
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);append=buf.getvalue().encode()
out.mkdir();(out/'changes.json').write_text(json.dumps(changes,indent=2)+'\n')
(out/'references.diff').write_text(''.join(difflib.unified_diff(before.decode().splitlines(True),s.splitlines(True),fromfile='references.before',tofile='references.after')))
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),references_before_sha256=sha(before),references_after_sha256=sha(after),entries_updated=2,
 changes=bind(str((out/'changes.json').relative_to(R))),metadata=bind('records/S6_SERIES_PUBLISH_II_bibliography_crossref_02.json'),
 source_binding=source,ledger_binding=ledger,source_unchanged=True,ledger_unchanged=True,defect_before_sha256=sha(db),defect_after_sha256=sha(db+append),events_added=0,required_rows_completed=0,article_reading_credit=0)
(out/'manifest.json').write_text(json.dumps(record,indent=2)+'\n');p.write_bytes(after)
with dp.open('ab') as f:f.write(append)
assert bind('S6_SERIES_PUBLISH_II.tex')==source and bind('CHECK_EVENTS.tsv')==ledger
print(json.dumps(dict(manifest=bind(str((out/'manifest.json').relative_to(R))),references_sha256=sha(after),rows=2)))
