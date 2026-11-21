#!/usr/bin/env python3
"""Add immutable raw-log diagnostics without modifying historical build summaries."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import re

R = Path(__file__).resolve().parents[1]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate', type=int)
    parser.add_argument('--expected-source-sha256', required=True)
    args = parser.parse_args()
    build = R / f'build/I_candidate{args.candidate}'
    source = R / f'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate{args.candidate}_source_for_mapping.tex'
    pdf, logp, summaryp = [build / p for p in ['S6_SERIES_PUBLISH_I.pdf', 'S6_SERIES_PUBLISH_I.log', 'build_summary.json']]
    summary = json.loads(summaryp.read_text())
    assert sha(source) == summary['source_sha256'] == args.expected_source_sha256
    assert sha(pdf) == summary['pdf_sha256']
    text = logp.read_text(errors='replace')
    assert 'Output written on ' in text and 'PDF statistics:' in text, 'Final log is incomplete.'
    underfull = []
    for m in re.finditer(r'(?m)^Underfull \\[hv]box[^\n]*', text):
        header = m[0]
        badness = re.search(r'badness (\d+)', header)
        lines = re.search(r'lines (\d+)--(\d+)', header)
        underfull.append({
            'header': header,
            'badness': int(badness[1]) if badness else None,
            'source_line_range': list(map(int, lines.groups())) if lines else None,
            'log_line': text[:m.start()].count('\n') + 1,
            'log_context': text[m.start():m.start() + 1000],
        })
    raw_overfull = re.findall(r'(?m)^Overfull \\[hv]box[^\n]*', text)
    record = {
        'paper': 'I', 'candidate': args.candidate,
        'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source_snapshot': str(source.relative_to(R)), 'source_sha256': sha(source),
        'pdf': str(pdf.relative_to(R)), 'pdf_sha256': sha(pdf),
        'log': str(logp.relative_to(R)), 'log_sha256': sha(logp),
        'historical_build_summary': str(summaryp.relative_to(R)), 'historical_build_summary_sha256': sha(summaryp),
        'underfull_total': len(underfull), 'underfull': underfull,
        'raw_overfull_total': len(raw_overfull), 'raw_overfull_headers': raw_overfull,
        'tex_error_headers': re.findall(r'(?m)^!.*', text),
        'historical_summary_counts': {k: summary[k] for k in ['overfull_total', 'overfull_above_2pt', 'undefined_references', 'undefined_citations', 'missing_characters', 'missing_fonts', 'multiply_defined', 'duplicate_destinations']},
        'scope': 'Direct final-log underfull/overfull/error diagnostics supplement the preserved historical build summary. A source-line range is not an assertion of a unique rendered page; actual full-page inspection supplies layout findings.',
        'mathematical_events_added': 0, 'page_reading_credit_added': 0,
        'historical_summary_modified': False,
    }
    out = R / f'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate{args.candidate}_build_diagnostics.json'
    assert not out.exists(), 'Refusing to overwrite a diagnostic receipt.'
    out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'path': str(out.relative_to(R)), 'sha256': sha(out), 'underfull_total': len(underfull), 'raw_overfull_total': len(raw_overfull), 'tex_errors': len(record['tex_error_headers']), **record['historical_summary_counts']}, indent=2))


if __name__ == '__main__':
    main()
