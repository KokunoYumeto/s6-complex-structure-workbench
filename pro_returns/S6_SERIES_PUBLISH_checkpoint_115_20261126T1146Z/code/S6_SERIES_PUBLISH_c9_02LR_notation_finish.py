"""Complete the three Smith-matrix bindings exposed by immediate readback."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
path = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
matches = [r for r in rows if r['change_id'] == 'CLAUDE-III-P15-02LR-SMITH-CHANGE-MATRICES']
assert len(matches) == 1
row = matches[0]
correct = row['old_text'].replace('U', r'{\mathsf U}').replace('V', r'{\mathsf V}')
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
assert before.count(row['new_text']) == 1
after = before.replace(row['new_text'], correct, 1)
assert after.replace(correct, row['new_text'], 1) == before
row['new_text'] = correct
row['review_status'] += ' Immediate readback found three incomplete font substitutions in the first applied block. The final block now carries both Smith matrices in every definition, product and inverse; finish program and actual output retain this correction. No new mathematical claim or check credit.'
source.write_text(after, newline='\n')
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print(correct)
print('The exact old/new defect row now contains the complete final substitution; original before-text retained.')
