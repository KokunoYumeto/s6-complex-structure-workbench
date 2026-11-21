#!/usr/bin/env python3
"""Preserve the completed candidate14 provenance artefacts without rebinding them."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil


def digest(data):
    return hashlib.sha256(data).hexdigest()


root = Path(__file__).resolve().parents[2]
agent = root / 'agents/i_cont_provenance'
archive = agent / 'candidate14'
assert not archive.exists(), 'Refusing to overwrite an existing candidate14 archive.'
binding = json.loads((agent / 'S6_SERIES_PUBLISH_I_cont_provenance_binding.json').read_text())
assert binding['source']['sha256'] == '1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f'
assert binding['final_pdf']['sha256'] == '1abe0fc16350045cd2ce0aae57ce377dcfe2400de0b0bf58ba7e559d360bcb37'
guard = json.loads((agent / 'S6_SERIES_PUBLISH_I_cont_shared_guard.json').read_text())
items = []
for path in sorted(agent.iterdir()):
    if path.is_file():
        items.append((path, Path(path.name), None, 'agent artefact preserved verbatim'))
for name in ['source', 'ledger', 'final_pdf', 'build_summary', 'inherited_required_check_completion']:
    info = binding[name]
    path = root / info['path']
    items.append((path, Path('inputs') / info['path'], info['sha256'], name))
scan = root / 'records/S6_SERIES_PUBLISH_I_continuation_rendered_residue_scan.json'
items.append((scan, Path('inputs') / scan.relative_to(root), None, 'immutable candidate13 residue scan'))
for entry in guard['updates']:
    path = Path(entry['target'])
    items.append((path, Path('inputs') / path.relative_to(root), entry['expected_sha256'], 'guard target baseline'))

# Read and validate all inputs before creating the archive.
prepared = []
for original, relative, expected, role in items:
    data = original.read_bytes()
    actual = digest(data)
    if expected:
        assert actual == expected, f'Input changed before archival: {original}: {actual}'
    prepared.append((original, relative, data, actual, role))

archive.mkdir()
manifest = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'paper': 'I',
    'candidate': 14,
    'purpose': 'Verbatim historical preservation before rebinding a later candidate. Existing claims and open page gate are unchanged.',
    'source_sha256': binding['source']['sha256'],
    'pdf_sha256': binding['final_pdf']['sha256'],
    'ledger_sha256': binding['ledger']['sha256'],
    'all_claims_closed_in_preserved_binding': binding['all_claims_closed'],
    'new_mathematical_events': 0,
    'new_page_reading_credit': 0,
    'shared_files_modified': False,
    'path_note': 'Preserved artefact contents and paths are unchanged. The manifest maps originals to archive copies. Run preserved scripts only with explicit --root/--base/--out arguments where available.',
    'files': [],
}
for original, relative, data, sha, role in prepared:
    target = archive / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    assert target.read_bytes() == data
    manifest['files'].append({
        'original': str(original.relative_to(root)),
        'archive_copy': str(relative),
        'sha256': sha,
        'bytes': len(data),
        'role': role,
        'copied_verbatim': True,
    })
manifest_path = archive / 'S6_SERIES_PUBLISH_I_candidate14_provenance_archive_manifest.json'
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({
    'archive': str(archive.relative_to(root)),
    'manifest': str(manifest_path.relative_to(root)),
    'manifest_sha256': digest(manifest_path.read_bytes()),
    'files_preserved': len(manifest['files']),
    'total_bytes': sum(row['bytes'] for row in manifest['files']),
    'source_sha256': manifest['source_sha256'],
    'pdf_sha256': manifest['pdf_sha256'],
    'new_mathematical_events': 0,
    'new_page_reading_credit': 0,
    'shared_files_modified': False,
}, indent=2))
