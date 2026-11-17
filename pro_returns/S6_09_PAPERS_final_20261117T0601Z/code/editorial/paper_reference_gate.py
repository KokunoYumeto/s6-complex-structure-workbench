"""Enumerate citation, label, and unresolved source-number issues; not a proof check."""
from pathlib import Path
import sys,re,json,collections
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables'
sys.path.insert(0,str(ROOT/'deps/python'));import bibtexparser
paper=sys.argv[1] if len(sys.argv)>1 else 'I'
s=(OUT/f'S6_09_PAPERS_{paper}.tex').read_text()
b={e.key:{x.key:x.value for x in e.fields} for e in bibtexparser.parse_string((OUT/'S6_09_PAPERS_references.bib').read_text()).entries}
cites=sorted(set(k.strip() for m in re.finditer(r'\\(?:cite\w*|nocite)(?:\[[^\]]*\])*\{([^}]+)\}',s) for k in m[1].split(',')))
labels=collections.Counter(re.findall(r'\\label\{([^}]+)\}',s));refs=set(k for m in re.finditer(r'\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}',s) for k in m[1].split(','))
raw_scope=re.sub(r'% BEGIN GENERATED (?:RESULT|PROGRAM) INDEX.*?% END GENERATED (?:RESULT|PROGRAM) INDEX','',s,flags=re.S)
r={'paper':paper,'citations':len(cites),'missing_bibliography':[k for k in cites if k not in b], 'unverified_cited':[k for k in cites if b.get(k,{}).get('verification')!='verified'], 'undefined_labels':sorted(refs-set(labels)), 'duplicate_labels':{k:v for k,v in labels.items() if v>1}, 'raw_source_numbers':[{ 'line_in_nonindex_text':raw_scope[:m.start()].count('\n')+1,'context':raw_scope[max(0,m.start()-80):m.end()+120]} for m in re.finditer(r'\b(?:FAM|PUSH|INV|MAPS|CDP|ARI|Statement|Proposition|Theorem|Lemma|Corollary|Conjecture)\s*~?\s*\(?[A-F]\.?[0-9]+\.[0-9]+',raw_scope)]}
(OUT/f'work/root/{paper}_citation_gate.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k!='raw_source_numbers'},indent=2));print('Raw source references',len(r['raw_source_numbers']))
