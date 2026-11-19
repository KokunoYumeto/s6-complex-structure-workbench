from pathlib import Path
import datetime, hashlib, json

root = Path(__file__).resolve().parents[2]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
qa_path = root / 'records/qa_k65.json'
qa = json.loads(qa_path.read_text())
qa['visual_review'] = 'PASS'
qa['visual_review_utc'] = now
qa['visual_reviewed_pages'] = list(range(1, 11))
qa['full_size_pages'] = [1, 5, 8, 9]
promoted = '**Proved.**' in (root/'notes/part3_os49_corrected_returns_working.md').read_text()
unchanged = []
for n in range(2,11):
    old=root/f'records/k65_audit_draft_preserved/page_{n:02d}.png'
    new=root/f'records/render_k65/page_{n:02d}.png'
    if old.exists() and old.read_bytes()==new.read_bytes(): unchanged.append(n)
if promoted: assert unchanged==list(range(2,11))
qa['visual_findings'] = [
    'All ten pages directly inspected in contact sheets; dense pages 5, 8 and 9 also inspected full size.',
    'No clipped text, colliding equations, malformed matrices or missing symbols observed.',
    'The final short certificate/scope paragraph occupies page 10; all mathematical argument ends on page 9.',
    ('The promoted Proved first page was directly re-inspected; pages 2 through 10 are byte-identical to the already visually reviewed draft.' if promoted else 'The statement remains labelled Audit draft pending the parent final mathematical promotion.')
]
qa_path.write_text(json.dumps(qa, indent=2) + '\n')
pdf = root / 'code/part3_fourfold/k65_standalone.pdf'
record = {
    'utc': now, 'statement': 'P3K.65', 'status': 'PASS',
    'reviewer': 'fourfold', 'page_count_reviewed': 10,
    'contact_sheets': {'1': [1,2,3,4], '2': [5,6,7,8], '3': [9,10]},
    'full_size_pages': [1,5,8,9], 'findings': qa['visual_findings'],
    'mathematical_status': 'Proved' if promoted else 'Audit draft',
    'unchanged_pages_after_promotion':unchanged,
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
}
(root/'records/k65_standalone_visual_qa.json').write_text(json.dumps(record, indent=2)+'\n')
with (root/'records/literature_fourfold.md').open('a') as f:
    f.write(f'\n## {now} — K65 standalone visual audit\n\n')
    f.write('Opened own records/render_k65/contact_1.png through contact_3.png and page_01.png, page_05.png, page_08.png, page_09.png. Reason: direct all-page layout verification of the corrected OS49 proof, followed by promoted first-page review and exact remaining-page comparison. Material taken: page bounds, equation and table rendering, full-unit endpoint seam table, and final scoped conclusion; no external mathematical claims. Result: PASS for all ten pages.\n')
print(json.dumps(record, indent=2))
