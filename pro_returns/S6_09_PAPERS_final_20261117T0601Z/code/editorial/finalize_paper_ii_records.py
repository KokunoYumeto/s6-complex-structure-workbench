"""Record scoped source-to-print retention and exact known-result placement.

The string comparison is an editorial retention check. Mathematical proof
checks come from the independently read source/repaired blocks and their
explicit dependency-closure records, not from this program.
"""
from pathlib import Path
import csv,json,re,hashlib
from paper_ii_transform import replace_external_I
from paper_ii_credit_annotations import KNOWN,CREDIT
D=Path(__file__).resolve().parents[2]
s=(D/'S6_09_PAPERS_II.tex').read_text()
def strip(x):
 # Cite arguments can contain newlines, so a line-based expression is
 # insufficient. Delete only balanced generated Uses macro invocations.
 while True:
  m=re.search(r'^\\Uses\{',x,re.M)
  if not m:break
  depth=1;i=m.end()
  while depth and i<len(x):
   if x[i]=='\\' and i+1<len(x) and x[i+1] in '{}':i+=2;continue
   if x[i]=='{':depth+=1
   elif x[i]=='}':depth-=1
   i+=1
  assert depth==0,'Unbalanced generated Uses argument'
  x=x[:m.start()]+x[i:]
 x=re.sub(r'\\label\{[^}]+\}','',x)
 # add_uses inserts a line after statement environments. Removing that
 # generated line may consume adjacent blank lines; compare the complete
 # retained token text with whitespace normalized, never selected excerpts.
 return re.sub(r'\s+',' ',x).strip()
core=strip(s);checks=[]
for p in sorted((D/'editorial').glob('II_cdp_*.tex')):
 expected=strip(replace_external_I(p.read_text()))
 passed=expected in core
 checks.append({'file':str(p.relative_to(D)),'normalized_block_sha256':hashlib.sha256(expected.encode()).hexdigest(),'complete_block_retained':passed})
assert len(checks)==237 and all(x['complete_block_retained'] for x in checks),[x for x in checks if not x['complete_block_retained']]
known=json.loads((D/'work/cdp_audit/known_rederivation_routing.json').read_text())
known_ids={x['source_id'] for x in known if 'PaperII' in x['route']}
assert known_ids==KNOWN|{'A.2.3','C.2.NC.1','C.2.RAT.6'},known_ids
appendix=s.index('\\section{Known source results re-derived}')
for sid in known_ids:assert s.index('\\label{cdp:st:'+sid+'}')>appendix,sid
p=D/'S6_09_PAPERS_inventory.csv'
with p.open(newline='') as f:rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
labels=set(re.findall(r'\\label\{([^}]+)\}',s))
for r in rows:
 if r['paper']!='II':continue
 assert r['printed_label'] in labels,(r['source_run'],r['source_id'])
 if r['source_run']=='S6_03_CDP' and r['source_id'] in known_ids:r['kind']='Cited/re-derived'
 if r['source_run']=='S6_02_PUSH' and r['source_id']=='E.5.1':r['kind']='Correction of input configuration; cited source retained'
 note='Final II source-to-print retention: complete normalized canonical blocks retained; exact mathematical/citation changes separately reviewed in records/II_editorial_mathematical_changes.json, II_working_supplement_root_changes.json and II_positive_credit_changes.json.'
 if note not in r['notes']:r['notes']+=' | '+note
with p.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
(D/'records/II_source_to_print_retention.json').write_text(json.dumps({'canonical_blocks':checks,'whole_known_ids':sorted(known_ids),'canonical_reading_record':'work/cdp_audit/result_audit.json','source_dependency_closure':'work/cdp_audit/dependency_closure_events.json','supplement_retention':'work/cdp_audit/working_supplement_mapping.json','method':'Literal complete normalized-block comparison after dropping generated Uses lines and aliases and normalizing whitespace; no inference of mathematical truth from this comparison.'},indent=2)+'\n')
print('II complete normalized blocks retained:',len(checks),'known statements in credited appendix:',len(known_ids))
