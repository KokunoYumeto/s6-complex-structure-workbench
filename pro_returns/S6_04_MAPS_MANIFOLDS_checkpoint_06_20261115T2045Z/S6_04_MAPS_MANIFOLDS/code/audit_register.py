"""Check the expanded manuscript against the statement register and prompt table.

Run after build.py (which regenerates maps_A/maps_B) and assemble_register.py.
This is a deliverable consistency audit, not a test of mathematical claims.
"""
from pathlib import Path
from collections import Counter
import csv, re, json

root = Path(__file__).resolve().parents[1]
included = []

def expand(path, chain=()):
    if path in chain:
        raise RuntimeError('Recursive TeX inclusion: '+str(path))
    included.append(str(path.relative_to(root)))
    text = path.read_text()
    def replace(match):
        child = root / match.group(1)
        if not child.suffix:
            child = child.with_suffix('.tex')
        return expand(child, chain+(path,)) if child.exists() else ''
    return re.sub(r'\\input\{([^}]+)\}', replace, text)

text = expand(root/'S6_04_MAPS_MANIFOLDS_paper.tex')
heads = []
for match in re.finditer(r'\\paragraph\{', text):
    start = match.end()
    depth, end = 1, start
    while depth and end < len(text):
        if text[end] == '{' and text[end-1] != '\\':
            depth += 1
        elif text[end] == '}' and text[end-1] != '\\':
            depth -= 1
        end += 1
    heads.append(text[start:end-1])
# A scope heading may refer to several earlier statements without defining
# any new one. Count only the statement identifier immediately after its
# explicit theorem-type label.
paper_ids = [m.group(1) for h in heads
             if (m := re.match(r'(?:Theorem|Proposition|Lemma|Corollary|Problem|Conclusion|Computation|Remaining task)\s+([A-F]\.\d+\.\d+)\b', h))]
with (root/'S6_04_MAPS_MANIFOLDS_results.csv').open(newline='') as f:
    rows = list(csv.DictReader(f))
csv_ids = [row['id'] for row in rows]
expected = {f'{part}.{i}' for part, n in
            [('A',3),('B',6),('C',1),('D',3),('E',2),('F',4)]
            for i in range(1,n+1)}
coverage = {item for row in rows
            for item in re.findall(r'\b[A-F]\.\d+\b', row['item_of_the_prompt'])}
report = (root/'S6_04_MAPS_MANIFOLDS_report.md').read_text()
report_items = re.findall(r'^\| ([A-F]\.\d+) \|', report, re.M)
result = {
    'manuscript_statement_count':len(paper_ids),
    'register_statement_count':len(csv_ids),
    'duplicate_paper_ids':[x for x,n in Counter(paper_ids).items() if n>1],
    'duplicate_register_ids':[x for x,n in Counter(csv_ids).items() if n>1],
    'paper_missing_from_register':sorted(set(paper_ids)-set(csv_ids)),
    'register_missing_from_paper':sorted(set(csv_ids)-set(paper_ids)),
    'missing_prompt_items':sorted(expected-coverage),
    'report_prompt_rows':len(report_items),
    'report_missing_items':sorted(expected-set(report_items)),
    'report_duplicate_items':[x for x,n in Counter(report_items).items() if n>1],
    'open_statements':[row['id'] for row in rows if row['status']=='Open'],
    'report_marked_incomplete':report.startswith('INCOMPLETE\n'),
    'included_files':included,
}
(root/'records/register_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
for key in ['duplicate_paper_ids','duplicate_register_ids','paper_missing_from_register',
            'register_missing_from_paper','missing_prompt_items','report_missing_items',
            'report_duplicate_items']:
    assert not result[key], (key,result[key])
assert result['report_prompt_rows']==19
assert not result['open_statements'] or result['report_marked_incomplete']
