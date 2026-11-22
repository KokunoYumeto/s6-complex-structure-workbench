from pathlib import Path
import csv,datetime as dt,difflib,hashlib,io,json,re

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):
 b=(R/p).read_bytes();return dict(path=p,sha256=sha(b),bytes=len(b))
p=R/'S6_SERIES_PUBLISH_II.tex';before=p.read_bytes();s=before.decode()
assert sha(before)=='58ba5d83132bd593a91c06e4c9fa07cadf32aceb24ace297da05430f43a6fdea'
a=s.index('\\begin{thebibliography}');b=s.index('\\end{thebibliography}',a)
parts=re.split(r'(?=\\bibitem)',s[a:b]);prefix=parts[0];entries={};sortkeys={}
def letters(x):
 x=x.replace('\\L','L').replace('\\l','l')
 x=re.sub(r'\\[\'"^`~=.]\s*\{?([A-Za-z])\}?',r'\1',x)
 x=re.sub(r'\\[uvHckbdtr]\s*\{?([A-Za-z])\}?',r'\1',x)
 x=x.replace("'",'').replace('~',' ').replace('{','').replace('}','')
 return re.sub(r'[^a-z0-9]+',' ',x.lower()).strip()
for e in parts[1:]:
 m=re.match(r'\\bibitem\[([\s\S]*?)\]\{([^{}]+)\}',e);assert m
 label,key=m.groups();assert key not in entries;entries[key]=e
 first,rest=label.split('(',1);date,tail=rest.split(')',1);full=tail.strip() or first
 authors=[letters(x) for x in re.split(r',\s*(?:and\s+)?|\s+and\s+',full)]
 assert all(authors)
 year=re.search(r'\d{4}',date);suffix=re.search(r'\\natexlab\{([a-z])\}',date)
 sortkeys[key]=(tuple(authors),int(year.group()) if year else 9999,suffix.group(1) if suffix else '',key)
order=sorted(entries,key=lambda k:sortkeys[k]);assert len(order)==125
assert order.index('AbashevaDeev2024AB')<order.index('AKMW2002')<order.index('ACampo1975')
assert order.index('DlousskyOeljeklaus1999')<order.index('DOT2000')<order.index('DlousskyTeleman2012')
assert order.index('GHK2015')<order.index('GrossSiebert2006I')
assert order.index('KhaledTeleman2026')<order.index('KhaledTeleman2026Journal')
newbib=prefix+''.join(entries[k] for k in order);after=(s[:a]+newbib+s[b:]).encode()
assert prefix+''.join(entries.values())==s[a:b]
assert set(order)==set(entries)
out=R/'records/S6_SERIES_PUBLISH_II_bibliography_order_03';assert not out.exists()
dp=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=dp.read_bytes();rd=csv.DictReader(io.StringIO(db.decode(),newline=''),delimiter='\t');prior=list(rd);fields=rd.fieldnames
oldpos={k:i+1 for i,k in enumerate(entries)};rows=[]
for i,k in enumerate(order,1):
 if i==oldpos[k]:continue
 r={f:'' for f in fields};r.update(change_id='II-BIB03-'+k,type='D18',statement_id='Bibliography:'+k,
  old_location='Bibliography position'+str(oldpos[k]),new_location='Bibliography position'+str(i),old_page='pending integrated locator',new_page='pending integrated PDF',
  old_text=entries[k],new_text=entries[k],reason='Correct the author-key tokenization: compare ordered surnames with conjunctions separated; ignore apostrophe punctuation in the sorting key; then compare publication year and existing citation suffix. The complete entry is byte-identical.',
  review_status='Root reviewed exact author arrays and inverse entry permutation; no citation key, edition, label, or body text changes.')
 rows.append(r)
assert len({r['change_id'] for r in prior+rows})==len(prior)+len(rows)
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);append=buf.getvalue().encode()
out.mkdir();mapping=dict(old_order=list(entries),new_order=order,author_year_keys=sortkeys,entry_sha256={k:sha(e.encode()) for k,e in entries.items()})
(out/'permutation.json').write_text(json.dumps(mapping,indent=2)+'\n')
(out/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),after.decode().splitlines(True),fromfile='II.before',tofile='II.after')))
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);(out/'defect_rows.tsv').write_text(buf.getvalue())
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),source_before_sha256=sha(before),source_after_sha256=sha(after),entry_count=125,all_entry_bytes_unchanged=True,
 old_order_reconstruction_exact=True,permutation=bind(str((out/'permutation.json').relative_to(R))),defect_rows=len(rows),defect_before_sha256=sha(db),defect_after_sha256=sha(db+append),
 previous_pass_preserved='records/S6_SERIES_PUBLISH_II_bibliography_style_02/manifest.json',correction='The preceding flat author string included conjunctions and split A Campo at its apostrophe. The printed bibliography order now uses ordered author-name arrays, year and the existing year suffix; all complete entry bytes are preserved.',events_added=0,required_rows_completed=0,global_D18_closed=False)
(out/'manifest.json').write_text(json.dumps(record,indent=2)+'\n');p.write_bytes(after)
with dp.open('ab') as f:f.write(append)
assert dp.read_bytes()==db+append
print(json.dumps(dict(manifest=bind(str((out/'manifest.json').relative_to(R))),source_sha256=sha(after),changed_positions=len(rows),order=order)))
