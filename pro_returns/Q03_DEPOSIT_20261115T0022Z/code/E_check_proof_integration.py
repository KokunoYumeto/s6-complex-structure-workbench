#!/usr/bin/env python3
"""Independent consistency checks for the assembled Q03 mathematical text.

Run from any directory. Reads each artifact once, records the exact hashes,
and compares the post, reviewed proof extract, dependency concordance, and CSV.
No source artifact is modified. The JSON output is printed on standard output.
"""
from pathlib import Path
from io import StringIO
from collections import Counter
import csv
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
paths={
 'post':'Q03_DEPOSIT_post.tex',
 'results':'Q03_DEPOSIT_results.csv',
 'reviewed_extract':'work/B_proof_revised.tex',
 'source_map':'code/C_dependency_source_map.json',
 'record':'work/record.json',
}
data={k:(ROOT/p).read_text() for k,p in paths.items()}
hashes={k:hashlib.sha256(s.encode()).hexdigest() for k,s in data.items()}
post=data['post']
expected_ids=[f'{s}.{i}' for s,n in [(2,10),(3,7),(4,5),(5,5),(6,5),(7,3),(8,5),(9,4)] for i in range(1,n+1)]


def argument(s,p):
    assert s[p]=='{'
    depth=1
    j=p+1
    while depth:
        if s[j] in '{}' and s[j-1]!='\\':depth+=1 if s[j]=='{' else -1
        j+=1
    return s[p+1:j-1],j


def statement_rows(s):
    result=[]
    for mm in re.finditer(r'\\begin\{(numbered(?:up)?)\}\{([^{}]+)\}\{([0-9.]+)\}',s):
        title,p=argument(s,mm.end())
        end=s.index(r'\end{'+mm.group(1)+'}',p)
        nxt=end+len(r'\end{'+mm.group(1)+'}')
        um=re.match(r'\s*\\uses',s[nxt:])
        assert um,('missing Uses',mm.group(3))
        uses,_=argument(s,nxt+um.end())
        result.append({'id':mm.group(3),'kind':mm.group(2),'title':title,
                       'statement':s[p:end].strip(),'uses':uses})
    return result

rows=statement_rows(post)
ids=[r['id'] for r in rows]
assert ids==expected_ids,(ids,expected_ids)
csvrows=list(csv.DictReader(StringIO(data['results'])))
counts=Counter(r['id'] for r in csvrows)
assert len(csvrows)==47 and all(v==1 for v in counts.values())
extra=['Cited result 1','Theorem A / supplied-return 1.1','Theorem B']
assert set(counts)==set(expected_ids+extra)
csvmap={r['id']:r for r in csvrows}
for r in rows:
    c=csvmap[r['id']]
    assert c['statement']==r['kind']+' '+r['id']+' ('+r['title']+').\n'+r['statement'],('CSV statement',r['id'])
    assert c['depends_on']==r['uses'],('CSV dependencies',r['id'])
    assert c['status']==('definition checked' if r['kind']=='Definition' else 'proved as stated')

# Compare all of Sections 2--8 after the recorded removal of two obsolete
# descriptive proof headings and the explicit standing m>=3 scope in 8.5.
# This comparison includes unnumbered prose.
start=post.index(r'\section{Foundations, descriptions, and the finite search}')
end=post.index(r'\section{Correctness and running time}')
actual=post[start:end].strip()
reviewed=data['reviewed_extract'].strip().replace(
    "\\begin{proof}[Proof (step layout of the format; the argument is the answer's)]",r'\begin{proof}')
old_scope=r'Every full schedule of \(J\) on \(m\) machines admits a hierarchy'
new_scope=r'For \(m\geq3\), every full schedule of \(J\) on \(m\) machines admits a hierarchy'
assert reviewed.count(old_scope)==1
reviewed=reviewed.replace(old_scope,new_scope)
assert actual==reviewed,'Sections 2--8 differ beyond the explicitly recorded m>=3 clarification in 8.5.'
assert r"$x_K$ be the least-rank job of $K\cap W'$." in actual

# Independently parse the actual typeset dependency-table rows.
table_rows={}
for line in post.splitlines():
    mm=re.match(r'^(Lemma|Proposition|Theorem|Corollary|Definition) (\d+\.\d+) & (.*?) & (.*?) & (.*?)\\\\\[3pt\]$',line)
    if mm:
        assert mm.group(2) not in table_rows
        table_rows[mm.group(2)]={'kind':mm.group(1),'source':mm.group(3),'uses':mm.group(4),'delta':mm.group(5)}
assert set(table_rows)==set(expected_ids)
source_map={r['q03_id']:r for r in json.loads(data['source_map'])}
assert set(source_map)==set(expected_ids)
for r in rows:
    table=table_rows[r['id']]
    assert table['kind']==r['kind'] and table['uses']==r['uses'],('table/Uses',r['id'])
    sm=source_map[r['id']]
    actualsource=table['source'].replace(r'\allowbreak ','')
    actualsource=re.sub(r'\\textsf\{([^{}]*)\}',r'\1',actualsource)
    expectedsource=sm['source_display']+('; '+sm['source_label'] if sm['source_label'] else ' (prose)')
    assert actualsource==expectedsource,('source counterpart',r['id'],actualsource,expectedsource)
    c=csvmap[r['id']]
    for item in (sm['source_display'],sm['source_locator'],sm['note']):assert item in c['notes']

# Every direct named result in a Uses line is already available. Displayed
# definitions such as (5.3) are standing data, not named-result invocations.
def named_refs(s):
    refs=set()
    for match in re.finditer(r'\b(?:Lemmas?|Theorems?|Propositions?|Corollar(?:y|ies)|Definitions?)\s+([0-9.,\s-]+(?:and[0-9.,\s-]+)?)',s):
        seq=match.group(1)
        for ran in re.finditer(r'(\d+)\.(\d+)--(\d+)\.(\d+)',seq):
            a,b,c,d=map(int,ran.groups())
            assert a==c
            refs.update(f'{a}.{v}' for v in range(b,d+1))
        refs.update(re.findall(r'\d+\.\d+',seq))
    return refs
for r in rows:
    refs=named_refs(r['uses'])
    for ident in refs:
        assert ident in expected_ids and tuple(map(int,ident.split('.')))<tuple(map(int,r['id'].split('.'))),('forward Uses',r['id'],ident)

# Main theorem counts and cross-references.
assert len(re.findall(r'\\begin\{maintheorem\}',post))==2
assert len(re.findall(r'\\begin\{cited\}',post))==1
assert set(csvmap['Theorem A / supplied-return 1.1']['depends_on'].split(';'))=={'9.1','9.2','9.3'}
assert set(csvmap['Theorem B']['depends_on'].split(';'))=={'2.9','7.3','8.2','8.3','8.4'}
record=json.loads(data['record'])
assert record['statements_in_proof']==44
assert record['claim_status']=='proved'
assert '60m^2+129m+2' in record['statement_plain']
assert '60m^2+129m+1' in record['statement_plain']

# Numeric state-bound renaming: every uppercase S token in Section 9 math must
# be the declared calligraphic S. Check juxtaposed products as well.
section9=post[end:post.index(r'\fixedhead{Limits and open points}',end)]
mathsegments=re.findall(r'(?s)(?<!\\)\$(?!\$)(.*?)(?<!\\)\$|\\\((.*?)\\\)|\\\[(.*?)\\\]',section9)
plain_s=[]
for pieces in mathsegments:
    seg=next((p for p in pieces if p),'')
    reduced=seg.replace(r'\mathcal{S}','')
    if 'S' in reduced:plain_s.append(seg)
assert not plain_s,('unconverted numeric S in math',plain_s)

warnings=[]
if table_rows['8.1']['delta'].endswith('---'):
    warnings.append('Dependency-table row 8.1 has an empty capacity-transfer explanation (Unchanged argument: ---); replace by the concrete predicate/carry-count relationship.')
if re.search(r'Final PDF: 0 pages',post):
    warnings.append('Final PDF page count is still the temporary zero placeholder; root is performing the final build/render pass.')

print(json.dumps({
 'date':'2026-11-15','checker':'GPT-6 Astra (OpenAI), effort ChatGPT Pro mode',
 'input_sha256':hashes,
 'checks':{
  'numbered_statements':44,'csv_rows':47,'rows_missing_or_duplicated':0,
  'csv_statement_mismatches':0,'csv_dependency_mismatches':0,
  'dependency_table_rows':44,'table_uses_mismatches':0,
  'source_counterpart_mismatches':0,'source_note_mismatches':0,
  'forward_named_uses':0,'reviewed_sections_2_to_8_equal_after_recorded_scope_clarification':True,
  'least_rank_choice_domain_explicit':True,
  'main_theorems':2,'cited_results':1,
  'unconverted_numeric_state_symbols':0,
 },
 'warnings':warnings,
 'verdict':'All mathematical integration and cross-file consistency assertions passed.'
},indent=2))
