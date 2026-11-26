#!/usr/bin/env python3
"""Inspect the bounded 02 -> 05 -> 07 reading-history reconciliation.

The default reads existing reports/comparison outputs and prints coverage only.
An optional preview must be outside the checkpoint tree. Only an explicit
--apply writes the one canonical reading Markdown file, after exact baseline
and inverse guards. It adds no image, proof, computation, or check-event credit.
The final successor remains pending. No source, ledger, status, count, or PDF is written.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'S6_SERIES_PUBLISH_reading_III.md'
BASE_SHA = '28bdc2aaf3e1a48537a90fe81c1be110be7e3d13c712c02544e18fafd5973904'
OLD_STATUS = '''Status: all 696 physical pages of the converged current-kernel candidate02
were actually image-read on 26 November 2026, with the attributed page notes
retained below. Exact source repairs followed that reading. The final-PDF
gate remains open for the repaired build. The earlier pass08 retains only
its recorded 80-page partial scope; no reading credit is enlarged by this
consolidation.
'''
NEW_STATUS = '''Status: complete attributed page coverage is recorded for current-kernel
candidate02 (696 pages), candidate05 (699 pages), and candidate07 (701 pages).
Candidate02 was read in full. The later coverage joins actual changed-page
readings to exact full decoded-pixel equality at the same physical page,
preserving the original reader and PDF version of each transferred observation.
The final successor after candidate07 remains pending: no later image credit
or final-PDF closure is assigned here. The earlier pass08 retains its recorded
80-page partial scope. This reconciliation adds no reading or mathematical
checking event and does not close source, layout, provenance, or joint gates.
'''

VERSIONS = {
    '02': (696, '482f63f9871dd1da8f3065664f4a44cec2d1d8345b46119429541a44761aee01',
           '12ac7263a7720a8ec8910f588a4f753e60294036cb4a57ad1aa9e36c47694e65',
           'code/S6_SERIES_PUBLISH_c9_render_III_current_candidate02.out'),
    '05': (699, '90d14a1f46004223a1b3ac7bd520024ddb05e8051cacc30f054a3d6e06d5c2e6',
           '7769c410dbc30e0171a298400d54baf75481a4c358133564fac064b9da5598f4',
           'code/S6_SERIES_PUBLISH_c9_render_current_candidate05.out'),
    '07': (701, 'de3ac6c29a2794176a70a4abf0c40c4702ad27a08d2c13ea223f6b509ca98bca',
           '178fc512258907264ab80d01e426ca269b975a0ee5bf6b005bfb5aaaeee861c2',
           'code/S6_SERIES_PUBLISH_c9_render_current_candidate07.out'),
}
REPORTS = {
    ('02', 'global'): ('agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_current_pdf_pages_001_174.md', 'bold', '1-174'),
    ('02', 'named'): ('agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate02_pages175_348_review.md', 'table', '175-348'),
    ('02', 'backend'): ('agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_III_candidate02_pages349_522.md', 'physical', '349-522'),
    ('02', 'root'): ('agents/continuation9_root/S6_SERIES_PUBLISH_III_pages_523_696_reading.md', 'table', '523-696'),
    ('05', 'global'): ('agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate05_first_range_images.md', 'bold',
        '2-6, 11, 14-16, 20-21, 28-30, 32, 40, 42, 52, 55, 57, 71, 75-84, 86, 96, 111-112, 116, 121, 123-124, 126-129, 136-139, 141-143, 165-173, 224-299'),
    ('05', 'named'): ('agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate05_pages300_433_review.md', 'bold', '300-433'),
    ('05', 'backend'): ('agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_c9_candidate05_pages434_567_review.md', 'physical', '434-567'),
    ('05', 'root'): ('agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate05_final_reading.md', 'bold', '568-699'),
    ('07', 'global'): ('agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate07_first_range_images.md', 'bold', '3-5, 14, 245-280, 297-300, 366-379, 476-488'),
    ('07', 'named'): ('agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate07_pages489_559_review.md', 'bold', '489-559'),
    ('07', 'backend'): ('agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_c9_candidate07_pages560_630_review.md', 'physical', '560-630'),
    ('07', 'root'): ('agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate07_final_reading.md', 'table', '631-701'),
}
COMPARISONS = {
    ('02', '05'): ('code/S6_SERIES_PUBLISH_c9_compare_candidate02_candidate05.out',
        '1, 7-10, 12-13, 17-19, 22-27, 31, 33-39, 41, 43-51, 53-54, 56, 58-70, 72-74, 85, 87-95, 97-110, 113-115, 117-120, 122, 125, 130-135, 140, 144-164, 174-223',
        '2-6, 11, 14-16, 20-21, 28-30, 32, 40, 42, 52, 55, 57, 71, 75-84, 86, 96, 111-112, 116, 121, 123-124, 126-129, 136-139, 141-143, 165-173, 224-699'),
    ('05', '07'): ('code/S6_SERIES_PUBLISH_c9_compare_candidate05_candidate07.out',
        '1-2, 6-13, 15-244, 281-296, 301-365, 380-475',
        '3-5, 14, 245-280, 297-300, 366-379, 476-701'),
}
READER_NAMES = {'global': 'global reader (`/root/iii_global_sweep`)',
                'named': 'named reader (`/root/iii_reading_findings`)',
                'backend': 'backend reader (`/root/iii_defect_records`)',
                'root': 'root reader (`/root`)'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def expand(spec):
    result = []
    for part in spec.split(', '):
        ends = [int(x) for x in part.split('-')]
        assert len(ends) in (1, 2) and ends[0] <= ends[-1]
        result.extend(range(ends[0], ends[-1] + 1))
    assert result == sorted(set(result)), spec
    return result


def text(path):
    raw = (ROOT / path).read_bytes()
    assert b'\r' not in raw and raw.endswith(b'\n'), path
    return raw.decode('utf-8')


def actual_entries(report, form):
    if form == 'bold':
        pairs = re.findall(r'^- \*\*(\d+)(?:[–-](\d+))?[.:]?\*\*', report, re.M)
        return [n for a, b in pairs for n in range(int(a), int(b or a) + 1)]
    pattern = r'^\| (\d+) \|' if form == 'table' else r'^##(?:#)? Physical page (\d+)$'
    return [int(x) for x in re.findall(pattern, report, re.M)]


def link(label, path):
    return f'[{label}]({path})'


def verify_evidence(base):
    page_sets = {}
    for (version, reader), (path, form, spec) in REPORTS.items():
        report = text(path)
        actual = actual_entries(report, form)
        expected = expand(spec)
        assert actual == expected, (version, reader, len(actual), len(expected))
        if version == '02':
            assert path in base
        else:
            assert VERSIONS[version][1] in report and VERSIONS[version][2] in report, path
        page_sets[(version, reader)] = set(actual)
    extra = text(REPORTS[('05', 'global')][0])
    assert '- **44, additional verification.**' in extra
    assert 'page 44 was additionally viewed' in extra
    for version, (count, pdf, _, path) in VERSIONS.items():
        render = text(path)
        assert f'SHA256 {pdf} total physical pages {count}\n' in render, path
        assert f'Requested pages 1 {count} ' in render and ' dpi150\n' in render, path
        assert re.search(rf'^UTC complete .+ images {count}$', render, re.M), path
        chunks = re.findall(r'^Rendered (\d+) (\d+) exit (\d+)$', render, re.M)
        rendered = [n for a, b, code in chunks if code == '0' for n in range(int(a), int(b) + 1)]
        assert all(code == '0' for _, _, code in chunks), path
        assert sorted(rendered) == list(range(1, count + 1)), path
    transfers = {}
    for (prior, current), (path, same_spec, changed_spec) in COMPARISONS.items():
        same, changed = set(expand(same_spec)), set(expand(changed_spec))
        expected = f'''Prior images: {VERSIONS[prior][0]} Current images: {VERSIONS[current][0]}
Full decoded pixel equality at the same physical page: {len(same)}
UNCHANGED: {same_spec}
Current pages requiring actual new image reading: {len(changed)}
CHANGED: {changed_spec}
Prior physical pages beyond the current document: (none)
Every changed current page remains open for authored actual-image reading.
Identical pixels only preserve the exact prior image observation, with its original scope and attribution. No additional proof or reading credit is created.
'''
        assert text(path) == expected, path
        assert not same & changed
        assert same | changed == set(range(1, VERSIONS[current][0] + 1))
        observed = [p for (v, _), pages in page_sets.items() if v == current for p in pages]
        assert len(observed) == len(set(observed)) and set(observed) == changed
        transfers[current] = same
    origins = {p: ('02', reader) for (version, reader), pages in page_sets.items()
               if version == '02' for p in pages}
    assert sorted(origins) == list(range(1, 697))
    origin_counts = {}
    for version in ('05', '07'):
        inherited = {p: origins[p] for p in transfers[version]}
        origins = dict(inherited)
        for (v, reader), pages in page_sets.items():
            if v == version:
                for p in pages:
                    assert p not in origins
                    origins[p] = (v, reader)
        assert sorted(origins) == list(range(1, VERSIONS[version][0] + 1))
        origin_counts[version] = Counter(origins.values())
    assert origin_counts['05'] == Counter({('02', 'global'):115, ('02', 'named'):49,
        ('05', 'global'):135, ('05', 'named'):134, ('05', 'backend'):134, ('05', 'root'):132})
    assert origin_counts['07'] == Counter({('02', 'global'):115, ('02', 'named'):49,
        ('05', 'global'):92, ('05', 'named'):119, ('05', 'backend'):42,
        ('07', 'global'):71, ('07', 'named'):71, ('07', 'backend'):71, ('07', 'root'):71})
    return page_sets, origin_counts


def make_addendum(page_sets, origin_counts):
    out = ['\n\n## Candidate05 and candidate07: completed attributed coverage\n',
        'This historical reconciliation links the actual reports without replacing their observations. '
        'Their reader names, exposure descriptions, findings and then-pending repairs remain in those reports. '
        'Every later transfer below means equality of the complete decoded pixel array, dimensions and mode '
        'at the same physical page. The comparator uses no crop, rescaling, perceptual tolerance or extracted text. '
        'It preserves the original observation, PDF version and reader; it supplies no new image or proof reading.\n',
        'The existing pass08 and candidate02 history above is retained byte for byte. '
        'Candidate02 has actual coverage of pages 1–174 by the global reader, 175–348 by the named reader, '
        '349–522 by the backend reader and 523–696 by root.\n',
        '### Exact PDF and source versions\n',
        '| Current-kernel version | Physical pages | PDF SHA-256 | Input-source SHA-256 |\n|---|---:|---|---|']
    for version, (count, pdf, source, _) in VERSIONS.items():
        out.append(f'| candidate{version} | {count} | `{pdf}` | `{source}` |')
    out.append('\nThe actual renderer records are ' + ', '.join(
        link('candidate' + version, data[3]) for version, data in VERSIONS.items()) +
        '. Each records the corresponding complete 150 dpi image range and completed render. '
        'Rendering itself carries no image-reading credit.\n')
    for version, prior in [('05', '02'), ('07', '05')]:
        path, same_spec, changed_spec = COMPARISONS[(prior, version)]
        out += [f'### Candidate{version}: direct observations and exact transfers\n',
            f'The {link("actual candidate" + prior + " to candidate" + version + " comparison", path)} '
            f'contains {len(expand(same_spec))} unchanged physical pages and '
            f'{len(expand(changed_spec))} changed/new pages.\n',
            f'**Unchanged physical pages:** {same_spec}.\n',
            f'**Changed/new physical pages:** {changed_spec}.\n',
            '| Original reader of the fresh images | Actual changed-page allocation | Pages | Authored report |\n|---|---|---:|---|']
        for reader in ('global', 'named', 'backend', 'root'):
            report, _, spec = REPORTS[(version, reader)]
            out.append(f'| {READER_NAMES[reader]} | {spec} | {len(page_sets[(version, reader)])} | {link("candidate" + version + " observations", report)} |')
        if version == '05':
            out += ['\nThe global reader also actually viewed candidate05 page 44. Its exact-pixel '
                'transfer and original candidate02 attribution are retained, and the additional actual '
                'candidate05 observation is linked in the same report. It is not counted a second time '
                'in the 699-page coverage. The complete partition is 164 transfers plus 535 freshly read '
                'changed pages. The 299/300, 433/434 and 567/568 boundaries retain their respective '
                'readers and the continuity observations in those reports.\n']
        else:
            out += ['\nThe complete partition is 417 transfers plus 284 freshly read changed pages. '
                'Each of the four fresh allocations contains 71 pages. The 488/489 proof continuation, '
                '559/560 integral-specialization continuation and 630/631 definition/proposition transition '
                'retain the actual adjoining readers. Their complete-unit discussions remain in the '
                'linked reports; this summary assigns no other reader those direct-image scopes.\n',
                'Of the 417 transfers, 164 retain candidate02 observations through both exact comparisons '
                'and 253 retain fresh candidate05 observations. The original attribution is:\n',
                '| Original observation | Original reader | Transferred pages in candidate07 |\n|---|---|---:|']
            for (v, reader), count in sorted(origin_counts['07'].items()):
                if v != '07':
                    out.append(f'| candidate{v} | {READER_NAMES[reader]} | {count} |')
    out += ['\n### Findings and successor gate\n',
        'Completed page coverage does not erase the defects observed on those pages. The reports retain '
        'the actual heading/display/notation findings and their exact PDF versions. Later source admission '
        'and canonical defect status remain separate; neither a source repair nor this reconciliation '
        'pre-credits the repaired page image. The helper validates report-entry coverage and the recorded '
        'equality partitions, not the mathematics or page appearance afresh.\n',
        '### Final successor: pending\n',
        'No later candidate PDF identity, pixel-equality transfer or actual changed-page reading is admitted '
        'by this reconciliation. The diagnostic current08/legacy07 build pair adds no page coverage here. '
        'Its actual compiler findings remain in the '
        '[diagnostic log review](agents/continuation9_defect_records/S6_SERIES_PUBLISH_c9_current08_legacy07_build_logs_review.md). '
        'The next final join requires its completed exact source/PDF/build identity, '
        'the actual same-physical-page decoded-pixel comparison and attributed reading of every changed/new '
        'page, including adjoining unit boundaries. Final-PDF, D14/D23, provenance and joint-phase criteria '
        'remain with their canonical gates. This document adds no CHECK_EVENTS association or mathematical '
        'checking credit.\n']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', type=Path, help='Optional complete preview outside the checkpoint tree')
    parser.add_argument('--apply', action='store_true', help='Root-reviewed application to reading_III.md only')
    args = parser.parse_args()
    original = TARGET.read_bytes()
    assert sha(original) == BASE_SHA, 'Canonical reading history changed; inspect before revising this guard.'
    assert b'\r' not in original and original.endswith(b'\n')
    base = original.decode('utf-8')
    assert base.count(OLD_STATUS) == 1 and NEW_STATUS not in base
    page_sets, origin_counts = verify_evidence(base)
    addendum = make_addendum(page_sets, origin_counts)
    candidate = base.replace(OLD_STATUS, NEW_STATUS, 1) + addendum
    assert candidate.endswith(addendum) and candidate.count(NEW_STATUS) == 1
    reverse = candidate[:-len(addendum)].replace(NEW_STATUS, OLD_STATUS, 1)
    assert reverse.encode('utf-8') == original
    assert candidate.split('## Pass08:', 1)[1].startswith(base.split('## Pass08:', 1)[1])
    proposed = candidate.encode('utf-8')
    assert b'\r' not in proposed and proposed.endswith(b'\n')
    print('Canonical baseline SHA-256:', BASE_SHA)
    print('Proposed reading-history SHA-256:', sha(proposed))
    print('Exact inverse recovers every original byte; existing Pass08 and candidate02 body preserved.')
    for version in ('02', '05', '07'):
        counts = [(reader, len(page_sets[(version, reader)])) for reader in ('global', 'named', 'backend', 'root')]
        print('Actual report-entry coverage', version, counts)
    print('Candidate05: 164 exact transfers + 535 fresh changed pages = 699; page44 additionally viewed.')
    print('Candidate07: 417 exact transfers + 284 fresh changed pages = 701; four allocations of71.')
    print('Candidate07 transfer origins:', dict(sorted((key, count) for key, count in origin_counts['07'].items() if key[0] != '07')))
    print('No successor, independent-proof, new image or CHECK_EVENTS credit is created.')
    if args.preview:
        preview = args.preview.resolve()
        assert not preview.is_relative_to(ROOT), 'Preview must remain outside the checkpoint tree.'
        preview.parent.mkdir(parents=True, exist_ok=True)
        preview.write_bytes(proposed)
        print('Temporary external preview:', preview)
    if args.apply:
        assert TARGET.read_bytes() == original, 'Canonical reading file changed during inspection.'
        TARGET.write_bytes(proposed)
        assert TARGET.read_bytes() == proposed
        print('APPLIED: only S6_SERIES_PUBLISH_reading_III.md changed.')
    else:
        assert TARGET.read_bytes() == original
        print('INSPECT ONLY: canonical reading history and all other canonical files unchanged.')


if __name__ == '__main__':
    main()
