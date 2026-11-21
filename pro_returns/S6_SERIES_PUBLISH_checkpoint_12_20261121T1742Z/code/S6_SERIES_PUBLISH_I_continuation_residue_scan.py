#!/usr/bin/env python3
"""Repeat the bounded rendered-text residue search; hits require contextual review.

This saves the documented pattern procedure executed inline in the continuation.
The D11 replay also includes 'is not asserted'; its one additional occurrence
is explicitly reported against the original saved hit list, not silently merged.
It contributes neither an automatic defect classification nor page-reading or
mathematical-check credit. The first inline result is preserved separately.
"""
from pathlib import Path
import argparse
import collections
import hashlib
import json
import re
import fitz

PATTERNS = {
    'D01': r'\b(corrected|repaired|former|earlier|previously|superseded|retained|diagnostic|original|this run|our draft)\b',
    'D02': r'rather than|not merely|not just|without assuming|is not assumed|has not been assumed|silently|no unrecorded|no unspecified',
    'D04': r'\b(P1A?\.[0-9]|P3K|P3F|inv:|night:|maps:|push:|ari:|cdp:|compendium)',
    'D05': r'Lead [0-9]|the prompt|requested|asked for|as required by',
    'D07': r'worker|independently authored|S6_0|S6_1|SERIES_GRIND|night run|this run',
    'D08': r'\b(actual|retain\w*|supplied|specified|fresh|executed|saved|receipt|candidate|survivor|verified|probe)\b',
    'D09': r'\.py\b|\.json\b|code/|audit_|receipt|SHA-256|columns numbered|identities at their recorded scopes|--fresh',
    'D11': r'does not identify|is not asserted|does not assert|not a claim|no assertion|is not inferred|it is still',
    'D23': r'Kahler|Poincare|Item1|\+cdots',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--compare-inline', type=Path)
    args = parser.parse_args()
    rows = []
    with fitz.open(args.pdf) as doc:
        for number, page in enumerate(doc, 1):
            text = re.sub(r'\s+', ' ', page.get_text())
            for kind, pattern in PATTERNS.items():
                for match in re.finditer(pattern, text, re.I):
                    rows.append({'page': number, 'type': kind, 'hit': match[0],
                                 'context': text[max(0, match.start()-110):match.end()+180]})
    result = {'source': str(args.pdf.resolve()),
              'pdf_sha256': hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
              'scope': 'Pattern hits to inspect; no automatic defect classification or reading credit.',
              'patterns': PATTERNS, 'rows': rows,
              'counts': dict(collections.Counter(row['type'] for row in rows)),
              'mathematical_events_added': 0}
    if args.compare_inline:
        old = json.loads(args.compare_inline.read_text())['rows']
        key = lambda row: (row['page'], row['type'], row['hit'])
        result['inline_hit_multiset_identical'] = collections.Counter(map(key, old)) == collections.Counter(map(key, rows))
        result['inline_context_multiset_identical'] = collections.Counter(json.dumps(row, sort_keys=True) for row in old) == collections.Counter(json.dumps(row, sort_keys=True) for row in rows)
        result['inline_result_sha256'] = hashlib.sha256(args.compare_inline.read_bytes()).hexdigest()
        result['inline_counts'] = dict(collections.Counter(row['type'] for row in old))
        result['inline_only_hits'] = list((collections.Counter(map(key, old)) - collections.Counter(map(key, rows))).elements())
        result['replay_only_hits'] = list((collections.Counter(map(key, rows)) - collections.Counter(map(key, old))).elements())
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('patterns','rows')}, indent=2))


if __name__ == '__main__':
    main()
