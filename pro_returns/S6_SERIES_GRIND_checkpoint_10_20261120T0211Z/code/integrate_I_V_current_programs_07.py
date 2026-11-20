"""Root-reviewed complete current cusp and CM program replacements."""
from pathlib import Path
import hashlib,json,datetime,re
R=Path(__file__).resolve().parents[1];receipts=[]
for paper,patchname in [('I','audit_paper_i/arithmetic_06/C7_10_current_program_patch.json'),('V','audit_corrections/V_P111_guarded_patches_06.json')]:
    p=R/f'parts/{paper}.body.linked.tex';before=p.read_text();s=before
    patches=json.loads((R/patchname).read_text())
    for patch in patches:
        old=patch.get('old',patch.get('old_text'));new=patch.get('new',patch.get('new_text'))
        assert s.count(old)==1,(paper,patch.get('label'),s.count(old))
        s=s.replace(old,new,1)
    pattern=r'\\(?:tag|label)\{[^}]+\}'
    assert re.findall(pattern,before)==re.findall(pattern,s)
    p.write_text(s)
    receipts.append(dict(paper=paper,patch_file=patchname,patch_sha256=hashlib.sha256((R/patchname).read_bytes()).hexdigest(),before_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(s.encode()).hexdigest(),changes=patches))
programs=[]
for name,outname,countfield,count in [
('audit_paper_i/arithmetic_06/cm_witness_exact.py','audit_paper_i/arithmetic_06/cm_witness_exact.output.json','checks_passed',39),
('audit_paper_i/arithmetic_06/cm_analytic_balls.py','audit_paper_i/arithmetic_06/cm_analytic_balls.output.json','checks_passed',10),
('audit_corrections/code/reconstruct_V_cusp_06.py','audit_corrections/code/reconstruct_V_cusp_06.json','assertions',186)]:
    data=json.loads((R/outname).read_text());assert data[countfield]==count
    phash=hashlib.sha256((R/name).read_bytes()).hexdigest()
    if 'program_sha256' in data:assert phash==data['program_sha256']
    programs.append(dict(program=name,program_sha256=phash,output=outname,output_sha256=hashlib.sha256((R/outname).read_bytes()).hexdigest(),assertions=count))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),review='Root read the entire current C7.10 proposition/proof and all nine P1.11 proof steps, all three fresh programs, their guarded replacements and producing receipts. This receiving review follows printed-proof/code access and carries no new blind-reproof attribution.',scope='Exact CM algebra and stated analytic branch; complete cusp incidence/graded integral collapse calculation with actual geometric comparison retained. No transcendence conclusion or P1.19 global-cone conclusion is inferred.',receipts=receipts,programs=programs,pending='Fresh build and actual changed-page inspection.')
(R/'analysis/I_V_current_program_integration_07.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'guards':sum(len(x['changes']) for x in receipts),'programs':3}))
