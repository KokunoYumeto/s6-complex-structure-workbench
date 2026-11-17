"""Inline the final Paper II bibliography without reassembling its proofs."""
from pathlib import Path
import hashlib, json, re
D = Path(__file__).resolve().parents[2]
p = D/'S6_09_PAPERS_II.tex'
before = p.read_text()
pattern = r'\\begin\{thebibliography\}.*?\\end\{thebibliography\}'
old = re.findall(pattern, before, re.S)
assert len(old) == 1
new = (D/'editorial/II_bibliography.tex').read_text().strip()
assert new.startswith(r'\begin{thebibliography}') and new.endswith(r'\end{thebibliography}')
after = re.sub(pattern, lambda m: new, before, flags=re.S)
p.write_text(after)
record = {
    'reason': 'Final credited re-derivation adds the actually opened DGKX version 1 citation; the source now contains all 102 cited entries inline.',
    'before_tex_sha256': hashlib.sha256(before.encode()).hexdigest(),
    'after_tex_sha256': hashlib.sha256(after.encode()).hexdigest(),
    'previous_bibliography': old[0],
    'current_bibliography': new,
    'mathematical_text_changed': False,
}
(D/'records/II_final_inline_bibliography_refresh.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(record['after_tex_sha256'])
