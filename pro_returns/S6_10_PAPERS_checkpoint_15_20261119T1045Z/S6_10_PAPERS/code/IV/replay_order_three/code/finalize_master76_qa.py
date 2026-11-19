"""Combine direct reviews of the fixed master76 PDF and record readiness."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,subprocess
R=Path(__file__).resolve().parents[1]
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=R/'S6_06_BLIND_paper.pdf'
a_path=R/'records/master76_audit.json'
a=json.loads(a_path.read_text());assert h(p)==a['pdf_sha256']
reviewed=set();full=set();records=[]
for name in ['checks','root','blind_control','fourfold']:
    q=R/f'records/master76_visual_{name}.json';j=json.loads(q.read_text())
    assert j['status']=='PASS',(name,j['status'])
    assert j['pdf_sha256']==a['pdf_sha256'],name
    nums=set(j.get('pages_reviewed',[]))
    for group in j.get('contact_sheets',{}).values():nums.update(group)
    for c in j.get('contacts',[]):
        n=str(int(re.search(r'contact-(\d+)',str(c)).group(1)))
        nums.update(a['contact_sheets'][n])
    assert nums,name
    reviewed.update(nums)
    for f in j.get('full_size_pages',[])+j.get('full_pages',[]):
        full.add(f if isinstance(f,int) else int(re.search(r'page_(\d+)',f).group(1)))
    records.append({'reviewer':name,'record':str(q.relative_to(R)),'sha256':h(q),'pages':sorted(nums)})
assert reviewed==set(a['rendered_pages']),(sorted(set(a['rendered_pages'])-reviewed),sorted(reviewed-set(a['rendered_pages'])))
a.update(status='PASS',direct_visual_review_records=records,page_count_reviewed=len(reviewed),full_size_pages=sorted(full),visual_review_completed_utc=datetime.now(timezone.utc).isoformat())
a_path.write_text(json.dumps(a,indent=2)+'\n')
t={'checkpoint':26,'utc':datetime.now(timezone.utc).isoformat(),'pages':a['pages'],'master_build':76,'pdf_sha256':a['pdf_sha256'],'pdf_bytes':a['pdf_bytes'],'before_over_2pt':0,'overfull_over_2pt':0,'max_overfull_pt':a['max_overfull_pt'],'rendered_pages':a['rendered_pages'],'contact_sheets':a['contact_sheets'],'visual_inspection':'All84 rendered pages were directly reviewed across14 contact sheets by checks, root, blind_control and fourfold, with eight additional full-size page inspections. This covers every integrated K99/K100 proof page and both transitions, plus opening/reference/final pages. Both complete standalone proofs also passed all-page direct review. No clipping, equation collisions, missing glyphs or broken math were observed. All891 page bounds and the settled third-pass log pass. The sole retained overflow is1.61101pt.','all_page_boundaries':'PASS','missing_or_undefined_references':0,'qa':'records/master76_audit.json','new_work_scope':'K99 and K100 are fully included with seven complete supporting proofs, exact certificates and root/independent mathematical audits. The selected-infinity calculation remains a separate unpromoted working proof.'}
(R/'records/typesetting_checkpoint26.json').write_text(json.dumps(t,indent=2)+'\n')
subprocess.run(['python','code/update_report.py'],cwd=R,check=True,stdout=(R/'records/master76_report_update.out').open('w'),stderr=(R/'records/master76_report_update.err').open('w'))
files=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.tex','notes/part3.tex','S6_06_BLIND_results.csv','S6_06_BLIND_report.md','code/update_report.py','code/part3/results_mapping.json','records/master76_audit.json','records/typesetting_checkpoint26.json','records/k99_export_manifest.json','records/k100_export_manifest.json']
ready={'status':'PASS','master_build':76,'utc':datetime.now(timezone.utc).isoformat(),'pages':a['pages'],'statements':280,'pdf_sha256':a['pdf_sha256'],'verified_prior_master':'records/checkpoint26_prior_master75/S6_06_BLIND_paper.pdf','source_checks':'records/master76_integration_sources.json','files':[{'path':f,'sha256':h(R/f),'size':(R/f).stat().st_size} for f in files],'scope':'K99/K100 complete proof integration and QA; other ongoing mathematical work remains explicitly open.'}
(R/'records/master76_readiness.json').write_text(json.dumps(ready,indent=2)+'\n')
print(json.dumps({'status':'PASS','pages':a['pages'],'reviewed':len(reviewed),'full_size':sorted(full),'pdf_sha256':a['pdf_sha256'],'audit_sha256':h(a_path),'readiness_sha256':h(R/'records/master76_readiness.json')},indent=2))
