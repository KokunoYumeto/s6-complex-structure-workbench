"""Export explicitly recorded independent II reviews; never infer a verdict."""
from pathlib import Path
import csv, hashlib, json

B = Path(__file__).resolve().parents[1]
reviews = json.loads((B/'analysis/II_independent_reviews.json').read_text())
manifest = {r['label']:r for r in json.loads((B/'analysis/II_independent_source_manifest.json').read_text())}
fields = ['event_id','labels','who','date','type','verdict','scope','derivation','independence','source_sha256','remaining_gates']
with (B/'records/II_independent_events.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
    for i,r in enumerate(reviews,1):
        src=manifest[r['label']]
        row={'event_id':f'II-INV-D-{i:03d}','labels':r['label'],
             'who':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)',
             'date':r['recorded_at'],'type':'full source-proof reading and independent mathematical rederivation',
             'verdict':r['verdict'],'scope':r['scope'],'derivation':r['derivation'],
             'independence':'New derivation after reading the supplied proof; not a blind review and not an independent human check.',
             'source_sha256':hashlib.sha256(Path(src['file']).read_bytes()).hexdigest(),
             'remaining_gates':r.get('remaining_gates','')}
        w.writerow(row)
print(json.dumps({'explicit_reviews':len(reviews),'labels':[r['label'] for r in reviews]}))
