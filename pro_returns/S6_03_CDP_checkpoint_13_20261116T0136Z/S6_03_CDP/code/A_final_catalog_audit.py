"""Read-only audit of authored/assembled statements and catalogue metadata.

The script writes only its own JSON/text audit outputs.  It does not assemble,
edit, or certify mathematical proofs.  Historical drafts are intentionally not
treated as additional manuscript statements.
"""
from pathlib import Path
import collections
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PAT = re.compile(r'\\begin\{statement\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}|'
    r'\\begin\{(?:proposition|theorem|corollary|lemma|example|remark)\}'
    r'\[([A-E]\.\d+(?:\.(?:\d+|[A-Z]+))*);\s*([^\]]+)\]')

def lineof(text, pos):
    return text.count('\n', 0, pos) + 1

def recursive_text(path, trail=()):
    """Expand non-part proof fragments; part_* are independently assembled."""
    if path in trail:
        raise ValueError(f'cyclic input: {path}')
    text = path.read_text()
    def replace(m):
        target = ROOT / m.group(1)
        if target.suffix != '.tex':
            target = target.with_suffix('.tex')
        if target.name.startswith('part_'):
            return ''
        if not target.exists():
            return m.group(0)
        return recursive_text(target, (*trail, path))
    return re.sub(r'\\input\{([^}]+)\}', replace, text)

statements = []
source_texts = {}
for path in sorted((ROOT / 'sections').glob('part_*.tex')):
    text = path.read_text()
    source_texts[str(path.relative_to(ROOT))] = recursive_text(path)
    for m in PAT.finditer(text):
        statements.append(dict(id=m.group(1) or m.group(4),
            status=m.group(2) or m.group(5), title=m.group(3) or '',
            source=str(path.relative_to(ROOT)), line=lineof(text,m.start())))

by_id = collections.defaultdict(list)
for row in statements:
    by_id[row['id']].append(row)
meta = collections.defaultdict(list)
for path in sorted((ROOT / 'records').glob('*_results.csv')):
    with path.open(newline='') as stream:
        for n,row in enumerate(csv.DictReader(stream),2):
            row['_file'] = str(path.relative_to(ROOT)); row['_line'] = n
            meta[row['id']].append(row)
with (ROOT / 'S6_03_CDP_results.csv').open(newline='') as stream:
    consolidated_rows = list(csv.DictReader(stream))
consolidated = {r['id']:r for r in consolidated_rows}

tags = collections.defaultdict(list)
labels = collections.defaultdict(list)
cites = collections.defaultdict(list)
for source,text in source_texts.items():
    for m in re.finditer(r'\\tag\*?\{([^}]+)\}',text):
        tags[m.group(1)].append(source)
    for m in re.finditer(r'\\label\{([^}]+)\}',text):
        labels[m.group(1)].append(source)
    for m in re.finditer(r'\\(?:cite|citep|citet|citeauthor|citeyear|nocite)\*?(?:\[[^\]]*\])*\{([^}]+)\}',text):
        for key in m.group(1).split(','):
            cites[key.strip()].append(source)

bibtext = (ROOT / 'S6_03_CDP_references.bib').read_text()
starts = list(re.finditer(r'(?m)^@\w+\{([^,]+),',bibtext))
bib = {}
for i,m in enumerate(starts):
    end = starts[i+1].start() if i+1<len(starts) else len(bibtext)
    entry=bibtext[m.start():end]
    bib[m.group(1)] = dict(text=entry, verified=bool(re.search(r'\bverified\b',entry,re.I)),
        unverified=bool(re.search(r'\bunverified\b',entry,re.I)))

all_items = [f'{a}.{i}' for a,n in [('A',5),('B',3),('C',5),('D',2),('E',4)] for i in range(1,n+1)]
coverage = {i:[] for i in all_items}
leads = {str(i):[] for i in range(1,10)}
for ident in by_id:
    row = meta.get(ident,[consolidated.get(ident,{})])[-1]
    items = row.get('item_of_the_prompt','')
    for item in coverage:
        if re.search(r'(?<![A-Z0-9])'+re.escape(item)+r'(?![0-9])',items):
            coverage[item].append(ident)
    for lead in leads:
        if re.search(r'\bLead\s*'+lead+r'\b',items,re.I):
            leads[lead].append(ident)

status_mismatches=[]
semantic_status_mismatches=[]
def status_class(value):
    m=re.match(r'\s*(Proved|Refuted|Known|Open)\b',value,re.I)
    return m.group(1).lower() if m else None
for ident,ss in by_id.items():
    for row in meta.get(ident,[]):
        if row.get('status','').strip()!=ss[0]['status'].strip():
            status_mismatches.append(dict(id=ident,source_status=ss[0]['status'],
                metadata_status=row.get('status'),file=row['_file']))
        if status_class(row.get('status','')) != status_class(ss[0]['status']):
            semantic_status_mismatches.append(dict(id=ident,source_status=ss[0]['status'],
                metadata_status=row.get('status'),file=row['_file']))

stale = []
stale_pat = re.compile(r'(?i)unresolved|remain(?:s)? open|still open|remaining gap|not settled|unfinished|not yet|not complete')
for source,text in source_texts.items():
    for n,line in enumerate(text.splitlines(),1):
        if stale_pat.search(line):
            stale.append(dict(source=source,line=n,text=line))

built_manifest = json.loads((ROOT/'build/ordered/manifest.json').read_text())
result = dict(
    source_statement_count=len(statements), source_unique_ids=len(by_id),
    assembled_statement_count=len(built_manifest),
    source_not_assembled=sorted(set(by_id)-{r['id'] for r in built_manifest}),
    assembled_not_source=sorted({r['id'] for r in built_manifest}-set(by_id)),
    duplicate_statement_ids={k:v for k,v in by_id.items() if len(v)>1},
    duplicate_equation_tags={k:v for k,v in tags.items() if len(v)>1},
    duplicate_labels={k:v for k,v in labels.items() if len(v)>1},
    missing_author_metadata=sorted(set(by_id)-set(meta)),
    metadata_without_current_statement=sorted(set(meta)-set(by_id)),
    duplicate_author_metadata={k:[r['_file'] for r in v] for k,v in meta.items() if len(v)>1},
    status_wording_differences=status_mismatches,
    semantic_status_mismatches=semantic_status_mismatches,
    unclassified_source_statuses=[r for r in statements if status_class(r['status']) is None],
    consolidated_source_status_mismatches=[dict(id=k,source_status=v[0]['status'],catalog_status=consolidated[k]['status'])
        for k,v in by_id.items() if k in consolidated and v[0]['status']!=consolidated[k]['status']],
    source_not_consolidated=sorted(set(by_id)-set(consolidated)),
    consolidated_not_source=sorted(set(consolidated)-set(by_id)),
    consolidated_duplicate_ids=[k for k,v in collections.Counter(r['id'] for r in consolidated_rows).items() if v>1],
    coverage=coverage, leads=leads,
    bibliography_entries=len(bib),
    duplicate_bibliography_keys=[k for k,v in collections.Counter(m.group(1) for m in starts).items() if v>1],
    bibliography_without_verification_tag=[k for k,v in bib.items() if not(v['verified'] or v['unverified'])],
    unverified_bibliography=[k for k,v in bib.items() if v['unverified']],
    cited_keys_missing_from_bibliography={k:v for k,v in cites.items() if k!='*' and k not in bib},
    unresolved_phrase_hits=stale)
(ROOT/'records/A_final_catalog_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print('STATEMENTS',len(statements),'unique',len(by_id),'assembled',len(built_manifest))
for key in ['source_not_assembled','assembled_not_source','duplicate_statement_ids',
        'duplicate_equation_tags','duplicate_labels','missing_author_metadata',
        'metadata_without_current_statement','duplicate_author_metadata','semantic_status_mismatches',
        'unclassified_source_statuses','consolidated_source_status_mismatches',
        'source_not_consolidated','consolidated_not_source','consolidated_duplicate_ids',
        'duplicate_bibliography_keys','bibliography_without_verification_tag',
        'unverified_bibliography','cited_keys_missing_from_bibliography','unresolved_phrase_hits']:
    print(key+':',json.dumps(result[key],ensure_ascii=False))
print('PROMPT COVERAGE', {k:len(v) for k,v in coverage.items()})
print('LEAD COVERAGE',leads)
print('BIBLIOGRAPHY',len(bib))
