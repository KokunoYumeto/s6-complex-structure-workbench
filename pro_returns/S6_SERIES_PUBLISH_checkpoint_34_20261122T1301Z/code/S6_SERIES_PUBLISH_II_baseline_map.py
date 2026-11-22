#!/usr/bin/env python3
"""Bind all source structure to baseline SyncTeX without reading PDF/proof text."""
from pathlib import Path
import bisect,collections,datetime,gzip,hashlib,importlib.util,json,re
import fitz
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'agents/ii_infra';BUILD=ROOT/'build/II_baseline'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load_module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
pack=load_module('packet_tools',ROOT/'code/S6_SERIES_PUBLISH_II_packets.py')
syn=load_module('synctex',ROOT/'code/S6_SERIES_PUBLISH_synctex_batch.py')
source=OUT/'S6_SERIES_PUBLISH_II_original_source_embargoed.tex';transport=OUT/'S6_SERIES_PUBLISH_II_pdftex_baseline.tex'
s=source.read_text();t=transport.read_text();offset=t[:t.index(r'\begin{document}')].count('\n')-s[:s.index(r'\begin{document}')].count('\n')
assert s[s.index(r'\begin{document}'):]==t[t.index(r'\begin{document}'):]
pdf=BUILD/(transport.stem+'.pdf');sync=BUILD/(transport.stem+'.synctex.gz');logpath=BUILD/(transport.stem+'.log');auxpath=BUILD/(transport.stem+'.aux')
structure=json.loads((OUT/'S6_SERIES_PUBLISH_II_structure_metadata.json').read_text())
raw=gzip.open(sync,'rt').read().splitlines();inputs={}
for line in raw:
 m=re.match(r'Input:(\d+):(.*)',line)
 if m:inputs[int(m[1])]=m[2]
tags=[k for k,v in inputs.items() if Path(v).resolve()==transport.resolve()];assert len(tags)==1;tag=tags[0]
page=None;line_pages=collections.defaultdict(set)
for line in raw:
 m=re.match(r'\{(\d+)$',line)
 if m:page=int(m[1]);continue
 if line.startswith('}'):page=None;continue
 m=re.match(r'[\[\(hvgkx$!r]\s*(\d+),(\d+)(?:,\d+)?:',line)
 if m and int(m[1])==tag and page:line_pages[int(m[2])].add(page)
keys=sorted(line_pages)
def span_pages(a,b):
 return sorted({p for k in keys[bisect.bisect_left(keys,a+offset):bisect.bisect_right(keys,b+offset)] for p in line_pages[k]})
aux={}
for m in re.finditer(r'\\newlabel\s*(?=\{)',auxpath.read_text()):
 vals,_=pack.read_args(auxpath.read_text(),m.end(),2);body=vals[1];v=[];i=0
 while i<len(body):
  while i<len(body) and body[i].isspace():i+=1
  if i>=len(body):break
  x,i=pack.argument(body,i);v.append(x)
 if len(v)>1:aux[vals[0]]={'printed_number':v[0],'printed_page':v[1]}
with syn.Scanner(pdf) as scanner:
 for row in structure['statements']:
  row['baseline_start_line']=row['start_line']+offset;row['baseline_end_line']=row['end_line']+offset
  row['exact_synctex_record_pages']=span_pages(row['start_line'],row['end_line'])
  row['start_query_pages']=scanner.pages(transport,row['baseline_start_line'])
  row['end_query_pages']=scanner.pages(transport,row['baseline_end_line'])
  row['aux']=aux.get(row['owner'],{})
  for proof in row['proofs']:
   proof['exact_synctex_record_pages']=span_pages(proof['start_line'],proof['end_line'])
   proof['start_query_pages']=scanner.pages(transport,proof['start_line']+offset)
   proof['end_query_pages']=scanner.pages(transport,proof['end_line']+offset)
 for h in structure['headings']:h['baseline_query_pages']=scanner.pages(transport,h['line']+offset)
 for label,row in structure['labels'].items():
  row['baseline_line']=row['line']+offset;row['baseline_query_pages']=scanner.pages(transport,row['baseline_line']);row['aux']=aux.get(label,{})
doc=fitz.open(pdf);pages=len(doc);doc.close();log=logpath.read_text(errors='replace')
diagnostics={
 'tex_errors':len(re.findall(r'^!',log,re.M)),
 'overfull_hboxes':len(re.findall(r'Overfull \\hbox',log)),
 'overfull_vboxes':len(re.findall(r'Overfull \\vbox',log)),
 'underfull_hboxes':len(re.findall(r'Underfull \\hbox',log)),
 'underfull_vboxes':len(re.findall(r'Underfull \\vbox',log)),
 'undefined_references':len(re.findall(r'Reference .*? undefined',log)),
 'undefined_citations':len(re.findall(r'Citation .*? undefined',log)),
 'missing_characters':len(re.findall(r'Missing character:',log)),
 'missing_fonts':len(re.findall(r'Font .*?not found|font .*?not loadable',log)),
 'multiply_defined':len(re.findall(r'multiply defined',log)),
 'duplicate_destinations':len(re.findall(r'destination with the same identifier',log)),
 'rerun_warnings':len(re.findall(r'Rerun to get|Label\(s\) may have changed',log))}
warnings=[]
for m in re.finditer(r'(Overfull|Underfull) \\([hv])box(?: \(([^\n]+)\))?(?:[^\n]*?lines? (\d+)(?:--(\d+))?)?',log):
 warnings.append({'kind':m[1],'box':m[2],'severity':m[3],'baseline_line_start':m[4],'baseline_line_end':m[5]})
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_path':str(source.relative_to(ROOT)),'source_sha256':sha(source),
 'transport_path':str(transport.relative_to(ROOT)),'transport_sha256':sha(transport),'document_body_byte_identical':True,'document_line_offset':offset,
 'pdf':str(pdf.relative_to(ROOT)),'pdf_sha256':sha(pdf),'pages':pages,'engine':'pdfLaTeX','passes':3,'shell_escape':False,
 'synctex_sha256':sha(sync),'aux_sha256':sha(auxpath),'log_sha256':sha(logpath),'diagnostics':diagnostics,'box_warning_metadata_only':warnings,
 'statement_environments':len(structure['statements']),'proof_environments':len(structure['proofs']),'headings':len(structure['headings']),
 'labels':len(structure['labels']),'source_lines_with_direct_synctex_records':len(keys),'page_map_scope':'Direct SyncTeX records for every source line represented in the PDF plus complete statement/proof ranges, heading anchors and all labels. Nearest-line queries are identified separately. No PDF page or target proof was visually read.',
 'certified':False,'page_reading_credit':0,'mathematical_events_added':0}
structure.update({'baseline_receipt':receipt,'direct_synctex_line_pages':{str(k-offset):sorted(v) for k,v in sorted(line_pages.items())}})
p=OUT/'S6_SERIES_PUBLISH_II_baseline_structure_pages.json';assert not p.exists();p.write_text(json.dumps(structure,ensure_ascii=False,indent=2)+'\n')
receipt['complete_structure_page_map']=str(p.relative_to(ROOT));receipt['complete_structure_page_map_sha256']=sha(p)
p=OUT/'S6_SERIES_PUBLISH_II_baseline_diagnostics.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
