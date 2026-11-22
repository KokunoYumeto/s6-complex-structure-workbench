from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime as dt, gzip, hashlib, io, json, tarfile
import urllib.request, urllib.parse

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
versions=[
 ('Albanese2020','2005.09494v2','../S6_PUBLISH_literature_arxiv/2005.09494/2005.09494.tex','turn668443341view0'),
 ('Catanese2002','math/0111245v2','../S6_PUBLISH_literature_arxiv/math_0111245/math_0111245.tex','turn668443341view1'),
 ('LRS2019','1912.09719v1','../S6_GRIND_6_literature/papers/arXiv_1912.09719_Lehn_Rollenske_Schinko_src/main.tex','turn668443341view2'),
 ('Steenbrink1999','math/9902134v1','../S6_PUBLISH_literature_arxiv/math_9902134/math_9902134.tex','turn668443341view3'),
 ('SchuttShioda2010','0907.0298v3','../S6_PUBLISH_literature_arxiv/0907.0298/0907.0298.tex','turn668443341view4')]
queries=[
 ('Albanese2020','The Yamabe invariants of Inoue surfaces Kodaira surfaces and their blowups'),
 ('Catanese2002','Deformation types of real and complex manifolds'),
 ('SchuttShioda2010','Elliptic surfaces Schutt Shioda 2010'),
 ('Greb2011','Rational singularities and quotients by holomorphic group actions'),
 ('Steenbrink1999','Cup products and mixed Hodge structures')]

def get(url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'S6-bibliography-verification/1.0'}),timeout=35) as r:
  return r.read(),r.headers.get('Content-Type'),r.url

def arxiv(row):
 key,version,local,ref=row;url='https://arxiv.org/src/'+version
 lb=(R/local).read_bytes()
 out=dict(key=key,version=version,url=url,metadata_web_ref=ref,
     local=dict(path=local,bytes=len(lb),sha256=sha(lb)),scope='Source identity and version metadata only; no new mathematical reading.')
 try:
  raw,content_type,final_url=get(url)
  out['response']=dict(bytes=len(raw),sha256=sha(raw),content_type=content_type,final_url=final_url)
  try:
   with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tf:
    members=[]
    for member in tf.getmembers():
     if member.isfile() and member.name.endswith('.tex'):
      b=tf.extractfile(member).read()
      members.append(dict(name=member.name,bytes=len(b),sha256=sha(b),exact_local_match=b==lb))
    out['tex_members']=members
    out['exact_local_match']=any(x['exact_local_match'] for x in members)
  except tarfile.ReadError:
   try:b=gzip.decompress(raw)
   except (OSError,EOFError):b=raw
   out['source']=dict(bytes=len(b),sha256=sha(b))
   out['exact_local_match']=b==lb
 except Exception as e:out['error']=repr(e)
 return out

def crossref(row):
 key,title=row
 url='https://api.crossref.org/works'
 out=dict(key=key,query=title,scope='Official registry bibliographic metadata only; no article-reading credit.')
 try:
  raw,content_type,final_url=get(url+'?'+urllib.parse.urlencode({'query.title':title,'rows':3}))
  out.update(url=final_url,response_sha256=sha(raw),response_bytes=len(raw))
  fields=['DOI','title','author','container-title','publisher','volume','issue','page','published','published-print','published-online','type','URL']
  out['items']=[{k:x[k] for k in fields if k in x} for x in json.loads(raw)['message']['items']]
 except Exception as e:out['error']=repr(e)
 return out

with ThreadPoolExecutor(max_workers=5) as ex:version_rows=list(ex.map(arxiv,versions))
with ThreadPoolExecutor(max_workers=5) as ex:crossref_rows=list(ex.map(crossref,queries))
out=R/'records/S6_SERIES_PUBLISH_II_bibliography_primary_03.json'
assert not out.exists()
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),arxiv=version_rows,crossref=crossref_rows,
 source_changes=0,events_added=0,required_checks_completed=0,
 execution_history='Initial launch stopped before any acquisition because requests is absent from system Python. Replaced that dependency with the standard-library urllib client and retained this failure description; no source or reading credit was assigned to the failed launch.',
 acquisition='Responses inspected in memory and discarded after hashes/metadata/source comparisons. No downloaded published work enters deliverables.')
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(path=str(out.relative_to(R)),sha256=sha(out.read_bytes()),bytes=out.stat().st_size,
 arxiv=[{k:v for k,v in r.items() if k in ['key','version','exact_local_match','error']} for r in version_rows],
 crossref=[dict(key=r['key'],error=r.get('error'),items=r.get('items')) for r in crossref_rows]),indent=2))
