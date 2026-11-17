from pathlib import Path
import re,json,urllib.request,hashlib,subprocess,concurrent.futures,time
ROOT=Path(__file__).resolve().parents[3];DEST=ROOT/'sources/audit_cache/inv_ari/literature';DEST.mkdir(parents=True,exist_ok=True)
keys=['CrGrossZagier1986','CrGross1991','CrJetchev2008','CrRubin1999','CrBDP2012','CrCastella2025','CrCremonaSiksek2006','CrDarmon2009','CgzCai2014','CgzBelabas2019','CgzYZZ2011','CgzStein2007','miller2011','agboola2006','waldschmidt1979sigma','waldschmidt1975dimension','waldschmidt2009auxiliary','callSilverman1993','silverman2006heights','bertrand2017','bertrand1995','bost2009','nguyen2023','noguchi2024','xie2024algebraicity','gramain1986values','gasbarri2010analytic','herblot2012meromorphic','waldschmidt1988theta','reyssat1982weierstrass','adamczewski2017mahler','einsiedler2001entropy','waldschmidt1988periodrank','roy1993periodrank']
entries={}
for p in (ROOT/'sources/returns/S6_05_ARITHMETIC').glob('*.bib'):
 t=p.read_text()
 for m in re.finditer(r'@\w+\{([^,]+),',t):
  i=m.end();depth=1
  while i<len(t) and depth:
   if t[i]=='{':depth+=1
   elif t[i]=='}':depth-=1
   i+=1
  entries[m[1]]=t[m.start():i]
urls=[]
for key in keys:
 text=entries.get(key,'');m=re.search(r'url\s*=\s*\{([^}]+)\}',text)
 if m:urls.append((key,m[1]))
urls.append(('Schnell19','https://www.math.stonybrook.edu/~cschnell/mat615/lectures/lecture4.pdf'))
def fetch(item):
 key,url=item;start=time.time();row={'key':key,'url':url}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  raw=urllib.request.urlopen(req,timeout=35).read();ext='.pdf' if raw.startswith(b'%PDF') else ('.ps' if raw.startswith(b'%!PS') else '.html');p=DEST/(key+ext);p.write_bytes(raw);row.update(file=str(p.relative_to(ROOT)),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),kind=ext)
  if ext=='.ps':
   q=p.with_suffix('.pdf');subprocess.run(['ps2pdf',str(p),str(q)],check=True,capture_output=True);p=q
  if p.suffix=='.pdf':subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True,capture_output=True)
 except Exception as e:row['error']=str(e)
 row['seconds']=time.time()-start;return row
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 for row in pool.map(fetch,urls):
  rows.append(row);(DEST/'fetch_manifest.json').write_text(json.dumps(rows,indent=2));print(row['key'],row.get('kind'),row.get('error',''),flush=True)
