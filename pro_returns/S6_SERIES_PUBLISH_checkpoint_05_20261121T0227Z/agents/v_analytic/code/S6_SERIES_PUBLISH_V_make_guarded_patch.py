"""Create guarded analytic-integration replacements; never edit main source."""
from pathlib import Path
import json, hashlib

base=Path(__file__).resolve().parent.parent
source=base.parents[1]/'S6_SERIES_PUBLISH_V.tex'
original=source.read_text()
current=original
items=[]
def add(location,old,new,reason,kind='D08'):
 global current
 count=current.count(old)
 if count!=1:
  raise ValueError((location,'expected exactly one sequential match',count))
 items.append({'type':kind,'location':location,'old_text':old,'new_text':new,
               'expected_count':1,'reason':reason,
               'old_pdf_page':'root to fill from corrected baseline',
               'new_pdf_page':'root to fill after final pagination'})
 current=current.replace(old,new,1)

draft=(base/'S6_SERIES_PUBLISH_V_filling_parameter_patch.tex').read_text()
remark_start=draft.index('\\begin{remark}')
remark_end=draft.index('\\end{remark}',remark_start)+len('\\end{remark}')
new_remark=draft[remark_start:remark_end]
old_start=current.index('\\begin{remark}[The parameter under base and fibre conjugation]')
old_end=current.index('\\end{remark}',old_start)+len('\\end{remark}')
add('rem:V:conjugation-parameter (old position)',current[old_start:old_end],'',
    'Move the exact parameter comparison before the construction that uses it.','D07')
header='\\begin{theorem}[compact holomorphic filling]\\hypertarget{tag-02O9}{}\\label{maps:src:F.3.7}\\hypertarget{tag-02QJ}{}\\label{night:P1.10}'
add('rem:V:conjugation-parameter (new position)',header,new_remark+'\n\n'+header,
    'Prove the based conjugation matrix and exact parameter map before applying them.','D07')

start=current.index('\\item We first fix the dual convention.')
end=current.index('Put $M_1=A^t$',start)
dstart=draft.index('\\item We fix the dual convention together with the parameter.')
dend=draft.index('\n% In the remaining part',dstart)
add('maps:src:F.3.7 proof item 1',current[start:end],draft[dstart:dend].rstrip()+'\n',
    'Use raw parameter -conjugate(xi) in the actual construction, making the resulting family holomorphic in xi.')

start=current.index('In the real-normalized cusp coordinate,',current.index(header))
end=current.index('$(I_3,sI_3-C^\\kappa(q))$.',start)+len('$(I_3,sI_3-C^\\kappa(q))$.')
dstart=draft.index('In the real-normalized cusp coordinate,')
dend=draft.index('\n% In item 5',dstart)
add('maps:src:F.3.7 proof item 1 cusp formula',current[start:end],draft[dstart:dend].strip(),
    'Track the same parameter through the bounded cusp correction.')

old=r'''\[
 q=\bar q_o,\qquad x=(\bar x_o)^{-1},\qquad
 \nu=-\nu_o,
 \qquad C_{\rm new}(q)=-C^\kappa(q).
\]'''
new=r'''\[
 q=\bar q_o,\qquad x=(\bar x_o)^{-1},\qquad
 \nu=-\nu_o,\qquad
 C_{{\rm new},\xi}(q)=-C^\kappa_\xi(q).
\]'''
add('maps:src:F.3.7 proof item 5 multiplicative comparison',old,new,
    'Keep the exact parameter map in the multiplicative action and fan comparison.')
add('maps:src:F.3.7 proof item 5 action',
    '$x\\mapsto\\exp(2\\pi iC_{\\rm new}(q)\\nu)q^\\nu x$.',
    '$x\\mapsto\\exp(2\\pi iC_{{\\rm new},\\xi}(q)\\nu)q^\\nu x$.',
    'Use the same indexed correction in the resulting action.')

old='is the gluing of \\cref{pub:V:smooth-gluing}. Its fundamental group is trivial and its Euler number is six by that lemma.'
dstart=draft.index('The finite actions and all gluing maps are holomorphic in $\\xi$.')
addition=draft[dstart:].strip()
add('maps:src:F.3.7 proof conclusion',old,old+'\n\n'+addition,
    'Explain joint holomorphic dependence and uniform local cusp radius in the family parameter.')

old=r'''For every transverse period parameter of \cref{night:P1.8}, the
marked gluing of \cref{pub:V:smooth-gluing} has a compact smooth
complex realization and a proper holomorphic map to $\mathbb P^1$.'''
new=r'''In the notation of \cref{pub:V:parameter}, for every $\xi\in\mathcal U$
the marked gluing of \cref{pub:V:smooth-gluing} has a compact smooth
complex realization $M_\xi$ and a proper holomorphic map to $\mathbb P^1$.
This includes the subfamily $M_c$, $c>c_*$.'''
add('maps:src:F.3.7 statement',old,new,
    'Use the single global parameter notation declared in the introduction.')

old=r'\StatementRecord{night:P1.15}{proved}{02QO}{\SeriesRef{night:P1.1}, \SeriesRef{night:P1.8}}'
new=r'\StatementRecord{night:P1.15}{proved}{02QO}{\SeriesRef{night:P1.1}, \SeriesRef{night:P1.2}, \SeriesRef{night:P1.5}, \SeriesRef{night:P1.7}}'
add('night:P1.15 dependency record',old,new,
    'Remove the obsolete dependency on the later lift theorem; retain the monodromy, quotient, bundle and marking inputs.')

old=r'''1.094540250311402780116268263054945703725<c_*
 <1.094540250311402780116268263054945703726.'''
new=r'''\begin{aligned}
1.094540250311402780116268263054945703725&<c_*,\\
c_*&<1.094540250311402780116268263054945703726.
\end{aligned}'''
add('night:P1.18 exact interval',old,new,
    'Split the unchanged exact interval over two aligned lines to remove overflow.','D10')

out=base/'S6_SERIES_PUBLISH_V_analytic_guarded_replacements.json'
out.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
receipt={'source':str(source),'source_sha256':hashlib.sha256(original.encode()).hexdigest(),
         'sequential_replacements':len(items),'all_expected_counts':1,
         'main_source_written':False,
         'PV01_owner':'v_topology_check: n=2,3 plus uniform shrinking',
         'root_owned_prerequisite':'pub:V:parameter / PV14 notation definition'}
(base/'S6_SERIES_PUBLISH_V_analytic_guarded_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
