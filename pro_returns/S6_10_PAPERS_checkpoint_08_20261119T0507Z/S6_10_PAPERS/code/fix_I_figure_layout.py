"""Repair two observed TikZ label collisions without changing their content."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

P=Path(__file__).resolve().parents[1]
replacements=[
    (r'align=center,minimum width=2.65cm,minimum height=1.05cm',
     r'align=center,text width=2.8cm,minimum height=1.2cm'),
    (r'{$3S_1$\\free order-three root quotient};',
     r'{$3S_1$\\free order-three\\root quotient};'),
    (r'{$4S_2$\\free order-four root quotient};',
     r'{$4S_2$\\free order-four\\root quotient};'),
    (r'\node[anchor=west,align=left] at (.25,-2.1)'+'\n'+
     r' {all admissible members\\retain $3S_1,4S_2,W$};',
     r'\node[anchor=west,align=left] at (3.15,-2.1)'+'\n'+
     r' {all admissible members\\retain $3S_1,4S_2,W$};'+'\n'+
     r'\draw[->] (3.05,-1.95)--(1.85,-1.7);')
]
records=[]
for name in ['papers/I/figures.tex','build/I_preview/preview.tex']:
    p=P/name;s=p.read_text();t=s
    for index,(a,b) in enumerate(replacements):
        assert t.count(a)==(3 if index==0 else 1),(name,index,t.count(a))
        t=t.replace(a,b)
    p.write_text(t)
    records.append({'path':name,'before_sha256':hashlib.sha256(s.encode()).hexdigest(),
                    'after_sha256':hashlib.sha256(t.encode()).hexdigest()})
receipt={'recorded_at':datetime.now(timezone.utc).isoformat(),
         'scope':'Observed visual layout correction only; wording, mathematical coordinates, maps and labels unchanged.',
         'observations':['Figure1 long node text overlapped the adjacent node. Explicit three-line captions and fixed text widths separate the boxes.',
                         'Figure2 the dashed outer circle crossed the lower annotation. Its unchanged text is moved outside the circle with a leader arrow.'],
         'problem_images':['analysis/final_root_visual/I_p0096.png','analysis/final_root_visual/I_p0097.png'],
         'files':records}
(P/'analysis/I_final_figure_layout_repair.json').write_text(json.dumps(receipt,indent=2)+'\n')
manifest=P/'analysis/final_root_visual/render_manifest.json'
x=json.loads(manifest.read_text())
x[0]['finding']='Sampled text pages were clean. Figure1 showed adjacent node-text overlap and Figure2 a boundary stroke crossing its lower annotation; these exact images prompted the separate layout repair. The later rebuilt PDF requires fresh final visual evidence.'
manifest.write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
