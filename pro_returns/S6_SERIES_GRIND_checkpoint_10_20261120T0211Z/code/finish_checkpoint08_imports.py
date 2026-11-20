"""Complete only the P1.19 tail after the recorded owner-assertion failure."""
from pathlib import Path
from datetime import datetime, timezone
import json
R=Path(__file__).resolve().parents[1]
out=R/'analysis/final_imports_checkpoint08.json'
assert not out.exists()
for name in ['UN13_final_completion_08.json','P14_final_completion_08.json']:
    assert (R/'analysis'/name).exists()
p=R/'audit_corrections/row_assessments.json'; rows=json.loads(p.read_text())
before=rows['night:P1.19'].copy()
assert not before.get('completion_state','').startswith('done')
rows['night:P1.19']['format_check']='PASS for the open-problem disposition: P1.19 is in the final part with original permanent labels and all formula tags retained. Global geometric-complex claims are qualified; the exact integral polyhedral-to-finite-cap/based-meridian adapter is stated as the remaining gate. Inventory status is open.'
rows['night:P1.19']['layout_check']='PASS: root actually viewed all final-part pages213–217 in build31; audit_root/build31_V_final_part_visual_QA.json. Each page is exactly pixel-identical in current build32; audit_root/build32_V_final_part_transport.json. Build32 page107 diagnostic was separately viewed. This grants no mathematical completion.'
p.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
receipt={'utc':datetime.now(timezone.utc).isoformat(),'completed':['cdp:st:C.2.UN.13','night:P1.4'],'P119_before':before,'P119_after':rows['night:P1.19'],'execution_note':'final_imports_checkpoint08.py completed both whole-row imports and QA receipts, then raised at its incorrect audit_root owner assertion before touching P1.19. This tail uses the actual audit_corrections owner and does not repeat either completed import.'}
out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'completed':receipt['completed'],'P1.19':'open; format/layout updated only'}))
