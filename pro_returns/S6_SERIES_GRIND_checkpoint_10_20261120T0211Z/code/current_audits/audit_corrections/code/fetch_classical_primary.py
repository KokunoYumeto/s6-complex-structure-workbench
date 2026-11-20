from pathlib import Path
import urllib.request,hashlib,json,subprocess,sys
root=Path(__file__).resolve().parents[1]/'primary_sources'
root.mkdir(exist_ok=True)
sources={
 'Jiang2014':('https://archive.ymsc.tsinghua.edu.cn/pacm_download/613/12072-v4Regular_circle_actions_on_2-connected_7-manifolds.pdf','1bc65d56cb2dd79e9c08f4dee3dab5fd4f82c65b0bdb6b95ebc5a3336504e762'),
 'HarveyKerinShankar2020':('https://ems.press/content/serial-article-files/26574?nt=1','2330706f3e68a3bdfe19d8068e4ce5c520e2123c85952d655254cbe734295870'),
 'Davis1982':('https://people.math.osu.edu/davis.12/old_papers/AJM-82.pdf','1c42dd240d64efc5378b052ffa18431622ff412fcf5f4887cb875f5f3d34ba9b')}
name=sys.argv[1];url,old_hash=sources[name]
meta={'source':name,'url':url,'date':'2026-11-19','retained_edition_sha256':old_hash}
try:
 data=urllib.request.urlopen(url,timeout=25).read()
 if not data.startswith(b'%PDF'):raise RuntimeError('Returned file is not a PDF')
 p=root/(name+'_fresh.pdf');p.write_bytes(data)
 meta.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 meta['same_as_retained_edition']=meta['sha256']==old_hash
 done=subprocess.run(['pdftotext','-layout',str(p),str(root/(name+'_fresh.txt'))],capture_output=True,text=True)
 meta.update(pdftotext_returncode=done.returncode,pdftotext_stderr=done.stderr)
except Exception as ex:meta['error']=str(ex)
(root/(name+'_fresh_metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
