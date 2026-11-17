#!/usr/bin/env python3
"""Extend the final PaperII render selection and compare it with reviewed PNGs.

This script makes no visual-quality assertion. Images still must be opened.
"""
from pathlib import Path
import hashlib,json,re,subprocess,math
from PIL import Image,ImageChops,ImageDraw

D=Path(__file__).resolve().parents[2]
W=D/'work/cdp_audit/II_final_visual_review';W.mkdir(exist_ok=True)
pdf=D/'S6_09_PAPERS_II.pdf'
pdfhash=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert pdfhash=='f48505e66a68095c8bde9969866da6d6dbd21f341edf077339200316ffec745c'
dest=D/'validation'/('II_'+pdfhash[:12])
base=json.loads((dest/'render_manifest.json').read_text())
old=D/'validation/II_c8feaaa21980'
oldmanifest=json.loads((old/'render_manifest.json').read_text())
oldreview=json.loads((old/'visual_review.json').read_text())
previous_covered=set(oldreview['previously_reviewed_pixel_identical_pages'])|set(oldreview['actual_final_contact_pages'])
selected={r['page']:list(r['reasons']) for r in base['rendered']}
def add(p,why):
    assert 1<=p<=659
    if why not in selected.setdefault(p,[]):selected[p].append(why)
for p in range(543,549):add(p,'Known INV E1.1 statement/credit and complete moved proof with surrounding flow')
for p in [560,561,568,569,571,572,593,594,595,596,597]:
    add(p,'One of six exact new WORKING_CDP attribution passages and following flow')
for p in [570,571]:add(p,'Corrected BS76 finite-complex theorem locator and Uses line')
for p in range(601,640):add(p,'Complete result index, including continuation on p639; 50 attribution rows changed')
for p in range(649,660):add(p,'Complete final inline bibliography')

records=[]
for p,why in sorted(selected.items()):
    png=dest/f'page_{p:04d}.png'
    if not png.exists():
        subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','110','-png','-singlefile',str(pdf),str(png.with_suffix(''))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    prev=old/f'page_{p:04d}.png'
    identical=False;priorhash=None
    if prev.exists() and p in previous_covered:
        current_im=Image.open(png).convert('RGB');previous_im=Image.open(prev).convert('RGB')
        identical=current_im.size==previous_im.size and ImageChops.difference(current_im,previous_im).getbbox() is None
        priorhash=hashlib.sha256(prev.read_bytes()).hexdigest()
    records.append({'page':p,'file':str(png.relative_to(D)),
      'sha256':hashlib.sha256(png.read_bytes()).hexdigest(),'reasons':why,
      'previous_image':str(prev.relative_to(D)) if prev.exists() else None,
      'previous_sha256':priorhash,'previous_review_covers_page':p in previous_covered,
      'pixel_identical_to_previously_reviewed_image':identical,
      'requires_actual_new_opening':not identical})

todo=[r for r in records if r['requires_actual_new_opening']]
contacts=[]
for start in range(0,len(todo),4):
    group=todo[start:start+4]
    canvas=Image.new('RGB',(1240,840*math.ceil(len(group)/2)),'white')
    for j,r in enumerate(group):
        im=Image.open(D/r['file']).convert('RGB');im.thumbnail((600,800))
        tile=Image.new('RGB',(620,840),'#d9dfe7');tile.paste(im,((620-im.width)//2,30))
        ImageDraw.Draw(tile).text((14,8),f"Final Paper II, page {r['page']}",fill='black')
        canvas.paste(tile,((j%2)*620,(j//2)*840))
    path=W/f'review_contact_{start//4+1:02d}.png';canvas.save(path)
    contacts.append({'file':str(path.relative_to(D)),'pages':[r['page'] for r in group],
      'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
report={'paper':'II','build':15,'pdf_sha256':pdfhash,'pdf_pages':659,
 'tex_sha256':hashlib.sha256((D/'S6_09_PAPERS_II.tex').read_bytes()).hexdigest(),
 'base_render_manifest':str((dest/'render_manifest.json').relative_to(D)),
 'prior_render_manifest':str((old/'render_manifest.json').relative_to(D)),
 'prior_visual_review':str((old/'visual_review.json').relative_to(D)),
 'prior_review_chain':'validation/II_c8feaaa21980/visual_review.json -> validation/II_665a15babe20/visual_review.json',
 'total_selected_pages':len(records),'selected_pages':[r['page'] for r in records],
 'pixel_identical_previously_reviewed_pages':[r['page'] for r in records if not r['requires_actual_new_opening']],
 'requires_actual_new_opening':[r['page'] for r in todo],
 'rendered':records,'contacts':contacts,
 'visual_inspection_status':'Not yet asserted. Exact images in requires_actual_new_opening must be opened before a final quality conclusion.'}
(W/'render_comparison.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['pdf_sha256','tex_sha256','total_selected_pages','pixel_identical_previously_reviewed_pages','requires_actual_new_opening']},indent=2))
print('Contact sheets requiring actual opening:',len(contacts))
