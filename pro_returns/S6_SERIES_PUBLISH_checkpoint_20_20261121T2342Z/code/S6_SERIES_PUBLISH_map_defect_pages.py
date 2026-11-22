#!/usr/bin/env python3
"""Locate logged edits in the corrected starting PDF and a specified current PDF.

Exact source matches are located with pdfLaTeX SyncTeX. Intermediate source
wording absent from the corrected starting source is identified as such; its
nearest retained statement/section locus is given where available. Absence
from the starting source does not assert absence from all intermediate PDFs.
Shared bibliography metadata is explicitly outside the paper's page sequence.
This program supplies locations, not page-reading or mathematical evidence.
"""
from pathlib import Path
import argparse, bisect, collections, concurrent.futures, csv, hashlib, importlib.util, json, re, subprocess

csv.field_size_limit(100_000_000)
ROOT = Path(__file__).resolve().parents[1]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def group(s, i):
    while i < len(s) and s[i].isspace():
        i += 1
    assert s[i] == '{'
    start, level = i + 1, 1
    i += 1
    while level:
        if s[i] == '{' and s[i - 1] != '\\':
            level += 1
        elif s[i] == '}' and s[i - 1] != '\\':
            level -= 1
        i += 1
    return s[start:i - 1], i


def read_aux(p):
    s, out = p.read_text(), {}
    for m in re.finditer(r'\\newlabel\{', s):
        label, j = group(s, m.end() - 1)
        value, j = group(s, j)
        if label.endswith('@cref'):
            continue
        number, j = group(value, 0)
        page, j = group(value, j)
        out[label] = {'number': number, 'page': page}
    return out


class Document:
    def __init__(self, source, build):
        self.source, self.build = source.resolve(), build.resolve()
        self.pdf = self.build / (self.source.stem + '.pdf')
        self.text = self.source.read_text()
        self.aux = read_aux(self.build / (self.source.stem + '.aux'))
        self.docstart = self.text.index('\\begin{document}')
        self.line_starts = [0] + [m.end() for m in re.finditer('\n', self.text)]
        self.sections = list(re.finditer(r'\\(?:sub)*section\*?\{([^}]+)\}', self.text))
        self.labels = {m[1]: m.start() for m in re.finditer(r'\\label\{([^}]+)\}', self.text)}
        self.cache_path = ROOT / 'records' / ('S6_SERIES_PUBLISH_synctex_cache_' + digest(self.pdf) + '.json')
        self.cache = ({int(k): v for k, v in json.loads(self.cache_path.read_text()).items()}
                      if self.cache_path.exists() else {})

    def line(self, pos):
        return bisect.bisect_right(self.line_starts, pos)

    def exact_spans(self, text):
        if not text:
            return []
        out, pos = [], 0
        while True:
            start = self.text.find(text, pos)
            if start < 0:
                return out
            out.append((start, start + len(text)))
            pos = start + max(1, len(text))

    def sync(self, line):
        result = subprocess.run(
            ['synctex', 'view', '-i', f'{line}:0:{self.source}', '-o', str(self.pdf)],
            check=True, capture_output=True, text=True)
        pages = sorted({int(x) for x in re.findall(r'^Page:(\d+)$', result.stdout, re.M)})
        return line, pages

    def prepare(self, requests):
        needed = sorted(set(requests) - set(self.cache))
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            for line, pages in pool.map(self.sync, needed):
                self.cache[line] = pages
        self.cache_path.write_text(json.dumps(self.cache, sort_keys=True) + '\n')

    def section(self, pos):
        previous = [m for m in self.sections if m.start() <= pos]
        return previous[-1][1] if previous else 'title, abstract or introduction'


def page_ranges(pages):
    values = sorted(set(int(p) for p in pages))
    groups = []
    for v in values:
        if groups and v == groups[-1][-1] + 1:
            groups[-1].append(v)
        else:
            groups.append([v])
    return ', '.join(str(g[0]) if len(g) == 1 else f'{g[0]}–{g[-1]}' for g in groups)


def identity_candidates(row):
    candidates = [row['statement_id']] + row['statement_id'].split(',')
    candidates += [x.split()[0] for x in row['statement_id'].split(',') if x.split()]
    for field in ('old_text', 'new_text'):
        candidates += re.findall(r'\\StatementRecord\{([^}]+)\}', row[field])
        candidates += re.findall(r'\\label\{([^}]+)\}', row[field])
    candidates += re.findall(r'\\(?:c|C)?ref\{([^}]+)\}', row['new_location'])
    return list(dict.fromkeys(candidates))


def fallback(doc, row):
    identity = row['statement_id']
    if identity == 'methodology':
        pos = doc.text.find('\\subsection{Methodology}')
        if pos >= 0:
            return {'method': 'named section locus', 'lines': [doc.line(pos)],
                    'location': 'Section1.5, Methodology', 'exact': False}
    if identity.startswith('bibliography:'):
        key = identity.split(':', 1)[1]
        m = re.search(r'\\bibitem(?:\[[^\]]*\])?\{' + re.escape(key) + r'\}', doc.text)
        if m:
            return {'method': 'retained bibliography entry locus', 'lines': [doc.line(m.start())],
                    'location': 'Bibliography entry ' + key, 'exact': False}
        return {'method': 'removed uncited bibliography entry', 'pages': [],
                'location': 'Bibliography entry ' + key + '; retained in shared bibliography records', 'exact': False}
    for label in identity_candidates(row):
        if label in doc.aux:
            r = doc.aux[label]
            return {'method': 'retained label locus', 'pages': [r['page']],
                    'location': f"{label}, number {r['number']}", 'exact': False}
    # Long unchanged lines are useful only when uniquely present. They locate a
    # related passage; the record explicitly calls this a fragment locus.
    fragments = sorted({x.strip().rstrip('.;:,') for k in ('old_text', 'new_text')
                        for x in row[k].splitlines() if len(x.strip()) >= 50}, key=len, reverse=True)
    for fragment in fragments:
        if doc.text.count(fragment) == 1:
            pos = doc.text.index(fragment)
            if pos >= doc.docstart:
                return {'method': 'unique unchanged fragment locus', 'lines': [doc.line(pos)],
                        'location': doc.section(pos), 'exact': False}
    return {'method': 'source-only change', 'pages': [],
            'location': row.get('new_location') or row.get('statement_id') or 'nonprinted source metadata',
            'exact': False}


def plan(doc, row, side):
    if 'shared bibliography' in row['old_location']:
        return {'method': 'shared bibliography metadata', 'pages': [],
                'location': row['old_location'], 'exact': False}
    text = row[side + '_text']
    if (row['statement_id'] == 'preamble' or
            row['old_text'].lstrip().startswith('\\expandafter\\def\\csname SBack@')):
        return {'method': 'nonprinting preamble source', 'pages': [],
                'location': 'preamble metadata; removed or updated without a printed page', 'exact': True}
    spans = doc.exact_spans(text)
    if spans:
        visible = [(a, b) for a, b in spans if a >= doc.docstart]
        if not visible:
            return {'method': 'nonprinting preamble source', 'pages': [],
                    'location': 'preamble; no paper page', 'exact': True}
        lines = sorted({doc.line(a) for a, b in visible} |
                       {doc.line(max(a, b - 1)) for a, b in visible})
        return {'method': 'exact source match and SyncTeX', 'lines': lines,
                'spans': [[doc.line(a), doc.line(max(a, b - 1))] for a, b in visible],
                'location': '; '.join(dict.fromkeys(doc.section(a) for a, b in visible)),
                'occurrences': len(visible), 'exact': True}
    return fallback(doc, row)


def materialize(doc, item):
    if item.get('reused_from_unchanged_baseline_receipt'):
        return item
    if 'lines' in item:
        item['pages'] = sorted({p for line in item['lines'] for p in doc.cache[line]})
        # A contiguous exact source span traverses its intervening rendered pages.
        for a, b in item.get('spans', []):
            pa, pb = doc.cache.get(a, []), doc.cache.get(b, [])
            if pa and pb and b > a:
                item['pages'] = sorted(set(item['pages']) | set(range(min(pa), max(pb) + 1)))
    return item


def description(item, side, row):
    if item['method'] in ('shared bibliography metadata', 'nonprinting preamble source'):
        return 'not a printed paper page (' + item['method'] + ')'
    if item['method'] == 'removed uncited bibliography entry':
        return 'removed uncited bibliography entry; no current printed page'
    pages = page_ranges(item.get('pages', []))
    if not pages:
        if side == 'old' and row['old_location'] == 'intermediate revision':
            return 'intermediate revision; no exact locus in the corrected starting PDF'
        return 'source-only change; no printed-page locus established'
    result = 'p. ' + pages
    if not item['exact']:
        if side == 'old' and row['old_location'] == 'intermediate revision':
            result = 'intermediate source text; corrected-start locus ' + result
        elif side == 'new' and not row['new_text']:
            result = 'deleted duplicate; retained result at ' + result
        else:
            result += ' (' + item['method'] + ')'
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('paper')
    p.add_argument('--baseline-source', type=Path, required=True)
    p.add_argument('--baseline-build', type=Path, required=True)
    p.add_argument('--baseline-page-receipt', type=Path)
    p.add_argument('--baseline-page-helper', type=Path)
    p.add_argument('--baseline-pdf', type=Path)
    p.add_argument('--current-build', type=Path, required=True)
    p.add_argument('--certified', action='store_true')
    a = p.parse_args()
    old = None
    new = Document(ROOT / f'S6_SERIES_PUBLISH_{a.paper}.tex', a.current_build)
    build = json.loads((new.build / 'build_summary.json').read_text())
    assert build['source_sha256'] == digest(new.source), 'Current build does not match source'
    path = ROOT / f'S6_SERIES_PUBLISH_defects_{a.paper}.tsv'
    with path.open() as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    if a.baseline_page_receipt:
        assert a.baseline_page_helper and a.baseline_pdf
        spec = importlib.util.spec_from_file_location('baseline_page_helper', a.baseline_page_helper)
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        reusable = helper.load_old_side(a.baseline_page_receipt, a.baseline_pdf, a.baseline_source, rows)
        assert len(reusable) == len(rows), 'Regenerate baseline receipt for missing or changed old rows'
        baseline_source_sha = digest(a.baseline_source)
        baseline_pdf_sha = digest(a.baseline_pdf)
    else:
        old = Document(a.baseline_source, a.baseline_build)
        baseline_source_sha, baseline_pdf_sha = digest(old.source), digest(old.pdf)
    target = ROOT / 'records' / f'S6_SERIES_PUBLISH_{a.paper}_defect_page_mapping.json'
    prior = json.loads(target.read_text()) if target.exists() else {}
    if old is not None:
        reusable = ({r['change_id']: r['old'] for r in prior['details']}
                    if prior.get('baseline_pdf_sha256') == baseline_pdf_sha and
                       prior.get('baseline_source_sha256') == baseline_source_sha else {})
    plans = []
    for r in rows:
        x = reusable.get(r['change_id'])
        if x and (old is None or x['method'] != 'source-only change'):
            x = dict(x, reused_from_unchanged_baseline_receipt=True)
        else:
            x = plan(old, r, 'old')
        plans.append((r, x, plan(new, r, 'new')))
    if old is not None:
        old.prepare(line for _, x, _ in plans if not x.get('reused_from_unchanged_baseline_receipt') for line in x.get('lines', []))
    new.prepare(line for _, _, x in plans for line in x.get('lines', []))
    details = []
    for r, x, y in plans:
        x, y = materialize(old, x), materialize(new, y)
        r['old_page'], r['new_page'] = description(x, 'old', r), description(y, 'new', r)
        r['mapped_old_location'], r['mapped_new_location'] = x['location'], y['location']
        r['page_mapping_method'] = x['method'] + ' -> ' + y['method']
        r['review_status'] = ('applied; final PDF page-reading receipt verified' if a.certified else
                              'applied; source locations mapped; final PDF gate pending')
        details.append({'change_id': r['change_id'], 'old': x, 'new': y})
    fields = list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    receipt = {'paper': a.paper, 'baseline_source_sha256': baseline_source_sha,
               'baseline_pdf_sha256': baseline_pdf_sha, 'current_source_sha256': digest(new.source),
               'current_pdf_sha256': digest(new.pdf), 'rows': len(rows),
               'current_mapping_methods': dict(collections.Counter(y['method'] for _, _, y in plans)),
               'historical_mapping_methods': dict(collections.Counter(x['method'] for _, x, _ in plans)),
               'certified': a.certified, 'details': details,
               'scope': 'Locations only. An intermediate revision without a corrected-start locus is identified explicitly; no assertion is made about whether it occurred in another intermediate PDF. Candidate reading records retain their own page-specific findings.'}
    if a.baseline_page_receipt:
        receipt['baseline_page_receipt'] = str(a.baseline_page_receipt)
        receipt['baseline_page_receipt_sha256'] = digest(a.baseline_page_receipt)
        receipt['baseline_page_helper_sha256'] = digest(a.baseline_page_helper)
    target.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'details'}))


if __name__ == '__main__':
    main()
