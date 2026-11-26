#!/usr/bin/env python3
"""Scheduled lean snapshots relative to the supplied merged checkpoint70."""
import argparse
import csv
import hashlib
import io
import json
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
START = datetime(2026, 11, 24, 19, 34, 24, tzinfo=timezone.utc)
SOURCE_SHA = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def table(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))

def changed():
    baseline = table(BASE / 'BASE_FILELIST.tsv')
    prefix = ROOT.name + '/'
    old = {r['path'][len(prefix):]: r['sha256'] for r in baseline
           if r['path'].startswith(prefix)}
    old_hashes = {r['sha256'] for r in baseline}
    old_hashes.update(r['sha256'] for r in table(BASE / 'CP70_INDEX.tsv'))
    payload = {}
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in {'__pycache__', '.git', 'build', 'renders', 'rendered',
                        'tmp', 'downloads', 'external_tmp'} for part in rel.parts):
            continue
        if path.suffix.lower() in {'.pyc', '.aux', '.fls', '.fdb_latexmk', '.toc',
                                   '.synctex', '.zip', '.png', '.jpg', '.jpeg'}:
            continue
        data = path.read_bytes()
        digest = sha(data)
        if old.get(str(rel)) == digest or digest in old_hashes:
            continue
        if path.suffix.lower() in {'.md', '.tex', '.tsv', '.csv', '.py', '.json',
                                   '.out', '.txt', '.bib'}:
            assert b'\r\n' not in data, ('Non-LF text', str(rel))
        assert 'temporary_literature' not in str(rel)
        payload[str(rel)] = data
    return payload

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['inspect', 'pack'])
    ap.add_argument('--number', type=int, default=71)
    args = ap.parse_args()
    if args.mode == 'inspect':
        payload = changed()
        print(json.dumps({'changed_files': len(payload),
                          'uncompressed_bytes': sum(map(len, payload.values())),
                          'largest': sorted(((len(v), k) for k, v in payload.items()),
                                            reverse=True)[:12]}, indent=2))
        return
    assert args.number >= 71
    due = START + timedelta(minutes=45 * (args.number - 70))
    now = datetime.now(timezone.utc)
    assert now >= due, ('Checkpoint not due', due.isoformat())
    output = BASE.parent / 'output'
    output.mkdir(exist_ok=True)
    destination = output / f'S6_SERIES_PUBLISH_checkpoint_{args.number}.zip'
    assert not destination.exists(), 'Do not replace a previously delivered checkpoint.'
    rows = table(ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv')
    done = [r for r in rows if r['status'] == 'done']
    # K9 was already closed in the supplied checkpoint70. Its c7 events
    # correct a primary-source description and restore that same check;
    # they do not close a new required identity in this continuation.
    preexisting_rechecks = {'02K9'}
    closed = [r['tag'] for r in done
              if r['check_event_id'].startswith('publish:c7:')
              and r['tag'] not in preexisting_rechecks]
    restored = [r['tag'] for r in done
                if r['tag'] in preexisting_rechecks
                and r['check_event_id'].startswith('publish:c7:')]
    pending = [r['tag'] for r in rows if r['status'] != 'done'
               and r['proof_status'] == 'released_after_derivation']
    open_tags = [r['tag'] for r in rows if r['status'] != 'done']
    state = {r['tag']: r['packet_status'] for r in rows}
    units = table(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
    unit_open = {p: sum(r['paper'] == p and r['status'] != 'done' for r in units) for p in ['III', 'IV']}
    source_sha = sha((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes())
    assert source_sha == SOURCE_SHA
    assert (ROOT / 'S6_SERIES_PUBLISH_report.md').read_text().splitlines()[0].startswith('INCOMPLETE')
    next_review = START + timedelta(hours=int((now - START).total_seconds() // 3600) + 1)
    previous_path = ROOT / 'code' / f'S6_SERIES_PUBLISH_c7_checkpoint_{args.number - 1}.out'
    previous_closed = set(json.loads(previous_path.read_text()).get('closed_this_continuation', [])) if previous_path.exists() else set()
    newly_closed = [tag for tag in closed if tag not in previous_closed]
    section = f'''

## Checkpoint {args.number} — {now.isoformat()}

Paper III has {len(done)}/128 required checks complete. Newly closed
since the previous checkpoint: {', '.join(newly_closed) or 'none'}.
LS was admitted at10:58:36.188625 UTC after the full original,
787-line receiver, all auxiliaries, exact maps and actual streams
were read. Its two guarded replacements, five defects and three
scoped events are retained; the canonical source is unchanged.

LT's historical220-line source was replayed unchanged and reproduced
all120275 saved JSON bytes. Root read all488 new audit lines and the
exact byte-inverse reader. Its two bounded auxiliary repairs have
complete maps and concrete examples. The973-line receiver and313-line
comparison are staged; root whole reading and admission remain open.

LV's complete936-line fresh proof froze11:16:04.388868 UTC. It proves
the full invariant package, actual global primitive sphere, reference
parity one and direct critical-chain intersection minus one. Every
fresh source/actual output and all2591 graph JSON lines were read.
The individual original was released11:18:22.502431 UTC, proof lines
21514--22383, after that completed derivation. Its full comparison
remains open. The failed first location guard and actual traceback
are retained. LT/LV close no invented required identities.

LG remains the sole required identity open. Its new raw-fixture
catalogue has been executed and agent-read; the complete fresh
synthesis and root whole reading still await LT/LV final comparisons.
LG's original and historical target inputs remain closed.

All {unit_open['III']} III unit criteria and all66 IV required checks
and {unit_open['IV']} IV unit criteria remain open. III's source SHA256
is {source_sha}. Provenance, final build and every-page review follow
the required checks and final unit pass. IV follows III; I/II/V wait
for the joint final step. Review63 recorded movement; the consecutive
no-movement count is zero. Packaging earns no movement credit.
Next checkpoint: {(due + timedelta(minutes=45)).isoformat()}.
Next hourly review: {next_review.isoformat()}. The report is INCOMPLETE.
'''
    for name in ('S6_SERIES_PUBLISH_report.md', 'PROGRESS_LEDGER.md'):
        with (ROOT / name).open('a', newline='') as stream:
            stream.write(section)
    summary = {'checkpoint': args.number, 'scheduled_utc': due.isoformat(),
               'snapshot_utc': now.isoformat(), 'required_done': len(done),
               'required_open': len(open_tags), 'open_unit_criteria': unit_open, 'closed_this_continuation': closed,
               'pending_released': pending, 'restored_preexisting_checks': restored,
               'path': str(destination)}
    log = json.dumps(summary, indent=2) + '\n'
    (ROOT / 'code' / f'S6_SERIES_PUBLISH_c7_checkpoint_{args.number}.out').write_text(log, newline='\n')
    payload = changed()
    assert 'CHECK_EVENTS.tsv' in payload
    readme = f'''# S6_SERIES_PUBLISH checkpoint {args.number}\n\nSnapshot: {now.isoformat()}; scheduled from {START.isoformat()}.\n\nUnpack the supplied S6_SERIES_PUBLISH_continue_cp70.zip once and run\npython restore_cp70.py at its root. Extract this checkpoint directly into\nthe restored S6_SERIES_PUBLISH_checkpoint_70 directory, replacing the same\nrelative paths. The supplied base and this newest checkpoint restore the\nworking state; no earlier return checkpoint is needed.\n\nRead the latest report and ledger sections, the required-progress table,\nand the complete fresh, comparison and admission records. Current III\nchecks: {len(done)}/128; all {unit_open['III']} unit criteria remain open. A saved fresh\nderivation, authorized release or staged receiver earns no closure until\nthe full comparison and receiver are admitted. Continuation-seven admitted\nrows: {', '.join(closed) or 'none'}.\n\nKS's complete D.V3 refutation and flag-manifold refinement and KU's\n58-response saved-API audit are admitted. S8/S9 retain every failed\nintermediate substitution and its correction. Use the complete receivers\nat their recorded scopes; never infer admission from file existence.\nKX: {state['02KX']}; L0: {state['02L0']}; L1: {state['02L1']}.\nContinue III, then IV, then the five-together step. I, II and V stay closed\nuntil that step. No work after this snapshot is assumed.\n\nThe file list records size and SHA256 of each payload except itself. No\nunchanged base file, other-author source download, source-page image, old\narchive, edit manifest, seal, census or inventory refresh is included.\nNext checkpoint: {(due + timedelta(minutes=45)).isoformat()}.\nNext hourly review: {next_review.isoformat()}. Continue without asking whether to proceed.\n'''
    payload[f'S6_SERIES_PUBLISH_checkpoint_{args.number}_README.md'] = readme.encode()
    buffer = io.StringIO(newline='')
    writer = csv.writer(buffer, delimiter='\t', lineterminator='\n')
    writer.writerow(['path', 'size', 'sha256'])
    for name, data in sorted(payload.items()):
        writer.writerow([name, len(data), sha(data)])
    payload[f'S6_SERIES_PUBLISH_checkpoint_{args.number}_filelist.tsv'] = buffer.getvalue().encode()
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            archive.writestr(name, data)
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        for name, data in payload.items():
            assert archive.read(name) == data
    print(log, end='')

if __name__ == '__main__':
    main()
