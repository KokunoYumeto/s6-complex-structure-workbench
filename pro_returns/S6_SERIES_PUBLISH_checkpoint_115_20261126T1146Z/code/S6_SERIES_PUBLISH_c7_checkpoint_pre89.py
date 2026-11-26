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

Paper III has {len(done)}/128 required checks complete and {len(open_tags)} open.
Required rows closed since the previous checkpoint: {', '.join(newly_closed) or 'none'}.
The individual comparisons, defect rows, exact replacement guards and
root admission reviews give each conclusion and its checked scope.
LM, LF and LI are admitted at their precise recorded scopes. LM's whole
998-line receiver and every new source/stream are read. Eight of eleven
P/model assignments change; the five-copy b20 framing bridge is expressly
post-exposure used-and-rechecked work. LF's whole796-line receiver,
original, auxiliary and all new sources/streams are read. All eight model
conclusions stand, with three D25 repairs for the rotating cusp, Borel line
relation and transported wall computation. LI's whole498 mathematical
lines plus the exact printed-tag addition give the final499-line receiver.
All fifteen integral formulas stand; the D26 count is495 in the broad
family and459 in its all-star-original subset, related by exact inclusion
and replacement maps. The saved-data validator checks all35 stored full
matrices,141 whole quadratic coefficient blocks and65 finite-power tests;
it earns no historical-program execution credit. LM, LF and LI admissions
occurred at06:57:20,07:19:16 and07:31:46 UTC respectively.

LF's redundant file
agents/continuation7_iii_three_primary_receiving/S6_SERIES_PUBLISH_III_02LF_packet_manifest_v001.json
was removed under prompt section0.5's prohibition on edit manifests.
Its authoritative defects, CHECK_EVENTS and exact guards, and all actual
executed sources/streams, are retained. The removal and prior hash are
recorded by the retained root correction source and admission review.

LK is admitted at08:05:55.936627 UTC, bringing III to122/128. Root read
the entire962-line receiver, all originals and auxiliaries, the complete
Laurent/Tor sources and actual streams, the exact historical replay and
the75-case validator. All mathematical assertions stand. Its29 defects
are presentation corrections; the14 manual numbers map bijectively by
permanent equation identities to automatic numbering. The narrow LK
admission helper verifies these exact maps and all three guarded spans.

LJ is admitted at08:51:05.219879 UTC, bringing III to123/128. Root read
its whole original and auxiliaries, the complete receiver and exact final
changes, all new sources and actual streams, the118-line historical
source and724-line saved JSON, and every comparison, guard and defect.
The final1476-line receiver gives six oriented types across the fourteen
patterns and changes seven assignments. Its full three-primary class
vanishes in Z/9. The historical executable was not run; the new77-line
validator output has its exact independent finite scope. The five defects
comprise one conclusion repair and four intermediate repairs. D19 internal
automatic-numbering work remains in the open publication-unit pass.

LN's1078-line fresh proof was released at08:20:46.096207 UTC after whole
root review. Root has read the entire original statement/proof and its
following auxiliary, and the complete1191-line staged replacement. The
final one-word grammar correction and its source are retained. The new
post-exposure checks verify284 normal closures,912 local projections,
21 products/unit claims,148 examples and90 overlaps. Three unsuccessful
mathematical versions and two unsuccessful pre-write assembly attempts
are preserved. The full historical source/new-source/actual-output root
review and final admission remain open. The support-based OS45 extension
argument replaces the insufficient index-only argument. The exact limited
incidental exposures are disclosed in its source note.

LQ's736-line fresh proof is frozen at08:47:03.397764 UTC and individually
released at08:54:58.364200 UTC. Root read every fresh line, all534 new
source lines, all44 actual stdout lines and all three empty stderr files,
and the full input, calculation and failed-edit notes. Its exact toric
action retains both anti-invariant units; conductor and central-prism
maps give all integral kernels and inverse markings. The computation
checks12 markings,80 conductor complexes,1260 local inverse cases,
11340 global Smith cases and1500 central-word cases. The complete original
comparison and historical audit are in progress; no admission is claimed.

LS's corrected-line proof notes and16 new OS45 full bar matrices remain
fresh work. Root has read its entire381-line source. Lossless output
readbacks preserve exact reconstruction of the original88-line output;
whole mathematical output reading and final fresh completion remain open.
LU's new254-line cone source and all33 stdout lines are wholly read, with
its actual empty stderr. It proves and checks29 additive cones, including
14 nonzero h=1 examples, and the explicit area, normal and inverse maps.
The written IC8 component permutation/divisor and global assembly are now
saved fresh work, pending final supporting readback and freeze. LS, LU and
LG originals remain closed. K9 restores a preexisting identity and earns
no new-row movement. Review61 completed at08:35:16.892032 UTC with122/128,
one new LK closure and consecutive no-movement count zero. LJ is movement
for Review62, due09:34:24 UTC.
Current LL state: {state['02LL']}.
Current LE state: {state['02LE']}.
Current LH state: {state['02LH']}.
Current LP state: {state['02LP']}.
Current LM state: {state['02LM']}.
Current LI state: {state['02LI']}.
Current LF state: {state['02LF']}.
Current LK state: {state['02LK']}.
Current LJ state: {state['02LJ']}.
Current LN state: {state['02LN']}.
Released comparisons still open: {', '.join(pending) or 'none'}.
All open III tags: {', '.join(open_tags)}.
All {unit_open['III']} III unit criteria and all 66 IV required checks and
{unit_open['IV']} IV unit criteria remain open. III's canonical source
remains at SHA256 {source_sha}. The complete required checks precede the
unit pass, repairs, provenance, clean build and rendered-page reading.
IV follows III; I, II and V retain their closed gates until the joint step.
The report remains INCOMPLETE. The checkpoint contains new or changed
work relative to checkpoint70, excluding fetched publications, extracted
source passages, page images and unchanged copies.
Next checkpoint: {(due + timedelta(minutes=45)).isoformat()}.
Next hourly review: {next_review.isoformat()}. Packaging earns no movement credit.
'''
    section += '\nThe admitted KS, LB and LC D27 refinements and all associated III/IV and later I/II/V applications retain their recorded scopes and open unit gates.\n'
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
