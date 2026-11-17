"""Replace a vague unopened book citation by opened exact toric/GAGA statements."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[2];p=D/'editorial/II_working_supplement.tex';s=p.read_text()
old=r'''gives $c_1(\eta^*A_L)=0$.  The surface $\mathrm{dP}_6$ is the blow-up of
$\mathbb P^2$ at three noncollinear points; the standard blow-up calculation
gives $H^1(\mathrm{dP}_6,\mathcal O)=0$
\cite[Chapter~V]{Hartshorne1977}.  In the exponential sequence, the kernel'''
new=r'''gives $c_1(\eta^*A_L)=0$. The surface $\mathrm{dP}_6$ is the blow-up of
$\mathbb P^2$ at three noncollinear points. A projective change of coordinates
moves these points to the three coordinate points, so this is the smooth
complete toric surface obtained by subdividing the three two-dimensional
cones of the fan of $\mathbb P^2$. Its fan has support $\mathbb R^2$,
and the zero Cartier divisor is nef. Demazure vanishing therefore gives
$H^1(\mathrm{dP}_6,\mathcal O)=0$ in algebraic cohomology
\cite[Theorem~9.2.3, author preprint p.~410]{CoxLittleSchenck2011}.
Since this surface is projective and $\mathcal O$ is coherent,
Serre's comparison theorem identifies that group with analytic cohomology
\cite[\S12, Theorem~1, p.~19]{Serre1956GAGA}.
In the exponential sequence, the kernel'''
assert old in s;s=s.replace(old,new);p.write_text(s)
p=D/'work/root/references_verified.json';rows=json.loads(p.read_text())
for r in rows:
 if r.get('keys')==['CoxLittleSchenck2011']:
  r['locator']+='; Theorem9.2.3, p410'
  r['verification']+=' Demazure vanishing theorem and its proof opened in full: convex support and nef Q-Cartier divisor. For dP6 the fan is complete and D=0, so algebraic H1(O)=0. Web ref turn262view0.'
rows.append({'keys':['Serre1956GAGA'],'status':'verified in the specified scope','source':'https://www.numdam.org/article/AIF_1956__6__1_0.pdf','locator':'Section12, Theorem1, printed p19; projective hypothesis immediately preceding; complete proof in section13 pp20–22 also opened','verification':'Original article opened. Coherent algebraic sheaf on a complex projective variety has canonical cohomology comparison isomorphisms in all degrees. Applied only to the structure sheaf of the projective smooth toric surface dP6, to transport the opened Demazure vanishing. Not used for a nonprojective compact complex space. Web refs turn266view0,turn267view0 and exact section12 opening.','reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November2026'})
p.write_text(json.dumps(rows,indent=2)+'\n')
p=D/'records/II_working_citation_normalizations.json';obj=json.loads(p.read_text());obj['replacements'].append({'source':'Hartshorne1977 ChapterV vague blow-up reference','state':'Original cited chapter notopened','action':'Replace with a full identification of dP6 as the complete toric blow-up, exact opened Demazure Theorem9.2.3 and Serre1956GAGA Section12 Theorem1. Algebraic-to-analytic comparison is explicit.'});p.write_text(json.dumps(obj,indent=2)+'\n')
print('Completed dP6 H1 vanishing source comparison')
