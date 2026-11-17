from pathlib import Path
import concurrent.futures, hashlib, json, subprocess, urllib.request
ROOT=Path(__file__).resolve().parents[3]
DEST=ROOT/'sources/audit_cache/inv_ari/working_literature'
DEST.mkdir(parents=True,exist_ok=True)
urls={
 'Schweitzer2007':'https://arxiv.org/pdf/0709.3528',
 'Serre1955Duality':'https://www.college-de-france.fr/media/jean-pierre-serre/UPL35645220559164287_Un_theoreme_de_dualite.pdf',
 'AtiyahSinger1963':'https://www.ams.org/bull/1963-69-03/S0002-9904-1963-10957-X/S0002-9904-1963-10957-X.pdf',
 'Grothendieck1957':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf',
 'Deligne1970':'https://publications.ias.edu/sites/default/files/Number9.pdf',
 'Frolicher1955':'https://pmc.ncbi.nlm.nih.gov/articles/PMC528153/pdf/pnas00697-0029.pdf',
 'AngellaTomassini2013':'https://arxiv.org/pdf/1402.1954',
}
def get(item):
 k,u=item;r={'citation_key':k,'url':u}
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
  raw=urllib.request.urlopen(req,timeout=40).read()
  ext='.pdf' if raw.startswith(b'%PDF') else '.html';p=DEST/(k+ext);p.write_bytes(raw)
  r.update(source_file=str(p.relative_to(ROOT)),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),kind=ext)
  if ext=='.pdf':subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True,capture_output=True)
 except Exception as e:r['error']=str(e)
 return r
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for r in pool.map(get,urls.items()):
  rows.append(r);(DEST/'fetch_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
  print(r['citation_key'],r.get('kind'),r.get('error',''),flush=True)
