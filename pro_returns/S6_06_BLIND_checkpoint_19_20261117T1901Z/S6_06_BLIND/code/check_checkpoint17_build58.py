"""Verify that the final cap-exponent correction changes exactly its one page."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
import fitz
root=Path(__file__).resolve().parents[1]
archive=root/'records/checkpoint17_before_cap_exponent_typo_fix'
old=json.loads((archive/'page_word_geometry_before.json').read_text())
pdf=fitz.open(root/'S6_06_BLIND_paper.pdf')
assert len(pdf)==len(old)==650
changed=[];outside=[]
for i,page in enumerate(pdf):
    words=[list(w) for w in page.get_text('words')]
    if words!=old[i]['words']:changed.append(i+1)
    for w in words:
        if w[0]<-0.5 or w[1]<-0.5 or w[2]>page.rect.width+0.5 or w[3]>page.rect.height+0.5:
            outside.append({'page':i+1,'word':w[4],'bbox':w[:4]})
assert changed==[513],changed
assert not outside,outside
log=(root/'S6_06_BLIND_paper.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
assert not any(x>2 for x in over)
assert not re.search(r'undefined|Missing character|LaTeX Error|Fatal error|Label\(s\) may have changed',log)
dest=root/'records/render_checkpoint17/page_513_build58.png'
pdf[512].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(dest)
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PENDING_DIRECT_VISUAL_REVIEW',
        'master_build':58,'pages':650,'changed_text_or_word_geometry_pages':changed,
        'all_other_pages_text_and_geometry_identical_to_reviewed_build57':True,
        'overfull_above2pt':0,'max_overfull_pt':max(over,default=0),
        'out_of_page_words':outside,'new_page_image':str(dest.relative_to(root)),
        'pdf_bytes':(root/'S6_06_BLIND_paper.pdf').stat().st_size,
        'pdf_sha256':hashlib.sha256((root/'S6_06_BLIND_paper.pdf').read_bytes()).hexdigest()}
(root/'records/checkpoint17_build58_exact_change.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
