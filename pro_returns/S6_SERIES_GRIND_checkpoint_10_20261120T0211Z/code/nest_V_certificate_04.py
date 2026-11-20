"""Number the seven authored analytic subclaims inside P1.18 item three.

The seven original outer items and every reference to their numbers stay
fixed. Only the paragraph-heading/list presentation changes.
"""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1]
p=R/'parts/V.body.linked.tex';s=p.read_text()
a=s.index(r'\label{night:P1.18}');b=s.index(r'\end{proof}',a)
proof=s[a:b]
start=proof.index(r'\paragraph{Fresh normalization from the two finite roots.}')
end=proof.index(r'\item \textbf{The infinity value and its strict local minimum.}')
old=proof[start:end]
heads=re.findall(r'\\paragraph\{([^{}]+)\}',old);assert len(heads)==7,heads
body=re.sub(r'\\paragraph\{([^{}]+)\}',lambda m:r'\item \textbf{'+m.group(1)+'}',old)
new='\n\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n'+body+'\n\\end{enumerate}\n\n'
def project(x):
    x=re.sub(r'\\(?:paragraph|textbf)\{([^{}]+)\}',r'{\1}',x)
    x=re.sub(r'\\(?:begin|end)\{enumerate\}(?:\[[^\n]*\])?','',x)
    x=re.sub(r'\\item\b','',x)
    return re.sub(r'\s+',' ',x).strip()
assert project(old)==project(new)
result=s[:a]+proof[:start]+new+proof[end:]+s[b:]
assert re.findall(r'\\(?:tag|label)\{[^}]+\}',s)==re.findall(r'\\(?:tag|label)\{[^}]+\}',result)
p.write_text(result)
(R/'analysis/V_certificate_hierarchy_04.json').write_text(json.dumps({'label':'night:P1.18','original_outer_items_preserved':7,'new_nested_claims':heads,'old':old,'new':new,'mathematical_projection_sha256':hashlib.sha256(project(old).encode()).hexdigest(),'exact_transport':'Replace paragraph-heading style by bold item-heading style; erase the newly inserted nested list delimiters and item tokens. The seven numbered outer items and all their referring numbers are unchanged.'},indent=2)+'\n')
print(json.dumps({'outer_items_preserved':7,'nested_claims':len(heads),'projection_verified':True}))
