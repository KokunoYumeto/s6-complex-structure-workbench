"""Apply two observed final-print repairs, with exact retained evidence."""
from pathlib import Path
import json
import hashlib

D = Path(__file__).resolve().parents[2]
changes = []
for rel in ['S6_09_PAPERS_I.tex', 'editorial/I_result_index.tex']:
    p = D / rel
    s = p.read_text()
    old = 'The generator xi⊗gamma and isomorphism'
    new = r'The generator $\xi\otimes\gamma$ and isomorphism'
    if old not in s:
        assert new in s
        continue
    assert s.count(old) == 1
    t = s.replace(old, new)
    p.write_text(t)
    changes.append({'file': rel, 'before': old, 'after': new,
                    'before_sha256': hashlib.sha256(s.encode()).hexdigest(),
                    'after_sha256': hashlib.sha256(t.encode()).hexdigest(),
                    'reason': 'Actual LuaLaTeX build32 and PDF page465 omitted the unsupported text-font tensor glyph. The same generator is now set in mathematical notation.'})

p = D / 'S6_09_PAPERS_references.bib'
s = p.read_text()
old = '@misc{mapsPetersonPinned,\n  author = {Peterson, Eric C.},'
new = '@misc{mapsPetersonPinned,\n  author = {Peterson, Eric C.},\n  year = {n.d.},'
if old in s:
    assert s.count(old) == 1
    t = s.replace(old, new)
    p.write_text(t)
    changes.append({'file': p.name, 'before': old, 'after': new,
                    'before_sha256': hashlib.sha256(s.encode()).hexdigest(),
                    'after_sha256': hashlib.sha256(t.encode()).hexdigest(),
                    'reason': 'The opened pinned author-source checkout supplies no publication date. Explicit n.d. preserves that fact and resolves the BibTeX empty-year warning without inventing a year.'})
else:
    assert new in s
record = D / 'records/final_glyph_and_undated_entry_repairs.json'
if changes:
    if record.exists():
        changes = json.loads(record.read_text())['changes'] + changes
    record.write_text(json.dumps({'changes': changes}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'exact_repairs': len(changes)}))
