from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parents[2];W=D/'work/invariants_arithmetic'
sys.path.insert(0,str(D/'code/invariants_arithmetic'))
from build_all_papers_notation import brace_group
paths={k:D/v for k,v in {'tex':'S6_09_PAPERS_III.tex','aux':'S6_09_PAPERS_III.aux','pdf':'S6_09_PAPERS_III.pdf','repairs':'records/III_course_structure_repairs.json'}.items()}
raw={k:p.read_bytes() for k,p in paths.items()};tex=raw['tex'].decode();aux=raw['aux'].decode();repair=json.loads(raw['repairs'])
labels={}
for m in re.finditer(r'\\newlabel(?=\s*\{)',aux):
 k,j=brace_group(aux,m.end());outer,j=brace_group(aux,j);groups=[];i=0
 while i<len(outer):
  if outer[i].isspace():i+=1;continue
  q,i=brace_group(outer,i);groups.append(q)
 labels[k]=groups
native=[];formal=set();new=[]
for e in repair['events']:
 if e.get('anchor') and e['reason'].startswith('Attach'):
  oldlabels=re.findall(r'\\label\{([^}]+)\}',e['after']);key=next(x for x in oldlabels if x.endswith(':'+e['anchor']));target=e['target']
  same=labels.get(key)==labels.get(target)
  native.append({'label':key,'target':target,'provenance_only':e['provenance_only'],'source_heading':e['source_heading'],'aux_values':labels.get(key),'target_aux_values':labels.get(target),'exact_aux_tuple_equal':same,'unique_tex_label':tex.count('\\label{'+key+'}')==1})
 if e['reason'].startswith('Attach the existing numbered-result label') or e['reason'].startswith('Restore the separate nowhere-zero-section proposition'):
  formal.update(re.findall(r'\\label\{([^}]+)\}',e['after']))
 if e.get('new_label'):new.append(e['new_label'])
def unit(key):
 p=tex.index('\\label{'+key+'}');beg=list(re.finditer(r'\\begin\{(theorem|lemma|proposition|corollary)\}(?:\[[^\]]*\])?',tex[:p]));m=beg[-1];tail=tex[m.end():p];env=m[1];kind=labels.get(key+'@cref',[''])[0]
 return {'label':key,'environment':env,'label_inside_own_environment':('\\end{'+env+'}') not in tail,'aux_values':labels.get(key),'cref_kind':kind,'correct_result_kind':kind.startswith('['+env+']'),'unique_tex_label':tex.count('\\label{'+key+'}')==1}
units=[unit(k) for k in sorted(formal)];newunits=[unit(k) for k in new]
assert len(native)==26,len(native)
assert len(units)==14,len(units)
assert len(newunits)==4,len(newunits)
passed=all(x['exact_aux_tuple_equal'] and x['unique_tex_label'] for x in native) and all(x['label_inside_own_environment'] and x['correct_result_kind'] and x['unique_tex_label'] for x in units+newunits)
for k,p in paths.items():assert p.read_bytes()==raw[k],f'Input changed during check: {k}'
result={'reviewer':{'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date_utc':'2026-11-17'},'scope':'Read-only actual final TeX/AUX comparison of every requested moved course anchor and new formal theorem; not a new full proof review.','input_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},'native_anchors':native,'formal_result_labels':units,'new_theorem_labels':newunits,'counts':{'native_anchors':len(native),'native_provenance_aliases':sum(x['provenance_only'] for x in native),'formal_result_labels':len(units),'new_theorems':len(newunits)},'all_checks_passed':passed}
(W/'final_course_anchor_AUX_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':passed,**result['counts'],'pdf_sha256':result['input_sha256']['pdf']}))
if not passed:sys.exit(1)
