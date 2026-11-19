"""Read the six actual standalone outputs and compare their resolved references.

This is a production audit. It confers no mathematical proof credit.
"""
from pathlib import Path
import hashlib
import json
import re
import sys
from datetime import datetime, timezone

import fitz

P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'code'))
from build_standalone import PREVIEWS, aux_records


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    snapshot = []
    canonical_aux = {
        p: aux_records(P / 'build/standalone' / p / f'S6_10_PAPERS_{p}.aux')
        for p in PREVIEWS
    }
    mismatches = []
    compared = 0
    for paper, source in PREVIEWS.items():
        folder = P / 'build/standalone' / paper
        record = json.loads((folder / 'assembly_record.json').read_text())
        assert record['source_sha256'] == sha(P / source / 'preview.tex'), (paper, 'stale preview')
        tex = P / f'S6_10_PAPERS_{paper}.tex'
        pdf = P / f'S6_10_PAPERS_{paper}.pdf'
        logpath = folder / f'S6_10_PAPERS_{paper}.log'
        log = logpath.read_text(errors='replace')
        assert sha(tex) == record['tex_sha256'] == sha(folder / tex.name)
        assert sha(pdf) == record['pdf_sha256'] == sha(folder / pdf.name)
        counts = {
            'overfull_hbox_above_2pt': sum(float(x) > 2 for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt', log)),
            'overfull_vbox_above_2pt': sum(float(x) > 2 for x in re.findall(r'Overfull \\vbox \(([0-9.]+)pt', log)),
            'missing_characters': log.count('Missing character:'),
            'font_warnings': len(re.findall(r'(?:LaTeX Font Warning|fontspec[^\n]*(?:Warning|Error)|Font shape[^\n]*undefined|font[^\n]*not loadable|Missing font)', log, re.I)),
            'undefined_reference_messages': len(re.findall(r'LaTeX Warning: Reference|There were undefined references', log)),
            'undefined_citation_messages': len(re.findall(r'Package natbib Warning: Citation|There were undefined citations', log)),
            'multiply_defined_labels': len(re.findall(r'multiply[- ]defined', log, re.I)),
            'label_rerun_messages': len(re.findall(r'Label\(s\) may have changed|Rerun to get cross-references right', log)),
            'fatal_errors': len(re.findall(r'^!|Fatal error occurred', log, re.M)),
        }
        for k, v in counts.items():
            assert v == 0, (paper, k, v)
        with fitz.open(pdf) as doc:
            pages = len(doc)
        for change in record['cross_reference_changes']:
            if 'label' not in change or not change.get('destination', '').startswith('Paper '):
                continue
            owner = change['destination'].split(' ', 1)[1]
            label = change['label']
            actual = canonical_aux[owner].get(label, {}).get('number')
            expected = change['number']
            if change.get('source_command') == 'eqref':
                actual = '(' + str(actual) + ')'
            compared += 1
            if actual != expected:
                mismatches.append({'calling_paper': paper, 'label': label, 'destination': owner,
                                   'resolved': expected, 'actual': actual})
        snapshot.append({
            'paper': paper, 'pages': pages,
            'tex_path': tex.name, 'tex_size_bytes': tex.stat().st_size, 'tex_sha256': sha(tex),
            'pdf_path': pdf.name, 'pdf_size_bytes': pdf.stat().st_size, 'pdf_sha256': sha(pdf),
            'source_sha256': record['source_sha256'],
            'log_path': str(logpath.relative_to(P)), 'log_sha256': sha(logpath), 'log': counts,
            'external_reference_change_count': len(record['cross_reference_changes']),
            'cited_key_count': len(record['citations']),
            'assembly_grants_no_check': True,
        })
    xref = {'recorded_at': datetime.now(timezone.utc).isoformat(),
            'scope': 'Compare every resolved cross-paper receiving reference with the actual final canonical AUX number; no proof credit.',
            'compared_reference_instances': compared, 'mismatches': mismatches}
    (P / 'analysis/final_cross_reference_audit.json').write_text(json.dumps(xref, indent=2) + '\n')
    assert not mismatches, mismatches
    (P / 'analysis/final_deliverable_snapshot.json').write_text(json.dumps(snapshot, indent=2) + '\n')
    print(json.dumps({'papers': [{'paper': r['paper'], 'pages': r['pages'], 'log': r['log']} for r in snapshot],
                      'total_pages': sum(r['pages'] for r in snapshot),
                      'cross_reference_instances_compared': compared, 'cross_reference_mismatches': 0}, indent=2))


if __name__ == '__main__':
    main()
