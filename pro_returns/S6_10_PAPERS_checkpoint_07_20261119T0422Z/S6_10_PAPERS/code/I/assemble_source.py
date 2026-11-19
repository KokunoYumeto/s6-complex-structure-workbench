"""Assemble Paper I with exact source contexts; this operation grants no checks."""
from pathlib import Path
import sys,json,csv,re,hashlib
PROJECT=Path(__file__).resolve().parents[2];ROOT=PROJECT.parents[1]
sys.path.insert(0,str(PROJECT/'code'))
from inventory_reconcile import TexIndex,commands
SOURCE=ROOT/'sources/s6_09/S6_09_PAPERS_I.tex'; idx=TexIndex(SOURCE);lines=idx.text.splitlines(keepends=True)
rows=list(csv.DictReader((PROJECT/'S6_10_PAPERS_inventory.csv').open()))
by_label={r['label']:r for r in rows if r['paper']=='I'}
# Whole intervals keep mathematical setup, displayed definitions, and notes.
# Apparatus and the long classical compendium are excluded explicitly.
intervals={
 '00_conventions':[(231,278),(25046,25259)],
 '01_periods':[(586,710),(925,1415),(5244,5398),(5709,5992),(7434,7889)],
 '02_moduli':[(279,585),(711,924),(23978,24257)],
 '03_monodromy_and_fibres':[(2010,2578),(1629,2009),(1416,1628),(10981,11441)],
 '04_hodge':[(2579,3473),(4155,4756)],
 '05_tangent':[(37241,37649),(4757,5243),(24258,24705)],
 '06_ends':[(11442,22600-1),(22600,23977)],
 '07_arithmetic':[(5399,5708),(5993,7433),(7890,8898)],
 '08_higher_multiplicities':[(3474,4154)],
 '09_integral_circle':[(10676,10980)],
 '10_interval_certificate':[(24706,25042)],
 '90_credited_appendices':[(34806,35957),(35995,36341)],
 '99_open_questions':[(8899,10675),(38209,38323)]}
# Exact exclusions remove only known/classical/duplicate proof containers.
# Statements retained as known inputs are resolved to primary citations later.
all_locations=json.loads((PROJECT/'analysis/inventory_source_index.json').read_text())
exclusions=[]
for r in rows:
 if r['paper']=='I' and r['in_compendium_only_because']:
  loc=all_locations.get(r['source_run']+':'+r['source_id'])
  if loc and loc.get('file')==str(SOURCE.relative_to(ROOT)) and loc.get('container_kind')=='statement_environment':
   exclusions.append((loc['start'],loc['end'],r))
# Deduplicate source aliases before applying replacements.
seen=set(); unique=[]
for a,b,r in exclusions:
 if (a,b) in seen:continue
 seen.add((a,b));unique.append((a,b,r))
base_offsets=[0]
for line in lines:base_offsets.append(base_offsets[-1]+len(line))
manifest=[]
for name,ranges in intervals.items():
 segments=[]
 for first,last in ranges:
  a=base_offsets[first-1];b=base_offsets[last];text=idx.text[a:b]
  edits=[]
  for x,y,r in unique:
   if a<=x and y<=b:
    # Keep an exact source locator. This is an editorial placeholder, not a
    # substitute for any retained new proof; later citation pass resolves it.
    labels=[c['value'] for c in commands(idx.text[x:y],'label')]
    placeholder='\n\\paragraph{Cited input.} '+''.join('\\label{'+q+'}' for q in labels)+'The source statement and its expanded derivation are retained in the proof compendium, Paper~I, label \\nolinkurl{'+r['label']+'}.\\par\n'
    edits.append((x-a,y-a,placeholder))
  for x,y,value in sorted(edits,reverse=True):text=text[:x]+value+text[y:]
  segments.append(text)
  manifest.append({'fragment':name,'source':str(SOURCE.relative_to(ROOT)),'line_start':first,'line_end':last,'source_sha256':idx.sha256,'excluded_containers':len(edits),'proof_check_awarded':False})
 text='\n'.join(segments)
 text=re.sub(r'% (?:BEGIN|END) [^\n]*\n','',text)
 (PROJECT/'papers/I'/f'{name}.source.tex').write_text(text)
(PROJECT/'analysis/I_assembly_manifest.json').write_text(json.dumps(manifest,indent=2))
print('Assembled',len(intervals),'whole-context source fragments,',sum((PROJECT/'papers/I'/f'{n}.source.tex').stat().st_size for n in intervals),'bytes. No proof checks awarded.')
