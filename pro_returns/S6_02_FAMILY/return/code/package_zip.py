"""Build and validate the complete research ZIP with a SHA-256 manifest.

Only the six named root deliverables and the sections/, code/, evidence/
trees are included. Temporary compiler files, caches, private helper
programs and rendered review PNGs remain outside the archive.
"""
from pathlib import Path
import hashlib
import json
import os
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / 'S6_02_FAMILY.zip'
ROOT_NAMES = (
    'S6_02_FAMILY_paper.tex',
    'S6_02_FAMILY_paper.pdf',
    'S6_02_FAMILY_results.csv',
    'S6_02_FAMILY_references.bib',
    'S6_02_FAMILY_report.md',
    'README.txt',
)
LOG = ROOT / 'code/package_zip.out'
MANIFEST = ROOT / 'MANIFEST.json'


def payload_paths():
    paths = [ROOT / name for name in ROOT_NAMES]
    for directory in ('sections', 'code', 'evidence'):
        paths.extend(
            p for p in (ROOT / directory).rglob('*')
            if p.is_file() and '__pycache__' not in p.parts
            and p.suffix != '.pyc' and p != LOG
        )
    assert all(p.is_file() and not p.is_symlink() for p in paths)
    assert len(paths) == len(set(paths))
    return sorted(paths, key=lambda p: p.relative_to(ROOT).as_posix())


paths = payload_paths()
LOG.write_text(
    'PASS: every required root deliverable exists.\n'
    'PASS: all included files are regular non-symlink files.\n'
    'PASS: temporary compiler files and Python caches are excluded.\n'
    f'ARCHIVE_ROOT {ROOT.name}/\n'
    f'PAYLOAD_FILES_WITH_LOG {len(paths) + 1}\n'
    f'ZIP_MEMBERS_WITH_MANIFEST {len(paths) + 2}\n'
    'MANIFEST_ALGORITHM SHA-256\n'
    'ZIP_METADATA_DATE 2026-11-12 00:00:00\n'
    'The final archive is additionally checked by testzip(), and its\n'
    'member set and every member hash are compared with this manifest.\n',
    encoding='utf-8',
)
paths = sorted(paths + [LOG], key=lambda p: p.relative_to(ROOT).as_posix())
records = []
for p in paths:
    data = p.read_bytes()
    records.append({
        'path': p.relative_to(ROOT).as_posix(),
        'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest(),
    })
MANIFEST.write_text(json.dumps({
    'package': 'S6_02_FAMILY',
    'credit': 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
    'algorithm': 'SHA-256',
    'scope': 'Every archive member except MANIFEST.json itself.',
    'files': records,
}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

members = sorted(paths + [MANIFEST], key=lambda p: p.relative_to(ROOT).as_posix())
temporary = ARCHIVE.with_suffix('.zip.tmp')
with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9, allowZip64=False) as zf:
    for p in members:
        info = zipfile.ZipInfo(
            ROOT.name + '/' + p.relative_to(ROOT).as_posix(),
            date_time=(2026, 11, 12, 0, 0, 0),
        )
        info.compress_type = zipfile.ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = (0o100644 << 16)
        zf.writestr(info, p.read_bytes(), compress_type=zipfile.ZIP_DEFLATED,
                    compresslevel=9)
with zipfile.ZipFile(temporary) as zf:
    assert zf.testzip() is None
    assert set(zf.namelist()) == {
        ROOT.name + '/' + p.relative_to(ROOT).as_posix() for p in members
    }
    for record in records:
        data = zf.read(ROOT.name + '/' + record['path'])
        assert len(data) == record['bytes']
        assert hashlib.sha256(data).hexdigest() == record['sha256']
    assert zf.read(ROOT.name + '/MANIFEST.json') == MANIFEST.read_bytes()
os.replace(temporary, ARCHIVE)
assert ARCHIVE.stat().st_size < 50 * 1024 * 1024
print('PASS: ZIP CRCs, exact member set, every payload SHA-256, size below 50 MiB.')
print('ZIP_MEMBERS', len(members))
print('ZIP_BYTES', ARCHIVE.stat().st_size)
print('ZIP_SHA256', hashlib.sha256(ARCHIVE.read_bytes()).hexdigest())
print('ZIP_PATH', ARCHIVE)
