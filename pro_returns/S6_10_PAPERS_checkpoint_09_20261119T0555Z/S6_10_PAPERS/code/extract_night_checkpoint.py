"""Recover the current textual research payload from a supplied checkpoint.

No archive-supplied program is executed. Every written payload is checked
against the checkpoint's recorded byte length and SHA256. Historical images
and PDF reconstruction objects remain in the source archive.
"""
from pathlib import Path
import collections
import hashlib
import json
import tarfile
import zipfile
import argparse

ROOT = Path(__file__).resolve().parents[3]
ARCHIVE = ROOT / 'sources/newer_night/S6_06_BLIND_checkpoint_25.zip'
DESTINATION = ROOT / 'sources/newer_night/checkpoint25'
PREVIOUS = ROOT / 'sources/night_run'
TEXT_SUFFIXES = {'.tex', '.bib', '.md', '.csv', '.tsv', '.json', '.txt', '.py', '.sh', '.gp', '.sage', '.jl', '.cpp', '.c', '.h', '.toml', '.bbl', '.aux', '.log'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    global ARCHIVE, DESTINATION, PREVIOUS
    parser=argparse.ArgumentParser();parser.add_argument('--number',type=int,default=25);args=parser.parse_args()
    number=args.number
    ARCHIVE=ROOT/f'sources/newer_night/S6_06_BLIND_checkpoint_{number:02d}.zip'
    DESTINATION=ROOT/f'sources/newer_night/checkpoint{number}'
    if number>25:PREVIOUS=ROOT/f'sources/newer_night/checkpoint{number-1}'
    DESTINATION.mkdir(parents=True, exist_ok=True)
    written = []
    with zipfile.ZipFile(ARCHIVE) as z:
        manifest = json.loads(z.read(f'checkpoint{number}_transport_manifest.json'))
        selected = {}
        for name, record in manifest['files'].items():
            p = Path(name)
            if p.parts[0] != 'S6_06_BLIND' or p.suffix.lower() not in TEXT_SUFFIXES:
                continue
            relative = Path(*p.parts[1:])
            if any(part in {'history', 'checkpoints', 'checkpoint_versions', '__pycache__', 'sources', 'rendered'} for part in relative.parts):
                continue
            selected[name] = record
        waiting = collections.defaultdict(list)
        archive_names = set(z.namelist())

        def install(name, data, origin):
            record = selected[name]
            if len(data) != record['bytes'] or digest(data) != record['sha256']:
                raise ValueError('Content mismatch: ' + name)
            relative = Path(*Path(name).parts[1:])
            target = DESTINATION / relative
            if not target.resolve().is_relative_to(DESTINATION.resolve()):
                raise ValueError('Unsafe target: ' + name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            written.append({'file': str(relative), 'bytes': len(data), 'sha256': record['sha256'], 'origin': origin})

        for name, record in selected.items():
            previous = PREVIOUS / Path(*Path(name).parts[1:])
            if name in archive_names:
                install(name, z.read(name), 'direct checkpoint member')
            elif previous.is_file() and previous.stat().st_size == record['bytes'] and digest(previous.read_bytes()) == record['sha256']:
                install(name, previous.read_bytes(), 'byte-identical attached payload')
            else:
                content = manifest['contents'][record['sha256']]
                if content['storage'] != 'raw':
                    raise ValueError('Text unexpectedly requires reconstruction: ' + name)
                waiting[content['name']].append(name)
        print('Selected', len(selected), 'text files;', len(waiting), 'distinct payloads need recovery.', flush=True)
        for bundle in manifest['bundles']:
            if not waiting:
                break
            bundle_name = bundle['file']
            with tarfile.open(fileobj=z.open(bundle_name), mode='r|xz') as t:
                for member in t:
                    if member.name not in waiting:
                        continue
                    data = t.extractfile(member).read()
                    for name in waiting.pop(member.name):
                        install(name, data, bundle_name)
            print('Read', bundle_name, '; remaining payloads', len(waiting), flush=True)
        if waiting:
            raise ValueError('Missing payloads: ' + ', '.join(waiting))
        result = {'archive': ARCHIVE.name, 'snapshot': manifest['snapshot'], 'files': written, 'verified': len(written)}
        report = ROOT / f'work/S6_10_PAPERS/analysis/night_checkpoint{number}_extraction.json'
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(result, indent=2))
        print('Verified', len(written), 'files at', DESTINATION, flush=True)

if __name__ == '__main__':
    main()
