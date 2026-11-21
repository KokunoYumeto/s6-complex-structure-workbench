"""Current-source guards for regular-root limits and analytic dependencies."""
from pathlib import Path
import json,hashlib,re
base=Path(__file__).resolve().parent.parent
source=base.parents[1]/'S6_SERIES_PUBLISH_V.tex'
original=source.read_text();current=original;items=[]
def add(location,old,new,reason):
 global current
 assert current.count(old)==1,(location,current.count(old))
 items.append(dict(type='D08',location=location,old_text=old,new_text=new,
   expected_count=1,reason=reason,old_pdf_page='root to fill',new_pdf_page='root to fill'))
 current=current.replace(old,new,1)
def record(sid,deps,reason):
 old=next(x for x in current.splitlines() if x.startswith('\\StatementRecord{'+sid+'}'))
 prefix=re.match(r'(\\StatementRecord\{[^}]*\}\{[^}]*\}\{[^}]*\})',old).group(1)
 add(sid+' dependency record',old,prefix+'{'+deps+'}',reason)

record('maps:src:F.3.7',
 r'\cref{night:P1.8,night:P1.9,pub:V:rank-six-data,pub:V:smooth-gluing,pub:V:cusp-smooth-dependence,rem:V:conjugation-parameter}',
 'Use the actual preceding period, local filling, marked gluing and conjugation inputs; remove obsolete later integral-homology and fibre-product dependencies.')
record('night:P1.8',r'\cref{night:P1.5,night:P1.15,def:hb}',
 'Record the well-defined normalized real intersection used by the transversality proof.')
record('night:P1.18',r'\cref{night:P1.15,def:hb,night:P1.8,rem:V:conjugation-parameter}',
 'Record the exact normalized real system and proved conjugation used in the certificate cover.')

old=r'''\cref{night:P1.15,def:hb}. Hence the regular limiting frames are
$F_0=XU_0(1)^{-1}$ and $F_\infty=XU_\infty(1)^{-1}$.'''
new=r'''\cref{night:P1.15,def:hb}. In these gauges the exact identities are
\[
 H(u^4)D_0(u)=U_0(1)^{-1}U_0(u),\qquad
 H(u^{-5})D_\infty(u)=U_\infty(1)^{-1}U_\infty(u).
\]
Thus the regular infinity limit in the statement means precisely
\[
 H_\infty=\lim_{u\to0}H(u^{-5})D_\infty(u)
             =U_\infty(1)^{-1}.
\]
The regular limiting frames are consequently
$F_0=XU_0(1)^{-1}$ and $F_\infty=XU_\infty(1)^{-1}$.'''
add('night:P1.18 regularized limits',old,new,
 'Define the exact gauge-regularized limit; the original meromorphic columns are not assigned an ordinary matrix limit.')
old=r'''At infinity the deck action sends the normalized coefficient
pair to $(\zeta^8v_2,\zeta^4v_1)$, with
$\zeta=e^{2\pi i/5}$. Its value at the root point is therefore
zero.'''
new=r'''At infinity use the regular frame
$Y(u^{-5})D_\infty(u)=F_\infty U_\infty(u)$.
The normalized vector in that frame is $D_\infty(u)^{-1}q$;
its two variable coefficients are
$\widetilde v_2=u^8v_2$ and $\widetilde v_1=u^4v_1$.
The deck action sends this pair to
$(\zeta^8\widetilde v_2,\zeta^4\widetilde v_1)$,
where $\zeta=e^{2\pi i/5}$. Its value at the root point
is therefore zero.'''
add('night:P1.18 root coefficient map',old,new,
 'Distinguish the regular-frame coefficient pair from the meromorphic-frame pair by its exact diagonal map.')
old=r'''This proves the two strict bounds. At zero the nontrivial deck
characters likewise force the normalized coefficients
$v_2,v_1$ to vanish. With the regular limiting frame $F_0$'''
new=r'''This proves the two strict bounds. At zero the normalized vector
in the regular frame is $D_0(u)^{-1}q$; its variable coefficients
are $u^{-6}v_2,u^{-3}v_1$. The nontrivial deck characters
force their limiting values to vanish. With the regular limiting frame $F_0$'''
add('night:P1.16 root coefficient map',old,new,
 'Use the exact zero-root gauge when evaluating the normalized intersection at the endpoint.')

record('night:P1A.2',r'\cref{night:P1.15,night:P1A.1,night:P1.18}',
 'The proof uses the certified parameter threshold to exclude its exceptional residue determinant.')
record('night:P1.17',r'\cref{night:P1.1,night:P1A.4,night:P1.9}',
 'The proof uses intrinsic base-map rigidity and the prescribed cusp fan in addition to integral monodromy.')
old=next(x for x in current.splitlines() if x.startswith('\\StatementRecord{night:P1A.5}'))
new=old.replace(r'\cref{night:P2.4}, ', '').replace(
 r'\cref{night:P1.8};',r'\cref{night:P1.8}, \cref{night:P1.18}, \cref{rem:V:conjugation-parameter};')
assert new!=old
add('night:P1A.5 dependency record',old,new,
 'Remove the unused shifted-fivefold theorem and record the actual normalized minimum and marking comparison used in the boundary proof.')

(base/'S6_SERIES_PUBLISH_V_tiny_guarded_replacements.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
receipt={'source_sha256':hashlib.sha256(original.encode()).hexdigest(),
 'sequential_replacements':len(items),'all_expected_counts':1,'main_source_written':False}
(base/'S6_SERIES_PUBLISH_V_tiny_guarded_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
