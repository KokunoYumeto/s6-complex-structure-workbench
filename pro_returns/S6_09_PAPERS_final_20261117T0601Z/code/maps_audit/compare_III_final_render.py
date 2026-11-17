#!/usr/bin/env python3
"""Pixel comparison and four-page contacts; rendering is not a visual pass."""
from pathlib import Path
import hashlib
import json
import math
import subprocess
from PIL import Image, ImageChops, ImageDraw

D=Path(__file__).resolve().parents[2]
OLD=D/'validation/III_0b2ac1b041c6'
NEW=D/'validation/III_2cfadc0d4d62'
OUT=NEW/'maps_changed_review'
PDF=D/'S6_09_PAPERS_III.pdf'
EXPECTED='2cfadc0d4d62cc8754ff2ff7a56de60b36cdb8ccad49d60c716fed5696951fa7'
PRIOR_REVIEW=OLD/'root_visual_review_build19.json'
CURRENT_MANIFEST=NEW/'render_manifest.json'

def file_sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pixels_sha(im): return hashlib.sha256(im.tobytes()).hexdigest()

def main():
    old_path=OLD/'render_manifest.json';new_path=CURRENT_MANIFEST
    old=json.loads(old_path.read_text());new=json.loads(new_path.read_text())
    review_path=PRIOR_REVIEW
    reviewed=json.loads(review_path.read_text())
    assert old['pdf_sha256']==reviewed['pdf_sha256']
    assert file_sha(PDF)==new['pdf_sha256']==EXPECTED
    old_pages={r['page']:r for r in old['rendered']}
    new_pages={r['page']:r for r in new['rendered']}
    covered=set(reviewed['actually_viewed_pages'])
    if reviewed.get('pixel_comparison'):
        chain_path=D/reviewed['pixel_comparison']
        assert file_sha(chain_path)==reviewed['pixel_comparison_sha256']
        chain=json.loads(chain_path.read_text())
        assert chain['pdf_sha256']==old['pdf_sha256']
        prior_chain_review=D/chain['prior_actual_visual_review']
        assert file_sha(prior_chain_review)==chain['prior_actual_visual_review_sha256']
        covered.update(r['page'] for r in chain['records'] if r['pixel_identical'])
    assert set(old_pages)<=covered
    OUT.mkdir(parents=True,exist_ok=True)
    extra=[]
    for p in sorted(set(old_pages)-set(new_pages)):
        prefix=OUT/f'page_{p:04d}_prior_selected'
        command=['pdftoppm','-f',str(p),'-l',str(p),'-r','110','-png','-singlefile',str(PDF),str(prefix)]
        proc=subprocess.run(command,capture_output=True,text=True)
        assert proc.returncode==0,(command,proc.stderr)
        new_pages[p]={'page':p,'file':str(prefix.with_suffix('.png').relative_to(D)),
                      'reasons':['Previously selected baseline page retained in final union coverage']}
        extra.append({'page':p,'command':command,'exit_code':proc.returncode,'stderr':proc.stderr})
    rows=[];changed=[]
    for p,row in sorted(new_pages.items()):
        current_path=D/row['file'];current=Image.open(current_path).convert('RGB')
        record={'page':p,'current_file':row['file'],'current_png_sha256':file_sha(current_path),
                'current_pixel_sha256':pixels_sha(current),'dimensions':list(current.size),
                'selection_reasons':row['reasons']}
        if p in old_pages:
            old_image_path=D/old_pages[p]['file'];previous=Image.open(old_image_path).convert('RGB')
            record.update({'previous_file':old_pages[p]['file'],'previous_png_sha256':file_sha(old_image_path),
                           'previous_pixel_sha256':pixels_sha(previous)})
            if current.size==previous.size:
                difference=ImageChops.difference(current,previous)
                bbox=difference.getbbox();identical=bbox is None
                record['difference_bounding_box']=list(bbox) if bbox else None
            else:
                identical=False;record['difference_bounding_box']=None
            record['pixel_identical']=identical
            record['status']='unchanged_pixels_prior_actual_review_applies' if identical else 'changed_needs_actual_visual_review'
            if identical:record['prior_actual_review']=str(review_path.relative_to(D))
        else:
            record.update({'pixel_identical':False,'status':'newly_selected_needs_actual_visual_review'})
        if not record['pixel_identical']:changed.append(record)
        rows.append(record)
    contacts=[]
    for start in range(0,len(changed),4):
        group=changed[start:start+4]
        canvas=Image.new('RGB',(1240,840*math.ceil(len(group)/2)),'white')
        for j,row in enumerate(group):
            im=Image.open(D/row['current_file']).convert('RGB');im.thumbnail((600,800))
            tile=Image.new('RGB',(620,840),'#d9dfe7');tile.paste(im,((620-im.width)//2,30))
            ImageDraw.Draw(tile).text((14,8),f"Paper III, final page {row['page']}",fill='black')
            canvas.paste(tile,((j%2)*620,(j//2)*840))
        file=OUT/f'changed_contact_{start//4+1:02d}.png';canvas.save(file)
        contacts.append({'file':str(file.relative_to(D)),'sha256':file_sha(file),
                         'pages':[r['page'] for r in group],
                         'actual_visual_inspection':'Not yet asserted; contact generation is not inspection.'})
    report={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date_utc':'2026-11-17',
            'scope':'Exact RGB pixel comparison of every final selected page and every selected page in the reviewed baseline, followed by contact generation only for changed/new pages.',
            'pdf_sha256':EXPECTED,'prior_pdf_sha256':old['pdf_sha256'],
            'prior_render_manifest_sha256':file_sha(old_path),'current_render_manifest_sha256':file_sha(new_path),
            'prior_actual_visual_review':str(review_path.relative_to(D)),
            'prior_actual_visual_review_sha256':file_sha(review_path),
            'current_manifest_selected_pages':len(new['rendered']),
            'union_selected_pages':len(rows),'unchanged_pages':sum(r['pixel_identical'] for r in rows),
            'changed_existing_pages':sum(r['status']=='changed_needs_actual_visual_review' for r in rows),
            'newly_selected_pages':sum(r['status']=='newly_selected_needs_actual_visual_review' for r in rows),
            'pages_requiring_new_visual_review':[r['page'] for r in changed],
            'extra_prior_selected_render_runs':extra,'records':rows,'contacts':contacts,
            'current_visual_review_status':'Pending actual image opening; no automated visual pass asserted.'}
    (OUT/'pixel_comparison.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:report[k] for k in ['current_manifest_selected_pages','union_selected_pages','unchanged_pages','changed_existing_pages','newly_selected_pages','pages_requiring_new_visual_review']}))
    print('contacts',len(contacts),'report',str(OUT/'pixel_comparison.json'))

if __name__=='__main__':main()
