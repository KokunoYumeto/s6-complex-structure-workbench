from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'sources/external/maps_audit'
OUT=ROOT/'deliverables/work/maps_audit'
spec=[('seidel2003v2','math/0105186v2'),('baez2002v4','math/0105155v4'),('hill_taylor2010v2','0710.2310v2'),('michel_weber2014v1','1409.0704v1'),('snaith2010v1','1001.4751v1'),('benedetti2019v1','1907.10297v1'),('durst_geiges_kegel2018v1','1811.09055v1'),('laudenbach2013v1','1307.2545v1'),('strickland2024v1','2412.09361v1')]
records=[]
for stem,ident in spec:
 for suffix,route in [('.pdf','pdf'),('.tar','src')]:
  p=SRC/(stem+suffix)
  if p.exists(): records.append(dict(filename=str(p.relative_to(ROOT)),url=f'https://arxiv.org/{route}/{ident}',sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,date='2026-11-17',retrieval='Original arXiv version retrieved by HTTPS; retrieval does not imply proof reading',read_locators='See separate scoped course source-check events'))
 folder=SRC/(stem+'_source')
 if folder.exists():
  for p in sorted(folder.rglob('*')):
   if p.is_file() and p.suffix.lower()=='.tex':records.append(dict(filename=str(p.relative_to(ROOT)),url=f'https://arxiv.org/src/{ident}',sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,date='2026-11-17',retrieval='Exact TeX extracted from retained original arXiv source archive; some archives are single gzip TeX streams',read_locators='See separate scoped course source-check events'))
p=SRC/'milnor_stasheff1974.pdf'
if p.exists():records.append(dict(filename=str(p.relative_to(ROOT)),url='https://www.maths.ed.ac.uk/~v1ranick/papers/milnstas.pdf',sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,date='2026-11-17',retrieval='University-hosted reproduction of the 1974 original; not the re-typeset transcription',read_locators='Not yet read at retrieval-record time'))
(OUT/'course_external_retrieval.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
path=OUT/'external_provenance.json';old=json.loads(path.read_text());keys={(r.get('filename'),r.get('sha256')) for r in old};old.extend(r for r in records if (r['filename'],r['sha256']) not in keys);path.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'course_source_artifacts':len(records)}))
