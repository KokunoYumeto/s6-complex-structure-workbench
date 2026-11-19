"""Merge exact current source loci; never infer an unrecorded source opening."""
from pathlib import Path
import csv,json,re
P=Path(__file__).resolve().parents[1]
matches={}
def add(key,locator,scope,origin):
 matches.setdefault(key,[]).append({'locator':locator,'scope':scope,'record':origin})
f=P/'analysis/I_sources/current_source_matches.json'
for key,r in json.loads(f.read_text()).items():
 add(key,r['exact_locator'],r['scope'],str(f.relative_to(P)))
f=P/'analysis/IV/root_source_matches.json'
if f.exists():
 for key,r in json.loads(f.read_text()).items():
  add(key,r['exact_locator'],r['scope'],str(f.relative_to(P)))
f=P/'analysis/IV/root_cusp_primary_matches.json'
if f.exists():
 for key,r in json.loads(f.read_text()).items():
  add(key,r['exact_locator'],r['scope'],str(f.relative_to(P)))
f=P/'analysis/IV_product_batch/source_reads.json'
if f.exists():
 for r in json.loads(f.read_text()):
  if r.get('status','').startswith('opened and matched'):
   add(r['source_key'],r['locus'],r['scope'],str(f.relative_to(P)))
   for alias in r.get('aliases',[]):
    add(alias,r['locus'],r['scope']+' Same-work identity: '+r.get('alias_evidence','')+' No additional independent reading credit.',str(f.relative_to(P)))
f=P/'records/sign_source_reads.tsv'
for r in csv.DictReader(f.open(),delimiter='\t'):
 if r['status'].startswith('opened and matched'):
  add(r['source_key'],r['locus'],r['scope'],str(f.relative_to(P)))
f=P/'analysis/II_independent_source_reads.json'
if f.exists():
 for r in json.loads(f.read_text()):
  if r['status'].startswith('opened and matched'):
   add(r['source_key'],r['locus'],r['scope'],str(f.relative_to(P)))
   if r['source_key']=='BS76':
    add('BS76push',r['locus'],r['scope']+' Same-book alias, no additional reading credit.',str(f.relative_to(P)))
f=P/'analysis/IV_independent_source_reads.json'
if f.exists():
 for r in json.loads(f.read_text()):
  if r['status'].startswith('opened and matched'):
   add(r['source_key'],r['locus'],r['scope'],str(f.relative_to(P)))
f=P/'analysis/II_remaining_source_reads.json'
if f.exists():
 for r in json.loads(f.read_text()):
  if r['status'].startswith('opened and matched'):
   add(r['source_key'],r['locus'],r['scope'],str(f.relative_to(P)))
f=P/'analysis/III_references_opened.json'
for r in json.loads(f.read_text()):
 if r.get('status','').startswith('verified'):
  add(r['key'],r['locator'],r['scope'],str(f.relative_to(P)))
f=P/'analysis/IV/paper_I_KKN/current_reference_audit.json'
for r in json.loads(f.read_text()):
 add(r['bib_key'],'; '.join(r['opened_locators']),r['finding'],str(f.relative_to(P)))
for paper in ['IV','V']:
 f=P/'analysis'/paper/'reference_checks.json'
 for r in json.loads(f.read_text()):
  if not r.get('bib_key_match_scope'):continue
  for key in [r['bib_key']]+r.get('bib_aliases',[]):
   add(key,r['locator'],r['check']+' '+r['bib_key_match_scope'],str(f.relative_to(P)))
f=P/'analysis/bibliography_aliases.json'
if f.exists():
 for key,r in json.loads(f.read_text()).items():
  for reading in list(matches.get(r['canonical'],[])):
   add(key,reading['locator'],reading['scope']+' Bibliographic identity: '+r['identity_evidence']+' This is the same reading event, with no additional independent credit.',str(f.relative_to(P)))
f=P/'analysis/sign_bibliography_alias_evidence.json'
if f.exists():
 for r in json.loads(f.read_text())['mappings']:
  for reading in list(matches.get(r['current_record_key'],[])):
   add(r['bibliography_key'],reading['locator'],reading['scope']+' Bibliographic identity: '+r['evidence']+' This is the same reading event, with no additional independent credit.',str(f.relative_to(P)))
def tex(s):
 table={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','_':r'\_','#':r'\#',
        '{':r'\{','}':r'\}','$':r'\$','^':r'\textasciicircum{}','~':r'\textasciitilde{}',
        '≥':r'$\geq$','≤':r'$\leq$'}
 return ''.join(table.get(c,c) for c in s)
def replacefield(block,key,value):
 m=re.search(r'(?m)^\s*'+key+r'\s*=\s*\{',block)
 if not m:
  prefix=block.rstrip()[:-1].rstrip()
  if not prefix.endswith(','):prefix+=','
  return prefix+f'\n  {key} = {{{value}}},\n}}\n'
 start=m.end();depth=1;end=start
 while depth:
  c=block[end]
  if c=='{' and (end==0 or block[end-1]!='\\'):depth+=1
  if c=='}' and (end==0 or block[end-1]!='\\'):depth-=1
  end+=1
 return block[:start]+value+block[end-1:]
f=P/'S6_10_PAPERS_references.bib';parts=re.split(r'(?m)(?=^@)',f.read_text());seen=set();out=[]
for block in parts:
 m=re.match(r'@\w+\{([^,]+),',block)
 if m and m.group(1) in matches:
  key=m.group(1);seen.add(key)
  notes=['Verified in this writing on 18 November 2026 at these loci only.']
  notes.extend(x['locator']+'. Scope: '+x['scope'] for x in matches[key])
  block=replacefield(block,'verification','verified at listed scope')
  block=replacefield(block,'note',tex(' '.join(notes)))
 out.append(block)
f.write_text(''.join(out))
(P/'analysis/current_bibliography_verification.json').write_text(json.dumps({'matched_keys':sorted(seen),'unmatched_record_keys':sorted(set(matches)-seen),'records':matches},indent=2))
print('Verified bounded source entries',len(seen),'unmatched alias records',sorted(set(matches)-seen))
