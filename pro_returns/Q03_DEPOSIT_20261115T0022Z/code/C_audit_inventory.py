#!/usr/bin/env python3
"""Print a compact inventory of the saved source-audit evidence."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'code/C_dependency_source_map.json').read_text())
print('Dependency counterpart rows:',len(rows),'unique ids:',len({x['q03_id'] for x in rows}))
print('Expected Q03 statement rows:',sum([10,7,5,5,5,3,5,4]))
c=json.loads((ROOT/'code/C_retrieve_compare_output.json').read_text())
print('OpenAI byte comparisons:',len(c['comparison']),'all identical:',all(x['equal'] for x in c['comparison']))
c=json.loads((ROOT/'code/C_course_compare_output.json').read_text())
print('Course chapters:',len(c),'first-eight identical:',all(x['attached_identical'] for x in c[:8]))
c=json.loads((ROOT/'code/C_search_history_complete.json').read_text())
print('Search batches:',len(c),'queries:',sum(len(x['queries']) for x in c),'result headings:',sum(len(x['result_sources']) for x in c))
for name in ['Q03_DEPOSIT_sources.md','Q03_DEPOSIT_literature.md']:
 t=(ROOT/name).read_text();print(name,len(t.splitlines()),'lines;',len(t.split()),'words')
