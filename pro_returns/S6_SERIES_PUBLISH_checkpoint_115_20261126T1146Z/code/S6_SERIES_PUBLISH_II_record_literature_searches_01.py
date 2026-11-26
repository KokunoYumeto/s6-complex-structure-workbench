from pathlib import Path
import csv,datetime as dt,hashlib,io,json
R=Path(__file__).resolve().parents[1]
source=R/'records/S6_SERIES_PUBLISH_II_provenance_primary_reading_01.json'
record=json.loads(source.read_text())
ref=dict(path=str(source.relative_to(R)),sha256=hashlib.sha256(source.read_bytes()).hexdigest())
mapping={'series:II:A':[(0,0),(1,1)],'series:II:C':[(0,1),(1,0)],'series:II:F':[(0,2),(1,3)],'series:II:G':[(0,3),(1,2)]}
p=R/'S6_SERIES_PUBLISH_inventory.csv';before=p.read_bytes();reader=csv.DictReader(io.StringIO(before.decode(),newline=''));fields=reader.fieldnames;rows=list(reader)
changes=[]
for label,pairs in mapping.items():
 matches=[r for r in rows if r['paper']=='II' and r['label']==label];assert len(matches)==1
 row=matches[0];old=row['literature_searches'];assert not old
 additions=[]
 for group,index in pairs:
  q=record['queries'][group]
  additions.append(dict(date_utc=record['created_utc'],engine=q['engine'],query=q['queries'][index],evidence=ref,scope='Bounded online discovery search; exact retrieved-primary openings and receiving-text comparison are recorded in the evidence. No novelty, absence or final provenance closure is inferred from search snippets.'))
 row['literature_searches']=json.dumps(additions,ensure_ascii=False)
 changes.append(dict(paper='II',label=label,tag=row['tag'],field='literature_searches',old=old,new=row['literature_searches']))
out=io.StringIO(newline='');writer=csv.DictWriter(out,fieldnames=fields,lineterminator='\n');writer.writeheader();writer.writerows(rows);after=out.getvalue().encode()
oldrows=list(csv.DictReader(io.StringIO(before.decode(),newline='')))
for old,new in zip(oldrows,rows):
 if old['paper']!='II' or old['label'] not in mapping:assert old==new
 else:assert {k:v for k,v in old.items() if k!='literature_searches'}=={k:v for k,v in new.items() if k!='literature_searches'}
receipt=R/'records/S6_SERIES_PUBLISH_II_literature_search_inventory_append_01.json';assert not receipt.exists()
p.write_bytes(after)
receipt.write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),evidence=ref,before_sha256=hashlib.sha256(before).hexdigest(),after_sha256=hashlib.sha256(after).hexdigest(),changes=changes,other_rows_unchanged=True,events_added=0,provenance_claims_closed=0),indent=2)+'\n')
print(json.dumps(dict(receipt=str(receipt.relative_to(R)),rows_updated=len(changes),searches_recorded=8,events_added=0)))
