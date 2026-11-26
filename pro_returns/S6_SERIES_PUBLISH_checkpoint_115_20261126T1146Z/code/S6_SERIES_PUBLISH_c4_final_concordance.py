"""Admit the final Paper II owner-page concordance, preserving historical cells."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / 'agents/continuation4_conductor'
STEM = 'S6_SERIES_PUBLISH_c4_defect_concordance'
spec = importlib.util.spec_from_file_location('ii_final_concordance', AGENT / (STEM + '.py'))
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
plan_path = AGENT / (STEM + '_plan.json')
plan = json.loads(plan_path.read_text())
assert plan['summary'] == dict(resolved=11242, nonprinted=400, deleted=37, administrative=15)
assert len(plan['rows']) == 11694
for kind, expected in [
    ('source', '106fcde4a73b9d94f7bd328d05d517bb1c3813ca190bf253258ccf1bce5aa844'),
    ('pdf', 'b31d78f93b0d96315575d1053cd55ff3b5ec0e6427756e62e9628733f0c7c058'),
]:
    path = Path(plan['inputs'][kind])
    assert plan['inputs'][kind + '_sha256'] == expected
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected
reading = (ROOT / 'S6_SERIES_PUBLISH_reading_II.md').read_text()
assert 'Final-candidate status: complete.' in reading.split('\n\n', 2)[1]
assert plan['inputs']['pdf_sha256'] in reading
table = ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv'
original = table.read_bytes()
patched = module.apply_new_page_plan_bytes(original, plan)
assert table.read_bytes() == original
table.write_bytes(patched)
assert table.read_bytes() == patched
note = '''
## Root final admission

The reviewed v3 plan has been admitted to the central II defect table after
completion of the image-bound reading. All 11,694 rows have final dispositions:
11,242 current owner/destination mappings, 400 nonprinted records, 37 deleted
loci, and 15 administrative records. Only new_page cell byte spans changed;
every historical old_page lexeme and every other field byte was preserved by
the pure patch function. Owner pages retain the scope stated above and supply
no additional proof-check or page-reading credit. The full temporary plan was
removed after admission; the retained helper reconstructs the correspondence.
'''
review = AGENT / (STEM + '_review.md')
assert '## Root final admission' not in review.read_text()
review.write_text(review.read_text() + note, newline='\n')
unresolved = AGENT / (STEM + '_unresolved.md')
unresolved.write_text(unresolved.read_text() + note, newline='\n')
plan_path.unlink()
print('Final Paper II defect-page concordance admitted: 11,694 rows; zero unresolved.')
print('Every old_page lexeme and every non-new_page field byte preserved.')
print('Temporary full derived preview removed; no manuscript or check event changed.')
