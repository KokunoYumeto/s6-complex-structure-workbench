#!/usr/bin/env python3
"""Audit final schema, item coverage, statement labels and bibliography access notes."""
from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','notes']
with (root/'S6_05_ARITHMETIC_results.csv').open(newline='') as f:
    reader=csv.DictReader(f)
    assert reader.fieldnames==fields
    rows=list(reader)
assert len(rows)==len({r['id'] for r in rows})
assert all(r['id'] and r['statement'] and r['status'] and r['where_proved'] and r['item_of_the_prompt'] for r in rows)
missing_labels=[]
for path in sorted((root/'sections').glob('*.tex')):
    for line in path.read_text().splitlines():
        if ('\\begin{statement}[' in line or '\\paragraph{Statement ' in line):
            if not any(s in line for s in ['Proved','Refuted','Known','Open']):
                missing_labels.append((path.name,line))
assert not missing_labels,missing_labels
report=(root/'S6_05_ARITHMETIC_report.md').read_text()
assert report.splitlines()[0]=='INCOMPLETE'
items=[f'A.{i}' for i in range(1,6)]+[f'B.{i}' for i in range(1,5)]+[f'C.{i}' for i in range(1,9)]
assert all(f'| {item} |' in report for item in items)
assembly=json.loads((root/'records/assembly_audit.json').read_text())
assert assembly['statement_count']==len(rows)
text=(root/'S6_05_ARITHMETIC_references.bib').read_text()
notes=re.findall(r'\bnote\s*=\s*\{([^\n]*)',text)
assert len(notes)==assembly['bibliography_count']
assert all(re.match(r'(verified|unverified)',n,re.I) for n in notes)
result={'schema':'PASS','statement_count':len(rows),'unique_ids':len(rows),
        'explicit_heading_labels':'PASS','report_item_rows':len(items),
        'bibliography_entries':len(notes),'access_status_notes':'PASS',
        'overall_status':'INCOMPLETE','unresolved':['A.5 numbered-known-conjecture implication','C.7(c) unconditional norm classification']}
(root/'records/final_register_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
