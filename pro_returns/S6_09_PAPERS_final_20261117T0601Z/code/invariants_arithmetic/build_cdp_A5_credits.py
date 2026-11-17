from pathlib import Path
import csv,json,re,unicodedata
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/invariants_arithmetic'
audits=json.loads((OUT/'cdp_A5_independent_audit.json').read_text())
specs=json.loads((OUT/'credit_search_log.json').read_text())['sources']
refs={x['citation_key']:x for x in json.loads((OUT/'references_verified.json').read_text())}
def fold(s):
 s=''.join(c for c in unicodedata.normalize('NFKD',s).lower() if not unicodedata.combining(c))
 return re.sub(r'[\\{}"\'`~-]','',s)
data={k:list(map(fold,(ROOT/v['index_source']).read_text(errors='replace').splitlines())) for k,v in specs.items()}
terms=['conductor','normalization','ruled','cusp','tacnode','triple','symbolic','genus','triangulation','metabelian','spherical']
rows=[];logs=[]
for a in audits:
 row=dict(source_run=a['source_run'],source_id=a['source_id'],paper='II',reviewer=a['own_check'])
 for key in ['AC26','E26','DGKX_v1']:
  hits={term:[i+1 for i,line in enumerate(data[key]) if fold(term) in line] for term in terms}
  logs.append(dict(source_id=a['source_id'],source=key,index_source=specs[key]['index_source'],terms=hits))
  val=dict(status='not_found_in_checked_scope',full_statement_found=False,source=specs[key]['local_source'],source_sha256=specs[key]['source_sha256'],actual_reading_scope=specs[key]['opened_locator'],terms_searched=terms,search_record='work/invariants_arithmetic/cdp_A5_credit_search.json#'+a['source_id']+'|'+key,locator='',relation='This exact general conductor/ruled-surface/local-exclusion statement was not found in the listed original-source scopes and executed whole-text terms. No absence is asserted in unread material or in all literature.')
  if a['source_id']=='A.5.16' and key in ['AC26','DGKX_v1']:
   val.update(status='found',kind='special_example_only',locator='AC26 Lemma9.12 pp.71–74 and Proposition9.13 pp.74–76' if key=='AC26' else 'DGKXv1 p2:lem:cusp-normalization-resolution and p2:prop:cusp-structure-cup lines8768–8877',relation='The periodic hexagonal cusp with rational dP6 normalization and structure dimensions(1,2,1) is a known example. The general rational-normalization topology, coefficient-map injectivity, off-conductor correction and boundary classifications of A5.16 are not stated there.')
  row['found_in_'+key]=val
 matches=[]
 for k in a['reference_dependencies']:
  r=refs[k];matches.append(dict(citation_key=k,locator=r['opened_locator'],status=r['status'],kind='operative_general_input',full_statement_found=False,relation='Opened primary theorem used by the proof, not a claim that the complete specialized row is stated in this reference.'))
 other=[]
 for key,spec in specs.items():
  if key in ['AC26','E26','DGKX_v1']:continue
  hits={term:[i+1 for i,line in enumerate(data[key]) if fold(term) in line] for term in terms}
  logs.append(dict(source_id=a['source_id'],source=key,index_source=spec['index_source'],terms=hits))
  other.append(dict(citation_key=spec['citation_key'],actual_reading_scope=spec['opened_locator']))
 row['found_elsewhere']=dict(status='found' if matches else 'not_found_in_checked_scope',full_statement_found=False,matches=matches,other_sources_searched=other,terms_searched=terms,search_record='work/invariants_arithmetic/cdp_A5_credit_search.json',relation='General operative inputs are credited; exact general rows were not found in the nine specified additional source scopes. These bounded comparisons make no worldwide novelty assertion.')
 rows.append(row)
 a['credit_comparison_record']='work/invariants_arithmetic/cdp_A5_credit_comparison.json#'+a['source_id']
(OUT/'cdp_A5_credit_comparison.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
(OUT/'cdp_A5_credit_search.json').write_text(json.dumps(dict(method='Executed folded literal searches; semantic comparisons bounded by each actual reading scope.',records=logs),indent=2,ensure_ascii=False)+'\n')
(OUT/'cdp_A5_independent_audit.json').write_text(json.dumps(audits,indent=2,ensure_ascii=False)+'\n')
with (OUT/'cdp_A5_independent_audit.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(audits[0]));w.writeheader()
 for r in audits:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
print(f'{len(rows)} credit rows; {len(logs)} executed source/row searches')
