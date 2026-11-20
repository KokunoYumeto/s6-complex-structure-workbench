"""Use opened surgery/classical invariant results with exact transports."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
p=R/'parts/IV.body.linked.tex';t=p.read_text();records=[]
at=t.index('\\label{night:P3F.22}');a=t.index('\\begin{proof}',at);b=t.index('\\end{proof}',a)+len('\\end{proof}')
old=t[a:b];new=(R/'audit_corrections/IV_F22_cited_specialization.tex').read_text().strip()
labels=re.findall(r'\\label\{([^}]+)\}',old)
assert len(labels)==4
pieces=new.split('\\item ');assert len(pieces)==5
new=pieces[0]+''.join('\\item \\label{'+label+'}'+piece for label,piece in zip(labels,pieces[1:]))
assert set(re.findall(r'\\tag\{([^}]+)\}',old))==set(re.findall(r'\\tag\{([^}]+)\}',new))
t=t[:a]+new+t[b:]
records.append({'label':'night:P3F.22','old':old,'new':new,'preserved_heading_labels':labels,'reason':'Apply opened Jiang Lemma3.5 Case2 with the exact source substitution; retain the collar, extending quaternionic map, surgery boundary orientation and characteristic normalization.'})
at=t.index('\\label{night:P3F.24}');a=t.index('The rational relative-to-absolute',at);b=t.index(' Both values for the product are zero',a)
old=t[a:b];new=(R/'audit_corrections/IV_F24_known_invariant.tex').read_text().strip()
t=t[:a]+new+t[b:];records.append({'label':'night:P3F.24','old':old,'new':new,'reason':'Cite the opened classical invariant with the exact p_W=p1/2 and factor28 transport; retain all ball/collar constructions and both spin structures.'})
p.write_text(t)
(R/'analysis/IV_surgery_citation_changes.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'changes':len(records),'characters_removed':sum(len(r['old'])-len(r['new']) for r in records),'preserved_heading_labels':labels}))
