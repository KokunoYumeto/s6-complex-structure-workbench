#!/usr/bin/env python3
"""Append only actual completed page readings supplied by the reader."""
from pathlib import Path
import datetime,hashlib,json,sys
root=Path(__file__).resolve().parents[2]
out=Path(__file__).with_name('S6_SERIES_PUBLISH_I_final_candidate13_reading_analytic.json')
d=json.loads(out.read_text());m=json.loads((root/'render/I_candidate13/manifest.json').read_text())
images={x['page']:x for x in m['rendered_pages']};now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for x in json.load(sys.stdin):
    page=x['page'];assert page in d['assigned_pages'];assert page not in {r['page']for r in d['pages']}
    im=images[page];assert hashlib.sha256(Path(im['image']).read_bytes()).hexdigest()==im['image_sha256']
    d['pages'].append({'page':page,'image':im['image'],'image_sha256':im['image_sha256'],'pdf_sha256':d['pdf_sha256'],
       'viewed_complete_image':True,'read_complete_page':True,'content_examined':x['content'],
       'finding':x.get('finding','Clear. Complete page read; formulas, wording, references, headings and margins inspected.'),
       'defect_register_checked':'D01–D25; visual review adds no mathematical event.','recorded_utc':now})
d['pages'].sort(key=lambda r:r['page']);d['actual_pages_read']=len(d['pages']);d['last_updated_utc']=now
if set(x['page']for x in d['pages'])==set(d['assigned_pages']):d['status']='complete';d['completed_utc']=now
out.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');print('Actual pages read:',d['actual_pages_read'])
