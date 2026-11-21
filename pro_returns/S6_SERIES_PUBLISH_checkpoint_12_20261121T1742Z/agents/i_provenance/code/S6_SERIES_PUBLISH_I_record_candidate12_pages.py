"""Append explicit human-readable observations after actual candidate12 image views."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

W=Path('/workspace/scratch/653608133b22/work');O=W/'agents/i_provenance'
M=W/'render/I_candidate12/manifest.json';D=json.loads(M.read_text())
SOURCE='38fd3831cb7be2eb60d856024571f9f8ec9105df45b445714251c41932580bbb'
PDF='81e248f91faf3e69f8f5b9a93c94d7eb68c6a40496d3d4d9dfa26e0c62094248'
P=O/'S6_SERIES_PUBLISH_I_final_candidate12_reading_provenance.json'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert D['pdf_sha256']==PDF and D['pages']==344 and sha(D['pdf'])==PDF
pages={r['page']:r for r in D['rendered_pages']}
now=datetime.now(timezone.utc).isoformat()
record=json.loads(P.read_text()) if P.exists() else dict(
 schema=1,agent='provenance_inventory',paper='I',candidate='12',source_sha256=SOURCE,
 pdf=D['pdf'],pdf_sha256=PDF,pdf_pages=344,render_manifest=str(M),render_manifest_sha256=sha(M),
 assigned_pages=list(range(256,345)),method='Actually displayed and read each complete rendered page image; text extraction is not substituted for page reading.',
 started_utc=now,status='in progress',mathematical_events_added=0,pages=[],pages_read=0,
 checks_scope='Register defects, mathematical wording and retained maps/hypotheses, references, typography, page layout, final program table and bibliography. Only concrete unavoidable defects are proposed to root.')
assert record['source_sha256']==SOURCE and record['pdf_sha256']==PDF
seen={r['page'] for r in record['pages']}
for observation in json.load(sys.stdin):
 n=observation['page'];assert n in record['assigned_pages'] and n not in seen
 r=pages[n];assert sha(r['image'])==r['image_sha256']
 record['pages'].append(dict(page=n,image=r['image'],image_sha256=r['image_sha256'],pdf_sha256=PDF,
   source_sha256=SOURCE,read_utc=now,method='Actually displayed and read the complete rendered page image.',
   content=observation['content'],finding=observation.get('finding','All text, formulas, references and layout are legible; no concrete defect found.'),math_events_added=0))
 seen.add(n)
record['pages'].sort(key=lambda r:r['page']);record['pages_read']=len(record['pages'])
if seen==set(record['assigned_pages']):record['status']='complete';record['completed_utc']=now
P.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
md=['# Paper I candidate12: actual rendered-page reading','',f'Source SHA-256: `{SOURCE}`. PDF SHA-256: `{PDF}`.',
 f"Read {record['pages_read']} of {len(record['assigned_pages'])} assigned complete page images. Mathematical events added: zero.",'',
 '| Page | Content actually read | Finding | Image SHA-256 |','|---|---|---|---|']
for r in record['pages']:md.append('| '+' | '.join(str(x).replace('|','\\|') for x in [r['page'],r['content'],r['finding'],r['image_sha256']])+' |')
P.with_suffix('.md').write_text('\n'.join(md)+'\n')
print(json.dumps(dict(pages_read=record['pages_read'],status=record['status'],record=str(P),sha256=sha(P)),indent=2))
