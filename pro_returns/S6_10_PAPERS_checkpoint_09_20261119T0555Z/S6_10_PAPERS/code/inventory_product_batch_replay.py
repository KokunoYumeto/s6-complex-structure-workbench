#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,shutil,tempfile,concurrent.futures
R=Path('/workspace/scratch/490d8ca4e928');W=R/'work/S6_10_PAPERS';S=R/'sources/newer_night/checkpoint29'
O=W/'analysis/IV_product_batch/replays';O.mkdir(parents=True,exist_ok=True)
T=Path(tempfile.mkdtemp(prefix='s6_product_batch_20261118_'))
P=T/'code/part3';P.mkdir(parents=True)
names=[('P3K.38','scalar_cap_minimality'),('P3K.42','source_cusp_characteristic_pair'),('P3K.47','source_cusp_product_obstruction'),('P3K.48','source_cusp_ordinary_product'),('P3K.49','source_zero_relative_comparison'),('P3K.51','source_cusp_circle_trace'),('P3K.53','source_unselected_collision')]
for _,n in names:shutil.copy2(S/'code/part3'/f'{n}.py',P/f'{n}.py')
shutil.copy2(S/'code/part3/canonical_scalar_catalogue.json',P/'canonical_scalar_catalogue.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in {'utc','generated_at','recorded_at','timestamp'}}
 if isinstance(x,list):return [clean(v) for v in x]
 return x
def differences(a,b,p='$'):
 if type(a)!=type(b):return [{'path':p,'old':a,'new':b}]
 if isinstance(a,dict):
  out=[]
  for k in sorted(set(a)|set(b)):
   if k not in a or k not in b:out.append({'path':p+'.'+k,'old':a.get(k),'new':b.get(k)})
   else:out.extend(differences(a[k],b[k],p+'.'+k))
  return out
 if isinstance(a,list):
  if len(a)!=len(b):return [{'path':p,'old_length':len(a),'new_length':len(b)}]
  return [x for i,(u,v) in enumerate(zip(a,b)) for x in differences(u,v,p+f'[{i}]')]
 return [] if a==b else [{'path':p,'old':a,'new':b}]
def run(pair):
 sid,n=pair;start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 completed=subprocess.run([sys.executable,str(P/f'{n}.py')],cwd=T,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=180)
 log=O/f'{n}.log';log.write_text(completed.stdout)
 original=S/'code/part3'/f'{n}.py';current=P/f'{n}.py'
 assert sha(original)==sha(current),'script mutated'
 outputs=[]
 for q in sorted(P.glob(n+'.*')):
  if q.suffix=='.py':continue
  target=O/q.name;shutil.copy2(q,target);old=S/'code/part3'/q.name
  comparison='no historical output';diff=[]
  if old.exists():
   if q.suffix=='.json':
    a=json.loads(old.read_text());b=json.loads(q.read_text());diff=differences(clean(a),clean(b));comparison='all non-timestamp fields identical' if not diff else 'differences retained for explicit audit'
   else:comparison='byte-identical' if old.read_bytes()==q.read_bytes() else 'text differs; explicit audit pending'
  outputs.append({'file':str(target.relative_to(W)),'sha256':sha(q),'historical_file':str(old.relative_to(R)) if old.exists() else None,'historical_sha256':sha(old) if old.exists() else None,'comparison':comparison,'differences':diff})
 if n=='scalar_cap_minimality':
  q=P/'scalar_cap_minimality_table.md';target=O/q.name;shutil.copy2(q,target);old=S/'code/part3'/q.name
  outputs.append({'file':str(target.relative_to(W)),'sha256':sha(q),'historical_file':str(old.relative_to(R)),'historical_sha256':sha(old),'comparison':'byte-identical' if old.read_bytes()==q.read_bytes() else 'text differs; explicit audit pending','differences':[]})
 return {'label':'night:'+sid,'program':str(original.relative_to(R)),'program_sha256':sha(original),'started_at':start,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':completed.returncode,'status':'passed' if completed.returncode==0 else 'failed','stdout':str(log.relative_to(W)),'outputs':outputs,'scope':'Unchanged exact source program replay. Its algebra and finite samples retain the original scope; this execution creates no extra mathematical proof review.'}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 results=list(ex.map(run,names))
report={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_checkpoint':29,'isolated_directory':str(T),'programs':results,'all_passed':all(x['status']=='passed' for x in results),'all_outputs_compared':all(not o['differences'] and o['comparison'] in {'all non-timestamp fields identical','byte-identical'} for x in results for o in x['outputs'])}
(O/'replay_manifest.json').write_text(json.dumps(report,indent=2)+'\n')
for x in results:print(x['label'],x['status'],(W/x['stdout']).read_text().splitlines()[0])
print('OUTPUTS',sum(len(x['outputs']) for x in results),'all_passed',report['all_passed'],'all_outputs_compared',report['all_outputs_compared'])
