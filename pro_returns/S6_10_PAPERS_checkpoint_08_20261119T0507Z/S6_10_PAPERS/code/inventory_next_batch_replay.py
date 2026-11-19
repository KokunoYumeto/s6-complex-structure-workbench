from pathlib import Path
import datetime,hashlib,json,subprocess,sys,shutil,tempfile,concurrent.futures
R=Path('/workspace/scratch/490d8ca4e928');W=R/'work/S6_10_PAPERS';S=R/'sources/newer_night/checkpoint29';O=W/'analysis/IV_next_batch/replays';O.mkdir(parents=True,exist_ok=True)
T=Path(tempfile.mkdtemp(prefix='s6_next_batch_20261118_'));P=T/'code/part3';P.mkdir(parents=True);(T/'notes').mkdir()
names=[('P3K.84','os49_reduced_ii_caps'),('P3K.85','os49_reduced_ii_return'),('P3K.85','os49_page_sign_audit'),('P3K.87','os49_reduced_ii_all_fans'),('P3K.91','os49_reduced_ii_endpoints')]
for _,n in names:shutil.copy2(S/'code/part3'/f'{n}.py',P/f'{n}.py')
for p in (S/'notes').glob('part3_os49_reduced_ii*_working.md'):shutil.copy2(p,T/'notes'/p.name)
Q=T/'code/part3_root';Q.mkdir()
for n in ['source_all_fans','scalar_all_fans','os49_all_fans']:shutil.copy2(S/'code/part3_root'/f'{n}.py',Q/f'{n}.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in {'utc','generated_at','recorded_at','timestamp'}}
 if isinstance(x,list):return [clean(v) for v in x]
 return x
def diff(a,b,p='$'):
 if type(a)!=type(b):return [{'path':p,'old':a,'new':b}]
 if isinstance(a,dict):return [d for k in sorted(set(a)|set(b)) for d in ([{'path':p+'.'+k,'old':a.get(k),'new':b.get(k)}] if k not in a or k not in b else diff(a[k],b[k],p+'.'+k))]
 if isinstance(a,list):
  if len(a)!=len(b):return [{'path':p,'old_length':len(a),'new_length':len(b)}]
  return [d for i,(u,v) in enumerate(zip(a,b)) for d in diff(u,v,p+f'[{i}]')]
 return [] if a==b else [{'path':p,'old':a,'new':b}]
def run(pair):
 sid,n=pair;start=datetime.datetime.now(datetime.timezone.utc).isoformat();c=subprocess.run([sys.executable,str(P/f'{n}.py')],cwd=T,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=240)
 (O/(n+'.log')).write_text(c.stdout);p=P/(n+'.json');outs=[]
 if p.exists():
  old=S/'code/part3'/p.name;shutil.copy2(p,O/p.name);dd=diff(clean(json.loads(old.read_text())),clean(json.loads(p.read_text()))) if old.exists() else []
  outs=[{'file':str((O/p.name).relative_to(W)),'sha256':sha(p),'historical_file':str(old.relative_to(R)),'historical_sha256':sha(old) if old.exists() else None,'differences':dd}]
 assert sha(P/(n+'.py'))==sha(S/'code/part3'/(n+'.py'))
 return {'label':'night:'+sid,'program':str((S/'code/part3'/(n+'.py')).relative_to(R)),'program_sha256':sha(P/(n+'.py')),'started_at':start,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':c.returncode,'status':'passed' if c.returncode==0 else 'failed','stdout':str((O/(n+'.log')).relative_to(W)),'outputs':outs}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(run,names[:4]))
assert results[-1]['status']=='passed',results[-1]
results.append(run(names[4]))
report={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_checkpoint':29,'isolated_directory':str(T),'programs':results,'all_passed':all(x['status']=='passed' for x in results),'supporting_programs':[{'program':str((S/'code/part3_root'/p.name).relative_to(R)),'sha256':sha(p)} for p in Q.glob('*.py')],'all_non_timestamp_output_fields_identical':all(not y['differences'] for x in results for y in x['outputs'])}
(O/'replay_manifest.json').write_text(json.dumps(report,indent=2)+'\n')
for x in results:print(x['label'],x['status'],(W/x['stdout']).read_text().splitlines()[0])
print('outputs identical',report['all_non_timestamp_output_fields_identical'])
