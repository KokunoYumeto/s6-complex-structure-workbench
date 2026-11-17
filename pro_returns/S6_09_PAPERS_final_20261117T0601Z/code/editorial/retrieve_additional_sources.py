"""Fetch specifically identified primary literature; never marks a proof verified."""
from pathlib import Path
import sys,json,urllib.request,concurrent.futures,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'deps/python'))
import bibtexparser
entries={x.key:{f.key:f.value for f in x.fields} for x in bibtexparser.parse_string((ROOT/'deliverables/S6_09_PAPERS_references.bib').read_text()).entries}
OUT=ROOT/'sources/external/root/retrieved'
def get(k):
 url=entries[k]['url'];p=OUT/(k+'.pdf')
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read()
  if not data.startswith(b'%PDF'):return {'key':k,'url':url,'status':'non-PDF response'}
  p.write_bytes(data);subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  return {'key':k,'url':url,'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),'status':'retrieved; not verified'}
 except Exception as e:return {'key':k,'url':url,'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(4) as e:r=list(e.map(get,sys.argv[1:]))
p=ROOT/'deliverables/work/root/additional_retrieval.json';old=json.loads(p.read_text()) if p.exists() else [];p.write_text(json.dumps(old+r,indent=2)+'\n');print(json.dumps(r,indent=2))
