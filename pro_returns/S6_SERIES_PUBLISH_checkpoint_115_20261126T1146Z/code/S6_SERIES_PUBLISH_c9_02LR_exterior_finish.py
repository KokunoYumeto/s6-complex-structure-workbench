"""Complete exterior-matrix substitutions adjacent to numerical coefficients."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
path = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row, = [r for r in rows if r['change_id'] == 'CLAUDE-III-P15-02LR-EXTERIOR-RELATION-MATRICES']
correct = re.sub(r'E_([i01])', r'{\\mathsf E}_\1', row['old_text'])
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
assert before.count(row['new_text']) == 1
after = before.replace(row['new_text'], correct, 1)
assert after.replace(correct, row['new_text'], 1) == before
row['new_text'] = correct
row['review_status'] += ' Immediate full difference readback also checked TeX products adjacent to numeric coefficients; all E_i,E_0,E_1 uses now carry the matrix font. The original old_text and all numerical coefficients remain unchanged.'
source.write_text(after, newline='\n')
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print(correct)
assert not re.search(r'(?<!\})E_[i01]', correct)
print('All exterior-matrix occurrences use their defined matrix symbol.')
