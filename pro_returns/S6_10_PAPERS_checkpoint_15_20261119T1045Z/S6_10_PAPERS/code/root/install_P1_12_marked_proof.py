"""STAGED, NOT EXECUTED: superseded by the retained-dependency decision.

P1.19 uses the old complement route. It remains in-paper while a separately
unexposed reviewer derives that route. An aggregate installer will be written
after its comparison. Keep this draft as provenance; do not run its mutation.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

raise SystemExit('Deferred: P1.19 needs the retained P1.12 complement route; see P1_12_comparison_and_dependency_decision.md')

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS = ROOT / 'analysis/continuation_root'
RECEIPT = ANALYSIS / 'P1_12_marked_proof_replacement_receipt.json'
assert not RECEIPT.exists(), 'One-shot installation already recorded'
frozen = json.loads((ANALYSIS / 'P1_12_prereading_frozen_receipt.json').read_text())
for row in frozen['files']:
    assert hashlib.sha256((ROOT / row['path']).read_bytes()).hexdigest() == row['sha256'], row['path']

fragment = ROOT / 'papers/V/revisions/P1_12_marked_leray_proof.tex'
new = fragment.read_text().strip()
assert new.startswith('\\begin{proof}') and new.endswith('\\end{proof}')
uses = r'\cref{night:P1.1,night:P1.9,night:P1.10,night:P1.11,maps:src:F.2.6}'
sources = ['papers/V/body.tex', 'papers/V/body_source.tex', 'S6_10_PAPERS_V.tex']
rows = []
for name in sources:
    f = ROOT / name
    text = f.read_text()
    label = text.index(r'\label{night:P1.12}')
    start = text.rfind(r'\begin{theorem}', 0, label)
    a = text.index(r'\begin{proof}', label)
    b = text.index(r'\end{proof}', a) + len(r'\end{proof}')
    old_block = text[start:b]
    old_proof = text[a:b]
    stem = ('standalone' if name == 'S6_10_PAPERS_V.tex' else f.stem)
    backup = ANALYSIS / f'P1_12_superseded_{stem}.tex'
    assert not backup.exists()
    backup.write_text(old_block + '\n')
    header = text[start:a]
    pos = header.index(r'\StatementRecord') + len(r'\StatementRecord')
    args = []
    for _ in range(4):
        while header[pos].isspace():
            pos += 1
        assert header[pos] == '{'
        opening = pos
        depth = 1
        pos += 1
        while depth:
            if header[pos] == '{':
                depth += 1
            elif header[pos] == '}':
                depth -= 1
            pos += 1
        args.append((opening, pos))
    u, v = args[3]
    header = header[:u] + '{' + uses + '}' + header[v:]
    updated = text[:start] + header + new + text[b:]
    f.write_text(updated)
    rows.append({'path': name, 'old_file_sha256': hashlib.sha256(text.encode()).hexdigest(),
                 'new_file_sha256': hashlib.sha256(updated.encode()).hexdigest(),
                 'old_proof_sha256': hashlib.sha256(old_proof.strip().encode()).hexdigest(),
                 'preserved_block': str(backup.relative_to(ROOT)),
                 'preserved_block_sha256': hashlib.sha256(backup.read_bytes()).hexdigest()})

receipt = {'installed_at_utc': datetime.now(timezone.utc).isoformat(),
           'target': 'night:P1.12', 'prereading_frozen_at_utc': frozen['frozen_at_utc'],
           'new_proof_sha256': hashlib.sha256(new.encode()).hexdigest(),
           'new_proof_path': str(fragment.relative_to(ROOT)), 'files': rows,
           'reason': 'Install the complete independently prewritten marked evaluation, finite collar, integral Leray and UCT proof. The full former complement-cone proof is preserved; its extra matrices/programs receive no retrospective prereading or new-code credit.',
           'unchanged_assertion': True, 'new_uses': uses,
           'build_status': 'Source installed; new PDF will be produced by the next current-source build.'}
RECEIPT.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
