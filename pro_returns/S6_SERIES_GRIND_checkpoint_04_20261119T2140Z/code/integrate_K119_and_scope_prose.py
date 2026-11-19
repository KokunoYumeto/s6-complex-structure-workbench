"""Apply K119's complete-scope review and remove receiving-history prose."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1];records=[]
iv=R/'parts/IV.body.linked.tex';t=iv.read_text()
for p in json.loads((R/'audit_paper_i/iv_os45/K119_patches.json').read_text()):
    assert t.count(p['old'])==1,p['id']
    t=t.replace(p['old'],p['new'],1);records.append(p)
old='\\StatementRecord{night:P3K.119}{open}'
assert t.count(old)==1;t=t.replace(old,'\\StatementRecord{night:P3K.119}{proved}')
at=t.index('\\label{night:P3K.119}')
a=t.index('\\par\\medskip\\noindent\\textbf{Exact construction and audit dependencies.}',at)
b=t.index('\n% End expanded verified cp36 input',a)
old=t[a:b]
new=r'''\par\medskip\noindent\textbf{Source maps and exact calculation.}\par
The source, point line, five marked monodromy matrices and primitive
fillings are those of \cref{night:P3K.116}; the prescribed-fan sphere
transport uses the common blowup and ruling maps of \cref{night:P3F.35}.
The four complete arguments above retain the source, Cartier, integral,
analytic, proper-family and directed endpoint maps.

The program
\path{audit_paper_i/iv_os45/code/k119_afterreading_exact.py}, also
included under \path{code/current_audits/}, reconstructs the four
selected-zero choices and all twenty inverse-transpose matrices.
It computes the full $20\times20$ raw/based maps and their integral
inverses, the $20\times36$ cone boundary, the primitive image
coordinates and the degree-one contraction. Its 175 exact checks
also verify the original source/node and chronological Miller
identities, the full Laurent solve and the noncommutative endpoint
word. The output is
\path{audit_paper_i/iv_os45/output/k119_afterreading_exact.json}.
'''
t=t[:a]+new+t[b:]
records.append({'id':'IV-K119-computation','old':old,'new':new,'reason':'Name the fresh supplied program, full inputs and results; move historical file manifests to check provenance.'})
iv.write_text(t)

for paper in ['I','II','III','IV','V']:
    path=R/f'parts/{paper}.body.linked.tex';s=path.read_text()
    pat=re.compile(r'% BEGIN CORRECTION_DEPENDENCY_SCOPE ([^\n]+)\n(.*?)% END CORRECTION_DEPENDENCY_SCOPE \1',re.S)
    def replace(m):
        refs=list(dict.fromkeys(re.findall(r'\\cref\{(iv:correction:[^}]+)\}',m.group(2))))
        assert refs,m.group(1)
        new='\\par\\noindent\\textit{Dependency scope.} We use '+', '.join('\\cref{'+lab+'}' for lab in refs)+' only at their stated retained-construction or corrected-conclusion scopes.\n'
        records.append({'id':'scope:'+m.group(1),'paper':paper,'old':m.group(0),'new':new,'reason':'Keep the corrected mathematical dependency scope in place; retain the former receiving-locator history in this receipt.'})
        return new
    s=pat.sub(replace,s);path.write_text(s)

csv.field_size_limit(10**9);path=R/'S6_SERIES_GRIND_inventory.csv'
with path.open() as f:rows=list(csv.DictReader(f));fields=list(rows[0])
found=0
for row in rows:
    if row['label']=='night:P3K.119':row['status']='proved';found+=1
assert found==1
with path.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
(R/'analysis/K119_and_scope_prose_changes.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'changes':len(records),'status':'K119 proved'}))
