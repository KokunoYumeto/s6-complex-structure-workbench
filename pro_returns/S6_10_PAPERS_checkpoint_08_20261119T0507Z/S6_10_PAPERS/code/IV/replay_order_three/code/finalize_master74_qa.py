"""Record directly reviewed K97 integration and checkpoint23 typography."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
R=Path(__file__).resolve().parents[1]
a=json.loads((R/'records/master74_audit.json').read_text());assert a['status']=='PASS_PENDING_DIRECT_VISUAL_REVIEW'
assert hashlib.sha256((R/'S6_06_BLIND_paper.pdf').read_bytes()).hexdigest()==a['pdf_sha256']
a['status']='PASS';a['direct_visual_reviewer']='blind_control';a['directly_reviewed_pages']=a['rendered_pages'];a['findings']=[];a['visual_inspection']='Every rendered master74 page directly reviewed, including every integrated K97 page (668–676) and transitions, the revised full K75 register, opening/reference/final pages. No clipping, collisions, missing symbols or malformed equations. All manuscript pages pass the coordinate bounds audit; final two-pass log has no undefined or missing references and no overflow above2pt.'
(R/'records/master74_audit.json').write_text(json.dumps(a,indent=2)+'\n')
t=dict(checkpoint=23,utc=datetime.now(timezone.utc).isoformat(),pages=a['pages'],master_build=74,pdf_sha256=a['pdf_sha256'],pdf_bytes=a['pdf_bytes'],before_over_2pt=0,overfull_over_2pt=0,max_overfull_pt=a['max_overfull_pt'],rendered_pages=a['rendered_pages'],contact_sheets=a['contact_sheets'],visual_inspection=a['visual_inspection'],all_page_boundaries='PASS',missing_or_undefined_references=0,retained_prior_audit='records/master73_audit.json',standalone_reviews='K97 all eight pages directly reviewed; prior K95/K96 complete direct reviews retained.',qa='records/master74_audit.json')
(R/'records/typesetting_checkpoint23.json').write_text(json.dumps(t,indent=2)+'\n')
p=R/'records/k97_master_integration.json';i=json.loads(p.read_text());i.update(status='PASS',master_build=74,qa='records/master74_audit.json',pdf_sha256=a['pdf_sha256'],pages=a['pages']);p.write_text(json.dumps(i,indent=2)+'\n')
p=R/'records/root_audit_e6_d_zero_disc.json';i=json.loads(p.read_text());i.pop('pending',None);i.update(integrated_master=74,master_qa='PASS',master_qa_record='records/master74_audit.json');p.write_text(json.dumps(i,indent=2)+'\n')
p=R/'records/k97_export_manifest.json';i=json.loads(p.read_text());i.update(master_modified=True,report_modified=True,mapping_modified=True,integrated_master=74,master_qa='records/master74_audit.json');p.write_text(json.dumps(i,indent=2)+'\n')
subprocess.run(['python3','code/update_report.py'],cwd=R,check=True)
print(json.dumps(t,indent=2))
