from pathlib import Path
import json,hashlib,datetime,shutil
import fitz
from PIL import Image
W=Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_work')
A=W/'audit_corrections/P119_geometric_09'
diag=W/'code/outputs/build_41/S6_SERIES_GRIND_V_diagnostics.json'
if not diag.exists():
    print('V BUILD41 PENDING')
    raise SystemExit(2)
diagnostics=json.loads(diag.read_text())
assert diagnostics['returncode']==0,diagnostics
Q=A/'QA_build41';Q.mkdir(exist_ok=True)
for src,dst in [('S6_SERIES_GRIND_V.pdf','S6_SERIES_GRIND_V_build41.pdf'),('S6_SERIES_GRIND_V.tex','S6_SERIES_GRIND_V_build41.tex'),('parts/V.body.linked.tex','V.body.linked_build41.tex'),('S6_SERIES_GRIND_V.aux','S6_SERIES_GRIND_V_build41.aux'),('code/outputs/build_41/S6_SERIES_GRIND_V_diagnostics.json','build41_diagnostics.json')]:
    shutil.copyfile(W/src,Q/dst)
def rec(p):
    return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
base=json.loads((A/'build40_V_visual_QA.json').read_text())
doc=fitz.open(Q/'S6_SERIES_GRIND_V_build41.pdf')
rows=[]
for r in base['actually_viewed_page_images']:
    n=r['page'];old=Image.open(r['path']).convert('RGB')
    pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(110/72,110/72),alpha=False)
    new=Q/f'V41_page_{n:03d}.png';pix.save(new)
    match=old.size==(pix.width,pix.height) and old.tobytes()==pix.samples
    rows.append({'page':n,'source_actually_viewed_image':r,'current_image':rec(new),'render_dimensions':[pix.width,pix.height],'raw_pixel_sha256':hashlib.sha256(pix.samples).hexdigest(),'exact_full_page_pixels_equal':match})
receipt={'task':'Exact full-page transport of current V visual QA from build40 to build41','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'GPT-6 Astra, ChatGPT Pro mode; reasoning effort inherited and not separately exposed','current_pdf':rec(Q/'S6_SERIES_GRIND_V_build41.pdf'),'pages':len(doc),'current_assembled_source':rec(Q/'S6_SERIES_GRIND_V_build41.tex'),'current_linked_body':rec(Q/'V.body.linked_build41.tex'),'current_aux':rec(Q/'S6_SERIES_GRIND_V_build41.aux'),'diagnostics':diagnostics,'source_actual_view_receipt':rec(A/'build40_V_visual_QA.json'),'source_actual_views':[94,95,96,97,98,99,100,101,102,103,116,215,216,217,218,219,220],'transport_method':'Render each complete current page at the identical110-dpi fitz RGB settings, then compare width, height and every RGB byte against its previously actually viewed build40 page PNG. PNG file metadata/compression is not used as a substitute for raw pixel equality.','comparisons':rows,'fresh_actual_build41_views':[],'transported_pages':[r['page'] for r in rows if r['exact_full_page_pixels_equal']],'different_pages':[r['page'] for r in rows if not r['exact_full_page_pixels_equal']],'result':'PASS' if all(r['exact_full_page_pixels_equal'] for r in rows) else 'DIFFERENT PAGES REQUIRE ACTUAL VIEW','canonical_writes':False,'completion_scope':'Rendering/wording QA only. P1.19 all-degree before-reading confidence is still pending; no whole-row completion asserted.'}
out=A/'build41_V_visual_QA_transport.json';out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receipt':rec(out),'current_pdf':receipt['current_pdf'],'transported_pages':receipt['transported_pages'],'different_pages':receipt['different_pages'],'result':receipt['result']},indent=2))
