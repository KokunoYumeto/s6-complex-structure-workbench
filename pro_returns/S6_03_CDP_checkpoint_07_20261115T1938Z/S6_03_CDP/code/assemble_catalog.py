"""Assemble every numbered manuscript statement and all checked bibliography entries.

Author-supplied metadata are retained. Newly written statements receive an
explicit proof-file location and scope, rather than disappearing from the table.
"""
from pathlib import Path
import csv
import re

root = Path(__file__).resolve().parents[1]
fields = ['id','statement','status','where_proved','depends_on','item_of_the_prompt',
          'findings_of_the_survey_settled (F-numbers)','notes']
meta = {}
for path in sorted((root/'records').glob('*_results.csv')):
    with path.open(newline='') as f:
        for row in csv.DictReader(f):
            row[fields[6]] = row.get(fields[6], row.get('findings_of_the_survey_settled',''))
            meta[row['id']] = row

root_items = {
 'B1':('B.1; Lead 2','F13'), 'B2':('B.2','F13'), 'B3':('B.2','F13'),
 'C2a':('C.2; Lead 5','F16'), 'C2b':('C.2','F16'), 'C2c':('C.2','F16'),
 'C2d':('C.2; B.3; A.2','F13; F16'),
 'C4a':('C.4; B.3','F6; F13; F14; F16'),
 'C4b':('B.3; C.4','F13; F16'),
 'C4c':('B.3; C.4','F6; F13; F14; F16'),
 'C4d':('B.3; C.4; A.3','F6; F13; F14; F16'),
 'C4e':('B.3; C.4; A.2','F13; F16'),
 'C4f':('C.4; B.3; A.3','F6; F13; F14; F16'),
 'C4g':('B.3; C.4','F13; F16'),
 'C5a':('C.5; Lead 8','F13'), 'C5b':('C.5; Lead 8','F13'),
 'C5c':('C.5; Lead 8','F13'),
 'E16':('E.4; Lead 9','F19'),
}
statements = []
seen = set()
for path in sorted((root/'sections').glob('*.tex')):
    text = path.read_text()
    matches = []
    pat = r'\\begin\{statement\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}'
    for match in re.finditer(pat, text):
        matches.append((match.start(),match.group(1),match.group(2),match.group(3)))
    pat2 = r'\\begin\{(?:proposition|theorem|corollary|lemma|example|remark)\}\[([A-E]\.\d+(?:\.(?:\d+|[A-Z]+))*);\s*([^\]]+)\]'
    for match in re.finditer(pat2, text):
        start = match.end()
        end = text.find(r'\end{', start)
        title = re.sub(r'\\label\{[^}]*\}', '',text[start:end]).strip()
        title = re.sub(r'\s+', ' ',title)
        matches.append((match.start(),match.group(1),match.group(2),title))
    for _, ident, status, title in sorted(matches):
        if ident in seen:
            raise ValueError(f'Duplicate numbered statement {ident}')
        seen.add(ident)
        row = {k:'' for k in fields}
        row.update({k:v for k,v in meta.get(ident,{}).items() if k in fields})
        row.update(id=ident, status=status, where_proved=f'{path.relative_to(root)}; Statement {ident}')
        if not row['statement']:
            row['statement'] = title
        if not row['item_of_the_prompt']:
            if ident in root_items:
                row['item_of_the_prompt'],row[fields[6]]=root_items[ident]
            elif ident.startswith('C.2.NC.'):
                row['item_of_the_prompt']='C.2; B.3; C.4'
            else:
                row['item_of_the_prompt']='.'.join(ident.split('.')[:2])
        statements.append(row)
with (root/'S6_03_CDP_results.csv').open('w', newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader();writer.writerows(statements)
print('Numbered statements:',len(statements))
print('IDs:',', '.join(row['id'] for row in statements))

bibpath=root/'S6_03_CDP_references.bib'
old=bibpath.read_text() if bibpath.exists() else ''
alltexts=[old]+[p.read_text() for p in sorted((root/'records').glob('*references.bib'))]
entries={}
for text in alltexts:
    starts=list(re.finditer(r'(?m)^@\w+\{([^,]+),',text))
    for i,match in enumerate(starts):
        end=starts[i+1].start() if i+1<len(starts) else len(text)
        entries[match.group(1)]=text[match.start():end].strip()
bibpath.write_text('\n\n'.join(entries.values())+'\n')
print('Bibliography entries:',len(entries))
