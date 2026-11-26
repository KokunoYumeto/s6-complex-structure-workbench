#!/usr/bin/env python3
"""Match every final rendered image to an actual, individually recorded reading.

An earlier reading transfers only when the entire PNG is byte-identical,
including the page number. A text comparison or a rendered manifest alone
never establishes a reading. Certification is an explicit final operation.
"""
from pathlib import Path
import argparse, collections, csv, datetime, hashlib, json, shutil

ROOT = Path(__file__).resolve().parents[1]

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def page_records(value):
    if isinstance(value, dict):
        if all(k in value for k in ('page', 'image_sha256', 'pdf_sha256')):
            yield value
        else:
            for item in value.values():
                yield from page_records(item)
    elif isinstance(value, list):
        for item in value:
            yield from page_records(item)

def clean(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('paper')
    ap.add_argument('--render', type=Path, required=True)
    ap.add_argument('--certify', action='store_true')
    ns = ap.parse_args()
    manifest_path = ns.render / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    pdf = Path(manifest['pdf'])
    assert digest(pdf) == manifest['pdf_sha256']
    source = ROOT / f'S6_SERIES_PUBLISH_{ns.paper}.tex'
    build = json.loads((pdf.parent / 'build_summary.json').read_text())
    assert build['source_sha256'] == digest(source)
    assert build['pdf_sha256'] == manifest['pdf_sha256']
    files = sorted(ROOT.glob(f'records/S6_SERIES_PUBLISH_{ns.paper}_final*reading*.json'))
    files += sorted(ROOT.glob(f'agents/**/S6_SERIES_PUBLISH_{ns.paper}_final*reading*.json'))
    readings = collections.defaultdict(list)
    for p in files:
        value = json.loads(p.read_text())
        for row in page_records(value):
            readings[row['image_sha256']].append({
                'record': str(p.relative_to(ROOT)), 'record_sha256': digest(p),
                'page_record': row})
    covered, missing = [], []
    for page in manifest['rendered_pages']:
        image = Path(page['image'])
        assert digest(image) == page['image_sha256']
        choices = readings.get(page['image_sha256'], [])
        if not choices:
            missing.append(page['page'])
            continue
        choices.sort(key=lambda x: (x['page_record']['pdf_sha256'] == manifest['pdf_sha256'], x['record']), reverse=True)
        item = choices[0]
        row = item['page_record']
        finding = next((row[k] for k in ('finding', 'content_and_findings', 'content_examined_and_findings', 'findings', 'notes') if k in row), 'Full page reading recorded in the source record.')
        covered.append({'page': page['page'], 'image_sha256': page['image_sha256'],
                        'reading_pdf_sha256': row['pdf_sha256'], 'reading_page': row['page'],
                        'reading_record': item['record'], 'reading_record_sha256': item['record_sha256'],
                        'method': 'read in this PDF' if row['pdf_sha256'] == manifest['pdf_sha256'] else 'entire rendered image byte-identical to an actually read earlier candidate',
                        'finding': finding})
    result = {'paper': ns.paper, 'source_sha256': digest(source), 'pdf_sha256': manifest['pdf_sha256'],
              'render_manifest_sha256': digest(manifest_path), 'page_count': manifest['pages'],
              'covered_pages': len(covered), 'missing_pages': missing, 'all_pages_read': not missing,
              'certified': ns.certify, 'pages': covered,
              'scope': 'Only complete rendered-image equality carries an earlier actual reading forward. Rendering alone supplies no reading evidence.'}
    (ROOT / 'records' / f'S6_SERIES_PUBLISH_{ns.paper}_page_coverage.json').write_text(json.dumps(result, indent=2) + '\n')
    if ns.certify:
        assert not missing, missing
        for key in ('overfull_above_2pt', 'undefined_references', 'undefined_citations', 'missing_characters', 'missing_fonts', 'multiply_defined', 'duplicate_destinations'):
            assert build.get(key,0) == 0, (key, build.get(key,0))
        destination = ROOT / f'S6_SERIES_PUBLISH_{ns.paper}.pdf'
        shutil.copyfile(pdf, destination)
        receipt = {k: v for k, v in result.items() if k != 'pages'}
        receipt.update(certified_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                       final_pdf=str(destination.relative_to(ROOT)),
                       reading_coverage_record=f'records/S6_SERIES_PUBLISH_{ns.paper}_page_coverage.json',
                       build_summary=str((pdf.parent / 'build_summary.json').relative_to(ROOT)))
        (ROOT / 'records' / f'S6_SERIES_PUBLISH_{ns.paper}_final_pdf_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
        lines = [f'# Paper {ns.paper}: final rendered-page reading', '',
                 f'Final PDF: {manifest["pages"]} pages. PDF SHA-256: `{manifest["pdf_sha256"]}`.', '',
                 f'Source SHA-256: `{digest(source)}`. Every final page image has an actual complete reading. A prior reading is carried forward only when its entire rendered PNG, including the page number, is byte-identical.', '',
                 'The earlier candidate reading records preserve each finding and its exact before/after repair. The final coverage record supplies per-page image hashes and hashes of the individual reading records. This visual review creates no mathematical check event.', '',
                 '| Final page | Reading evidence | Finding and disposition |',
                 '|---:|---|---|']
        for row in covered:
            evidence = f"{row['method']}; page {row['reading_page']} in {row['reading_record']}"
            lines.append(f"| {row['page']} | {clean(evidence)} | {clean(row['finding'])} |")
        (ROOT / f'S6_SERIES_PUBLISH_reading_{ns.paper}.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'pages'}))

if __name__ == '__main__':
    main()
