"""Record actual root image inspections and render the remaining IV changes."""
from pathlib import Path
import datetime, hashlib, json, re
import fitz
from PIL import Image, ImageDraw

R=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for paper in ['I','III','V']:
    data=json.loads((R/f'analysis/build26_changed_render_{paper}.json').read_text())
    assert hashlib.sha256((R/f'S6_SERIES_GRIND_{paper}.pdf').read_bytes()).hexdigest()==data['pdf_sha256']
    for sheet in data['sheets']:
        assert hashlib.sha256((R/sheet['path']).read_bytes()).hexdigest()==sheet['sha256']
    data.update({'inspection_state':'Actually viewed every listed sheet in the root image tool',
      'recorded_at_utc':now,'reviewer':'GPT-6 Astra, root, inherited effort',
      'result':'PASS: no clipping, missing glyph, equation, proof-label or path defect on the listed pages',
      'scope':'Changed-page visual inspection; this receipt does not assert a view of every page or a new prereading proof.'})
    if paper=='I':
        data['specific_observation']='The formerly deferred/overlapping proof labels are now separate at the repaired headings; the exact CM program and period-basis map fit completely on page397.'
    if paper=='III':
        p=R/'build/visual_qa_26/III279_top_detail.png'
        data['additional_actual_view']={'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
        data['specific_observation']='Standalone top detail confirms the complete level-one label7 immediately before the second framing heading. Page278 was rendered and text-read but not image-viewed.'
    if paper=='V':
        data['specific_observation']='Includes the complete P1.12 and P1.19 statements/proofs on pages91–98, with the full degree2/3 matrices, primitive functional, cokernel adapter and actual chain homotopies. The complete period proofs have a separate agent receipt.'
    (R/f'audit_root/build26_{paper}_changed_visual_QA.json').write_text(json.dumps(data,indent=2)+'\n')

pdf=R/'S6_SERIES_GRIND_IV.pdf';d=fitz.open(pdf)
needles=['Closed forms on the exterior','Geometric cap restrictions','Boundary primitives',
 'Multiplicative collar calculation','Explicit change to the inverse mapping-torus convention',
 'proof 20, substep 6']
texts=[' '.join(p.get_text().split()) for p in d]
hits={s:[i+1 for i,t in enumerate(texts) if s in t] for s in needles}
assert all(hits.values()),hits
pages=sorted({p for ps in hits.values() for p in ps})
sheets=[]
for k in range(0,len(pages),2):
    pair=pages[k:k+2];canvas=Image.new('RGB',(2260,1600),(235,235,235));draw=ImageDraw.Draw(canvas)
    for j,p in enumerate(pair):
        pm=d[p-1].get_pixmap(matrix=fitz.Matrix(1.85,1.85))
        im=Image.frombytes('RGB',(pm.width,pm.height),pm.samples)
        im.thumbnail((1085,1505))
        canvas.paste(im,(30+1130*j,40));draw.text((30+1130*j,15),f'IV, page {p}',fill='black')
    rel=f'build/visual_qa_26/root_IV_repaired_{k//2+1:02d}.png';canvas.save(R/rel)
    sheets.append({'path':rel,'pages':pair,'sha256':hashlib.sha256((R/rel).read_bytes()).hexdigest()})
out={'build':26,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':pages,'hits':hits,
 'sheets':sheets,'inspection_state':'Rendered; not yet viewed','recorded_at_utc':now}
(R/'analysis/build26_root_IV_repaired_render.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'recorded_actual_root_view':{'I':8,'III':3,'V':22},'IV_rendered':pages,'sheets':sheets}))
