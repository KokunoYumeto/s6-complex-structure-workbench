#!/usr/bin/env python3
"""Reproducible bounded searches for the eleven cp36 main statements."""
from pathlib import Path
import csv,hashlib,json,re,datetime
import fitz

ROOT=Path(__file__).resolve().parents[2]
MAT=Path('/workspace/scratch/ae06852560d6/materials/S6_08_PAPERS_5_literature')
groups={
 'endpoint':['centralizer','linearization','endpoint','pair-core-linearization','full-automorphisms','exact-period','intrinsic-fibration','Mordell'],
 'fan_return':['Eells','Kuiper','mapping torus','mapping class','homotopy sphere','exotic','flop','triangulation','prism'],
 'source':['IV^*','IV^{*}','E_6','III','I_3','OS45','OS49','discriminant','Mordell','collision'],
 'literal':['8l+5','8\\ell+5','71','6912','2187','48 punctures','sixteen','twenty-eight','degree-six','order-three'],
}
row_groups={
 'night:P3K.109':['endpoint','source'], 'night:P3K.110':['endpoint','source'],
 'night:P3K.111':['fan_return','source','literal'], 'night:P3K.112':['fan_return','literal'],
 'night:P3K.113':['endpoint','source'], 'night:P3K.114':['endpoint','source'],
 'night:P3K.115':['endpoint','fan_return','literal'], 'night:P3K.116':['source','literal'],
 'night:P3K.117':['fan_return','source','literal'], 'night:P3K.118':['endpoint','fan_return','source'],
 'night:P3K.119':['source','endpoint','literal']}
sources=[]
pdf=MAT/'original/AC26_original_manuscript.pdf'
doc=fitz.open(pdf)
sources.append((pdf,[(f'PDF page {i+1}, text line {j+1}',line) for i,p in enumerate(doc) for j,line in enumerate(p.get_text().splitlines())]))
# Every supplied TeX paper, including full nested source versions, is searched.
for p in sorted((MAT/'papers').rglob('*.tex')):
 sources.append((p,[(f'line {i+1}',line) for i,line in enumerate(p.read_text(errors='replace').splitlines())]))
logs=[]
for p,lines in sources:
 queries={}
 for group,terms in groups.items():
  queries[group]={}
  for term in terms:
   hits=[{'locator':loc,'text':text[:1200]} for loc,text in lines if term.casefold() in text.casefold()]
   queries[group][term]={'count':len(hits),'hits':hits}
 logs.append({'path':str(p),'relative_material_path':str(p.relative_to(MAT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'queries':queries})
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation',
 'method':'Fresh literal case-insensitive searches of original PDF extraction and every attached TeX paper. No hit count is a claim of global literature absence. Relevant original passages were opened and compared in renewed_credit_comparison.md.',
 'row_query_groups':row_groups,'groups':groups,'sources':logs}
out=ROOT/'analysis/continuation_IV/renewed_credit_searches.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sources':len(logs),'rows':len(row_groups),'source_term_searches':len(logs)*sum(map(len,groups.values())),'path':str(out)}))
