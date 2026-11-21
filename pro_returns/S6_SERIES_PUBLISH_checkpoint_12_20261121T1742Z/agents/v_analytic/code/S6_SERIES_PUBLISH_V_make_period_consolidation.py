"""Prepare, check and map the P1.16/P1.18 consolidation without editing V."""
from pathlib import Path
from fractions import Fraction
import json,re,hashlib

base=Path(__file__).resolve().parent.parent
source=base.parents[1]/'S6_SERIES_PUBLISH_V.tex'
original=source.read_text(); current=original; items=[]
def add(location,old,new,reason,kind='D07'):
 global current
 assert current.count(old)==1,(location,current.count(old))
 items.append(dict(type=kind,location=location,old_text=old,new_text=new,
                   expected_count=1,reason=reason,
                   old_pdf_page='baseline P1.16 pp.52-55; root to confirm',
                   new_pdf_page='root to fill after final pagination'))
 current=current.replace(old,new,1)

start=current.index('\\begin{theorem}[Certified values of $h_b$]')
end=current.index('\\end{proof}',start)+len('\\end{proof}')
old=current[start:end]
(base/'S6_SERIES_PUBLISH_V_P1_16_before.tex').write_text(old+'\n')
add('night:P1.16 old position',old,'',
    'Place the endpoint result after the common whole-base enclosure argument; preserve its complete earlier computation in the check record.')
oldtail=r''' e^{MR}\frac{(r/R)^{N+1}}{1-r/R}.
\]'''
newtail=r''' e^{MR}\frac{(r/R)^{N+1}}{1-r/R}.
 \tag{1.16.1}
\]'''
add('night:P1.18 common Taylor tail anchor',oldtail,newtail,
    'Preserve the original Taylor-tail tag at the single remaining statement of the bound.')
add('night:P1.18 intertwiner dependency',
    'The unique common intertwiner fixing $e_0$ is $X$, by\n\\cref{night:P1.15}.',
    'The unique common intertwiner fixing $e_0$ is $X$, by\n\\cref{night:P1.15,def:hb}.',
    'Point to the explicit based-meridian uniqueness proof as well as existence of the normalized comparison.','D08')
ending=r'''The strict central Hessian inequality, the four outer bounds and
the inner cusp inequality prove that infinity is the unique
minimum. The exact domain now follows from
\cref{night:P1.8}.
\hypertarget{tag-03L1}{}\label{layout:V:fresh-splitting}
\end{proof}'''
new=(base/'S6_SERIES_PUBLISH_V_P1_16_consolidated.tex').read_text().strip()
add('night:P1.16 new position',ending,ending+'\n\n'+new,
    'Reuse the certified root enclosure for h_b(1), retaining the exact gauge comparison, zero endpoint and excluded parameter.')

certificate=base/'code/period_certificate_rerun/output/fresh_frobenius.json'
data=json.loads(certificate.read_text())
ball=data['h_b']['one']
m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',ball)
center,rad=map(Fraction,m.groups())
display=Fraction('-1.03427662241632179949424884537834605259496477790218821132')
display_rad=Fraction('8.11e-57')
lo=Fraction('-1.0342766224163217994942488453783461')
hi=Fraction('-1.0342766224163217994942488453783460')
assert rad<Fraction('7e-76')
assert abs(center-display)+rad<display_rad
assert lo<center-rad and center+rad<hi
assert current.count('\\label{night:P1.16}')==1
assert current.count('\\hypertarget{tag-02QP}')==1
assert current.count('\\tag{1.16.1}')==1
assert current.index('\\label{night:P1.18}')<current.index('\\label{night:P1.16}')
(base/'S6_SERIES_PUBLISH_V_period_guarded_replacements.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
receipt={'source_sha256':hashlib.sha256(original.encode()).hexdigest(),
         'sequential_replacements':len(items),'main_source_written':False,
         'P1.16_label_and_tag_preserved':True,'Taylor_tail_tag_preserved_once':True,
         'P1.18_precedes_P1.16':True,
         'point_enclosure_independent_of_loop_method':True,
         'point_enclosure_source':str(certificate),
         'exact_rational_containment_checks':True}
(base/'S6_SERIES_PUBLISH_V_period_consolidation_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
