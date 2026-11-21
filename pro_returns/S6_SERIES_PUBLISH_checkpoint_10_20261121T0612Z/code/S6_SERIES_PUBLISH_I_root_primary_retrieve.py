from pathlib import Path
import concurrent.futures,datetime,hashlib,json,re,urllib.request
root=Path(__file__).resolve().parents[1]/'agents/root_primary'
root.mkdir(parents=True,exist_ok=True)
targets={
 'BS76':('https://djvu.online/file/2hQiOnz8WuoQk','html'),
 'Knudson2004':('https://arxiv.org/pdf/math/0409133','pdf'),
 'Buchdahl1999':('https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf','pdf'),
 'Levy08':('https://www.numdam.org/article/AIF_2008__58_2_571_0.pdf','pdf'),
 'FG10':('https://msp.org/gt/2010/14-1/gt-v14-n1-p02-p.pdf','pdf'),
 'AKMW02AB':('https://personal.math.ubc.ca/~karu/papers/semist.pdf','pdf')}
def one(item):
 key,(url,ext)=item;p=root/f'S6_SERIES_PUBLISH_I_{key}.{ext}'
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as response:
   data=response.read();resolved=response.url;mime=response.headers.get('Content-Type')
  if ext=='pdf':assert data[:4]==b'%PDF',mime
  p.write_bytes(data)
  return {'key':key,'requested_url':url,'resolved_url':resolved,'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'retrieved':True}
 except Exception as e:return {'key':key,'requested_url':url,'retrieved':False,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:rows=list(ex.map(one,targets.items()))
(root/'S6_SERIES_PUBLISH_I_root_primary_retrieval.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows},indent=2)+'\n')
print(json.dumps(rows,indent=2))
