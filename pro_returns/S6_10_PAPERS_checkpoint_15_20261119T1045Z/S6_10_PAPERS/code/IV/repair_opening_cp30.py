from pathlib import Path
import re,json,hashlib
w=Path('/workspace/scratch/490d8ca4e928/work/S6_10_PAPERS')
updates={
'The selected-infinity E6 return and its fourteen fan values':r'''\RungZero{For the original $M_6$ family with its quadratic norm-one
cap, fixed scalar, retained finite character and original selected
height, the actual normal and moving-cap comparison gives physical
pair $(-4,8)$ and class $27$ for the positive $\epsilon=w^{-1}$
loop on the initial fan. Its full native fan arrows transport those
integers and give precisely the fourteen odd residues modulo $28$.}
''',
'Every reduced and good cap at selected infinity':r'''\RungZero{The proper relative cap products and their matched boundary
connections preserve the two integers $\int x^3$ and $\int p_1x$
separately for both complete progressions: $M_6$, translation by
$-G$, $m=3l+2$, $l\geq0$, and $M_2$, translation by $-3G$,
$m=3l$, $l\geq1$. They retain both primitive norm signs, every
admitted finite character, the full annular reference, each cap and
reference's common strict scalar range, and every selected basis
fan, carrying the initial pair $(-4,8)$ and the entire fourteen-odd-residue
fan image through the actual comparison maps.}
''',
'The selected-I3 source loop and all twenty-eight classes':r'''\RungZero{For the original E6 point line
$M_6=\mathcal O([6G]-[O])$, translation by $-G$, the quadratic
cap $(m,n)=(2,1)$, its prescribed finite character and full annular
reference, the compact fixed-stratum and moving-cap comparison
fixes the selected-I3 source loop's physical pair $(47,-4)$ and
initial class eight. The actual native fan arrows transport those
integers, and the complete witness words of at most seven flops
from the initial fan realize all of $\mathbb Z/28$.}
''',
'The complete $M_2$ order-three return':r'''\RungZero{For $M_2=\mathcal O([2G]-[O])$ and the three
chronological translations by $-G$, the full point-to-theta map
and compact-versus-reference cancellation give initial and vertical
physical pair $(-3,-12)$ for every good cap $m=3l$, $l\geq1$,
either primitive norm sign, each admitted finite character and full
annular reference, with the fixed scalar in the chosen cap and
reference's common strict contraction range. The actual directed
prism identities then give every selected basis fan the integer
\[
 A(P)=-\frac38(S-1)(S-3),\qquad
 S=x^2+xy+y^2,\quad (x,y)^t=P^{-1}e_2,
\]
whose exact image modulo $28$ has sixteen elements.}
'''
}
records=[]
for name in ['opening.tex','opening_cp29.tex']:
 p=w/'papers/IV'/name;s=p.read_text();old=s
 for title,new in updates.items():
  token='\\subsection{'+title+'}'
  if token not in s:continue
  a=s.index(r'\RungZero{',s.index(token));b=s.index(r'\RungOne',a)
  before=s[a:b];s=s[:a]+new+s[b:]
  records.append({'file':str(p.relative_to(w)),'title':title,'old':before,'new':new,'operation':'Add the exact geometric mechanism while retaining the stated choices and result; one or two sentences.'})
 olditem=r'\item The literal marked-source reflection carries the branch'
 assert s.count(olditem)==1,(name,s.count(olditem))
 s=s.replace(olditem,'  The literal marked-source reflection carries the branch',1)
 s=s.replace(r'\cref{iv:i3_all_reduced_caps}',r'\cref{night:P3K.108}')
 p.write_text(s)
 records.append({'file':str(p.relative_to(w)),'operation':'Merge the complete marked-reflection paragraph into native-fan step seven; no content removed.','sha256':hashlib.sha256(s.encode()).hexdigest()})
p=w/'papers/IV/opening_icap.tex';s=p.read_text().replace(r'\cref{iv:i3_all_reduced_caps}',r'\cref{night:P3K.108}');p.write_text(s)
(w/'analysis/IV/opening_cp30_revisions.json').write_text(json.dumps(records,indent=2)+'\n')
for p in [w/'papers/IV/opening.tex',w/'papers/IV/opening_cp29.tex']:
 text=p.read_text();a=text.index('\\subsection{The selected-I3');a=text.index('\\begin{enumerate}',a);b=text.index('\\end{enumerate}',a);print(p.name,'K106 steps',text[a:b].count('\\item'))
