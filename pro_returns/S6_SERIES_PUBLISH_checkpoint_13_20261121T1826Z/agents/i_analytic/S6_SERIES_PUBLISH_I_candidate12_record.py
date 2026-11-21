import json, pathlib, hashlib, datetime, sys
base=pathlib.Path('/workspace/scratch/653608133b22')
p=base/'work/agents/i_analytic/S6_SERIES_PUBLISH_I_final_candidate12_reading_analytic.json'
d=json.loads(p.read_text())
m=json.loads((base/'work/render/I_candidate12/manifest.json').read_text())
lookup={x['page']:x for x in m['rendered_pages']}
entries=json.load(sys.stdin)
for e in entries:
    page=e['page']; src=lookup[page]; ip=pathlib.Path(src['image'])
    sha=hashlib.sha256(ip.read_bytes()).hexdigest()
    assert sha==src['image_sha256']
    assert page in d['assigned_pages']
    assert not any(x['page']==page for x in d['pages']),page
    d['pages'].append({'page':page,'image':str(ip),'image_sha256':sha,'pdf_sha256':d['pdf_sha256'],'viewed_complete_image':True,'read_complete_page':True,'content_examined':e['content'],'finding':e.get('finding','Clear: all text, formulae, references, heading and page flow examined; no concrete remaining mathematical, wording, citation or layout defect observed.'),'defect_register_checked':'D01-D24 and mathematical consistency','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
d['pages'].sort(key=lambda x:x['page'])
d['actual_pages_read']=len(d['pages'])
d['last_updated_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
d['status']='complete' if len(d['pages'])==len(d['assigned_pages']) else 'in_progress'
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
print(f"Saved {len(d['pages'])}/{len(d['assigned_pages'])} actually read pages; last {d['pages'][-1]['page']}.")
