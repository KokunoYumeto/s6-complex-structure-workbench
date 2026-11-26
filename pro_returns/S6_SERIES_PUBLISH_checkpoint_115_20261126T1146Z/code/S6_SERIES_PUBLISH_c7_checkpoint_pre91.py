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

LN was admitted at09:08:51.122973 UTC, bringing III to124/128. Its whole
1191-line receiver, originals, auxiliaries, historical sources and every
new source and actual stream were read, including all retained failed
versions. The scalar-exclusion reason is corrected precisely: index16
alone is shared by a natural I1 scalar example, whereas the explicit
scalar map preserves positive-I1 support. Twenty narrow defects and
six events retain the exact mathematical and chronology scopes.

LQ was admitted at09:43:52.976553 UTC, bringing III to125/128. Its736-line
fresh proof preceded original release08:54:58.364200. Root wholly read
the131-line statement,396-line proof and17 following auxiliary lines,
the725-line final receiver, all comparison/record fields and all new
sources and actual streams. One narrow D25 corrects the original
complex-orientation assertion; the explicit involutive conductor map
and inverse preserve all theorem conclusions in hatted coordinates.
Its24 D19 changes preserve the permanent identities bijectively. The
pinned210-line historical main was actually replayed byte for byte at
its exact12-marking,95-local,1638-global scope, with one local symbolic
expansion. D09 corrects the broader symbolic-global execution wording.
All12 old/fresh basis transitions and inverses were read entry by entry.

LS's complete1216-line fresh proof was frozen09:29:21 and individually
released09:37:04.929071 UTC. Root wholly read the1183-line first assembly
and all final changed hunks, every executed assembly/edit source and
actual stream. Both lossless-reader inverses and every600 final output
lines were read; they recover all88 main stdout lines and16 complete
JSON records exactly. All23-by59 relations, cap/normal maps and the
six-disc inverse are proved. Root read the entire released statement,
232-line original proof and following auxiliary. Root has now wholly
read all three primary historical sources160/60/82 and every retrieval,
retention, inspection and bounded-extraction source/actual stream.
Both new post-local150 and post-relations161 sources are wholly read.
Their direct lossless2038-line readback recovers all627+37+138 actual
stdout lines and both historical JSON files exactly; agent whole reading
is complete, root whole reading remains pending. The full old70-to-new59
relation maps and inverses, physical-reflection divisor difference and
relative meridian shear are retained. The772-line receiver and final
comparison/proposal records are under review; no admission is claimed.

LU was admitted10:20:11.164157 UTC, bringing III to126/128. Its complete
698-line fresh proof and135-line graph peer review preceded original
release09:21:18.362497. Root wholly read the56-line statement,92-line
original proof, full following auxiliary,652-line final receiver, all
comparison/source-check/post-exposure notes and every defect/event/guard.
All assembly/edit/record sources and actual streams are wholly read.
The archived comparison checks42 tables,273 whole records and1151 local
maps, preserving the212 residue cases and45 additional higher-weight/log
cases. Both historical209/61-line sources are read; only their isolated
multiplicative-rejection expression was executed. No whole historical
module execution is claimed. The exact default-kernel/selector input,
literal KS d=0 and whole-fibre divisor difference are recorded. Its16
defects and six events retain the precise implementation/frame scopes.

LT's complete798-line fresh proof was frozen10:20:03 UTC and root-read.
Root read all293 source lines,21 actual stdout lines, captured empty
stderr,71/112-line scope/calculation notes, and the retained failed-edit
argument/diagnostic. The1911 finite cones supplement explicit general
quotient/inverse/bounding maps, retaining the order-h torsion coordinate.
The original was released as a unit-only obligation10:29:02.864443,
proof21120--21275. No required identity or publication unit was closed.
The full original comparison remains open.

LV's original/history remain closed. Root has written a substantial new
fresh derivation and executed one lattice run and one toric coefficient
run, each with whole source/output reading. Exact inverse maps give the
index-two divisor lattice, primitive basis, all680 cubic coordinates,
mixed coordinates and cyclic boundary periods. The component restrictions
give the Pontryagin-square values and all256 tested character shifts agree
with the general fixed-curve formula. The graph lane's fresh306-line
circle-bordism note gives the refined-class route and an exact local
chain obstruction showing why the requested source-sphere transport
needs global geometry. Root wholly read that306-line note and checked
its circle bordism; the global sphere construction remains open.
No complete LV admission or original release is inferred.

LG's original remains closed and its fresh synthesis is pending the
completed supporting results. LT/LV create no invented required rows.
Review63 at the10:34:24 scheduled boundary records126/128, newly admitted
LQ/LU, and consecutive no-movement count zero. K9 remains a restored
preexisting check and earns no new-row movement credit.
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
Current LQ state: {state['02LQ']}.
Current LS state: {state['02LS']}.
Current LU state: {state['02LU']}.
Current LG state: {state['02LG']}.
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
