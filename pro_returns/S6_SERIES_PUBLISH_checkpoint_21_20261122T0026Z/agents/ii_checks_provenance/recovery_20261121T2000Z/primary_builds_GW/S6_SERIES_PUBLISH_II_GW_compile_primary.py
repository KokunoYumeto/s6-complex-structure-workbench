from pathlib import Path
import os,subprocess,json,hashlib,datetime,concurrent.futures,re
root=Path.cwd();d=root/'agents/ii_checks_provenance/recovery_20261121T2000Z/primary_builds_GW'
j=json.loads((d/'S6_SERIES_PUBLISH_II_GW_primary_build_inputs.json').read_text())
env=os.environ.copy();runtime=root/'tex-runtime';env['TEXMFCNF']=str(runtime/'web2c')+':/usr/share/texlive/texmf-dist/web2c';env['TEXMFCACHE']=str(d/'lua-cache')
def run(a):
 sub=root/a['directory'];passes=[]
 for n in range(1,4):
  log=sub/f'build_pass{n}.out'
  with log.open('w') as f:z=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-no-shell-escape',a['source_name']],cwd=sub,env=env,stdout=f,stderr=subprocess.STDOUT)
  passes.append({'pass':n,'exit_code':z.returncode,'output':str(log.relative_to(root)),'sha256':hashlib.sha256(log.read_bytes()).hexdigest()})
  if z.returncode:break
 stem=Path(a['source_name']).stem;files={}
 for ext in ['tex','aux','log','pdf']:
  p=sub/(stem+'.'+ext)
  if p.exists():files[ext]={'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 text=(sub/(stem+'.aux')).read_text() if (sub/(stem+'.aux')).exists() else ''
 labels={k:[s for s in text.splitlines() if s.startswith('\\newlabel{'+k+'}') ] for k in a['requested_labels']}
 return dict(key=a['key'],passes=passes,files=files,labels=labels,source_hash_preserved=files.get('tex',{}).get('sha256')==a['source_sha256'])
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows=list(ex.map(run,j['sources']))
p=d/'S6_SERIES_PUBLISH_II_GW_primary_build_receipt.json';p.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':rows,'source_mutations':0,'canonical_mutations':0,'scope':'Private compilation of byte-identical attached primary source files; aux locators are for these precise source editions.'},indent=2)+'\n')
print(json.dumps(rows,indent=2))
