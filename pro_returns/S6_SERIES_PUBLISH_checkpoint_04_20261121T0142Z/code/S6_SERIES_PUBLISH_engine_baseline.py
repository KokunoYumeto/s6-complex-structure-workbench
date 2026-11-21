#!/usr/bin/env python3
"""Reproduce the received mathematical body with a portable pdfLaTeX preamble.

The received I–IV sources require LuaLaTeX's unavailable luaotfload runtime.
This transport changes only font/engine declarations before begin{document}.
It supplies a precisely identified baseline for page locations, without
claiming the pagination is the old LuaLaTeX pagination.
"""
from pathlib import Path
import argparse, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]

def portable(text):
    start = text.index('\\begin{document}')
    pre, body = text[:start], text[start:]
    changes = []
    for line in pre.splitlines(keepends=True):
        if line.startswith('\\pdfextension mapfile') or line.startswith('\\setmonofont'):
            changes.append((line, ''))
    changes.append(('\\usepackage{fontspec}\n\\setmainfont{Latin Modern Roman}',
                    '\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{lmodern}'))
    for old, new in changes:
        assert pre.count(old) == 1, repr(old)
        pre = pre.replace(old, new, 1)
    assert (pre + body)[len(pre):] == body
    return pre + body, changes

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('paper'); ns = ap.parse_args()
    p = ROOT.parent / 'source' / f'S6_SERIES_GRIND_{ns.paper}.tex'
    s = p.read_text(); result, changes = portable(s)
    dest = ROOT / 'baseline' / f'S6_SERIES_PUBLISH_{ns.paper}_engine_baseline.tex'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(result)
    digest = lambda b: hashlib.sha256(b).hexdigest()
    receipt = {'received_source_sha256': digest(p.read_bytes()),
               'baseline_source_sha256': digest(dest.read_bytes()),
               'document_body_sha256': digest(s[s.index('\\begin{document}'):].encode()),
               'body_byte_identical_after_utf8_decode': s[s.index('\\begin{document}'):] == result[result.index('\\begin{document}'):],
               'font_engine_changes': [{'old': a, 'new': b} for a,b in changes],
               'scope': 'Font/engine transport only; original LuaLaTeX page numbers remain in received tags/inventory. New baseline pages are identified as pdfLaTeX baseline pages.'}
    (ROOT / 'records' / f'S6_SERIES_PUBLISH_{ns.paper}_engine_baseline_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({'source':str(dest), **{k:v for k,v in receipt.items() if k!='font_engine_changes'}}))
