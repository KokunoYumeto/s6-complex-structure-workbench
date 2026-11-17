"""Initialize the delegated MAPS D source concordance without claiming unread checks."""
from pathlib import Path
import json, hashlib

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/invariants_arithmetic'
SRC = ROOT / 'sources/returns/S6_04_MAPS_MANIFOLDS'
DELEGATED = ROOT / 'deliverables/work/maps_audit/delegated_D_batch.json'
dest = OUT / 'maps_D_extracted'
dest.mkdir(parents=True, exist_ok=True)
rows = json.loads(DELEGATED.read_text())['rows']
oldp = OUT / 'maps_D_independent_audit.json'
old = {r['source_id']: r for r in json.loads(oldp.read_text())} if oldp.exists() else {}
records = []
for r in rows:
    ident = r['id']
    blocks = r['source_blocks']
    if ident in ('D.2.2', 'D.2.4'):
        lo, hi = (820, 853) if ident == 'D.2.2' else (889, 963)
        blocks = [dict(id=ident, file=str(SRC.relative_to(ROOT) / 'sections/manifolds.tex'),
                       start_line=lo, end_line=hi)]
    text = []
    blockinfo = []
    for block in blocks:
        path = ROOT / block['file']
        s = ''.join(path.read_text().splitlines(keepends=True)[block['start_line']-1:block['end_line']])
        text.append('% Source: '+block['file']+':'+str(block['start_line'])+'–'+str(block['end_line'])+'\n'+s)
        blockinfo.append({**block, 'sha256': hashlib.sha256(s.encode()).hexdigest()})
    target = dest / (ident.replace('.', '_')+'.tex')
    target.write_text('\n'.join(text))
    record = old.get(ident, {
        'source_run':'S6_04_MAPS_MANIFOLDS', 'source_id':ident,
        'source_title':r['statement'], 'source_status':r['status'],
        'printed_label':'maps:'+ident, 'paper':'III',
        'recorded_checks':[], 'source_inventory_record':r,
        'own_check':{'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
                     'effort':'Pro', 'date':'2026-11-17 UTC',
                     'proof_read':'not yet read in this audit', 'details':'', 'outcome':'pending'},
        'check_outcome':'pending independent reading', 'depends_on':r.get('depends_on',''),
        'reference_dependencies':[], 'program_runs':[], 'unresolved_claims':[],
        'editorial_changes':[],
    })
    record['source_blocks'] = blockinfo
    record['extracted_file'] = str(target.relative_to(ROOT / 'deliverables'))
    record['extracted_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    records.append(record)
oldp.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(f'Initialized {len(records)} rows and complete source-block copies; prior checks preserved.')
