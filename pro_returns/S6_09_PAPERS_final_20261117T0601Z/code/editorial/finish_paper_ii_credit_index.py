"""Insert six scoped source credits and refresh only II's result concordance."""
from pathlib import Path
import json
import hashlib
import subprocess
import sys

D = Path(__file__).resolve().parents[2]
p = D / 'S6_09_PAPERS_II.tex'
s = p.read_text()
before = s
credits = json.loads((D / 'work/cdp_audit/II_working_credit/positive_credit_insertions.json').read_text())
for item in credits['replacements']:
    assert s.count(item['old']) == item['expected_occurrences'], (item['name'], s.count(item['old']))
    s = s.replace(item['old'], item['new'])
p.write_text(s)
old_index = (D / 'editorial/II_result_index.tex').read_text()
old_programs = (D / 'editorial/II_programs.tex').read_bytes()
result = subprocess.run([sys.executable, str(D / 'code/editorial/build_paper_ii_indices.py')], check=True, capture_output=True, text=True)
new_index = (D / 'editorial/II_result_index.tex').read_text()
assert (D / 'editorial/II_programs.tex').read_bytes() == old_programs, 'Unexpected change in the frozen program appendix'
assert s.count(old_index) == 1
s = s.replace(old_index, new_index)
p.write_text(s)
record = {'before_tex_sha256': hashlib.sha256(before.encode()).hexdigest(),
          'after_tex_sha256': hashlib.sha256(s.encode()).hexdigest(),
          'exact_credit_insertions': credits,
          'before_complete_result_index': old_index,
          'after_complete_result_index': new_index,
          'program_appendix_byte_identical': True,
          'indexer_output': result.stdout,
          'mathematical_statements_and_proofs_changed': False,
          'scope': 'Six exact attribution paragraphs and the full313-row credit concordance; every existing result label and proof remains in place.'}
(D / 'records/II_final_credit_index_refresh.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(result.stdout.strip())
print('Six exact source-credit insertions applied; complete result concordance refreshed; program appendix byte-identical.')
