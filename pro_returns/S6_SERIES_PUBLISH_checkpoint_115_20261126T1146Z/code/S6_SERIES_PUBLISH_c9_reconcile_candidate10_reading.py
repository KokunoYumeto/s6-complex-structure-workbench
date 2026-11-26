"""Append attributed current10 coverage, preserving all earlier reading history."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]
BASE_SHA = 'c923399571e61b60e646721c5f292cb38de2892057e3ecf5df886ad8a16fe08e'
SOURCE_SHA = '5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187'
PDF_SHA = 'f284a0556c64684531f1d05b5370be02b111f8c9abee8c5ec7463bcf12ed2dc4'
spec = importlib.util.spec_from_file_location('history', ROOT / 'code/S6_SERIES_PUBLISH_c9_reconcile_III_reading.py')
history = importlib.util.module_from_spec(spec)
spec.loader.exec_module(history)
REPORTS = {
    'global': ('agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate10_first_range_images.md', r'^### Page (\d+)$', '3-5, 14, 252, 257-264, 361-436'),
    'named': ('agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate10_pages437_525_review.md', r'^\| (\d+) \|', '437-525'),
    'backend': ('agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_c9_candidate10_pages526_614_review.md', r'^### Physical page (\d+)$', '526-614'),
    'root': ('agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate10_final_reading.md', r'^\| (\d+) \|', '615-703'),
}
SAME = '1-2, 6-13, 15-251, 253-256, 265-360'
CHANGED = '3-5, 14, 252, 257-264, 361-703'
NEW_STATUS = '''Status: complete attributed page coverage is recorded for current-kernel
candidate02 (696 pages), candidate05 (699 pages), candidate07 (701 pages),
and candidate10 (703 pages). Candidate02 was read in full. Later coverage
joins actual changed-page readings to exact full decoded-pixel equality at
the same physical page, preserving the original reader and PDF version.
Candidate10 coverage consists of347 exact transfers and356 freshly read
changed pages. Its observed source and layout findings remain open for
their exact correction and successor verification. The earlier pass08
retains its recorded80-page partial scope. This reconciliation adds no
image or mathematical event and closes no source, layout, provenance or
joint gate. Final publication-PDF closure remains pending.
'''

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    target = ROOT / 'S6_SERIES_PUBLISH_reading_III.md'
    original = target.read_bytes()
    assert hashlib.sha256(original).hexdigest() == BASE_SHA
    assert digest(ROOT / 'S6_SERIES_PUBLISH_III.tex') == SOURCE_SHA
    assert digest(ROOT / 'agents/continuation9_build_III/current/S6_SERIES_PUBLISH_III.pdf') == PDF_SHA
    base = original.decode()
    assert base.count(history.NEW_STATUS) == 1 and NEW_STATUS not in base
    page_sets, _ = history.verify_evidence(base)
    origins = {p: ('02', reader) for (version, reader), pages in page_sets.items() if version == '02' for p in pages}
    for prior, current in [('02', '05'), ('05', '07')]:
        transferred = history.expand(history.COMPARISONS[(prior, current)][1])
        origins = {p: origins[p] for p in transferred}
        for (version, reader), pages in page_sets.items():
            if version == current:
                for p in pages:
                    assert p not in origins
                    origins[p] = (version, reader)
    same, changed = set(history.expand(SAME)), set(history.expand(CHANGED))
    assert len(same) == 347 and len(changed) == 356 and not same & changed
    assert same | changed == set(range(1, 704))
    comparison = history.text('code/S6_SERIES_PUBLISH_c9_compare_candidate07_candidate10.out')
    expected = f'''Prior images: 701 Current images: 703
Full decoded pixel equality at the same physical page: 347
UNCHANGED: {SAME}
Current pages requiring actual new image reading: 356
CHANGED: {CHANGED}
Prior physical pages beyond the current document: (none)
Every changed current page remains open for authored actual-image reading.
Identical pixels only preserve the exact prior image observation, with its original scope and attribution. No additional proof or reading credit is created.
'''
    assert comparison == expected
    inherited = Counter(origins[p] for p in same)
    actual = []
    for reader, (path, pattern, scope) in REPORTS.items():
        report = history.text(path)
        assert SOURCE_SHA in report and PDF_SHA in report
        entries = [int(x) for x in re.findall(pattern, report, re.M)]
        assert entries == history.expand(scope) and len(entries) == 89, reader
        actual.extend(entries)
    assert len(actual) == len(set(actual)) and set(actual) == changed
    render = history.text('code/S6_SERIES_PUBLISH_c9_render_III_current_candidate10.out')
    assert f'SHA256 {PDF_SHA} total physical pages 703\n' in render
    assert 'Requested pages 1 703 ' in render and ' dpi150\n' in render
    assert re.search(r'^UTC complete .+ images 703$', render, re.M)
    chunks = re.findall(r'^Rendered (\d+) (\d+) exit (\d+)$', render, re.M)
    assert all(code == '0' for _, _, code in chunks)
    assert sorted(n for a, b, _ in chunks for n in range(int(a), int(b)+1)) == list(range(1, 704))
    out = ['\n\n## Candidate10: completed attributed coverage\n',
        'This later record supersedes the earlier then-pending successor status without altering its historical text. '
        'Root read all402 lines of the global report, all120 lines of the named report, and all1137 lines of the backend report in visible contiguous outputs. '
        'Root authored the complete final-range observations after actually viewing each image. Discarded truncated attempts confer no reading credit.\n',
        f'The accepted current10 PDF has703 pages and SHA-256 `{PDF_SHA}`; its frozen source has SHA-256 `{SOURCE_SHA}`. '
        'The paired current10/legacy09 build was admitted at2026-11-26T09:35:34.563481+00:00. '
        'All actual image readings recorded here followed that admission. '
        'The complete150-dpi [render record](code/S6_SERIES_PUBLISH_c9_render_III_current_candidate10.out) supplies generation and identity evidence only.\n',
        'The complete [candidate07→candidate10 pixel comparison](code/S6_SERIES_PUBLISH_c9_compare_candidate07_candidate10.out) '
        'compares dimensions, mode and every decoded pixel at the same physical page, without a crop, resizing or tolerance.\n',
        f'**Exact transfers,347 pages:** {SAME}.\n', f'**Fresh changed pages,356 pages:** {CHANGED}.\n',
        '| Actual reader | Fresh physical pages | Count | Authored observations |\n|---|---|---:|---|']
    for reader, (path, _, scope) in REPORTS.items():
        out.append(f'| {history.READER_NAMES[reader]} | {scope} | 89 | [Full report]({path}) |')
    out += ['\nThe436/437,525/526 and614/615 joins were actually read on both sides by their attributed readers. '
        'Root also viewed614 as an extra boundary observation; it is not counted twice. '
        'Root read every Programs row on690–698 and every References entry on699–703. '
        'The complete-section discussions, exact displayed-map judgments and observed findings remain in the reports.\n',
        'The347 transferred pages retain the following original observation lineage through the recorded02→05→07 comparisons. '
        'These are attributions, not new readings.\n',
        '| Original PDF | Original reader | Transferred pages |\n|---|---|---:|']
    for (version, reader), count in sorted(inherited.items()):
        out.append(f'| candidate{version} | {history.READER_NAMES[reader]} | {count} |')
    out += ['\n### Observed findings and successor gate\n',
        'The complete image pass observed the02LJ isolated QED, three mathematical-typography issues, and selected-role questions in02LN,02LT,02LU,02LE,039U,038V,0370 and Q30X with their actual callers. '
        'The [root finding record](agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate10_new_source_findings.md) '
        'and the reader reports preserve their bounded evidence and pending whole-proof dispositions. '
        'Completed image coverage does not close those findings. '
        'Any admitted correction requires its accepted successor and the actual changed-image reading or exact unchanged-image transfer. '
        'No final publication-PDF, D14/D23, source, provenance, joint gate or CHECK_EVENTS association is closed or created by this historical join.\n']
    addendum = '\n'.join(out)
    candidate = base.replace(history.NEW_STATUS, NEW_STATUS, 1) + addendum
    assert candidate[:-len(addendum)].replace(NEW_STATUS, history.NEW_STATUS, 1).encode() == original
    assert b'\r' not in candidate.encode() and candidate.endswith('\n')
    print('Baseline', BASE_SHA)
    print('Proposed', hashlib.sha256(candidate.encode()).hexdigest())
    print('Source and accepted current10 PDF guards agree.')
    print('Coverage:347 exact transfers +356 fresh pages =703; four actual89-page allocations.')
    print('Original transfer attribution', dict(sorted(inherited.items())))
    print('Full historical bytes recovered by exact inverse; no new event or criterion closure.')
    if args.apply:
        assert target.read_bytes() == original
        target.write_text(candidate, newline='\n')
        assert target.read_bytes() == candidate.encode()
        print('APPLIED only S6_SERIES_PUBLISH_reading_III.md')
    else:
        print('INSPECT ONLY; no canonical file changed.')

if __name__ == '__main__':
    main()
