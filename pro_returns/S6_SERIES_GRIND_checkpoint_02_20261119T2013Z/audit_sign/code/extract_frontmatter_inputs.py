from pathlib import Path
import re,json,importlib.util
sp=importlib.util.spec_from_file_location('extract',str(Path(__file__).with_name('extract_audit_statements.py')));e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
labels=['cdp:st:A.1.1','cdp:st:B1','cdp:st:C4f','cdp:st:D.1.2','cdp:st:C.3.1','cdp:st:C5b','cdp:st:C5c','cdp:st:E6','cdp:st:E13','cdp:st:E14','cdp:st:E15','push:src:E.2.23','push:src:E.2.24','cdp:st:C.2.G.1','cdp:st:C.2.INT.3','night:P4.58','cdp:st:E12','cdp:st:E17','inv:E2.4','cdp:st:E18']
out=[]
for paper in ['II','VI']:
 s=(e.SRC/f'S6_10_PAPERS_{paper}.tex').read_text()
 for lab in labels:
  target='\\label{'+lab+'}'
  if target not in s:continue
  p=s.index(target);b=s.rfind('\\begin{',0,p);m=re.match(r'\\begin\{([^}]+)\}',s[b:]);z=s.index('\\end{'+m[1]+'}',p)+len('\\end{'+m[1]+'}')
  out.append({'label':lab,'paper':paper,'statement':e.strip_record(s[b:z])})
(e.OUT/'frontmatter_inputs.json').write_text(json.dumps(out,indent=2))
print('\n\n'.join(o['statement'] for o in out))
