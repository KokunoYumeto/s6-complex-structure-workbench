"""Replace bounded known inputs by their opened-source specializations."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
p=R/'parts/IV.body.linked.tex';t=p.read_text();records=[]
at=t.index('\\label{night:P3F.3}')
a=t.index('\\begin{proof}',at);b=t.index('\\end{proof}',a)+len('\\end{proof}')
old=t[a:b];new=(R/'audit_corrections/IV_F3_cited_proof.tex').read_text().strip()
new=new.replace('where $A=(4k-\\ell)/24$.',r'''Here the source's preferred spin mapping torus and characteristic numbers are
\[
 M_f=M\times[0,1]/((z,0)\sim(f(z),1)),\qquad
 k=\langle x^3,[M_f]\rangle,\quad
 \ell=\langle p_1(TM_f)x,[M_f]\rangle,
\]
with $x$ restricting to the positive $S^2$ generator, and
$A=(4k-\ell)/24$.''')
t=t[:a]+new+t[b:]
records.append({'label':'night:P3F.3','old':old,'new':new,'reason':'Cite the opened Torelli classification and retain only the explicit coordinate inverse and source convention.'})
at=t.index('\\label{night:P3F.7}');a=t.index('\\item On an ordinary fibre',at);b=t.index('\\item For the vertical wall',a)
old=t[a:b];new=(R/'audit_corrections/IV_F7_known_input.tex').read_text().strip()+'\n\n'
t=t[:a]+new+t[b:]
records.append({'label':'night:P3F.7','old':old,'new':new,'reason':'Cite the known reference fixed-locus calculation; retain every subsequent actual conifold, Hopf, orbit, framing and line map.'})
p.write_text(t)
(R/'analysis/IV_known_input_changes_03.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'changes':len(records),'characters_removed':sum(len(r['old'])-len(r['new']) for r in records)}))
