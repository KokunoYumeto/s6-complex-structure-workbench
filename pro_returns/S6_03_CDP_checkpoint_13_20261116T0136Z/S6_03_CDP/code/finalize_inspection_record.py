"""Record the additional final PDF pages actually inspected by root."""
from pathlib import Path
from datetime import datetime,timezone
import json,shutil
r=Path(__file__).resolve().parents[1]
p=r/'records/root_final_visual_inspection.json';inspection=json.loads(p.read_text());old=inspection['pages'];new=sorted(set(old)|{121,207});inspection['pages']=new;inspection['recorded_utc']=datetime.now(timezone.utc).isoformat();p.write_text(json.dumps(inspection,indent=2)+'\n')
q=r/'build/visual_qa/manifest.json';qa=json.loads(q.read_text());old_count=len(qa['rendered_pages'])
for n in [121,207]:
 shutil.copy2(r/f'build/final_inspection/page_{n:03}.png',r/f'build/visual_qa/page_{n:03}.png')
 qa['additional_final_inspection_images'][str(n)]=f'page_{n:03}.png'
qa['rendered_pages']=sorted(set(qa['rendered_pages'])|set(new));q.write_text(json.dumps(qa,indent=2)+'\n')
m=r/'records/root_completion_manifest.json';v=json.loads(m.read_text());v['actually_inspected_pages']=new;v['rendered_pages']=len(qa['rendered_pages']);m.write_text(json.dumps(v,indent=2)+'\n')
p=r/'S6_03_CDP_report.md';s=p.read_text();s=s.replace('inspected final pages '+','.join(map(str,old)),'inspected final pages '+','.join(map(str,new)));s=s.replace(str(old_count)+' actually rendered pages',str(len(qa['rendered_pages']))+' actually rendered pages');p.write_text(s)
print(json.dumps({'inspected_pages':new,'rendered_pages':len(qa['rendered_pages'])},indent=2))
