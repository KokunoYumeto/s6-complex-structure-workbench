from pathlib import Path
import json,hashlib,datetime,urllib.request,concurrent.futures
p=Path(__file__).parent;tree=json.loads((p/'S6_SERIES_PUBLISH_I_pinned_program_tree.json').read_text());rec=json.loads((p/'S6_SERIES_PUBLISH_I_program_primary_receipt.json').read_text());by={x['path']:x for x in tree['tree']};pin=rec['commit'];choices=[]
for f in rec['files']:
 stem=f['repository_path'][:-3]
 for ext in ['.json','.out']:
  if stem+ext in by:choices.append(by[stem+ext]);break
dest=p.parent/'programs';dest.mkdir(exist_ok=True)
def fetch(x):
 u='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'+pin+'/'+x['path']
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'S6-publication-source-check'}),timeout=35) as f:data=f.read();status=f.status
  blob=hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest();assert blob==x['sha']
  q=dest/('S6_SERIES_PUBLISH_I_saved_'+Path(x['path']).name);q.write_bytes(data)
  return {'repository_path':x['path'],'url':u,'http_status':status,'git_blob_sha1':blob,'sha256':hashlib.sha256(data).hexdigest(),'local_file':str(q),'bytes':len(data),'scope':'Retained pinned output, not a current execution.'}
 except Exception as e:return {'repository_path':x['path'],'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:rows=list(pool.map(fetch,choices))
(p/'S6_SERIES_PUBLISH_I_program_output_receipt.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':pin,'files':rows},indent=2)+'\n')
print(json.dumps({'files':len(rows),'success':sum('error'not in r for r in rows),'errors':[r for r in rows if'error'in r]},indent=2))
