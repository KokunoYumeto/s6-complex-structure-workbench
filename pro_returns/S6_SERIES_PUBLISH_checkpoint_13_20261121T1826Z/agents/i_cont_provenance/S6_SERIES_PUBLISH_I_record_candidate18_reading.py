#!/usr/bin/env python3
"""Serialize completed manual full-PNG readings; never overwrite the final receipt."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SOURCE_SHA='3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
PDF_SHA='702aaa0abd1a4d8376e213ecaf03a0296592e22063f26db324d805502987e66e'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
notes_path=OUT/'S6_SERIES_PUBLISH_I_candidate18_completed_reading_notes.json'
notes=json.loads(notes_path.read_text())['pages']
expected=list(range(246,276))+[278,281,290]
assert [x['page'] for x in notes]==expected
assert sha(ROOT/'S6_SERIES_PUBLISH_I.tex')==SOURCE_SHA
assert sha(ROOT/'build/I_candidate18/S6_SERIES_PUBLISH_I.pdf')==PDF_SHA
manifest_path=ROOT/'render/I_candidate18/manifest.json'
manifest=json.loads(manifest_path.read_text())
assert manifest['pdf_sha256']==PDF_SHA and manifest['pages']==346
by={x['page']:x for x in manifest['rendered_pages']}
pages=[]
for note in notes:
    image=Path(by[note['page']]['image'])
    assert sha(image)==by[note['page']]['image_sha256']
    pages.append({**note,'image':str(image.relative_to(ROOT)),
                  'image_sha256':sha(image),'pdf_sha256':PDF_SHA,
                  'actual_full_page_image_read':True,
                  'pending_guards':'Separate complete-source review/guard record pending.' if note.get('pending_review') else ''})
record={
    'paper':'I','candidate':18,
    'reader':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation provenance agent',
    'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,
    'render_manifest_sha256':sha(manifest_path),'register':'S6_DEFECT_REGISTER.csv',
    'register_sha256':sha(ROOT/'S6_DEFECT_REGISTER.csv'),
    'register_types_read':[f'D{i:02d}' for i in range(1,26)],
    'pages':pages,'actual_full_page_images_read':len(pages),'pending_guards':[],
    'pending_guard_reviews':[{'page':n['page'],'review':n['pending_review']} for n in notes if n.get('pending_review')],
    'guard_file':None,
    'guard_status':'All assigned images read. Five wording/reference/spacing loci are identified for complete-source disposition in a separate guard record; no source change has been made by this reader.',
    'mathematical_events_added':0,'source_changes_applied':False,
    'manual_notes_sha256':sha(notes_path),
    'partial_receipt':'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_partial_candidate18_reading_provenance_001.json',
    'partial_receipt_sha256':sha(OUT/'S6_SERIES_PUBLISH_I_partial_candidate18_reading_provenance_001.json'),
    'scope':'Actual complete-image reading of each of pages246–275,278,281,290 against all25 register types. Each full PNG was individually emitted and read. No unassigned image receives new full-page reading credit. The page272 underfull spacing is visibly confirmed; proposed typography is a separate private preview. All historical candidate15–17 readings and the candidate18 partial receipt remain immutable. This receipt adds no mathematical proof-check event.'
}
path=OUT/'S6_SERIES_PUBLISH_I_final_candidate18_reading_provenance.json'
assert not path.exists(),'The completed reading receipt is immutable.'
path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
md=['# Paper I candidate18: completed provenance-agent page reading','',
    'Read all33 assigned complete PNGs:246–275,278,281,290. The image hashes are listed in the JSON receipt. This is page-reading evidence only; no mathematical check event was added.','',
    f'Source SHA-256: `{SOURCE_SHA}`','',f'PDF SHA-256: `{PDF_SHA}`','',
    f'Reading JSON SHA-256: `{sha(path)}`','',
    'Five loci require separate full-source disposition: the recaps on252/255/278, the convention locator on259, and visible paragraph spacing on272. This immutable receipt records what was seen before those reviews and must not be rewritten after repair.','']
for n in notes:
    md += [f"## Page {n['page']}",'',n['finding'],'']
path.with_suffix('.md').write_text('\n'.join(md))
print(json.dumps({'path':str(path.relative_to(ROOT)),'sha256':sha(path),'actual_full_page_images_read':len(pages),'pages':expected,'pending_review_pages':[x['page'] for x in record['pending_guard_reviews']]},indent=2))
