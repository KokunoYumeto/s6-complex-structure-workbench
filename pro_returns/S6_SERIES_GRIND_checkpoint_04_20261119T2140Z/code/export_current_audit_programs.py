"""Place exact copies of current audit programs and receipts under code/.

Canonical working locations remain available so relative-path programs run
unchanged. The manifest records that correspondence and every copied hash.
"""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1];dest=R/'code/current_audits';dest.mkdir(parents=True,exist_ok=True)
suffixes={'.py','.js','.sage','.sh','.json','.jsonl','.out','.txt','.tsv','.md'}
entries=[]
for audit in sorted(R.glob('audit_*')):
 for p in sorted(audit.rglob('*')):
  if not p.is_file() or p.suffix not in suffixes or '__pycache__' in p.parts:continue
  # Large primary-source transcriptions remain at their canonical source path.
  if 'primary_sources' in p.parts:continue
  target=dest/p.relative_to(R);target.parent.mkdir(parents=True,exist_ok=True)
  shutil.copyfile(p,target)
  entries.append({'canonical_path':str(p.relative_to(R)),'code_copy':str(target.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(dest/'manifest.json').write_text(json.dumps(entries,indent=2)+'\n')
(dest/'README.md').write_text('''# Current audit programs and outputs

These are exact copies of the fresh audit programs and their derivations,
outputs and receipts. `manifest.json` maps every copy to its canonical
working path in the package and records its size and SHA-256.

Run a relative-path program from its listed canonical path. Both that
program and its inputs remain in the package. For example:

```sh
python audit_paper_i/iv_os45/code/k119_afterreading_exact.py
```

Copying and packaging do not count as another execution or proof check.
The original typed events state which programs were actually run, which
were newly written, and whether their derivation preceded proof reading.
Primary-source PDFs and large source transcriptions remain in the
corresponding `audit_*/primary_sources` directories.
''')
print(json.dumps({'files_copied':len(entries),'bytes':sum(x['bytes'] for x in entries),'programs':sum(Path(x['canonical_path']).suffix in {'.py','.js','.sage','.sh'} for x in entries)}))
