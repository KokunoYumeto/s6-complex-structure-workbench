from pathlib import Path
import datetime, hashlib, json, sys

ROOT=Path('/workspace/scratch/653608133b22')
OUT=ROOT/'work/agents/i_analytic/S6_SERIES_PUBLISH_I_final_candidate11_reading_analytic.json'
manifest=json.loads((ROOT/'work/render/I_candidate11/manifest.json').read_text())
images={x['page']:x for x in manifest['rendered_pages']}
record=json.loads(OUT.read_text())
incoming=json.loads(sys.stdin.read())
for x in incoming:
    p=x['page']; assert 86<=p<=170
    im=images[p]; image_hash=hashlib.sha256(Path(im['image']).read_bytes()).hexdigest()
    assert image_hash==im['image_sha256']
    assert p not in {y['page'] for y in record['pages']},p
    record['pages'].append({'page':p,'image_path':im['image'],'image_sha256':image_hash,
       'pdf_sha256':record['pdf_sha256'],'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'view_method':'Complete manifest image explicitly emitted with view_image; visually read at native legible scale.',
       'content_examined':x['content'],'finding':x.get('finding','CLEAR: no concrete mathematical, wording, reference, typography or layout defect found on this page.'),
       'defect_types_considered':'D01–D24, plus mathematical consistency and legibility; no automated check credit.',
       'status':x.get('status','clear')})
record['pages'].sort(key=lambda x:x['page'])
record['pages_actually_read']=[x['page'] for x in record['pages']]
record['read_count']=len(record['pages'])
record['status']='complete' if record['read_count']==85 else 'in progress'
OUT.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
md=OUT.with_suffix('.md')
lines=['# Paper I candidate 11: analytic rendered-page reading','',
       'Assigned pages: 86–170. PDF SHA256: `'+record['pdf_sha256']+'`.','',
       'Only the pages in the table below have actually been viewed and read. Rendered-page review creates no CHECK_EVENTS.','',
       '| Page | Content examined | Finding | Image SHA256 |','|---|---|---|---|']
for x in record['pages']:
    lines.append('| '+str(x['page'])+' | '+x['content_examined'].replace('|','\\|')+' | '+x['finding'].replace('|','\\|')+' | `'+x['image_sha256']+'` |')
md.write_text('\n'.join(lines)+'\n')
print(json.dumps({'read_count':record['read_count'],'last_page':record['pages'][-1]['page'],'status':record['status']}))
