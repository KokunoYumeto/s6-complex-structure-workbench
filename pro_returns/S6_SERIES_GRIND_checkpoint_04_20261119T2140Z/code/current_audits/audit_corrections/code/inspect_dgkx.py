from pathlib import Path
import re, json
base=Path(__file__).resolve().parents[3]/'S6_SERIES_GRIND_source'/'S6_GRIND_6_literature'/'papers'
result={}
for version in [1,2]:
 p=base/f'arXiv_2610.00250v{version}_Du_Guo_Kusakabe_Xie.tex'
 s=p.read_text()
 headings=[{'line':s.count('\n',0,m.start())+1,'level':m.group(1),'title':m.group(2)} for m in re.finditer(r'\\(section|subsection)\*?\{([^\n]+)',s)]
 terms={term:[s.count('\n',0,m.start())+1 for m in re.finditer(re.escape(term),s)] for term in ['Kuranishi','miniversal','p2:thm:exact-period','p2:thm:kuranishi-aut','(1,1,1,0)','Aut(X_a)']}
 result[str(version)]={'source':str(p),'headings':headings,'terms':terms}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
