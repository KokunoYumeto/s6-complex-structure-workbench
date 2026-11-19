"""Export explicit current IV readings. No status is inferred from extraction."""
from pathlib import Path
import csv
import hashlib
import json

B = Path(__file__).resolve().parents[1]
reviews = json.loads((B / 'analysis/IV_independent_reviews.json').read_text())
manifest = {r['label']: r for r in json.loads((B / 'analysis/IV_independent_manifest.json').read_text())}
fields = ['event_id', 'labels', 'who', 'date', 'type', 'verdict', 'scope', 'derivation',
          'independence', 'source_sha256', 'source_block_sha256', 'receiving_block_sha256', 'remaining_gates']
with (B / 'records/IV_independent_events.tsv').open('w') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    for i, r in enumerate(reviews, 1):
        src = manifest[r['label']]
        writer.writerow({
            'event_id': f'IV-INV-D-{i:03d}', 'labels': r['label'],
            'who': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)',
            'date': r['recorded_at'], 'type': r['type'], 'verdict': r['verdict'],
            'scope': r['scope'], 'derivation': r['derivation'],
            'independence': 'New derivation after reading the supplied proof; not a blind review and not an independent human check.',
            'source_sha256': hashlib.sha256(Path(src['original_source']).read_bytes()).hexdigest(),
            'source_block_sha256': src['source_block_sha256'],
            'receiving_block_sha256': src.get('receiving_block_sha256', ''),
            'remaining_gates': r.get('remaining_gates', '')
        })
print(json.dumps({'explicit_reviews': len(reviews), 'labels': [r['label'] for r in reviews]}))
