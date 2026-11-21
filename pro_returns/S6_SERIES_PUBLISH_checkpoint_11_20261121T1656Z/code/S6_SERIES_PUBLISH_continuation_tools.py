#!/usr/bin/env python3
"""Portable continuation snapshots and immutable timed checkpoints.

This program records evidence already present. It performs no mathematical
review, creates no check event, and supplies no page-reading credit by itself.
The original helpers and checkpoint records remain unchanged.
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent / 'S6_SERIES_PUBLISH_work'
RESTORE_RECEIPT = ROOT / 'records/S6_SERIES_PUBLISH_continuation_restore.json'
START = dt.datetime.fromisoformat(json.loads(RESTORE_RECEIPT.read_text())['continuation_started_utc'])
PAPERS = ['I', 'II', 'III', 'IV', 'V']
csv.field_size_limit(100_000_000)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def now():
    return dt.datetime.now(dt.timezone.utc)


def rel(path):
    p = Path(path).resolve()
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def current_snapshot(render_args=(), initial=False):
    previous = load(ROOT / 'records/S6_SERIES_PUBLISH_progress_review_05.json')
    ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
    rows = []
    defects = re.findall(r'^\| (I|II|III|IV|V) \| (D\d+): (.*?) \| (.*?) \|$', ledger, re.M)
    for paper, code, title, status in defects:
        rows.append(dict(id=f'defect:{paper}:{code}', kind='defect', paper=paper,
                         status='done' if status.startswith('done') else 'open',
                         detail=status, title=title))
    assert len(defects) >= 125, ('Missing defect rows', len(defects))
    renders = dict(x.split('=', 1) for x in render_args)
    page_sources = {}
    for paper in PAPERS:
        if paper in renders:
            manifest_path = Path(renders[paper])
            if not manifest_path.is_absolute():
                manifest_path = ROOT / manifest_path
            if manifest_path.is_dir():
                manifest_path /= 'manifest.json'
            manifest = load(manifest_path)
            pdf = Path(manifest['pdf'])
            assert sha(pdf) == manifest['pdf_sha256']
            coverage_path = ROOT / f'records/S6_SERIES_PUBLISH_{paper}_page_coverage.json'
            coverage = load(coverage_path) if coverage_path.exists() else {}
            if coverage.get('pdf_sha256') != manifest['pdf_sha256']:
                coverage = {}
            covered = {x['page']: x for x in coverage.get('pages', [])}
            page_sources[paper] = dict(pdf_sha256=manifest['pdf_sha256'],
                                      render_manifest=rel(manifest_path),
                                      render_manifest_sha256=sha(manifest_path))
            for page in manifest['rendered_pages']:
                number, image_sha = page['page'], page['image_sha256']
                assert sha(page['image']) == image_sha
                evidence = covered.get(number, {})
                done = evidence.get('image_sha256') == image_sha
                if done:
                    record = ROOT / evidence['reading_record']
                    assert sha(record) == evidence['reading_record_sha256']
                rows.append(dict(id=f'page:{paper}:{number}:{image_sha}', kind='page', paper=paper,
                                 page=number, image_sha256=image_sha, status='done' if done else 'open',
                                 evidence=evidence if done else None))
        elif paper in {'I', 'V'}:
            name = ('S6_SERIES_PUBLISH_I_candidate13_complete_coverage_snapshot.json'
                    if paper == 'I' and initial else f'S6_SERIES_PUBLISH_{paper}_page_coverage.json')
            path = ROOT / 'records' / name
            coverage = load(path)
            # This is the current archived candidate, not an assertion that a
            # subsequently edited canonical source has already been compiled.
            page_sources[paper] = dict(pdf_sha256=coverage['pdf_sha256'],
                                      source_sha256=coverage.get('source_sha256'),
                                      coverage_record=rel(path), coverage_record_sha256=sha(path),
                                      canonical_source_matches=coverage.get('source_sha256') == sha(ROOT / f'S6_SERIES_PUBLISH_{paper}.tex'))
            covered = {x['page']: x for x in coverage.get('pages', [])}
            for number in range(1, coverage['page_count'] + 1):
                evidence = covered.get(number, {})
                image_sha = evidence.get('image_sha256', 'unrecorded')
                done = bool(evidence)
                if done:
                    assert sha(ROOT / evidence['reading_record']) == evidence['reading_record_sha256']
                rows.append(dict(id=f'page:{paper}:{number}:{image_sha}', kind='page', paper=paper,
                                 page=number, image_sha256=image_sha, status='done' if done else 'open',
                                 evidence=evidence if done else None))
        else:
            rows.append(dict(id=f'page:{paper}:candidate_pending', kind='page', paper=paper,
                             status='open', detail='No publication candidate has reached page reading.'))

    completion = load(ROOT / 'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json')
    for label, event in completion['rows'].items():
        assert event['status'] == 'done'
        assert sha(ROOT / event['evidence_path']) == event['evidence_sha256'], label
    original_dispositions = []
    for item in previous['original_underchecked_row_dispositions']:
        item = dict(item)
        label = item['label']
        if label in completion['rows']:
            item['disposition'] = 'done: ' + completion['rows'][label]['scope']
        original_dispositions.append(item)
        if item['disposition'].startswith('done'):
            rows.append(dict(id=f'check:{label}', kind='required_check', paper=item['paper'],
                             status='done', detail=item['disposition']))
    with (ROOT / 'records/S6_SERIES_PUBLISH_required_check_candidates.csv').open() as f:
        candidates = list(csv.DictReader(f))
    known = {x['id'] for x in rows}
    for item in candidates:
        key = f'check:{item["label"]}'
        if key not in known:
            rows.append(dict(id=key, kind='required_check', paper=item['paper'],
                             status='open', detail=item))
            known.add(key)

    with (ROOT / 'S6_SERIES_PUBLISH_provenance_checks.tsv').open() as f:
        provenance = list(csv.DictReader(f, delimiter='\t'))
    for item in provenance:
        done = not item.get('remaining_gate', '').strip() and bool(item.get('resolution_status', '').strip())
        rows.append(dict(id='provenance:' + item['claim_id'], kind='provenance', paper=item['paper'],
                         status='done' if done else 'open', detail=item))
    for paper in PAPERS:
        if not any(x['paper'] == paper for x in provenance):
            rows.append(dict(id=f'provenance:{paper}:inventory_pending', kind='provenance',
                             paper=paper, status='open', detail='Claim inventory pending sequential work.'))
    counts = {}
    for paper in PAPERS:
        counts[paper] = {kind: dict(collections.Counter(x['status'] for x in rows
                                                       if x['paper'] == paper and x['kind'] == kind))
                         for kind in ('defect', 'page', 'required_check', 'provenance')}
    return dict(schema='continuation-0.3', recorded_utc=now().isoformat(),
                continuation_start_utc=START.isoformat(), rows=rows, row_counts=counts,
                page_sources=page_sources, original_underchecked_row_dispositions=original_dispositions,
                current_required_candidates=candidates,
                current_candidate_counts=dict(collections.Counter(x['paper'] for x in candidates)),
                canonical_source_sha256={p: sha(ROOT / f'S6_SERIES_PUBLISH_{p}.tex') for p in PAPERS},
                ledger_sha256=sha(ROOT / 'CHECK_EVENTS.tsv'),
                scope='Statuses record existing evidence. Every new rendered image is an open page until an actual reading record covers that exact image. No mathematical event is created.')


def snapshot(args):
    data = current_snapshot(args.render, args.initial)
    data['consecutive_reviews_without_movement'] = 0 if args.initial else None
    path = ROOT / args.output
    if path.exists():
        raise SystemExit('Refusing to overwrite an immutable snapshot: ' + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps(dict(path=str(path), sha256=sha(path), row_counts=data['row_counts'])))


def review(args):
    assert args.number >= 6
    due = START + dt.timedelta(hours=args.number - 5)
    assert now() >= due, 'Scheduled hourly review is not due.'
    before_path = (ROOT / 'records/S6_SERIES_PUBLISH_continuation_progress_baseline.json'
                   if args.number == 6 else ROOT / f'records/S6_SERIES_PUBLISH_progress_review_{args.number-1:02d}.json')
    before = load(before_path)
    data = current_snapshot(args.render)
    prior = {x['id']: x for x in before['rows']}
    newly_done = [x['id'] for x in data['rows'] if x['status'] == 'done'
                  and prior.get(x['id'], {}).get('status') != 'done']
    data.update(review=args.number, scheduled_utc=due.isoformat(), newly_done_rows=newly_done,
                movement_since_previous_review=bool(newly_done),
                consecutive_reviews_without_movement=0 if newly_done else before['consecutive_reviews_without_movement'] + 1,
                previous_snapshot=rel(before_path), previous_snapshot_sha256=sha(before_path))
    data['mandatory_stop'] = data['consecutive_reviews_without_movement'] >= 2
    path = ROOT / f'records/S6_SERIES_PUBLISH_progress_review_{args.number:02d}.json'
    assert not path.exists(), 'Refusing to overwrite an earlier review.'
    path.write_text(json.dumps(data, indent=2) + '\n')
    # Root owns canonical ledger/report and inserts this concrete review text.
    md = f'\n## Progress review {args.number:02d} — {data["recorded_utc"]}\n\n'
    md += f'{len(newly_done)} open rows reached their done state. Consecutive reviews without movement: {data["consecutive_reviews_without_movement"]}. '
    md += 'The page rows use complete rendered-image hashes; changed images reopen until actually read. Defect rows reflect their individual recorded dispositions.\n\n'
    md += f'Exhaustive snapshot: `{rel(path)}`.\n\n'
    md += '| Paper | Open defect types | Unread current pages | Required candidates | Open provenance rows |\n|---|---:|---:|---:|---:|\n'
    for p in PAPERS:
        c = data['row_counts'][p]
        md += f'| {p} | {c["defect"].get("open", 0)} | {c["page"].get("open", 0)} | {data["current_candidate_counts"].get(p, 0)} | {c["provenance"].get("open", 0)} |\n'
    if data['mandatory_stop']:
        md += '\nThe specified two-review stop rule is triggered. Package the exact incomplete state and stop.\n'
    text_path = ROOT / 'agents/continuation_infra' / f'S6_SERIES_PUBLISH_progress_review_{args.number:02d}_insert.md'
    text_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.write_text(md)
    print(json.dumps(dict(path=str(path), insert=str(text_path), newly_done=len(newly_done),
                          stalled=data['consecutive_reviews_without_movement'], mandatory_stop=data['mandatory_stop'])))


def checkpoint(args):
    assert args.number >= 11
    due = START + dt.timedelta(minutes=45 * (args.number - 10))
    assert now() >= due, 'Scheduled checkpoint time has not arrived.'
    inherited_manifest = ROOT / 'S6_SERIES_PUBLISH_checkpoint_10_filelist.tsv'
    with inherited_manifest.open() as f:
        inherited = {x['path'] for x in csv.DictReader(f, delimiter='\t')}
    inherited.add(inherited_manifest.name)
    missing = [name for name in inherited if not (ROOT / name).is_file()]
    assert not missing, ('A restored checkpoint10 file is missing', missing)
    out = ROOT.parent / 'deliverables'
    out.mkdir(exist_ok=True)
    dest = out / f'S6_SERIES_PUBLISH_checkpoint_{args.number:02d}.zip'
    assert not dest.exists(), 'Refusing to overwrite a checkpoint.'
    # Rendering manifests and extracted page text are evidence; only the page
    # bitmap files are excluded below. Runtime caches are reproducible inputs.
    exclude_dirs = {'vendor', 'tex-runtime', '__pycache__', '.git'}
    files = []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        name = path.relative_to(ROOT).as_posix()
        if name not in inherited:
            if any(x in exclude_dirs for x in path.relative_to(ROOT).parts):
                continue
            if path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.whl', '.pyc', '.fmt', '.synctex', '.gz'}:
                continue
            if re.fullmatch(r'S6_SERIES_PUBLISH_checkpoint_\d+(?:_part\d+)?\.zip', path.name):
                continue
            if path.suffix.lower() == '.pdf':
                receipt = ROOT / 'records' / f'{path.stem}_final_pdf_receipt.json'
                if path.parent != ROOT or not receipt.is_file():
                    continue
                record = load(receipt)
                if not record.get('all_pages_read') or record.get('pdf_sha256') != sha(path):
                    continue
        files.append((name, path.read_bytes()))
    names = {name for name, _ in files}
    assert inherited <= names
    manifest = [{'path':name, 'size':len(b), 'sha256':hashlib.sha256(b).hexdigest()} for name,b in files]
    buffer = io.StringIO()
    w = csv.DictWriter(buffer, fieldnames=['path','size','sha256'], delimiter='\t')
    w.writeheader(); w.writerows(manifest)
    pending = dest.with_suffix('.zip.pending')
    with zipfile.ZipFile(pending, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for name, b in files:
            archive.writestr(name, b)
        archive.writestr(f'S6_SERIES_PUBLISH_checkpoint_{args.number:02d}_filelist.tsv', buffer.getvalue())
    assert pending.stat().st_size < 500_000_000, 'Split packaging required; pending file retained.'
    with zipfile.ZipFile(pending) as archive:
        for row in manifest:
            b = archive.read(row['path'])
            assert len(b) == row['size'] and hashlib.sha256(b).hexdigest() == row['sha256']
    os.link(pending, dest)
    pending.unlink()
    print(json.dumps(dict(path=str(dest), files=len(files), restored_files_preserved=len(inherited),
                          size=dest.stat().st_size, sha256=sha(dest), created_utc=now().isoformat(), scheduled_utc=due.isoformat())))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    s = commands.add_parser('snapshot')
    s.add_argument('--output', default='records/S6_SERIES_PUBLISH_continuation_progress_baseline.json')
    s.add_argument('--initial', action='store_true')
    s.add_argument('--render', action='append', default=[], metavar='PAPER=MANIFEST_OR_DIR')
    s.set_defaults(func=snapshot)
    r = commands.add_parser('review')
    r.add_argument('number', type=int)
    r.add_argument('--render', action='append', default=[], metavar='PAPER=MANIFEST_OR_DIR')
    r.set_defaults(func=review)
    c = commands.add_parser('checkpoint')
    c.add_argument('number', type=int)
    c.set_defaults(func=checkpoint)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
