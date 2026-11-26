#!/usr/bin/env python3
"""Prepare three observed fibre-name typography guards; never edit the source."""
import csv
import hashlib
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
PREFIX = ROOT / 'agents/continuation9_defect_records/S6_SERIES_PUBLISH_c9_candidate07_02S8_fibre_typography'
BASE_HASH = '178fc512258907264ab80d01e426ca269b975a0ee5bf6b005bfb5aaaeee861c2'
PDF_HASH = 'de3ac6c29a2794176a70a4abf0c40c4702ad27a08d2c13ea223f6b509ca98bca'
OWNER = 'night:P3F.31'
REVIEW = 'agents/continuation9_defect_records/S6_SERIES_PUBLISH_c9_candidate07_02S8_fibre_typography_review.md'


def main():
    raw = SOURCE.read_bytes()
    assert b'\r' not in raw
    assert hashlib.sha256(raw).hexdigest() == BASE_HASH
    source = raw.decode('utf-8')
    start = source.index(r'\begin{theorem}[Return of the positive-diagonal OS49 family]')
    stop = source.index(r'\end{proof}', start) + len(r'\end{proof}')
    scope = source[start:stop]
    assert r'\label{night:P3F.31}' in scope and r'\hypertarget{tag-02S8}' in scope
    with (ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').open(newline='') as f:
        progress = [r for r in csv.DictReader(f, delimiter='\t')
                    if (r['paper'], r['unit_id'], r['row_kind'], r['defect_type'])
                    == ('III', OWNER, 'defect', 'D23')]
    assert len(progress) == 1
    texts = [
        'positive nodes and separates the two I2 node values.\n',
        'At I2 the frames \\(V/Z,V/q\\) have geometric w-disc windings\n',
        'Its entries on each I2 pair agree, and both component values are zero.\n',
    ]
    contexts = [
        'The adjoining line says that the inverse deformations restore the same source fibres and line. The statement identifies both I_2 components and both nodes; the correction retains this identical fibre and the two node-deformation maps.',
        'The same two-component fibre has frames V/Z and V/q, geometric winding values -1,0 and raw coefficients 1,0. Their difference remains degree +1 on C_1 with raw chain Delta_even-Delta_odd. Every frame, value, orientation and map is unchanged.',
        'The displayed relative cochain a=-ell+sum e_even has the same entries per block, and reference-frame changes still add V^t lambda. The two entries and zero component values refer to the identical I_2 pair already specified; no cochain or pairing changes.',
    ]
    rows = []
    candidate = source
    for n, (old, context) in enumerate(zip(texts, contexts), 1):
        new = old.replace('I2', r'\(I_2\)')
        assert source.count(old) == scope.count(old) == 1
        assert source.count(new) == 0
        line = source.count('\n', 0, source.index(old)) + 1
        row = {
            'change_id': f'III-C9-CURRENT07-02S8-FIBRE-{n:02d}',
            'type': 'D23', 'statement_id': OWNER,
            'old_location': f'Theorem 19.6/tag 02S8 proof; frozen source line {line}',
            'old_page': '579',
            'new_location': f'Theorem 19.6/tag 02S8 proof; same full source line',
            'new_page': 'pending successor build and actual changed-page reading',
            'old_text': old, 'new_text': new,
            'reason': 'Actually read the complete current07 page 579 at 150 dpi: the fibre name is printed as baseline I2. Set the already identified type as I_2 in mathematical typography. ' + context + ' Full statement/proof source scope and actual containing D23 unit night:P3F.31 were checked. ' + REVIEW,
            'review_status': 'proposed; root admission and changed-page image gate pending',
        }
        rows.append(row)
        candidate = candidate.replace(old, new, 1)
    assert candidate.count(r'\(I_2\)') == source.count(r'\(I_2\)') + 3
    restored = candidate
    for row in reversed(rows):
        assert restored.count(row['new_text']) == 1
        restored = restored.replace(row['new_text'], row['old_text'], 1)
    assert restored == source
    for pattern in [r'\\(?:label|hypertarget)\{[^{}]*\}', r'\\(?:begin|end)\{[^{}]*\}']:
        assert re.findall(pattern, candidate) == re.findall(pattern, source)
    assert candidate.replace(r'\(I_2\)', 'I2').count('I2') == source.replace(r'\(I_2\)', 'I2').count('I2')
    data = {
        'source': SOURCE.name, 'source_sha256': BASE_HASH,
        'pdf_sha256': PDF_HASH, 'actual_image_page': 579,
        'scope_start_line': source.count('\n', 0, start) + 1,
        'scope_end_line': source.count('\n', 0, stop) + 1,
        'containing_progress_key': ['III', OWNER, 'defect', 'D23'],
        'observed_progress_status': progress[0]['status'],
        'rows': rows,
        'scope': 'Typography only; no events, mathematical counts, canonical source, or status writes.',
    }
    PREFIX.with_suffix('.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    PREFIX.with_suffix('.tsv').write_text(out.getvalue(), encoding='utf-8')
    print(json.dumps({
        'source_sha256': BASE_HASH, 'pdf_sha256': PDF_HASH,
        'rows': len(rows), 'scope_lines': [data['scope_start_line'], data['scope_end_line']],
        'actual_containing_D23_key': data['containing_progress_key'],
        'observed_status': progress[0]['status'],
        'full_source_reverse': 'pass', 'labels_targets_environments': 'unchanged',
        'change': 'three literal I2 spellings to the same I_2 type in math mode',
        'canonical_writes': 0, 'events': 0,
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
