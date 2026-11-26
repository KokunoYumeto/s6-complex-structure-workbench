"""Small text-edit and ledger helpers for the third continuation.

The defects TSV is the edit record. CHECK_EVENTS is the check record.
No per-edit manifest, census, seal or derived-file copy is produced.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_II.tex'


def now():
    return datetime.now(timezone.utc).isoformat()


def read_tsv(path):
    with Path(path).open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)


def write_tsv(path, fields, rows):
    with Path(path).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def append_rows(path, rows, key):
    fields, prior = read_tsv(path)
    known = {r[key]: r for r in prior}
    additions = []
    for row in rows:
        row = {k: row.get(k, '') for k in fields}
        if row[key] in known:
            if known[row[key]] != row:
                raise ValueError(f'Conflicting existing {key}: {row[key]}')
            continue
        known[row[key]] = row
        additions.append(row)
    with Path(path).open('a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        writer.writerows(additions)
    return len(additions)


def identifiers(text):
    return Counter(re.findall(r'\\label\{([^}]+)\}', text)), Counter(re.findall(r'\\hypertarget\{(tag-[^}]+)\}', text))


def preserve_identifiers(before, after):
    for old, new in zip(identifiers(before), identifiers(after)):
        missing = old - new
        if missing:
            raise ValueError(f'Missing identifiers: {missing}')


def replace_fragment(start, end, fragment):
    text = SOURCE.read_text()
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError('Fragment boundary is not unique')
    left, right = text.index(start), text.index(end)
    if right <= left:
        raise ValueError('Reversed fragment boundaries')
    before = text[left:right]
    after = Path(fragment).read_text()
    preserve_identifiers(before, after)
    SOURCE.write_text(text[:left] + after + text[right:], newline='\n')
    return before, after


def apply_edit(old, new, change_id, types, statement_id, location, reason, review='Complete old and new context read by root.'):
    text = SOURCE.read_text()
    if text.count(old) != 1:
        raise ValueError(f'{change_id}: expected one source match, found {text.count(old)}')
    preserve_identifiers(old, new)
    SOURCE.write_text(text.replace(old, new, 1), newline='\n')
    rows = []
    for index, kind in enumerate(types, 1):
        rows.append({'change_id': f'{change_id}-{index:02}', 'type': kind,
            'statement_id': statement_id, 'old_location': location,
            'old_page': 'checkpoint 35 source; concordance at integrated build',
            'new_location': location, 'new_page': 'integrated build pending',
            'old_text': old, 'new_text': new, 'reason': reason, 'review_status': review})
    append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', rows, 'change_id')
    print(f'{change_id}: {len(rows)} defect rows')


def add_event(statement, event_id, kind, outcome, where, group='', source=''):
    stamp = now()
    row = {'statement_id': statement, 'date': stamp[:10],
        'who': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; effort setting not separately exposed; third-continuation root',
        'type': kind, 'outcome': outcome, 'event_id': event_id,
        'phase': 'publication text and proof comparison', 'source_file': source,
        'source_row': '', 'source_event_type': kind,
        'evidence_group': group or event_id, 'publish_input_file': '',
        'publish_input_row': '', 'date_utc': stamp, 'where': where}
    return append_rows(ROOT / 'CHECK_EVENTS.tsv', [row], 'event_id')


def set_unit_status(unit, row, status, detail, evidence):
    path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
    fields, rows = read_tsv(path)
    found = 0
    for item in rows:
        if item['paper'] == 'II' and item['unit_id'] == unit and (item['defect_type'] or item['row_kind']) == row:
            item.update(status=status, date_utc=now(), detail=detail, evidence=evidence)
            found += 1
    if found != 1:
        raise ValueError(f'Expected one progress row: {unit} {row}, found {found}')
    write_tsv(path, fields, rows)


def import_unit_status(path, units):
    _, incoming = read_tsv(path)
    for item in incoming:
        if item['unit'] in units:
            set_unit_status(item['unit'], item['row'], item['status'], item['basis'], item['fragment'])


def import_restructured_status(old_unit, fragment, status_file):
    path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
    fields, prior = read_tsv(path)
    old_units = {old_unit} if isinstance(old_unit, str) else set(old_unit)
    old_description = ', '.join(sorted(old_units))
    retained = [r for r in prior if not (r['paper'] == 'II' and r['unit_id'] in old_units)]
    _, incoming = read_tsv(status_file)
    text = Path(fragment).read_text()
    titles = {}
    for match in re.finditer(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}', text, re.M):
        titles[match.group(2)] = match.group(1)
    seen = {(r['paper'], r['unit_id'], r['defect_type'] or r['row_kind']) for r in retained}
    for item in incoming:
        criterion = item.get('row', item.get('criterion'))
        if criterion == 'restructuring':
            criterion = 'structure'
        unit = item['unit']
        key = ('II', unit, criterion)
        if key in seen:
            raise ValueError(f'Duplicate new unit row: {key}')
        seen.add(key)
        status = item['status']
        detail = item.get('basis', item.get('reason', ''))
        if criterion in ['D14', 'structure']:
            status = 'open'
            detail += ' Local ordering is reviewed; final whole-paper placement remains to be settled by root.'
        retained.append(dict(zip(fields, ['II', unit, titles.get(unit, unit),
            'structure' if criterion == 'structure' else 'defect',
            '' if criterion == 'structure' else criterion, status, now(),
            str(Path(fragment).relative_to(ROOT)), f'Replaces part of {old_description}. ' + detail])))
    write_tsv(path, fields, retained)
    print(f'{old_description}: current units replaced by {len(set(x["unit"] for x in incoming))} mathematical subsections; migration is not itself check or movement credit.')
