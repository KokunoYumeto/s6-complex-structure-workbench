from pathlib import Path
import json,hashlib,datetime,urllib.request,concurrent.futures
p=Path(__file__).parent;tree=json.loads((p/'S6_SERIES_PUBLISH_I_pinned_program_tree.json').read_text());names=json.loads((p/'S6_SERIES_PUBLISH_I_program_file_index.json').read_text());pin='83d76022bcd442278b760db9ff438afceed6c6ea';prefix='pro_returns/S6_02_PUSH_final_20261115T2217Z/S6_02_PUSH/code/'
choices=[]
for name in names:
 xs=[x for x in tree['tree'] if x['path']==prefix+name]
 if not xs and name=='e_degeneration.py':xs=[x for x in tree['tree'] if x['path']=='pro_returns/S6_02_FAMILY/return/code/'+name]
 if xs:choices.append(xs[0])
dest=p.parent/'programs';dest.mkdir(exist_ok=True)
def fetch(x):
 u='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'+pin+'/'+x['path']
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'S6-publication-source-check'}),timeout=35) as f:data=f.read();status=f.status
  blob=hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest();assert blob==x['sha'],(blob,x['sha'])
  q=dest/('S6_SERIES_PUBLISH_I_source_'+Path(x['path']).name);q.write_bytes(data)
  return {'repository_path':x['path'],'url':u,'http_status':status,'git_blob_sha1':blob,'sha256':hashlib.sha256(data).hexdigest(),'local_file':str(q),'bytes':len(data),'source_opened':True,'source_read_scope':'Awaiting manual mathematical inspection; download alone gives no check credit.'}
 except Exception as e:return {'repository_path':x['path'],'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:rows=list(pool.map(fetch,choices))
rec={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':pin,'tree_sha':tree.get('sha'),'recursive_tree_truncated':tree.get('truncated'),'files':rows,'scope':'Current pinned-commit primary program openings; not executions or mathematical check events.'}
(p/'S6_SERIES_PUBLISH_I_program_primary_receipt.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps({'files':len(rows),'success':sum('error'not in r for r in rows),'errors':[r for r in rows if'error'in r]},indent=2))
