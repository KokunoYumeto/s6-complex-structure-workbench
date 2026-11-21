from pathlib import Path
import json,hashlib,datetime,sys
R=Path('/workspace/scratch/653608133b22');D=R/'work/agents/i_topology';M=json.loads((R/'work/render/I_candidate13/manifest.json').read_text());P=D/'S6_SERIES_PUBLISH_I_final_candidate13_reading_topology.json';src='26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e';pdf='519355e39d7d821a10d728d5c8dbf69a50826ee215ab98619803d44e1cae2a2b';assert M['pdf_sha256']==pdf
if P.exists():d=json.loads(P.read_text())
else:d=dict(candidate='I_candidate13',source_sha256=src,pdf_sha256=pdf,assigned_pages=[171,255],method='Every recorded page was explicitly viewed as a complete rendered image and read. Text is supplementary only; no mathematical event or independent credit arises from this visual gate.',pages=[])
rows={x['page']:x for x in d['pages']};manifest={x['page']:x for x in M['rendered_pages']};new=json.load(sys.stdin)
for x in new:
 n=x['page'];assert 171<=n<=255;m=manifest[n];p=Path(m['image']);h=hashlib.sha256(p.read_bytes()).hexdigest();assert h==m['image_sha256'];assert n not in rows,'Do not silently overwrite an earlier actual-reading row'
 x.update(image=str(p),image_sha256=h,pdf_sha256=pdf,read_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reading='entire rendered page explicitly viewed and read');x.setdefault('status','clear');rows[n]=x
assert d['pdf_sha256']==pdf;d['pages']=[rows[n] for n in sorted(rows)];d['completed_pages']=len(rows);d['missing_pages']=[n for n in range(171,256) if n not in rows];d['updated_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();P.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
md=['# Paper I candidate13 — topology rendered-page reading','',f'Source SHA256: `{src}`',f'PDF SHA256: `{pdf}`',f'Actual pages read: {len(rows)}/85.', '',d['method'],'']
for x in d['pages']:md.extend([f"## Page {x['page']}",'',x['content_examined'],'',x['finding'],'',f"Image SHA256: `{x['image_sha256']}`",''])
P.with_suffix('.md').write_text('\n'.join(md)+'\n');print(json.dumps({'recorded':sorted(x['page'] for x in new),'complete':len(rows),'remaining':len(d['missing_pages'])}))
