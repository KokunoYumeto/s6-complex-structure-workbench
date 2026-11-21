from pathlib import Path
import json,hashlib,datetime,sys
base=Path('/workspace/scratch/653608133b22');folder=base/'work/agents/i_topology';out=folder/'S6_SERIES_PUBLISH_I_final_candidate11_reading_topology.json'
manifest=json.loads((base/'work/render/I_candidate11/manifest.json').read_text());m={x['page']:x for x in manifest['rendered_pages']}
pdfsha='02033ddcb1602d22fc09bc05865e772392daadc54c93cb60da14c91f6dfe62cc'
assert manifest['pdf_sha256']==pdfsha
if out.exists():j=json.loads(out.read_text())
else:j={'candidate':'I_candidate11','source_sha256':'7479a42f0c18cb2853e483ba3b0b222087e800a6a720ca5f2a21313ff6706cc6','pdf_sha256':pdfsha,'assigned_pages':[171,255],'method':'Every recorded page was explicitly viewed as a complete rendered image and read. Text was used only as a supplement; source/zoom checks are separately disclosed. Visual QA creates no mathematical check credit.','pages':[]}
rows=json.load(sys.stdin)
for row in rows:
 n=row['page'];assert 171<=n<=255
 im=Path(m[n]['image']);h=hashlib.sha256(im.read_bytes()).hexdigest();assert h==m[n]['image_sha256']
 row.update({'image':str(im),'image_sha256':h,'pdf_sha256':pdfsha,'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reading':'entire rendered page explicitly viewed and read'})
 j['pages']=[x for x in j['pages'] if x['page']!=n]+[row]
j['pages'].sort(key=lambda x:x['page']);j['read_page_count']=len(j['pages']);j['complete']=len(j['pages'])==85
out.write_text(json.dumps(j,indent=2)+'\n')
md=['# Paper I candidate11: rendered topology reading','',f'PDF SHA256 `{pdfsha}`.',f'Assigned pages171–255. Actually read: {len(j["pages"])}/85.','',j['method'],'']
for r in j['pages']:
 md += [f'## Page {r["page"]}','',r['content_examined'],'',r['finding'],'',f'Image SHA256 `{r["image_sha256"]}`. PDF SHA256 `{r["pdf_sha256"]}`.','']
(folder/'S6_SERIES_PUBLISH_I_final_candidate11_reading_topology.md').write_text('\n'.join(md))
print(json.dumps({'read_page_count':j['read_page_count'],'latest_pages':[x['page'] for x in rows],'complete':j['complete']}))
