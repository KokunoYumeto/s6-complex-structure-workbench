#!/usr/bin/env python3
"""Prepare/apply the exact root-reviewed candidate19 -> candidate20 body batch.

Every guard, complete compared block and complete source must retain identical
inline mathematics, displayed mathematics and reference/citation/link sequences.
The input source/PDF/log/check hashes, full-image reading coverage, complete-block
archives, exact forward/inverse maps and existing log bytes are bound.
Preparation writes review artifacts only. Application requires the exact reviewed
manifest and preparation hashes and adds no mathematical check event.
"""
from pathlib import Path
import argparse
import collections
import csv
import datetime
import difflib
import hashlib
import io
import json
import os
import re

from S6_SERIES_PUBLISH_synctex_batch import Scanner

R = Path(__file__).resolve().parents[1]
O = R / 'agents/continuation_infra'
SOURCE = 'f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
PDF = 'e7a48c79d7bc5588f272b7d138f82fef8bbc504e86626f06a01c0bd86de32f7f'
LOG = '541ff9755885d8430a183befe6f9767509e7ab1ebc8aa0755d414cc842cd7030'
CHECKS = 'e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
EXISTING_ROWS = 2217
COVERAGE = 'records/S6_SERIES_PUBLISH_I_candidate19_complete_coverage_snapshot.json'
COVERAGE_SHA = 'c00de02dea2fbd759e61c88ed289adab670ffb62f6bf7eb06cf10c3e33534b93'

csv.field_size_limit(100_000_000)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def path(relative):
    p = (R / relative).resolve()
    assert p.is_relative_to(R) and p != R, ('path outside active tree', relative)
    return p


def read_exact(relative, expected=None):
    raw = path(relative).read_bytes()
    if expected is not None:
        assert sha(raw) == expected, ('file hash changed', relative)
    return raw


def math_segments(s):
    """Exact delimited segments, consuming TeX control symbols before delimiters."""
    inline, display = [], []
    i, n = 0, len(s)
    env_pattern = re.compile(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}')
    command_pattern = re.compile(r'\\[A-Za-z@]+')

    def closing(start, delimiter):
        j = start
        while j < n:
            if s.startswith(delimiter, j):
                return j + len(delimiter)
            if s[j] == '%':
                k = s.find('\n', j)
                j = n if k < 0 else k + 1
                continue
            if s[j] == '\\':
                j += 2
                continue
            j += 1
        raise AssertionError(('unclosed mathematical delimiter', delimiter, start))

    while i < n:
        if s[i] == '%':
            j = s.find('\n', i)
            i = n if j < 0 else j + 1
            continue
        if s[i] == '$':
            delimiter = '$$' if s.startswith('$$', i) else '$'
            end = closing(i + len(delimiter), delimiter)
            (display if delimiter == '$$' else inline).append(s[i:end])
            i = end
            continue
        if s[i] == '\\':
            if s.startswith('\\(', i) or s.startswith('\\[', i):
                is_display = s[i + 1] == '['
                end = closing(i + 2, '\\]' if is_display else '\\)')
                (display if is_display else inline).append(s[i:end])
                i = end
                continue
            m = env_pattern.match(s, i)
            if m:
                stop = '\\end{' + m[1] + '}'
                j = s.find(stop, i + len(m[0]))
                assert j >= 0
                end = j + len(stop)
                display.append(s[i:end])
                i = end
                continue
            m = command_pattern.match(s, i)
            if m:
                command = m[0]
                i += len(command)
                if command == '\\verb' and i < n:
                    if s[i] == '*':
                        i += 1
                    delimiter = s[i]
                    j = s.find(delimiter, i + 1)
                    assert j >= 0
                    i = j + 1
            else:
                i += 2
            continue
        i += 1
    return inline, display


def refs(s):
    """Exact reference/citation/link calls, including all balanced arguments."""
    names = 'eqref|ref|cref|Cref|cite|citet|citep|SeriesRef|SeriesRefText|CompendiumRef|ExternalPaperRef|hyperref|href'
    result = []
    for m in re.finditer(r'\\(?:' + names + r')(?![A-Za-z@])\*?', s):
        end = m.end()
        while True:
            j = end
            while j < len(s) and s[j].isspace():
                j += 1
            if j == len(s) or s[j] not in '[{':
                break
            close = ']' if s[j] == '[' else '}'
            opener = s[j]
            depth, k = 1, j + 1
            while k < len(s) and depth:
                if s[k] == '\\':
                    k += 2
                    continue
                if s[k] == opener:
                    depth += 1
                elif s[k] == close:
                    depth -= 1
                k += 1
            assert not depth, ('unclosed reference argument', s[m.start():j + 1])
            end = k
        result.append(s[m.start():end])
    return result


def validate_guard(g, before):
    gid = g['id']
    old, new = g.get('before', g.get('old')), g.get('after', g.get('new'))
    assert g['source_sha256'] == SOURCE
    assert isinstance(old, str) and old and isinstance(new, str)
    assert before.count(old) == 1, ('nonunique old literal', gid)
    assert math_segments(old) == math_segments(new), (gid, 'mathematical sequence changed')
    assert refs(old) == refs(new), (gid, 'reference sequence changed')
    return old, new


def archive(g):
    if 'full_block_archive' in g:
        a = g['full_block_archive']
        return a['original'], a['original_sha256'], a['proposed'], a['proposed_sha256']
    keys = ['original_full_block', 'original_full_block_sha256', 'proposed_full_block', 'proposed_full_block_sha256']
    assert all(k in g for k in keys), ('complete path-valued block archives required', g['id'])
    return tuple(g[k] for k in keys)


def stable_write(p, content):
    data = content.encode() if isinstance(content, str) else content
    if p.exists():
        assert p.read_bytes() == data, ('refusing changed artifact', str(p.relative_to(R)))
    else:
        p.write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', required=True)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--approved-inputs-sha')
    parser.add_argument('--approved-preparation-sha')
    args = parser.parse_args()
    manifest_raw = read_exact(args.inputs)
    manifest = json.loads(manifest_raw)
    assert manifest['source_sha256'] == SOURCE and manifest['root_approved'] is True
    assert manifest.get('pdf_sha256', PDF) == PDF
    assert manifest.get('candidate', 19) == 19 and manifest.get('paper', 'I') == 'I'
    if args.apply:
        assert args.approved_inputs_sha == sha(manifest_raw), 'Exact approved input hash required.'
        assert args.approved_preparation_sha, 'Exact reviewed preparation hash required.'

    source = R / 'S6_SERIES_PUBLISH_I.tex'
    log = R / 'S6_SERIES_PUBLISH_defects_I.tsv'
    source_bytes = read_exact('S6_SERIES_PUBLISH_I.tex', SOURCE)
    log_bytes = read_exact('S6_SERIES_PUBLISH_defects_I.tsv', LOG)
    before = source_bytes.decode()
    assert '\r' not in before and log_bytes.endswith(b'\r\n')
    reader = csv.DictReader(io.StringIO(log_bytes.decode()), delimiter='\t')
    fields, oldrows = reader.fieldnames, list(reader)
    assert len(oldrows) == EXISTING_ROWS
    pdf = R / 'build/I_candidate19/S6_SERIES_PUBLISH_I.pdf'
    read_exact(str(pdf.relative_to(R)), PDF)
    read_exact('CHECK_EVENTS.tsv', CHECKS)
    protected = {}

    def protect(p, expected=None):
        raw = read_exact(p, expected)
        digest = sha(raw)
        if p in protected:
            assert protected[p] == digest
        protected[p] = digest
        return raw

    protect(args.inputs, sha(manifest_raw))
    protect(str(pdf.relative_to(R)), PDF)
    cov = json.loads(protect(COVERAGE, COVERAGE_SHA))
    assert cov['source_sha256'] == SOURCE and cov['pdf_sha256'] == PDF
    assert cov['all_pages_read'] and cov['page_count'] == cov['covered_pages'] == 346
    assert not cov['missing_pages'] and len(cov['pages']) == 346
    render = json.loads(protect('render/I_candidate19/manifest.json', cov['render_manifest_sha256']))
    rendered = {p['page']: p for p in render['rendered_pages']}
    assert sorted(p['page'] for p in cov['pages']) == list(range(1, 347))
    for p in cov['pages']:
        im = rendered[p['page']]
        assert im['image_sha256'] == p['image_sha256']
        protect(im['image'], im['image_sha256'])
        protect(p['reading_record'], p['reading_record_sha256'])
    for relative in ['S6_SERIES_PUBLISH_report.md', 'PROGRESS_LEDGER.md', 'CHECK_EVENTS.tsv']:
        protect(relative)
    for folder, pattern in [
        ('records', '*candidate19*.json'),
        ('agents/i_cont_edits', '*candidate19_type*'),
        ('agents/i_cont_edits', '*candidate19*preparation*.json'),
        ('agents/i_cont_provenance', '*candidate19*review*.json'),
    ]:
        for p in sorted((R / folder).glob(pattern)):
            if p.is_file():
                protect(str(p.relative_to(R)))
    for item in manifest.get('review_evidence', []) + manifest.get('protected_records', []):
        protect(item['path'], item['sha256'])
    for key in ['complete_coverage', 'root_review']:
        if key in manifest:
            item = manifest[key]
            protect(item['path'], item['sha256'])

    changes, files, supplied, retained = [], [], {}, []
    for item in manifest['guard_files']:
        raw = protect(item['path'], item['sha256'])
        doc = json.loads(raw)
        guards = doc if isinstance(doc, list) else doc['guards']
        assert len(guards) == item['count']
        ids = []
        for g in guards:
            old, new = validate_guard(g, before)
            pos, arc = before.index(old), archive(g)
            pa, ha, pb, hb = arc
            x = protect(pa, ha).decode()
            y = protect(pb, hb).decode()
            assert before.count(x) == 1, ('archive not exact unique source block', g['id'])
            start = before.index(x)
            assert start <= pos and pos + len(old) <= start + len(x)
            supplied.setdefault(arc, []).append(g['id'])
            witnesses = g.get('retained_witnesses', [])
            for w in witnesses:
                if isinstance(w, str):
                    w = {'exact_text': w, 'sha256': sha(w.encode())}
                assert sha(w['exact_text'].encode()) == w['sha256']
                assert before.count(w['exact_text']) == 1
                retained.append({'guard_id': g['id'], **w})
            change = {
                'guard_id': g['id'], 'type': g['type'], 'statement_id': g['statement_id'],
                'old': old, 'new': new, 'reason': g['reason'],
                'old_source_line': before[:pos].count('\n') + 1,
                'candidate19_read_page': g.get('page'),
                'guard_file': item['path'], 'guard_file_sha256': item['sha256'],
                'original_offset': pos, 'block_start': start, 'block_end': start + len(x),
                'inline_math_segments_identical': True,
                'display_math_segments_identical': True,
                'reference_sequence_identical': True,
            }
            changes.append(change)
            ids.append(g['id'])
        files.append({**item, 'active_ids': ids})
    ids = {c['guard_id'] for c in changes}
    expected_count = manifest.get('approved_guard_count', manifest.get('total_guards'))
    assert isinstance(expected_count, int) and expected_count == sum(f['count'] for f in manifest['guard_files'])
    assert len(ids) == len(changes) == expected_count
    ordered = sorted(changes, key=lambda c: c['original_offset'])
    for x, y in zip(ordered, ordered[1:]):
        assert x['original_offset'] + len(x['old']) <= y['original_offset'], ('overlapping guards', x['guard_id'], y['guard_id'])

    after = before
    for c in changes:
        assert after.count(c['old']) == 1
        pos = after.index(c['old'])
        c['applied_offset'] = pos
        after = after[:pos] + c['new'] + after[pos + len(c['old']):]
    reverse = after
    for c in reversed(changes):
        pos = c['applied_offset']
        assert reverse[pos:pos + len(c['new'])] == c['new']
        reverse = reverse[:pos] + c['old'] + reverse[pos + len(c['new']):]
    assert reverse == before
    assert math_segments(after) == math_segments(before)
    assert refs(after) == refs(before)
    for w in retained:
        assert after.count(w['exact_text']) == 1, ('retained witness changed', w['guard_id'])

    sequence_counts = {}
    patterns = {
        'labels': r'\\label\{([^}]+)\}',
        'tag_targets': r'\\hypertarget\{(tag-[^}]+)\}',
        'all_targets': r'\\hypertarget\{([^}]+)\}',
        'bibliography_keys': r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}',
        'environment_sequence': r'\\(?:begin|end)\{[^}]+\}',
    }
    for name, pattern in patterns.items():
        a, b = re.findall(pattern, before), re.findall(pattern, after)
        assert a == b, name
        sequence_counts[name] = len(a)
    byid = {c['guard_id']: c for c in changes}
    verified = []
    for (pa, ha, pb, hb), group_ids in supplied.items():
        x, y = read_exact(pa, ha).decode(), read_exact(pb, hb).decode()
        t = x
        for gid in group_ids:
            c = byid[gid]
            assert t.count(c['old']) == 1
            t = t.replace(c['old'], c['new'], 1)
        assert t == y, ('supplied full-block map changed', pa, group_ids)
        verified.append({'original': pa, 'original_sha256': ha, 'proposed': pb, 'proposed_sha256': hb, 'guard_ids': group_ids, 'exact_replacement_verified': True})

    groups = []
    for c in sorted(changes, key=lambda c: (c['block_start'], c['block_end'])):
        if groups and c['block_start'] < groups[-1]['end']:
            groups[-1]['end'] = max(groups[-1]['end'], c['block_end'])
            groups[-1]['changes'].append(c)
        else:
            groups.append({'start': c['block_start'], 'end': c['block_end'], 'changes': [c]})
    archives, masked_before, masked_after = [], before, after
    for i, group in enumerate(groups, 1):
        x = before[group['start']:group['end']]
        y = x
        group_ids = {c['guard_id'] for c in group['changes']}
        gc = [c for c in changes if c['guard_id'] in group_ids]
        for c in gc:
            assert y.count(c['old']) == 1
            y = y.replace(c['old'], c['new'], 1)
        assert after.count(y) == 1
        assert math_segments(y) == math_segments(x)
        assert refs(y) == refs(x)
        stem = O / f'S6_SERIES_PUBLISH_I_candidate19_combined_block_{i:02}'
        pa, pb, pd = [Path(str(stem) + suffix) for suffix in ['_original.tex', '_proposed.tex', '.diff']]
        stable_write(pa, x)
        stable_write(pb, y)
        stable_write(pd, ''.join(difflib.unified_diff(x.splitlines(True), y.splitlines(True), fromfile='candidate19/' + gc[0]['statement_id'], tofile='candidate20-proposal/' + gc[0]['statement_id'])))
        archives.append({
            'statement_id': gc[0]['statement_id'], 'guard_ids': [c['guard_id'] for c in gc],
            'original': str(pa.relative_to(R)), 'original_sha256': sha(pa.read_bytes()),
            'proposed': str(pb.relative_to(R)), 'proposed_sha256': sha(pb.read_bytes()),
            'diff': str(pd.relative_to(R)), 'diff_sha256': sha(pd.read_bytes()),
            'all_display_mathematical_segments_identical': True,
            'all_inline_mathematical_segments_identical': True,
            'all_reference_sequences_identical': True,
        })
        marker = f'EXACT_CANDIDATE19_COMPARED_BLOCK_{i}'
        assert masked_before.count(x) == masked_after.count(y) == 1
        masked_before = masked_before.replace(x, marker, 1)
        masked_after = masked_after.replace(y, marker, 1)
    assert masked_before == masked_after

    with Scanner(pdf) as scan:
        for c in changes:
            line = c['old_source_line']
            pages = sorted({p for n in range(line, line + c['old'].count('\n') + 1) for p in scan.pages(source, n)})
            hint = c['candidate19_read_page']
            if hint is not None:
                assert not pages or hint in pages, ('page hint outside exact source mapping', c['guard_id'], hint, pages)
            c['candidate19_synctex_pages'] = pages
            c['candidate19_pages'] = pages or ([hint] if hint is not None else [])
            assert c['candidate19_pages'], c['guard_id']

    proposal = O / 'S6_SERIES_PUBLISH_I_candidate20_proposed_source.tex'
    stable_write(proposal, after)
    diff = O / 'S6_SERIES_PUBLISH_I_candidate19_combined.diff'
    stable_write(diff, ''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile='candidate19', tofile='candidate20-proposed')))
    receipt = {
        'paper': 'I', 'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'mode': 'applied' if args.apply else 'prepared only',
        'input_manifest': args.inputs, 'input_manifest_sha256': sha(manifest_raw),
        'before_source_sha256': SOURCE, 'candidate19_pdf_sha256': PDF,
        'before_defect_log_sha256': LOG, 'existing_defect_rows': EXISTING_ROWS,
        'proposed_source_sha256': sha(after.encode()), 'proposal': str(proposal.relative_to(R)),
        'guard_files': files, 'changes': changes, 'archives': archives,
        'supplied_complete_block_replacements_verified': verified,
        'exact_forward_and_inverse_source_maps_verified': True,
        'all_source_outside_compared_blocks_byte_identical': True,
        'all_display_mathematical_segments_identical': True,
        'all_inline_mathematical_segments_identical': True,
        'all_reference_sequences_identical': True,
        'retained_witnesses': retained,
        'all_label_target_environment_and_bibliography_key_sequences_preserved': True,
        'sequence_counts': sequence_counts,
        'check_ledger_sha256': CHECKS,
        'immutable_reading_dossier_and_status_records': protected,
        'proposed_defect_rows': len(changes),
        'new_defect_rows': len(changes) if args.apply else 0,
        'projected_total_defect_rows': EXISTING_ROWS + len(changes),
        'mathematical_events_added': 0, 'canonical_status_files_modified': False,
        'review_scope': manifest.get('review_scope', 'The root-approved input manifest and its exact complete-proof comparison record define the completed review scope. This helper checks the specified source transformations and adds no independent mathematical check.'),
        'root_review_binding': manifest.get('root_review'),
        'pending': ['Candidate20 clean build and complete changed-image reading after methodology count update', 'Final source/PDF/ledger metadata, mapped-log, provenance and individual type closure bindings'],
    }
    prep = O / 'S6_SERIES_PUBLISH_I_candidate19_combined_preparation.json'
    out = O / ('S6_SERIES_PUBLISH_I_candidate19_combined_apply_receipt.json' if args.apply else 'S6_SERIES_PUBLISH_I_candidate19_combined_preparation.json')
    assert not out.exists(), 'Refusing to overwrite an operation receipt.'
    if args.apply:
        preparation = json.loads(read_exact(str(prep.relative_to(R)), args.approved_preparation_sha))
        for key in ['input_manifest_sha256', 'before_source_sha256', 'candidate19_pdf_sha256', 'before_defect_log_sha256', 'proposed_source_sha256', 'guard_files', 'changes', 'archives', 'supplied_complete_block_replacements_verified']:
            assert preparation[key] == receipt[key], ('prepared operation no longer exact', key)
        # Root may add a new review receipt after preparation. Every record
        # already bound by preparation must retain its exact bytes; new records
        # are additionally protected during application.
        for p, h in preparation['immutable_reading_dossier_and_status_records'].items():
            assert protected.get(p) == h, ('prepared protected record changed', p)
        additions = []
        for index, c in enumerate(changes, EXISTING_ROWS + 1):
            pages = ','.join(map(str, c['candidate19_pages']))
            row = {f: '' for f in fields}
            row.update(
                change_id=f'I-{index:05d}', type=c['type'], statement_id=c['statement_id'],
                old_location=f"candidate19 source line {c['old_source_line']}; {c['statement_id']}", old_page=pages,
                new_location=c['statement_id'], new_page='pending candidate20 build',
                old_text=c['old'], new_text=c['new'], reason=c['reason'],
                review_status='applied; complete supplied and combined block comparisons verified; candidate20 changed-page reading pending',
                mapped_old_location=f"candidate19 {c['statement_id']}; pages {pages}",
                mapped_new_location='pending candidate20 build and changed-page reading',
                page_mapping_method=f'candidate19 source-bound libsynctex plus exact recorded guard context; source SHA {SOURCE}; PDF SHA {PDF}',
            )
            additions.append(row)
            c['change_id'] = row['change_id']
        buf = io.StringIO(newline='')
        writer = csv.DictWriter(buf, fieldnames=fields, delimiter='\t', lineterminator='\r\n')
        writer.writerows(additions)
        new_log = log_bytes + buf.getvalue().encode()
        parsed = list(csv.DictReader(io.StringIO(new_log.decode()), delimiter='\t'))
        assert parsed[:EXISTING_ROWS] == oldrows and parsed[EXISTING_ROWS:] == additions
        assert new_log[:len(log_bytes)] == log_bytes
        for p, h in protected.items():
            read_exact(p, h)
        assert source.read_bytes() == source_bytes and log.read_bytes() == log_bytes
        staged_source = O / 'S6_SERIES_PUBLISH_I_candidate20_source.commit'
        staged_log = O / 'S6_SERIES_PUBLISH_I_candidate20_defects.commit'
        stable_write(staged_source, after)
        stable_write(staged_log, new_log)
        # Each replacement is atomic; all input, inverse, archive and protection
        # checks have completed before the first canonical byte is replaced.
        os.replace(staged_source, source)
        os.replace(staged_log, log)
        assert source.read_bytes() == after.encode() and log.read_bytes() == new_log
        receipt.update(after_source_sha256=sha(source.read_bytes()), after_defect_log_sha256=sha(log.read_bytes()), total_defect_rows=len(parsed), existing_log_rows_preserved=EXISTING_ROWS, existing_log_bytes_preserved=len(log_bytes), approved_inputs_sha256=args.approved_inputs_sha, approved_preparation_sha256=args.approved_preparation_sha)
    else:
        assert source.read_bytes() == source_bytes and log.read_bytes() == log_bytes
    for p, h in protected.items():
        read_exact(p, h)
    assert sha((R / 'CHECK_EVENTS.tsv').read_bytes()) == CHECKS
    out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'mode': receipt['mode'], 'receipt': str(out.relative_to(R)), 'receipt_sha256': sha(out.read_bytes()), 'guards': len(changes), 'complete_blocks': len(archives), 'proposed_source_sha256': receipt['proposed_source_sha256'], 'after_source_sha256': receipt.get('after_source_sha256'), 'projected_total_rows': EXISTING_ROWS + len(changes), 'types': dict(collections.Counter(c['type'] for c in changes)), 'sequence_counts': sequence_counts, 'mathematical_events_added': 0}, indent=2))


if __name__ == '__main__':
    main()
