"""Snapshot the six actual standalone deliverables without overwriting them.

This records production state and never awards proof-reading credit.
"""
from pathlib import Path
import argparse,hashlib,json,re,subprocess
P=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('number',type=int);args=ap.parse_args()
records=[]
for paper in ['I','II','III','IV','V','VI']:
 base=P/'build/standalone'/paper
 assembly=json.loads((base/'assembly_record.json').read_text())
 rec={'paper':paper,'source_directory':str(base.relative_to(P)),'status':'INCOMPLETE; remaining proof/source and final delivery reviews are separately recorded','assembly_grants_no_check':True}
 for ext in ('tex','pdf'):
  path=P/f'S6_10_PAPERS_{paper}.{ext}'
  before=path.stat();data=path.read_bytes();after=path.stat()
  assert (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns),path
  sha=hashlib.sha256(data).hexdigest()
  assert sha==assembly[ext+'_sha256'],(paper,ext,'canonical file differs from its successful assembly')
  rec[ext]={'path':path.name,'source':str((base/path.name).relative_to(P)),'size_bytes':len(data),'sha256':sha}
 info=subprocess.run(['pdfinfo',str(P/f'S6_10_PAPERS_{paper}.pdf')],capture_output=True,text=True,check=True).stdout
 rec['pages']=int(re.search(r'^Pages:\s*(\d+)',info,re.M).group(1))
 log=(base/f'S6_10_PAPERS_{paper}.log').read_text(errors='replace')
 h=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
 v=[float(x) for x in re.findall(r'Overfull \\vbox \(([0-9.]+)pt too high\)',log)]
 rec['log']={'sha256':hashlib.sha256(log.encode()).hexdigest(),'overfull_hbox_above_2pt':sum(x>2 for x in h),'overfull_vbox_above_2pt':sum(x>2 for x in v),'missing_characters':len(re.findall('Missing character:',log)),'font_warnings':len(re.findall(r'(?:LaTeX Font Warning|fontspec Warning)',log)),'undefined_reference_messages':len(re.findall(r'LaTeX Warning: Reference',log)),'undefined_citation_messages':len(re.findall(r'Package natbib Warning: Citation',log)),'multiply_defined_labels':len(re.findall(r'multiply defined',log))}
 rec['external_reference_count']=len(assembly['cross_reference_changes']);rec['cited_key_count']=len(assembly['citations'])
 records.append(rec)
dest=P/f'analysis/checkpoint{args.number:02d}_deliverable_snapshot.json';dest.write_text(json.dumps(records,indent=2))
print(json.dumps([{'paper':r['paper'],'pages':r['pages'],**r['log']} for r in records],indent=2))
