from pathlib import Path
import datetime, hashlib, json, shutil

root = Path(__file__).resolve().parents[2]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
archive = root/'records/k65_audit_draft_preserved'
archive.mkdir(exist_ok=True)
files = [
    'notes/part3_os49_corrected_returns_working.md',
    'notes/part3_os49_corrected_returns.tex',
    'code/part3_fourfold/k65_standalone.pdf',
    'records/qa_k65.json', 'records/k65_standalone_visual_qa.json'
]
manifest = {}
for rel in files:
    p = root/rel
    dest = archive/p.name
    if not dest.exists():
        shutil.copy2(p, dest)
    manifest[rel] = hashlib.sha256(dest.read_bytes()).hexdigest()
for n in range(1,11):
    p=root/f'records/render_k65/page_{n:02d}.png'
    dest=archive/p.name
    if not dest.exists(): shutil.copy2(p,dest)
p=root/files[0]
s=p.read_text()
s=s.replace('Audit draft, 17 November 2026. This proof retains', '**Proved.** Root independently audited OR65.1--7 in full; blind_control\nindependently audited the actual shorter endpoint and all three seams.\nPromotion: 17 November 2026. This proof retains', 1)
p.write_text(s)
record={'utc':now,'statement':'P3K.65','status':'Proved',
        'parent_audit':'Full OR65.1--7 PASS, including positive reference page, signed native Cox flop, and shorter plus-sigma seams.',
        'peer_audit':'records/blind_audit_os49_corrected_shorter_return.json',
        'scope':'Two specified OS49 fans; actual r and w loops; negative integer remains unassigned.',
        'preserved_audit_draft_sha256':manifest}
(root/'records/k65_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
